from flask import Flask 
import config
# from exts import db 
# from models import UserModel
from blueprints.qa import bp  as qa_bp
from blueprints.auth import bp  as auth_bp

app = Flask(__name__)
# 绑定配置文件
app.config.from_object(config)

# db.init_app(app)

app.register_blueprint(qa_bp)
app.register_blueprint(auth_bp)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
