ob=["國文","英文","微積分","體育","程式設計"]
all_course=[]
avg=0
for i in range(len(ob)):
    use_course=int(input(ob[i]+":"))
    avg=avg+use_course
    all_course.append(use_course)

max_ob=all_course.index(max(all_course))
min_ob=all_course.index(min(all_course))
print("平均分數"+str(round(avg/5,2)))
print("最高分課目"+ob[max_ob]+str(all_course[max_ob])+"分")
print("最低分課目"+ob[min_ob]+str(all_course[min_ob])+"分")