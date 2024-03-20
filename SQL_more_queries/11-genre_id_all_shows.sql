-- Select the title of the TV show and the genre ID
-- Left join the tv_shows table with the tv_show_genres table on their respective IDs
-- Order the results by the title of the TV show in ascending order, and then by the genre ID in ascending order
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
