-- Select the title of the TV show and the linked genre ID
-- Join the tables tv_shows and tv_show_genres on their respective IDs
-- Order the results by ascending order of the TV show title and the genre ID
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
