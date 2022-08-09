import yolov5.detect as dt


def Yolorun(path):
    FoodList = ['.', '닭볶음탕', '된장찌개', '갈치구이', '감자조림', '김밥', '김치전', '계란찜', '깻잎장아찌', '메추리알장조림', '떡볶이', '떡국']
    result = dt.run(weights='C:\\G_Project\\Code\\Pycharm\\Main\\test\\best.pt', source=path)
    result_foodlist = []
    for foodname in result:
        menu = FoodList[foodname]
        result_foodlist.append(menu)
    return result_foodlist

# print(YoloRun(r"C:\Users\hk_edu\Desktop\mania-done-20191102215825_lmgvwhlk.jpg"))
