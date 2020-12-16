select d_year, s_nation, p_category, sum(lo_revenue - lo_supplycost) as profit
from denormalized HINT(access_path=column_scan)
where c_region = 'AMERICA'
  and s_region = 'AMERICA'
  and (d_year = 1997 or d_year = 1998)
  and (p_mfgr = 'MFGR#1' or p_mfgr = 'MFGR#2')
  and p_category between 'MFGR#11' and 'MFGR#29'
group by d_year, s_nation, p_category
order by d_year, s_nation, p_category;
