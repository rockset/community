select c_nation, s_nation, d_year, sum(lo_revenue) as revenue
from denormalized
where c_region = 'ASIA'
  and s_region = 'ASIA'
  and d_year >= 1992
  and d_year <= 1997
group by c_nation, s_nation, d_year
order by d_year asc, revenue desc;
