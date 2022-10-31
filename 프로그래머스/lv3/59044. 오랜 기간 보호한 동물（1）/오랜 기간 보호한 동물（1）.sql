-- 코드를 입력하세요
SELECT ins.NAME, ins.DATETIME
FROM ANIMAL_INS ins
LEFT JOIN ANIMAL_OUTS outs on outs.ANIMAL_ID = ins.ANIMAL_ID
where outs.ANIMAL_ID is null
order by DATETIME
limit 3