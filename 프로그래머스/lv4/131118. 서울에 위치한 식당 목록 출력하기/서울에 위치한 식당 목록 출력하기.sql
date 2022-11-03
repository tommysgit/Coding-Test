-- 코드를 입력하세요
SELECT ri.REST_ID, ri.REST_NAME, FOOD_TYPE, FAVORITES, ADDRESS,
round(sum(REVIEW_SCORE)/count(*), 2) as SCORE
from REST_INFO ri
join REST_REVIEW rr on rr.REST_ID = ri.REST_ID
where ADDRESS like '서울%'
group by ri.REST_ID
order by SCORE desc, FAVORITES desc