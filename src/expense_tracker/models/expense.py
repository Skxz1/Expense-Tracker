from datetime import date, datetime  # date -> for expense_date, datetime -> for created_at

from sqlalchemy import Date, DateTime, Integer, String, func
from sqlalchemy.orm import (  # Mapped -> attribute mapped to column, mapped_column -> defines column in db
    Mapped,
    mapped_column,
)

from expense_tracker.db.base import Base  # Defines base class for all db models


class Expense(Base):
    __tablename__ = "expenses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    amount_pence: Mapped[int] = mapped_column(Integer)
    category: Mapped[str] = mapped_column(String)
    marchant: Mapped[str] = mapped_column(String)
    expense_date: Mapped[date] = mapped_column(Date)
    notes: Mapped[str | None] = mapped_column(String, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now()
    )  # server_default -> database sets teh timestamp automatically
