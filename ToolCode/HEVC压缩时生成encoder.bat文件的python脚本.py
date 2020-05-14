import os


def file_name(file_dir):
    File_Name = []
    for files in os.listdir(file_dir):
        if os.path.splitext(files)[1] == '.cfg':  # 只读cfg文件
            File_Name.append(files)
    return File_Name


def main():
    # 文件要素：所有cfg文件放一起，创建I_PUNum和P_PUNum文件夹,再加上Encoder.exe和原始视频。只需修改路径即可
    path = r'C:\Users\45452\OneDrive\科研\HEVC_CNN_信息隐藏EMD pro\HM-16.15\bin\vc2010\Win32\Debug\批处理 Stega\信息隐藏压缩'
    txt_file_name = file_name(path)
    batfile = open(path + r"\encode.bat", 'w')
    batfile.write("set  classpath = .;\n")
    for item in txt_file_name:
        item = item.strip('.cfg')
        Onefile = "TAppEncoder.exe -c " + item + ".cfg " + ">" + item + ".txt\n"
        print(Onefile)
        batfile.write(Onefile)  # bat文件写入
    batfile.close()


if __name__ == '__main__':
    main()
