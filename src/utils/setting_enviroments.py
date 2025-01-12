import os


# 現在のユーザー名を取得
def init() -> None:
    user_name = os.getlogin()
    # 環境変数を設定
    os.environ["TCL_LIBRARY"] = (
        rf"C:\Users\{user_name}\AppData\Local\Programs\Python\Python313\tcl\tcl8.6"
    )
    return 1
