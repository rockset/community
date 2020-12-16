select dwdate.d_year, supplier.s_nation, part.p_category, sum(lineorder.lo_revenue - lineorder.lo_supplycost) as profit
from lineorder
  join customer on lineorder.lo_custkey = customer.c_custkey
  join supplier on lineorder.lo_suppkey = supplier.s_suppkey
  join part on lineorder.lo_partkey = part.p_partkey
  join dwdate on lineorder.lo_orderdate = dwdate.d_datekey
where customer.c_region = 'AMERICA'
  and supplier.s_region = 'AMERICA'
  and (dwdate.d_year = 1997 or dwdate.d_year = 1998)
  and (part.p_mfgr = 'MFGR#1' or part.p_mfgr = 'MFGR#2')
group by d_year, s_nation, p_category
order by d_year, s_nation, p_category;
