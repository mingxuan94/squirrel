/* How many visitors change their order payment method? 
Assumptions: 
1. Update order payment will trigger eventAction = 'order_payment_method.chosen' 
2. Event action will be triggered more than once if visitors were to change their order payment method. Check timestamps of every trigger of eventAction = 'order_payment_method.chosen' for eash session
3. If timestamp between 2 events are more than 5 seconds apart, we assume that there is a change in order payment method 
*/
select count(distinct fullvisitorid) visitors
from (
  select 
  *
  , datetime_diff(timestamp, lag(timestamp) over (partition by fullvisitorid, visitId order by timestamp), second) update_payment_time
  from (
    select 
    fullvisitorid
    , visitId
    , PARSE_DATETIME('%Y%m%d %H:%M:%S' , date||' '|| SUBSTR(CAST(TIME(TIMESTAMP_MILLIS(visitStartTime)) AS STRING), 1,8)) timestamp
    from dhh-analytics-hiringspace.GoogleAnalyticsSample.ga_sessions_export, UNNEST(hit) 
    where eventAction = 'order_payment_method.chosen'
  )
)
where update_payment_time >= 5


