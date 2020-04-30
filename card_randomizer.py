from app import app, db
from app.models import Pass, User, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'pass':Pass, 'User': User, 'Post': Post}