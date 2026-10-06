import pickle
import pandas as pd
import streamlit as st
import time

def predict_loan_default(user_data):
    try:
        model = pickle.load(open('loan_default_rf_model.pkl', 'rb'))
        df_input = pd.DataFrame([{
            'LoanAmount': float(user_data.get('LoanAmount', 0)),
            'InterestRate': float(user_data.get('InterestRate', 0)),
            'Income': float(user_data.get('Income', 0)),
            'Age': float(user_data.get('Age', 0)),
            'CreditScore': float(user_data.get('CreditScore', 0)),
            'LoanPurpose': user_data.get('LoanPurpose', ''),
            'EmploymentType': user_data.get('EmploymentType', '')
        }])
        result = model.predict(df_input)
        return result[0]    
    except Exception as e:
        print("Lỗi hệ thống:", e)
        return 1   
st.set_page_config(page_title="Hệ thống Xét Duyệt Tín Dụng AI", page_icon="🏦")
st.title("Trợ lý Xét Duyệt Khoản Vay ")
st.caption("Ứng dụng thuật toán Random Forest phân tích đa biến để ra quyết định tín dụng")
if "messages" not in st.session_state:
    st.session_state.messages = []
if "step" not in st.session_state:
    st.session_state.step = 0
if "user_data" not in st.session_state:
    st.session_state.user_data = {}
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
if st.session_state.step == 0 and len(st.session_state.messages) == 0:
    first_msg = "Chào bạn. Hệ thống có thể giúp gì cho khoản vay tài chính của bạn? Bạn muốn đăng ký số tiền vay là bao nhiêu?"
    st.session_state.messages.append({"role": "assistant", "content": first_msg})
    with st.chat_message("assistant"):
        st.markdown(first_msg)
if prompt := st.chat_input("Nhập tin nhắn của bạn..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("⏳ *Đang ghi nhận...*")
        time.sleep(0.5) 
        reply = ""    
        if st.session_state.step == 0:
            st.session_state.user_data['LoanAmount'] = prompt
            st.session_state.step = 1
            reply = "Bạn dự định sử dụng khoản vay này cho mục đích gì?"          
        elif st.session_state.step == 1:
            st.session_state.user_data['LoanPurpose'] = prompt
            st.session_state.step = 2
            reply = "Xin vui lòng cho biết tuổi hiện tại của bạn."     
        elif st.session_state.step == 2:
            st.session_state.user_data['Age'] = prompt
            st.session_state.step = 3
            reply = "Thu nhập trung bình hàng tháng của bạn là bao nhiêu?"
        elif st.session_state.step == 3:
            st.session_state.user_data['Income'] = prompt
            st.session_state.step = 4
            reply = "Tình trạng công việc hiện tại của bạn như thế nào? Bạn đang làm toàn thời gian, tự do hay hình thức khác?" 
        elif st.session_state.step == 4:
            st.session_state.user_data['EmploymentType'] = prompt
            st.session_state.step = 5
            reply = "Điểm tín dụng (Credit Score) hiện tại của bạn là bao nhiêu? Nếu không rõ, bạn có thể ước lượng con số."         
        elif st.session_state.step == 5:
            st.session_state.user_data['CreditScore'] = prompt
            st.session_state.step = 6
            reply = "Cuối cùng, mức lãi suất vay mong muốn của bạn là bao nhiêu % một năm?"        
        elif st.session_state.step == 6:
            st.session_state.user_data['InterestRate'] = prompt
            st.session_state.step = 7 
            message_placeholder.markdown("🔄 *Hệ thống Random Forest đang phân tích chéo các dữ liệu hồ sơ...*")
            time.sleep(2)    
            risk_score = predict_loan_default(st.session_state.user_data)    
            if risk_score == 0:
                reply = "**THÔNG BÁO DUYỆT HỒ SƠ:** Dựa trên các chỉ số tài chính, hồ sơ của bạn được xếp hạng rủi ro thấp. Khoản vay của bạn đã được chấp thuận."
            else:
                reply = "**THÔNG BÁO TỪ CHỐI:** Hệ thống nhận thấy một số yếu tố rủi ro từ dữ liệu công việc và tài chính hiện tại. Chúng tôi chưa thể cấp khoản vay cho bạn lúc này."       
            reply += "\n\n*(Gõ bất kỳ ký tự nào để bắt đầu phiên tư vấn mới)*"         
        elif st.session_state.step == 7:
            st.session_state.step = 0
            st.session_state.messages = []
            st.session_state.user_data = {}
            st.rerun()
        if reply:
            message_placeholder.markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})