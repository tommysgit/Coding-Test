-- 코드를 입력하세요
-- ins의 intake_condition 보다 datetime이 더 빠른 동물반환
SELECT ins.ANIMAL_ID, ins.NAME
FROM ANIMAL_INS as ins
JOIN ANIMAL_OUTS as outs on outs.ANIMAL_ID = ins.ANIMAL_ID
where outs.DATETIME < ins.DATETIME
order by ins.DATETIME