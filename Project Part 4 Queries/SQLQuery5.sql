INSERT INTO dbo.Game_Wishlist
	([Wish_ID],[Game_Name],[Platform],[Price],[Genre],[User_ID])
VALUES
	( 300, 'Cyberpunk 2077', 'Steam', 59.99, 'Action', 1 ),
	( 301, 'Halo Infinite', 'Steam', 59.99, 'Action', 1 ),
	( 302, 'Arkham Asylum', 'Steam', 19.99, 'Action', 2 ),
	( 303, 'Gotham Origins', 'Steam', 19.99, 'Action', 2 )
GO

INSERT INTO dbo.Game_Tags
	([Tag_ID], [Tag], [Game_Associated_With_Tag], [Tag_Popularity_Rating], [Tag_User_Relevance_Rating], [User_ID])
VALUES
	( 400, 'rpg', 'Borderlands2', 0.7, 0.75, 1 ),
	( 401, 'shooter', 'Halo MCC', 0.8, 0.85, 1 ),
	( 402, 'batman', 'Arkham Knight', 0.9, 0.9, 2 ),
	( 403, 'dark', 'Arkham Knight', 0.9, 0.9, 2 )
GO