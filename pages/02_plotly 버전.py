import streamlit as st
import pandas as pd
import plotly.express as px

# 페이지 기본 설정
st.set_page_config(
    page_title="MBTI by Country Explorer",
    layout="wide"
)

@st.cache_data
def load_data():
    # 같은 폴더에 있는 CSV 파일을 읽어옵니다.
    df = pd.read_csv("countriesMBTI_16types.csv")
    return df

df = load_data()

# MBTI 유형 리스트 (Country 컬럼 제외)
mbti_types = [col for col in df.columns if col != "Country"]

st.title("🌍 MBTI 유형별 국가 분포 시각화")
st.write("MBTI 유형을 선택하면, 그 유형 비율이 **가장 높은 10개 나라**와 **가장 낮은 10개 나라**를 Plotly 막대그래프로 보여줍니다.")

# MBTI 선택
selected_mbti = st.selectbox(
    "MBTI 유형을 선택하세요",
    mbti_types,
    index=mbti_types.index("INFJ") if "INFJ" in mbti_types else 0
)

st.markdown(f"### 선택한 MBTI 유형: **{selected_mbti}**")

# 선택한 MBTI 기준으로 정렬
sorted_df_desc = df.sort_values(by=selected_mbti, ascending=False)
sorted_df_asc = df.sort_values(by=selected_mbti, ascending=True)

top10 = sorted_df_desc.head(10).copy()
bottom10 = sorted_df_asc.head(10).copy()

# 퍼센트 표시용 컬럼 추가 (0.0463 → 4.63%)
top10["percentage"] = top10[selected_mbti] * 100
bottom10["percentage"] = bottom10[selected_mbti] * 100

# ---------- 상위 10개 나라 그래프 ----------
st.subheader(f"🔼 {selected_mbti} 비율이 가장 높은 10개 나라")

top10_display = top10.sort_values(by=selected_mbti, ascending=True)  # 막대가 낮은 → 높은 순으로 보이도록

fig_top = px.bar(
    top10_display,
    x="Country",
    y=selected_mbti,
    title=f"Top 10 Countries for {selected_mbti}",
    labels={
        "Country": "국가",
        selected_mbti: f"{selected_mbti} 비율"
    },
    hover_data={
        "Country": True,
        selected_mbti: False,
        "percentage": ":.2f"
    }
)

fig_top.update_traces(
    hovertemplate="<b>%{x}</b><br>" +
                  f"{selected_mbti} 비율: %{customdata[0]:.2f}%"
)

# 위에서 hovertemplate에 쓸 customdata 설정
fig_top.update_traces(customdata=top10_display[["percentage"]].to_numpy())

fig_top.update_layout(
    xaxis_tickangle=-45,
    margin=dict(l=40, r=40, t=60, b=80)
)

st.plotly_chart(fig_top, use_container_width=True)

# ---------- 하위 10개 나라 그래프 ----------
st.subheader(f"🔽 {selected_mbti} 비율이 가장 낮은 10개 나라")

bottom10_display = bottom10.sort_values(by=selected_mbti, ascending=True)

fig_bottom = px.bar(
    bottom10_display,
    x="Country",
    y=selected_mbti,
    title=f"Bottom 10 Countries for {selected_mbti}",
    labels={
        "Country": "국가",
        selected_mbti: f"{selected_mbti} 비율"
    },
    hover_data={
        "Country": True,
        selected_mbti: False,
        "percentage": ":.2f"
    }
)

fig_bottom.update_traces(
    hovertemplate="<b>%{x}</b><br>" +
                  f"{selected_mbti} 비율: %{customdata[0]:.2f}%"
)

fig_bottom.update_traces(customdata=bottom10_display[["percentage"]].to_numpy())

fig_bottom.update_layout(
    xaxis_tickangle=-45,
    margin=dict(l=40, r=40, t=60, b=80)
)

st.plotly_chart(fig_bottom, use_container_width=True)

# ---------- 선택한 MBTI 수치 간단 표 ----------
with st.expander("📊 원자료 일부 보기 (선택한 MBTI 기준 상·하위 10개 나라)"):
    st.write("**상위 10개 나라**")
    st.dataframe(
        top10_display[["Country", selected_mbti, "percentage"]]
        .rename(columns={"percentage": "percentage(%)"})
        .reset_index(drop=True)
    )
    st.write("**하위 10개 나라**")
    st.dataframe(
        bottom10_display[["Country", selected_mbti, "percentage"]]
        .rename(columns={"percentage": "percentage(%)"})
        .reset_index(drop=True)
    )
