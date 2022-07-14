from datetime import datetime
from chatbot import db


class Members(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    userid = db.Column(db.String(20, 'utf8mb4_unicode_ci'), nullable=False)
    userpw = db.Column(db.String(20, 'utf8mb4_unicode_ci'), nullable=False)
    name = db.Column(db.String(20, 'utf8mb4_unicode_ci'), nullable=False)
    email = db.Column(db.String(20, 'utf8mb4_unicode_ci'), nullable=False)
    phone = db.Column(db.String(20, 'utf8mb4_unicode_ci'), nullable=False)
    start = db.Column(db.DateTime, default=datetime.utcnow())
