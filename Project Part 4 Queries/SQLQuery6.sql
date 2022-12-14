INSERT INTO dbo.Per_Genre_Statistics
	([Genre_ID],[Genre_Name],[Sessions_Played],[Hours_Played],[User_ID])
VALUES
	( 500, 'Action', 100, 1000, 1 ),
	( 501, 'Strategy', 5, 50, 1 ),
	( 502, 'Batman', 1000, 10000, 2 ),
	( 503, 'Stealth', 1500, 12500, 2 )
GO

INSERT INTO dbo.Per_Game_Statistics
	([Stat_ID],[User_ID])
VALUES
	( 600, 1 ),
	( 601, 1 ),
	( 602, 1 ),
	( 603, 2 ),
	( 604, 2 ),
	( 605, 2 )
GO

INSERT INTO dbo.Singleplayer_Game_Statistics
	([Stat_ID], [Game_Name], [Platform], [Genre], [Hours_Played], [Achievements_Completed_Percentage], [Playthroughs_Started], [Playthroughs_Completed], [Easter_Eggs_Found], [Side_Quests_Started], [Side_Quests_Completed], [Bosses_Defeated], [Highest_Difficulty_Defeated], [Number_of_Difficulties_Completed], [Sessions_Played], [Achievement_Score], [Total_Achievements_Count], [Achievements_Completed])
VALUES
	( 600, 'Halo MCC', 'Steam', 'Action', 300, 0.4, 3, 2, 10, 52, 51, 8, 'Heroic', 4, 35, 53.2, 100, 40 ),
	( 603, 'Arkham Knight', 'Steam', 'Action', 500, 0.9, 10, 10, 100, 40, 40, 9, 'Insane', 6, 300, 90.5, 100, 90 )
GO

INSERT INTO dbo.Multiplayer_Game_Statistics
	([Stat_ID], [Game_Name], [Platform], [Hours_Played], [Sessions_Played], [Games_Played], [K_D_Ratio], [Win_Loss_Ratio], [Opponents_Played], [Player_Ranking])
VALUES
	( 601, 'Halo MCC', 'Steam', 300, 45, 80, 1.1, 1.1, 640, 3500 ),
	( 604, 'Arkham Knight', 'Steam', 500, 50, 50, 100.0, 20.0, 50, 1 )
GO

INSERT INTO dbo.Co_op_Game_Statistics
	([Stat_ID], [Game_Name], [Platform], [Genre], [Hours_Played], [Co_op_Players_Played_With], [Sessions_Played], [Missions_Completed], [Missions_Failed], [Missions_Started], [Total_Achievements_Count], [Achievements_Completed], [Achievements_Completed_Percentage], [Achievement_Score])
VALUES
	( 602, 'Borderlands2', 'Steam', 'Action', 600, 10, 200, 1500, 40, 2000, 100, 60, 0.6, 65.5 ),
	( 605, 'Gotham City', 'Steam', 'Action', 1000, 5, 250, 7500, 150, 10000, 100, 90, 0.9, 90.5 )
GO

INSERT INTO dbo.Overall_Gaming_Statistics
	([User_ID], [Hours_Played], [Total_Achievements_Count], [Achievements_Completed], [Achievements_Completed_Percentage], [Achievements_Score], [Idle_Time])
VALUES
	( 1, 20000, 3000, 2000, 0.6, 2555.5, 750 ),
	( 2, 40000, 5000, 4900, 0.98, 6555.8, 400 )
GO

INSERT INTO dbo.Game_Client
	([Client_ID], [Platform], [Username], [User_ID])
VALUES
	( 700, 'Steam', 'Evo', 1 ),
	( 701, 'Steam', 'Batman', 2 )
GO