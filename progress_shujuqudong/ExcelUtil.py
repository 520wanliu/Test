# 将excel中的数据读入并转化
import xlrd
class ExcelUtil():
    def __init__(self,excelPath, SheetName = "Sheet1"):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(SheetName)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数和总列数
        self.Nrows = self.table.nrows
        self.Ncols = self.table.ncols
    def dict_data(self):
        if(self.Nrows <= 1):
            print("总行数不超过1")
        else:
            r = []
            j = 1
            for i in range(self.Nrows - 1):
                s = {}
                # 从第二行开始获取对应values值
                values = self.table.row_values(j)
                for x in range(self.Ncols):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
            return r
if __name__ == '__main__':
    filePath = r"very_excel.xlsx"
    data1 = ExcelUtil(filePath)
    data = data1.dict_data()
    print(data)
    # for i in data:
    #     print(i)
