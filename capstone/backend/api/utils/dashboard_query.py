OVERALL_CHAT = """
SELECT 
    COUNT(*) as total_chat
FROM 
    logs
"""



TIME_USAGE = """
SELECT
	AVG(time_usage) as average_time_usage
FROM
	logs
"""



TOP_USER_TIME = """
WITH rename_recast as(

SELECT 
	id
	,llm_model
	,prompt
	,question
	,answer
	,time_usage
	,strftime('%k', datetime) as datetime
from
	logs
),
count_usage as(

SELECT
	COUNT(*) as usage
	,datetime
from 
	rename_recast
group by
	datetime
order by 
    usage DESC
)

select * from count_usage
"""

PEAK_USER="""



"""

TOP_CATEGORY="""
SELECT 
	count(category) as count_category
	,category
from 
	category
group by 
	category
order by
	count_category DESC
"""