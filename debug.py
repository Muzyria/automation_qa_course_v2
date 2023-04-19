data_1 = ['Commands', 'WorkSpace', 'React', 'Angular', 'Veu', 'Public', 'Classified', 'Downloads', 'Word File.doc', 'Excel File.doc']
data_2 = ['commands', 'workspace', 'react', 'angular', 'veu', 'public', 'classified', 'downloads', 'wordFile', 'excelFile']


data_3 = [item.replace(".doc", "").replace(" ", "").lower() for item in data_1]
data_4 = [item.lower() for item in data_2]
print(data_3 == data_4)

print(str(data_1).replace(".doc", ""))