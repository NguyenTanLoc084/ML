import pickle
import streamlit as st
import time

def predict_credit_risk(user_data):
    try:
        model = pickle.load(open('credit_model.pkl', 'rb'))
        age = int(user_data['age'])
        income = int(user_data['income'])
        late_history = 1 if 'có' in user_data.get('late', '').lower() else 0
        result = model.predict([[age, income, late_history]])
        return result[0] 
    except Exception as e:
        print("Lỗi:", e)
        return 1 
st.set_page_config(page_title="Chatbot Xét Duyệt Tín Dụng", page_icon="🤖")
st.title("Trợ lý Ảo Duyệt SPayLater")
st.caption("Chatbot tự động đánh giá hồ sơ rủi ro tín dụng bằng Machine Learning")

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
    first_msg = "Chào bạn! Bạn muốn đăng ký hạn mức vay là bao nhiêu VNĐ?"
    st.session_state.messages.append({"role": "assistant", "content": first_msg})
    with st.chat_message("assistant"):
        st.markdown(first_msg)
if prompt := st.chat_input("Nhập tin nhắn của bạn..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("*Đang xử lý...*")
        time.sleep(0.5)      
        reply = ""
        if st.session_state.step == 0:
            st.session_state.user_data['loan_amount'] = prompt
            st.session_state.step = 1
            reply = "Để hệ thống đánh giá hồ sơ, vui lòng cho biết **Tuổi** của bạn."
            
        elif st.session_state.step == 1:
            st.session_state.user_data['age'] = prompt
            st.session_state.step = 2
            reply = "Mức **Thu nhập hàng tháng** của bạn là bao nhiêu?"
            
        elif st.session_state.step == 2:
            st.session_state.user_data['income'] = prompt
            st.session_state.step = 3
            reply = "Bạn đã từng **trả chậm** hay **trễ hạn** khoản vay nào chưa?"
            
        elif st.session_state.step == 3:
            st.session_state.user_data['late'] = prompt
            st.session_state.step = 4
            message_placeholder.markdown("*Hệ thống đang chạy mô hình Machine Learning đánh giá rủi ro...*")
            time.sleep(1.5)          
            risk_score = predict_credit_risk(st.session_state.user_data)
            
            if risk_score == 0:
                reply = "**XIN CHÚC MỪNG!** Dựa trên đánh giá rủi ro, hồ sơ của bạn đạt độ tin cậy cao. Hạn mức của bạn đã được **DUYỆT**."
            else:
                reply = "**RẤT TIẾC!** Dựa trên thuật toán đánh giá an toàn tín dụng, hồ sơ của bạn hiện chưa đủ điều kiện để cấp hạn mức lúc này. Vui lòng thử lại sau."
                
            reply += "\n\n*(Gõ bất kỳ ký tự nào để bắt đầu lại)*"
            
        elif st.session_state.step == 4:
            st.session_state.step = 0
            st.session_state.messages = []
            st.session_state.user_data = {}
            st.rerun()
        if reply:
            message_placeholder.markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})