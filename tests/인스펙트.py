import os
print(os.getcwd())

folder = "sample_folder"

if os.path.exists(folder):
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder)
    print("폴더를 제거하였습니다.")
else:
    os.makedirs(folder)
    print(folder, "폴더를 생성하였습니다.")

print(os.listdir())