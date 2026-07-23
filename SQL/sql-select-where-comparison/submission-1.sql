CREATE TABLE basketball_boxscore (
    game_id INT PRIMARY KEY,
    away_team_points INT,
    home_team_points INT
);

INSERT INTO basketball_boxscore (game_id, away_team_points, home_team_points) VALUES
(1, 100, 95),
(2, 105, 110),
(3, 90, 92),
(4, 110, 105),
(5, 95, 98);
-- Do not modify above this line --


SELECT * FROM basketball_boxscore WHERE away_team_points > home_team_points;


