import streamlit as st

# 页面基础设置
st.set_page_config(page_title="AI Cockpit Dashboard", layout="wide")
st.title("AI Cockpit for a Manufacturing Line")
st.markdown("Bringing together predictive maintenance and analytics.")

# ========= Exercise3 新增内容 =========
import pandas as pd
import matplotlib.pyplot as plt

# 模拟设备数据
data = pd.DataFrame({
    "设备名称":["电机A","轴承B","泵C","齿轮箱D"],
    "风险分数":[0.82,0.45,0.66,0.30]
})

# 滑块：风险阈值
threshold = st.slider("风险判定阈值", min_value=0.0, max_value=1.0, value=0.5)

# 统计数量
high_risk = len(data[data["风险分数"] >= threshold])
st.metric(label="高风险设备数量", value=high_risk)

# 绘制条形图
fig, ax = plt.subplots()
ax.bar(data["设备名称"], data["风险分数"])
ax.axhline(y=threshold, color="red", linestyle="--", label="风险阈值")
ax.set_ylabel("风险分数")
ax.legend()
st.pyplot(fig)
