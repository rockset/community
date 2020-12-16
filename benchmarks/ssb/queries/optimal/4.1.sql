select d_year, c_nation, sum(lo_revenue - lo_supplycost) as profit
from denormalized HINT(access_path=column_scan)
where c_region = 'AMERICA'
  and s_region = 'AMERICA'
  and (p_mfgr = 'MFGR#1' or p_mfgr = 'MFGR#2')
  and p_category between 'MFGR#11' and 'MFGR#29'
group by d_year, c_nation
order by d_year, c_nation;
