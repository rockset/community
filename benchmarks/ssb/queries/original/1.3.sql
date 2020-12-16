select sum(lineorder.lo_extendedprice * lineorder.lo_discount) as revenue
from lineorder
  join dwdate on lineorder.lo_orderdate = dwdate.d_datekey
where dwdate.d_weeknuminyear = 6
  and dwdate.d_year = 1994
  and lineorder.lo_discount between 5 and 7
  and lineorder.lo_quantity between 26 and 35;
