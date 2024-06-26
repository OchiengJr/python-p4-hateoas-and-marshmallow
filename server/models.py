from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Newsletter(db.Model):
    __tablename__ = 'newsletters'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text)
    published_at = db.Column(db.DateTime, server_default=db.func.now())
    edited_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Example relationship, replace with actual relationship as needed
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # user = db.relationship('User', backref='newsletters')

    # Example index for title
    # db.Index('idx_title', 'title')

    def __repr__(self):
        return f'<Newsletter {self.title}, published at {self.published_at}.>'

    def publish(self):
        """Publish the newsletter."""
        self.published_at = db.func.now()
        db.session.commit()
