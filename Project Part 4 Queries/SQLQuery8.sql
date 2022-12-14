/*
INSERT INTO dbo.Owned_Games
	(User_ID )
	SELECT User_ID FROM dbo.Game_User
	WHERE User_ID = 2
GO
*/

/*
UPDATE dbo.Owned_Games
SET Game_Name = 'Halo MCC', Platform = 'Steam', Genre = 'Action', Rating = 4.25
WHERE User_ID = 1
*/

UPDATE dbo.Game_User
SET Platform_ID = 800
WHERE User_ID = 1

UPDATE dbo.Game_User
SET Platform_ID = 800
WHERE User_ID = 2