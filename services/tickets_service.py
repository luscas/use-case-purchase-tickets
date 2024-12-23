from db.models import Ticket, UsersTicketsPurchase
from sqlalchemy.orm import Session


def buy_ticket(session: Session, ticket_id, user_id):
    session.begin()

    try:
        ticket = session.query(Ticket).filter_by(id=ticket_id).first()
        if not ticket or ticket.capacity <= 0:
            print("Ticket not available")
            return {"error": "Ticket not available"}

        ticket.capacity -= 1

        purchase = UsersTicketsPurchase(user_id=user_id, ticket_id=ticket_id)

        session.add(ticket)
        session.add(purchase)

        print("Success!")

        session.commit()
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")
        return {"error": str(e)}
    finally:
        session.close()
