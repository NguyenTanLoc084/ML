Trợ lý Ảo Xét Duyệt Tín Dụng Tự Động (Credit Risk Prediction)

Dự án này là một hệ thống Chatbot tương tác thông minh, được tích hợp Mô hình Học máy (Machine Learning) để đánh giá và dự đoán rủi ro tín dụng của khách hàng. Thay vì điền form truyền thống, người dùng sẽ trò chuyện với Chatbot để hệ thống tự động thu thập thông tin và đưa ra quyết định cấp hạn mức (Duyệt / Từ chối) theo thời gian thực.

Tính năng nổi bật

Giao diện tự nhiên (Conversational UI): Sử dụng Streamlit để tạo trải nghiệm nhắn tin mượt mà, giống các trợ lý ảo hiện đại.

Tự động trích xuất đặc trưng (Feature Extraction): Lấy dữ liệu về tuổi, thu nhập, và lịch sử trễ hạn trực tiếp từ cuộc hội thoại.

Tích hợp Machine Learning: Sử dụng thuật toán Logistic Regression kết hợp Chuẩn hóa dữ liệu (StandardScaler) để dự đoán rủi ro tín dụng.

🛠️ Công nghệ sử dụng

Ngôn ngữ: Python 3.x

Giao diện (Frontend): Streamlit

Xử lý dữ liệu: Pandas

Machine Learning: Scikit-learn (Logistic Regression, Pipeline, StandardScaler)

📁 Cấu trúc thư mục

📦 Thu_muc_du_an
 ┣ 📜 app.py                # Mã nguồn chính chạy giao diện Chatbot
 ┣ 📜 credit_model.pkl      # File mô hình học máy (đã được huấn luyện)
 ┗ 📜 README.md             # File hướng dẫn dự án


⚙️ Hướng dẫn cài đặt và khởi chạy

Bước 1: Cài đặt các thư viện cần thiết
Mở Terminal / Command Prompt và chạy lệnh sau:

pip install streamlit scikit-learn pandas


Bước 2: Khởi chạy ứng dụng
Di chuyển vào thư mục chứa dự án và gõ lệnh:

streamlit run app.py


Bước 3: Trải nghiệm
Trình duyệt sẽ tự động mở trang web tại địa chỉ http://localhost:8501. Bạn có thể bắt đầu nhắn tin với Chatbot để kiểm thử thuật toán dự đoán.

🧠 Thông tin về Mô hình Học máy

Dữ liệu huấn luyện: Lấy từ bộ dữ liệu Credit Risk (Kaggle).

Đầu vào (Features): Tuổi (Age), Thu nhập (Income), Lịch sử nợ xấu (Default History).

Đầu ra (Target): 0 (Đủ điều kiện cấp hạn mức) / 1 (Rủi ro vỡ nợ, từ chối).

Quy trình (Pipeline): Dữ liệu được đưa qua StandardScaler để cân bằng độ lớn trước khi đưa vào mô hình LogisticRegression dự đoán.