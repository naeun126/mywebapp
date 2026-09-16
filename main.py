import streamlit as st

st.title("첫 배포 확인 👋")
st.write("여기까지 보이면 배포 성공입니다.")
import streamlit as st
import random

# ---------------------------------------------------
# 페이지 기본 설정
# ---------------------------------------------------
st.set_page_config(
    page_title="MBTI 여행지 추천 💕",
    page_icon="🧳",
    layout="centered",
)

# ---------------------------------------------------
# 귀여운 스타일링 (CSS)
# ---------------------------------------------------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #ffe6f0 0%, #e6f0ff 50%, #fff9e6 100%);
    }
    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 800;
        color: #ff6fa5;
        padding-top: 10px;
        padding-bottom: 0px;
        text-shadow: 2px 2px 0px #ffffff;
    }
    .sub-title {
        text-align: center;
        font-size: 18px;
        color: #7a6f9b;
        padding-bottom: 25px;
    }
    .result-card {
        background: #ffffffcc;
        border-radius: 25px;
        padding: 30px;
        margin-top: 20px;
        box-shadow: 0px 8px 20px rgba(255, 111, 165, 0.25);
        border: 3px dashed #ffb6d9;
        text-align: center;
    }
    .dest-name {
        font-size: 30px;
        font-weight: 800;
        color: #ff4f8b;
        margin-bottom: 10px;
    }
    .dest-emoji {
        font-size: 60px;
    }
    .dest-desc {
        font-size: 17px;
        color: #555555;
        line-height: 1.6;
        margin-top: 10px;
    }
    .tag {
        display: inline-block;
        background: #ffe0ef;
        color: #ff6fa5;
        border-radius: 20px;
        padding: 5px 14px;
        margin: 4px;
        font-size: 14px;
        font-weight: 600;
    }
    div.stButton > button {
        background: linear-gradient(135deg, #ff9ecb, #ffc1e0);
        color: white;
        border: none;
        border-radius: 30px;
        padding: 12px 30px;
        font-size: 18px;
        font-weight: 700;
        box-shadow: 0px 4px 12px rgba(255, 111, 165, 0.4);
        transition: 0.2s;
    }
    div.stButton > button:hover {
        transform: scale(1.05);
        background: linear-gradient(135deg, #ff85bd, #ffb0d6);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------
# MBTI별 여행지 데이터
# ---------------------------------------------------
mbti_data = {
    "INTJ": {
        "emoji": "🗼",
        "destination": "일본 교토",
        "desc": "고요한 사찰과 정원을 거닐며 사색하기 좋은 도시예요. 계획적인 당신에게 딱 맞는 체계적인 일정 여행이 가능해요.",
        "tags": ["#전통", "#사색", "#계획형"],
    },
    "INTP": {
        "emoji": "🏛️",
        "destination": "그리스 아테네",
        "desc": "철학과 역사가 살아 숨쉬는 도시! 호기심 가득한 당신의 지적 탐구심을 자극하는 유적지 투어를 추천해요.",
        "tags": ["#철학", "#유적지", "#탐구"],
    },
    "ENTJ": {
        "emoji": "🏙️",
        "destination": "미국 뉴욕",
        "desc": "세계 경제와 문화의 중심지! 리더십 넘치는 당신에게 어울리는 역동적이고 스케일 큰 도시 여행이에요.",
        "tags": ["#도전", "#비즈니스", "#스케일"],
    },
    "ENTP": {
        "emoji": "🎡",
        "destination": "독일 베를린",
        "desc": "자유분방하고 실험적인 예술과 문화가 넘치는 도시예요. 새로운 아이디어를 좋아하는 당신과 찰떡궁합!",
        "tags": ["#자유", "#예술", "#토론"],
    },
    "INFJ": {
        "emoji": "🌸",
        "destination": "스위스 인터라켄",
        "desc": "평화로운 자연 속에서 깊은 사색을 즐길 수 있는 곳이에요. 조용히 힐링하고 싶은 당신에게 추천해요.",
        "tags": ["#자연", "#힐링", "#평화"],
    },
    "INFP": {
        "emoji": "🎨",
        "destination": "프랑스 파리",
        "desc": "예술과 낭만이 가득한 도시! 감성적이고 이상을 꿈꾸는 당신의 마음을 사로잡을 거예요.",
        "tags": ["#예술", "#감성", "#낭만"],
    },
    "ENFJ": {
        "emoji": "🌺",
        "destination": "태국 치앙마이",
        "desc": "따뜻한 사람들과 봉사 여행지로 유명한 곳! 사람을 아끼는 당신에게 잘 맞는 온정 넘치는 여행지예요.",
        "tags": ["#봉사", "#소통", "#따뜻함"],
    },
    "ENFP": {
        "emoji": "🌈",
        "destination": "호주 시드니",
        "desc": "액티비티와 자유로운 분위기가 가득한 곳! 에너지 넘치는 당신의 텐션을 200% 채워줄 거예요.",
        "tags": ["#액티비티", "#자유", "#에너지"],
    },
    "ISTJ": {
        "emoji": "⛩️",
        "destination": "일본 나라",
        "desc": "전통과 규칙이 살아있는 차분한 도시예요. 신뢰와 안정을 중시하는 당신에게 딱 맞는 계획형 여행지예요.",
        "tags": ["#전통", "#안정", "#질서"],
    },
    "ISFJ": {
        "emoji": "🏡",
        "destination": "체코 프라하",
        "desc": "동화 같은 골목길과 따뜻한 분위기가 매력적인 도시예요. 배려심 많은 당신에게 편안한 힐링 여행이 될 거예요.",
        "tags": ["#동화", "#포근함", "#배려"],
    },
    "ESTJ": {
        "emoji": "🏰",
        "destination": "영국 런던",
        "desc": "체계적인 시스템과 전통이 공존하는 도시! 계획적이고 리더십 있는 당신과 잘 어울려요.",
        "tags": ["#체계적", "#전통", "#효율"],
    },
    "ESFJ": {
        "emoji": "🌻",
        "destination": "이탈리아 로마",
        "desc": "사람 사이의 정과 맛있는 음식이 가득한 도시예요. 따뜻하고 사교적인 당신에게 즐거운 추억을 선물할 거예요.",
        "tags": ["#사교", "#미식", "#정"],
    },
    "ISTP": {
        "emoji": "🏔️",
        "destination": "뉴질랜드 퀸스타운",
        "desc": "익스트림 스포츠의 성지! 손재주 좋고 모험을 즐기는 당신에게 짜릿한 경험을 선사할 곳이에요.",
        "tags": ["#모험", "#액티비티", "#실용"],
    },
    "ISFP": {
        "emoji": "🌊",
        "destination": "인도네시아 발리",
        "desc": "아름다운 자연과 여유로운 감성이 흐르는 섬이에요. 자유롭고 예술적인 당신에게 완벽한 힐링 스팟!",
        "tags": ["#자연", "#여유", "#감성"],
    },
    "ESTP": {
        "emoji": "🎢",
        "destination": "스페인 바르셀로나",
        "desc": "열정적인 축제와 다이나믹한 매력이 넘치는 도시! 즉흥적이고 활동적인 당신과 찰떡궁합이에요.",
        "tags": ["#열정", "#즉흥", "#다이나믹"],
    },
    "ESFP": {
        "emoji": "🎉",
        "destination": "브라질 리우데자네이루",
        "desc": "카니발처럼 신나는 에너지가 가득한 도시! 사교적이고 흥 넘치는 당신을 위한 최고의 파티 여행지예요.",
        "tags": ["#파티", "#흥", "#사교"],
    },
}

# ---------------------------------------------------
# 화면 구성
# ---------------------------------------------------
st.markdown('<div class="main-title">💖 MBTI 여행지 추천 💖</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">나의 MBTI에 딱 맞는 여행지를 찾아볼까요? 🧳✨</div>', unsafe_allow_html=True)

mbti_list = list(mbti_data.keys())
selected_mbti = st.selectbox("✏️ 당신의 MBTI를 선택해주세요!", mbti_list)

if st.button("🔮 여행지 추천 받기!"):
    result = mbti_data[selected_mbti]
    tags_html = "".join([f'<span class="tag">{t}</span>' for t in result["tags"]])
    st.markdown(
        f"""
        <div class="result-card">
            <div class="dest-emoji">{result['emoji']}</div>
            <div class="dest-name">{selected_mbti} 님을 위한 추천 여행지</div>
            <div class="dest-name" style="font-size:26px;">✨ {result['destination']} ✨</div>
            <div class="dest-desc">{result['desc']}</div>
            <div style="margin-top:15px;">{tags_html}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.balloons()

st.markdown("---")
st.markdown(
    "<div style='text-align:center; color:#aaaaaa; font-size:13px;'>Made with 💕 by Streamlit</div>",
    unsafe_allow_html=True,
)
