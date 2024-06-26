#!/usr/bin/env python3

from app import app
from models import db, Newsletter

if __name__ == '__main__':
    # Ensure the Flask app context is active
    with app.app_context():
        # Initialize the database within the app context
        db.init_app(app)
        
        # Create a new newsletter instance (example)
        newsletter = Newsletter(
            title="Latest News",
            content="This is the latest news update.",
            sent=True  # Example attribute
        )

        # Add the newsletter to the session and commit to the database
        db.session.add(newsletter)
        db.session.commit()

        # Debugging point to interactively inspect the state
        import ipdb; ipdb.set_trace()

        # You can perform further operations or test functionalities interactively
