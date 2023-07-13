-- SQL script that lists all bands with 'Glam rock' as their main style,
-- ranked by thier longevity

SELECT band_name,
       IF(split IS NULL, YEAR('2022-01-01') - formed, split - formed) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
