# 🏦 Trợ lý Tự động Xét Duyệt Khoản Vay (Loan Default Prediction) - Phiên bản Nâng cao

Dự án này là một hệ thống **Chatbot tương tác thông minh**, ứng dụng thuật toán **Random Forest** để đánh giá rủi ro tín dụng và khả năng trả nợ của khách hàng (Loan Default). Bằng cách thu thập 7 thông số tài chính và nhân khẩu học qua giao diện trò chuyện tự nhiên, hệ thống sẽ tự động đưa ra quyết định duyệt hoặc từ chối khoản vay theo thời gian thực.

## 🌟 Điểm nổi bật của Phiên bản Nâng cao

* **Xử lý Dữ liệu Đa biến (Multi-variable):** Hệ thống phân tích chéo nhiều yếu tố bao gồm cả dữ liệu dạng số (Số tiền vay, Lãi suất, Thu nhập, Tuổi, Điểm tín dụng) và dữ liệu dạng phân loại/chữ (Mục đích vay, Tình trạng việc làm).
* **AI Pipeline Tự động hóa:** 
  * Ứng dụng `SimpleImputer` để tự động xử lý các giá trị bị khuyết/thiếu (Missing values).
  * Ứng dụng `OneHotEncoder` để mã hóa các biến dạng phân loại thành các vector toán học.
  * Ứng dụng `StandardScaler` để chuẩn hóa khoảng cách dữ liệu.
* **Thuật toán Rừng ngẫu nhiên (Random Forest):** Xử lý hiệu quả bộ dữ liệu lớn, chống hiện tượng học vẹt (overfitting) tốt hơn, mang lại độ chính xác và độ tin cậy cao trong các quyết định tài chính.

## 🛠️ Công nghệ sử dụng

* **Ngôn ngữ:** Python 3.x
* **Giao diện (Frontend):** Streamlit
* **Xử lý dữ liệu:** Pandas
* **Machine Learning:** Scikit-learn (RandomForestClassifier, ColumnTransformer, Pipeline)

## 📁 Cấu trúc thư mục

```text
📦 Model_2_Project
 ┣ 📜 app.py                      # Mã nguồn chính chạy giao diện Chatbot Streamlit
 ┣ 📜 loan_default_rf_model.pkl   # File mô hình Pipeline đã được huấn luyện
 ┗ 📜 README.md                   # File tài liệu dự án
```

## ⚙️ Hướng dẫn cài đặt và khởi chạy

**Bước 1: Cài đặt các thư viện máy học cần thiết**
Mở Terminal / Command Prompt hoặc PowerShell tại thư mục dự án và chạy lệnh:
```bash
pip install streamlit scikit-learn pandas
```

**Bước 2: Khởi chạy ứng dụng Web**
Sử dụng Streamlit để chạy file mã nguồn:
```bash
streamlit run app.py
```

**Bước 3: Trải nghiệm**
Hệ thống sẽ tự động mở giao diện tại `http://localhost:8501`. Đóng vai khách hàng và nhập các thông số để kiểm thử khả năng ra quyết định của mô hình.

## 🧠 Thông tin chi tiết về Thuật toán

* **Bộ dữ liệu (Dataset):** Loan Default Prediction Dataset (hơn 250,000 bản ghi).
* **Đầu vào (Features - 7 biến):** 
  * `LoanAmount` (Số tiền vay)
  * `LoanPurpose` (Mục đích vay)
  * `Age` (Độ tuổi)
  * `Income` (Thu nhập trung bình)
  * `EmploymentType` (Tình trạng việc làm)
  * `CreditScore` (Điểm tín dụng)
  * `InterestRate` (Lãi suất mong muốn)
* **Đầu ra (Target):** `0` (An toàn - Đủ điều kiện duyệt) hoặc `1` (Rủi ro vỡ nợ - Từ chối).