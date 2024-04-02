from flask import Flask,Blueprint, render_template,request
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sports import db
from sports.models import plan, player,Cheer

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    return render_template('/main.html')


@bp.route('/video')
def index2():
    return render_template('/video.html')


@bp.route('/cheer', methods=['GET','POST'])
def cheer():
    cheer_list = Cheer.query.order_by(Cheer.cheer_id)
    if request.method == 'GET':
        return render_template('/cheer.html',cheer_list=cheer_list)
    elif request.method == 'POST':
        content = request.form.to_dict()
        print(content)
        for key,value in content.items():
            print(value)
            cheer = Cheer(date=datetime.now(), content=value)
            db.session.add(cheer)
        db.session.commit()
        print('커밋완료')
        return render_template('/cheer.html',cheer_list=cheer_list)


    

# 경기 일정 데이터
def get_game_schedule():
    # 경기 일정 데이터를 데이터베이스에서 가져옴
    schedule = plan.query.all()
    return schedule

@bp.route('/schedule')
def index4():
    # 템플릿에 경기 일정 데이터 전달
    beverage_list = plan.query.order_by(plan.date2)
    return render_template('schedule.html', schedule=beverage_list)

@bp.route('/result')
def index5():
    players = player.query.order_by(player.date)
    return render_template('result.html', players=players)

