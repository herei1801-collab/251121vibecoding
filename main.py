import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="MBTI 진로 상담실",
    page_icon="🎓",
    layout="centered",
)

# 약간의 스타일(기본 기능: st.markdown + CSS)
st.markdown(
    """
    <style>
    .main {
        background: radial-gradient(circle at top, #fdfbfb 0%, #ebedee 60%, #ffffff 100%);
    }
    .title-box {
        padding: 1.5rem 1.8rem;
        border-radius: 1.5rem;
        background: linear-gradient(135deg, #4f46e5, #6366f1);
        color: white;
        box-shadow: 0 18px 35px rgba(15, 23, 42, 0.25);
        margin-bottom: 1.5rem;
    }
    .title-main {
        font-size: 1.9rem;
        font-weight: 800;
        margin-bottom: 0.4rem;
    }
    .title-sub {
        font-size: 0.95rem;
        opacity: 0.9;
    }
    .card {
        padding: 1.2rem 1.4rem;
        border-radius: 1.2rem;
        background: rgba(255, 255, 255, 0.88);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(148, 163, 184, 0.3);
        box-shadow: 0 12px 25px rgba(15, 23, 42, 0.12);
        margin-bottom: 1rem;
    }
    .mbti-pill {
        display: inline-block;
        padding: 0.35rem 0.8rem;
        border-radius: 999px;
        background: #eef2ff;
        color: #3730a3;
        font-weight: 700;
        font-size: 0.85rem;
        margin-right: 0.4rem;
    }
    .tag-soft {
        display: inline-block;
        padding: 0.25rem 0.65rem;
        border-radius: 999px;
        background: #f3f4f6;
        color: #4b5563;
        font-size: 0.8rem;
        margin-right: 0.3rem;
        margin-top: 0.2rem;
    }
    .career-title {
        font-weight: 700;
        font-size: 1rem;
        margin-bottom: 0.1rem;
    }
    .career-desc {
        font-size: 0.9rem;
        color: #4b5563;
    }
    .footer-text {
        font-size: 0.8rem;
        color: #6b7280;
        margin-top: 0.8rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ===== 데이터: MBTI별 추천 진로 =====

CAREERS_BY_MBTI = {
    "INTJ": [
        ("전략기획자", "📊", "복잡한 문제를 구조화하고 장기 플랜을 세우는 데 강점이 있어."),
        ("연구원(사회·공학·자연)", "🔬", "깊이 파고드는 탐구력과 분석력이 잘 살 수 있는 진로야."),
        ("데이터 분석가", "🧠", "논리와 패턴을 좋아한다면 숫자로 말하는 직업도 어울려."),
    ],
    "INTP": [
        ("연구개발직(R&D)", "🧪", "새로운 개념·아이디어를 실험하고 검증하는 과정이 잘 맞아."),
        ("소프트웨어 개발자", "💻", "문제 해결과 시스템 설계를 좋아한다면 찰떡 진로."),
        ("학자/교수", "📚", "추상적인 개념을 다루고 이론화하는 일을 좋아하는 편이야."),
    ],
    "INFJ": [
        ("상담사/심리전문가", "🛋️", "사람의 마음을 깊이 이해하고 돕는 데 강점이 있어."),
        ("교사/교육자", "👩‍🏫", "학생의 성장 과정을 긴 안목으로 바라보고 지원해 줄 수 있어."),
        ("비영리단체 활동가", "🌱", "가치와 신념을 실천하는 일에 의미를 많이 느끼는 유형이야."),
    ],
    "INFP": [
        ("작가/콘텐츠 크리에이터", "✍️", "자신만의 스토리와 감성을 표현하는 데 강점이 있어."),
        ("예술가/디자이너", "🎨", "감수성이 풍부해서 예술적 표현에 잘 어울려."),
        ("아동·청소년 관련 직업", "🧸", "따뜻함과 공감 능력이 큰 힘이 되는 분야야."),
    ],
    "ISTJ": [
        ("공무원/행정직", "🏛️", "책임감 있고 꼼꼼한 성향이 행정 업무에 잘 맞아."),
        ("회계·재무 전문가", "📑", "숫자와 규칙을 다루는 안정적인 직무에 강점이 있어."),
        ("품질관리/감사", "🧾", "규정과 절차를 철저히 지키는 성향이 장점이 되는 일."),
    ],
    "ISFJ": [
        ("간호사/보건의료직", "🚑", "헌신적이고 성실한 성향이 환자를 돌보는 데 큰 힘이 돼."),
        ("교사/보육교사", "🍎", "학생·아이들의 일상을 세심히 챙기는 역할에 잘 어울려."),
        ("행정/지원 직무", "📂", "팀을 조용히 뒷받침하는 역할에서 안정감을 느끼는 편이야."),
    ],
    "ISTP": [
        ("엔지니어(기계·전기 등)", "⚙️", "손으로 만지고 직접 고치는 실용적인 문제 해결에 강해."),
        ("응급구조·소방 관련 직업", "🚒", "위기 상황에서 침착함과 행동력이 빛나는 유형이야."),
        ("IT 인프라/보안 엔지니어", "🛠️", "시스템을 세팅하고 유지·보수하는 일에 잘 어울려."),
    ],
    "ISFP": [
        ("그래픽/패션 디자이너", "🧵", "감각적인 미적 기준을 실제 결과물로 만드는 일을 좋아해."),
        ("작업치료사/재활 관련 직무", "🦴", "조용히 돕는 방식으로 타인을 지원하는 데 강점이 있어."),
        ("사진·영상 크리에이터", "📷", "순간의 분위기와 감정을 담아내는 표현력이 좋아."),
    ],
    "ENTJ": [
        ("경영자/사업가", "🏢", "목표를 세우고 사람들을 이끌며 추진하는 데 강점이 있어."),
        ("전략컨설턴트", "📈", "복잡한 문제를 구조화하고 해결 방안을 제시하는 일을 잘해."),
        ("조직 리더(팀장, 학교·기관 리더)", "🧭", "큰 그림을 보고 방향을 제시하는 역할에 어울려."),
    ],
    "ENTP": [
        ("스타트업/창업가", "🚀", "새로운 아이디어를 현실로 옮기는 걸 즐기는 편이야."),
        ("마케팅/브랜딩 기획자", "📣", "재치와 말발, 관찰력이 모두 활용되는 직무야."),
        ("기획 PD/예능·콘텐츠 기획자", "🎬", "다양한 사람·아이디어를 섞어서 새로운 걸 만드는 일에 강해."),
    ],
    "ENFJ": [
        ("교사/교육 리더", "🧑‍🏫", "사람을 성장시키고 팀 분위기를 이끄는 데 특화된 유형이야."),
        ("HR/인사 담당자", "🤝", "사람을 이해하고 적재적소에 배치하는 역할이 잘 맞아."),
        ("커뮤니티 매니저/코디네이터", "🫱🏼‍🫲🏽", "사람과 사람을 연결하고 네트워크를 만드는 일을 잘해."),
    ],
    "ENFP": [
        ("콘텐츠 크리에이터/유튜버", "📹", "아이디어와 에너지를 바탕으로 사람들에게 영감을 줄 수 있어."),
        ("광고·홍보·마케팅", "🎯", "사람의 마음을 사로잡는 메시지를 만드는 데 강점이 있어."),
        ("진로·청소년 상담/코치", "🧑‍🎓", "상대의 가능성을 발견하고 응원해 주는 역할이 잘 어울려."),
    ],
    "ESTJ": [
        ("경영관리/운영관리자", "📋", "조직과 시스템을 효율적으로 돌리는 데 특화되어 있어."),
        ("군·경찰·행정 관련 직무", "🛡️", "질서와 규칙을 지키는 환경에서 실력을 발휘해."),
        ("프로젝트 매니저(PM)", "🧱", "계획·실행·점검을 체계적으로 관리하는 역할이 강점이야."),
    ],
    "ESFJ": [
        ("교사/학급담임", "🏫", "사람들 사이의 분위기를 따뜻하게 만드는 능력이 뛰어나."),
        ("서비스·CS 관련 직무", "🤗", "친절함과 공감 능력이 곧 경쟁력이 되는 직업이야."),
        ("이벤트·행사 기획자", "🎉", "사람들이 함께 즐기는 자리를 만드는 데 재능이 있어."),
    ],
    "ESTP": [
        ("영업/세일즈 전문가", "💼", "즉흥적 대처와 말솜씨가 큰 무기가 되는 직무야."),
        ("스포츠·트레이너/코치", "🏋️", "몸으로 부딪히고 역동적인 환경에서 에너지가 살아나."),
        ("현장 중심 직무(건설·제조 등)", "🏗️", "현장에서 직접 보고 판단하는 일을 선호하는 편이야."),
    ],
    "ESFP": [
        ("연예·공연·엔터 분야", "🎤", "사람들 앞에서 에너지를 나누는 데 강점이 있어."),
        ("유아·초등 교육/방과후 강사", "🧩", "즐겁게 놀고 배우는 환경을 만드는 걸 잘해."),
        ("여행·관광 관련 직무", "🧳", "새로운 경험을 다른 사람과 공유하는 일을 즐기는 편이야."),
    ],
}

MBTI_LIST = list(CAREERS_BY_MBTI.keys())
MBTI_LIST.sort()


# ===== 레이아웃 =====

# 상단 타이틀 박스
st.markdown(
    """
    <div class="title-box">
        <div class="title-main">🎓 MBTI 기반 진로 상담실</div>
        <div class="title-sub">
            오늘의 나는 어떤 유형일까? <br>
            MBTI를 가볍게 참고해서, 나와 어울릴 수 있는 진로 아이디어를 함께 떠올려 보자 💡
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# 좌우 컬럼 레이아웃
left, right = st.columns([1.5, 1])

with left:
    st.markdown("### 1️⃣ 나의 MBTI를 선택해 주세요")

    selected_mbti = st.selectbox(
        "MBTI 유형",
        options=MBTI_LIST,
        index=MBTI_LIST.index("INFJ") if "INFJ" in MBTI_LIST else 0,
        help="최근 검사 결과나, 나와 제일 비슷하다고 느끼는 유형을 선택해도 괜찮아요 🙂",
    )

    st.markdown("---")
    st.markdown("### 2️⃣ 추천 진로 보기 버튼을 눌러 보세요")

    show = st.button("✨ 진로 추천 받기", use_container_width=True)

with right:
    st.markdown("### 💡 이 웹앱 활용 꿀팁")
    st.markdown(
        """
        - MBTI는 **정답이 아니라 ‘참고용 도구’**예요.  
        - “딱 한 가지”가 아니라, **어울릴 수 있는 여러 가능성**을 보는 데 초점을 맞춰 주세요.  
        - 마음이 끌리는 직업이 있다면  
          👉 *“왜 끌릴까?”*, *“어떤 점이 좋을까?”* 를 스스로 적어보면 좋아요. 📝
        """
    )

# ===== 결과 영역 =====

st.markdown("### 3️⃣ 결과 🎯")

if show:
    careers = CAREERS_BY_MBTI.get(selected_mbti, [])

    st.markdown(
        f"""
        <div class="card">
            <span class="mbti-pill">{selected_mbti}</span>
            <span class="tag-soft">진로 아이디어 3가지 추천</span>
            <div style="margin-top:0.6rem; font-size:0.95rem;">
                아래 직업들이 반드시 “운명의 직업”은 아니에요 😉<br>
                다만, <b>{selected_mbti}</b> 유형에게 자주 어울리는 특징과 강점을 바탕으로 고른
                <b>아이디어 리스트</b>라고 생각해 주세요.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    for title, emoji, desc in careers:
        with st.container():
            st.markdown(
                f"""
                <div class="card">
                    <div class="career-title">{emoji} {title}</div>
                    <div class="career-desc">{desc}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown(
        """
        <div class="footer-text">
        🧭 *추가 팁:*<br>
        이 결과를 가지고 담임 선생님, 진로 상담 선생님, 친구와 이야기를 나눠 보세요.<br>
        “나는 이 직업의 이런 점이 좋은 것 같아” 같은 문장으로 대화를 시작하면 좋아요 😊
        </div>
        """,
        unsafe_allow_html=True,
    )
else:
    st.info("위에서 MBTI를 고르고 **`✨ 진로 추천 받기`** 버튼을 눌러 보세요! 🙌")
