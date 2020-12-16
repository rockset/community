select sum(lo_revenue), d_year, p_brand1
from denormalized HINT(access_path=column_scan)
where p_category = 'MFGR#12'
  and s_region = 'AMERICA'
group by d_year, p_brand1
order by d_year, p_brand1;
