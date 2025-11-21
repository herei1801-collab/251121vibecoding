import streamlit as st

# 기본 설정 🎨
st.set_page_config(
    page_title="MBTI 고전 책 추천",
    page_icon="📚",
    layout="centered"
)

# ---------- 데이터 영역 ----------
MBTI_BOOKS = {
    "INTJ": {
        "title": "『죄와 벌』",
        "author": "표도르 도스토예프스키",
        "tag": "도덕·심리·사고력",
        "emoji": "🧠",
        "reason": "도덕적 딜레마와 인간 심리를 깊이 파고드는 작품이라 계획적이고 분석적인 INTJ에게 잘 맞아요.",
        "point": "주인공 라스콜리니코프의 사고 과정을 따라가며 ‘정의란 무엇인가’를 스스로 정리해 볼 수 있어요."
    },
    "INTP": {
        "title": "『변신』",
        "author": "프란츠 카프카",
        "tag": "실존·아이디어",
        "emoji": "🌀",
        "reason": "‘왜?’를 끊임없이 던지는 INTP에게 상징과 해석의 여지가 많은 작품이에요.",
        "point": "한 문장, 한 장면마다 여러 가지 해석을 떠올려 보는 지적 놀이를 해 볼 수 있어요."
    },
    "ENTJ": {
        "title": "『군주론』",
        "author": "니콜로 마키아벨리",
        "tag": "리더십·권력",
        "emoji": "👑",
        "reason": "목표 지향적이고 전략적인 ENTJ에게 권력과 통치에 대한 냉철한 관점을 던져 줍니다.",
        "point": "좋은 리더십이란 무엇인지, ‘효율’과 ‘윤리’의 균형을 생각해 볼 수 있어요."
    },
    "ENTP": {
        "title": "『국가』",
        "author": "플라톤",
        "tag": "토론·철학",
        "emoji": "💬",
        "reason": "토론과 아이디어 싸움을 좋아하는 ENTP에게 철학 대화를 형식으로 한 고전이에요.",
        "point": "정의, 이상 국가, 교육 등 다양한 주제로 끝없는 토론거리를 던져 줍니다."
    },
    "INFJ": {
        "title": "『레 미제라블』",
        "author": "빅토르 위고",
        "tag": "공감·이상",
        "emoji": "🌈",
        "reason": "이상과 현실 사이에서 고민하는 INFJ에게 사회 정의와 사랑, 용서의 이야기를 전해 줘요.",
        "point": "한 사람의 선택이 주변과 사회에 어떤 파장을 주는지 깊이 느껴 볼 수 있어요."
    },
    "INFP": {
        "title": "『어린 왕자』",
        "author": "앙투안 드 생텍쥐페리",
        "tag": "감성·상징",
        "emoji": "🪐",
        "reason": "내면의 세계와 감성을 소중히 여기는 INFP에게 짧지만 깊은 상징으로 가득한 작품이에요.",
        "point": "‘중요한 것은 눈에 보이지 않는다’는 메시지가 INFP의 마음에 오래 남을 거예요."
    },
    "ENFJ": {
        "title": "『사람은 무엇으로 사는가』",
        "author": "레프 톨스토이",
        "tag": "관계·윤리",
        "emoji": "🤝",
        "reason": "사람과 관계, 공동체를 중요하게 생각하는 ENFJ에게 딱 맞는 인간 이해의 이야기예요.",
        "point": "사람이 살아가는 힘이 무엇인지, 타인을 대하는 태도에 대해 다시 생각해 볼 수 있어요."
    },
    "ENFP": {
        "title": "『데미안』",
        "author": "헤르만 헤세",
        "tag": "자아·성장",
        "emoji": "✨",
        "reason": "자신만의 길을 찾아가는 ENFP에게 ‘나답게 산다’는 게 무엇인지 던지는 성장 소설입니다.",
        "point": "빛과 그림자를 모두 끌어안는 성장을 통해, 자기만의 색깔을 찾는 여행을 함께할 수 있어요."
    },
    "ISTJ": {
        "title": "『논어』",
        "author": "공자",
        "tag": "원칙·실천",
        "emoji": "📜",
        "reason": "원칙과 책임을 중시하는 ISTJ에게 삶의 기준이 될 만한 짧은 문장들이 가득해요.",
        "point": "한 구절씩 천천히 읽고, 자신의 생활 규칙으로 정리해 보는 공부법도 잘 어울립니다."
    },
    "ISFJ": {
        "title": "『작은 아씨들』",
        "author": "루이자 메이 올컷",
        "tag": "가족·배려",
        "emoji": "🏡",
        "reason": "주변 사람을 돌보는 ISFJ에게 따뜻하고 섬세한 가족 이야기가 큰 위로를 줍니다.",
        "point": "각 자매의 성격을 보며 자신의 모습과 주변 친구들을 떠올려 보는 재미가 있어요."
    },
    "ESTJ": {
        "title": "『무소유』",
        "author": "법정",
        "tag": "질서·절제",
        "emoji": "🧘",
        "reason": "현실적이고 일 잘하는 ESTJ에게 ‘효율’ 대신 ‘비움’이라는 다른 기준을 보여 줍니다.",
        "point": "바쁜 일상 속에서 무엇을 우선순위에 둘지 다시 정리하는 시간을 줄 거예요."
    },
    "ESFJ": {
        "title": "『안네의 일기』",
        "author": "안네 프랑크",
        "tag": "공감·기록",
        "emoji": "📖",
        "reason": "타인의 감정에 민감한 ESFJ에게 한 소녀의 솔직한 기록은 강한 공감과 울림을 줍니다.",
        "point": "‘기록’이 한 사람의 삶을 어떻게 남기는지, 나만의 일기를 써 보고 싶어질 거예요."
    },
    "ISTP": {
        "title": "『로빈슨 크루소』",
        "author": "다니엘 디포",
        "tag": "생존·문제 해결",
        "emoji": "🛠️",
        "reason": "실용적이고 손으로 부딪치는 ISTP에게 혼자서 문제를 해결하며 살아가는 이야기가 딱이에요.",
        "point": "‘나였으면 어떻게 했을까?’를 떠올리며, 생존 스킬과 계획을 상상해 보는 재미가 있습니다."
    },
    "ISFP": {
        "title": "『월든』",
        "author": "헨리 데이비드 소로",
        "tag": "자연·내면",
        "emoji": "🌿",
        "reason": "감성적이고 조용한 ISFP에게 자연과 함께하는 고요한 사색이 잘 맞아요.",
        "point": "조용한 공간에서, 좋아하는 음악과 함께 조금씩 읽으면 최고의 힐링 시간이 됩니다."
    },
    "ESTP": {
        "title": "『삼국지연의』",
        "author": "나관중",
        "tag": "전략·액션",
        "emoji": "⚔️",
        "reason": "에너지 넘치고 승부욕 강한 ESTP에게 전쟁, 전략, 카리스마 넘치는 인물들이 꽉 찬 작품이에요.",
        "point": "전투 장면을 읽으며 ‘내가 장수라면 어떻게 움직였을까’를 상상해 보는 재미가 있어요."
    },
    "ESFP": {
        "title": "『돈키호테』",
        "author": "미겔 데 세르반테스",
        "tag": "모험·유머",
        "emoji": "🎭",
        "reason": "현재를 즐기고 분위기를 살리는 ESFP에게 웃음과 생각거리를 동시에 주는 모험담이에요.",
        "point": "엉뚱한 돈키호테를 보며, ‘꿈꾸는 사람’의 용기와 한계를 같이 느껴볼 수 있습니다."
    },
}

MBTI_LIST = list(MBTI_BOOKS.keys())

# ---------- 사이드바 ----------
with st.sidebar:
    st.markdown("### 🔍 사용 방법")
    st.markdown(
        """
        1. MBTI 유형을 선택해요  
        2. 추천받은 고전을 읽어볼지 고민해 봐요 📚  
        3. 친구들과 **왜 이 책이 나와 어울리는지** 이야기해 보세요!
        """
    )
    st.markdown("---")
    st.markdown("#### 💡 Tip")
    st.markdown(
        "MBTI는 성격을 100% 규정하지 않아요. **‘이런 성향이라서 이런 책도 잘 맞을 수 있겠다’** 정도로 가볍게 봐 주세요 🙂"
    )

# ---------- 메인 화면 ----------
st.markdown("# 📚 MBTI 기반 고전 책 추천")
st.markdown("### 나의 성향에 어울리는 클래식 한 권, 오늘 골라볼까? ✨")

# 이름(선택)
col_name, col_mbti = st.columns([1, 1.2])

with col_name:
    name = st.text_input("이름 (선택) ✍️", placeholder="예: 김학생")

with col_mbti:
    mbti = st.selectbox(
        "MBTI 유형을 선택해 주세요 🔠",
        ["선택 안 함"] + MBTI_LIST,
        index=0
    )

st.markdown("---")

if mbti == "선택 안 함":
    st.info("왼쪽 상단에서 **MBTI 유형**을 선택하면, 당신에게 어울리는 고전 한 권을 추천해 줄게요 😉")
else:
    data = MBTI_BOOKS[mbti]

    display_name = f"{name}님을 위한" if name else "당신을 위한"

    st.markdown(
        f"""
        <div style="
            padding: 1.8rem;
            border-radius: 1.2rem;
            background: linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%);
            border: 1px solid #e0e0e0;
        ">
            <p style="margin:0; font-size:0.95rem; color:#666;">{display_name} MBTI {mbti} 타입 맞춤 추천 📌</p>
            <h2 style="margin-top:0.4rem; margin-bottom:0.2rem;">
                {data['emoji']} {data['title']}
            </h2>
            <p style="margin:0.2rem 0 0.6rem 0; color:#555;">저자: <b>{data['author']}</b></p>
            <span style="
                display:inline-block;
                padding:0.2rem 0.6rem;
                border-radius:999px;
                background-color:#f5f5f5;
                font-size:0.8rem;
                color:#555;
                margin-bottom:0.8rem;
            ">
                #{data['tag']}
            </span>
            <p style="margin:0.2rem 0; font-size:0.95rem; line-height:1.5; color:#333;">
                {data['reason']}
            </p>
            <p style="margin:0.4rem 0 0; font-size:0.92rem; color:#444;">
                💭 <b>이 책 포인트</b> – {data['point']}
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("")

    # 독서 다짐 & 활동 아이디어
    with st.expander("📒 읽을 때 이렇게 해 보면 어때요?"):
        st.markdown(
            f"""
            - 마음에 남는 문장을 발견하면 **밑줄 긋기 / 캡처 / 노트 정리** 해 보기  
            - MBTI {mbti} 성향과 연결해서  
              - “이 인물의 선택, 나는 어떻게 했을까?”를 적어 보기  
            - 친구들과 한 문장씩 골라서 **서로 소개 & 이유 나누기** 🗣️  
            """
        )

    # 작은 체크박스
    finished = st.checkbox("이 책, 언젠가 꼭 읽어보고 싶어요 ✅")

    if finished:
        st.success("좋아요! 언젠가 문득 시간이 날 때, 이 책부터 천천히 펼쳐 보면 어떨까요? ☕📖")


# 하단 푸터
st.markdown("---")
st.caption("✨ 이 웹앱은 MBTI를 가벼운 재미로 활용해 고전을 추천해 주는 작은 도서 큐레이터예요.")


