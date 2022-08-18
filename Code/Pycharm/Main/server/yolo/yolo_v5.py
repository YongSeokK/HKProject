import traceback

import yolov5.detect as dt


class Yolo:

    def __init__(self, pt_Path, Food_List, img_path):
        self.pt_Path = pt_Path
        self.Food_List = Food_List
        self.img_path = img_path

    def Yolorun(self):
        try:
            result = dt.run(weights=self.pt_Path, source=self.img_path)
            result_foodlist = []
            for food_name in result:
                menu = self.Food_List[food_name]
                result_foodlist.append(menu)
            return result_foodlist
        except Exception as e:
            message = traceback.format_exc()
        return message
