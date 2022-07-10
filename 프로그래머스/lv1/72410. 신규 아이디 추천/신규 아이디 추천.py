import re
def solution(new_id):
    # 1 단계
    new_id = new_id.lower()
    # 2 단계
    new_id = [ s for s in new_id if s.islower() or s.isdigit() or s == '-' or s == '_' or s == '.']
    # 3 단계
    new_id = re.sub('(([.])\\2{1,})', '.' , ''.join(new_id))
    # 4 단계
    if new_id != '' and new_id[0] == '.' : new_id = new_id[1:] 
    if new_id != '' and new_id[len(new_id)-1] == '.' : new_id = new_id[:len(new_id)-1] 
    # # 5 단계
    if new_id == '' : new_id = new_id + 'a'
    # # 6 단계
    if len(new_id) > 15:
        new_id = new_id[:15]
        if new_id[14] == '.':
            new_id = new_id[:14]
    # # 7 단계
    while len(new_id) < 3:
        new_id += new_id[len(new_id)-1]
    return new_id