select dwdate.d_year, supplier.s_city, part.p_brand1, sum(lineorder.lo_revenue - lineorder.lo_supplycost) as profit
from lineorder
  join customer on lineorder.lo_custkey = customer.c_custkey
  join supplier on lineorder.lo_suppkey = supplier.s_suppkey
  join part on lineorder.lo_partkey = part.p_partkey
  join dwdate on lineorder.lo_orderdate = dwdate.d_datekey
where customer.c_region = 'AMERICA'
  and supplier.s_nation = 'UNITED STATES'
  and (dwdate.d_year = 1997 or dwdate.d_year = 1998)
  and part.p_category = 'MFGR#14'
group by d_year, s_city, p_brand1
order by d_year, s_city, p_brand1;
