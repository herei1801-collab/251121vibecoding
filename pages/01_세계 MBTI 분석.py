import streamlit as st
import pandas as pd
import altair as alt

# 데이터 불러오기 (캐시)
@st.cache_data
def load_data():
    # CSV 파일 이름/경로는 필요에 따라 수정
    return pd.read_csv("countriesMBTI_16types.csv")

df = load_data()

st.title("🌍 MBTI별 국가 비율 탐색 웹앱")
st.write("MBTI 유형을 선택하면, 그 유형 비율이 **가장 높은 10개 국가**와 **가장 낮은 10개 국가**를 확인할 수 있어요.")

# MBTI 유형 리스트 (Country 열 제외)
mbti_types = [c for c in df.columns if c != "Country"]

selected_mbti = st.selectbox("MBTI 유형을 선택하세요", mbti_types)

# 선택한 MBTI 기준으로 정렬
sorted_df = df[["Country", selected_mbti]].dropna().sort_values(by=selected_mbti, ascending=False)

top10 = sorted_df.head(10)                     # 가장 높은 10개
bottom10 = sorted_df.tail(10).sort_values(     # 가장 낮은 10개 (다시 오름차순 정렬)
    by=selected_mbti,
    ascending=True
)

st.subheader(f"🔝 {selected_mbti} 비율이 가장 높은 10개 국가")

top_chart = (
    alt.Chart(top10)
    .mark_bar()
    .encode(
        x=alt.X(f"{selected_mbti}:Q", title=f"{selected_mbti} 비율"),
        y=alt.Y("Country:N", sort="-x", title="국가"),
        tooltip=[
            alt.Tooltip("Country:N", title="국가"),
            alt.Tooltip(f"{selected_mbti}:Q", title="비율", format=".2%")
        ],
    )
    .properties(
        width="container",
        height=400,
        title=f"{selected_mbti} 비율 상위 10개 국가"
    )
    .interactive()
)

st.altair_chart(top_chart, use_container_width=True)

st.subheader(f"🔻 {selected_mbti} 비율이 가장 낮은 10개 국가")

bottom_chart = (
    alt.Chart(bottom10)
    .mark_bar()
    .encode(
        x=alt.X(f"{selected_mbti}:Q", title=f"{selected_mbti} 비율"),
        y=alt.Y("Country:N", sort="x", title="국가"),
        tooltip=[
            alt.Tooltip("Country:N", title="국가"),
            alt.Tooltip(f"{selected_mbti}:Q", title="비율", format=".2%")
        ],
    )
    .properties(
        width="container",
        height=400,
        title=f"{selected_mbti} 비율 하위 10개 국가"
    )
    .interactive()
)

st.altair_chart(bottom_chart, use_container_width=True)
