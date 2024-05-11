import openpyxl
def read_crad_from_xlsx(file_name_path):
    cred = []
    wb = openpyxl.load_workbook(filename=file_name_path)
    sheet = wb.active
    for r in sheet.iter_rows(min_row=2, values_only=True):
        x, b = r
        cred.append((dict(username=x, password=b)))
    return cred

hh=read_crad_from_xlsx(r"C:\Users\91939\Downloads\visu2.xlsx")
print(hh)