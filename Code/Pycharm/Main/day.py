from config import DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME, Area_Dict, Whole_List, Daily_FolderPath, Root_Path
from server.define.daily_DB import DailyDB
from server.prophet.parameter import W_Parameter_Dict, R_Parameter_Dict
from server.prophet.prophet_code import MyProphet

Daily = DailyDB(DB_USERNAME, DB_HOST, DB_PASSWORD, DB_NAME, Area_Dict, Whole_List, Daily_FolderPath)

Daily_Prophet = MyProphet(DB_USERNAME, DB_HOST, DB_PASSWORD, DB_NAME, Root_Path, W_Parameter_Dict, R_Parameter_Dict)

# Daily_Check = Daily.Daily_Data()
# print(Daily_Check)
# Daily_Wholesale = Daily_Prophet.Wholesale()
# Daily_Retail = Daily_Prophet.Retail()
# print(Daily_Wholesale)
# print(Daily_Retail)
