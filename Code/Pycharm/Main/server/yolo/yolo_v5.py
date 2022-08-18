import traceback

import yolov5.detect as dt


class Yolo:

    def __init__(self, pt_path, FoodList, img_path):
        self.pt_path = pt_path
        self.FoodList = FoodList
        self.img_path = img_path

    def Yolorun(self):
        try:
            result = dt.run(weights=self.pt_path, source=self.img_path)
            result_foodlist = []
            for foodname in result:
                menu = self.FoodList[foodname]
                result_foodlist.append(menu)
            return result_foodlist
        except Exception as e:
            message = traceback.format_exc()
        return message
