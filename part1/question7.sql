/* What’s the conversion rate from the shop list page to the shop details page? 
*/
select 
*
, transactions / sessions conversion_rate
from (
  select 
  deviceCategory
  , operatingSystem
  , count(distinct visitId) sessions
  , count(distinct case when eventCategory like '%transaction%' or screenName = 'DeliveryDetailsScreen' then visitId end) transactions
  from dhh-analytics-hiringspace.GoogleAnalyticsSample.ga_sessions_export, unnest(hit)
  group by 1,2
  )
