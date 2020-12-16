select c_city, s_city, d_year, sum(lo_revenue) as revenue
from denormalized HINT(access_path=column_scan)
where c_nation = 'UNITED STATES'
  and s_nation = 'UNITED STATES'
  and c_region = 'AMERICA'
  and s_region = 'AMERICA'
  and d_year >= 1992
  and d_year <= 1997
group by c_city, s_city, d_year
order by d_year asc, revenue desc;
