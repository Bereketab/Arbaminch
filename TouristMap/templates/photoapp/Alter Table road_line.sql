Alter Table road_line
Alter Column geom TYPE geometry(MULTILINESTRING, 4326)
Using ST_Force2D(geom)

ALTER TABLE road_line
  ALTER COLUMN geom 
  TYPE Geometry(LineString,4326) 
  USING ST_GeometryN(geom,1);
  
ALTER TABLE road_line
ADD COLUMN source integer,
ADD COLUMN target integer,
ADD COLUMN cost_len double precision,
ADD COLUMN cost_time double precision,
ADD COLUMN rcost_len double precision,
ADD COLUMN rcost_time double precision,
ADD COLUMN x1 double precision,
ADD COLUMN y1 double precision,
ADD COLUMN x2 double precision,
ADD COLUMN y2 double precision,
ADD COLUMN to_cost double precision,
ADD COLUMN rule text,
ADD COLUMN isolated integer,
ADD COLUMN len_km double precision,
ADD COLUMN len_miles  double precision,
ADD COLUMN  speed_mph double precision,
ADD COLUMN  speed_kmh double precision;

CREATE INDEX road_line_source_idx ON road_line (source);
CREATE INDEX road_line_target_idx ON road_line (target);

SELECT pgr_createTopology('road_line', 0.00001, 'geom', 'gid');

UPDATE road_line SET x1 = st_x(st_startpoint(geom)),
y1 = st_y(st_startpoint(geom)),
x2 = st_x(st_endpoint(geom)),
y2 = st_y(st_endpoint(geom)),
cost_len = St_lengthSpheroid(geom, 'SPHEROID["WGS84",6378137,298.25728]'),
rcost_len = St_lengthSpheroid(geom, 'SPHEROID["WGS84",6378137,298.25728]'),
len_km = St_lengthSpheroid(geom, 'SPHEROID["WGS84",6378137,298.25728]')/1000.0,
len_miles = St_lengthSpheroid(geom, 'SPHEROID["WGS84",6378137,298.25728]')/ 1000.0 * 0.6213712
speed_mph = CASE WHEN rd_type='Express way' THEN 65
WHEN rd_type='Avenu' THEN 65
WHEN rd_type='Streat' THEN 55
ELSE null END,
speed_kmh = CASE WHEN rd_type='Express way' THEN 104
WHEN rd_type='Avenu' THEN 88
WHEN rd_type='Streat' THEN 67
ELSE null END;

UPDATE road_line SET
cost_time = CASE
WHEN oneway='FT' THEN 10000.0
ELSE cost_len/1000.0/speed_kmh::numeric*3600.0
END,
rcost_time = CASE
WHEN oneway='TF' THEN 10000.0
ELSE cost_len/1000.0/speed_kmh::numeric*3600.0
END;

SELECT pgr_analyzeGraph('road_line', 0.00001, 'geom', 'gid');


SELECT seq, node, edge, cost
        FROM pgr_dijkstra('
                SELECT gid as id, source, target,
                cost_len as cost FROM road_line',
                100, 600, false
        );


/////////////////////////////////////////////////////////////////////////////////

SELECT seq, node, edge, cost_len as cost, agg_cost, geom
FROM pgr_dijkstra(
'SELECT gid as id, source, target, cost_len as cost FROM road_line',
(SELECT source from road_line order by geom <-> ST_SetSrid(ST_MakePoint(%x1% , %y1%), 4326) limit 1),
  (SELECT source from road_line order by geom <-> ST_SetSrid(ST_MakePoint(%x2% , %y2%), 4326) limit 1),false
    ) as pt
    JOIN road_line rd ON (pt.edge =rd.gid)






