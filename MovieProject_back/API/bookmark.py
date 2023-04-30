target_title = '해리 포터와 불사조 기사단'
compare_lst = ['해리 포터와 불의 잔', '해리 포터와 비밀의 방', '해리 포터와 마법사의 돌', '해리 포터와 혼혈 왕자', '아바타', '어벤져스 : 인피니티 워', '어벤져스 : 에이지 오브 울트론']
lst = []
for movie in compare_lst:
    cnt = 0
    for i in range(len(target_title)):
        if target_title[i] == movie[i]:
            cnt += 1
        else:
            break
    if cnt > 4:
        lst.append(movie)
print(lst)

