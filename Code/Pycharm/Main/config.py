DB_USERNAME = 'root'
DB_HOST = 'localhost'
DB_PORT = '3306'

DB_PASSWORD = 'test1234'  # MySQL Password
DB_NAME = 'projectdb'  # MySQL Name

SECRET_KEY = 'dev'

## Path
Root_Path = 'C:\\G_Project\\Code\\Pycharm\\Main'

## Daily DATA관련 init
Daily_FolderPath = Root_Path + '\\DB_source\\Daily\\'

## csv DATA관련 init
csv_FolderPath = Root_Path + '\\DB_source\\csv\\'

## 초기 DATA관련 init
Retail_FolderPath = Root_Path + "\\DB_source\\Init\\retail_json\\"
RecipeData_FilePath = Root_Path + "\\DB_source\\Init\\recipe.json"
WholesaleVolume_FilePath = Root_Path + "\\DB_source\\Init\\220726_농산물거래량.json"
WholesalePrice_FilePath = Root_Path + "\\DB_source\\Init\\220726_농산물가격.json"

Area_Dict = {'광주': 'gwangju', '대구': 'daegu', '대전': 'daejeon', '부산': 'busan',
             '서울': 'seoul', '울산': 'ulsan', '인천': 'incheon', '전체': 'total'}