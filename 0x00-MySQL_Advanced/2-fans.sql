-- a SQL scripts that ranks country origins of bands, ordered by the number of non-uniqque fans

SELECT origin, nb_fans
FROM (
  SELECT origin, COUNT(DISTINCT id) AS nb_fans
  FROM metal_bands
  GROUP BY origin
) AS subquery
ORDER BY nb_fans DESC;
