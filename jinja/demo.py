import os

import pandas as pd
from xlsxtpl.writerx import BookWriter  # 需要提前pip install xlsxtpl


def write_test():
    pth = os.path.dirname(__file__)
    fname = os.path.join(pth, 'jinjia-excel-demo.xlsx')
    writer = BookWriter(fname)
    writer.jinja_env.globals.update(dir=dir, getattr=getattr)
    fname2 = os.path.join(pth, '营业额.xlsx')
    df1 = pd.read_excel(fname2, sheet_name='Sheet1')
    location = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    payloads = []
    for i in location:  # 根据不同的location写入不同的sheet
        lo_info = {
            'location': i}  # 对应模板中的location变量
        df_l1 = df1[df1['区域'] == i]
        rows = df1[df1['区域'] == i].values.tolist()  # 对应模板中的rows变量
        # print(rows)
        lo_info['rows'] = rows
        lo_info['sheet_name'] = i  # 对应模板中该sheet的名称
        payloads.append(lo_info)
    writer.render_book(payloads=payloads)
    fname = os.path.join(pth, 'jinjia-excel-demo-over.xlsx')
    writer.save(fname)


if __name__ == "__main__":
    write_test()
