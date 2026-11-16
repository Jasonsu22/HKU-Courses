# Discussion 1 — Idea & Plan Consultation · 准备包

> 时长：3–5 分钟口头 walkthrough，不需要 slides，可以带文档/草图。
> 目标：讲清楚 **story → 三个模块 → 怎么排 → 我们的问题**，并让 tutor 觉得「他们已经想过可行性」。

---

## 0. 30 秒速览（自己先记住）

**一句话 story**
> Everest 看起来是「去不去」一个决定，但数据显示它其实是四个出行前就能选的东西决定的：**哪一侧、哪个季节、哪条路线、多少支持与氧气**；历史还经历了明显的年代跃迁（1950s 22% → 2020s 89%）。

**产品路径**：History（背景）→ Routes（主探索）→ Your plan（把选择变成带不确定性的估计）。

**三个数字**：2,347 expeditions / 25,274 参与记录 / 1,479 次成功（63.0%）。

**我们已经做过的证据**：28 条数据核验 + 三个模块的可运行早期原型（不是 PPT 承诺）。

---

## 1. 4 分钟逐字稿（English，可直接照着说）

> 语速约 140–150 wpm，全文约 500 词。括号里是动作提示。

### 0:00–0:30 — The story

> Everest is usually framed as one decision: go or don't go. The records say something different. Between 1921 and 2024 there were 2,347 expeditions and 25,274 participation records, and the outcome depends heavily on four choices a climber makes **before** leaving: which side, which season, which route, and how much support and oxygen. Our project makes those choices explorable, and ends with an uncertainty-aware historical estimate instead of a single number.

### 0:30–1:15 — Module 1: history

> The first view is the historical baseline: what changed? Scale, seasonal mix, success, duration, team structure, oxygen and deaths. The headline is that 63% of Everest expeditions put someone on the summit, but that number hides a regime change — expedition success ran around 22% in the 1950s and 89% in the 2020s. Every rate carries its numerator, denominator and sample size, and a season-by-decade heatmap stops people reading isolated totals.

### 1:15–2:15 — Module 2: routes (the core)

> The second view is the one we consider the core: a route and situation explorer. You filter by side, season, period and route group, then compare south and north like-for-like on success, days from base camp to summit, team size, hired support, oxygen and deaths per thousand.
>
> Two design decisions matter. First, the source has no coordinates — no latitude, longitude or route geometry — so the route panel is an explicitly labelled schematic cross-section built from the campsite field. That is the fallback our proposal promised, not an invented map. Second, the 2026 spring aggregates from the Department of Tourism are shown as a separate layer and never merged into the historical microdata.

### 2:15–3:20 — Module 3: your plan

> The third view is personal. You describe a plan — age band, recorded sex, season, side, route group, team size, support and oxygen — and we show two things: what comparable historical climbing members actually did, and a regularised logistic regression estimate with a 95% bootstrap interval. It is benchmarked against a constant baseline and a side-by-season baseline, and we show calibration on a held-out 2020–2024 period. If the exact profile has fewer than ten comparable records, we return “insufficient evidence” rather than a confident number.

### 3:20–4:00 — Arrangement and feasibility

> The three views are arranged as one planning path — history, routes, your plan — in a single offline page with shared definitions and a data-and-methods panel. We have already run a 28-check audit of the dataset and prototyped all three views to test feasibility, so the risks we want to discuss are specific, not hypothetical.

### 4:00–4:45 — Questions（选 2–3 个问，见第 4 节）

> We would like your view on three things: whether the schematic route panel is acceptable instead of a georeferenced 3D view; whether a member-level personal estimate with expedition-level context fits what you expect from “recorded expedition summit success”; and how to handle a 2020–2024 test window that contains only 189 expeditions because of COVID.

---

## 2. 60 秒压缩版（如果对方时间紧）

> Everest planning is a choice of side, season, route, support and oxygen, and the historical record shows a regime change of more than 40 points in success. We are building one offline page with three linked views: history for context, a route explorer for like-for-like comparison, and a profile-based estimate with intervals and a calibration check. We have already audited the dataset — 28 checks, no wrong numbers — and prototyped the three views. Our main open questions are how much weight the map/3D layer carries in grading, and whether a member-level estimate is acceptable.

---

## 3. 他们问的 "what visualizations / how arranged" — 直接给这张表

| 模块 | 屏幕上的图 | 回答什么问题 | 编码选择 |
|---|---|---|---|
| **01 History** | 年度 expedition + 参与人次双面板 | 规模怎么变 | 条形 + 共用 x 的第二个面板，避免双 y 轴 |
| | 年代成功率 + 95% Wilson 区间 | 成功率真的变了吗 | 点/条 + 区间，n 写在图上 |
| | 季节 × 年代热力（counts / success） | 增长是哪个季节带来的 | 行列热力，n<5 淡化 |
| | BC→顶峰天数分布（p10/p25/中位/p75/p90） | 攀登变快了吗 | 区间条 + 中位线 |
| | 队员 vs 雇佣人员堆叠面积 | 队伍结构怎么变 | 两个量的堆叠面积 |
| | 氧气采用率、死亡人数与每千人死亡率 | 风险与依赖 | 折线 + 堆叠柱，比例单独标注 |
| **02 Routes** | 南/北六指标对比小倍数 | 同季节/同年代下两侧差多少 | 2×3 小倍数，统一 0–100% 或 max |
| | 路线族成功率（≥20 次） | 哪条线可靠 | 横向条 + n，按成功率排序 |
| | 营地海拔剖面（示意） | 爬升结构、营地被使用比例 | 海拔阶梯 + 节点 + 比例；明示 schematic |
| | 2026 春季独立卡片 | 现在怎么样 | 与历史分开的卡片，带来源 |
| **03 Your plan** | 概率 + 95% 区间 + 可比样本 | 这个计划历史上怎样 | 大数字 + 区间条 + 队列人数 |
| | 驱动因素（倍数） | 哪些选择在起作用 | 水平条，正负分色 |
| | 可比队列阶梯 | 换匹配规则结果怎么变 | 三行表格，高亮实际使用的一层 |
| | 校准图（2020–2024） | 模型可信吗 | 预测 vs 实际 + 45° 线 |

**版面**：单页、三个 tab、每屏一个模块；Module 2 顶部一条 filter bar；Module 3 左表单右结果；右上角 Data & methods。**联动**：Module 1 点年代 → 热力/时长联动；Module 2 筛选 → KPI、对比、路线族全部重算；Module 3 改任一输入 → 结果、区间、驱动、队列即时更新。

---

## 4. 要主动问的问题（按优先级，附「没答案时的默认做法」）

1. **地图/3D 在评分里的权重**
   > The dataset has no coordinates at all. Would a clearly labelled schematic elevation profile be acceptable for the route panel, or do you expect a MapLibre/3D layer as a scored deliverable?
   - 默认：继续用 schematic，并在报告里把它作为受数据限制的 fallback 写清楚。

2. **估计对象：member-level 还是 expedition-level**
   > Age and sex only exist at member level, so we estimate the chance that a member with this profile summits, and show expedition-level success as context. Is that acceptable, or should the estimate be strictly expedition-level?
   - 默认：member 为主 + expedition 为辅，两者都写进方法。

3. **2020–2024 测试集太小**
   > 2020 has only three expeditions because of COVID, so the test window has 189 expeditions. Would you prefer 2021–2024 or a rolling-origin evaluation?
   - 默认：报告里同时给 2020–2024 和 2021–2024，主结论用 rolling-origin。

4. **部署窗口与提案切分不一致**
   > We keep the proposed 1990–2014 / 2015–2019 / 2020–2024 split for evaluation, but refit the deployed model on 2005–2024 because 1990s success is a different regime. Is that acceptable practice for the project?
   - 默认：评估按提案，部署用近 20 年，写清楚理由。

5. **数据质量限制怎么写**
   > The member table's year field is wrong before 2000 and hired staff are only half-listed. We handle both at expedition level — would you like that documented as a limitation section, or as part of the contributions?
   - 默认：单独一节 “data provenance & limitations”，并把 28 条核验作为附录。

6. **2026 新闻层算不算 "current situation"**
   > We show the 2026 spring aggregates as a separate, clearly labelled layer. Is that enough for the “current situation” part, or do you expect more recent official data?
   - 默认：保持独立卡片 + 来源，不并入模型。

7. **交付与评分关注点**
   > Should the final deliverable stay a fully offline `index.html`, and where is the balance between interaction/visual design and model rigour in grading?
   - 默认：离线优先；两侧都做，但以「可解释 + 有不确定性」为主。

---

## 5. 可能被问到的问题 & 回答

| 他们可能问 | 回答要点 |
|---|---|
| Why not just one number? | 因为 2020–2024 与 1990s 的成功率差 40+ 点（expedition 48% → 89%）；给单点会假装精确，我们给区间 + 校准 + 可比样本。 |
| Is this causal? | 不是。全部是历史记录的关联；氧气在近年几乎是完美分离变量，系数不能读成因果。 |
| What is the hardest part? | 数据质量（成员表年份坏、雇佣人员只登记一半）+ 年代漂移下的校准。我们已经有核验和原型，风险是可控的。 |
| What will you cut if time is short? | 按 proposal 的优先级：先砍装饰性 3D、外部现状数据、数值预测的精细度；保留路线对比、分母、区间、解释。 |
| Why route families instead of route names? | 136 个原始名称太碎，单个名称 n<10；按起首归族后每个比例都有 20+ 样本，仍保留原始名称在 tooltip。 |
| How do you know the numbers are right? | 28 条核验：11,425 / 89,000 / 480 / 15,586 / 2,347 / 25,274 / 1921–2024 全部对上；撞号 expid、myear、hired 三个坑都写进了处理规则。 |
| What does the user actually decide with this? | 选侧别/季节/路线/支持/氧气；工具给的是「历史上类似的人做到了多少、区间多宽、样本多少」，不是保证。 |

---

## 6. 带什么、演示顺序

**带**：
- 笔记本，`everest-app/index.html` 直接用浏览器打开（离线，双击即可）
- 一页纸（`discussion_1_onepager.pdf`）：三个模块各 1 张缩略图 + 4 个数字 + 3 个问题
- 可选：`proposal_check/claim_checks.csv` 打印版（证明核验做过）

**演示顺序（如果对方让你现场看）**：
1. History → 指出 63% 与 2020s 89% 的对比（10 秒）
2. Routes → 切到 North / Autumn，展示同季节下南北差异与 n（20 秒）
3. Your plan → 默认档案 75% vs 精确队列 75.0%（587 人），再把氧气关掉看 insufficient/警告（20 秒）
4. Data & methods → 30 秒讲清口径与局限

---

## 7. 不要说的话

- ❌ “我们会做 3D 地形和真实地图” —— 数据没有坐标，先别提，等 tutor 明确要求再评估。
- ❌ “这个模型能预测你能否登顶” —— 说 “historical association / estimate”，不说 predict。
- ❌ “数据没问题” —— 我们恰恰发现了三个坑，主动说出来是加分项。
- ❌ 承诺所有模块都做完 —— 按 proposal 的优先级讲，留出 fallback。

---

## 附：现场 30 秒版（如果只给你半分钟）

> We turn Everest planning into three linked views: how the mountain changed, how the two sides and route families compare like-for-like, and what a described profile achieved historically — with intervals, calibration and an explicit “insufficient evidence” rule. The dataset has no coordinates, so the route panel is a labelled schematic; we have already audited the data and prototyped all three views. Our questions are about how much the map layer counts, and whether a member-level estimate is acceptable.
