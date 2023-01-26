from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Message

ENGINE = create_engine('sqlite:///database.db?check_same_thread=False')
Base.metadata.create_all(ENGINE)
DBSession = sessionmaker(bind=ENGINE)
SESSION = DBSession()

def add_message(username, text):
    """Adds a message to the database.

    Args:
        username (str): 
        text (str): the text of the message.

    """
    # Create the Message object to store in the database
    message = Message(username=username, text=text)
    # Save it
    SESSION.add(message)
    SESSION.commit()

def get_all_messages():
    """Retrieves all messages.

    Returns:
        :obj:`list` of :obj:`Message`: list of all messages.

    """
    return reversed(SESSION.query(Message).all())

def delete_all_messages():
	num_rows_deleted = SESSION.query(Message).delete()
	print(num_rows_deleted)









