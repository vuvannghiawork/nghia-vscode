import os


file = os.path.abspath(__file__)
file_settings = os.path.join(os.path.dirname(file), "../../.vscode/settings.json")

settings_path = os.path.expanduser('~/AppData/Roaming/Code/User/settings.json')


try:
    if os.path.exists(settings_path):
        os.remove(settings_path)
        print(f"Đã xóa symlink: {settings_path}")
    os.symlink(os.path.abspath(file_settings), settings_path)
    print(f"Tạo link: {settings_path}")
except OSError as e:
    print(f"Lỗi: {e}")
