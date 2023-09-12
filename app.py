import streamlit as st
from streamlit_echarts import st_echarts
import plotly.express as px

with st.sidebar:
    st.header("<3")
    st.write("Dear Sru, by no doubt in this world, you have been the best person I have met. The way you have been there for me like no one other, is just something which would be too good to be true for me at one point.")
    st.write("I made a little something for you. Take your time and enjoy it. <3")

st.markdown(
        """
        <style>
            section[data-testid="stSidebar"] {
                width: 40px !important;
                background-image: linear-gradient(#27005D,#FFA1F5);
            }
        </style>
        """,
        unsafe_allow_html=True,
)

st.title("For the cutuest person ever",anchor=False)
st.subheader("29th September",anchor=False)

numbers, photos, end = st.tabs(['By the Numbers','Some Memories','Not Something You Want'])

with numbers:
    fig = px.bar(x=['Happy','Sad'],y = [10,1],title="Impact on Life ever since we met",color_discrete_sequence=px.colors.sequential.Burg)
    st.plotly_chart(fig)
    st.write("No sad at all but I just wanted it to be seen on the graph hehe.")

with photos:
    st.write("Feels like yesterday only, we bumping into each other, that waters party, the houseparty. Got so comfortable that it felt like you have become a habit, a good one. Whatever you have achieved is just out of this world and you have always done a super job in taking care of everyone along. Were, is and will be my cutu mood setter everytime. Times are always just the best with you and no price or no one can buy me these again. I just love you so so much. <3")
    
    st.markdown(
    """
    <style>
    .stButton {
        position: absolute;
        top: 60px;
        right: 290px;
        background-image: linear-gradient(#064663,#041C32);
        color: #ECB365;
        border: none;
        padding: 1px 10px;
        cursor: pointer;
        border-radius: 5px;

    }
    .stButton:hover {
        background-color: #2D6830; /* Change the hover background color */
    }
    </style>
    </style>
    """,
    unsafe_allow_html=True
    )
    new_page_url = "https://drive.google.com/file/d/1_TXDfD07mg15ILjPVhVwku-tCekiZ0_-/view?usp=sharing"
    st.markdown("""<a href="{}" target="_self"><button class='stButton'>Click Here! </button></a>""".format(new_page_url), unsafe_allow_html=True)

with end:
    st.write("I am sorry for messing up the audio. I like music and beats a lot but messed it up in the worst possible way. Anyways, cheers to us sru !")