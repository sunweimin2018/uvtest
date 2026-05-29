---
name: streamlit-dashboard
description: 将 Jupyter 笔记本转成专业 Streamlit 仪表盘。含布局、KPI、Plotly 图表、日期筛选、趋势颜色。当用户要求将 notebook 转成仪表盘、创建 dashboard、或生成 Streamlit 数据看板时使用。
---

# Streamlit Dashboard 生成器

将 Jupyter 笔记本转成专业 Streamlit 仪表盘。

## 布局规范

```
┌─────────────────────────────────┐
│  标题（左）      日期筛选（右）  │  ← 顶部行
├─────────────────────────────────┤
│  营收 KPI │ 月增 │ AOV │ 订单数  │  ← KPI 行：4 卡
├─────────────────────────────────┤
│   图表 1        │   图表 2      │
│                 │               │  ← 2×2 Plotly 图表
├─────────────────┼───────────────┤
│   图表 3        │   图表 4      │
├─────────────────┼───────────────┤
│ 平均配送时间     │  评分星级      │  ← 底部：2 卡
└─────────────────────────────────┘
```

## KPI 卡片

- **总营收** — 累计营收金额
- **月增** — 月度增长率（百分比）
- **AOV** — 平均客单价
- **订单数** — 总订单量

## 图表（2×2 Plotly）

使用 Plotly Express 或 graph_objects 绘制，响应式交互。

## 底部卡片

- **平均配送时间** — 数值 + 趋势
- **评分星级** — 平均评分 + 趋势

## 样式规则

### 趋势颜色
- 正值（涨）：<span style="color:green">绿色</span>
- 负值（跌）：<span style="color:red">红色</span>
- 保留两位小数

### Y 轴格式
- 使用 `$300K` 格式（缩写千/百万）
- 通过 Plotly tickformat 或自定义 formatter 实现

### 卡片
- 所有卡片**等高**，使用 `st.metric` 或自定义 CSS
- **不使用图标**（如 emoji 或 icon）

## 实现要点

1. 从 Jupyter notebook 中提取数据处理逻辑
2. 用 `st.columns()` 控制布局
3. KPI 卡片用 `st.metric(label, value, delta)`
4. 图表用 `st.plotly_chart()` 嵌入
5. 日期筛选用 `st.date_input()` 放在标题右侧
6. 自定义 CSS 确保卡片等高
