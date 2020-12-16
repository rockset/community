select sum(lo_revenue), d_year, p_brand1
from denormalized HINT(access_path=column_scan)
where p_brand1 = 'MFGR#2221'
  and s_region = 'EUROPE'
  and p_category = 'MFGR#22'
group by d_year, p_brand1
order by d_year, p_brand1;
