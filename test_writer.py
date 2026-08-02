from cataloger.excel.writer import ExcelWriter

writer = ExcelWriter("sample_data/ASP Library Catalog Project.xlsx")

writer.write_headers()

print(writer.ai_columns)

writer.save("sample_data/ASP Library Catalog Project AI.xlsx")

print("Success!")