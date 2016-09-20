-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP DATABASE IF EXISTS	tournament;

CREATE DATABASE tournament;

\c tournament

CREATE TABLE players (
id SERIAL PRIMARY KEY,
name TEXT
);

CREATE TABLE matches (
match_id SERIAL PRIMARY KEY,
winner INTEGER REFERENCES players(id) NOT NULL,
loser INTEGER REFERENCES players(id) NOT NULL
);

-- Creates the "Matches" view
CREATE VIEW matches_view AS
SELECT id AS player_id, name AS player_name, SUM(CASE WHEN players.id = matches.winner THEN 1 ELSE 0 END) AS wins,
COUNT(matches) AS matches
FROM players LEFT OUTER JOIN matches
ON players.id = matches.winner OR players.id = matches.loser
GROUP BY id
ORDER BY wins DESC, matches ASC;