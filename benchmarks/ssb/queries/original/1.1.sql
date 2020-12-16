select sum(lineorder.lo_extendedprice * lineorder.lo_discount) as revenue
from lineorder
  join dwdate on lineorder.lo_orderdate = dwdate.d_datekey
where dwdate.d_year = 1993
  and lineorder.lo_discount between 1 and 3
  and lineorder.lo_quantity < 25;
