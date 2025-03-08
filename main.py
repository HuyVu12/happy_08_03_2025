import streamlit as st
from streamlit_extras.let_it_rain import rain

st.set_page_config(page_title="Chúc mừng 8/3", page_icon="🌸", layout="centered")

rain(
    emoji="🌸", 
    font_size=20,
    falling_speed=5,
    animation_length="infinite",
)

st.write("## 💖 Chúc mừng Ngày Quốc tế Phụ nữ 8/3 💖")
st.subheader("Gửi Mẹ Nhu và chị Hai yêu quý!")

st.subheader("🎁 Nhấn vào hộp quà để mở bất ngờ!")

if st.button("🎁 Mở Quà"):
    st.write("##### Vẽ hình mẹ bằng Fourier Drawing nè :))")
    st.write('''###### Video hơi giật do vừa vẽ vừa quay á :'<''')
    video_path = "./videos/v01.mp4"
    st.video(video_path)

    st.write(
        """
        **🌹 Mẹ yêu quý,**  
        Nhân ngày 8/3, con muốn gửi đến mẹ những lời chúc yêu thương nhất.  
        Mẹ luôn là người tuyệt vời nhất trong lòng con. Chúc mẹ thật nhiều sức khỏe, niềm vui và hạnh phúc!  
        **Cảm ơn mẹ vì tất cả!** 💖  
        """
    )

    st.subheader("🌸 Chúc thêm cho mẹ zui :>")
    loi_chuc = [
        "💐 Chúc mẹ luôn mạnh khỏe, hạnh phúc và mãi trẻ đẹp!",
        "🌼 Con yêu mẹ nhiều lắm! Chúc mẹ luôn vui vẻ và yêu đời!",
        "🌻 Cảm ơn mẹ vì đã luôn yêu thương và chăm sóc con!",
        "🌷 Mẹ là món quà quý giá nhất mà con có được trong cuộc đời!",
        "💕 Chúc mẹ một ngày 8/3 thật đặc biệt và ý nghĩa!"
    ]

    for chuc in loi_chuc:
        st.write(chuc)

    st.subheader("🌼 Chúc Hai yêu quý 😻")
    st.write(
        """
        **Chị Hai yêu dấu,**  
        Chúc chị có một ngày 8/3 thật ý nghĩa!  
        Mong chị luôn vui vẻ, thành công trong công việc và tràn đầy hạnh phúc.  
        Cảm ơn chị vì luôn là một người chị tuyệt vời, luôn yêu thương và giúp đỡ em! 💕  
        """
    )
    st.write("------")
    st.write(" #### 👾 P/s: Do trục trặc kỹ thuật nên hoàn thành hơi trễ nên sorry hai với mẹ nhiều :'<")
    st.write(
        """
        Cụ thể là trễ khoảng 20h42' với top lí do sau: \n
        Top 1: Do vẽ gà 🐤🐣🐤\n
        Top 2: Do tìm nhạc 🎶\n
        Top 3: Do trời không mưa ⛅ ??\n

        TOP 4: Do gà 🐧. \n
        """
    )
    st.write("------")
    st.write(
        """
        P/s 2: Hình hai chưa làm kịp ròi để hồi sau nha :<<. 
        """
    )
    st.image("./images/a02.jfif", caption="Chúc hai và mẹ luôn vui vẻ và hạnh phúc! 💖", use_container_width =True)


st.write("Trong trường hợp nhạc không tự chạy thì hai với mẹ ấn cái ni nhá :v")
st.audio('./musics/m01.mp3', format="audio/wav", start_time=0, loop=True, autoplay=True)