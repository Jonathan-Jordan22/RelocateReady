"""add countries table and link locations

Revision ID: b153537b1d53
Revises: 83ff118177d7
Create Date: 2026-11-03 02:41:29.384372

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# Existing location labels → the country whose visa and currency rules apply
LABEL_TO_COUNTRY = {
    "Scotland": "United Kingdom",
    "England": "United Kingdom",
    "Ireland": "Ireland",
    "Netherlands": "Netherlands",
    "Australia": "Australia",
    "Canada": "Canada",
}


# revision identifiers, used by Alembic.
revision: str = 'b153537b1d53'
down_revision: Union[str, Sequence[str], None] = '83ff118177d7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    countries = op.create_table(
        "countries",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("code", sa.String(length=2), nullable=False),
        sa.Column("currency", sa.String(length=3), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
        sa.UniqueConstraint("code"),
    )

    op.bulk_insert(countries, [
        {"name": "United Kingdom", "code": "GB", "currency": "GBP"},
        {"name": "Ireland", "code": "IE", "currency": "EUR"},
        {"name": "Netherlands", "code": "NL", "currency": "EUR"},
        {"name": "Australia", "code": "AU", "currency": "AUD"},
        {"name": "Canada", "code": "CA", "currency": "CAD"},
    ])

    # 1. Add the column as nullable so existing rows are allowed to be empty
    op.add_column("locations", sa.Column("country_id", sa.Integer(), nullable=True))

    # 2. Backfill: point every existing location at its country
    conn = op.get_bind()
    for label, country in LABEL_TO_COUNTRY.items():
        conn.execute(
            sa.text(
                "UPDATE locations "
                "SET country_id = (SELECT id FROM countries WHERE name = :country) "
                "WHERE country = :label"
            ),
            {"country": country, "label": label},
        )

    # 3. Tighten: now every row has a value, so require one
    op.alter_column("locations", "country_id", nullable=False)
    op.create_foreign_key(
        "fk_locations_country_id", "locations", "countries", ["country_id"], ["id"]
    )


def downgrade() -> None:
    op.drop_constraint("fk_locations_country_id", "locations", type_="foreignkey")
    op.drop_column("locations", "country_id")
    op.drop_table("countries")