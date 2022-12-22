from flask import Flask, render_template, g, session, request
#import pyodbc
#from flask_sqlalchemy import SQLAlchemy
import urllib
#from sqlalchemy import create_engine

from gamestatsModels import db, Game_User, Owned_Games, Achievements, Game_Wishlist, Game_Tags, Per_Genre_Statistics, Per_Game_Statistics, Singleplayer_Game_Statistics, Multiplayer_Game_Statistics, Co_op_Game_Statistics, Overall_Gaming_Statistics, Game_Client, Vendor_Platform, Game_Company, Games
from ml_alg import calculate_nearest_centroid
"""
server = 'EVO\SQLEXPRESS' # to specify an alternate port
database = 'Game_Project_DBClass' 
username = 'EVO\Tom' 
password = ''

#print("connecting.......")
#cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
#cursor = cnxn.cursor()
#print("connected!")

"""
#db = SQLAlchemy()

app = Flask(__name__)

print("Connecting...")

#app.config["SQLALCHEMY_DATABASE_URI"] = 'mssql+pyodbc:///?odbc_connect=DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password+';'

params = urllib.parse.quote_plus('DRIVER={SQL Server};SERVER=EVO\SQLEXPRESS;DATABASE=Game_Project_DBClass;Trusted_Connection=yes;')

app.config["SQLALCHEMY_DATABASE_URI"] = "mssql+pyodbc:///?odbc_connect=%s" % params

db.init_app(app)

print("Connected!")

@app.route("/", methods=['GET', 'POST'])
def main_page():
    """
    try:
        #cursor.execute('SELECT * FROM Game_Project_DBClass.dbo.Achievements')
        #user = db.session.execute(db.select(Game_User)).first()
        user = Game_User.query.filter_by(User_ID=1).all()
        print(user)
        print(user[0].User_ID)
        game = Owned_Games.query.filter_by(User_ID=1).all()
        print(game[0])
        print(game[1])
        achievement = Achievements.query.filter_by(Game_ID=100).all()
        print(achievement[0])
        return '<h1>It works.</h1> <p>Hello, World!</p>'
    except:
        return '<h1>Something is broken.</h1> <p>Hello, World!</p>'
    """
    user = None
    owned_games = None
    achievements = []
    game_wishlist = None
    game_tags = None
    per_genre_stats = None
    sing_game_stats = None
    multi_game_stats = None
    coop_game_stats = None
    overall_game_stats = None
    game_clients = None
    if request.method == 'POST':
        req_id = request.form['User_ID']
        users = Game_User.query.filter_by(User_ID=request.form['User_ID']).all()
        user = users[0]
        owned_games = Owned_Games.query.filter_by(User_ID=req_id).all()
        for o in owned_games:
            achievement_list = Achievements.query.filter_by(Game_ID=o.Game_ID).all()
            achievements.append(achievement_list[0])
        game_wishlist = Game_Wishlist.query.filter_by(User_ID=req_id).all()
        game_tags = Game_Tags.query.filter_by(User_ID=req_id).all()
        per_genre_stats = Per_Genre_Statistics.query.filter_by(User_ID=req_id).all()
        per_game_stats = Per_Game_Statistics.query.filter_by(User_ID=req_id).all()
        list_of_games = []
        for p in per_game_stats:
            list_of_games.append(p.Stat_ID)
        list_of_games.sort()
        sing_game_stats = Singleplayer_Game_Statistics.query.filter_by(Stat_ID=list_of_games[0]).all()
        multi_game_stats = Multiplayer_Game_Statistics.query.filter_by(Stat_ID=list_of_games[1]).all()
        coop_game_stats = Co_op_Game_Statistics.query.filter_by(Stat_ID=list_of_games[2]).all()
        overall_game_stats = Overall_Gaming_Statistics.query.filter_by(User_ID=req_id).all()
        game_clients = Game_Client.query.filter_by(User_ID=req_id).all()
        g.showData = True
    return render_template('main_page.html', user=user, owned_games=owned_games, achievements=achievements, game_wishlist=game_wishlist, game_tags=game_tags, per_genre_stats=per_genre_stats, sing_game_stats=sing_game_stats, multi_game_stats=multi_game_stats, coop_game_stats=coop_game_stats, overall_game_stats=overall_game_stats, game_clients=game_clients)

@app.route("/game_recommender", methods=['GET', 'POST'])
def ml_page():
    result = 0
    if request.method == 'POST':
        review_rating = request.form['Review_Rating']
        review_count = request.form['Review_Count']
        player_count = request.form['Player_Count']
        result = calculate_nearest_centroid(review_rating, review_count, player_count)
        g.showResult = True
    return render_template('ml_page.html', result=result)
    
if __name__ == '__main__':
    app.run()