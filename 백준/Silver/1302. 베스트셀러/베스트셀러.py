import sys
N = int(input())
book_hash = {}
for i in range(N):
    book = sys.stdin.readline().strip()
    if book not in book_hash:
        book_hash[book] = 1
    else:
        book_hash[book] += 1
sorted_book = sorted(book_hash.items(), key= lambda x : [-x[1], x[0]])
print(sorted_book[0][0])