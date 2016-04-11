number_of_strings = int(raw_input())
arr_string = []
for i in xrange(number_of_strings):
    arr_string.append(raw_input())


no_of_queries = int(raw_input())
arr_queries = []
for i in xrange(no_of_queries):
    arr_queries.append(raw_input())

arr_query_cnt = [0]*len(arr_queries)


for i in range(len(arr_queries)):
    cnt = 0
    for j in range(len(arr_string)):
        if arr_queries[i] == arr_string[j]:
            cnt = cnt + 1
            j = j + 1
        else:
            j = j + 1
    arr_query_cnt[i] = cnt

print '\n'.join(map(str,arr_query_cnt))


