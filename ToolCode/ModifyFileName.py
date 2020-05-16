import os
def file_name(file_dir):
    File_Name=[]
    for files in os.listdir(file_dir):
        if os.path.splitext(files)[1] == '.cfg':
            File_Name.append(files)
    return File_Name

#bat文件和所有bin文件放一起，创建I_PUNum和P_PUNum文件夹
path = r'C:\Users\45452\OneDrive\科研\HEVC_CNN_信息隐藏EMD pro\HM-16.15\bin\vc2010\Win32\Debug\批处理 Stega\多层次cfg压缩\QP=38'
os.chdir(path)
txt_file_name=file_name(path)
print(txt_file_name[1][1])
for item in txt_file_name:
    newname = item[2:]
    os.rename(item, '3'+'8'+newname)

