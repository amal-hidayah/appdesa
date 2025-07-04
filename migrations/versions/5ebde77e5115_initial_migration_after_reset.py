"""Initial migration after reset

Revision ID: 5ebde77e5115
Revises: 
Create Date: 2025-06-28 17:36:54.762157

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ebde77e5115'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('berita',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('judul', sa.String(length=200), nullable=False),
    sa.Column('isi_berita', sa.Text(), nullable=False),
    sa.Column('url_gambar_utama', sa.String(length=255), nullable=True),
    sa.Column('tanggal_publikasi', sa.DateTime(), nullable=True),
    sa.Column('penulis', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password_hash', sa.String(length=255), nullable=True),
    sa.Column('role', sa.String(length=20), nullable=False),
    sa.Column('tanggal_daftar', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('apb_des',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tahun', sa.Integer(), nullable=False),
    sa.Column('judul', sa.String(length=200), nullable=False),
    sa.Column('deskripsi', sa.Text(), nullable=True),
    sa.Column('url_file_apbdes', sa.String(length=255), nullable=True),
    sa.Column('tanggal_unggah', sa.DateTime(), nullable=True),
    sa.Column('pengunggah_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['pengunggah_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pengaduan',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('judul', sa.String(length=100), nullable=False),
    sa.Column('deskripsi', sa.Text(), nullable=False),
    sa.Column('lokasi', sa.String(length=200), nullable=True),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.Column('url_bukti_media', sa.String(length=255), nullable=True),
    sa.Column('status', sa.String(length=20), nullable=False),
    sa.Column('tanggal_pengaduan', sa.DateTime(), nullable=True),
    sa.Column('tanggal_update_status', sa.DateTime(), nullable=True),
    sa.Column('respon_admin', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pengaduan')
    op.drop_table('apb_des')
    op.drop_table('user')
    op.drop_table('berita')
    # ### end Alembic commands ###
