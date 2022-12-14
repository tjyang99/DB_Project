INSERT INTO dbo.Vendor_Platform
	([Platform_ID], [Platform], [Company])
VALUES
	( 800, 'Steam', 'Valve' ),
	( 801, 'Xbox', 'Microsoft' ),
	( 802, 'Playstation', 'Sony' )
GO

INSERT INTO dbo.Game_Company
	([Company_ID], [Company_Name], [Number_of_Games_Released], [Platform_ID])
VALUES
	( 900, 'Bandai Namco', 30, 800 ),
	( 901, 'Sony', 10, 800 ),
	( 902, 'Microsoft', 8, 800 ),
	( 903, 'CD Projekt Red', 10, 800)
GO

INSERT INTO dbo.Games
	([Product_ID], [Game_Name], [Genre], [Rating], [Price], [Platform_ID], [Company_ID])
VALUES
	( 1000, 'Spiderman', 'Action', 4.9, 59.99, 800, 901 ),
	( 1001, 'Ace Combat 7', 'Flying', 4.7, 49.99, 800, 900 ),
	( 1002, 'Witcher 3', 'Adventure', 4.9, 59.99, 800, 903 )
GO