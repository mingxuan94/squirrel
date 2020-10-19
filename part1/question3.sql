/* How much time does it take on average to reach the order confirmation page?  
Assumptions: 
- No eventAction 'order_tracking.loaded' as stated in the PDF, 
  Using the following as proxies for order confirmation page 
  1. eventCategory containing the term 'order_confirmation' 
  2. screenName = 'CartCheckoutScreen' and eventCategory like 'checkout' and eventAction = 'surcharge.accepted'
 
*/

SELECT 
AVG(DATETIME_DIFF(order_confirm_page, session_start, SECOND)) average_seconds_to_order_confirm_page
FROM (
  SELECT 
  visitId
  , MIN(PARSE_DATETIME('%Y%m%d %H:%M:%S' , date||' '|| SUBSTR(CAST(TIME(TIMESTAMP_MILLIS(visitStartTime)) AS STRING), 1,8))) session_start
  , MIN(CASE WHEN eventCategory LIKE '%order_confirmation%' 
       OR (screenName = 'CartCheckoutScreen' AND eventCategory LIKE '%checkout%' AND eventAction = 'surcharge.accepted')
       THEN PARSE_DATETIME('%Y%m%d %H:%M:%S' , date||' '|| SUBSTR(CAST(TIME(TIMESTAMP_MILLIS(visitStartTime)) AS STRING), 1,8)) END) order_confirm_page
  FROM dhh-analytics-hiringspace.GoogleAnalyticsSample.ga_sessions_export, UNNEST(hit) 
  GROUP BY 1
  )
WHERE order_confirm_page IS NOT NULL /* Consider only sessions that reached the order confirmation page */

