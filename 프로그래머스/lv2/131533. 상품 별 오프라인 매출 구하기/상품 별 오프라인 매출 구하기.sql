-- 코드를 입력하세요
SELECT p.PRODUCT_CODE, PRICE*sum(SALES_AMOUNT) as SALES
FROM PRODUCT p
JOIN OFFLINE_SALE os on p.PRODUCT_ID = os.PRODUCT_ID
GROUP BY p.PRODUCT_ID
ORDER BY PRICE*sum(SALES_AMOUNT) desc, p.PRODUCT_CODE