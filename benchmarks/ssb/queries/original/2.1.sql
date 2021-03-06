select sum(lineorder.lo_revenue), dwdate.d_year, part.p_brand1
from lineorder
  join part on lineorder.lo_partkey = part.p_partkey
  join supplier on lineorder.lo_suppkey = supplier.s_suppkey
  join dwdate on lineorder.lo_orderdate = dwdate.d_datekey
where part.p_category = 'MFGR#12'
  and supplier.s_region = 'AMERICA'
group by d_year, p_brand1
order by d_year, p_brand1;
