/* What’s the conversion rate from the shop list page to the shop details page? 
*/
select 
*
, shop_details_page / shop_list_page shop_list_to_details_conversion 
from (
  select 
  count(distinct case when eventCategory like '%shop_list%' then visitId end) shop_list_page
  , count(distinct case when eventCategory like '%shop_details%' then visitId end) shop_details_page
  from dhh-analytics-hiringspace.GoogleAnalyticsSample.ga_sessions_export, unnest(hit)
  )