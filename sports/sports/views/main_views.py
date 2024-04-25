from flask import Flask,Blueprint, render_template,request
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sports import db
from sports.models import plan, player,Cheer
from flask import current_app



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
def show_schedule():
    try:
        events = plan.query.all()
        current_app.logger.info(f"Fetched {len(events)} events")
    except Exception as e:
        current_app.logger.error("Failed to fetch events", exc_info=True)
        events = []
    return render_template('schedule.html', schedule=events)



@bp.route('/result')
def index5():
    players = player.query.all()
    return render_template('result.html', players=players)

