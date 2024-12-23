import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)


class Ticket(Base):
    __tablename__ = "tickets"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)
    capacity = sa.Column(sa.Integer)


class UsersTicketsPurchase(Base):
    __tablename__ = "users_tickets_purchase"

    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey("users.id"))
    ticket_id = sa.Column(sa.Integer, sa.ForeignKey("tickets.id"))
