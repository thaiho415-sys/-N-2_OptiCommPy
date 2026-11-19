# Đồ án 2: Mô phỏng và đánh giá một tuyến thông tin quang IM-DD / OOK / PAM bằng Python

Dự án mô phỏng tuyến truyền dẫn quang điều chế cường độ - tách sóng trực tiếp (IM-DD) dựa trên thư viện mã nguồn mở OptiCommPy, đồng thời mở rộng so sánh hiệu năng giữa hai định dạng điều chế **OOK** và **4-PAM** có xét đến ảnh hưởng của bộ tách sóng quang (Photodiode) và cự ly sợi quang.

## 1. Code tham khảo ban đầu
* **Thư viện gốc:** [OptiCommPy](https://github.com/edsonportosilva/OptiCommPy) (tác giả: Edson Porto da Silva).

## 2. Các phần đã xây dựng và mở rộng
Toàn bộ mã nguồn thực nghiệm được đặt trong thư mục `OptiCommPy-main/`, bao gồm các phần tự xây dựng và mở rộng sau:
* `OptiCommPy-main/1_OOK.ipynb`: Mô phỏng tuyến truyền dẫn quang IM-DD cơ bản sử dụng điều chế OOK.
* `OptiCommPy-main/2_PAM4.ipynb`: Mở rộng mô phỏng tuyến truyền dẫn quang IM-DD sang định dạng điều chế 4-PAM.
* `OptiCommPy-main/3_OOK có dùng photodiode.ipynb`: Tích hợp khối tách sóng quang (Photodiode) vào đầu thu cho hệ thống OOK để đánh giá thực tế hơn.
* `OptiCommPy-main/4_PAM4 có dùng photodiode.ipynb`: Tích hợp khối tách sóng quang (Photodiode) cho hệ thống 4-PAM để đánh giá thực thế hơn
* Cả 4 phần đều có mở rộng tính toán và so sánh BER theo cự ly.
  
## 3. Hướng dẫn cài đặt môi trường và cách chạy code: 
Yêu cầu máy tính đã cài đặt **Python 3.10+** (dự án được phát triển trên Python 3.10.11).

1. Clone repository về máy:
   ```bash
   git clone [https://github.com/thaiho415-sys/-N-2_OptiCommPy.git](https://github.com/thaiho415-sys/-N-2_OptiCommPy.git)
   (Hoặc tải trực tiếp file ZIP từ GitHub về giải nén và chạy trên máy tính cá nhân, ví dụ sử  VS Code).
2. Mở Terminal và trỏ đến thư mục:
   cd -N-2_OptiCommPy
   cd OptiCommPy-main
3. Cài đặt các thư viện phụ thuộc và gói OptiCommPy
   pip install -r requirements.txt
   pip install -e .
4. Ghi nhận kết quả
   * Nếu cần quan sát từng kết quả: chạy từng cell code trong 4 file .jpynb của đề tài
   * Nếu cần lấy kết quả hình ảnh số liệu: python run_all_experiments.py => các file kết quả sẽ được lưu tự động vào thư mục **results/**
