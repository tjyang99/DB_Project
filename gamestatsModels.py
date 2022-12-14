from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy.inspection import inspect

db = SQLAlchemy()
"""
class Serializer(object):

	def serialize(self):
		return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

	@staticmethod
	def serialize_list(l):
		return [m.serialize() for m in l]
"""


class Game_User(db.Model):
    __tablename__ = "Game_User"
    
    User_ID = db.Column(db.Integer, primary_key=True)
    First_Name = db.Column(db.String(20))
    Username = db.Column(db.String(20))
    Last_Name = db.Column(db.String(20))
    Date_of_Birth = db.Column(db.DateTime)
    Email = db.Column(db.String(20))
    Phone_Number = db.Column(db.String(20))
    Platform_ID = db.Column(db.Integer, primary_key=False)
    
    def __repr__(self):
        return '%r, %r, %r, %r' % (self.User_ID, self.First_Name, self.Last_Name, self.Username)


class Owned_Games(db.Model):
    __tablename__ = "Owned_Games"

    Game_ID = db.Column(db.Integer, primary_key=True)
    Game_Name = db.Column(db.String(20))
    Platform = db.Column(db.String(20))
    Genre = db.Column(db.String(20))
    Rating = db.Column(db.Float)
    User_ID = db.Column(db.Integer, primary_key=False)
    
    def __repr__(self):
        return '%r, %r, %r, %r, %r' % (self.Game_ID, self.Game_Name, self.Platform, self.Genre, self.Rating)


class Achievements(db.Model):
    __tablename__ = "Achievements"
    
    Achievement_ID = db.Column(db.Integer, primary_key=True)
    Achievement_Name = db.Column(db.String(20))
    Game_Name = db.Column(db.String(20))
    Achievement_Score = db.Column(db.Float)
    Game_ID = db.Column(db.Integer, primary_key=False)
    
    def __repr__(self):
        return '%r, %r, %r, %r' % (self.Achievement_ID, self.Achievement_Name, self.Game_Name, self.Achievement_Score)

        
class Game_Wishlist(db.Model):
    __tablename__ = "Game_Wishlist"
    
    Wish_ID = db.Column(db.Integer, primary_key=True)
    Game_Name = db.Column(db.String(20))
    Platform = db.Column(db.String(20))
    Genre = db.Column(db.String(20))
    Price = db.Column(db.Float)
    User_ID = db.Column(db.Integer, primary_key=False)
    
    def __repr__(self):
        return '%r, %r, %r, %r, %r' % (self.Wish_ID, self.Game_Name, self.Platform, self.Genre, self.Price)

        
class Game_Tags(db.Model):
    __tablename__ = "Game_Tags"
    
    Tag_ID = db.Column(db.Integer, primary_key=True)
    Tag = db.Column(db.String(20))
    Game_Associated_With_Tag = db.Column(db.String(20))
    Tag_Popularity_Rating = db.Column(db.Float)
    Tag_User_Relevance_Rating = db.Column(db.Float)
    User_ID = db.Column(db.Integer, primary_key=False)
    
    def __repr__(self):
        return '%r, %r, %r, %r, %r' % (self.Tag_ID, self.Tag, self.Game_Associated_With_Tag, self.Tag_Popularity_Rating, self.Tag_User_Relevance_Rating)


class Per_Genre_Statistics(db.Model):
    __tablename__ = "Per_Genre_Statistics"
    
    Genre_ID = db.Column(db.Integer, primary_key=True)
    Genre_Name = db.Column(db.String(20))
    Sessions_Played = db.Column(db.Integer)
    Hours_Played = db.Column(db.Integer)
    User_ID = db.Column(db.Integer, primary_key=False)
    
    def __repr__(self):
        return '%r, %r, %r, %r' % (self.Genre_ID, self.Genre_Name, self.Sessions_Played, self.Hours_Played)

        
class Per_Game_Statistics(db.Model):
    __tablename__ = "Per_Game_Statistics"
    
    Stat_ID = db.Column(db.Integer, primary_key=True)
    User_ID = db.Column(db.Integer, primary_key=False)
    
    def __repr__(self):
        return '%r, %r' % (self.Stat_ID, self.User_ID)


class Singleplayer_Game_Statistics(db.Model):
    __tablename__ = "Singleplayer_Game_Statistics"
    
    Stat_ID = db.Column(db.Integer, primary_key=True)
    Game_Name = db.Column(db.String(20))
    Platform = db.Column(db.String(20))
    Genre = db.Column(db.String(20))
    Hours_Played = db.Column(db.Integer)
    Achievements_Completed_Percentage = db.Column(db.Float)
    Playthroughs_Started = db.Column(db.Integer)
    Playthroughs_Completed = db.Column(db.Integer)
    Easter_Eggs_Found = db.Column(db.Integer)
    Side_Quests_Started = db.Column(db.Integer)
    Side_Quests_Completed = db.Column(db.Integer)
    Bosses_Defeated = db.Column(db.Integer)
    Highest_Difficulty_Defeated = db.Column(db.String(20))
    Number_of_Difficulties_Completed = db.Column(db.Integer)
    Sessions_Played = db.Column(db.Integer)
    Achievement_Score = db.Column(db.Float)
    Total_Achievements_Count = db.Column(db.Integer)
    Achievements_Completed = db.Column(db.Integer)
    
    def __repr__(self):
        return '%r, %r, %r, %r, %r, %r, %r, %r, %r, %r, %r, %r, %r, %r, %r, %r, %r, %r' % (self.Stat_ID, self.Game_Name, self.Platform, self.Genre, self.Hours_Played, self.Achievements_Completed_Percentage, self.Playthroughs_Started, self.Playthroughs_Completed, self.Easter_Eggs_Found, self.Side_Quests_Started, self.Side_Quests_Completed, self.Bosses_Defeated, self.Highest_Difficulty_Defeated, self.Number_of_Difficulties_Completed, self.Sessions_Played, self.Achievement_Score, self.Total_Achievements_Count, self.Achievements_Completed)


class Multiplayer_Game_Statistics(db.Model):
    __tablename__ = "Multiplayer_Game_Statistics"
    
    Stat_ID = db.Column(db.Integer, primary_key=True)
    Game_Name = db.Column(db.String(20))
    Platform = db.Column(db.String(20))
    Hours_Played = db.Column(db.Integer)
    Sessions_Played = db.Column(db.Integer)
    Games_Played = db.Column(db.Integer)
    K_D_Ratio = db.Column(db.Float)
    Win_Loss_Ratio = db.Column(db.Float)
    Opponents_Played = db.Column(db.Integer)
    Player_Ranking = db.Column(db.Integer)
    
    def __repr__(self):
        return '%r, %r, %r, %r, %r, %r, %r, %r, %r, %r' % (self.Stat_ID, self.Game_Name, self.Platform, self.Hours_Played, self.Sessions_Played, self.Games_Played, self.K_D_Ratio, self.Win_Loss_Ratio, self.Opponents_Played, self.Player_Ranking)
    

class Co_op_Game_Statistics(db.Model):
    __tablename__ = "Co_op_Game_Statistics"
    
    Stat_ID = db.Column(db.Integer, primary_key=True)
    Game_Name = db.Column(db.String(20))
    Platform = db.Column(db.String(20))
    Genre = db.Column(db.String(20))
    Hours_Played = db.Column(db.Integer)
    Co_op_Players_Played_With = db.Column(db.Integer)
    Sessions_Played = db.Column(db.Integer)
    Missions_Completed = db.Column(db.Integer)
    Missions_Failed = db.Column(db.Integer)
    Missions_Started = db.Column(db.Integer)
    Total_Achievements_Count = db.Column(db.Integer)
    Achievements_Completed = db.Column(db.Integer)
    Achievements_Completed_Percentage = db.Column(db.Float)
    Achievement_Score = db.Column(db.Float)
    
    def __repr__(self):
        return '%r, %r, %r, %r, %r, %r, %r, %r, %r, %r, %r, %r, %r, %r' % (self.Stat_ID, self.Game_Name, self.Platform, self.Genre, self.Hours_Played, self.Co_op_Players_Played_With, self.Sessions_Played, self.Missions_Completed, self.Missions_Failed, self.Missions_Started, self.Total_Achievements_Count, self.Achievements_Completed, self.Achievements_Completed_Percentage, self.Achievement_Score)


class Overall_Gaming_Statistics(db.Model):
    __tablename__ = "Overall_Gaming_Statistics"
    
    User_ID = db.Column(db.Integer, primary_key=True)
    Hours_Played = db.Column(db.Integer)
    Total_Achievements_Count = db.Column(db.Integer)
    Achievements_Completed = db.Column(db.Integer)
    Achievements_Completed_Percentage = db.Column(db.Float)
    Achievements_Score = db.Column(db.Float)
    Idle_Time = db.Column(db.Integer)

    def __repr__(self):
        return '%r, %r, %r, %r, %r, %r, %r' % (self.User_ID, self.Hours_Played, self.Total_Achievements_Count, self.Achievements_Completed, self.Achievements_Completed_Percentage, self.Achievements_Score, self.Idle_Time)
        

class Game_Client(db.Model):
    __tablename__ = "Game_Client"
    
    Client_ID = db.Column(db.Integer, primary_key=True)
    User_ID = db.Column(db.Integer, primary_key=False)
    Platform = db.Column(db.String(20))
    Username = db.Column(db.String(20))
    
    def __repr__(self):
        return '%r, %r, %r' % (self.Client_ID, self.Platform, self.Username)


class Vendor_Platform(db.Model):
    __tablename__ = "Vendor_Platform"
    
    Platform_ID = db.Column(db.Integer, primary_key=True)
    Platform = db.Column(db.String(20))
    Company = db.Column(db.String(20))
    
    def __repr__(self):
        return '%r, %r, %r' % (self.Platform_ID, self.Platform, self.Company)


class Game_Company(db.Model):
    __tablename__ = "Game_Company"
    
    Company_ID = db.Column(db.Integer, primary_key=True)
    Platform_ID = db.Column(db.Integer, primary_key=False)
    Company_Name = db.Column(db.String(20))
    Number_of_Games_Released = db.Column(db.Integer)
    
    def __repr__(self):
        return '%r, %r, %r, %r' % (self.Company_ID, self.Platform_ID, self.Company_Name, self.Number_of_Games_Released)


class Games(db.Model):
    __tablename__ = "Games"
    
    Product_ID = db.Column(db.Integer, primary_key=True)
    Platform_ID = db.Column(db.Integer, primary_key=False)
    Game_Name = db.Column(db.String(20))
    Genre = db.Column(db.String(20))
    Rating = db.Column(db.Float)
    Price = db.Column(db.Float)
    Company_ID = db.Column(db.Integer, primary_key=False)
    
    def __repr__(self):
        return '%r, %r, %r, %r, %r, %r, %r' % (self.Product_ID, self.Platform_ID, self.Game_Name, self.Genre, self.Rating, self.Price, self.Company_ID)
