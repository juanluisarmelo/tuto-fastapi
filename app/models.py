from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from .database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))


class AssetType(Base):
    __tablename__ = "asset_types"

    id = Column(Integer, primary_key=True, nullable=False)
    description = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True, nullable=False)
    description = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))


class Asset(Base):
    __tablename__ = "assets"

    id = Column(Integer, primary_key=True, nullable=False)
    model = Column(String, nullable=False)
    serial_number = Column(String, nullable=False)
    asset_tag = Column(String, nullable=True)
    name = Column(String, nullable=True)
    note = Column(String, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    asset_type_id = Column(Integer, ForeignKey(
        "asset_types.id", ondelete="CASCADE"), nullable=False)

    asset_type = relationship("AssetType")


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, nullable=False)
    gid = Column(Integer, nullable=False)
    user_id = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    role_id = Column(Integer, ForeignKey(
        "roles.id", ondelete="CASCADE"), nullable=False)
