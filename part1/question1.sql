/* How many sessions are there? 
Assumption: Each visitID is a unique session 
*/ 

select 
count(distinct visitId) sessions 
from dhh-analytics-hiringspace.GoogleAnalyticsSample.ga_sessions_export;

