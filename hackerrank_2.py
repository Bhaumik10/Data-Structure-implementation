arr = []
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)

sum = -64
a = []


for i in xrange(4):
    for j in xrange(5):
        new_sum = arr[j][i] + arr[j][i+1] + arr[j][i+2]
        print arr[j][i] , arr[j][i+1] , arr[j][i+2]
        if j < 5:
            j = j + 1
        if i < 5 :
            i = i + 1
        new_sum = new_sum + arr[j][i]
        print arr[j][i]
        if j < 5:
            j = j + 1
        if i < 5:
            i = i - 1
        new_sum = new_sum + arr[j][i] + arr[j][i+1] + arr[j][i+2]
        print arr[j][i] , arr[j][i+1] , arr[j][i+2]
        print  "new_sum ", new_sum
        if new_sum > sum:
            sum = new_sum
            a.append(sum)
        else:
            ''
        if j == 5:
            break

print a
print max(a)