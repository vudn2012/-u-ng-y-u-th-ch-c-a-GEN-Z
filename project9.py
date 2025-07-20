import streamlit as st
from datetime import datetime

with st.form('Order đồ uống'):
    drinks = ('Trà sữa truyền thống', 'Trà sữa matcha', 'Trà sữa', 'Trái cây') 
    option_drink = st.selectbox('Bạn muốn loại đồ uống gì?', drinks)

    sizes = ('S', 'M', 'L')
    option_size = st.radio('Bạn muốn size nào?', sizes)

    sugars = ('Đường trắng', 'Đường nâu', 'Không thêm đường')
    option_sugar = st.selectbox('Bạn thích thêm loại đường nào?', sugars)

    jellys = ('Thạch rau câu', 'Thạch nha đam', 'Không thêm thạch')
    option_jelly = st.selectbox('Bạn thích thêm loại thạch nào?', jellys)

    nums = st.slider('Số lượng bạn muốn đặt:', 1, 10, 1)

    notes = st.text_area('Ghi chú thêm cho đơn hàng (nếu có):')

    submitted = st.form_submit_button("Xác nhận")

    bill = {
        'Tên shop:': 'Tiệm Trà Mát Mẻ',
        'Ngày giờ xuất bill:': datetime.now().strftime("%d/%m/%Y %H:%M"),
        'Loại đồ uống:': option_drink,
        'Size:': option_size,
        'Loại đường:': option_sugar,
        'Loại thạch:': option_jelly,
        'Số lượng:': nums,
        'Ghi chú thêm:': notes
    }

    if submitted:
        st.write('📄 **Thông tin đơn hàng**')
        for key, value in bill.items():
            st.write(f"🔹 {key} {value}")

print_bill = st.checkbox('🎟️ In hóa đơn')
if print_bill:
    ans = ""
    for key, value in bill.items():
        ans += f"{key} {value}\n"
    st.download_button('📥 Tải về hóa đơn', ans, file_name="hoa_don.txt")
