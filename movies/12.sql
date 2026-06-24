-- 12. Titles of all of movies in which both Jennifer Lawrence and Bradley Cooper starred
SELECT title
FROM movies
JOIN stars ON movies.id = stars.movie_id
JOIN people ON people.id = stars.person_id
JOIN ratings ON movies.id = ratings.movie_id
WHERE name = 'Jennifer Lawrence' AND movies.id IN (
    SELECT movie_id
    FROM stars
    JOIN people ON people.id = stars.person_id
    WHERE name = 'Bradley Cooper'
);
