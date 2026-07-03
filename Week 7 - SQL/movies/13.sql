-- 13. Names of all people who starred in a movie in which Kevin Bacon also starred
SELECT DISTINCT name
FROM people
JOIN stars ON people.id = stars.person_id
JOIN movies ON movies.id = stars.movie_id
WHERE movie_id IN (
    SELECT movie_id
    FROM stars
    JOIN people ON people.id = stars.person_id
    JOIN movies ON movies.id = stars.movie_id
    WHERE name = 'Kevin Bacon'
)
AND name != 'Kevin Bacon';

