import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Wedge

plt.rcParams["font.sans-serif"] = ["Noto Sans SC", "Microsoft YaHei", "SimHei"]
plt.rcParams["axes.unicode_minus"] = False

fig, ax = plt.subplots(figsize=(12, 12))
ax.set_facecolor("#fdf8f0")
fig.patch.set_facecolor("#fdf8f0")

rings = [
    {"r0": 0.0, "r1": 2.0,
     "colors": ["#e8c4a0", "#f0d4b8", "#e8b890", "#eccca8", "#e8c4a0", "#f0d4b8"],
     "labels": ["策略 A", "策略 B", "策略 C", "策略 D", "策略 E", "策略 F"]},
    {"r0": 2.0, "r1": 3.0,
     "colors": ["#d4a878", "#e8c098", "#d4a878", "#e8c098", "#d4a878", "#e8c098"],
     "labels": ["产品 A", "产品 B", "产品 C", "产品 D", "产品 E", "产品 F"]},
    {"r0": 3.0, "r1": 4.0,
     "colors": ["#c09068", "#d8b088", "#c09068", "#d8b088", "#c09068", "#d8b088"],
     "labels": ["区域 A", "区域 B", "区域 C", "区域 D", "区域 E", "区域 F"]},
]

n = 6
angle = 2 * np.pi / n
start = -np.pi / 2

for ring in rings:
    r0, r1 = ring["r0"], ring["r1"]
    for i in range(n):
        t0 = start + i * angle
        t1 = start + (i + 1) * angle

        w = Wedge(
            (0, 0), r1, np.degrees(t0), np.degrees(t1),
            width=r1 - r0,
            facecolor=ring["colors"][i],
            edgecolor="white", linewidth=2.5,
        )
        ax.add_patch(w)

        # 文字沿圆弧顺时针排列，居中紧凑显示
        t_mid = (t0 + t1) / 2
        r_mid = (r0 + r1) / 2
        label = ring["labels"][i]
        chars = list(label)
        n_chars = len(chars)

        fs = {0.0: 10, 2.0: 12, 3.0: 14}.get(r0, 12)

        char_angle = np.radians(4.5)          # 紧凑间距，仅保留弧度感
        total_span = (n_chars - 1) * char_angle
        start_arc = t_mid - total_span / 2    # 整体居中

        for j, ch in enumerate(chars):
            theta = start_arc + j * char_angle
            cx = r_mid * np.cos(theta)
            cy = r_mid * np.sin(theta)
            rot = np.degrees(theta) + 90      # 切线方向

            ax.text(
                cx, cy, ch,
                ha="center", va="center",
                fontsize=fs, fontweight="bold",
                color="#4a3020",
                rotation=rot,
            )

ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect("equal")
ax.axis("off")
ax.set_title("三层环形分布图", fontsize=22, fontweight="bold", color="#4a3020", pad=18)

plt.tight_layout()
plt.savefig("c:/Users/swm/Desktop/uvtest/aaa_output.png", dpi=150, bbox_inches="tight",
            facecolor="#fdf8f0")
print("图表已保存至 aaa_output.png")
