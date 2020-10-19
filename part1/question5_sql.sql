select 
hour
, count(distinct viquestiositId) sessions
from dhh-analytics-hiringspace.GoogleAnalyticsSample.ga_sessions_export, unnest(hit)
group by 1

