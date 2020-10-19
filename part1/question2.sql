/* How many sessions does each user create? 
Assumption:
 Each visitID is a unique session 
fullvisitorId represent user id
*/


select fullvisitorid user_id
, count(distinct visitId) session_count
from dhh-analytics-hiringspace.GoogleAnalyticsSample.ga_sessions_export
group by fullvisitorid

