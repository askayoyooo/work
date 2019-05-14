import xlrd
import xlwt
from xlutils.copy import copy
import os, shutil


def get_clean_data(filename):
    clean_data = []
    origin_lines = []
    with open(filename, 'r') as file_to_read:
        while True:
            lines = file_to_read.readline()
            if not lines:
                break
            l_tmp = [i for i in lines.split('\n')[0].split('\t')]
            origin_lines.append(l_tmp)
    for i in origin_lines:
        if i[0].startswith('[Type ') or len(i[0]) == 24 or len(i[0]) == 42 or len(i[0]) == 25 or len(i[0]) == 29:
            clean_data.append(i)
    return clean_data


def no_space(list_l):
    new_list = []
    for i in list_l:
        new_list.append(i.strip())
    return new_list


def report_writer(file_path, position, value, style):
    rd_book = xlrd.open_workbook(file_path, formatting_info=True)
    wt_book = copy(rd_book)
    wt_book.get_sheet(0).write(*position, value, style)
    wt_book.save(file_path)


def report_writer_repeat(file_path, position, value, style):
    rd_book = xlrd.open_workbook(file_path, formatting_info=True)
    wt_book = copy(rd_book)
    wt_book.get_sheet(0).write(*position, value, style)
    return wt_book


def report_writer_without_save(file_path, position, value, style):
    rd_book = xlrd.open_workbook(file_path, formatting_info=True)
    wt_book = copy(rd_book)
    wt_book.get_sheet(0).write(*position, value, style)
    return wt_book


def write_by_type(type_start, type_end, rd_book, new_l, xls_type_line_sn, style, file_path, i):
    for j in range(xls_type_line_sn[type_start], xls_type_line_sn[type_end]):
        if rd_book.sheet_by_index(0).cell(j, 1).value == new_l[i][0]:
            position = (j, 4)
            report_writer(file_path, position, new_l[i][2], style)


def write_by_repeat_type(type_start, type_end, new_l, xls_type_line_sn, style, file_path, i):
    rd_book = xlrd.open_workbook(file_path, formatting_info=True)
    for j in range(xls_type_line_sn[type_start], xls_type_line_sn[type_end]):
        if rd_book.sheet_by_index(0).cell(j, 1).value == new_l[i][0]:
            position = (j, 4)
            report_writer(file_path, position, rd_book.sheet_by_index(0).cell(j, 4).value + '\n' + new_l[i][2], style)


def file_name_p(file_dir, ext):
    L=[]
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == ext:
                # L.append(os.path.join(root, file))
                L.append(file)
    return L


def main():
    print('==========================================\n')
    print('Process is on going! Please wait patiently！\n')
    print('==========================================\n')
    style = xlwt.XFStyle()  # 格式信息
    font = xlwt.Font()  # 字体基本设置
    font.name = u'Arial'
    font.colour_index = 4
    font.height = 220  # 字体大小，220就是11号字体，大概就是11*20得来的吧
    style.font = font
    alignment = xlwt.Alignment()  # 设置字体在单元格的位置
    alignment.horz = xlwt.Alignment.HORZ_CENTER  # 水平方向
    alignment.vert = xlwt.Alignment.VERT_CENTER  # 竖直方向
    style.alignment = alignment
    border = xlwt.Borders()  # 给单元格加框线
    border.left = xlwt.Borders.THIN  # 左
    border.top = xlwt.Borders.THIN  # 上
    border.right = xlwt.Borders.THIN  # 右
    border.bottom = xlwt.Borders.THIN  # 下
    border.left_colour = 0x40  # 设置框线颜色，0x40是黑色，颜色真的巨多，都晕了
    border.right_colour = 0x40
    border.top_colour = 0x40
    border.bottom_colour = 0x40
    style.borders = border

    original_model = 'SMBIOS Table Checklist v1.8.xls'
    filename = file_name_p(os.path.dirname(os.path.realpath(__file__)), '.txt')[0]
    shutil.copy(original_model, filename[0:-3]+'.xls')
    file_path = filename[0:-3]+'.xls'

    data_list = get_clean_data(filename)
    new_l = []
    for i in data_list:
        new_l.append(no_space(i))

    # 获取dictionary: type line sn {'Type 000':5, 'Type 001':19,...]
    type_line_sn = {}
    xls_type_line_sn = {'Type 000': 1, 'Type 001': 11, 'Type 002': 22, 'Type 003': 32, 'Type 004': 41, 'Type 007': 66,
                        'Type 009': 77, 'Type 010': 88, 'Type 011': 93, 'Type 016': 110, 'Type 017': 120,
                        'Type 019': 148,
                        'Type 020': 157, 'Type 024': 176, 'Type 032': 234, 'Type 041': 272, 'Type 043': 284, 'end': 298}
    for line in new_l:
        if line[0].startswith('[Type'):
            if line[0][1:9] in type_line_sn:
                pass
            else:
                type_line_sn[line[0][1:9]] = new_l.index(line)

    rd_book = xlrd.open_workbook(file_path, formatting_info=True)

    for i in range(len(new_l)):
        if type_line_sn['Type 000'] < i < type_line_sn['Type 001']:
            write_by_type('Type 000', 'Type 001', rd_book, new_l, xls_type_line_sn, style, file_path, i)
        elif type_line_sn['Type 001'] < i < type_line_sn['Type 002']:
            write_by_type('Type 001', 'Type 002', rd_book, new_l, xls_type_line_sn, style, file_path, i)
        elif type_line_sn['Type 002'] < i < type_line_sn['Type 003']:
            write_by_type('Type 002', 'Type 003', rd_book, new_l, xls_type_line_sn, style, file_path, i)
        elif type_line_sn['Type 003'] < i < type_line_sn['Type 004']:
            write_by_type('Type 003', 'Type 004', rd_book, new_l, xls_type_line_sn, style, file_path, i)
        elif type_line_sn['Type 004'] < i < type_line_sn['Type 007']:
            write_by_type('Type 004', 'Type 007', rd_book, new_l, xls_type_line_sn, style, file_path, i)
        elif type_line_sn['Type 011'] < i < type_line_sn['Type 016']:
            for j in range(xls_type_line_sn['Type 011'], xls_type_line_sn['Type 016']):
                if rd_book.sheet_by_index(0).cell(j, 1).value == new_l[i][0]:
                    position = (j, 4)
                    if rd_book.sheet_by_index(0).cell(j, 1).value == 'String #1':
                        report_writer(file_path, position, new_l[i][2] + '\n' + new_l[i + 1][2], style)
                    else:
                        report_writer(file_path, position, new_l[i][2], style)
        elif type_line_sn['Type 016'] < i < type_line_sn['Type 017']:
            write_by_type('Type 016', 'Type 017', rd_book, new_l, xls_type_line_sn, style, file_path, i)
        elif type_line_sn['Type 019'] < i < type_line_sn['Type 020']:
            write_by_type('Type 019', 'Type 020', rd_book, new_l, xls_type_line_sn, style, file_path, i)
        elif type_line_sn['Type 024'] < i < type_line_sn['Type 032']:
            write_by_type('Type 024', 'Type 032', rd_book, new_l, xls_type_line_sn, style, file_path, i)
        elif type_line_sn['Type 032'] < i < type_line_sn['Type 041']:
            write_by_type('Type 032', 'Type 041', rd_book, new_l, xls_type_line_sn, style, file_path, i)
        elif type_line_sn['Type 043'] < i < len(new_l):
            write_by_type('Type 043', 'end', rd_book, new_l, xls_type_line_sn, style, file_path, i)
        elif type_line_sn['Type 007'] < i < type_line_sn['Type 009']:
            if len(new_l[i]) == 1:
                continue
            else:
                write_by_repeat_type('Type 007', 'Type 009', new_l, xls_type_line_sn, style, file_path, i)
        elif type_line_sn['Type 009'] < i < type_line_sn['Type 010']:
            if len(new_l[i]) == 1:
                continue
            else:
                write_by_repeat_type('Type 009', 'Type 010', new_l, xls_type_line_sn, style, file_path, i)
        elif type_line_sn['Type 010'] < i < type_line_sn['Type 011']:
            if len(new_l[i]) == 1:
                continue
            else:
                write_by_repeat_type('Type 010', 'Type 011', new_l, xls_type_line_sn, style, file_path, i)
        elif type_line_sn['Type 017'] < i < type_line_sn['Type 019']:
            if len(new_l[i]) == 1:
                continue
            else:
                write_by_repeat_type('Type 017', 'Type 019', new_l, xls_type_line_sn, style, file_path, i)
        elif type_line_sn['Type 020'] < i < type_line_sn['Type 024']:
            if len(new_l[i]) == 1:
                continue
            else:
                write_by_repeat_type('Type 020', 'Type 024', new_l, xls_type_line_sn, style, file_path, i)
        elif type_line_sn['Type 041'] < i < type_line_sn['Type 043']:
            if len(new_l[i]) == 1:
                continue
            else:
                write_by_repeat_type('Type 041', 'Type 043', new_l, xls_type_line_sn, style, file_path, i)
    print('==========================================\n')
    print('Finished 1 SKU result')
    print('==========================================\n')


if __name__ == '__main__':
    main()

