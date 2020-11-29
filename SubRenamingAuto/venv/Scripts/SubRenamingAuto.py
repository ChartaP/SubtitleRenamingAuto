import os

Path_dir = input('경로를 입력하세요 : ')
Movie_type = input('영상 확장자를 입력하세요 : ')
Subtitle_type = input('자막 확장자를 입력하세요 : ')

File_list = os.listdir(Path_dir)
Movie_list = list( str for str in File_list if Movie_type in str )
Subtitle_list = list ( str for str in File_list if Subtitle_type in str)

print(Movie_list)
print(Subtitle_list)

if len(Movie_list) == len(Subtitle_list) :
    for i in range(len(Movie_list)) :
        new_Name = os.path.splitext(Movie_list[i])[0]+'.'+Subtitle_type
        os.rename(Path_dir+'\\'+Subtitle_list[i] , Path_dir+'\\'+new_Name)
    print('자막 변경완료')
    os.system("pause")
else :
    print('영상 갯수와 자막 갯수가 일치 하지 않습니다')
    os.system("pause")