from flask import Blueprint,render_template
# 蓝图的名字为"auth"，而使用该蓝图的视图函数均需要使用"/auth"作为前缀
bp = Blueprint("auth",__name__,url_prefix="/auth")

@bp.route("/login")
def login():
    pass

@bp.route("/register")
def register():
    return render_template("register.html")