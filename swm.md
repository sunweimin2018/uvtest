
用streamlit生成仪表盘（dashboard）
将 Jupyter 笔记本转成专业 Streamlit 仪表盘，含布局、KPI、Plotly 图表、日期筛选、趋势颜色


仪表盘规范
 布局
顶部：标题左、日期筛选右
 KPI 行：4 卡（总营收、月增、AOV、订单数）
 图表：2×2 Plotly
底部：2 卡（平均配送时间、评分星级）

样式
趋势：红负绿正，保留两位小数
 Y 轴：$300K 格式
 卡片等高，不用图标