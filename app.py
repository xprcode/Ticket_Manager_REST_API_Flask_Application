from flask import Flask
from werkzeug.security import generate_password_hash
from rest_api_application import app, db
from rest_api_application.models.user import User
from rest_api_application.models.events import Events 






@app.route('/')
def index():
    # new_user = User(name='Joe',
    #         password=generate_password_hash('newpassword'),
    #         email="xprtsw@o2.pl")

    # db.session.add(new_user)
    # db.session.commit()
    
    return 'ok'



if __name__ == "__main__":
    app.run()