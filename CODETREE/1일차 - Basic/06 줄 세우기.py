# 키가 더 큰 학생 -> 몸무게가 더 큰 학생 -> 번호가 작은 학생
# 키, 몸무게, 번호
student = int(input())
info = []
for i in range(student):
    h, w = input().split()
    info.append((int(h),int(w),i+1))
ans_list = sorted(info, key = lambda x : (x[0]*(-1), x[1]*(-1), x[2]))
for i in ans_list:
    print(f'{i[0]} {i[1]} {i[2]}')