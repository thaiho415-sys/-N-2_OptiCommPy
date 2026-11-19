import os
import subprocess
import sys

# Tự động tạo thư mục 'results'
os.makedirs("results", exist_ok=True)

notebooks = [
    "1_OOK.ipynb",
    "2_PAM4.ipynb",
    "3_OOK có dùng photodiode.ipynb",
    "4_PAM4 có dùng photodiode.ipynb",
]

print("=== BẮT ĐẦU CHẠY TOÀN BỘ THÍ NGHIỆM ===")

for nb in notebooks:
  print(f"\n>>> Đang chạy: {nb} ...")
  # Tự động chạy toàn bộ các cell từ trên xuống dưới và lưu kết quả vào notebook
  result = subprocess.run([
      sys.executable,
      "-m",
      "jupyter",
      "nbconvert",
      "--to",
      "notebook",
      "--execute",
      "--inplace",
      nb,
  ])

  if result.returncode == 0:
    print(f"[THÀNH CÔNG] Đã chạy xong {nb}")
  else:
    print(f"[LỖI] Có sự cố khi chạy {nb}")
    break

print(
    "\n=== HOÀN TẤT! Toàn bộ hình ảnh và dữ liệu đã được cập nhật trong thư"
    " mục 'results' ==="
)