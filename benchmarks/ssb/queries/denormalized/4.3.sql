select d_year, s_city, p_brand1, sum(lo_revenue - lo_supplycost) as profit
from denormalized
where c_region = 'AMERICA'
  and s_nation = 'UNITED STATES'
  and (d_year = 1997 or d_year = 1998)
  and p_category = 'MFGR#14'
group by d_year, s_city, p_brand1
order by d_year, s_city, p_brand1;
