import streamlit as st

# 页面配置
st.set_page_config(page_title="Ziqi's Command Center", layout="wide")

st.title("🚀 Ziqi's Command Center")
st.markdown("---")

# 创建三列布局
col1, col2, col3 = st.columns(3)

with col1:
    st.header("🏫 Academic & Career")
    st.page_link("https://canvas.eee.uci.edu/", label="UCI Canvas", icon="📚")
    st.page_link("https://scholar.google.com/", label="Google Scholar", icon="🎓")
    st.page_link("https://github.com/", label="GitHub", icon="💻")
    st.page_link("https://www.overleaf.com/", label="Overleaf", icon="📝")

with col2:
    st.header("📊 Data Science Tools")
    st.page_link("https://console.cloud.google.com/", label="GCP Console", icon="☁️")
    st.page_link("https://chat.openai.com/", label="ChatGPT / Claude", icon="🤖")
    st.page_link("https://www.datacamp.com/", label="DataCamp", icon="🐍")
    st.page_link("https://gemini.google.com/", label = "Gemini", icon = "✨")

with col3:
    st.header("🎮 Hobby & Life")
    st.page_link("https://www.padi.com/", label="PADI", icon="🛠️")
    st.page_link("https://store.steampowered.com/", label="Steam", icon="🕹️")
    st.page_link("https://www.bilibili.com/?spm_id_from=333.788.0.0", label="Bilibili", icon="🍱")

# 极客彩蛋：加一个简单的当日心情数据可视化或待办清单
st.sidebar.title("System Status")
st.sidebar.info("Current Program: UCI MSBA 2026")
st.sidebar.progress(65, text="MSBA Progress") # 进度条