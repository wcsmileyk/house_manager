import os
from app import create_app, db


app = create_app(os.getenv('FLASK_ENV') or 'default')


@app.shell_context_processor
def make_shell_context():
    return dict(db=db)
