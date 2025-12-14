from sqlalchemy import Integer, Text
from sqlalchemy.orm import Mapped, mapped_column
from helpers.database.database import db


class CBOEntidade(db.Model):
    __tablename__ = "tb_CBOEntidade"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    codigo: Mapped[int] = mapped_column(Integer, nullable=False)
    titulo: Mapped[str] = mapped_column(Text, nullable=False, index=True)
