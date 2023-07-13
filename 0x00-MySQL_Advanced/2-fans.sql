-- a SQL scripts that ranks country origins of bands, ordered by the number of non-uniqque fans

SELECT origin, COUNT(*) AS nb_fans from metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;
