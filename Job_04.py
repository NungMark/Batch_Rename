import os

def rename_files_in_directory(directory_path, target_extension):
    # ดึงรายชื่อไฟล์ทั้งหมดในโฟลเดอร์
    files = os.listdir(directory_path)

    # นับจำนวนไฟล์ที่มีนามสกุลเป้าหมาย
    target_files = [file for file in files if file.endswith(target_extension)]
    total_target_files = len(target_files)

    # เริ่มต้นตัวเลขเรียงลำดับ
    count = 1

    # วนลูปผ่านไฟล์ที่มีนามสกุลเป้าหมายและเปลี่ยนชื่อ
    for file in target_files:
        # แยกนามสกุลไฟล์และชื่อไฟล์
        filename, file_extension = os.path.splitext(file)

        # สร้างชื่อไฟล์ใหม่
        new_filename = f"{count:03d}.jpg"

        # สร้างเส้นทางเต็มของไฟล์เดิมและใหม่
        old_filepath = os.path.join(directory_path, file)
        new_filepath = os.path.join(directory_path, new_filename)

        # เปลี่ยนชื่อไฟล์
        os.rename(old_filepath, new_filepath)

        # เพิ่มตัวเลขเรียงลำดับ
        count += 1

    print(f"Successfully renamed {total_target_files} files.")

# เรียกใช้งานฟังก์ชั่น
directory_path = "D:/CDTI/Y2Semester/Ood/25_01_2567"  # แทนที่ด้วยเส้นทางที่ถูกต้อง
target_extension = ".jpg"
rename_files_in_directory(directory_path, target_extension)
