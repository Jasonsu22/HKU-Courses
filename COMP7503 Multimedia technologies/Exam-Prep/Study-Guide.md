# COMP7503 Multimedia Technologies：第 1–5 次课完整复习讲义

> 版本：2026-10-19 重写版。用途：先读懂每个概念、原理和例子，再用配套 A4 双面速查页回忆答案。本文按课件与主题编排，含中文详解、英文简答表述、计算过程、易错辨析及逐页覆盖记录。

## 0. 阅读范围、考务和资料依据

### 0.1 本次究竟整理了什么

本次按你指定的“第 1–5 次讲课”复习需求，对照 **S01–S05 五份知识课件，共 231 个 PDF 物理页**，并结合当前已导出的 **8 段课堂原始转写**重写。不是把自动纪要再次缩写；定义、原理、比较、流程、计算和课堂案例均在对应章节展开。篇章编号是知识组织顺序，**课件编号、讲义章号与课表 Lecture 编号不是严格一一对应**；一次课堂会跨多个课件。

纳入的课件是 Introduction（35 页）、Elements of Multimedia Computing（22 页）、Example Applications（63 页）、Media Sensor and Reproduction 1（49 页）、Media Sensor and Reproduction 2（62 页）。课程信息 S00 用于核对考务，不计入 231 页。S06 Multimedia Documents 不作为这次指定范围的主体；第一、二份课件里已经涉及的多源同步、系统组织等基础概念仍完整保留。

**资料缺口必须保留：**课表前五次日期为 9 月 3、10、17、24 日和 10 月 8 日；现有录音只覆盖后四个日期，未找到 9 月 3 日录音。10 月 8 日录音从语音识别相关内容中途开始，S05 p.2–11 的扬声器等内容有完整课件，但未找到相应现场讲解段。仅有课件视频链接、缺少可核实画面或转写的演示，不虚构视频细节。本文据此可做到对**已取得课件的逐页知识覆盖**，不能把缺失录音中的未知话语声称为已全部恢复。

### 0.2 考务事实与“可能考点”分开看

- S00 PDF p.13 的考核结构是：Final Examination 50%；In-Course Assessment 共 50%，其中 Written Assignment 10%、Quiz 20%、Programming Assignment 20%。**Quiz 的 20% 是课程总评的 20 个百分点，不能再乘一次 50%。**旧版“平时评估中的 20%”容易造成误解，已更正。
- S00 PDF p.16 将 **2026 年 10 月 22 日（周四）**列为 Quiz & Programming Tutorial。T08 01:27:37 附近老师说先进行约一个半小时 Quiz，随后教程；实际安排以 Moodle/教师通知为准。
- T08 00:05:02 附近老师说明 cheat sheet 可打印或手写、尺寸限制 A4。**本次根据你补充确认的规则，按一张 A4 正反两面制作速查版。**完整讲义保留所有详细解释，双面页压缩为考场查询和答案提示。
- 已找到的资料没有一句可以据以断言“官方书面 Quiz 范围就是某几页”。本文的范围是你指定的前五次课与 S01–S05；各节“可直接答”“复习重点”是根据材料组织的答案模板，**不是老师公布的考题或保证会考的题目**。

### 0.3 如何用这份长文档

第一遍按第 1–6 章读原理：每节先知道它解决什么问题，再记住输入、处理步骤和输出，最后理解限制。第二遍做第 7 章计算题，确认自己能写出公式、代入单位并解释结果。第三遍用第 8 章问答查漏补缺，最后把不熟的内容在 A4 双面页上标出。

英文答题段可用作表达框架，不需要逐字背诵。简答题通常按“定义 → 原理/流程 → 例子或比较 → 限制”组织；计算题按“已知量 → 单位换算 → 公式 → 代入 → 结果/假设”组织。不要只写一个英文缩写或几个技术名词。

### 0.4 来源编号和页码规则

`[Sxx PDF p.x–y]` 一律表示 PDF 阅读器从 1 开始数的物理页码，不一定等于页脚印刷号。`[Txx 时间]` 为原始录音转写段落中的时间戳；ASR 长段只能用已有段首定位，不伪造逐句话语时间。“理解补充”表示为讲清机制而添加的标准背景，不意味着老师逐字讲过。

- S00：00 - Course Information.pdf，20 页。
- S01：01 - Introduction.pdf，35 页。
- S02：02 - Elements of Multimedia Computing.pdf，22 页。
- S03：03 - Example Applications.pdf，63 页。
- S04：04 - Media Sensor and Reproduction - 1.pdf，49 页。
- S05：05 - Media Sensor and Reproduction - 2.pdf，62 页。
- T01：9 月 10 日 19:01，多媒体-01，43 分 42 秒。
- T02：9 月 10 日 19:59，多媒体-02，36 分 42 秒。
- T03：9 月 10 日 20:36，多媒体-03，23 分 58 秒。
- T04：9 月 10 日 21:10，多媒体-04，29 分 51 秒。
- T05：9 月 17 日 19:01，多媒体-01，52 分 30 秒。
- T06：9 月 17 日 20:05，多媒体-02，1 小时 18 分 19 秒。
- T07：9 月 24 日 19:00，多媒体-01，2 小时 17 分 42 秒。
- T08：10 月 8 日 19:45，多媒体-01，1 小时 28 分 30 秒。

自动会议纪要用于辅助定位和检查主题；知识判断以课件、原始转写和必要的技术纠错为依据。ASR 中把 candela 听成 camera、把 CMOS 听成 Simons 等情况，本文使用课件中的正确术语；原始转写文件继续保留原貌。

### 0.5 目录

1. Introduction：多媒体定义、通信演进、体验式环境、同步多源系统。
2. Elements：经验、信息、知识、感知循环、语义鸿沟、系统模块。
3. Example Applications：音频、图像、视频增强，检测、识别、重建与检索，DIKW。
4. Sensors & Digitization：传感器、限制、波、采样量化、声音、麦克风。
5. Sound Reproduction, Speech & Music：扬声器、空间听觉、语音、乐音与合成。
6. Light, Imaging & Vision：光学计量、成像、相机、显示、人眼、颜色。
7. 计算专题：完整公式、单位、代入过程与结果。
8. 综合简答与辨析：可直接参考的答案结构。
9. 资料清单、录音定位和最终核对。

## 1. Introduction：多媒体计算到底在解决什么问题

### 1.1 Multimedia 的定义：为什么“有音乐、有图片”不是完整答案

**是什么。** 多媒体（multimedia）是把多种媒体结合起来，通过一种或多种感觉通道，向使用者传达与任务有关的信息。常见媒体包括文字、图形、照片、声音、动画和视频；它们可以刺激视觉、听觉，也可以扩展到触觉、嗅觉和味觉。注意，“多种媒体”不等于“必须同时刺激多种感官”：文字和照片都主要作用于视觉，但仍是不同媒体形式。

**为什么需要组合。** 每个感官和每个媒体只揭示现实的一部分。录到一句话的声音，可能听得见语气，却看不到谁在什么场景说；只有文字，也容易丢失语气、动作和场景。课件用一句容易引起误解的指令作例子，补上“说话者是牙医”的背景后，读者才会按检查牙齿的场景解释。结论不是媒体数量越多越好，而是要补齐任务需要、单一媒体没有提供的证据。

**为什么音视频最常见。** 人类对视觉和听觉信号的分析能力很强，日常活动也大量依靠它们。相机、麦克风、显示器和扬声器已经能较方便地采集和再现这两类信号，因此现有多媒体系统多围绕音视频构建。课件认为味道、气味和触觉较难采集和再现；应理解为实现难度和普及程度的差异，不应写成它们绝对不能数字化。

**可直接用于简答。** “Multimedia combines several media to deliver relevant information through one or more sensory modalities. A single medium provides only partial evidence, whereas complementary media can reduce ambiguity and communicate an event more completely. For example, text describing an instruction becomes much clearer when the associated visual scene and context identify the speaker as a dentist.”

来源：[S01 PDF p.2–7]。p.3 是演示视频引导页；这里只保留其‘单靠音频是否足够’的教学问题，不臆测视频中未提供的细节。

### 1.2 Computing 与 multimedia computing：从信号走向有关的信息

**Computing 是什么。** 本课把计算理解为借助或创造计算机器完成有目标的活动，而不是只做算术。系统可以进行采集、存储、压缩、传输、分析、选择和呈现；这些步骤都应服务一个任务。

**Multimedia computing 做什么。** 它利用不同传感器产生的信号，把与当前问题有关的部分整合起来，并选择合适的媒体呈现给用户。两个目标是：分享经验中的信息，以及从经验中提取知识。录音录像是资料采集；把声音和课件对齐、找到老师解释某概念的片段、让学生据此理解课程，才体现信息组织和任务目标。

**媒体与模态。** Media 强调信息承载形式，例如文本、图像和视频；sensory modality 强调感觉通道，例如视觉、听觉。**理解补充：** 视频流也可以只含图像序列；日常所谓“视频文件”常把视频轨和音频轨放在同一容器中。不能据此把“视频”严格定义为“声音加图像”。

**可直接用于简答。** “Multimedia computing acquires signals from multiple sources, integrates and processes the relevant evidence in the context of a task, and presents useful information through suitable media. Its goals include sharing experiences and extracting knowledge from them. Its output should be relevant information or insight, rather than merely an unorganized collection of files.”

来源：[S01 PDF p.8、32–34]。

### 1.3 传播的三个维度：time、space、addressee invariance

本课用三个问题比较通信技术：信息能否跨越**时间**保存和重放，能否跨越**空间**传到远处，能否扩大或改变**接收者（addressee）**的范围。这里 invariance 是摆脱某种时空或受众限制的教学说法，并不表示技术传输完全无损、没有延迟。

1. **Across time：跨时间。** 录音、文字和照片让事件结束后的人仍能接收其记录。课堂录像使缺席者后来复习，是时间分离；存储介质、编码格式和可用的播放设备是支撑技术。
2. **Across space：跨空间。** 电话、无线电、网络会议让不同地点的人交流。需要信号编码、通信信道和接收端；发送纸质信件也能跨空间，但速度与实时通信不同。
3. **Across addressees：面向更多接收者。** 印刷、广播和网络发布降低把同一内容送到多人手中的成本。它既涉及分发规模，也涉及接收者能否按自己的兴趣选择内容。

**答题方法。** 比较一项发明时，先写它把什么信号变成什么可传播形式，再分别判断“能不能保存到以后、能不能送到远处、能不能让很多人接收”。不要只背“电话是 space”而忘记理由：传统电话延伸了自然语音交流的距离，但本身不自动产生可供未来重放的持久记录。

来源：[S01 PDF p.9–16]。

### 1.4 通信技术的发展：每一种发明消除了什么限制

**口语（spoken language）。** 人用发声器官产生连续声音，以共同语言描述复杂事实。在没有录音和远程信道时，说话者与听者通常需要处在相近时间和空间，传播范围有限。它天然、直接，但声音瞬时消失。

**文字（written language）。** 由图画等表达形式发展而来，把语言和经验描述保存为符号，因此信息可以超过人的当下记忆和寿命继续存在。早期石板笨重；纸和墨提高便携性，进而使记录更容易跨地点传递。关键变化是从转瞬即逝的声音变成持久、可运输的记录。

**印刷（printing）。** 可重复复制文稿，使相同信息可以大规模分发，降低抄写成本并提高一致性。课件以约1440年的 Gutenberg 印刷术作历史例子；理解上重点是机械复制与大众传播的关系。这不是“人类最早印刷技术”的全球史断言。

**电报（telegraph）与电话（telephone）。** 电报把符号信息编码为适合远距离信道的信号，显著缩短消息传递时间；电话把自然语音送往远方，使双方不必先把每句话改写为文字。课件把两者的主要突破归为跨空间。电报是否保留纸带、电话是否另行录音属于附加存储功能。

**广播（radio）。** 用无线方式把声音同时送给大量接收者，突破接收者规模的限制，适合实时大众传播。**电影和电视（movies and television）**共同调动视听，提供更自然、容易引起情感反应的场景。电影中的内容预先记录，可重复放映；电视的典型历史角色是跨地域实时广播，录制后才同时具备后续重放能力。

**记录介质、数字媒体和网络。** 磁带、光盘、硬盘等让声音和影像能保存、复制和分发；数字化进一步使机器能编辑、增强、搜索和分析这些记录。分发可通过实体副本、线路复制和 Internet 完成。Internet 除了扩大传播范围，也让接收者搜索、点播和个性化选择内容，因此受众可以主动探索信息。

**考试答案骨架。** “Communication technology progressed by reducing constraints on time, space and audience. Writing and recording preserve information across time; telegraphy and telephony extend it across space; printing and broadcasting increase the audience. Digital media enable machine processing, while the Internet combines remote distribution with interactive and personalized access.”

来源：[S01 PDF p.10–16]。

### 1.5 计算机何时成为日常多媒体设备：瓶颈与变化

**1960年代的例子。** 课件用 IBM 1620 说明早期计算机庞大、存储很小、输入输出依靠纸带或穿孔卡，软件以汇编和 Fortran 为例；某些算术通过查表实现。重要的是其资源和交互形式距离今天的连续音视频处理很远。具体机型细节是历史背景，不能推成“所有早期计算机都没有算术单元”。

**1990年代之前。** 大规模普及音视频计算受到四方面共同限制：CPU处理能力、存储容量、网络带宽、处理算法。即使传感器可以采到信号，计算机也可能装不下、来不及处理或传不出去。课件以低主频CPU、小内存、小硬盘、低分辨率和有限颜色的PC作说明，应用大多仍以文本为主。

**1990年代初到中期。** CPU、内存、图形模式和硬盘改善，加上声卡、CD-ROM和音视频软件，使声音、图像和游戏成为PC常见能力。课件以386/486、Pentium、Windows 95、立体声音频和播放器等列出阶段性变化。重点是硬件、软件和分发介质一起成熟，而不是某一CPU单独“发明了多媒体”。

**1990年代末和21世纪。** 当多媒体成为电脑标配，厂商不必再特意标注“multimedia computer”，但语音、音频、图像和视频的处理、压缩、识别研究继续发展，电话、广播和娱乐推动了研究。移动设备又把摄像、录音、显示、网络和多种传感器带到用户身边，形成随时采集、随地交流的系统。

**可直接用于简答。** “Multimedia became practical through joint advances in processing power, memory and storage, communication bandwidth, algorithms and software. Early machines could not economically handle the size and real-time demands of audio and video. As these constraints weakened, multimedia became standard on PCs and later on mobile devices.”

**史例限定。** 课件中“before 1990s”的规格是示例，不是整个年代所有机器的上限；‘移动设备替代PC’是发展趋势的概括，不是说PC已不存在。p.20正文与图片对同一Presario机器的品牌写法不一致，复习不应把该品牌冲突记作知识点。

来源：[S01 PDF p.17–22]。

### 1.6 移动设备的多传感器：各自提供什么证据

手机不只是缩小的电脑。相机采集光形成图像和视频，麦克风采集声压变化，GPS提供地理定位，磁力计支持方向估计，加速度计测量加速度，陀螺仪测量角速度。接近传感器可判断物体是否靠近，环境光传感器用于亮度适配；某些设备还提供气压、温湿度等读数。触摸屏采集触点和手势，指纹传感器获取指纹特征供身份相关任务使用。

**为什么要组合。** 单独GPS可能知道位置但不知道用户面向何方；组合定位、方向和相机信息，才能支持更有意义的导航和增强现实。加速度计与陀螺仪对姿态估计提供互补证据；仅有相机画面则不能直接等同于可靠的运动状态。与人类感官相比，设备能直接测量部分人类不擅长精确测量的量，例如经纬度，但这些读数本身还需要解释。

**理解补充：图中的类别要分清。** 课件示意图把 Bluetooth、NFC 和 voice processor 也画在手机周围。Bluetooth、NFC首先是通信技术，voice processor是处理模块，不应把图上的每一项都机械地称为“物理传感器”；图中也不意味着每一部手机都具备温湿度传感器。

**可直接用于简答。** “A mobile multimedia device combines capture, sensing, computation, communication and presentation. Cameras and microphones capture visual and acoustic content; GPS and inertial sensors provide location and motion context. Integrating complementary measurements supports tasks such as navigation that cannot be solved reliably using one signal alone.”

来源：[S01 PDF p.22–24；p.23传感器图已核看]。

### 1.7 应用如何推动技术：需求、数据和设备共同演化

课件把计算机发展串成一条应用推动技术的链：数值运算要求算术处理能力；商业数据处理推动文字数字处理、数据库与服务器；文档、电子表格、邮件和WWW推动个人电脑、图形交互和联网；社交、摄影、即时聊天和分享推动移动通信、音视频处理和地理位置服务。

这条链的含义是：系统能力应由要解决的任务反推。视频分享不仅需要相机，还需要压缩、存储、无线带宽和播放；导航不仅需要GPS，还要道路数据、路径计算和适合驾驶者理解的输出。课件把“未来应用、未来技术、未来设备”留作开放问题，不能把某一产品预测写成已经确定的课程结论。

**可直接用于简答。** “Applications drive computing technology by imposing new data, processing and interaction requirements. Numerical computation emphasized arithmetic; business systems emphasized structured data and databases; multimedia sharing emphasized sensing, compression, networking and mobile devices. A multimedia design should therefore begin with the application objective and derive the required technologies.”

来源：[S01 PDF p.24]。

### 1.8 新应用的五个特点：为什么不能只查一张静态表

**第一，时空数据与实时流是常态。** 数据不仅有数值，还在何时、何地产生，并持续变化，例如公交位置、交通视频、温湿度序列。分析时忽略时间戳，可能把不同瞬间的观测错拼成同一状态。

**第二，关注事件的整体。** 孤立的一帧、一次温度测量、一条订单记录都只是局部。系统需要关联多个来源，判断完整事件和情境，例如“道路拥堵”应结合车速、位置、时间和画面。

**第三，用户要的是信息与洞察。** 用户通常想知道“哪里堵、我该走哪条路”，不想逐个查看设备原始数据。结果应尽可能不要求用户理解每种数据格式和传感器来源，但系统内部仍必须保留来源与可靠性以正确解释证据。

**第四，只有相关信息才有价值。** 传更多数据并不等于帮助更大。相关性取决于用户当前任务和上下文，学习者想找某公式的推导时，应该展示对应讲解与板书，而不是整节课所有画面。

**第五，探索式浏览很重要。** 用户可以先看整体，再放大某地区、选择某时段、跟进某事件，逐渐形成问题；这与要求用户一开始就写好精确关系查询不同。课件说它是新应用的重要交互方式，并不表示SQL或数据库查询不再有用。

**可直接用于简答。** “Emerging applications involve live spatiotemporal streams, require a holistic view of events, and prioritize task-relevant insights over isolated media. They support exploratory browsing because users often refine their interests while interacting with the data. Therefore, systems must correlate multiple sources and present useful information in context.”

来源：[S01 PDF p.25–26]。

### 1.9 电商的三个问题：数据的变化性与期待的计算结果

课件以三个电商问题说明“有数据库”不等于“已定义好计算任务”。**某两个地区之间处理了多少订单**，通常是给定地区、时间范围和业务口径后的统计计数；如果不限定时间，“多少”就没有稳定含义。**世界哪些地区销售增长快**，需要比较不同时段的销售值，可能还要按人口、基数或季节归一化，输出地区分布和增长趋势。**现在最热门的商品是什么**，则需要先定义“热门”是销量、收入、搜索、增长速度还是综合指标，并持续更新。

三者的区别在于：数据随时间更新的速度、是否要结合多个维度、结果是数值还是趋势/排序、是否需要实时洞察。**理解补充：** “增长快”可能指绝对增量，也可能指增长率，小基数商品增长率高不等于总销量最大；这正说明系统必须理解问题的语义和上下文，不能仅返回一堆记录。

**可直接用于简答。** “An order-count query produces a value for a defined region and time interval. A growth query compares periods and regions to reveal change. A ‘hottest item now’ query requires an explicit popularity criterion and up-to-date data. The expected result and the temporal nature of the information determine the processing and presentation required.”

来源：[S01 PDF p.26–27；增长率/指标口径说明为理解补充]。

### 1.10 Experiential environment：让人直接感知并探索数据

**定义。** 体验式环境（experiential environment）让用户直接运用感觉观察与一个事件有关的数据和信息，并根据自己在该事件中的兴趣自然地交互。目标是改善 human-machine synergy：人擅长概念、感知和情境判断，计算机擅长大量、重复、精确的数学与逻辑处理，两者的长处应在一个任务中配合。

**特征一：Direct and intuitive。** 用户能迅速理解所呈现的事件整体，并通过熟悉的操作继续探索，而不必先学习大量陌生命令。课件举滑动照片、点按图标和Kinect身体交互。关键是动作与任务结果之间容易建立联系；“有图形界面”本身不能保证直观。

**特征二：Same query and presentation spaces。** 用户在看结果的同一环境里表达查询或修改，修改后立即看到新的关系。电子表格是例子：用户直接改表内某个数，公式结果与图表随之变化。这里课件借用 WYSIWYG 强调查询和呈现的一致性；它不只意味着打印结果与编辑画面相似。

**特征三：Consider user state and context。** 系统考虑用户的任务、已有知识、所处情境和当前状态，让感知分析与探索更容易。游戏组合音频、视频和触觉反馈，把操作与事件放在一致的虚拟环境里。**理解补充：** 驾驶导航应考虑用户正在开车，优先提供及时、简洁的语音与路线提示，不能用需要长时间阅读的复杂表格。

**可直接用于简答。** “An experiential environment enables users to observe and explore event-related information directly through their senses. It should be direct and intuitive, keep query and presentation in the same interaction space, and account for user state and context. This combines human perceptual and conceptual abilities with computer processing, improving human-machine synergy.”

来源：[S01 PDF p.28–32；导航例子为理解补充]。

### 1.11 多媒体计算的形式化框架：S、M、F 各是什么

假设物理环境中有多个传感器，产生同步的数据流 **S₁,…,Sₙ**；这些流可以属于 **K种数据类型**，例如图像序列、音频和运动探测器读数。注意，传感器/数据流数量 n 与数据类型数量 K 不相同：多台相机可以提供多个流，但都属于视觉类型。

每条流带有 **Mᵢ（metadata）**，如时间、地点、设备参数和人工注释。系统从第i条流提取一个或多个 **Fᵢⱼ（feature stream）**，例如图像中的运动量、音频中的频谱特征、运动传感器中的活动强度；第i条流的特征数量不必与其他流相同。**理解补充：** 特征通常是对原始数据的有用表示，元数据则描述数据本身和获取条件；它们的来源和角色不同，不应混为一谈。

流程可以记为：**环境 → 多源同步流S及元数据M → 各类特征F → 在任务上下文中整合与处理 → 用户所需的洞察 → 用户反馈成为新输入 → 再处理。** 用户不是只在最后被动接收；查询、选择和反馈可以变成系统的输入流，使计算结果随任务继续变化。

**为什么不同于单媒体处理。** Computer vision 可以专注视觉证据，audio processing可以专注声音；本课强调把多源局部证据的相关性利用起来，在一个问题的上下文中形成更完整的信息。只把几段互不相关的视频和音乐放在同一目录，不等于完成了这种整合。多源也不必意味着每个来源都是不同媒体：多个视角的视频可以互相补足。

**可直接用于简答。** “Let Sᵢ be a synchronized sensor stream, Mᵢ its metadata, and Fᵢⱼ its j-th feature stream. A multimedia system extracts features and integrates correlated evidence from these streams in the problem context to generate useful insights. User feedback can be treated as another input stream. The central task is the combination of partial information, rather than isolated processing of one medium.”

来源：[S01 PDF p.33–34]。

### 1.12 照片元数据恢复旅行路线：从记录到 insight 的例子

一张照片的内容是画面，例如人物、建筑或风景；照片还可能带有拍摄时间、经纬度、相机型号和曝光参数等元数据。把同一次旅行的照片按时间排序，再把位置投到地图上，系统便可以形成旅行路线。这是“输入metadata，输出insight”的例子：原始字段只是零散时间和位置，路线把它们组织成用户能够理解的事件顺序。

**理解补充：** 只有地理位置没有时间，通常不能可靠确定先后顺序；没有GPS时可能需要人工位置标签或其他来源。GPS缺失、时钟错误或照片导出时元数据被移除都会影响结果，所以不能说“每一张照片必然包含完整旅行轨迹”。判断路线的目标也可能不需要逐个识别照片里所有物体，体现了“只处理相关信息”。

**可直接用于简答。** “Photo metadata such as capture time and GPS coordinates provides context beyond the pixels. Sorting the photos by time and mapping their locations can reveal a travel route. The system transforms isolated metadata into event-level insight, illustrating task-specific multimedia integration.”

来源：[S01 PDF p.35；该页地图、照片及元数据示意已核看]。

## 2. Elements of Multimedia Computing：经验、感知、语义与系统

### 2.1 系统目标与两大挑战：correlation 与 holistic information

多媒体系统的目标是把不同类型的数据流作为**相互关联的一组流**处理，以形成解决问题所需的信息和知识。数据不能只因为同时存到电脑里就被认为有关联；系统必须确定它们是否来自同一事件、对应哪个时间段、描述哪个对象，以及它们能够共同回答什么问题。

**挑战一：发现相关性。** 课件与课堂录音指出，课堂录制中的麦克风声音与电脑课件画面来自不同设备，必须对齐时间线，才能知道一句解释对应哪一页和哪一次操作。若两设备时钟不同或持续漂移，时间戳就不能直接当成绝对一致，需要同步或校正。

**挑战二：把局部证据组合成整体。** 教室舒适度不能只看温度，还要考虑湿度等条件；测温和口罩图像各自回答不同问题，组合后才能支持某一检查决策。车辆也需要把多个视角与运动信息关联起来判断周围情境。注意，课堂举的舒适温度范围和摄像头数量是例子，不是所有系统适用的标准或最低规格。

**可直接用于简答。** “The objective is to process different streams as one correlated set representing the information needed for a problem. The main challenges are discovering cross-stream correlations and combining partial evidence from disparate sources into a holistic interpretation in context. A lecture recording, for example, must align audio and slide images so that the explanation refers to the correct visual material.”

来源：[S02 PDF p.2；2026-09-10第一段录音19:01，00:18:53、00:22:24、00:24:33、00:25:16、00:26:40、00:28:03各段]。时间戳是原始转写的段首；不把长段中未标时的句子标为精确教师原话。

### 2.2 Experience、information、knowledge 和 communication 的关系

**经验（experience）**是直接观察或参与事件。例如亲自上课，包含听到的解释、看到的板书、当时的问题、互动和情绪。人从不断积累、联系的经验中建立关于世界的知识。**信息（information）**是对经验的抽象和有效表达，例如“这节课讲了感知需要先验知识”。它降低传播负担，但也丢弃了经验中的部分细节。

**知识（knowledge）**是人据经验和信息形成的理解、结构与规律。**理解补充：** 数据是记录到的符号或测量值；把数据与情境和已有知识联系起来，才能回答有意义的问题。数据、信息、知识不是简单由文件扩展名决定：同一段录音对于设备是采样数据，对于学生可能提供一个定义，对于掌握该定义的人又可能成为新的推理依据。

**通信（communication）**是分享经验和信息的过程，允许参与者在时间和空间上分离。但我们通常传递的是经过选择、编码的描述与感官记录，不能把发送者完整的主观体验原封不动地交给接收者。因此课件强调，通信中会失去“亲身经历”的部分。

**可直接用于简答。** “Experience is direct observation of or participation in events. Information is an abstract and efficient representation communicated about those experiences. Knowledge develops as experiences and information are accumulated and related. Communication allows sharing across time and space, but the representation does not reproduce the sender’s complete act of experiencing.”

来源：[S02 PDF p.3–6；数据的分层说明为理解补充]。DIKW金字塔的完整原课件在[S03 PDF p.61]，应与应用章节一起复习。

### 2.3 为什么有经验的人更容易理解：口罩、地铁与文化手势

课件中一名戴口罩的乘客坐在空旷地铁里。只知道像素和物体名称，未必能理解这张照片为何特殊；有疫情相关经验的人，可能把口罩、空车和出行行为联系起来，理解其风险与社会情境。课堂用2003年的情境与学生后来经历的疫情作比较，重点是**共享经验帮助解释信息**。仅凭画面本身不能严谨地唯一确定拍摄年份或事件，这些需要额外上下文。

课堂还用手势表示数字的文化差异说明：即使使用同一个动作，不同地区的习惯也可能赋予它不同意义。由此可见，把一种模态换成另一种，并不自动消除歧义；声音语言不通时改用手势，手势本身仍需要共同约定。

**解决思路。** 提供与接收者有关的例子和上下文，建立共享词典，解释符号与所指对象的映射；必要时用照片、文字、时间、地点等互相补充。目的不是堆砌媒体，而是弥补接收者缺少的理解条件。

**可直接用于简答。** “Effective communication depends on relevant prior experience and shared conventions. The same image or gesture can lead to different interpretations when receivers have different backgrounds. Multimedia and contextual explanations can provide complementary cues, while an agreed dictionary establishes the intended meanings of symbols.”

来源：[S02 PDF p.4–7，p.5地铁图已核看；2026-09-10第一段录音19:01，00:28:03之后的长段包含早餐、香港饮食、地铁与文化手势例子；该长段未拆细时间戳，不伪造逐例时间]。

### 2.4 Dictionary 与 percept：共同词汇不只是语言词典

词典（dictionary）的核心是**一组双方认可的符号及其意义**。它能把接收者看到的记号与发送者想表达的内容联系起来。自然语言词典记录词语；程序系统中的词典可以包含代码、术语、键与相应值；压缩算法也会利用“重复模式与短代码之间的映射”。这些应用共享映射思想，但不能把它们的具体机制混为一种算法。

多媒体中的基本感知元素称为 **percept**，视觉例子包括线、曲线和形状。系统通过这些局部模式及其关系，尝试形成更高层次的对象解释。比如“圆形轮廓加眼鼻口的相对布局”可以帮助人把简单画图理解为脸。只有一个孤立圆形并不足以确认它是人脸；还需要组合方式和已有模型。

**理解补充：percept、feature 与 object。** Feature常指可计算的表示，例如边缘方向、颜色分布、局部描述符；percept侧重被组织和解释的感知单元；object是更高层次的实体，如人或汽车。具体研究领域的术语边界可能不同，但考试中至少应写出从局部信号模式到语义对象的层次，不能把“一个像素=一个完整对象”。

**可直接用于简答。** “A dictionary is an agreed mapping between symbols and meanings. In multimedia, percepts such as lines, curves and shapes act as basic perceptual elements that can be organized into recognizable patterns. Shared mappings and prior models make it possible to interpret sensory data rather than merely transmit uninterpreted symbols.”

来源：[S02 PDF p.7；2026-09-10第二段录音19:59，00:00:00–00:03:11；术语层次说明为理解补充]。

### 2.5 Objects 与 events：如何表示动态世界

**对象（object）**用于刻画相对稳定的实体及其属性，例如某个人、某辆车、一个路口；属性可以是颜色、身份、位置或当前状态。这里的“静态成分”指对象提供实体层面的结构，不是说对象永远不能运动、属性永远不能改变。**事件（event）**刻画对象之间关系或状态随时间的变化，例如人进入房间、车辆越过停止线、乘客加入队伍。

音频和视频天生具有时间性：声音记录声学属性如何变化，视频记录视觉场景如何变化。因此理解它们不仅要问“画面里有什么”，还要问“发生了什么、何时发生、涉及谁”。一个“人”的检测结果描述对象；“这个人在进入禁区”的判断则涉及位置、区域关系和时间变化，属于事件层面。

**理解补充：医院排队案例。** 对象可包括病人、队伍、服务窗口，事件可包括加入队尾、开始看诊、离开。单帧人数反映当下状态，等待时间预测还要结合到达率、服务速度和随时间的变化。人类自然地用对象与事件理解任务，因此系统也需要提供能够对齐这些概念的表示。

**可直接用于简答。** “Objects model the relatively stable entities and properties of a scene, whereas events model changes in object states or relationships over time. Audio and video are dynamic signals, so object descriptions alone are insufficient. A surveillance system must distinguish the presence of a person from an event such as that person entering a restricted area.”

来源：[S02 PDF p.8；2026-09-10第二段录音19:59，00:09:42–00:10:23、00:14:38–00:16:45；禁区例子为理解补充]。

### 2.6 编程范式：课堂补充的 procedure、object 和 function

老师借编程范式说明机器表示如何逐渐贴近人的任务描述。**过程式（procedural）**把任务分解成步骤、过程和控制流程，例如读取列表、比较元素、交换位置、重复直到排序完成。它的重点是“如何一步一步执行”。C、BASIC、Pascal是课堂提到的相关语言例子。

**面向对象（object-oriented）**把状态和行为组织到对象中，用class定义一类对象的属性与方法，用对象之间的交互表达系统行为。车辆可以有速度和位置等状态，也有加速、转弯等方法。C++、Java、C#是课堂用来讨论的语言例子。一个程序可以同时包含多种范式，Python等语言不能被绝对归到唯一一种。

**函数式（functional）**在严谨概念上强调函数应用与组合，常偏好不可变数据和减少副作用。**理解补充与纠偏：** 课堂把“只描述想要什么、让系统决定细节”与函数式、AI编码并列，是帮助理解声明式倾向的类比。它不能作为函数式编程的严格定义；调用一个排序函数也不代表运行时必然由AI发明排序方法。AI自然语言生成程序是另一种交互方式，仍需要检查需求和结果。

**可直接用于简答。** “Procedural programming organizes computation as explicit steps and control flow. Object-oriented programming organizes state and behavior into interacting objects and classes. Functional programming emphasizes function application and composition, often with immutable data and fewer side effects. These paradigms provide different ways to represent a task; object-based modeling is particularly intuitive for describing entities and interactions.”

来源：[2026-09-10第二段录音19:59，00:10:23–00:23:56；严格的函数式定义和多范式说明为理解补充]。本节是录音补充，S02 PDF未列编程范式细节。

### 2.7 Perception：不是“测到信号”，而是理解信号

**感知（perception）**是理解感觉信号、恢复有用信息的过程。输入是sensory signals，输出是在应用上下文中相关的信息。相机产生像素、麦克风产生采样值，是采集；识别画面中的行人、判断声音中说了什么，是对信号的解释。传感器采集是感知系统的基础，但不是完整的语义理解。

可以把本课的关系记为 **signal/data + existing knowledge + context → interpretation/information**。它是概念关系，不是简单数值相加。没有相关模型和约定，系统即使拿到大量数据，也不知道哪些差异对当前任务有意义；只有已有知识而没有新证据，也不能保证了解当前环境。

课件把感知类比为“受约束的假设生成与检验”：系统先提出可能的解释，再看当前证据支持哪一种。课件所谓 controlled hallucination 强调先验模型会参与构造解释，不应理解成“可以随意编造”。有意义的判断必须被外部信号约束；矛盾证据应该使系统修正假设。

**可直接用于简答。** “Perception is the process of interpreting sensory signals to recover useful information in an application context. It requires both incoming evidence and relevant prior knowledge. The system generates possible interpretations and evaluates which is best supported by the data; therefore, the same signal can be interpreted differently under different knowledge or context.”

来源：[S02 PDF p.9–10；2026-09-10第二段录音19:59，00:23:56–00:29:23]。

### 2.8 两个视觉例子：为什么同一幅图会被看成不同东西

**人脸与花瓶。** 黑白轮廓既可以看成两张面对面的侧脸，也可以看成中间的白色花瓶。像素没有改变，变化的是图形与背景的组织、注意的位置以及正在使用的对象解释。这说明感知不是对像素一对一贴标签：同一信号可以支持多个高层模型。

**斑点狗。** 另一幅高对比黑白图在没有提示时容易显得杂乱；一旦知道要找一只狗，观察者就更容易把相关斑块组织成狗的轮廓。提示提供了先验，输入则提供支持或反对该解释的证据。提示能帮助识别，不等于提示内容必然真实；如果图中没有狗，仍需证据检查。

**可直接用于简答。** “The face–vase figure demonstrates that figure-ground organization and prior interpretation can produce different percepts from the same pixels. The Dalmatian example shows that prior knowledge helps organize ambiguous local patterns into an object. Both illustrate the interaction of bottom-up sensory evidence and top-down knowledge in perception.”

来源：[S02 PDF p.11–13，图像已核看；2026-09-10第二段录音19:59，00:29:23–00:32:24；bottom-up/top-down术语为理解补充]。

### 2.9 Neisser’s perceptual cycle：三个环节和正确方向

Neisser感知循环把感知看成一个主动、持续的过程，而不是一次“收数据→出答案”。**Schema（图式/环境模型）**是系统已有的知识、预期和当前环境模型；它决定下一步要寻找什么。**Exploration（探索）**是根据模型采取观察或行动，例如转头、移动相机、放大局部或查询另一条数据。**Environment / available information（环境及可获得信息）**提供新的样本，样本反过来修改schema。

三个箭头应准确记住：**schema directs exploration；exploration samples the environment；environmental information modifies schema**。中文可背为“模型指导探索，探索采样环境，环境证据修正模型”。新模型又决定下一步探索，构成闭环。任务已经获得足够证据、目标改变或没有新的可用证据时，可以暂时停止；不应为了保持初始猜测而只选支持它的样本。

**理解补充：寻找图中物体。** 先怀疑某一轮廓是一张脸，于是把注意移到可能的眼鼻位置；找到合理布局使脸的解释更可信，找到矛盾细节则改用别的解释。用户浏览地图时先看区域、再放大拥堵点、查看实时画面并修改路线，也能体现主动采样与更新。

**可直接用于简答。** “In Neisser’s perceptual cycle, the schema directs exploration, exploration samples the environment, and available information modifies the schema. Perception is therefore active and iterative: prior knowledge guides what to inspect, while new evidence updates the model. The updated model then guides further exploration.”

来源：[S02 PDF p.14；2026-09-10第二段录音19:59，00:32:59–00:35:36；2026-09-10第三段录音20:36，00:00:31–00:03:07]。

### 2.10 葡萄酒还是酱油：上下文可能帮助，也可能误导

课件展示美孚站广告：人物拿着深色瓶子，桌上有菜，既可能让人想到搭餐葡萄酒，也可能因为“烹饪、滋味、瓶子”的情境联想到酱油。广告中的品牌、瓶标、形状、文字和摆放方式都可以作为进一步检查的证据。老师在下一段录音开头继续讨论这类“先作猜测，再寻找证据”的过程。

这张图主要用来说明**用户先验、局部线索与环境上下文如何共同形成假设**，不需要把广告当成题目要求识别的商品知识。复习时应会说明：先提出候选解释，主动检查能区分候选解释的细节，若证据矛盾则修正模型。上下文不是永远正确的标签，显眼的菜品或宣传词也可能先把人带向错误判断。

**可直接用于简答。** “Context creates expectations that guide the interpretation of ambiguous visual content. In the wine/soy-sauce example, bottle appearance, food, text and brand information provide different clues. The observer should compare these clues and update the hypothesis when evidence is inconsistent, illustrating the perceptual cycle and the possibility of contextual bias.”

来源：[S02 PDF p.15–16，广告图已核看；2026-09-10第二段录音19:59，00:35:36以后；第三段录音20:36，00:00:07–00:03:07]。

### 2.11 四类系统问题：representation、presentation、system、integration

**第一，如何紧凑表示。** 原始音视频很大，存储和带宽有限，因此需要合理的数据表示、编码和压缩。答案要同时考虑体积与保留的信息；压得很小但破坏关键辨认线索，可能无法完成任务。

**第二，如何向用户呈现大量数据。** 把所有数据一次展示会增加认知负担，应按任务组织、选择合适媒体、支持定位与探索。老师的长课录像可以结合章节、时间线、字幕与课件，使学生更容易找到一个定义，而不必从头播放。

**第三，如何处理异质数据的系统问题。** 不同来源可能具有不同格式、采样率、数据速率和时钟，网络又有带宽限制和延迟变化。采集、缓存、通信、处理、同步和输出需要协调。**理解补充：** 把视频帧与音频采样逐个放在一个数组中，并不能自动解决同步与实时播放。

**第四，如何组合成必要的信息。** 需要选取与任务相关的来源和特征，建立它们之间的关系，再进行推断。例如语音内容解释“这里”，画面才能指明“这里”对应哪个公式；单一来源常不够明确。

**可直接用于简答。** “Multimedia design addresses compact representation, effective presentation, system support for heterogeneous streams, and information integration. Compression must respect storage and bandwidth limits; presentation must communicate the intended information; the system must handle formats, timing and processing; integration must combine the relevant evidence for the task.”

来源：[S02 PDF p.17；2026-09-10第三段录音20:36，00:03:07、00:04:22两段谈带宽与压缩；概念具体化为理解补充]。

### 2.12 Semantic gap：机器的数据表示与人的意义之间有什么差距

传统数字系统把数据编码为比特和字节，并组织成数组、列表、表、图像、音频或视频等表示。用户却用对象、事件、意图和任务描述世界，例如“一个人在危险地越过马路”“找出这节课老师解释采样定理的片段”。底层像素值与这些概念之间没有天然的一对一对应。

**语义鸿沟（semantic gap）**是机器能从感知数据中提取的信息，与用户在特定情境中对同一数据的解释之间的差异。它不仅是“0/1与文字的差别”，更是低层测量、特征与高层意义之间的差距。机器找到了红色区域，仍不一定知道它是交通标志、衣服还是灯光；识别出一张脸，也不自动知道该人正在参加什么事件。

**怎样缩小。** 在任务上下文中结合内容特征、时间地点等元数据、对象关系、多源证据、已有模型与用户反馈，逐层形成更有意义的表示。**理解补充：** 学习模型可以改善语义解释，但不能声称多模态AI已经消除一切语义鸿沟；同一事件仍可能因目标、文化、缺失证据而有不同解释。

**可直接用于简答。** “The semantic gap is the difference between information that a machine can extract from perceptual data and the interpretation a user gives to the same data in a particular situation. Computers use low-level representations and features, whereas users reason about objects, events and intentions. Multimedia computing reduces the gap by combining content, context, prior knowledge and correlated sources.”

来源：[S02 PDF p.18–19；2026-09-10第三段录音20:36，00:10:10–00:14:30]。

### 2.13 Content、context、metadata：看到了什么与为什么这样理解

**Content（内容）**是采集到的媒体和信号，例如照片中的像素、录音中的波形。**Context（上下文）**是这些数据产生和被解释时相互关联的条件，例如拍摄时间、地点、设备、事件、用户任务和周围环境。**Metadata（元数据）**是关于数据的数据，它可以保存部分上下文，例如照片的EXIF记录中的时间、相机参数和可能的GPS信息。

三者不能简单等同。照片的GPS字段是metadata，可用来说明拍摄地点这一context；“用户正在找回某次旅行的路线”也是context，却未必存在照片EXIF里。元数据也不全是语义背景，例如文件尺寸描述文件本身，但单靠尺寸无法判断画面含义。课件的重点是content和context应一起用于理解多媒体，不能只做像素分析，也不能只看标签而忽略内容。

**例子。** 同一张人群照片，如果拍摄于演唱会、车站疏散或毕业典礼，对事件的理解完全不同。时间地点、声音、前后视频和用户问题都能帮助区分。照片管理软件按地点和时间聚合相册，也是用元数据建立用户容易理解的组织方式。

**可直接用于简答。** “Content is the acquired media data, while context is the set of related conditions in which the data is acquired or interpreted. Metadata is data about the data and may encode contextual parameters such as time and location. Combining content with context helps resolve ambiguity and supports a more accurate interpretation.”

来源：[S02 PDF p.20–21，照片管理与EXIF图已核看；2026-09-10第三段录音20:36，00:14:30–00:17:58；人群例子为理解补充]。

### 2.14 多媒体系统的五类组成：从采集到输出的完整解释

**Capture devices：采集/输入设备。** 相机、录像机、麦克风提供音视频，键盘、鼠标、触摸屏提供用户输入，压力传感器提供物理量。输入不只来自现场硬件；**理解补充：** 从HTTP接口获得已有传感器数据也是系统的数据入口，但API本身不是把物理量转成信号的传感器。

**Storage devices：存储。** 硬盘、闪存、光盘保存媒体和元数据；内存缓存支撑流处理，数据库帮助组织和检索。存储解决跨时间使用和处理速度不匹配的问题，但永久保存不是每个实时系统的必然要求。

**Communication networks：通信网络。** 局域网、4G/5G、Bluetooth、RF等负责把数据从采集端送到处理端或输出端。系统设计要结合需要的覆盖距离、速率与时延。名称不同的网络不能直接互换，也不应假定网络总能瞬间无损传完所有数据。

**Computer systems：计算与处理。** 工作站、服务器或DSP进行解码、滤波、压缩、特征提取、融合、分析及控制。DSP即digital signal processor，适合信号处理任务；并非任何多媒体系统都必须使用独立DSP芯片。

**Output devices：再现/反馈设备。** LCD等显示设备向视觉输出，扬声器向听觉输出，振动马达和haptic feedback向触觉输出。输出应让用户获得需要的信息；显示一排原始数字不一定比图像、曲线或语音提示更有效。

**完整链路例子：手机通话。** 麦克风把说话变成电信号，模数转换得到数字采样，处理器编码并暂存，通过网络送到对方，接收端缓存、解码并驱动扬声器。课堂录制则把麦克风音频与课件画面同步处理，存储后供复习，同时可把声音送到教室扬声器。

**可直接用于简答。** “A multimedia system includes capture, storage, communication, computation and output. Capture devices obtain sensory and user-input data; storage preserves or buffers it; networks transfer it; computer systems process and integrate it; output devices present the result to human senses. The components must work together with appropriate timing and data representations.”

来源：[S02 PDF p.22；2026-09-10第三段录音20:36，00:16:55–00:23:07；ADC和缓存功能的明确化为理解补充]。

### 2.15 课堂强调的辨析：人脸检测、识别与系统层次

**Face detection（人脸检测）**回答“有没有脸、脸在哪里、多少张脸”，输出通常是位置或区域；**face recognition（身份识别）**回答“这是谁、是否与已知身份匹配”。老师先用眼、鼻、嘴及其合理布局解释检测，再用五官之间的距离作为身份特征的直观例子，说明如何从图像数据走向关于人的信息。

**理解补充：** 五官距离只是教学上易理解的特征例子。它会受姿态、相机距离、表情和成像影响，不能保证同一人的所有图像都有完全相同的像素距离，也不能保证不同人不会有相近特征。现代系统可能使用学习得到的特征表示；本课此处要掌握的是“原始数据→特征→任务判断”的层次，而不是背一个过度简化的识别算法。

**可直接用于简答。** “Detection locates instances of a class, such as finding faces in an image. Recognition uses distinguishing features to identify an instance or match it to an identity. Both require converting raw sensory data into task-relevant representations, but their questions and outputs differ.”

来源：[2026-09-10第二段录音19:59，00:01:27–00:09:42；S02 PDF p.7–10提供词典、对象、感知框架；现代方法与距离限制说明为理解补充]。

### 2.16 第一、二份课件的逐页覆盖核对

以下“p.”统一指PDF阅读器从1开始的**物理页码**。S02页脚编号有跳号，例如PDF p.6页脚印7、PDF p.22页脚印24；不要把它误认为缺了PDF页。

- **S01 p.1**：课程及章节封面；无新增概念。
- **S01 p.2–7**：多媒体的狭义误解、单独音频/文字是否足够、牙医语境、五感与视听主导性；见1.1。
- **S01 p.8**：计算、多媒体计算及分享经验/提取知识目标；见1.2。
- **S01 p.9**：跨时、跨地、跨受众的传播问题；见1.3。
- **S01 p.10–16**：口语、文字、纸、印刷、电报、电话、广播、电影电视、存储、数字媒体、Internet及invariance汇总；见1.3–1.4。
- **S01 p.17–22**：1960年代至21世纪计算机与多媒体发展、资源瓶颈、PC与移动设备；见1.5。
- **S01 p.23**：移动设备传感器示意；见1.6，已经核对图片文字。
- **S01 p.24**：应用推动技术与设备演进；见1.7。
- **S01 p.25–26**：新计算应用的时空流、整体视角、相关信息和探索性质；见1.8。
- **S01 p.27**：电商订单数、地区增长与热门商品的不同计算需求；见1.9。
- **S01 p.28**：体验式环境与人机协同；见1.10。
- **S01 p.29–31**：直观、查询与呈现空间一致、用户状态与上下文三特征；见1.10。
- **S01 p.32**：通过多媒体技术实现体验式系统；见1.2、1.10。
- **S01 p.33–34**：同步S流、M元数据、F特征流、整合、用户反馈、多媒体与单媒体关系；见1.11。
- **S01 p.35**：从照片元数据形成旅行路线；见1.12，已经核对图片。
- **S02 p.1**：课程及章节封面；无新增概念。
- **S02 p.2**：系统目标、发现相关性、组合局部证据；见2.1。
- **S02 p.3–4**：experience、information、knowledge、communication及经验损失；见2.2。
- **S02 p.5–6**：口罩地铁图、共享经验的意义；见2.3，已经核对图片。
- **S02 p.7**：词典、程序映射、压缩词典、percepts；见2.4。
- **S02 p.8**：objects和events及媒体动态性；见2.5。
- **S02 p.9–10**：感知定义、信号与已有知识、假设解释；见2.7。
- **S02 p.11–13**：花瓶/双脸、斑点狗与提示；见2.8，已经核对图片。
- **S02 p.14**：Neisser三箭头感知循环；见2.9。
- **S02 p.15–16**：美孚广告的wine/soy sauce例子；见2.10，已经核对图片。
- **S02 p.17**：表示、呈现、异质系统、信息组合四问题；见2.11。
- **S02 p.18–19**：机器表示、人类抽象及semantic gap；见2.12。
- **S02 p.20–21**：content、context、metadata、EXIF；见2.13，已经核对图片。
- **S02 p.22**：采集、存储、网络、计算、输出五类模块；见2.14。
- **9月10日录音补充**：参数与单位、对时、温湿度、多传感器融合、共享经验、手势文化、编程范式、人脸检测/识别；分别见2.1、2.3、2.6、2.15及后续数字媒体参数章节。

### 2.17 需要防止背错的资料表述

1. **页码与录音不是一一对应的“第几次课”。** S01、S02是课件文件编号；9月10日录音已讲S02。本文按主题/课件编排，不能把编号自动当成课表中的某一次授课日期。
2. **编程范式有ASR误听和口头简化。** 转写某处把C听成面向对象，紧接着又讨论C++/Java与过程式语言差异；应按明确概念记忆：C通常用于过程式，C++/Java常用于对象建模，Python等可支持多范式。函数式不等于“AI自动替你实现一切”。
3. **人脸间距不严格不变。** 五官关系是解释特征的例子，图像中的距离会变，不是身份的绝对无误编码。
4. **计算机二进制的物理说法被简化。** 录音把数字电路概括为开/关、0/1。严谨说法是用可区分物理状态表示逻辑值；电路并非只存在两个数学电压，二进制也不代表只有一种计算体系。该历史旁话不需要替代本课的数据表示主线。
5. **上下文和先验会产生偏差。** 口罩图片、广告、花瓶/双脸、斑点狗的结论是用证据检验解释，不能写成“有先验就必然知道真相”。
6. **课件旧硬件与新设备预测是背景。** 不把个别配置当成所有当年机器的上限；不把‘移动设备替代PC’写成已完成的全面替代。
7. **本段录音个别长段缺少细分时间。** 可引用已有起始时间定位该段，不能根据总时长倒推出精确的教师原话时间。本文保留可查证的段落时间，并对解释性扩展明确标为理解补充。

## 3. 应用案例：把声音、图像与视频变成可处理、可检索、可决策的信息

本章覆盖 S03《Example Applications》全部 63 个 PDF 页面，并补入 9 月 10 日最后一段及 9 月 17 日课堂转写中的解释。课件页码使用 PDF 实际页码；录音时间戳是各段录音内部的相对时间。课件给出的是应用与方法；以下“答题模板”是按材料编写的复习示例，不代表老师公布的考题。标有“理解补充”的公式或实现说明用来解释机制，不应误认为课件要求背诵的细节。

### 3.1 这一章要学会的共同方法：先表示数据，再设计处理流程

来源：[S03 PDF p.1–2、21–22、55–63]；课堂补充：2026-09-10 21:10 段 00:00:49–00:01:54；2026-09-17 20:05 段 00:27:53–00:41:14（该长转写段末的系统层级总结）、00:58:55–结尾。

所有案例都可以用同一个系统问题来理解：**输入是什么数据 → 里面有什么问题或有用模式 → 用什么表示/特征/模型 → 怎样处理或比较 → 输出什么结果 → 哪些条件下会失败。** 例如输入麦克风波形时，目标可以是去掉噪声、输出文字、识别歌曲或压缩码流；输入摄像机画面时，目标可以是增强图像、消除抖动、识别人、统计过线人数或查找车辆。输入相同，任务不同，处理流程就不同。

老师在步态案例后特别说明，要理解解决问题的 methodology 和系统数据流，不要求在这门课中展开所有图像分割、神经网络或信号处理算法的实现。因此复习时应能讲清每个模块解决什么问题、依赖什么输入、把什么交给下一模块。知道算法名称而说不出输入输出，仍然没有掌握应用。

**可直接答：**“设计一个多媒体应用时，应先确认任务和媒体类型，建立可供计算机处理的数据表示，再做必要的预处理、特征提取和模型匹配，最后产生任务要求的输出。系统必须考虑传感器、噪声、时间和空间分辨率以及人类感知限制；错误的输入或表示会使后面的算法产生错误结果。”

### 3.2 课堂补充：声音、图像、颜色、透明度与视频到底怎样存在电脑里

来源：[S03 PDF p.9、20、22–24] 提供应用背景；本节具体数据表示与计算主要来自 2026-09-17 19:01 段 00:01:11–00:20:39，以及 20:05 段 00:00:20–00:11:37。下列算例已按数学核对；转写中的错数不照抄。

**声音是随时间变化的一维数据。** 麦克风把声压变化转换成电信号，A/D 再把它变成按时间排列的数字样本。可写成 `x[0], x[1], …`；如果采样间隔固定，样本编号配合采样率就确定时间，不一定要为每个样本额外保存时间戳。老师先用“在 17:00、18:00、19:00 分别测温”的两列表格作类比，再把测量对象换成声压/幅度。计算机处理的是测量数值；它不会天然知道这些数值意味着“冷”“热”或某种情绪，要由规则和模型建立含义。

**图像是二维像素阵列。** 横向有 `W` 个像素，纵向有 `H` 个像素，所以总像素数为 `W×H`。Pixel 是 picture element；一个像素存的是该位置的亮度或颜色。空间分辨率决定采样有多密；位深决定每个位置可区分多少数值。增加位深不会直接增加像素数，增加像素数也不保证光学清晰度或低噪声质量一定提高。

**灰度和 RGB。** `b` 位灰度像素有 `2^b` 个可编码级别：1 位是 2 级，8 位是 256 级。8 位灰度通常用 0 表示黑、255 表示白。RGB 彩色像素分别保存红、绿、蓝三个通道；若各为 8 位，则每像素共 24 位，有 `256³=16,777,216` 种编码组合。`#RRGGBB` 中每两个十六进制字符对应一个 0–255 的通道值，例如 `#FF0000` 是纯红。

**形状与透明度。** 存储画布可以保持矩形，同时另存 mask 指明哪些像素属于前景；二值 mask 可用 0/1，连续 alpha 可表示不同透明度。RGB 各 8 位再加 8 位 alpha，得到常见的 32 位 RGBA。**纠错：alpha 表示覆盖/不透明程度，不是窗口前后顺序或 z-order；并非所有图像都必须有 alpha，也并非所有彩色图像都用 32 位。** 老师在多窗口和非矩形形状例子中混合讲到了这些概念，答题时要分清。

**原始数据量公式。** 不计文件头、压缩、行填充和额外元数据时：

- 静态图像位数：`W×H×bits_per_pixel`；字节数再除以 8。
- 原始视频每秒位数：`W×H×bits_per_pixel×FPS`；总量还要乘时长。
- 原始 PCM 音频每秒位数：`sampling_rate×bits_per_sample×channels`。

`4×4` 的 32 位图像为 `16×32=512 bit=64 byte`，其中每像素是 `32 bit=4 byte`；不能把整张图误算为 4 byte。Full HD `1920×1080` 的 RGBA 单帧为 `8,294,400 byte≈8.29 MB≈7.91 MiB`；30 FPS 原始视频约为 `248.832 MB/s`，即 `1.990656 Gbit/s`。这解释了为什么视频系统需要压缩、合理编码和存储管理。

**视频是按时间组织的图像序列。** FPS 是每秒帧数；24、25、30 FPS 是课堂举例，不是所有视频必须采用的值。空间分辨率、位深、帧率和压缩码率分别描述不同维度。课上涉及 HD `1280×720`、Full HD `1920×1080`、4K 等命名；4K 的“K”大致指横向四千像素，消费级 UHD 常为 `3840×2160`，具体标准要看题目。**纠错：1280×720 是常见 720p HD，不应写为 DVD 的标准分辨率。**

**可直接答：**“一张图像可看成 H 行 W 列的像素矩阵，RGB 保存每个位置的颜色，alpha 可额外表示透明度。未压缩数据量等于像素数乘每像素位数；视频再乘帧率与时长。分辨率、位深和帧率分别控制空间、数值和时间采样精度，不能互相替代。”

### 3.3 主动降噪耳机、汽车降噪与多麦克风：都处理噪声，但作用位置不同

来源：[S03 PDF p.3–7]；课堂：2026-09-10 21:10 段 00:01:54–00:19:58（末尾长段同时涉及多麦克风、EQ 与 ASR）；2026-09-17 19:01 段 00:37:30–结尾的复述。

**主动降噪耳机（active noise cancellation, ANC）。** 输入是外界噪声的麦克风测量，以及原本要播放的音乐；输出是播放给耳朵的音乐加“反噪声”。声音是波，可以叠加。若到达耳朵处的反噪声与原噪声幅度相近、相位相反，则它们的声压变化相互抵消。理想化写成 `n(t)+[-n(t)]≈0`，耳朵主要听到期望音乐 `s(t)`。课件图的流程是外界噪声 → 麦克风 → 降噪电路反转波形 → 耳机扬声器发出补偿声 → 与原噪声在耳朵附近相消。

**为什么耳机上要装麦克风？** 麦克风负责测量需要抵消的环境声，扬声器负责产生补偿声，两者分别承担输入和输出功能。理解补充：现实系统要估计声传播路径与处理延迟，不能只把录音文件简单乘以 −1 就保证在任意位置抵消全部声响；持续、较可预测的低频噪声通常更适合 ANC，快速变化和高频噪声更难精确补偿。被动隔音靠物理阻挡声音，ANC 靠额外产生声波。

**汽车/巴士降噪。** 课件图包含发动机噪声、车内多处麦克风、ECU、音响/低音扬声器，及发动机转速信息。测量车厢噪声，利用处理系统产生反噪声，经车内音响播放，使目标区域的发动机声减弱。老师用汽车和双层巴士解释“扬声器除了广播也可参与噪声控制”。这用于说明原理，不能据此推断所有巴士或全部车型都实际配有这种系统。

**双麦克风通话降噪。** 主麦克风靠近嘴部，取得较强的语音加噪声；另一个麦克风取得较多环境噪声作为参考。处理器估计主通道中的噪声再抑制，输出更清晰的语音供对方听或供 ASR 使用。图中 `Subtract → Amplify` 是概念示意。理解补充：两个位置录到的噪声会有时差和幅度差，所以实做一般需要匹配/自适应处理；两个含语音的通道盲目相减也可能损伤语音。

**为什么需要三个、四个乃至更多麦克风？** 不同握机姿势、免提会议和不同说话方向会改变拾音条件；多通道提供方向和空间信息，可改善远场拾音、噪声分离及覆盖范围。麦克风方向性（directionality）表示对不同方向来声的响应，不同用途需要不同布置。S03 p.7 的历史文章还列出常开唤醒功耗、尺寸、过载能力与远距离拾音等工程取舍；它举旧款 iPhone 和 Echo 的数量作当时案例，不是现售设备规格。

**答题模板：**“ANC 耳机用麦克风取得环境噪声，处理电路估计在耳边所需的反相补偿声，再由扬声器播放，使噪声声压在目标位置相消。手机通话降噪则常利用参考麦克风估计主通道噪声，清理数字语音；前者改善听者处的声场，后者改善送出或识别的音频信号。多麦克风还能利用方向与位置差异提高拾音质量。”

### 3.4 数字均衡器（digital audio equalizer, EQ）

来源：[S03 PDF p.8]；课堂：2026-09-10 21:10 段00:12:21–00:19:58（同一长转写段内的 EQ 说明），以及 2026-09-17 19:01 段 00:37:30–结尾的复述。

EQ 的输入是音频，输出是改变了频率成分相对强弱的音频。它把可听频率范围分成若干频带，对每带分别设置 gain（增益）或 attenuation（衰减），再合成输出。课件给出范围约 20 Hz–20 kHz；高端系统可超过 200 个频带，调节范围示例为 ±6 dB 到 ±24 dB。具体频带数和范围是产品例子，不是 EQ 的固定定义。

降低低频、增强高频，或反过来，都会改变音色；Bass Booster 增强低音，Classical、Jazz、R&B、Rock 等 preset 是一组预先设好的各频带增益。它们不等于自动把一首歌改造成另一个音乐流派，而是改变听觉频谱平衡。总音量旋钮近似对整体幅度一起调节，EQ 可针对不同频带分别调节。

**限制/易错。** EQ 无法无条件区分同频带里的语音和噪声；若某频带既有噪声也有目标内容，衰减该带也会损失目标内容。大幅 boost 可能增加噪声、削波或失真（理解补充）。不要将 EQ 与前节波形相消的 ANC 混为一谈；老师用“频率上的保留/抑制”作类比，二者的信号作用机制并不完全相同。

**答题模板：**“数字均衡器按频率把音频划分为若干频带，对每带独立施加增益或衰减，以控制低音、高音等相对强度。预设模式就是一组频带增益设置。它改变频谱和音色，而普通音量控制主要整体调整响度。”

### 3.5 语音转文字（speech-to-text / automatic speech recognition, ASR）

来源：[S03 PDF p.9]；课堂：2026-09-10 21:10 段00:12:21–00:25:01（包含旧式 ASR 与过渡至 Shazam）；2026-09-17 19:01 段 00:37:30–结尾的复述。

**输入输出与意义。** 输入是人的语音波形，输出是词/句子文本。系统需要从连续、会受噪声、口音、语速影响的声音，推断说了哪些语言单位。它和“认出是谁在说话”的 speaker recognition 是不同任务，也和“把文字翻译为另一种语言”的 translation 不同。

**课件的传统流程：**

1. 麦克风拾音与 A/D：把连续声波变成数字音频。
2. 降噪与 normalization：减少环境干扰，并统一音量/特征尺度，避免录音大小声差异过度影响匹配。
3. 分成短时间片段：把长语音分为适于局部分析的短窗；课件说短到百分之一/千分之一秒量级，重点是短时处理，不是把每个字母等长切开。
4. 特征/音素匹配：将短片段的声学模式与已知 phoneme（音素）比较。英语约 40 个音素是课件近似说法，具体数目随口音和音系划分而变。
5. 统计语言解码：组合音素并结合统计模型推断最可能的词和句子。声音相似时，上下文可以帮助决定哪种词序更合理。

**课上补充。** 老师用旧式系统先读长文本、让电脑适应说话者音色和口音的例子解释训练，再以 apple 的声音模式说明从波形/频谱到符号的映射。转写把这一过程识别成“每个字母的频谱”，应按课件校正为**声学单元/音素，不是字母逐个发音**。现代系统可学习更复杂的特征，但录音质量仍影响结果；不能从课堂口述的零散准确率得出所有系统统一准确率。

**限制/易错。** 同音词、连读、口音、背景声和词表外内容可能产生歧义。清理信号不等于理解语义，声音识别成文本也不保证语句事实正确。输入音频不清晰时，后续强模型仍可能“garbage in, garbage out”。

**答题模板：**“传统语音转文字先将声波数字化，做降噪与归一化，再对短时片段提取声学模式并识别音素，最后用统计声学/语言模型将音素序列解码为最可能的词句。声学匹配回答‘听起来像什么’，语言模型帮助回答‘哪些词序更合理’。”

### 3.6 Shazam：音频指纹、频谱峰值与时间对齐

来源：[S03 PDF p.10–14]，包括 p.11–14 的 constellation map 与匹配峰值柱状图；课堂：2026-09-10 21:10 段00:19:58–00:29:51（该长段后半开始说明 Shazam）；2026-09-17 19:01 段 00:00:00–00:01:11。

**任务。** 输入一小段录到的音乐，输出歌曲候选、相关名称/歌手和匹配分数。课件以约 10 秒样本举例，目的不是要求整首歌全部上传，更不是把录音转换成歌词后搜歌词。

**关键表示。** Spectrogram（时频谱/声谱图）横轴为时间、纵轴为频率，强度表示该时刻的频率能量；从中选显著局部峰值，形成稀疏的 constellation map（星座图）。Audio fingerprint 是由这些稳定、可区分的声学结构形成的紧凑表示，用来和数据库中的已有歌曲比较。

**离线建库 → 在线查询：**

1. 对曲库每首歌计算指纹，并保存与歌曲 ID、歌曲内部时间的关联，建立索引。
2. 查询录音经过同样处理，得到短片段的峰值/指纹。
3. 查询片段从歌曲中间开始，时间原点未知，因此必须允许时间平移。
4. p.12–14 图把红色查询星座图沿蓝色数据库星座图移动；每个偏移量都统计峰值匹配数。
5. 正确位置会使许多峰值同时对齐，匹配柱状图出现明显峰值，系统由此判断歌曲及片段位置。随机噪声一般难在同一时间偏移上产生大量一致匹配。

课件称其对噪声、房间混响、均衡变化和叠加声音具有鲁棒性，含义是能容忍一定干扰，不是保证任何失真条件下都能识别。理解补充：稀疏峰值/相对结构通常比逐个比较原始波形更稳定；数据库索引可减少对整座曲库逐一完整比较的成本。课件展示的是峰值平移匹配概念，不要求在没有材料支持时背诵某种精确哈希编码格式。

**老师强调的“检索之前要建索引”。** 图书馆先给新到书建立记录、标识和位置关联，读者才能按关键词或编号快速找到书。歌曲同理：必须先把候选内容的可检索表示加入系统；只收集一堆录音而不建立指纹索引，无法直接获得高效内容检索。老师用 ISBN 作类比；实际检索特征不一定是像 ISBN 一样全局唯一的编号，而可用相似度比较。

**答题模板：**“Shazam 从短音乐样本的时频谱中提取显著峰值形成指纹，与预先索引的曲库指纹比较。由于查询可能从歌曲任意位置开始，匹配需要寻找一致的时间偏移；某个偏移下大量峰值对齐，就支持该歌曲为正确候选。使用稀疏稳定特征与索引，使系统能在一定噪声和混响下高效检索。”

### 3.7 音频压缩的一条路线：LPC vocoder 用发声模型传参数

来源：[S03 PDF p.15–16]，尤其 p.16 的生理发声与电子声码器框图；课堂：2026-09-17 19:01 段 00:20:39–00:32:04。

**为什么能压缩？** 原始波形包含很多样本；若一段语音可用一个简化生成模型近似，就可以传模型参数，接收端用相同模型重建，而不逐样本传完整波形。老师以“传乐谱/标准音符和系数，而不是传整段录音”作类比，并强调双方必须有相同的表示约定。这是一种解释压缩思想的类比，不是说所有语音都真的编码成七个音符。

**人体发声的 source–filter 视角。** 气流提供能量；浊音（voiced）含声带周期振动的激励，清音/非浊音（unvoiced）可用类噪声激励近似；口腔、鼻腔与发音器官形成声道共振，塑造输出语音的频谱包络。课件的生理解剖描述较简化，准确表述应是气流驱动声带及声道过程，不要把“epiglottis 直接产生全部声音”当作标准定义。

**LPC（linear predictive coding，线性预测编码）vocoder。** Vocoder 来自 voice + coder。编码器从短段语音估计：①表示声道滤波特性的系数；②能量/增益；③基音 pitch；④voiced/unvoiced 状态。传输这些参数后，解码器按浊音状态选周期/音调激励或噪声激励，按基音和能量调节，再通过可变声道滤波器合成语音。p.16 图依次显示 voiced/unvoiced decision、tone/noise generator、fundamental frequency、filter coefficients 与 variable filter。

理解补充：LPC 的“预测”可理解为用先前样本的加权组合近似当前样本，所估系数也可表示一个简化声道滤波模型。答题重点是模型和参数的关系，不应把 LPC 简单定义成“只删除听不到的频率”。后者属于下一节心理声学路线。

**用途、优点与限制。** 课件把 GSM 语音编码与 LPC 框架联系起来；其核心优势是对适合该模型的语音可用较少参数表示。它有语音生成模型假设，对复杂音乐和任意环境声未必合适，合成质量依赖模型与参数精度。p.16 问“还有什么用途”，可按机制答语音合成或改变 pitch/声道参数形成语音效果；这是从框图推导的理解补充，课件没有给唯一标准答案。

**答题模板：**“LPC vocoder 把语音近似为激励源经过声道滤波器的输出。编码端估计能量、基音、浊/清音状态与声道滤波系数，只传这些参数；解码端生成相应激励并通过滤波器重建语音。它利用语音产生机制降低传输数据量，因此适合语音，不能假设同样模型适用于所有音乐。”

### 3.8 另一条路线：MPEG Audio 利用听觉限制与掩蔽效应

来源：[S03 PDF p.17–20]，含 p.18 耳结构/频率分布图与 p.19 听阈/掩蔽曲线；课堂：2026-09-17 19:01 段 00:32:04–00:52:30。

**听觉系统为什么与编码有关？** 环境声压使鼓膜振动，经中耳机械结构传到内耳耳蜗；耳蜗液体与感觉结构把机械变化转成神经信号。耳蜗不同位置对不同频率敏感，课堂视频说明底部区域偏高频、顶部区域偏低频。人耳并非对所有频率和强度都一样敏感。课件用“感知 spectrogram”概括频率分析功能，这是直观类比，不是说耳朵真的存储一张数字声谱图。

**可听范围与听阈。** 课件使用大致 20 Hz–20 kHz 的常见年轻人听觉范围，实际听力随人和条件而变。即使在可听频率内，声音也必须达到相应频率的听觉阈值才可能听见。p.19 听阈曲线说明可听性取决于频率与强度，不只看有没有那个频率。

**Frequency masking（频率掩蔽/同时掩蔽）。** 一个频带的强声会使另一个较弱的声音听不见，而弱声单独存在时本来可以听见。强声在附近频率抬高了有效听阈，弱信号落在掩蔽阈值下。可用强乐器声掩盖同一时刻附近频率弱成分解释。不能写成“只要有一个大声，所有频率的声音都消失”。

**Temporal masking（时间掩蔽）。** 强声停止后的一小段时间内，某些弱声仍不易听到。课件侧重 post-masking（后掩蔽）；并没有给可以普遍套用的持续秒数。录音用枪声作直觉例子，不能把强声后长时间听力下降与音频编码采用的短时心理声学掩蔽混成同一精确机制。

**MPEG Audio 的 lossy 思想。** 根据心理声学模型判断哪些频率成分或量化噪声在人耳当前条件下不明显，为这些部分少分配数据，保留更容易被察觉的部分。输出波形通常无法逐样本精确恢复原输入，所以属于有损压缩；目标是在给定码率下保持感知质量。理解补充：实际编码可表现为不同频带不同量化精度，而不只是把每个被掩蔽音符完全删除。心理声学判定主要是编码处理功能，不能写成“所有麦克风硬件自动拒绝采集被掩蔽声音”。

**三个 Layer 与课件 MP3 流程。** Layer I 是基本方案（课件举 DCC 数字磁带）；Layer II 加入更高级 bit allocation；Layer III 加入 hybrid filters。MP3 指 MPEG Audio Layer III，**Layer I/II/III 不是 MPEG-1/2/3 三个 MPEG 版本**，也不是一首 MP3 必须先后保存三层完整音轨。

p.20 的概括流程为：每组处理 1152 个样本 → 分成 32 个频带 → 以心理声学模型判定掩蔽 → 分配表示精度/编码资源 → 用 variable-length coding 利用统计冗余。`1152/44100≈0.0261 s`，所以“约 26 ms”隐含 44.1 kHz 采样率；不能对任意采样率都写成固定 26 ms。更常见的符号用更短码是可变长编码节省数据的直观原因（理解补充）。

**比较与答题模板：**“LPC 主要利用语音产生模型，用激励和声道参数代替大量波形样本；MPEG Audio 主要利用人耳感知模型，在听阈及频率/时间掩蔽允许的范围内减少不易察觉的信息，再利用编码冗余降低码率。二者分别从‘怎样产生声音’和‘哪些声音值得保留’获得压缩机会。”

### 3.9 图像增强：HDR、夜景、多帧融合与超分辨率

来源：[S03 PDF p.22–24]；课堂：2026-09-17 20:05 段 00:11:37–00:24:44。HDR 与低分辨率融合的较长解释在录音；课件 p.23、24 具体展示 Night Mode 与 Deep Fusion。

**HDR（high dynamic range）解决什么？** 同一场景中有很亮和很暗的区域时，单次曝光受传感器可记录范围限制：为亮处曝光，暗处可能没有细节；为暗处曝光，亮处可能饱和。HDR 多曝光方法以不同曝光参数取得互补图像，将亮部保留良好的短曝光与暗部较好的长曝光信息对齐融合，形成更充分的明暗信息，再映射到可显示范围。最后一句 tone/display mapping 是理解补充。HDR 的“dynamic”在这里指亮暗范围，不是指物体必须在运动。

**夜景模式（Night Mode）。** 低光下，短曝光可减轻移动拖影，但获得的光少、噪声可能大；长曝光获得更多光，却更怕相机或被摄体运动。p.23 的方法是拍摄不同快门速度的多帧，再智能合并，兼顾暗部细节和运动模糊。输入多张暗光照片，输出细节/噪声更平衡的增强图像。不是简单把整张图亮度乘大，因为那也会放大噪声且不能恢复已经丢失的细节。

**Deep Fusion 历史案例。** p.24 引用 2019 年 iPhone 11 Pro/Pro Max 案例：总共九张图像，包括四张短曝光、一张长曝光、四张额外图像，组合以优化细节与低噪声。这里需要理解多帧提供互补信息的概念；九张是该课件所举产品流程，不是所有多帧算法的固定数量，也不是必须外推到其他手机。

**课堂补充：多帧超分辨率（super-resolution）。** 空间采样太稀时，微小细节无法在单张低分辨率图中充分表示；老师以 2×2 与 4×4 网格、远距离卫星目标说明。利用多帧之间不同视角或轻微位移取得互补采样，再配准和重建更细的表示。它与 HDR 都体现“单次传感受限，联合多次观测”，但 HDR 主要改善可记录亮暗范围，超分辨率主要改善空间细节。

**限制/易错。** 多帧必须对应同一场景结构，运动、遮挡或配准不准可产生重影；各帧都缺失或饱和的信息不能仅靠平均保证真实恢复。更多像素、HDR、低噪声和锐利不是同一指标。这里的“智能融合”不表示无条件创造真实细节。

**答题模板：**“多帧增强通过采集具有互补信息的多次观测，先对齐，再选择或融合有用区域。HDR 结合不同曝光以同时保留亮暗细节；夜景融合在收光与运动模糊间取平衡；多帧超分辨率利用不同采样位置补充空间细节。共同限制是场景运动及错误配准可能导致伪影。”

### 3.10 Retinex：亮度/颜色增强的例子

来源：[S03 PDF p.25]。该页只给 Retinex 名称与港口画面增强前后对比；下述原理标为理解补充，不把课件一幅图扩写为老师明确讲过的算法细节。

Retinex 是把视网膜 retina 与大脑皮层 cortex 的概念结合命名的一类增强思想，旨在分离照明影响与物体反射特征，改善不均匀照明下的可见性。输入偏暗、对比不足或照明不均的图像，输出局部细节/对比和颜色外观更适合观察的图像。课件图体现原画面灰暗、增强后港口结构较清楚。

**理解补充的机制：** 将观测亮度近似写成 `I(x,y)=R(x,y)L(x,y)`，其中 `R` 是反射率，`L` 是照明；估计缓慢变化的照明，再减弱其影响以突出反射结构。取对数可把乘法写成 `log I=log R+log L`，但课件没有要求具体滤波器或多尺度公式。

**限制/易错。** 增强不等于拿到绝对真实颜色或恢复所有原本不存在的细节；过强处理可能放大暗部噪声、产生光晕或不自然外观。与多曝光 HDR 不同，Retinex 可以是一幅图像上的照明/反射处理，不必一定拍九张。

**答题模板：**“Retinex 属于图像增强方法，利用照明与反射的分离思想减少不均匀照明影响，使暗部、局部对比和颜色更容易观察。它改善视觉呈现，但结果仍受原始图像信息和噪声限制。”

### 3.11 视频防抖（video stabilization）：估计相机运动，再补偿画面

来源：[S03 PDF p.26]；课堂：2026-09-17 20:05 段 00:24:44–00:27:53，以及 00:27:53–00:41:14 长段中的总结。

**输入输出。** 输入是因手持、无人机或船舶晃动而抖动的视频，输出是相邻帧视角变化更平稳的视频。要解决的主要问题是相机不希望发生的运动，而不是要求场景中的人和车全部停止移动。

**课上流程。** 在连续帧中找角点或其他可追踪 feature points；比较相同背景特征的位置变化，估计相机向上/下/左/右等整体运动；再对图像作反方向补偿，使背景在时间上保持较稳定。理解补充：可先把估计的相机路径平滑，再重映射每帧到平滑路径，因此可保留有意的平缓摇镜；电子防抖常需要裁剪边缘。

**限制/易错。** 若特征全部来自独立运动前景，可能误把物体运动当相机运动；遮挡、纹理太少、大幅运动及透视差会使估计不稳。帧间防抖与帧内去模糊有区别：把每帧摆稳不保证长曝光造成的拖影同时消失。

**答题模板：**“视频防抖从相邻帧跟踪特征，估计相机造成的整体运动，再对各帧作相应的几何补偿，得到更平滑的画面轨迹。它主要修正帧与帧之间的相机抖动；运动去模糊则处理一帧曝光期间累积的拖影。”

### 3.12 运动模糊与去模糊（motion blur / deblurring）

来源：[S03 PDF p.27–30]；课堂：2026-09-17 20:05 段00:27:53–00:41:14（一个连续长转写段）。

**为什么会模糊？** 图像传感器在曝光时间内累积光，不是完全没有时长的瞬间采样。若相机或物体在这段时间明显移动，同一结构在多个位置留下贡献，形成拖影。p.27 分别示范全局相机运动与快速前景运动。老师用乒乓球、运动比赛及行驶小巴说明；缩短曝光有助冻结动作，但收光减少，需要考虑光照、光圈和感光设置。

**三项拍摄参数。** 老师提到 exposure time、aperture、ISO：曝光时间控制累积多久；光圈开口控制进入光量并影响景深；ISO 是成像信号增益/感光设置。**纠错：数字相机中提高 ISO 通常不使传感器本身捕获更多光子。** 帧率和曝光时间也不是同一个参数；高速视频往往同时关注足够高帧率和短曝光，不能仅靠标称 FPS 推断完全没有模糊。

**为何不能假设单一全局运动？** p.28 明确指出，物体不同部分相对于相机可能有不同速度；加上前景物体与背景运动不同，各处模糊不一定一样。小巴上部、车身、下部的图像位移可不同，单一平移/单一 blur kernel（模糊核）未必能解释全图。

**p.29 的处理框图应能逐模块解释：**

1. **Blurred video frames**：输入多个模糊视频帧，时间相邻帧提供运动证据。
2. **Foreground extraction → foreground mask**：找出要处理的移动前景，生成区域掩膜，减少背景对运动估计和恢复的干扰。
3. **Segmentation & corner detection → extracted corners**：利用区域信息，在前景中分割并找可追踪的角点/特征。
4. **Feature tracking with HBMA → tracked corners**：图中称 HBMA 的跟踪模块把帧间相同特征对应起来；课件未展开 HBMA 缩写，复习不臆造全称。
5. **Motion estimation**：从特征轨迹估计物体运动/速度及可能的局部差异。
6. **Calculated blur kernel**：根据曝光期间运动估计形成描述像素如何被摊开的模糊核。
7. **Deblurring → deblurred result**：依据模糊模型恢复更清晰的前景。p.30 展示车身标志、路线文字等局部细节改善。

理解补充：常用模型 `blurred ≈ sharp * kernel + noise` 解释为什么先估计 kernel 再恢复；逆过程会受噪声和信息损失影响，不能保证完全恢复车牌或文字。这里星号指卷积，并非逐像素乘法。

**答题模板：**“运动模糊由曝光期间相机或被摄体运动造成，是不同瞬时位置在一帧中的累积。去模糊可先分离移动前景，跟踪角点估计运动，推算模糊核，再依据该核恢复图像。不同对象或同一物体不同部位可能有不同相对速度，所以不能总用一个全局运动模型处理整幅图。”

### 3.13 人脸检测、识别与特征：先分清任务

来源：[S03 PDF p.31、35–49]；课堂：2026-09-17 20:05 段 00:41:14–00:47:30。

**Face detection（人脸检测）** 输入整张图，输出哪里有人脸及其区域/框；回答“有没有脸、在哪里”。**Face recognition（人脸识别）** 输入人脸或其特征，输出身份匹配/相似度；回答“是谁，或是否同一个人”。**Tracking（跟踪）** 在连续帧中维持同一目标的时间关联；**3D reconstruction（重建）** 从观察图像推断三维几何和外观。一次系统可能串起这些模块，但它们的输出不一样。

**早期人工特征思路。** 先找眼、鼻、口等局部，再用位置关系、眼间距、眼到鼻/口距离等形成特征向量。两人脸的特征距离近，可支持“可能同一人”。问题是表情、姿态、投影、遮挡和相似外观会改变或混淆这些数值；一个人微笑和生气时的嘴部几何就可能不同，双胞胎也说明相似特征未必唯一。不能把找到两个眼睛就等同于证明身份。

**答题模板：**“检测定位人脸，识别比较身份，跟踪维持时间关联，重建生成三维表示。早期人工特征识别用面部几何或纹理形成向量，但特征会受姿态、表情和遮挡影响，因此需要更稳健的建模与匹配。”

### 3.14 Haar 特征、AdaBoost 与扫描：Viola–Jones 思路

来源：[S03 PDF p.31]，含矩形特征示意和逐级拒绝窗口的分类图；课堂：2026-09-17 20:05 段 00:41:14–00:46:26。

**Haar-like feature 是什么？** 用邻接亮/暗矩形区域的亮度和之差描述局部结构，例如眼区往往比其下方脸颊暗，鼻梁与旁侧区域亮暗不同。输入是候选图像窗口，输出是一组数值特征；单个特征只提供很弱的人脸证据。课件说它能高效计算；用积分图快速求矩形和是常见实现背景（理解补充），本课该页没有展开公式。

**AdaBoost 的作用。** 从许多弱特征/弱分类器中选择和组合，形成更强的分类器，而不是假定某一个矩形模板就能可靠判断所有人脸。p.31 右下图还显示：图像子区域依次通过多级检查；任一关判为 non-face 就尽快拒绝，全部通过才判为 face。这种 cascade（级联）让大量背景窗口不必做最贵的后续计算。弱学习器组合与级联是相关但不同的结构，答题可分别说清。

**如何找到整张图中的脸？** 用窗口扫描不同位置，并尝试不同尺度（或缩放图像）以适应近大远小的人脸；对每个候选窗口提取特征并分类。扫描解决位置未知，尺度搜索解决脸大小未知，分类器解决窗口是否像脸。

**限制/易错。** 光照、遮挡、大侧脸与与脸相似的纹理可能带来误检/漏检。Haar 是特征表示，AdaBoost 是组合/训练方法，滑动窗口是候选位置搜索；三者不能作为同一个东西互换名称。该页给的是经典方法，不是说所有现代人脸检测器都仍用它。

**答题模板：**“Viola–Jones 式检测在不同位置与尺度扫描窗口，计算可快速得到的 Haar 矩形亮暗特征，用 AdaBoost 组合弱分类器形成可靠判断，并以级联尽早排除大量非人脸窗口。它输出人脸位置，不直接给出人的身份。”

### 3.15 头部模型、跟踪与 tripwire 人数统计

来源：[S03 PDF p.32–34]，尤其 p.33 的 q₁–q₈ 控制点及不同侧视角轮廓、p.34 的过线截图；课堂：2026-09-17 20:05 段 00:48:11–00:50:56。

**模型式头部跟踪。** 输入连续视频，输出每个头部的位置、轮廓与轨迹。用若干控制点定义一个可变形头部轮廓，把模型拟合到图像边缘；q₁–q₈ 控制点改变后可得到不同头形及从左到右的侧视外观。随后在相邻帧更新位置与模型，维持同一个头部的关联。

**Tripwire（虚拟绊线/过线）计数。** 在出入口画一条虚拟线；当某条已跟踪的头部轨迹越过该线时，记录一次通过，可按方向分别累计进入/离开人数。p.34 在过线时截取头部图像作记录。与“每帧检测到几个头”相比，持续跟踪能避免同一个人连续十帧出现就被计十次。方向和防重复的具体规则是理解补充，但它们解释了为什么需要 tracker。

**模型式方法的限制。** 帽子、遮挡、人群拥挤或类似头部轮廓的包都会产生歧义；老师举衣服上的人脸图案和前抱背包等例子说明“看起来像头”不等于真的有人。跟踪还可能在相互遮挡后交换身份；计数系统必须把检测、时间关联及过线事件联合考虑。

**答题模板：**“头部跟踪用可变形形状模型拟合视频中的头部，并在帧间维持轨迹。过线计数把虚拟线与轨迹结合，只在同一目标穿越时触发计数。轮廓相似的非头部物体、遮挡和轨迹断裂会导致误检、漏计或重复计数。”

### 3.16 3D 人脸重建：为什么要把侧脸变成正脸

来源：[S03 PDF p.35–37、43–46]；课堂关联：2026-09-17 20:05 段 00:46:26–00:52:22 的模型式方法解释。

**问题与目标。** p.35 的示范软件对正脸与正脸比较较好，p.36 侧脸与正脸比较失败。原因是同一张脸在不同视角下的二维投影、可见区域与尺度会改变，部分五官还会被自身遮挡。这里说的是示范系统的姿态限制，**不是所有人脸识别算法在任何年代都只支持正脸**。

**完整输入输出。** 输入一张非正面人脸图像，估计此人的三维面部形状、相机姿态及表面纹理，再渲染出标准正面图像；把新正脸交给原来偏好正脸的识别系统，与 gallery（注册图库）比较。重建本身输出几何/纹理或规范化图像，最终身份匹配仍是后续识别模块。

**p.37 的四段主流程必须记住：** `Facial feature detection → 3D modeling → Pose estimation → Texture map rebuilding`。四段分别回答：图像里关键五官在哪？这个人脸的三维形状是什么？脸/相机朝向怎样？如何把图像外观贴回三维表面并生成其他视角？以下四节把每个子模块展开。

**答题模板：**“侧脸与注册正脸存在姿态和可见区域差异。先定位面部特征，拟合个体三维模型并估计姿态，再重建纹理并渲染正脸，可以减小姿态对匹配的影响。该方法是输入规范化策略，不能保证恢复看不见区域的真实细节或确保识别永远正确。”

### 3.17 3D 重建模块一：AAM 定位面部特征，比较多种视角模型

来源：[S03 PDF p.38]。

**Active appearance model（AAM，主动外观模型）** 用可变形的面部形状与外观模式去拟合输入图像，从而定位详细面部 landmarks，例如眉眼、鼻、嘴和脸部轮廓。它的任务不是先输出身份，而是产生后续三维拟合需要的可靠二维特征位置。

课件为 frontal、half-profile、profile（正脸、半侧脸、侧脸）准备三个不同外观模型。将每个模型分别尝试拟合输入，比较 residual error（残差/模型预测与观测的不一致），选择残差最小者。这样做的原因是正面和侧面的可见结构不同，一个仅适合正脸的模型很难准确解释完整侧脸。

**输入 → 过程 → 输出：** 人脸图像 → 分别调整三个 AAM 的位置/形状/外观使之匹配 → 计算拟合残差 → 选最小残差 → 输出所选模型和关键点。理解补充：这里比较的是拟合质量；残差最低不自动等同于“此人身份已经确认”。遮挡、极端姿态、模糊或模型训练范围不足都可能使最佳拟合仍然错误。

**答题模板：**“特征检测阶段用正面、半侧面和侧面三个 AAM 分别拟合输入人脸，比较重建/拟合残差，选择误差最低的模型以定位面部关键点。多视角模型使可见五官随姿态变化时仍有适合的结构约束，为后续个体三维建模提供二维对应点。”

### 3.18 3D 重建模块二：网格、个体形状修改与纹理坐标

来源：[S03 PDF p.39–40]。

**3D mesh（网格）是几何。** 顶点（vertices）给三维位置，小面片（facets）连接相邻顶点形成表面。p.39 示例用 6292 个顶点、6152 个面片；数字描述该项目采用的模型精度，不是“人脸天生由固定数量顶点组成”。p.40 一排正/侧模型说明基础脸形可调整，得到不同人的头脸轮廓与五官几何。

**个体化修改怎样工作？** 用上一阶段得到的眼、鼻、嘴和轮廓对应点约束通用三维人脸，把模型调整成更符合这个人的形状。理解补充：可以理解为调节少量形状参数或若干顶点位置，让投影后的模型特征贴近观测关键点。网格表达的是脸凸凹与形状，不只是把二维照片贴到平板上。

**Texture map（纹理图）是表面外观。** 二维纹理图保存面部颜色/细节；texture coordinates（纹理坐标，常称 UV）说明三维表面每个位置对应二维纹理图的哪里。几何告诉“表面在哪”，纹理告诉“表面长什么样”，纹理坐标建立二者的映射。只改颜色不会改变鼻子的三维突出程度，只改网格也不会自动给出皮肤、眉毛等颜色细节。

**答题模板：**“三维建模阶段把通用面部网格按输入关键点调整为个体形状。顶点与面片表示几何；二维纹理图表示皮肤和五官外观；纹理坐标把二维颜色映射到三维面片。这三者配合才能从不同角度渲染该人的面部。”

### 3.19 3D 重建模块三：姿态估计（pose estimation）

来源：[S03 PDF p.41]。

姿态估计要回答三维模型如何相对于摄像机放置，才能在图像上得到观察到的五官位置。输入是二维面部关键点和对应的三维模型；输出是脸/相机的朝向以及使模型与图像对齐的变换参数。课件图先展示通用网格关键位置，再叠加到真实侧脸，说明需要把模型正确旋转、定位。

**理解补充的过程：** 建立二维与三维特征对应 → 调整旋转、位置和投影尺度等 → 让模型投影点与输入点误差尽量小 → 得到输入姿态。姿态是“这个人当前朝哪”，几何形状是“这个人的脸是什么样”；两者都能改变二维轮廓，但意义不同，不能把一个人转头解释为脸形本身改变。

**为什么不能省？** 如果不知道输入是侧脸还是正脸，纹理采样将贴到错误表面，重建的正脸也会出现歪斜或五官错位。相机模型与三维形状本身的不确定也会限制姿态精度。

**答题模板：**“姿态估计把三维模型关键点与输入图像二维关键点对齐，求出模型相对摄像机的旋转和位置/尺度，使其投影解释当前面部视角。它把个体几何与当前拍摄朝向区分开，为正确采样纹理及生成标准正面视图提供条件。”

### 3.20 3D 重建模块四：纹理重建、补洞、渲染与最终识别

来源：[S03 PDF p.42–46]。

**p.42 的图应按模块理解。** 纹理、纹理坐标与三维网格配合 Rendering（渲染）产生面部图像；把输入图像已观察到的表面颜色映射到模型时，侧脸背向摄像机的一侧可能缺数据，因此需要 Fill & Interpolation（填充与插值）；再做 Postprocessing（后处理）以减轻拼接/色调等不连续，得到较完整外观。课件给流程示意，没有指定唯一插值公式，不能把某种具体神经生成方法当成该页原内容。

**三个词的可回答定义：** Rendering 是从三维几何、纹理和视角生成二维图像；fill/interpolation 是给未采样或稀疏区域补可用值；postprocessing 是改善重建结果边界、亮度或外观一致性。插值/模型补全不是直接观测，所以隐藏侧的痣、疤或精细纹理不能保证被真实恢复。

**p.43–45 的应用链。** p.43 显示从不同人物照片重建正面和其他朝向；p.44 把输入侧脸经过 Face Reconstruction 变成正脸；p.45 再用重建正脸送入原识别软件，示例能够匹配原来的注册正脸。由此应答“先重建再识别”而不是“重建自动就是身份验证”。

**p.46 的结果怎么读？** 四组示例中，非正脸与 gallery 正脸的相似度分别是 `0.7714、0.3341、0.1151、0.0000`；重建后的对应分数为 `0.8720、0.5469、0.6988、0.8474`。这些是该示范系统对各例的相似度，表明规范化后更接近注册图像，**不是 87.20% 等通用识别准确率，也不是统计大样本性能**。不同软件的分数尺度与判定阈值也可能不同。

**答题模板：**“纹理重建把可见人脸颜色映射到个体三维模型，补全未观测区域并作外观后处理，再从标准正面视角渲染。这样可缩小侧脸与 gallery 正脸的姿态差异，提高示例中的匹配相似度；但补全区域依赖模型推断，不能把相似度分数当作准确率或保证所有侧脸都能识别。”

### 3.21 人脸识别限制、Face ID 与从人工特征到学习特征

来源：[S03 PDF p.47–49]；课堂：2026-09-17 20:05 段 00:50:56–00:55:47。

**眼镜的两种不同例子。** p.47 引述特别设计的镜框可让自动人脸系统漏认或错认成他人，说明经过设计的外观变化可操纵模型特征。p.48 则讲普通外观变化如戴眼镜，也会影响人类对不熟悉面孔的辨认。一个是对自动系统的针对性扰动例子，一个是人类陌生脸认知限制；不能把两者都说成“所有眼镜都能破解所有识别系统”。

**p.49 的 Face ID 例子。** 图示包含 dot projector、infrared camera、flood illuminator，以及环境光/接近传感器、前置摄像头等部件。可理解为主动投射结构化光并观察面部，取得超出普通二维彩色照片的几何/深度信息，再用于脸部匹配。图中是在说明产品把多种光学传感器与算法组合，不能从此页推出某代所有规格、识别率或绝对防伪能力。理解补充：深度使真实三维脸与平面照片更易区分，但实际防攻击能力仍取决于完整系统。

**老师归纳的技术演进。** 第一类依赖人工设计的五官/几何特征；第二类用可变形形状、appearance 或三维模型拟合，借助模型容忍一定表情与姿态变化；第三类通过深度网络从大量样本学习特征和匹配表示。其差异在于有用特征由人手指定多少、由数据学习多少，而非“后面一代不需要特征”。神经网络仍需要合适数据、训练和评估，不能依据课堂例子里的约数宣称某代系统固定 40%/90% 准确率。

**答题模板：**“人脸识别的可靠性受姿态、光照、遮挡、外观变化与特征设计影响。模型式方法用几何/外观约束提高稳定性，学习方法从样本自动学习更强特征；主动深度传感还能提供二维照片没有的几何线索。但外观扰动与未见条件仍可能造成错误，必须针对具体系统和条件评价。”

### 3.22 步态识别（human gait recognition）与 Bag-of-Gait

来源：[S03 PDF p.50–54]；课堂：2026-09-17 20:05 段 00:55:47–00:59:08。

**步态是什么、为什么能识人？** Gait 指行走时身体、四肢随时间变化的方式，是 behavioral biometric（行为生物特征）。即使看不清脸，也可能从身形、步幅和摆臂节奏判断熟人。p.50 用 KGB/gunslinger gait 新闻作直觉示例；它不是严格证明某个群体的全部个体均可由一只手姿势识别。p.51 强调低分辨率、远距离、脸部只占很少像素时，整个人的轮廓运动仍可提供信号。

**码本与 codewords。** p.52 给 16 个典型轮廓姿态作为 codewords，组成一个“行走姿态字典”。一段视频先分离行人 silhouette（轮廓/剪影），再把每帧轮廓与字典中的典型姿态比较，编码成相应特征。p.53 以六项简图示范某帧匹配第 2 个 codeword，形成 `010000`；这是“如何从图像变为向量”的示意，不是所有步态系统都用六位或 16 维。

**理解补充：Bag-of-Gait 的整段表示。** 将序列中各类姿态的出现累积/统计，得到可比较的特征向量，数据库为每个人保存对应表示。查询轨迹同样编码，再比较向量相似度，输出候选身份。若采用纯 bag 统计，部分精确时间顺序可能被弱化或丢弃，因此不能无条件声称该示意保存了全部运动顺序。p.54 是跟踪/识别演示界面，说明它是跨帧应用而非单张脸部比对。

**限制/易错。** 行走视角、速度、衣着、背包、伤病、遮挡和背景分割质量都会改变外观；低分辨率提供潜力并不表示任意少的像素都足够唯一识人。步态是动态行为特征，人脸和指纹主要提供外观/生理线索；它们可互补而非必须替代。

**答题模板：**“步态识别利用行走时的轮廓和动作模式作为生物特征。可先从视频分割行人轮廓，与预定义姿态码本匹配，将序列编码为 Bag-of-Gait 特征向量，再与数据库比较。它对远距离、脸部低分辨率场景有价值，但受视角、衣着、携物及分割误差影响。”

### 3.23 视频检索（video retrieval）：编码、分割、跟踪、特征、索引与查询

来源：[S03 PDF p.55–59]；课堂：2026-09-17 20:05 段 00:59:08–结尾中关于 retrieval 的连续说明。

**任务。** 输入长期视频资料以及检索请求，输出包含相似人/车等对象的视频片段、对象记录或时间位置。系统不能只保存压缩视频然后期待自然知道“哪辆红色小巴在几点出现”；需要从媒体中提取可查找的表示，并关联原视频。

**p.55 的完整数据流：**

1. **Video source → H.264/MPEG-4 encoder → compressed video streams**：视频编码与存储分支保存媒体本体，减少传输/存储量。
2. **Motion vectors and background model → moving object segmentation**：运动信息和背景模型协助区分前景移动对象。压缩运动向量可作为线索，但不应无条件等同于真实物体的完整物理速度（理解补充）。
3. **Tracking**：把同一个对象在连续帧中的检测关联成轨迹，避免把每帧出现都当新物体，并获得路径/方向信息。
4. **Feature extraction for each tracked object**：为每条对象轨迹提取颜色、边缘/形状、大小和路径等描述。
5. **DB**：存特征/metadata、对象或轨迹标识，以及返回原视频所需的时间/位置关联。
6. **Retrieval request → DB matching → results**：把用户请求转成同类特征，与数据库索引匹配，再返回相关内容。

**p.56 的索引图。** 从视频中的行人框，提取 Color Distribution、Edge Feature、Size、Path 等 metadata，放入 indexed metadata database。图底部 `VIDEO DATA → ANALYTICS METADATA → INSIGHTS` 表示“原始画面 → 可搜索描述 → 更高层理解”。**压缩和索引的目的不同：压缩减少保存媒体的字节，索引建立支持查询的内容表示。** 二者在系统里合作，不能互相替代。

**p.57 的两个可计算特征。** Color histogram（颜色直方图）统计红、黄、蓝、紫、绿等色彩的分布；edge orientation histogram 统计 0°、45°、90°、135° 等边缘方向出现的数量，提供粗形状结构。将两者连成向量，可同时描述“颜色像不像”和“轮廓方向结构像不像”。理解补充：直方图弱化了精确空间位置，可能把颜色比例相同、布局不同的对象混在一起；照明和视角也会改变特征。

**p.58–59 的查询例子。** 系统可用对象照片（小巴、行人）作为 query，也展示手绘形状/颜色的车辆或人的查询；把查询与库中对象变成可比较特征后，返回一组相似候选。它不要求图像逐像素一样，排序结果是依据所选特征和相似度。红色物体很多时，只靠红色无法保证找到指定车；可以组合形状、轨迹与其他信息。

**与 Shazam 对应。** Shazam 的索引依据音频时频峰值；视频检索依据对象外观/运动特征。二者都先对库里项目建表示与索引，再把查询变成相同表示并比较。老师说现代系统可自动学习更强特征，是表示方式的演进；“索引 → 查询表示 → 相似度/匹配 → 返回内容”的流程仍成立。

**答题模板：**“内容式视频检索先从视频中分割和跟踪对象，为每条轨迹提取颜色、边缘、大小和路径等特征，并将这些 metadata 与原视频时间位置关联后建索引。查询图片或草图经过相同特征处理，再在库中比较并排序，返回相似对象片段。检索效果依赖特征能否区分目标，以及分割与跟踪是否可靠。”

### 3.24 元宇宙访谈：实时 3D 化身的综合系统

来源：[S03 PDF p.60]；课堂：2026-09-17 20:05 段 00:59:08–结尾中检索之后的 VR/重建讨论。

课件以 Lex Fridman 与 Mark Zuckerberg 的虚拟访谈展示，远程双方可通过数字化三维外观进行交流。与只传二维摄像头视频相比，系统可使用人物三维模型，并将当前表情和动作反映到化身上；它综合了人脸/头部获取、几何与纹理重建、动作估计、网络传输和渲染。

**理解补充的数据流。** 先建立人物模型 → 实时捕获面部/头部动态 → 提取需要更新的状态或参数 → 经网络送到对方 → 在共同的模型上渲染对应动作，同时同步音频。重点是“静态个体模型 + 随时间变化的状态”可以共同表达一次交互。课件没有给完整通信协议或准确延迟；录音中约 30–40 ms 的口述不能直接当该产品端到端性能保证。

**答题模板：**“实时三维化身交流需要先建立可渲染的人物模型，再连续估计表情和头部动作，并传输动态状态、在接收端更新模型与音视频输出。它将传感、分析、建模、传输、同步和呈现连接成一个多媒体系统；延迟和模型真实性会影响交流体验。”

### 3.25 DIKW：数据怎样变为信息、知识和行动

来源：[S03 PDF p.61]；课堂：2026-09-17 20:05 段 00:59:08–结尾中元宇宙之后的 DIKW 与客服分析例子。

**Data（数据）。** 传感器读数、原始音频、视频、位置或交易记录等观测；可以是结构化数值，也可以是未组织的多媒体内容。底层 Data Acquisitions 是获取这些观测，尚不能只凭大量原始数据直接得到合理决策。

**从 Data 到 Information（信息）。** 课件列 data tagging、cleansing、correlations：标注各字段/事件的含义，处理错误/重复或缺失，连接有关系的数据，把原始观测整理成可解释的结构。Reporting、dashboards、business analytics 将结果呈现为趋势、统计或事件信息。例如“某型号一周有六次同类投诉”比六段没有标签的录音更易理解。

**Knowledge（知识）。** 在信息中辨认规律、关联和原因线索，支持预测、insights 与 decision making。知道某类投诉集中于某区域/功能，或设备某种振动模式常出现在故障前，是把信息组织成可用于判断的知识。相关性本身不自动证明因果（理解补充），需要领域知识和进一步核对。

**Wisdom（智慧/合理行动）。** 将知识与目标、成本、风险及实际情境结合，选择该采取的措施；课件在顶层对应 prescriptive analytics。预测说“可能发生什么”，规范/处方分析进一步说“建议做什么”。层级间不是把文件改名，也不是输入任何数据就自动确定唯一正确行动。

**课堂客服案例完整展开：** 客服对话录音是 Data；先清除噪声、做 speech-to-text 和语气/情绪分析，得到投诉内容与不满迹象；把录音按产品型号、功能、时间等标注并聚合，形成某型号重复问题的 Information；从集中出现的投诉发现需要排查的故障模式/风险，形成 Knowledge；系统报告并通知产品/管理团队调查、调整产品或服务，是以知识支持行动。这里发通知是课堂案例，不是本学习材料要自动执行的指令。

**为什么需要领域知识？** 音频、图像、温度和股价的采样结构与含义不同，不能只因都变成数字就使用完全相同的清理和分析方式。老师反复强调，若不懂媒体表示和业务含义就直接喂给分析系统，会造成 garbage in, garbage out，最后得到错误决策。

**答题模板：**“DIKW 描述由观测到行动的提升：Data 是原始记录；经标注、清洗和关联得到有上下文的 Information；从中发现规律并作解释/预测形成 Knowledge；再结合目标和情境选择措施体现 Wisdom。以客服为例，录音经过语音识别和标注形成投诉统计，再发现集中故障线索，最后推动调查或产品改进。”

### 3.26 日常分析案例与智慧城市：把整章方法迁移到场景

来源：[S03 PDF p.62–63]；课堂：2026-09-17 20:05 段 00:59:08–结尾后半的多媒体、手机传感器与城市传感案例。

**p.62 的全部示例要会归类，而非死记公司名单。** 这张图是“不同领域的数据支持何种决策”的案例图，不代表课上给出每个领域的算法：

- Caterpillar：跟踪设备、提高使用效率、管理燃油和维护成本；Union Pacific：预测迫近故障。核心是设备状态数据 → 风险/效率信息 → 维护或运营行动。
- Hospitals：早产儿感染相关分析；核心是监测信号/临床数据 → 异常或风险提示。这里是课程应用例子，不构成诊疗建议。
- Google Maps：行程时间与实时交通；Airlines：高峰需求价格与安全问题；McDonald’s：drive-through 等待时间。核心是时空/运营数据 → 负载、时延或风险估计 → 调度和服务优化。
- Baseball：比赛活动与统计关联；核心是动作/事件 → 可比较的表现指标。
- Facebook：朋友推荐；Netflix：基于历史的内容推荐；Grocery stores：基于历史的优惠券；Consumer sales：会员卡与消费历史；Anheuser Busch：产品趋势。核心是行为历史与关系 → 偏好/关联 → 推荐或营销。
- Morgan Stanley：投资洞察与风险模式；Banks 和 State Farm：欺诈识别；Utility companies：按需求制定费率。核心是序列/交易/需求数据 → 模式与异常 → 风险或资源管理。

**Smart city 的完整链条。** 分布在城市中的传感器获取环境、交通、设施与人的活动；数据通过网络进入平台，经过清理、整合和分析产生监控、预警或控制动作。例子包括水管声学测漏、燃气监测、风速测量、桥梁振动监测、路面/交通视频分析。p.63 用 Mario/水管工及传统听漏工具引出“过去人到现场用耳朵听，现在可用传感器持续采集”的变化，重点是把物理现象转成可分析的数据。

**手机是小规模综合例子。** 麦克风感知声音、环境光传感器感知照明、运动传感器感知姿态，系统把传感输入映射到音量、降噪、亮度、旋转或交互输出。城市系统将类似的“感知 → 分析 → 行动”扩展到多地点、多媒体和公共设施；并不是把一座城的所有信号放进同一种图像算法。

**限制/易错。** 传感器覆盖与准确度、时间和位置对齐、缺失数据及错误解释都会影响结论。监测到异常不是已经知道所有原因；预警也不等同于保证预测所有事件。温度、风速、振动等非影音传感数据也可进入广义的多源媒体系统。

**答题模板：**“智慧城市把分布式传感、网络、数据管理和分析连成闭环：采集交通/环境/设施观测，按媒体和业务含义清理融合，提取状态与异常，再给出预警或控制。水管测漏可以把管道声音转成数字信号，分析异常声学模式并定位待排查区域；这体现了从数据获取到信息、知识和行动的全过程。”

### 3.27 本章可直接迁移的比较答法

来源：综合 [S03 PDF p.2–63]；以下题目是复习编写，不是已公布题目。

**Q：为什么同样是提高质量，HDR、super-resolution、防抖和去模糊不能当同义词？**

A：HDR 针对同一场景亮暗跨度超过单次可记录范围；super-resolution 针对空间采样不足；stabilization 针对相邻帧的非期望相机位移；deblurring 针对曝光期间运动形成的单帧拖影。它们可能联合使用，但输入缺陷、所估参数和输出改善维度不同。

**Q：如何按统一结构描述任何一个案例？**

A：先说输入与目标，再说表示、核心处理、输出与限制。例如“视频检索输入视频和查询图，先分割、跟踪，再提取颜色/边缘/路径特征并建立索引；查询转成同类特征，按相似度返回对象片段；光照、遮挡或弱特征会降低效果”。比只列“segmentation、tracking、DB”更完整。

**Q：为什么原始数据变成 bit 以后仍要区分音频、图像、视频？**

A：Bit 是共同的底层编码，但数据组织和物理意义不同：音频主要是一维时间序列，图像是二维空间采样，视频是带时间的图像序列。有效的滤波、特征、压缩和模型必须保留对应结构和领域含义；忽略这些差别会破坏信息或产生错误结论。

**Q：人工特征、模型式方法、深度学习的核心区别是什么？**

A：人工特征明确规定怎样度量眼鼻距离、颜色或边缘；模型式方法用可变形形状/外观等结构约束解释观察；深度学习从样本中学习复杂表示与预测参数。三者仍然需要恰当输入、表示和评价，学习特征并没有取消特征，而是改变特征的获得方式。

**Q：哪些地方真正体现人类感知对系统的影响？**

A：EQ 改变人听到的频谱平衡；心理声学压缩利用听阈和掩蔽，让有限比特优先保存可察觉内容；图像增强改善人在暗部或不均照明下的可见性；实时化身的延迟、同步和外观质量影响交流体验。系统输出要服务感知目的，不能只看处理后的数字是否与原来完全一样。

### 3.28 S03 逐页覆盖清单

本清单按 PDF 实际页号，包含只有图/演示的页面；封面和重复目录也列出以便确认没有漏页。

- p.1：应用章封面与主题，见 3.1。
- p.2：音频应用五类目录，见 3.3–3.8。
- p.3：耳机主动降噪的输入、反相输出与相消图，见 3.3。
- p.4：汽车麦克风、发动机信息、ECU、音响降噪架构，见 3.3。
- p.5：双麦克风语音/环境噪声参考与减法示意，见 3.3。
- p.6：更多麦克风的设问与旧手机例子，见 3.3。
- p.7：远场、背景声、功耗、过载点、尺寸及更多麦克风的历史文章，见 3.3。
- p.8：EQ 定义、频带、增益范围、预设，见 3.4。
- p.9：A/D、降噪归一化、短时分段、音素、统计到词，见 3.5。
- p.10：Shazam、约 10 秒查询、spectrogram、峰值及鲁棒性，见 3.6。
- p.11–14：数据库/查询 constellation map、时间平移、匹配峰值统计，见 3.6。
- p.15：LPC vocoder 与生理发声模型，见 3.7。
- p.16：声码器参数、音调/噪声激励、可变滤波器、GSM 与其他用途设问，见 3.7。
- p.17–18：MPEG 音频与耳结构/频率响应示意，见 3.8。
- p.19：听觉阈值、频率掩蔽与时间掩蔽，见 3.8。
- p.20：三个音频 Layer、1152 样本、32 频带、心理声学与可变长编码，见 3.8。
- p.21：音频应用回顾目录，见 3.3–3.8。
- p.22：图像/视频处理分析八类目录，见 3.9–3.23。
- p.23：Night Mode 多帧与不同快门速度，见 3.9；HDR 为对应录音补充。
- p.24：Deep Fusion 九帧历史案例，见 3.9；超分辨率为课堂补充。
- p.25：Retinex 港口画面增强，见 3.10；具体照明/反射公式已标理解补充。
- p.26：视频防抖示例，见 3.11。
- p.27：全局相机运动与高速物体两种模糊，见 3.12。
- p.28：同一对象各部位不同相对速度，见 3.12。
- p.29：前景、分割角点、HBMA 跟踪、运动估计、模糊核、去模糊流程，见 3.12。
- p.30：小巴细节恢复前后图，见 3.12。
- p.31：Haar、AdaBoost、级联、位置尺度扫描，见 3.13–3.14。
- p.32：多人头部检测/轨迹演示，见 3.15。
- p.33：q₁–q₈ 轮廓模型与左右视角，见 3.15。
- p.34：tripwire 过线人数与头部截图，见 3.15。
- p.35–36：正脸匹配成功、侧脸匹配困难，见 3.16。
- p.37：四阶段重建总流程，见 3.16。
- p.38：三种视角 AAM 与最小残差选择，见 3.17。
- p.39：6292 顶点/6152 面片、纹理图、纹理坐标，见 3.18。
- p.40：个体脸形模型修改，见 3.18。
- p.41：三维模型与侧脸姿态对齐，见 3.19。
- p.42：纹理重建、rendering、fill/interpolation、postprocessing，见 3.20。
- p.43：多个人物重建和视角示例，见 3.20。
- p.44–45：侧脸正面化并重新识别，见 3.16、3.20。
- p.46：四组重建前后 gallery 相似度，见 3.20。
- p.47：特制眼镜干扰自动系统，见 3.21。
- p.48：戴眼镜影响人类辨认陌生脸，见 3.21。
- p.49：Face ID 结构光、红外/补光、多个传感部件，见 3.21。
- p.50–51：步态生物特征、低分辨率行人轮廓序列，见 3.22。
- p.52–53：16 项姿态码本与 Bag-of-Gait 向量示例，见 3.22。
- p.54：步态跟踪演示界面，见 3.22。
- p.55：视频编码/存储、运动/背景、分割、跟踪、特征、DB/检索请求，见 3.23。
- p.56：对象颜色、边缘、大小、路径 metadata 与索引金字塔，见 3.23。
- p.57：颜色及边缘方向直方图，见 3.23。
- p.58–59：照片和手绘形状/颜色检索示例，见 3.23。
- p.60：Lex Fridman/Mark Zuckerberg 的虚拟访谈，见 3.24。
- p.61：DIKW、acquisition、tagging、cleansing、correlation、reporting、predictive/prescriptive，见 3.25。
- p.62：全部日常分析领域例子，见 3.26。
- p.63：Mario/水管工、听漏工具与智慧城市传感系统，见 3.26。

### 3.29 本章转写/课件歧义与使用边界

- **“voice/noise cancellation”“phase/face shift”混识：** 9/10 录音多个词被误识，应按 p.3–7 理解为 noise cancellation 和 phase shift；face detection 中 face 则确实是人脸。
- **“works”应为“words”：** p.9“map phonemes to works”是明显文字错误，语义为将音素映射成词；录音中的 alphabet 例子只是简化解释，不应把音素等同字母。
- **“high speed/ISBN/ID”混识：** 9/10 图书馆类比里转写多处 high speed，实际上下文指书的标识/索引；不逐字采信错词。
- **“MPEG/impact”“gait/gate”“mesh/mission”“gain/game”混识：** 均按对应课件术语校正。不要把 gate 当步态的正式拼写，或把 gain 误译为游戏。
- **频率数值：** 9/17 口述转写多次出现 2 Hz/200 Hz/20 Hz 与 20 kHz 的混杂；本章使用课件/标准概念的约 20 Hz–20 kHz，不引申为人人固定可听范围。
- **听觉机制：** p.17 将高低音敏感度简化为毛细胞毛长差异；理解应以耳蜗沿长度的频率选择性为主，不把单个细胞毛长当唯一决定因素。
- **掩蔽发生位置：** 人耳听不到某成分，不等于麦克风物理上一定采不到；MPEG 编码器依据感知模型分配数据，不能把编码逻辑全归给麦克风。
- **RGBA/位数计算：** 录音把 alpha、层级关系混在一起，且 4×4、Full HD 数据量有错读；3.2 已按透明度含义与准确乘法重算。
- **HD/DVD：** 录音里的“DVD 1280×720”不作为正确格式定义；1280×720 是常见 HD 720p。
- **音频 Layer 与版本：** Layer I/II/III 是音频编码层，MP3 为 Layer III，不是所谓 MPEG-3；26 ms 对应 1152 样本在约 44.1 kHz 下的时长。
- **相似度与准确率：** p.46 每例相似度不等于统计识别准确率；课堂关于 ASR/人脸“第几代多少准确率”的约数缺少数据集和条件，不用于定量结论。
- **旧产品/演示的适用范围：** 2016 年麦克风文章、2019 年九帧 Deep Fusion、示范软件仅正面好用、Face ID 组件图均是课件案例；不把它们当所有现售产品的最新通用规格。
- **没有在材料中展开的实现：** Retinex 公式、LPC 差分理解、卷积核模型、alpha 准确定义、跟踪防重复等已作为理解补充，用于能解释原理；它们不是老师公布的额外考纲。p.29 HBMA 未展开全称，p.16 vocoder 其他用途未给唯一答案，本章保留这种不确定性。

## 4. 传感器、数字化与声音采集（S04 全部内容）

本章依据 S04《Media Sensor and Reproduction - Part 1》PDF p.1–49；课堂补充来自 2026-09-24 的完整转写。以下把课件知识、课堂例子和为理解补充的推导分开说明。音频转写是 ASR 结果，技术词和单位一律用课件及数学关系核对，不能将识别错词当成新概念。

### 4.1 Sensor 是什么：把物理世界变成可用信号

**定义。** 传感器（sensor）测量一个物理量，把它转换成人或机器可以利用的信号。例如麦克风测量空气声压的变化，并输出电信号；相机感光元件把入射光转成电荷或电压；温度传感器把温度变成读数。传感器是多媒体系统中从物理世界进入信息处理世界的入口。[S04 PDF p.2–4]

**不要跳过中间过程。** `物理量 → 传感器的模拟电信号 → 调理/放大 → A/D 数字化 → 计算机分析` 是常见采集链路。传感器并不必然直接输出数字；“能测到声音”也不等于“能理解说了什么”。前者是 transduction/sensing，后者还需要特征提取、模型和语义解释。老师以温度“感觉冷热”和机器需要具体数值对比这一差别。（2026-09-24 转写 00:06:43–00:23:39）

课件按用途给出三组，分类可以有交叉：

- **模仿人的感官。** touch、sight、hearing、smell、taste 对应皮肤、眼、耳、鼻、舌；主要成熟多媒体输入是相机和麦克风。
- **测量生命/健康。** 体重、体温、心率、ECG、运动等，不必对应一种独立的传统“五感”。
- **测量环境事实。** 加速度、转动、地理位置、辐射、海拔等，使计算机获取人无法直接、精确或可靠感知的量。

**可直接答题。** “A sensor measures a physical quantity and converts it into a usable signal. Multimedia systems use microphones to acquire sound and cameras to acquire light, then digitize and analyze these signals. Sensors bridge the physical environment and computer representations, while interpretation requires additional processing.”

### 4.2 触觉：电阻、电容、压力检测与执行器

皮肤是人的触觉器官；人工 tactile sensor 把接触、压力等转为信号。触摸位置、接触面积、按压力度是不同的测量量，不应都笼统称为“感到压力”。[S04 PDF p.5–7]

**电阻式触摸（resistive touch，机制补充）。** 两层导电膜原本隔开，按压使它们接触；控制器根据接触导致的电压/电阻关系估计位置。通常需要实际压力，可用手指、戴手套的手或合适的触笔触发，适合某些工业、收银场景；多点触控能力取决于具体实现，传统结构的多点能力较弱。不能把某个商店设备的体验推广为所有电阻屏“完全不能多点触控”。

**电容式触摸（capacitive touch，机制补充）。** 导电手指接近或接触电极阵列，改变局部自电容或互电容，由控制器定位触点。轻触即可工作，常用来实现多点手势，例如双指缩放。普通绝缘手套会减弱耦合，水可能造成误触或影响定位；是否支持湿手/手套取决于设备设计。它主要检测电容变化，并非必须测得手指的按压力。

**3D Touch / force sensing。** 在位置输入以外增加“按得多重”的维度，把轻按和重按映射为不同命令，例如预览和打开。压力检测机制不能直接等同普通电容定位；课件用它展示输入维度增加。[S04 PDF p.6]

**反馈由 actuator 产生。** sensor 是输入，actuator 是输出。手机振动模块、Taptic Engine 将电信号转成机械运动，提供触觉反馈（haptic feedback）；触摸被检测后短振一下，使用户确认操作已发生。构成 `手指动作 → sensor → 控制逻辑 → actuator → 皮肤感知` 的交互回路。[S04 PDF p.7；2026-09-24 转写 00:23:39–00:26:40]

**比较题答案。** 电阻屏依靠压合导电层，电容屏依靠电容变化；因此两者在触发压力、手套/水的影响、多点触控实现上不同。执行器的任务是产生振动反馈，不能用“传感器产生振动”作答。

### 4.3 视觉不是相机拍下一张图就结束：感知、记忆和双眼视差

**人工视觉输入。** 相机利用光电效应把入射光变成电信号，课件列出 CCD 与 CMOS。感光点组成阵列，像素数增加通常允许更高的空间采样分辨率；但图像实际细节还受镜头、噪声、像素尺寸、曝光和处理影响，不能只看像素总数。[S04 PDF p.8；S05 的详细相机比较另见后章]

**“找不同”课堂实验。** 比较两幅图需要同时完成物体识别、分析空间关系、把前一幅图保存在短期记忆中、比较两幅图并记录/指出位置。课件用枕叶、顶叶、额叶的分工说明视觉涉及多个处理环节。应掌握功能分解，而不把一项复杂任务简单归到唯一脑区。[S04 PDF p.9–11；2026-09-24 转写 00:29:05–00:32:21]

**双眼视觉（binocular vision）。** 左右眼从略有不同的位置看同一物体，视网膜投影出现视差；大脑在两幅图之间建立对应，据此感知深度。单幅屏幕图也能通过 stereogram 的重复纹理/对应关系，让左右眼融合成有深度的知觉。这说明“二维输入”与“感到三维”不是同一回事。[S04 PDF p.12–15]

**立体图的观察方法。** 课件建议先把图靠近鼻端，使眼睛不能在图面正常对焦，再慢慢移远并保持视线像看向图后方；或将注意焦点放在图后约半米的位置。不同 stereogram 可能要求平行视或交叉视，课堂转写中的“cross eyes”不能一概代替课件具体示范方法。此演示的知识点是 binocular disparity 与大脑融合，不是强迫自己必须看出隐藏图。[S04 PDF p.13–15；2026-09-24 转写 00:32:21–00:34:34]

**可直接答题。** 视觉感知包括获取光信号、识别内容、分析空间关系和结合记忆等步骤；双眼的不同投影可以提供深度线索。因此提高相机像素数只能改进输入的一部分，不能自动完成视觉理解。

### 4.4 听觉传感器：dynamic 与 condenser microphone

麦克风（microphone）是 acoustic sensor，将声压变化转为电信号。声压推动 diaphragm（振膜）运动；不同麦克风用不同换能机制，把这个机械位移转换成电压、电流或电容变化。[S04 PDF p.16–17、43]

**动圈式（dynamic microphone）。** 振膜带动线圈在磁场中运动，磁通变化产生感应电压；这是 electromagnetic induction。典型被动动圈换能器本身无需外部供电，结构坚固，适用于舞台、人声和较高声压的场景。注意“麦克风不需供电”仅指该被动换能机制：无线发射器、附加前置放大器仍可能需要电源。[S04 PDF p.16；机制与课堂补充：2026-09-24 转写 00:35:01–00:38:12]

**电容式（condenser microphone）。** 振膜与固定背极板构成电容；声压改变极板距离，从而改变电容，配合偏置及电子电路得到电信号。简化关系为 `C = εA/d`：距离 d 改变会改变 C。常见电容麦需要供电用于偏置/内置电路，例如 phantom power 或电池；electret（驻极体）形式有永久极化材料，但内置阻抗变换电路通常仍需供电。常见设计灵敏度高、瞬态响应好，适合细节采集，但是否更“好”取决于用途、噪声与型号，而非价格或这两个类别本身。[S04 PDF p.16–17；理解性补充；2026-09-24 转写 00:37:55–00:43:40]

**选择题答法。** 两者输入都为声压、输出都为电信号；dynamic 用磁场中的相对运动感应，condenser 用振膜与背板间电容变化。换能原理与指向性是两个独立维度：不能说“动圈一定是心形，电容一定全向”。

### 4.5 其他感觉、健康与环境传感器

**嗅觉与味觉。** 课件强调其化学/物理机制复杂，本课重点放在视觉与听觉。复习时应写“较难通用地重现人的嗅觉/味觉”，不能把 p.18 的“没有人工鼻舌”当成永远成立的事实；电子鼻/电子舌可以针对特定化学物质或模式检测，仍不等于完整复制人的体验。[S04 PDF p.18；课件表述的适用范围说明]

**其他物种的感知。** 温度、重力、磁场、湿度、红外都是课件例子：某些动物的感觉范围与人不同，人工系统也可以通过对应传感器测量这些量。多媒体不能只按人能看到和听到的范围理解，因为机器可以采集人类感官范围之外的信息。[S04 PDF p.19]

**生命/健康相关。** [S04 PDF p.20–21]

- 体重传感器测质量/体重。标准 BMI 关系是 `BMI = 体重 kg / (身高 m)²`；年龄和性别可能参与健康解释，但不是标准 BMI 公式的必需输入，不能照抄成“BMI 公式还必须包含年龄性别”。
- 温度传感器测体温；噪声传感器监测是否处于高噪声环境；心率传感器估计每分钟心跳次数。
- ECG 测心脏电活动，能够支持分析节律等；它不只是一个“心率数字”，也不能从单个测量量自动推出所有健康结论。
- 运动传感器测加速度/活动，结合心率与个人参数可以估计能量消耗。这里的“消耗卡路里”是模型估计量，不是加速度计直接测出来的物理量。
- Care-on-Call 老人照护例子：穿戴设备持续采集状态，异常触发通知或呼叫响应。重点是多传感器、持续监测、事件检测与服务流程的结合，不必记某一示例设备的全部产品细节。（2026-09-24 转写 00:43:40–00:46:02）

**环境相关。** [S04 PDF p.22]

- **Accelerometer（加速度计）** 测加速度/比力，可结合重力方向估计静态倾斜，也能从步态周期估计步数；它并不直接测 GPS 位置。
- **Gyroscope（陀螺仪）** 测旋转角速度，积分可估计角度变化，但可能积累漂移；“加速度计测平移、陀螺仪测转动”是基础区别。
- **GPS receiver** 根据卫星定位信息估计位置，不是测方向旋转的器件。
- **Radiation sensor** 测辐射；**altimeter** 测/估计海拔，例如气压式高度计利用气压与高度关系。
- 人在飞机等环境可能产生 spatial disorientation（空间定向障碍）。仪表提供独立测量，有时比主观感觉可靠；“客观传感器完全无误差”仍然不成立，下一节正是其限制。

**可直接答题。** 多传感器把不同物理量结合起来，可以扩大观测范围、降低单一感觉的歧义，并支持健康监测或定位服务；但最终的活动/健康/状态结论通常需要模型解释，而不只是读取一个 sensor 数字。

### 4.6 Sensor limitations：动态范围、偏置、非线性、迟滞

**动态范围（dynamic range）。** 是可用输入最大与最小量级之间的范围。低于可检测下限，信号被噪声淹没；高于上限，输出可能饱和/削顶。同一张照片中高光和阴影差异过大时，曝光保护阴影可能丢高光，保护高光可能丢阴影。HDR 可用不同曝光/多个传感器获取互补范围，再对齐融合；对象运动和传感器不一致可能使融合困难。[S04 PDF p.23；2026-09-24 转写 00:49:03–00:55:10]

**不能把两个“范围”混为一谈。** 8 bit 数值编码提供 256 个数字码，但物理传感器真实动态范围不等于“只能拍 0–120 或 120–240”。课堂用这类数字作直觉例子；严谨理解是噪声下限、饱和上限、曝光与编码映射共同决定能保留多少实际场景明暗细节。

**偏置（offset / bias）。** 输入为零时输出不为零。线性模型 `y = kx + b` 中 b 是 offset，k 是灵敏度/增益；已知校准参数时用 `x = (y−b)/k` 还原。例：遮住光线后图像仍有黑电平；无目标输入时测量仍有零点偏差。手机待机耗电并不是 sensor offset 的精确定义，考试应写零输入非零输出。[S04 PDF p.24；2026-09-24 转写 00:50:29–00:55:54]

**非线性（nonlinearity）。** 输入等量增加，输出不按等比例增加。例如高声压下麦克风开始失真，不能继续用单一 k 将输出还原为声压。可以限定 operational range 或使用校准曲线；要区分“频率响应不平坦”和“幅值关系非线性”，二者会带来不同失真/着色。[S04 PDF p.24；2026-09-24 转写 00:55:10–00:57:15]

**迟滞（hysteresis）。** 输出不仅依赖当前输入，还依赖到达该输入之前的历史。输入从低往高扫与从高往低扫，会沿不同响应路径；同一个输入可能给出不同输出，反过来一个输出也可能对应不同输入状态。例：施压后释放，读数未沿加载时的曲线返回。不能只定义成“反应慢”或“长期漂移”。[S04 PDF p.24；2026-09-24 转写 00:57:15 起]

**随时间/温度变化（drift，理解补充）。** 老师还说明设备工作温度改变可能使响应曲线变化。校准、温度补偿和定期复核有助于控制偏移；温漂与迟滞有联系但不是同一个术语。课件 p.24 把“Sensor Response Deviation over time”列在迟滞附近，答题时应分别定义，不要互相替换。

**应用题完整答法。** 先点名限制，再写影响，再给措施：例如“输入超过相机动态范围导致高光 clipping 和阴影细节缺失；可采用多曝光 HDR/多传感器融合扩大可捕捉范围，并处理配准和运动问题”。仅写“sensor 有局限，换更贵的”不能解释原理。

### 4.7 从乐高到信号：正弦波与频域分析

老师用 LEGO house 作比喻：不同复杂结构由少量标准积木组合；复杂传感器输出也可用不同频率、幅度、相位的正弦/余弦分量表示与分析。课件 p.26–27 的图把复杂波形与多个简单周期分量放在一起。此处核心是 **decomposition 与 composition**，不是要求本课推导完整 Fourier transform。[S04 PDF p.25–30；2026-09-24 转写 00:57:15–01:18:19]

基本波形可写为 `x(t) = A cos(2πft + φ)`：

- **Amplitude A（振幅）**：相对中线的最大幅值。对于声波，它与声压强弱有关；主观响度还取决于频率和听觉，不能直接等同一个线性的“感觉音量”。
- **Frequency f（频率）**：每秒周期数，单位 Hz；周期 `T = 1/f`。对有明确周期的音调，基频与音高有关。
- **Phase φ（相位）**：指定时间零点时波形在周期中的位置；决定叠加时峰谷怎样对齐。两条频率相同、振幅相同且相差 π 的波在同一位置叠加可相消。

**几何解释。** 匀速圆周运动的点投影到一个轴上，位置随时间变化得到正弦波。增大圆半径改变 A，转得更快改变 f，改变初始角度改变 φ。[S04 PDF p.28–30]

**时域与频域。** 时域描述“这个时刻的幅值是什么”；频域描述“有哪些频率、各自多少强度/相位”。同样基频的笛子与钢琴可能在频域中有不同谐波强度，因此听起来不同。一般非周期信号可用连续频谱/适当变换描述，不能把“任何有限波形都一定只由几个整数倍谐波精确组成”当成通用定律。（严谨性补充）

**可直接答题。** Fourier analysis decomposes a complex signal into sinusoidal frequency components. Each component is specified by amplitude, frequency and phase; analyzing these components helps filtering, recognition and synthesis. The LEGO analogy illustrates how different signals can share basic building blocks while differing in their combinations.

### 4.8 Digitization：sampling 与 quantization 分别离散哪个轴

**数字化不是只“变成 0 和 1”这一句话。** 模拟信号随时间连续，幅度也连续；计算机通常需要在两个维度上离散化。[S04 PDF p.31–33]

1. **Sampling（采样）离散时间轴。** 每隔 `Ts = 1/fs` 秒读取一次，获得 `x[n] = x(nTs)`。fs 为每秒样本数，单位 samples/s 或 Hz。fs 越高，相同时间内样本越多，能够保留的最高频率上限也提高。
2. **Quantization（量化）离散幅值轴。** 将每个样本映射到有限个可表示的级别；n bit 可表示 `L = 2^n` 个码。8 bit 为 256 级，16 bit 为 65,536 级，24 bit 为 16,777,216 级。随后用二进制编码存储这些级别。

**量化误差（quantization error/noise）。** 量化值与原样本值之差。级别越少，幅值刻度越粗，弱细节越易损失。对满量程范围 R 的均匀量化，常用近似步长 `Δ = R/2^n`；最近邻舍入且未过载时，`|e| ≤ Δ/2`。若采用端点都包含的码值标定，Δ 的分母可能写 `2^n−1`，做题须跟随题目定义，不能两式混用。（公式为理解补充）

**为什么数字形式相对抗失真？** 在误差未使接收端把 0/1 判错的范围内，数字数据可再生、复制和检查；模拟复制中小幅度扰动会叠加。但采样、量化、压缩、丢包、溢出都可能丢失信息，所以“数字化无损、永不失真”错误。[S04 PDF p.31–33]

**课堂明确练过的文件大小。** 未压缩 PCM 的原始数据量为：

`bitrate = fs × n × C`（bit/s）

`size(bits) = fs × n × C × duration`；`size(bytes) = size(bits)/8`

其中 C 是声道数。示例：5 s、每秒 1 样本、4 bit/样本、单声道，需要 `5×1×4 = 20 bit`；这是老师用于讲清“样本数乘每样本位数”的课堂小例子，不是实用音频采样参数。（2026-09-24 转写 01:24:02–01:29:24）

**实际计算例。** 44.1 kHz、16 bit、stereo 的未压缩 PCM：`44100×16×2 = 1,411,200 bit/s`，一分钟为 `10,584,000 bytes ≈ 10.584 MB ≈ 10.094 MiB`，未计文件头。48 kHz、24 bit、mono、10 s 为 `48000×24×1×10/8 = 1,440,000 bytes`。压缩格式如 MP3/AAC 的文件大小通常按编码 bitrate×时长估计，不能直接把 PCM 公式当作压缩后大小。

**常见混淆。** sampling rate 是每秒多少“个样本”；bit depth 是每个样本多少“个位”；bitrate 是每秒多少“个位”。提高 fs 不能替代增加 bit depth 来降低量化步长；提高 bit depth 也不能解决时间采样不足导致的混叠。两者提高通常都增加存储和传输量。[S04 PDF p.33；2026-09-24 转写 01:30:44–01:41:47]

### 4.9 Nyquist、aliasing 与 44.1 kHz：必须分清两种频率

设模拟信号最高需要保留的频率为 B Hz。理想带限信号的采样要求为 `fs > 2B`；对给定采样率 fs，其 **Nyquist frequency 是 fs/2**。而 **Nyquist rate 是 2B**，表示由信号带宽决定的采样率边界。课堂转写多次把后者也叫 Nyquist frequency；考试写出两个量的定义和公式最清楚。[S04 PDF p.33–34；2026-09-24 转写 01:41:47–01:52:18]

**为何要求两倍以上。** 采样不足时，不同模拟频率可能产生相同样本序列，无法唯一重建，称 aliasing（混叠）。更密集地插值已经采完的样本不会找回原来丢失的信息。

**为什么不能把边界 `fs = 2B` 当作万能保证。** 对 `x(t) = A cos(2πBt + φ)`，若 `Ts = 1/(2B)`，则 `x[n] = A cos(πn + φ) = A(−1)^n cosφ`。当 `φ = π/2` 时，所有样本都是 0，原波明显不为零；不同振幅与相位组合也可能给相同序列。课件 p.34 正用此现象说明严格大于及边界相位歧义。原页三角恒等式漏了部分 A 的一致书写；这里已保留 A 以避免混淆。

**混叠例（理解性计算）。** fs=32 kHz 时，18 kHz 的分量会折叠成 `|18−32|=14 kHz` 的可观测低频。若只在采完之后低通，18 kHz 已经混进 14 kHz，不能再按原频率把它分开。

**Anti-aliasing filter（防混叠滤波器，工程补充）。** ADC 之前先低通，把超出目标带宽/接近 Nyquist 边缘的分量充分衰减，再采样。真实滤波器不是理想砖墙，需要 transition band（过渡带），所以实际 fs 常高于理论的 2B 边界；DAC 重放时还需要相应重建处理，不能用简单“把样本点用直线连起来”代替所有重建原理。

**44.1 kHz 怎么解释。** fs=44.1 kHz 对应 Nyquist=22.05 kHz；可容纳通常希望保留的人类可听音频带宽，同时为靠近音频上限的滤波留空间。课件 p.35 写 12 Hz–22 kHz，p.49 写 20 Hz–22 kHz；常用教学近似是约 20 Hz–20 kHz，个人和年龄有差异。老师用 `2×22 kHz≈44 kHz` 帮助理解采样与听觉范围的关系，但不能把 44.1 kHz 的完整历史起因简化成“唯一因为 22 kHz 加 0.1 kHz 容差”。更不能推断 44.1 kHz 能完美保留到 22.05 kHz 的实际满幅信号而无需滤波余量。[S04 PDF p.35、49；2026-09-24 转写 01:47:12–01:50:26]

**48/96 kHz 是否能让人听到超声？** 更高 fs 可以方便某些录音、数字处理、滤波或针对非人类可听范围的研究，也提高存储和运算成本；不能据此说人耳的生理听觉上限被扩展，或只凭 fs 越高就断言听感必然更好。[S04 PDF p.49]

**三问三答。**

- 需要保留 5 kHz，fs 至少怎样选？答：理论边界 10 kHz，稳妥条件 fs>10 kHz，实际须考虑滤波过渡带。
- fs=8 kHz 最多可表示多高的理想频率范围？答：Nyquist 为 4 kHz，实际可用带宽应低于它；绝不是“可表示 8 kHz 声音”。
- 信号最高 6 kHz，题给 fs=12 kHz，能否无条件保证重建？答：位于边界，存在相位/端点问题；采用严格条件 fs>12 kHz 并带限更清楚。

### 4.10 声音的物理性质：声压波、传播速度与波长

声音在空气/液体中的常见形式是 longitudinal mechanical pressure wave（纵向机械压力波）：介质局部压缩与稀疏向外传播，介质粒子主要在平衡位置附近振动。声音需要介质，不能在真空中传播；与无需物质介质的光不同。[S04 PDF p.35]

课件例：20°C 干空气声速约 **343 m/s**，20°C 水中约 **1482 m/s**。速度取决于介质与条件；Mach 1 是当地声速对应的速度，不是所有介质中永远固定的 343 m/s。转写误识别为“millimeters per second”，应按课件单位 m/s 纠正。（2026-09-24 转写 01:53:50 起）

波速、频率、波长关系为 `v = fλ`（理解性补充）。例如空气中 1 kHz 声波的波长约 `343/1000 = 0.343 m`；100 Hz 约 3.43 m。频率描述周期快慢，不表示声音“传播得更快”；在同一近似非色散介质内，高音与低音的传播速度基本相同。

**可直接答题。** Sound is a mechanical pressure wave that propagates through a material medium. Frequency relates to pitch, while amplitude relates to sound pressure; phase affects how waves combine. The speed depends on the medium and temperature, and sound cannot travel through a vacuum.

### 4.11 Sound Pressure Level、dB 与 dBA

**SPL 定义。** 声压级 `Lp = 20 log10(p_rms / p_ref) dB = 10 log10(p_rms² / p_ref²) dB`。p_rms 是均方根声压；空气常用参考 `p_ref=20 μPa`，水中常用 `1 μPa`。dB 表示相对于参考量的对数比值，不能仅写“声压是 60 dB”而完全忘记参考与测量条件。[S04 PDF p.36]

**为什么声压公式用 20？** 在可比较声场中强度与声压平方有关，因此 `10log(p²/p_ref²)=20log(p/p_ref)`。对功率/强度的直接比用 10log，对声压/幅度比用 20log；考试要先看题给的是哪一种物理量。

**小计算。** p=0.02 Pa 时，`p/p_ref=1000`，SPL=60 dB；声压翻倍时增加 `20log10 2≈6.02 dB`；在相应条件下强度翻倍增加约 3.01 dB。0 dB SPL 表示等于参考声压，不是完全没有声音。两路同频相干信号相加还受相位影响，不能把两声源的 dB 数直接相加。

**主观 loudness 不等于物理压力。** 人耳响应近似具有对数特征，且对不同频率敏感程度不同；相同 SPL 的低频和中频不必听起来同样响。因此声压不是主观响度的线性刻度。[S04 PDF p.36–37]

**A-weighting。** 测量时按频率施加权重，减弱某些人耳不敏感频段（尤其低频）的贡献，结果写 dBA 或 dB(A)，用于较贴近听觉敏感性的声级评价。它是频率加权，不是“把 dB 从对数变成线性”，也不是“每个频率减掉同一个常数”。若先处理各频带，综合总声级还需按能量关系合成，不能把频带 dB 普通相加。[S04 PDF p.37；2026-09-24 转写 01:55:17–01:59:43]

**可直接答题。** SPL measures a logarithmic ratio of RMS sound pressure to a reference pressure. A-weighted SPL additionally weights frequency components to approximate the ear's unequal frequency sensitivity; equal unweighted SPL does not necessarily mean equal perceived loudness.

### 4.12 Echo、reverberation、interference 与主动降噪

**Echo（回声）。** 一次或可区分的声反射在直达声之后到达，例如山谷、井底。课件用约 0.1 s 作为人耳把反射声与原声分开的经验延迟；它不是对所有声音、环境和人都完全固定的边界。即使听者没有听到独立回声，机器识别仍可能被延迟副本影响。[S04 PDF p.38]

**Reverberation（混响）。** 封闭空间中大量反射在时间上密集重叠，能量随着环境吸收逐渐衰减，形成拖尾；不是“另一个词表示一个清晰的回声”。拖尾把相邻音素混在一起，改变特征和时间边界，使 ASR、声源定位与内容分析变难。可通过吸声、改变麦克风与说话者距离、dereverberation 等控制。（处理方法为理解性补充）[S04 PDF p.39；2026-09-24 转写 01:59:43–02:01:32]

**反射路程计算（理解性补充）。** 若额外传播时延为 0.1 s，空气中的额外路程约 `343×0.1=34.3 m`；若简化为人面对一面墙、去返额外路程为 2d，则 `d≈17.15 m`。两种路程定义不同，不能直接把 34.3 m 当作墙到人的距离。

**Interference（干涉）。** 两个或多个波在同一时空叠加：同相分量增强（constructive），反相分量削弱（destructive）。振幅相同、频率相同且在目标位置反相时可理想相消；真实声音往往是多频、移动、多路径，不能靠一个固定延迟在所有位置和频率上完全消除。[S04 PDF p.40]

**主动降噪 ANC。** 麦克风测量环境噪声，系统估计需要在耳边叠加的反相信号，由扬声器重放，使目标位置的噪声幅度下降。持续、可预测的低频噪声（例如发动机声）通常较适合；高频、突发、位置变化和处理时延使控制更困难。它不是从文件里删除音轨；被动隔音则依靠材料阻挡/吸收，机制不同。（应用机制补充；2026-09-24 转写 01:16:17–01:18:00、02:01:32 起；9/10 录音也有降噪例子）

**对比题答案。** Echo is a delayed reflected copy; reverberation is the dense buildup and decay of many reflections; interference is the addition of waves and may increase or decrease their resultant amplitude. All can change the captured signal, but destructive interference can also be deliberately used for noise cancellation.

### 4.13 早期录音：机械存储与重放

圆筒留声机先将声压推动的机械振动刻在包有锡箔的旋转圆筒上；重放时针尖沿刻痕移动，把凹凸变化再转成机械振动，经机械结构/号角发声。知识点是 **recording 把随时间的变化存成某种持久形状，reproduction 再把它变回可感知的变化**，并非所有录音一开始就是数字或电信号。[S04 PDF p.41]

音乐盒用圆筒/机械结构上的凸点按规定时序拨动音片，播放预设音乐。它展示机械编码和自动演奏；不是把任意声音波形完整录下的同类装置。老师将其作为机械存储与重放机制的直觉类比。（2026-09-24 转写 02:02:05 起）[S04 PDF p.42]

### 4.14 麦克风方向性：polar pattern 怎么读、怎么选

**Directionality。** 维持声源声压相同，只改变声源相对于麦克风的方向，输出可能不同；polar pattern 表示各入射角的相对灵敏度。0° 通常是正前方，180° 是正后方；在以 dB 标注的极坐标图中，向内表示相对更弱。真实指向性还随频率变化，所以单张图只是某条件下的表现。[S04 PDF p.43–46]

- **Omnidirectional（全向）**：理想上从各方向拾音相近。适合多人围桌、希望保留环境声的场景；无法靠方向本身拒绝四周噪声/混响。安静录音室是课件例子，但不是“全向只能录音室用”。
- **Cardioid（心形）**：前方灵敏、后方抑制最大，课件标 180°。适合讲台/单个主讲者，减少后方观众或扩音声进入。若声源偏离主轴，音量及音色都可能改变。
- **Supercardioid（超心形）**：正前方覆盖更窄，但有后方拾音瓣；抑制最强处偏离正后方。课件给约 120°，理想/具体型号常有不同角度，应按实测 polar plot 选择摆放。不能把它理解成“所有后方都比心形更安静”。
- **Shotgun（枪式）**：高度指向性，常用干涉管等结构让某些离轴声音相消，适合定向采集；其效果随频率/环境变化，不代表能隔着距离把所有背景声完全消掉。
- **Bidirectional / figure-eight（双向，课堂补充）**：前后灵敏、侧方抑制，可用于面对面的采访；来源为老师讨论前后两人访谈的场景，不是 p.45 四类之外另有“课件遗漏必须背的产品”。

**老师强调的是场景匹配。** 围桌会议可用全向/阵列，单人讲课可选定向，采访需兼顾主持人与受访者；选择应看覆盖角、噪声位置、频响等参数，而非“越贵越好”。同样的麦克风摆错方向可能比便宜但选得合适的效果差。（2026-09-24 转写 02:02:05 起，后段连续讲解）

**可直接答题。** A polar pattern describes microphone sensitivity as a function of arrival angle, normally relative to its on-axis response. An omnidirectional pattern suits sources around a table, whereas a cardioid helps isolate a presenter by attenuating sound from the rear. The appropriate pattern depends on source and noise geometry and varies with frequency.

### 4.15 频率响应、增益与 clipping：为什么录到了也不一定好用

**理想与实际。** 理想麦克风在目标频率和声压范围内，输出电压与声压成比例，且不任意改变各频率之间的相对强度。实际只在某些频率与幅度范围内接近理想；p.46 展示不同入射角下频率响应也不同。Frequency response 是输出灵敏度随频率的关系，flat 表示目标范围较平坦，并非波形始终是一条直线。[S04 PDF p.46]

**Gain 太大。** 模拟输出先经 amplifier，再进入 ADC。若前置放大/ADC 输入超过满量程，峰值被截成平顶，产生 clipping/distortion。已经剪掉的峰形不能仅靠后期调小音量恢复；调小只会把被削顶的波形一起变小。[S04 PDF p.47]

**Gain 太小。** 有用声音只占 ADC 量程很小一部分，弱变化可能量化到同一码值，信噪比较差；后期大幅放大也把底噪放大。最小的变化甚至可能落到零/同一级，但并不是“只要信号小就必定全为零”。合理增益让有用信号充分使用量程，同时给突发峰值留 headroom。

**选择参数（课件知识的应用）。** 目标频段、polar pattern、允许的声压/动态范围、self-noise、输出接口与供电、前端增益和实际位置应一并考虑。“高采样率”无法弥补模拟前端已经 clipping 的信号，也不能消除错误指向性收进来的所有背景声。[S04 PDF p.43–49]

### 4.16 AES42 数字麦克风：标准化与局限

课件列出 AES42 digital output，用标准化数字连接把采集数据交给音视频后端，并展示某些设备可配置 polar pattern、low-cut filter（例 40/80/120 Hz）、gain（示例 unity 至 +63 dB）、mute。理解重点是数字传输、接口兼容和可控参数；这些具体选项/数值是示例设备能力，不能当作每台数字麦都必须具有的全部范围。[S04 PDF p.48]

**Low-cut 是什么。** 它衰减低频，帮助减少脚步、风/振动、空调低频 rumble；40/80/120 Hz 表示不同截止设置，截止越高可能越多影响目标声音低频。它不是“只允许 40 Hz 声音通过”。（理解性补充）

**“No interference problem”的严谨解释。** 尽早数字化、缩短脆弱的模拟链路，可以降低模拟电缆中拾取干扰、增益不一致等问题；数字接口仍存在模拟前端噪声、过载、时钟/传输错误等实际限制，不能答“数字麦克风完全没有噪声和干扰”。AES42 也不等于自动保证最佳音质的唯一选购条件。

**一句话答题。** A digital microphone integrates conversion and uses a standardized digital interface, reducing some problems of analog signal transmission and enabling supported remote controls. Its quality still depends on the acoustic transducer, analog front end, sampling, gain settings and implementation.

## 5. 声音重放、语音与音乐（S05 PDF p.1–20）

本节覆盖 S05 声音部分全部页。2026-10-08 现有录音从语音识别示例中途开始，能核实 p.12–20 的部分讲解；p.2–11 未在现有录音中找到独立、完整的对应现场段落，因此按完整课件及标注的理解性补充说明，不能声称已听到这些页的全部原话。

### 5.1 Loudspeaker：把电信号变回压力波

Speaker 是最常见的声音重放器件，功能方向与麦克风相反：电信号驱动振膜脉动，推动周围介质形成声压波，供人耳接收。典型动圈扬声器中，信号电流通过磁场中的音圈产生力，带动振膜；这是“电 → 机械运动 → 声”。麦克风则是“声 → 机械运动 → 电”。并不是所有麦克风/扬声器在结构和效率上都能直接互换。[S05 PDF p.2；结构机制为理解补充]

扬声器也有 directionality：不同方向收到的声级不同，且与频率相关。图中的一组 polar plots 在六种频率下形状变化，说明听众坐位、扬声器朝向和覆盖范围都会影响效果。输入同一文件不保证每个座位听到相同的频谱和声压。

**可直接答题。** A loudspeaker converts electrical signal variations into diaphragm motion and pressure waves. It is the reproduction counterpart of a microphone and has frequency-dependent directionality, so placement affects the sound reaching a listener.

### 5.2 Speaker characteristics：功率、阻抗、频段、分频点

**Rated power（额定功率，W）。** 与允许电输入、热和机械承受能力有关。课件简化为“损坏前最大输入”；严谨答法需说明持续/峰值/测试条件不同。额定功率不是声音大小的完整指标：声压还取决于灵敏度、距离、频率、箱体和失真限制。标 100 W 不等于在所有场景都比 50 W 音箱更响或更清楚。[S05 PDF p.3]

**Impedance（阻抗，Ω）。** 表示扬声器给功放的交流负载，通常随频率变化；名义阻抗用于判断功放匹配。例如低于功放允许负载的阻抗可能使电流过大。阻抗的单位是 ohm，不是 Hz、mm 或 watt，也不等于线圈直流电阻在所有频率下的固定值。

**Frequency range / response（频率范围/频响，Hz）。** 指系统能在指定偏差与条件下重放的频段与各频率强弱。例如一段频带内近似平坦意味着原有频率比例较少被音箱改变；单独给上下限而没有允许误差，不能充分比较音质。

**Crossover frequencies（分频频率，Hz）。** 将输入频谱分给不同单元的交接位置。低通把低频交给 woofer，高通把高频交给 tweeter；三分频再给 midrange 一个中间频带。真实滤波有斜率和重叠，交接处须处理幅值、相位与指向性，不能说每条波在一个点被机械剪断。[S05 PDF p.3–4]

### 5.3 为什么有 woofer、tweeter、subwoofer 和箱体

**不同单元分工。** 低频要产生足够声压，通常需要较大空气位移，因此大振膜/较大冲程有优势；高频要求快速响应且要控制指向性，较小轻质振膜更合适。课件用“大膜质量较大、较易对应低频”的直觉解释；完整物理原因还包括面积、冲程、共振、刚性、效率和高频 beaming，不能仅答“大东西只能慢，小东西只能快”。[S05 PDF p.4；严谨性补充]

**课件图的单位。** 69 mm subwoofer、40 mm 单元、20 mm super tweeter 指的是示例音箱中单元尺寸，绝不是“69 Hz、40 Hz、20 Hz 的分频点”。Passive radiator（被动辐射器）没有独立音圈输入，随箱内压力振动，帮助调节低频输出；它也不能直接当作另一个独立声道。

**箱体（enclosure）的首要作用。** 振膜前后两侧产生的声压在相位上相反；若背面声波绕到前面，尤其低频容易与前方辐射相消，降低输出。箱体把前后辐射隔开并控制背面声能；密闭、倒相/被动辐射等结构还会影响低频响应和共振。箱体不只是“保护扬声器的盒子”。[S05 PDF p.5]

**可直接答题。** A multiway loudspeaker divides frequencies among drivers suited to different bands. Large low-frequency drivers move more air, while smaller high-frequency drivers handle high-frequency radiation. The enclosure controls rear radiation and reduces front–rear cancellation, especially at low frequencies.

### 5.4 Surround sound：5.1、6.1、7.1 分别表示什么

Surround sound 通过围绕听者布置/重放多个声道，让声音具有方向和包围感，服务更真实、更投入的体验。[S05 PDF p.6]

- **5.1**：5 个主声道，通常为 front left/right、center、surround left/right，另有 1 个低频效果声道 LFE。
- **6.1**：在类似布置上增加后中置声道的示例。
- **7.1**：通常把环绕扩展为左右侧环绕和左右后环绕，加前方三声道及 LFE；具体布局应按题图说明。

`.1` 表示带宽受限的 LFE 声道，并不是“0.1 个喇叭”；物理低音炮数目也不必与音轨 LFE 声道数完全一致。声道数是独立音频信号的组织，单元数是实际硬件数量，二者不要混算。（解释性补充）

### 5.5 Virtual surround：用 ITD、ILD、HRTF 重建方向线索

真实 5.1/6.1/7.1 会有空间、布线和摆位困难，因此 virtual surround 希望用较少的物理设备模拟多扬声器包围效果。课件列出两种配置：前方两只扬声器加低音炮的 2.1，以及以一条小单元阵列进行 digital sound projection 的形式。[S05 PDF p.7]

**ILD（Interaural Level Difference，双耳声级差）。** 声源靠近一侧耳朵，加上头部遮挡使左右耳接收的强度不同；大脑用此差异辅助判断左右方向。

**ITD（Interaural Time Difference，双耳时间差）。** 声源到左右耳的传播路程不同，使到达时间/相位不同；大脑用差异辅助判断方向。它与“听起来哪只耳朵更响”是不同线索。

**HRTF（Head-Related Transfer Function，头相关传递函数）。** 头部、耳廓、躯干等对不同入射方向的声波产生方向相关的滤波、反射和延迟。耳廓提供的频谱形状可辅助判断前后/上下，帮助解决单靠 ITD/ILD 仍有歧义的方向。HRTF 不仅是“耳朵反射造成音量变化”，而是声源到耳朵这一完整方向相关传输关系。[S05 PDF p.8]

**实现思想。** 按目标虚拟声源方向对信号施加相应滤波、相对增益与延迟，使两耳接收到接近该方向应有的线索；听觉便可能感到声音从实际扬声器以外的位置来。条形音箱还可以利用阵列和房间反射形成声束。听众位置、房间反射、左右串音和个体耳形不匹配都会降低效果，不能保证任意座位都等于真 7.1。（实现与限制为理解性补充）

**可直接答题。** Virtual surround recreates spatial hearing cues with fewer physical loudspeakers. ITD is the interaural arrival-time difference, ILD is the level difference, and HRTF describes direction-dependent filtering by the head and ears. Appropriate delays, gains and filters can make the listener perceive a virtual direction, subject to listener and room conditions.

### 5.6 Speech production：基频、声道、音素不是同一个东西

**发声基本过程（理解补充）。** 肺部气流提供能量；有声发音时声带近似周期振动，提供基频及谐波；声道形状（舌、唇、口腔等）改变共振，使不同音素有不同频谱。这是 source–filter 的直觉：source 的周期与 pitch 有关，filter 的共振与 formants 有关。[S05 PDF p.9–10]

**课件参考范围。** 正常语音主信息频段约 80 Hz–5 kHz；示例成年男性 pitch 120–160 Hz，女性/儿童 220–330 Hz；元音能量可延伸到数 kHz，摩擦/齿擦音有更高频能量。它们是示例/典型值，不能写成所有人的固定生理上下限。一个人的基频 150 Hz，并不代表其整段语音只含 150 Hz，或只需要 300 Hz 采样率。

**音量条件也要保留。** p.9 示例以离口部约 60 cm 计，正常说话约 60 dBA，喊叫的男性/女性示例约 76/68 dBA。距离、说话人、环境都会改变读数；这些不应被记成通用最大值。讲题若只需语音机制，不必把这组示例数字当主要结论。

**Phoneme（音素）。** 可区分语言中词义的基本语音单位；具体音素体系因语言而异。课件按气流生成方式举例：[S05 PDF p.10]

- **Stop consonants（塞音/爆破音）**：先阻断气流，再释放，例英语 /p/、/t/、/k/。
- **Fricative consonants（擦音）**：气流通过狭窄通道产生湍流，例 /f/、/v/；课件接着讨论 /s/ 一类高频齿擦音。
- **Approximants（近音）**：声道变窄但湍流较弱，例 /w/、/r/。
- **Aspirates（送气/呼气类示例）**：课件以词首 /h/ 举例，重点是可听呼气成分；语言学中“送气特征”与 /h/ 音的分类细节不必在这里混同。
- **Vowels（元音）**：声道相对开放、气流不被显著阻断，例 /a/、/e/、/i/、/o/；口型/舌位仍改变声道共振，并非“所有元音都没有滤波”。

**可直接答题。** Speech consists of phonemes produced by different configurations of the vocal apparatus. Voiced excitation contributes a fundamental frequency and harmonics, while the vocal tract shapes resonant energy bands. Stops, fricatives, approximants and vowels differ in how airflow is obstructed or allowed to pass.

### 5.7 Spectrogram、formants 与语音识别线索

**Spectrogram（语谱图）怎么读。** 通常横轴 time、纵轴 frequency，颜色/亮度表示某个短时窗口中该频率的能量。它兼有时域定位和频域分布；普通频谱图只显示一段信号的频率组成，不能直接替代随时间变化的语谱图。短时 Fourier 分析是常见生成方法，此方法解释属于理解补充。[S05 PDF p.12–13]

**Formants（共振峰）。** 声道共振使某些频率区域能量较集中，元音中常见为语谱图上持续/变化的明亮带，可标 F1、F2 等。它们由声道形状决定，与声带振动的 **F0（基频）** 不同：同一个元音换一个音高时 F0 可变，但其共振模式仍有相似性；同一音高发不同元音，formants 也可能不同。不能把每条谐波都称为一个 formant。

**课件的典型识别线索。** [S05 PDF p.12]

- 有声音素经常呈现规则谐波及较集中的共振能量带。
- 塞音常见闭塞后的短暂静音/低能量，之后出现较宽频的爆破能量。
- 擦音/呼气类成分常见连续、较分散的噪声能量云，尤其一些擦音在高频有明显能量。
- “无声发音没有 formants”的课件说法是帮助区分典型图样的简化：噪声激励也会被声道滤波；不能据此以绝对规则断言任意真实片段完全没有共振痕迹。

**ASR 的机制框架。** 采集、预处理、分帧/特征提取、根据模型识别声学/音素/词序列，再结合语言上下文输出文字。老师把语谱图模式与人脸特征向量比较作类比：同类发音的模式相似可用于分类，而不能只靠原始波形逐点相同。（2026-10-08 转写 00:00:01–00:01:16）

**限制。** 同一个音素随人、口音、语速、上下文共发音而变化；同一个词还可能有不同读音。因此课件的“每个音素有独特图样”应理解成有统计可辨特征，并非一张永远固定、没有重叠的条码。

**可直接答题。** A spectrogram shows how energy at each frequency changes over time. Formants are vocal-tract resonance bands that help distinguish voiced phonemes, while stops may show a burst after a closure and fricatives may show noise-like energy. Recognition compares such patterns with learned models and context rather than expecting identical raw waveforms.

### 5.8 为什么噪声和窄带电话会让 ASR 变难

**噪声不只“叠上去”。** 人在嘈杂环境会增大音量、改变 pitch、拉长或调整音节；因此安静环境训练的模型不仅面对附加背景噪声，还面对说话方式变化，出现 train–test mismatch。混响、多说话人和麦克风频响还会改变特征。[S05 PDF p.14]

**电话采样率的限制。** 传统窄带电话常用 8 kHz 采样，Nyquist=4 kHz，实际通话带宽通常更窄；许多高频摩擦/齿擦音区别因此削弱。不能说“8 kHz 采样可以保留到 8 kHz”，也不能以成年人基频只有几百 Hz 推断语音所有细节都能保留。[S05 PDF p.14]

课件与转写提到 /s/、/f/ 等可能有很高的频率成分、甚至超过 20 kHz；严谨答法是“区分线索中有高频能量，受记录带宽限制会损失”，不要说这些音全部只在 20 kHz 以上，因此人耳从来听不到。电话中还能听到它们的一部分，但辨别可能更困难。（2026-10-08 转写 00:01:16–00:04:34）

**整词拼读的补救。** 用容易区分的完整单词代替相近字母音，例如 “Alpha/Alfa, Bravo, Charlie…”；增加冗余和声学差异，降低误听。课件写 Beta、Frankie、Sugar 等，是示例混合词表，不应原样标成正式 NATO phonetic alphabet。考试如果问原理，回答“用 whole words 代替容易混淆的孤立字母”，无需争论拼读表版本。

**改进方法（理解性补充）。** 多条件/噪声数据训练与适配、更合理麦克风位置/阵列、降噪和去混响、扩大有效语音带宽、结合语言上下文，都可以减轻问题；其中丢失的高频物理信息并不会因为“模型更聪明”就被保证真实还原。

**可直接答题。** Noise changes both the recorded signal and the speaker's articulation, creating a mismatch for a recognizer trained in quiet conditions. Narrowband sampling removes high-frequency cues important for some consonants. Whole-word spelling increases redundancy, while suitable capture and robust training improve recognition.

### 5.9 TTS、dictation、NLP 与 actionable intelligence

**Speech synthesizer / Text-to-Speech。** 把文字转换成可听语音，需处理文本读法、发音、节奏/重音等，再产生波形；课件的 Nuance 例子展示支持多种语言的 TTS，而不是要求记一个旧开发者网址。[S05 PDF p.11]

**Dictation → NLP → action。** Dictation/ASR 将声音转成文字；Natural Language Processing 再解释意图、实体和上下文；Actionable intelligence 将解释转成可执行动作，例如语音说“明天九点提醒我交作业”，系统识别文字后解析时间和任务，再创建提醒。ASR 文字正确也不保证意图理解正确，动作执行还需要应用接口和规则。这是 p.15 标题展示的能力链路，不应把“语音识别”直接等同完整智能助理。[S05 PDF p.15；链路例为理解性补充]

### 5.10 Music：pitch、fundamental、harmonic、overtone、partial

研究音乐信号的一般性质，有助于 audio compression、instrument detection、music manipulation/synthesis。[S05 PDF p.16]

**Pitch（音高）** 是听者感到的高低；对常见周期乐音，主要与 fundamental frequency（基频 F0/f0）相关。F0 不是音量。提高振幅主要影响响度，提高基频主要提高音高；同一个音高可以由多种乐器发出。

**Harmonic（谐波）** 是基频的整数倍频分量。f0=440 Hz 时：440 是第 1 谐波/基音，880 是第 2 谐波，1320 是第 3 谐波，1760 是第 4 谐波。

**Overtone（泛音）** 是基音以上的部分音；在纯谐和系列中，第 1 泛音=第 2 谐波，而不是第 1 谐波。**Partial（部分音）** 泛指组成复杂声的各个频率分量；它不必总是基频的整数倍，例如一些打击乐器有非谐和 partials。不能用“所有 overtone 都必定为整数倍”替代这一边界。

**例子。** 老师比较不同乐器演奏 middle C：基频大致相同（图示约 262 Hz），但除基频外的频谱结构不同，因此能听出不同乐器。注意 p.16 表格的 A4=440 Hz 与 p.17 的 middle C≈262 Hz 是两个例子；不能把所有图都写成“中音 C=440 Hz”。（2026-10-08 转写 00:05:02、00:09:17–00:11:12）[S05 PDF p.16–17]

### 5.11 Timbre：相同音高为什么声音仍不一样

**音色（timbre）** 是使我们区分不同发声来源的声音品质。课件强调两类线索：[S05 PDF p.17]

1. **Spectrum（频谱）**：哪些频率分量存在，各有多大幅度。笛子较接近基频主导的例子，钢琴/小号含不同谐波比例；波形和频谱因此不同。
2. **Time envelope（时间包络）**：整体音量如何随时间起、落、保持和消失。同样一个平均频谱，若起音过程不同，听起来仍可能明显不同。

因此“音高相同”“音量相同”“音色相同”是三件事。例：钢琴和小号演奏相同 F0 的 middle C，它们的谐波强弱和起音/衰减不同，所以保留同一音高却听起来不同。识别乐器若只估计 F0，会丢失大量用于区分的特征。

**可直接答题。** Two instruments can play the same note because they share a fundamental frequency, while sounding different because their harmonic/partial spectra and temporal envelopes differ. Pitch is mainly associated with the perceived fundamental, whereas timbre describes these source-specific qualities.

### 5.12 ADSR 四阶段：每个字母到底控制什么

ADSR 用分段包络描述声音幅度随时间的典型变化：[S05 PDF p.17、19]

- **Attack（起音）**：从开始到峰值；快 attack 像敲击/拨弦的锐利起音，慢 attack 像逐渐加入的柔和合成音。
- **Decay（衰减）**：从初始峰值下降到保持段的过程。
- **Sustain（保持）**：持续发声/按住音符期间维持的水平；在常用合成器中它主要是 level，其他 A/D/R 通常是 duration。不是“每种真实乐器都有一段严格恒定音量”。
- **Release（释音）**：停止激励/松键后下降到零的过程；短 release 很快截断，长 release 形成尾音。

**考试画图。** 横轴时间、纵轴幅度，先上升 A、下降 D、保持 S、最后下降 R，并标松键/停止激励的位置。不能把 release 误当成从 attack 峰值开始衰减的那一段；那一段是 decay。

**限制。** ADSR 是好用的参数化近似，不是每个真实乐器都完全符合四段折线。钢琴即使按住也有自然衰减；吉他的拨弦、持续运弓的小提琴、吹奏长音的包络不同。老师用吉他激发—振动—消失解释这种时间过程。（2026-10-08 转写 00:11:12 起）

### 5.13 乐器三组与激励方式

**String（弦乐器）。** 由弦振动发声，拨、拉、敲等激励方式改变泛音构成和包络；吉他拨弦与小提琴持续运弓，即使音高相同也会有不同音色。钢琴用锤击弦，说明“激励是敲击”与“主要振动体是弦”的分类角度可以不同。[S05 PDF p.18]

**Wind（管乐器）。** 吹气激发空气柱/共振器，管长、开孔、激励结构影响可出现的共振频率和谱形；笛子、单簧管等可有相同基频却不同谐波分布。

**Percussion（打击乐器）。** 由敲、摇、摩擦、刮等动作激发，振动体可能是膜、板或其他结构；有些有确定音高，有些有大量非整数倍的部分音。不能将“打击乐”都当作没有任何频率结构的随机噪声。

**应用。** 乐器检测需要频谱、时间变化、瞬态等线索；合成则可模拟振动体/激励与时间包络。三类的作用是帮助理解声源机制，并非仅背三个英文名称。

### 5.14 Music synthesis：怎样从参数生成一个像乐器的声音

课件提出物理建模、谐波与波形包络，以及使用原始乐器采样等思路。[S05 PDF p.19–20]

**基于分量的直觉。** 产生不同形状/频率的波（图中 sine、square、sawtooth、triangle），按适当比例组合出基频与谐波，再用 ADSR 改变幅度。简化加法合成可写为 `x(t)=e(t) Σ Ak cos(2πk f0 t+φk)`，其中 e(t) 是包络、Ak 控制第 k 个谐波强度。方波、锯齿波等本身就含多个谐波；它们不只是视觉形状不同，频谱也不同。（公式为理解性补充）

**Physical modelling（物理建模）。** 模拟弦、管、膜以及激励/阻尼的动力学，让参数对应真实声源机制。它与“手动把几个正弦相加”属于不同具体建模路线；课件把这些概念紧密列在一起是概要，不必误解为严格同义词。

**Sampling / wavetable。** 可以记录真实乐器的声音片段并按音高、力度等组织，播放、变调或拼接得到输出；wavetable 严格指可查表的波形/周期或其序列，并不等于任何完整采样库。核心共同点是利用预存真实/合成波形，而非每次从零计算物理过程。（术语细化为理解性补充）

**Hatsune Miku 例。** p.20 用初音未来展示歌声合成的应用：原始发音材料可经过组织和处理生成新的歌唱。应理解采样、音高/时长/连接与合成的关系；不应把它解释成“角色本人把每首生成歌曲完整唱过”，也不要将某个应用示例当成本课要求掌握其软件内部全部算法。（2026-10-08 转写 00:11:12–00:15:56）

**可直接答题。** Music synthesis generates sound using signal models, physical models or stored waveforms/samples. Fundamental frequency sets the intended pitch, the relative spectral components shape timbre, and an envelope such as ADSR controls its time evolution. Combining these controls can produce different instrument-like sounds.

### 5.15 声学与语音音乐的整合答题示例

**题：录音音量太小，增加采样率能否解决？** 答：主要不能。小电平使有用信号未充分使用 ADC 量程，需检查麦克风位置、灵敏度和前置增益；提高 fs 增加时间样本数，不能直接放大量化幅度，也不能恢复前端信噪比。应合理增益并保留 headroom；提高 bit depth 可减小量化步长，但同样不能消除已存在的模拟噪声。

**题：同样 262 Hz，为什么钢琴和笛子不一样？** 答：它们共享基频所以有相似 pitch；谐波/部分音的相对强度以及 attack、decay、sustain、release 的时间形态不同，因此 timbre 不同。F0 一样不表示整个频谱一样。

**题：一个麦克风记录整张会议桌，一只用于讲课，如何选？** 答：围桌声源来自各方向，可选择全向或覆盖适当的阵列；讲课希望突出讲台人声、抑制后方干扰，可选心形并正确朝向主讲者。还需检查频响、距离、声压、环境反射与增益；不能只按价格/动圈电容分类断言优劣。

**题：为何两个前方扬声器能造成后方声源的感觉？** 答：听觉依赖双耳接收到的时间差、声级差和 HRTF 频谱线索；虚拟环绕按目标方向重建这些差异，必要时结合阵列/房间反射。效果依赖位置、房间和个体 HRTF，物理喇叭少不等于没有空间声线索。

**题：为何电话里容易听错字母，报完整单词更可靠？** 答：窄带传输/采样削弱某些高频辅音线索，噪声与发音差异进一步增加混淆；用差异更大、有冗余的完整单词代替孤立字母，可降低误听。应谈信息与带宽，而非说“电话把所有辅音都删除”。

### 4–5 声音部分逐页覆盖核对与勘误说明

以下是本章写作核对清单，便于发现“只有标题却没有解释”的漏项；不是老师公开的考点清单。

- **S04 p.1–4**：标题；sensor 定义；三组用途；五感，见 4.1。
- **S04 p.5–7**：触觉、resistive/capacitive/pressure、3D Touch、actuator/Taptic，见 4.2。
- **S04 p.8–11**：人工视觉输入、CCD/CMOS、分辨率、找不同的识别/空间/记忆/动作，见 4.3。
- **S04 p.12–15**：binocular vision、stereogram 方法与图示，见 4.3。
- **S04 p.16–17**：耳、麦克风、dynamic/condenser 机制、产品图示，见 4.4；产品销量/型号不当作通用知识。
- **S04 p.18–22**：嗅味觉、其他物种、健康传感器、长者照护、环境传感器与定向障碍，见 4.5。
- **S04 p.23–24**：动态范围、偏置、非线性、迟滞，见 4.6。
- **S04 p.25–30**：LEGO 比喻、波形分解、正弦圆周投影，见 4.7。
- **S04 p.31–33**：sampling、quantization、误差、bit depth、采样率，见 4.8–4.9。
- **S04 p.34**：Nyquist 边界、相位反例、同一样本的不同模拟波，见 4.9；已看原页公式图。
- **S04 p.35**：机械声波、介质、声速、听觉参考范围，见 4.9–4.10。
- **S04 p.36–37**：SPL 原公式、参考声压、主观非线性、A-weighting，见 4.11；已看原页公式图。
- **S04 p.38–40**：echo、reverberation、interference，见 4.12。
- **S04 p.41–42**：锡箔圆筒机械录音与十八音音乐盒，见 4.13。
- **S04 p.43–46**：mic 定义/膜片、指向性、polar 图、四种方向性、频响/角度，见 4.14–4.15；已看 polar 图与频响图。
- **S04 p.47–49**：放大、clipping、弱信号、AES42、可配置参数、听觉范围/44.1/48/96 kHz，见 4.9、4.15–4.16。
- **S05 p.1–5**：标题、speaker 机制/方向性、功率/阻抗/分频/频段、尺寸图、箱体，见 5.1–5.3。
- **S05 p.6–8**：5.1/6.1/7.1、virtual surround、2.1/阵列、ILD/ITD/HRTF，见 5.4–5.5。
- **S05 p.9–10**：语音/音高/响度参考值、五组发音方式、phonemes，见 5.6。
- **S05 p.11–15**：TTS 示例、语谱图/formants、图示、ASR 限制/整词拼读、NLP/action 链路，见 5.7–5.9。
- **S05 p.16–18**：音乐处理目标、F0、harmonic/partial/overtone 表、timbre/频谱/ADSR、乐器分类，见 5.10–5.13。
- **S05 p.19–20**：合成路线、四种波形、ADSR 图、初音未来示例，见 5.14。

**本次明确修正的歧义。** ① Nyquist frequency=fs/2 与 Nyquist rate=2B 分开。② fs=2B 不能无条件保证所有边界相位的重建。③ 人耳范围课件 12/20 Hz 与 20/22 kHz 是不同近似，44.1 kHz 不等于人耳可听频率。④ BMI 不把年龄性别写入基本公式。⑤ offset 不用待机耗电作定义。⑥ hysteresis 与 drift 分开。⑦ echo 的 0.1 s 是经验尺度。⑧ SPL 参考值不是绝对静音，dBA 不把对数变线性。⑨ supercardioid 有后瓣，120° 是课件近似。⑩ AES42 不保证无任何干扰，设备设置范围不代表全标准设备。⑪ speaker 的 mm 为尺寸、Hz 为频率、Ω 为阻抗、W 为功率。⑫ 人声 F0 不等于语音最高频率，formants 不等于 F0/每个谐波。⑬ 部分音可不谐和，第 1 泛音在谐和情形是第 2 谐波。⑭ sustain 常指保持电平，物理建模/加法合成/采样/波表不视为完全同义。以上修正用于把课件简化与精确定义同时保留。

## 6. 光、图像采集、显示与人类视觉（S05 PDF p.21–62）

### 6.1 光是什么：振幅、频率、相位与偏振

**光（light）是电磁波。**课件采用的可见波长范围为约 400–780 nm；这是一种近似范围，人的敏感程度在边界附近逐渐下降，不是一条对所有人完全相同的硬界线。真空光速 `c = 299,792,458 m/s ≈ 3.00×10^8 m/s`，波速、频率和波长满足 `v = fλ`，在真空中为 `c = fλ`。因此波长越短，频率越高。例如 600 nm 的光在真空中的频率约为 `3×10^8 / (600×10^-9) = 5×10^14 Hz`。

用单一波的模型理解三个量：振幅描述电场变化的大小；频率/波长与光的颜色相关；相位描述周期变化进行到哪一步。**严谨说明：光强与电场振幅的平方相关，不能把振幅数值直接当作 lux，也不能认为所有混合光都有唯一一种波长。**白光通常由多种波长共同组成；人眼对不同光谱的响应还决定最终颜色感受。

**相干性（coherence）**描述不同波之间相位关系能否保持稳定。普通光源中大量发光过程的相位关系通常不稳定，课件称其为 non-coherent；激光是相干光的典型例子。相干不等于“所有波在所有位置相位都为零差”，关键是相对相位关系有序、稳定。普通成像和人眼一般测得经过时间平均的强度，不会像直接读数值一样读出电磁波每一瞬间的相位。

**偏振（polarization）**描述光波电场振动方向的性质。非偏振光的振动方向没有固定关联；偏振片选择性通过特定偏振分量。偏振太阳镜可以抑制部分反射眩光，LCD 利用液晶和偏振片控制透光，立体电影也可以让左右眼分别接收不同偏振的画面。

**易混点：**用不同颜色滤光片分离左右画面的是 anaglyph 色差立体法；用不同偏振方向分离的是偏振立体法。课堂 ASR 提到的“蓝/绿眼镜”不能当作偏振的定义。颜色与偏振是不同的光学属性。

**可直接答：Why do wavelength, phase and polarization matter?** Wavelength is associated with spectral color; phase relationships determine coherence and interference; polarization describes the orientation of the electric field and can be used to filter light or separate the left-eye and right-eye images.

来源：[S05 PDF p.21–23]；[T08 00:16:29–00:22:25]。波速关系和振幅平方关系为理解补充。

### 6.2 Candela、lumen、lux：方向、总量与单位面积

这三个单位回答不同的问题，不能互换。

- **发光强度 luminous intensity，candela（cd）：**光源沿某个方向、单位立体角发出的可见光通量有多少。适合描述灯具的方向性和某方向有多强。它不是观察者实际接收到的照度。
- **光通量 luminous flux，lumen（lm）：**某个角度范围或全部方向上发出的可见光总量。买灯泡时，用流明比较光输出，比仅用耗电瓦数更直接；不同发光技术可用不同电功率产生相近流明。
- **照度 illuminance，lux（lx）：**落在接收表面上、单位面积的光通量。适合描述办公桌照明、拍摄环境和相机最低照度规格所对应的环境条件。它不是相机量子效率或感光灵敏度本身。

**立体角 solid angle，steradian（sr）：**二维角度用弧度衡量圆周弧长；三维立体角衡量球面上覆盖的面积。以球心为顶点，覆盖球面面积为 `A`、球半径为 `r` 时，`Ω = A/r²`；整个球面对应 `4π sr`。面积必须是球面上的面积；小接收面正对光线时可近似用平面面积。

课件关系：`1 lm = 1 cd·sr`；方向上强度均匀时 `Φv = Iv Ω`。若所有方向都均匀为 1 cd，则总光通量为 `4π lm`；若照度均匀，则 `E = Φv/A`，所以 `1 lx = 1 lm/m²`。一般光源的总通量需要对不同方向的强度积分，不能不加条件地把任意一方向的 cd 乘 `4π`。

**课件 p.26 图中的完整计算例：**一个 `50 mm × 50 mm` 的小传感器距点状光源 2 m，正对光源，接收 0.1 W。先换算面积 `A = 0.05×0.05 = 0.0025 m²`；立体角约 `Ω = A/r² = 0.0025/4 = 0.000625 sr`；辐射强度 `Ie = P/Ω = 0.1/0.000625 = 160 W/sr`。**这个答案是 radiometric 的 W/sr，不是 candela。**转换成 cd 需要光的光谱和人眼光谱敏感度加权，不能只凭瓦数直接换算。这道图中例题在纯文字提取里容易漏掉。

**课件 p.29 例题：**1000 lm 均匀照到 1 m²，照度为 1000 lx；相同光通量照到 10 m²，照度为 100 lx。流明相同、覆盖面积不同，照度就不同。

课件 p.27 给出 candela 的单色光说明：在 `540×10^12 Hz`、该方向辐射强度为 `1/683 W/sr` 的条件下，对应 1 cd。这里的 683 和指定频率体现光度量对人眼视觉敏感性的关联。考试解释题首先应准确区分三种量；不要把“总能量”“照度”“方向强度”写成同一个定义。

**课件照度量级例子：**月光下可约 1 lx，办公室约 320–500 lx，电视演播室约 1000 lx，正午强日照可约 130,000 lx。它们是指定情境中的估算，实际受天气、表面方向、距离和遮挡影响。这里说的是接收面的照度；不能把课件中“月亮 emits lux”的简化措辞当作“lux是光源总输出”的定义。

**可直接答：Compare cd, lm and lx.** Candela measures luminous intensity in a particular direction; lumen measures luminous flux over a solid angle or all directions; lux measures the flux incident per unit area. Their relationships are `lm = cd·sr` and `lx = lm/m²`. The same lumen output can give different lux values when spread over different areas.

来源：[S05 PDF p.24–29]；[T08 00:24:18–00:35:08]。课堂转写把 candela 多次识别成 camera，把 lumen 识别成 woman，均依课件术语校正。

### 6.3 反射与折射：相机为什么能成像

**反射 reflection：**光到达表面后返回原介质。入射光线、反射光线和表面法线在同一平面，反射角等于入射角，角度都相对于法线测量。镜面反射保留明确方向，漫反射由表面微观方向差异把光散向多方向。凹面镜可使适当方向的光会聚，凸面镜产生更宽视场的成像效果；不要把不同镜面统称为同一种几何作用。

**折射 refraction：**光进入另一种透明介质时传播速度改变，通常使传播方向发生偏折。跨越静止介质界面时，频率保持不变，波长随波速改变。镜头和眼睛利用折射把不同方向的光聚焦到成像面。理解补充：折射满足 `n1 sinθ1 = n2 sinθ2`，`n = c/v`；沿法线入射时可以改变速度而不改变方向，不能把“进入另一介质”绝对等同于“必然弯折”。

**为什么对计算机视觉有影响：**透明物体会折射背景，镜面物体会映出环境，因此像素颜色和轮廓不一定直接对应物体本身的材质或位置。检测和三维重建若假设表面不透明且近似漫反射，就可能在玻璃、镜子和高光处失败。相反，图形渲染需要模拟反射与折射，才能让合成场景显得自然。

**可直接答：How does refraction help image formation?** A lens changes ray directions at its surfaces because light travels at different speeds in different media. Properly shaped lens surfaces bring rays from a scene point toward the corresponding image location, forming a focused image on the film, electronic sensor or retina.

来源：[S05 PDF p.30–32]；[T08 00:36:02–00:40:58]。

### 6.4 从暗箱到数字图像：投影、记录与图像形成的两部分

**Camera obscura（暗箱）**通过小孔或光学结构，把外部场景投影到暗箱内部。它可以形成图像，但本身没有能长期保存图像的记录介质。早期感光纸和胶片通过受光后发生的化学变化保留图像；课件以涂氯化银的纸张遇光变暗为例。数字相机把光转换成电信号，再经数字化、处理、编码与存储保存。

图像形成要回答两个独立问题：**几何 geometry 决定场景点投影到哪一个位置；光学/物理 physics 决定该位置有多亮、是什么颜色。**一个物体在图像中的位置取决于相机姿态、镜头和距离；像素值还受光源、表面反射、遮挡、曝光及传感器响应影响。相同物体改变光照后，几何位置可能不变，但像素亮度可以明显变化。

**透视投影的理解模型：**用与真实倒像等效的虚拟正像平面表示，相机坐标中的点 `(X,Y,Z)` 可写为 `x = fX/Z`、`y = fY/Z`。这里 `f` 为焦距，坐标需采用一致单位；真实成像面置于光心另一侧时会出现符号反转。远处同样大小的物体投影更小，因为投影大小与 `1/Z` 成正比。三维点被投影成二维位置，深度信息因此丢失；单张图像一般不能直接唯一确定真实深度。

**曝光三要素与取舍（课堂补充）：**光圈改变入光量和景深；曝光时间越长通常积累更多光，但增加运动模糊风险；提高 ISO/输出增益会提高输出亮度，同时也可能放大噪声，不会凭空增加已经捕获的光子。相机不是单靠“像素更多”就能在暗处拍得更好。

来源：[S05 PDF p.33–36]；[T08 00:36:32–00:42:06]。投影公式是对 p.36 示意图的解释；曝光取舍为理解补充，与 S03 的低光图像例子对应。

### 6.5 CCD 与 CMOS：感光与读出结构的比较

两者都使用像素化的半导体感光阵列，把入射光转换成电荷或电信号。**CCD（charge-coupled device）**典型结构把各像素积累的电荷逐级转移，经移位寄存器送到输出放大和电荷—电压转换电路。**CMOS（complementary metal-oxide-semiconductor）**典型有源像素结构在像素附近进行转换，通过行列选择读出，并更容易把控制电路集成在传感器上。

按课件表格，比较维度包括：电荷是逐级转移还是直接寻址；电荷—电压转换是在读出后还是像素内；曝光/读出是整帧还是行顺序；灵敏度；控制电路是片外还是片上。掌握这些结构性差异，才能解释集成、读出、噪声和成本方面的取舍。

具体对应课件 p.38 的曝光一行：CCD写为 single frame/field exposure，CMOS写为 single frame/line sequential exposure，后者包括整帧或逐行等不同安排，不能只记“CMOS一定逐行”。

**严谨说明：**课件“CCD 弱光较好、CMOS 灵敏度较低”是概括式比较，不能当作所有代际、所有芯片的固定排序。实际性能还受像素尺寸、量子效率、读出噪声、工艺和整体系统影响。也不能把 CMOS 一概等同于 rolling shutter，或把 CCD 一概等同于任何情况下都无扫描相关问题。理解补充：逐行曝光/读出会使运动对象在不同行记录于不同时刻，可能产生 rolling-shutter 形变。

**可直接答：Compare CCD and CMOS sensors.** Both convert light into electronic signals with a pixel array. A typical CCD transfers accumulated charges through shift registers to an output amplifier, whereas a typical CMOS sensor supports pixel addressing and local conversion with integrated control circuitry. Their performance depends on implementation; low-light quality cannot be judged from the family name alone.

来源：[S05 PDF p.37–38]；[T08 00:42:06–00:46:17]。

### 6.6 像素、分辨率、宽高比和帧率

**像素 pixel**是数字图像的离散采样位置；图像由 `宽 W × 高 H` 个像素组成。百万像素数 `MP = WH/10^6`，例如 `1920×1080 = 2,073,600 ≈ 2.07 MP`。更多像素通常提供更多空间采样，但实际可分辨细节还受镜头、噪声、对焦、运动模糊等限制。

**宽高比 aspect ratio**为 `W:H`，它描述形状，不等于像素数量。`640×480` 为 4:3；`1280×720`、`1920×1080`、`3840×2160` 为 16:9。两个画面可以宽高比相同而分辨率不同，也可以像素数接近而形状不同。**不要把“所有现代手机/电脑屏幕都是 16:9”写成定律**，课件是在比较常见格式。

**视频 video**是随时间排列的图像序列。**FPS（frames per second）**表示每秒记录/显示多少帧，是时间采样密度；分辨率表示空间采样密度。高 FPS 一般使快速运动表达更连续，但不自动提高每一帧的清晰度。快门曝光时长和帧间隔也不同：例如 30 fps 的帧间隔约 33.3 ms，每一帧仍可用 1/1000 s 曝光。视频通常还包含声音、时间戳及编码/容器信息。

**课件数字的使用：**p.40 的“照片最高 32 MP、视频最高 16 MP”是课件中的设备示例背景，不是数字成像理论上限。转写中“DVD 是 1280×720”“Full HD 是 1920×1020”不可靠；复习时以 720p=`1280×720`、Full HD=`1920×1080`、常见 UHD 4K=`3840×2160` 作为格式例子。4K 一词也可能用于别的标准尺寸，题目给出具体宽高时直接按题目计算。

来源：[S05 PDF p.39–40]；[T08 00:46:17–00:53:13]。完整的数据量例题见后文计算专题。

### 6.7 立体相机、多摄像头、ToF、折叠光路和手部追踪

**Stereo camera（立体相机）：**两个有一定间距的相机从不同视点观察同一场景。相同物体在左右图像中的位置差称为视差 disparity；已知两相机几何关系后，可通过匹配点和三角测量估计深度。基本流程是标定/对齐、左右对应点匹配、计算视差、转换为深度。理解补充：在理想平行双目模型下 `Z = fB/d`，`B` 是基线、`d` 是视差；`f` 和 `d` 同用像素单位时，`Z` 与 `B` 的长度单位一致。视差越小，一般距离越远；匹配错误、遮挡和无纹理区域会影响结果。

**为什么手机装多个摄像头：**不同焦距和视场可覆盖超广角、主摄和长焦等拍摄需求；双目或其他辅助传感器也可帮助深度估计和背景虚化。多个图像可在合适标定和算法下融合。但“镜头多”不自动等于像素相加或图像一定更好，镜头之间有视点、曝光、颜色和对齐差异。

**Time-of-Flight（ToF）sensor：**主动发出已知的光信号，测量反射光的延迟或调制相位变化，估计距离并形成深度图。p.44 示意流程是近红外主动照明 → 像素矩阵接收 → A/D 和深度处理 → 深度图/幅度图 → 应用。理解补充：直接往返计时时 `Z = cΔt/2`，除以 2 是因为光走了“出去再回来”两段；例如往返 20 ns，距离约为 3 m。间接 ToF 由调制相位推断距离，不是所有设备都直接逐个测量脉冲飞行时间。反光、多路径、强环境光和测量范围会影响结果。

**Folded optics（折叠/潜望式光路）：**利用棱镜或反射元件改变光路方向，把较长的光路安排在机身平面内，以适应手机厚度并实现较长等效焦距。它改变的是光路布局，不是靠软件把一个低清图像放大就得到光学长焦。

**Leap Motion：**课件用它说明非接触式手部/手势感知。其图示包含红外照明和多个红外相机，采集手部后估计手指和手部空间姿态，再驱动交互/虚拟手显示。传感是测量输入，屏幕中的虚拟手是处理结果；它不等于“把真正的手直接扫描进屏幕”。遮挡和有效感知范围会影响追踪。

**可直接答：Stereo vs ToF.** Stereo estimates depth from geometric disparity between different viewpoints, while ToF actively illuminates the scene and estimates distance from the returned light's timing or modulation phase. Stereo relies on reliable correspondence; ToF is sensitive to illumination, reflections and multipath effects.

来源：[S05 PDF p.41–46]；[T08 00:53:13–00:55:20]。算法和公式按图示作理解补充；课件只作设备举例的部分不扩展成未经讲授的详细硬件规范。

### 6.8 加色与减色：显示器和纸张为何不同

**加色 additive：**通过主动光源发出不同颜色的光，再让光进入眼睛形成颜色。RGB 三个分量同时为零是黑；在规定白点和足够输出下，三色适当叠加得到白。显示设备通常采用这种方式。

**减色 subtractive：**环境光照到表面后，颜料/墨水选择性吸收一部分光，剩余部分反射到眼睛。纸张没有环境照明就无法像自发光屏幕一样显示。印刷常用 cyan、magenta、yellow，再加 black（K）以更稳定、经济地形成黑色和细节。加墨越多一般反射越少，和 RGB 发光叠加的方向相反。

**电子墨水 E Ink（课堂例子）：**Kindle类阅读器的典型电子墨水显示主要调制反射光，和OLED自发光不同。带前光的阅读器是用额外照明照亮显示表面，因此“阅读器能在暗处亮起来”不能直接推出其每个像素都像OLED一样发光。

**应用题：Why does a printed image look different from the display?** The display combines emitted light, whereas printed paper selectively absorbs and reflects ambient light. They have different primaries, gamut, white points, illumination and device response. Therefore the same numeric-looking color description is not enough to guarantee the same appearance across the two devices.

来源：[S05 PDF p.47]；[T08 00:55:20 之后的颜色解释、00:59:51 电子墨水例子]。

### 6.9 CRT、LCD、OLED、裸眼立体显示和“全息”示例

**CRT（cathode-ray tube）：**电子枪发出电子束，由偏转系统控制扫描位置，电子束激发屏幕上的荧光材料发光。调节束强度可改变对应位置亮度；彩色 CRT 使用相应的彩色荧光结构。它通过扫描和荧光发光形成画面，不能仅按“很多独立小灯”理解。

**LCD（liquid-crystal display）：**典型透射式 LCD 使用背光、偏振片、液晶层和彩色滤光片。电场改变液晶取向，控制光经过液晶和偏振片后的透过量，再形成各子像素亮度。液晶主要负责调制光，通常不自己发光。课件图比较 TN 和 IPS 中液晶/电场安排，说明液晶分子转动和控制方式可不同。

**OLED（organic light-emitting diode）：**有机发光层由电流驱动产生光，像素可独立控制；AMOLED 的 AM 是 active matrix，指有源矩阵驱动方式。与典型 LCD 相比，OLED 不依赖统一背光，黑色可通过关闭相应像素实现。理解补充：这带来高对比的可能，但不能从结构直接推出所有画面下耗电一定更低、每台机器寿命相同等结论。

**Autostereoscopic display（裸眼立体显示）：**课件图用 parallax barrier（视差屏障）把不同像素方向的光分别送向左右眼，让两眼获得不同图像并产生立体感，不需要配戴分光眼镜。限制是最佳观看位置 sweet spots；偏离规定角度可能模糊、串扰或看错视图，也可能牺牲部分空间分辨率/亮度。

**“3D Hologram”示例：**p.52 是 Gatebox 虚拟角色显示案例。课件这一页没有给出光场记录或干涉重建算法，因此应掌握“把虚拟角色作为具立体感的视觉界面呈现”的例子，不能仅凭营销名称就断言设备实现了严格物理定义的全息重建。理解补充：严格的 holography 涉及光波信息的记录与重建，与普通二维视频经反射形成悬浮感的演示应区别。

**课堂的 VR/AR 辨析：**VR主要让用户进入计算机生成的虚拟环境；AR在真实环境感知之上叠加虚拟信息。它们是呈现与交互方式，不等同于某一种面板材料；LCD/OLED都可能服务于不同虚拟/增强显示系统。[T08 01:03:39–01:04:07]

**可直接答：Compare LCD and OLED.** A typical LCD modulates a backlight using liquid crystals and polarizers; an OLED pixel emits light when electrically driven. The key distinction is light modulation versus per-pixel light emission. Autostereoscopic presentation is a separate question about routing different views to the two eyes.

来源：[S05 PDF p.48–52]；[T08 显示设备讲解约 00:59–01:04]。各设备的工作原理为对课件结构图的解释。

### 6.10 眼睛的三个主要部分，以及 cones/rods

**Iris（虹膜）**调节瞳孔大小，从而控制进入眼睛的光量；**lens（晶状体）**参与聚焦；**retina（视网膜）**包含感光受体，将光刺激经生理过程转成神经系统可用信号，由视神经传向大脑。它和相机有可比关系：虹膜/瞳孔对应进光控制，眼球光学系统对应镜头，视网膜对应感光采样；大脑后续解释不能等同于单纯存一张照片。

**Cones（锥体细胞）与明视觉 photopic vision：**课件给数量约 600–700 万，中央凹 fovea 区域密度高，擅长明亮条件下的颜色和细节感知。中央高密度和较少汇聚的连接有利于空间分辨率。理解补充：颜色感知主要依靠不同光谱敏感性的锥体响应的比较，不是一个“红像素”只接受绝对单一红波长。

**Rods（杆体细胞）与暗视觉 scotopic vision：**课件给约 7500 万–1.5 亿，较多分布在中央凹以外区域，弱光灵敏度高，主要提供亮暗和整体场景信息，不能提供与锥体相同的颜色细节。多个受体汇聚到后续通路，可提高灵敏度，但会损失定位精细度。这里是解释性简化，不是完整神经连接图。

**分布图要会读：**中央处锥体密度极高、杆体不是在那里最多；在 optic disc（视神经盘）位置缺少感光受体，产生生理盲点。不能把“杆体在整个视网膜均匀分布”或“细胞总数多就空间分辨率更高”当答案。

**可直接答：Compare cones and rods.** Cones support color and fine-detail vision under bright conditions and are densely concentrated near the fovea. Rods are more sensitive in dim light, are abundant away from the foveal center, and provide coarser, largely achromatic information. Greater pooling improves sensitivity at the cost of spatial detail.

来源：[S05 PDF p.53–55]；[T08 01:04:55–01:12:15]。数量为课件估计值，不需把这种范围写成适用于所有人的精确计数。

### 6.11 中央凹分辨力、眼球运动和 foveated rendering

**课件的中央凹估算要会算：**把直径约 1.5 mm 的中央凹近似为 `1.5 mm × 1.5 mm` 方形阵列，按约 `150,000 cones/mm²`，得到 `1.5×1.5×150,000 = 337,500 ≈ 337,000` 个受体。它是为了和相机阵列类比而采用的**方形近似**，不是圆面积公式；若按直径 1.5 mm 的圆计算面积，会得到不同结果。课件还拿约 5 mm×5 mm 的中等分辨率 CCD 作原始采样数量类比，但“受体数量相同”不意味着整个视觉系统与相机性能完全等价。

**为什么人看场景时不断转动眼球：**最高空间分辨力只在中心小区域。眼球通过扫视 saccades 把重要对象依次放到中央视野，注视 fixation 时获取局部信息，大脑结合任务和已有知识整合场景。p.57 的不同任务对应不同眼动轨迹，说明观察不是均匀扫描所有像素；任务/先验会影响采样位置，与 Neisser 感知循环对应。

**Foveated rendering（注视点渲染，课堂补充）：**眼动追踪估计用户正在看哪里，在该区域保留高渲染分辨率，周边采用较低细节水平。目的是利用视觉非均匀性，减少计算、带宽或能耗，同时尽量维持主观画质。它可以只改变渲染采样密度，不必真的把显示面板物理像素重新排列；追踪精度和低延迟十分重要，否则转动眼睛时会看见低清区域或模糊边界。

**可直接答：Why is eye tracking useful in VR?** It estimates the gaze location so that the system can allocate high rendering quality to the foveal region and reduce peripheral work. This exploits the non-uniform spatial acuity of human vision to save computation and energy while preserving perceived detail near fixation.

来源：[S05 PDF p.56–57]；[T08 01:14:22–01:20:57]。

### 6.12 主观亮度、背景对比和亮度适应

**物理强度不等于主观亮度。**课件将主观亮度与入眼光强的对数响应联系起来，重点是感受并非简单线性。p.58 三个中央小方块可以具有相同物理灰度，但置于黑、灰、白背景后看起来不同，说明视觉解释受相对对比和周围环境影响。因此不能仅凭中心像素数值预测人在所有情境下看到的亮度。

**Brightness adaptation（亮度适应）：**视觉系统通过改变整体敏感程度，覆盖很宽的照明环境范围；课件给适应范围约 `10^10` 量级。**它不能同时在一个固定适应状态下分辨整个总范围。**从明处到暗处，需要适应时间；“眼睛适应能力大”不能直接解释为“单次观看的动态范围无限”。

**与 HDR 的关系：**传感器一次曝光有有限动态范围，太亮会饱和，太暗会受噪声限制；多曝光 HDR 把适合亮处和暗处的记录组合起来。人的整体亮度适应和相机 HDR 是可以比较的不同机制，不能混为“眼睛在一次快照内天然记录所有亮度”。

**可直接答：Why can the same grey patch look different?** Perceived brightness depends on local contrast, context and the viewer's adaptation state, rather than the patch's physical intensity alone. The visual system can adapt across a large overall intensity range, but cannot operate over that full range simultaneously.

来源：[S05 PDF p.58–59]；[T08 01:20:57–01:23:58]。

### 6.13 RGB(A)、CMYK、YUV：为什么要换颜色空间

**RGB**用红、绿、蓝发光分量表示颜色，适合显示；**RGBA**再加入 alpha 透明度/覆盖量，alpha 不是第四种可见光颜色，也不是图层先后顺序。**CMYK**描述印刷墨色，适合减色输出；不同设备、纸张和照明产生的可复现颜色范围 gamut 不同。课件的 CIE 图中不同三角形/区域说明各种设备或颜色空间的色域范围不同，不是存在一个所有设备都能精确显示的相同 RGB 三角形。

**YUV**把亮度相关分量和两个色差分量分开。课件 p.60 给出下列矩阵（按课件符号和系数）：

```text
Y′ = 0.299R + 0.587G + 0.114B
U  = -0.14713R - 0.28886G + 0.436B
V  = 0.615R - 0.51499G - 0.10001B

R = Y′ + 1.13983V
G = Y′ - 0.39465U - 0.58060V
B = Y′ + 2.03211U
```

**理解补充：**这类编码公式的 `Y′` 是 luma（由非线性/伽马编码分量组合的亮度相关信号），应与物理 luminance 区别。课件把输入简写成 R/G/B。具体数字格式若使用 YCbCr，会有不同的缩放、偏置和标准系数，不能把上面的 U/V 系数直接套给任何 YCbCr 文件。

为什么压缩用这类表示？视觉通常对亮度的空间细节比对色度的空间细节更敏感。把两者分开后，可以保留较多亮度信息、减少色度采样或精度，降低数据量而尽量保持主观画质。**“换颜色空间”本身不自动压缩**：若只是可逆线性变换且样本数/位深不变，数据量不一定减少；还要结合色度子采样、量化或其他编码步骤。

理解补充例：R=G=B 时，U/V 约为零，灰阶主要由 Y′ 表达。若用不含填充的 8-bit 4:2:0 YCbCr 图像作计算，平均约 12 bit/pixel，约为 24-bit RGB 的一半；这是特定采样格式的例子，不是“所有 YUV 都天然减半”。

**可直接答：Why separate luminance-related and chrominance information?** The separation allows the encoder to preserve spatial detail in the luma component while representing chroma more coarsely, exploiting the visual system's differing sensitivity to those components. A color transform alone does not reduce the number of bits; subsampling, quantization or coding is also required.

来源：[S05 PDF p.60]；[T08 01:23:58–01:26:19]。YUV 矩阵来自课件图中公式；luma/物理亮度与特定 4:2:0 格式的区别为理解补充。

### 6.14 True Tone：让显示白色随环境调整

纸张的白色受环境照明色温影响；屏幕如果保持固定白点，在某些环境里会显得特别偏蓝或偏黄。**True Tone**类显示根据环境光调整显示白点/色彩外观，使屏幕在不同照明下呈现更自然、类似纸面的观感。课件用同一平板在偏冷和偏暖环境中的图片说明这种变化。

它处理的是环境与视觉适应之间的关系，**不能等同于提高像素数量、锐化、HDR 或自动把相机中的噪声去掉**；也不等于在所有环境里保证标准色彩校准结果完全相同。理解补充：对严格按固定白点进行颜色制作的任务，自动环境适配与固定参考显示的目标并不相同。

**可直接答：What is the idea behind True Tone?** It adjusts the display's white point and color appearance according to ambient illumination, aiming for a more consistent perceived appearance as lighting changes.

来源：[S05 PDF p.61–62]；[T08 01:26:19–01:27:37]。

### 本部分逐页覆盖清单

- S05 p.21–23：可见光、电磁波、光速、相干与偏振 → 6.1。
- p.24–29：cd/lm/lx、sr、单色光定义、光源功率比较、面积照度，含 p.26 图中 160 W/sr 计算 → 6.2。
- p.30–32：镜面/漫反射、凹凸镜、折射和成像、透明/反光物体 → 6.3。
- p.33–36：暗箱、感光记录介质、几何和物理成像、透视模型 → 6.4。
- p.37–38：CCD/CMOS 结构与比较 → 6.5。
- p.39–40：分辨率图、宽高比、照片/视频、FPS和课件示例上限 → 6.6。
- p.41：双目深度 → 6.7；p.42–43：手机多摄 → 6.7；p.44：ToF 主动照明和深度图 → 6.7；p.45：折叠光学 → 6.7；p.46：Leap Motion → 6.7。
- p.47：加色/减色、RGB/CMYK → 6.8。
- p.48–50：CRT、LCD、OLED/AMOLED → 6.9；p.51：裸眼立体视差屏障与 sweet spots → 6.9；p.52：Gatebox 显示例子 → 6.9。
- p.53：眼睛结构 → 6.10；p.54–55：cones/rods 的数量、分布和功能、图中盲点 → 6.10。
- p.56：中央凹受体估算 → 6.11；p.57：任务依赖眼动 → 6.11。
- p.58：主观亮度、背景对比 → 6.12；p.59：亮度适应与非同时范围 → 6.12。
- p.60：色域和 YUV 正/逆变换矩阵 → 6.13；p.61–62：True Tone 概念和环境对比 → 6.14。

## 7. 计算专题：公式、代入和答案

本章把课件、课堂参数讨论和图中的计算集中起来。明确写“理解补充”的例题用于练会同一个原理，不能理解为老师已经公布的原题。

### 7.1 bit、byte、单位前缀与位深

`1 byte = 8 bits`。小写 b 常表示 bit，大写 B 常表示 byte。`Mb/s` 是每秒百万比特，`MB` 是百万字节；`1 MB = 10^6 B`，`1 MiB = 2^20 B = 1,048,576 B`。如果题目未说明，至少写明自己采用十进制 MB，防止把单位混淆。位深 n bit 可以表示 `2^n` 个离散码字；8 bit 对应 256 级，10 bit 对应 1024 级，16 bit 对应 65,536 级。

RGB 每通道 8 bit 时，每像素 `3×8 = 24 bit = 3 byte`；RGBA 每通道 8 bit 时为 32 bit/像素。**8-bit/channel 不等于整幅彩色像素只用 8 bit。**但索引色、灰度、浮点图像或具体像素格式可能不同，题目给什么格式就按什么格式计算，不能一律套 32 bit。

来源：[T01 00:03:06–00:09:50 参数与单位讨论；T05 00:01:11–00:20:39；T06 00:00:20–00:11:37 图像表示补充]。

### 7.2 量化步长和量化误差（理解补充例）

已知输入工作范围为 0–2 V，8-bit 均匀量化。若按 256 个等宽区间定义，量化步长 `Δ = 2/256 = 0.0078125 V = 7.8125 mV`。四舍五入到最近量化代表值，内部区间的最大误差约为 `Δ/2 = 3.90625 mV`。超出输入范围会饱和/削波，不再只是小的量化舍入误差。

有些题目把两端点都作为量化重建值，则用 `(Vmax−Vmin)/(2^n−1)`；看到题设应先确认约定，不能声称两种公式永远只有一种正确。提高位深改善振幅分辨能力，提高采样率改善时间采样密度，作用不同。

来源：[S04 采样/量化页]；数值例子为理解补充。

### 7.3 Nyquist、混叠和反例

**题 1：最高频率 B=18 kHz，如何选采样率？**理想带限条件下 Nyquist rate 为 `2B = 36 ksample/s`。实践中选 `fs > 36 ksample/s` 并给抗混叠滤波器留出过渡带，例如可考虑 44.1 或 48 ksample/s，具体取决于系统要求。不要写成“18 kHz 就只需每秒采 18k 次”。

**题 2：fs=44.1 kHz，其 Nyquist frequency 是多少？**`fs/2 = 22.05 kHz`。Nyquist frequency（由采样系统决定的半采样率）和 Nyquist rate（由目标信号带宽决定的两倍最高频率）要分清。

**题 3：23 kHz 单频被 44.1 kHz 采样会怎样？**23 kHz 高于 22.05 kHz，未经适当滤波就可能折回为 `|44.1−23| = 21.1 kHz` 的混叠分量。数字样本不能再唯一告诉你原来是 23 kHz 还是其别名；事后只提高播放采样率不能找回丢失信息。这个数值例为理解补充。

**为什么不把 fs=2B 当作任何信号都稳妥？**取 `x(t)=sin(2πBt)`，若 `fs=2B` 且从零相位开始采样，`x[n]=sin(πn)=0`，所有样本都是零，无法恢复振幅。这说明边界条件、相位和严格带限假设都重要。实际系统使用滤波和余量，而不是在边界上赌博。

**44.1 kHz 的正确解释：**半采样率是 22.05 kHz；通常用约 20 kHz 的音频目标带宽说明余量。课件另有“人耳到 22 kHz”概括，不能据此说 44.1 kHz 在 22 kHz 以上还具有宽裕滤波过渡带。

来源：[S04 采样定理与 aliasing 页]；相位及混叠数值例用于解释条件。

### 7.4 未压缩 PCM 音频的数据率和文件大小

公式：`bitrate = fs × bits/sample × channels`；`bytes = fs × bits/sample × channels × duration / 8`。假设所有样本按给定位数紧密保存，不计文件头、对齐和元数据。

**例：44.1 kHz、16 bit/sample、双声道、60 秒。**

1. 采样率转换为 `44,100 sample/s/channel`。
2. 码率 `44,100×16×2 = 1,411,200 bit/s = 1.4112 Mb/s`。
3. 总大小 `1,411,200×60/8 = 10,584,000 B`。
4. 即 `10.584 MB`，约 `10.09 MiB`。

**答案解释：**双声道的两个通道都要存；采样率不是总 bit/s。将文件改名为 MP3 不会产生压缩，实际压缩后大小取决于编码设置。

来源：[S04 数字化原理；课堂参数计算框架]；PCM 完整数值例为理解补充。

### 7.5 原始图像大小：RGB 与 RGBA

公式：`bytes = W × H × bits/pixel / 8`。

**1920×1080，RGB，每通道8 bit：**像素数 `2,073,600`；每像素 `24 bit=3 B`；总大小 `2,073,600×3 = 6,220,800 B = 6.2208 MB ≈ 5.93 MiB`。

**相同尺寸，RGBA，每通道8 bit：**每像素 `32 bit=4 B`；总大小 `8,294,400 B = 8.2944 MB ≈ 7.91 MiB`。alpha 是透明度相关值，不是把图像自动分成“4 层”。

若文件是 JPEG/PNG 等，不能只从扩展名推算实际大小；压缩比受内容、质量、编码和元数据影响。课件把未经压缩的像素表示与照片文件相比较，考试应先写清你算的是 raw pixel data。

来源：[T05 00:01:11–00:20:39；T06 00:00:20–00:11:37 图像表示、RGBA与大小计算讨论]。

### 7.6 原始视频的数据量：空间×时间

公式：`raw bitrate = W × H × bpp × fps`；`bytes = W × H × bpp × fps × seconds / 8`。若还有音频，应另加音频轨数据量；以下忽略音频、编码头与容器开销。

**例：1920×1080、RGB 24bpp、30fps、60s。**每帧 `6,220,800 B`；总帧数 `30×60=1800`；总大小 `6,220,800×1800 = 11,197,440,000 B = 11.19744 GB`。原始码率是 `1920×1080×24×30 = 1,492,992,000 bit/s ≈ 1.493 Gb/s`。

**为什么视频需要压缩？**一分钟原始数据已超过 11 GB，直接传输需要很高带宽；空间冗余、帧间冗余及视觉敏感性提供压缩机会。**同一分辨率和 FPS 的压缩文件大小仍可能不同**，因为压缩码率、编码器和内容复杂度不同。

来源：[T05/T06 视频序列和码率讨论；S05 PDF p.39–40]；60s 数值演算为理解补充。

### 7.7 已知压缩码率，怎样算文件大小

公式：`bytes ≈ bitrate(bit/s) × seconds / 8`。

**例 1：8 Mb/s，10 分钟视频。**`8×10^6×600/8 = 600,000,000 B = 600 MB`。如果 8 Mb/s 只指视频轨，不能忘记另加音频和封装开销；如果是总码率，则不要把音频再加一次。

**例 2：128 kb/s，3 分钟音频。**`128,000×180/8 = 2,880,000 B = 2.88 MB`。

**例 3：5 Mb/s 和 10 Mb/s 同长度的两段视频，后者一定清楚一倍吗？**大小在其他条件一致时约为两倍，但主观画质不随码率线性增加；分辨率、编码效率、噪声和运动也会影响质量。若是可变码率，应使用平均总码率估算，而非瞬时峰值。

来源：[T01 码率与时长计算讨论；S03 视频参数]。

### 7.8 声波波长、SPL 和反射距离

**声波关系：**`v=fλ`。空气声速取 `343 m/s`、频率 440 Hz，波长 `λ=343/440≈0.780 m`。声速改变时，相同频率的波长也改变；音高与频率相关，不能把声速、响度、音高混为一谈。

**SPL：**`Lp = 20 log10(prms/pref)`，空气中参考声压 `pref=20 μPa=2×10^-5 Pa`。若 `prms=0.2 Pa`，则比值为 `10,000`，SPL=`20×4 = 80 dB`。声压变为两倍，增加 `20log10(2)≈6.02 dB`；在适当相同阻抗条件下功率/强度变为两倍，对应 `10log10(2)≈3.01 dB`。**不能把声压公式中的20改成10。**

**回声理解补充：**如果声源与接收者位置接近，声音到平墙再返回，往返延迟 0.1s 对应距离 `d=vt/2=343×0.1/2=17.15 m`。必须除以2；如果题目是单向传播就不除。是否听成独立回声还受内容和环境影响，0.1s只是课堂经验阈值。

来源：[S04 声学、SPL、回声页]；具体数值演算为理解补充。

### 7.9 光学计算：sr、lm、lx、ToF 和双目

**光通量与方向：**均匀 2 cd 光源在 3 sr 范围内的通量 `Φ=2×3=6 lm`；若 2 cd 是全方向恒定，整个球面总通量 `2×4π=8π lm`。前提不同，不能看到 cd 就直接乘4π。

**照度：**1000 lm 均匀照到 10 m²，`E=1000/10=100 lx`；如果只照到1m²，就是1000lx。现实中分布不均时这是平均值。

**课件辐射强度图例：**50mm×50mm接收面、距光源2m、接收0.1W：`Ω≈0.05²/2²=0.000625sr`，`Ie=0.1/Ω=160W/sr`。这是W/sr，不是cd；缺少光谱与视觉加权时不能直接换算。

**ToF（理解补充）：**往返延迟20ns，`Z=cΔt/2=(3×10^8)(20×10^-9)/2=3m`。

**平行双目（理解补充）：**焦距800pixel、基线0.1m、视差20pixel，`Z=fB/d=800×0.1/20=4m`。焦距和视差的pixel相消；不要再把焦距800误当800m。视差越小，深度通常越大。

来源：[S05 PDF p.25–29、41、44]。

### 7.10 中央凹数量和颜色变换

**中央凹：**按课件方形近似 `1.5mm×1.5mm×150,000/mm²=337,500≈337,000`。题目如果让沿用课件模型，就使用方形面积，不擅自换圆面积。估算只比较局部受体数量，不能推出人眼整体等于0.337MP相机。

**YUV变换：**用课件矩阵，令 R=1、G=B=0，得到 `Y′=0.299`、`U=-0.14713`、`V=0.615`；反变换会近似恢复红色，舍入系数可产生微小误差。R=G=B=0.5 时，Y′≈0.5、U≈V≈0，说明无彩灰色不需要强色差信号。使用前确认输入是否归一化、采用哪种标准与范围。

来源：[S05 PDF p.56、60]；颜色数值代入为理解补充。

## 8. 综合简答、比较和设计题：参考答案

本章题目按材料中可出简答的关系整理；不是预测原题。各章已经提供更完整的机制和英文答案，此处训练跨知识点组织。

### 8.1 “设计一个课堂多媒体记录与检索系统”怎样答

**参考答案：**用摄像头采集教师/板书画面，麦克风采集声音，课件或屏幕共享提供清晰的教学内容流；为各流记录统一或可转换的时间戳，处理设备时钟差和传输延迟，保证语音、画面与课件时刻对应。采集后进行合适的采样量化、编码、缓存和存储，同时保存课次、讲者、时间、课件页等元数据。处理模块可执行语音转写、关键词/图像特征提取和索引；查询时先匹配索引，再返回对应时间段，不能每次把所有录像重新逐字扫描。输出端提供同步播放、章节导航和可检索讲义。噪声、误识别、断流、时钟漂移和数据量是需评估的限制。该答案把 capture、storage、network、processing、output 五模块连起来，而不是只说“用AI总结”。

依据：[S01–S02 系统框架；S03 检索；S04 数字化]。

### 8.2 “为什么要多源融合，而不是只提高单个传感器精度”怎样答

**参考答案：**精度改善减少某一个物理量的测量误差，多源融合则能提供不同语义层面的互补证据，两者作用不同。温度传感器再精确，也不能单独确定空气湿度；仅有GPS可能不能确定相机朝向，需结合姿态和视觉。融合前要处理时间对齐、坐标/单位一致性和可靠性；如果把不同时间的观测当成同时发生，可能形成错误事件解释。融合也不会保证绝对真相，系统要保留不确定性并持续用新证据更新模型。

依据：[S01 新应用与S/M/F框架；S02 correlation/holistic information；T01/T02课堂例子]。

### 8.3 “语义鸿沟、感知循环与上下文”怎样连成一段

**参考答案：**传感器提供像素和波形等底层数据，而人需要关于对象、事件和目的的意义；两者的差距称为semantic gap。已有schema帮助人提出解释并决定关注哪里，新的感官证据再更新schema，这就是Neisser感知循环。上下文和元数据提供时间、地点、任务等线索，帮助把同样的信号解释成更相关的信息。但先验也可能产生误导，因此要用进一步观察验证，而不是把第一印象当真。多媒体系统的目标是结合互补信号、上下文与任务，缩小这种差距。

依据：[S02 PDF p.3–21]。

### 8.4 “主动降噪、EQ、语音识别是不是同一件事”怎样答

**参考答案：**它们都处理音频，但目标和输出不同。ANC估计环境噪声，在目标位置产生合适的反相信号，利用声波相消减小噪声；EQ按频带增益或衰减，调整频谱/音色，并不自动理解语音；ASR从声音中推断语言单元和文字。高质量采集和降噪可能帮助识别，但降噪不等于已经识别出了文字。ANC受延迟、相位、空间位置和噪声变化影响；EQ的修改也可能损害需要保留的声音。

依据：[S03 音频应用；S04 干涉与采集；S05 语音]。

### 8.5 “Shazam为什么不用把每首歌从头听一遍”怎样答

**参考答案：**它在入库阶段为曲目提取音频指纹并建立索引。查询时，对短片段提取同类指纹，用哈希/索引找到候选曲目，再检查多个特征是否在一致的时间偏移下匹配。强的局部时频特征和相对关系有助于在片段位置未知、有一定噪声的情况下匹配，具体鲁棒性取决于实现。加快查询的关键工作是在查询前组织曲库，而不是到提问时才逐首完整比对原始音频。哼唱检索和原录音片段匹配也不是完全相同任务。

依据：[S03 Shazam页；T04/T05 索引讲解]。

### 8.6 “LPC和MPEG压缩利用什么不同依据”怎样答

**参考答案：**LPC以语音产生的模型为基础，用预测/声道相关参数与激励等较少信息近似重建语音；它主要利用语音信号的结构。MPEG音频编码可以结合人耳的频率与时间掩蔽，把难被察觉的成分降低精度或减少比特，并利用其他编码冗余。前者偏向生成/预测模型，后者强调感知编码，但实际标准可能结合多种技术。频率掩蔽是强音遮蔽邻近频带弱音，时间掩蔽是强音附近时间内的弱音较难察觉；不是所有“人暂时听不清”的声音都可任意删除。

依据：[S03 LPC、MPEG与掩蔽页]。

### 8.7 “HDR、视频稳定和去模糊”怎样区分

**参考答案：**HDR解决有限动态范围带来的高光/暗部信息丢失，通常组合不同曝光或其他互补记录；稳定化估计并补偿相机帧间整体运动，使画面轨迹更平稳；去模糊试图逆转曝光期间运动或其他原因造成的模糊。一个画面可能已经稳定但每帧仍有曝光拖影。多曝光融合若有运动，必须对齐并处理鬼影；相机全局运动补偿不一定能恢复每个独立运动物体。算法解决的问题不同，不能用“让画面更清楚”代替机制。

依据：[S03 图像/视频增强页]。

### 8.8 “检测、识别、跟踪、三维重建与检索”怎样区分

**参考答案：**检测输出目标是否存在以及位置；身份识别输出目标是谁或与哪个身份匹配；跟踪把不同时间的目标观测关联起来形成轨迹；三维重建恢复形状/几何和可能的纹理，便于从新视点呈现；检索根据查询条件/特征从已组织的集合中返回相关条目。它们可能共享特征，也可组成一个管线，例如先检测脸、跨帧跟踪，再选清晰图像做身份比对，但不能因为系统给脸画了框就声称完成身份识别。

依据：[S03 Haar、head tracking、3D face、gait与视频索引页；T02/T06]。

### 8.9 “同样一个middle C，为什么钢琴和小提琴不同”怎样答

**参考答案：**两者可共享相近基频，所以音高相同；不同乐器的振动和共鸣机制产生不同相对谐波强度，起音、衰减、持续和释音的时间包络也不同，所以音色不同。用频谱看是基频及泛音组成不同，用时间看是ADSR等动态特征不同。仅保存一个基频数值可以提示音高，不能完整重建乐器的真实音色。合成器需进一步模拟波形、谐波、包络或使用采样/物理模型。

依据：[S05 PDF p.15–20；T08 00:05:02、00:09:17–00:15:56]。

### 8.10 “为什么人眼能启发压缩、HDR和VR优化”怎样答

**参考答案：**人眼对亮度和色度空间细节的敏感性不同，因此编码可保留更多亮度细节并减少部分色度信息；中央凹细节分辨力高、周边低，因此VR可通过眼动追踪进行注视点渲染；人眼对亮度的感受受背景对比与适应影响，因此显示和图像呈现要考虑主观效果。相机多曝光HDR与视觉适应可用来讨论宽亮度环境，但二者机制不同，不能说人眼同时看到无限动态范围。利用视觉限制的前提是保留任务需要的信息，医学/测量等场景的评价标准也可能不同于一般娱乐画质。

依据：[S05 PDF p.53–62；S03 HDR]。

### 8.11 十四组一眼要能区分的概念

1. **Signal vs information：**前者是测量/编码值，后者是结合语义和上下文得出的有意义解释。
2. **Media vs modality：**前者是信息形式，后者是感觉通道；多媒体可通过同一种感觉呈现。
3. **Content vs context vs metadata：**内容是媒体本身；情境是解释条件；元数据是描述数据的数据，可以记录部分情境。
4. **Object vs event：**对象是实体/属性，事件是时间上发生的状态与关系变化。
5. **Accuracy vs resolution：**准确度关注接近真值，分辨能力关注能区分多小变化；更多刻度不保证无偏差。
6. **Sampling vs quantization：**时间或空间等独立变量连续变离散，和振幅连续变有限等级，不能互换。
7. **Nyquist rate vs Nyquist frequency：**2B与fs/2，分别从信号与采样系统出发。
8. **Frequency vs amplitude vs phase：**周期快慢、大小、周期中的相对位置，分别关联音高、声压和叠加关系。
9. **Echo vs reverberation vs interference：**可分离的延迟反射、密集衰减反射、波的叠加现象。
10. **Loudness vs pitch vs timbre：**主观响度、音高、音色，对应的主要因素不同。
11. **Resolution vs FPS vs bitrate：**空间采样数量、时间采样密度、单位时间编码数据量。
12. **cd vs lm vs lx：**方向发光强度、光通量、接收面单位面积通量。
13. **RGB vs CMYK vs YUV：**发光加色、印刷减色、亮度相关/色差分离表示。
14. **Cones vs rods：**明亮颜色细节与中央高分辨，和弱光灵敏/周边整体信息。

### 8.12 答题时的最终检查

- 定义有没有说清“测量/处理的是什么”，而不只写装置名称？
- 流程有没有输入、核心步骤和输出？检索有没有说明离线/入库索引？
- 比较题有没有沿相同维度比较，例如采集原理、输出、适用条件与限制？
- 数值题有没有区分bit/byte、k/M前缀、每通道/每像素、单程/往返？
- 对“更高”“更快”“更好”的判断有没有说明条件，避免把示例写成绝对定律？
- 老师例子、课件事实、理解补充和推测考点有没有分清？

## 9. 资料清单、回查路径和完整性核对

### 9.1 原始课件与页数

S00–S05 的原始 PDF 均位于课程目录的 Slides 文件夹。文中引用的 p. 是物理页码。S02 的页脚有跳号；引用时不能把页脚编号误作缺页。正文各课件结束附近附有逐页覆盖清单，包含标题/视频引导页的性质说明；已经把图片中的关键公式和流程纳入正文。

### 9.2 八段录音回查

- T01：`Transcripts/artifact-多媒体-01-obcnxzjs37165o216vrd19lx/transcript.txt`。
- T02：`Transcripts/artifact-多媒体-02-obcnxz2z26vl7c86iw194s83/transcript.txt`。
- T03：`Transcripts/artifact-多媒体-03-obcnx1n21qx2y87q95zk937g/transcript.txt`。
- T04：`Transcripts/artifact-多媒体-04-obcnx2la973g92y18fx6rek3/transcript.txt`。
- T05：`Transcripts/artifact-多媒体-01-obcn3sqjs2kzm7114n94lg5e/transcript.txt`。
- T06：`Transcripts/artifact-多媒体-02-obcn3t8a59263c8w6t3312q2/transcript.txt`。
- T07：`Transcripts/artifact-多媒体-01-obcn8l41ae3e23k112c2t4jm/transcript.txt`。
- T08：`Transcripts/artifact-多媒体-01-obcnh787mag6242rp5i573lz/transcript.txt`。

这些路径相对于本地 Exam-Prep；飞书云文档中保留它们用于说明来源，不代表点击后即可访问本机文件。`Transcripts/INDEX.md` 包含对应日期、时长和可点击的本地链接。原始转写约47,000个识别词，仍是自动识别原文，并非人工校订的逐句官方讲稿。

### 9.3 本次重写的重点修正

旧版只有概览，本次补全了通信技术的作用、S/M/F系统框架、感知循环各箭头、体验式环境、各应用的机制、3D人脸重建流程、步态与视频索引、传感器/音视频设备结构、声学/音乐/光学/视觉原理，以及可直接参考的答案和完整计算。课件图里的辐射强度例题、YUV正逆变换、中央凹估算也已单独展开。

Quiz权重、更高像素的局限、RGB/RGBA格式、Nyquist两种术语、44.1kHz边界、声压与功率的dB、cd/lm/lx、CCD/CMOS概括、偏振与色差立体、LCD与OLED、亮度适应与同时动态范围等容易背错之处已注明。现有材料未覆盖的录音内容和未查看的外链演示，不借推测补成教师原话。

**配套速查：**`Cheat-Sheet-A4-Duplex.md` 是双面页的可编辑文字；`COMP7503-Cheat-Sheet-A4-Duplex.pdf` 是供一张A4双面打印的两页PDF。长文档负责完整理解，双面页保留跨章节的定义、公式、机制流程与答题触发词。
