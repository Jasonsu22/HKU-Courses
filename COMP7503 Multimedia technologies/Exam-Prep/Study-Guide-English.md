# COMP7503 Multimedia Technologies: Complete Revision Notes for Lectures 1–5 (English Edition)

> Version: 2026-10-19, revised English edition. Purpose: understand every concept, mechanism and example, then use the companion A4 sheet to recall answers. These notes are organized by slide deck and topic and provide full explanations in English, exam-ready answers, worked calculations, distinctions that are easy to confuse, and page-by-page coverage records. The existing companion two-sided A4 PDF is in Chinese.

## 0. Scope, Assessment Information and Sources

### 0.1 What This Revision Covers

For your requested revision of the first five teaching sessions, this edition works through **five subject slide decks, S01–S05, containing 231 physical PDF pages**, together with the **eight exported original classroom transcripts** currently available. Definitions, principles, comparisons, workflows, calculations and classroom examples are developed in the relevant sections; the work is not another shortened version of the automatic meeting summaries. Chapter numbers organize the knowledge: **slide-deck numbers, revision-note chapters and the Lecture numbers in the timetable do not correspond strictly one to one**. One teaching session can span several decks.

The included decks are Introduction (35 pages), Elements of Multimedia Computing (22 pages), Example Applications (63 pages), Media Sensor and Reproduction 1 (49 pages), and Media Sensor and Reproduction 2 (62 pages). S00, the course-information deck, is used to check assessment arrangements and is not included in the 231 pages. S06, Multimedia Documents, is outside the main scope of this requested revision; foundational ideas already covered in the first two decks, including synchronization across sources and system organization, are retained in full. **The source files keep their original filenames**, as listed in Section 0.4.

**The source gaps remain relevant:** the first five scheduled sessions were on 3, 10, 17 and 24 September and 8 October. The available recordings cover only the latter four dates; no recording for 3 September was found. The 8 October recording begins partway through material related to speech recognition. Full slides are available for the loudspeaker and other material in S05 p.2–11, but the corresponding classroom explanation segment was not found. Where a demonstration is available only as a video link in the slides, without verifiable footage or a transcript, its details are not invented. These notes can therefore provide **page-by-page coverage of the knowledge in the acquired slides**, but cannot claim to recover all unknown remarks from missing recordings.

### 0.2 Assessment Facts and Possible Revision Topics

- S00 PDF p.13 gives the assessment structure: Final Examination 50%; In-Course Assessment 50% in total, consisting of Written Assignment 10%, Quiz 20%, and Programming Assignment 20%. **The Quiz contributes 20 percentage points to the overall course grade; do not multiply that figure by 50% again.** The previous wording, “20% of the in-course assessment,” was potentially misleading and has been corrected.
- S00 PDF p.16 lists **Thursday, 22 October 2026** as “Quiz & Programming Tutorial.” Around T08 01:27:37, the lecturer says that the Quiz will take approximately the first one and a half hours, followed by a tutorial. Moodle and the lecturer's notices govern the actual arrangements.
- Around T08 00:05:02, the lecturer says that the cheat sheet may be printed or handwritten and is limited to A4 size. **Following the additional rule you confirmed, the companion quick-reference edition uses both sides of one A4 sheet.** The complete notes retain the detailed explanations, while the two-sided sheet provides examination lookup material and answer cues. The existing companion PDF is the Chinese version.
- None of the acquired material establishes an official written Quiz scope consisting of a particular page range. The scope here follows your requested first five teaching sessions and S01–S05. Labels such as “Exam-ready answer” and “Revision focus” identify answer structures organized from the material; **they are not questions announced by the lecturer or a guarantee that those topics will be examined**.

### 0.3 How to Use This Long Document

On the first pass, read the principles in Chapters 1–6. For each section, identify the problem being solved, then learn the inputs, processing steps and outputs, and finally understand the limitations. On the second pass, work through the calculations in Chapter 7 and check that you can write the formula, substitute values with consistent units, and explain the result. On the third pass, use the questions in Chapter 8 to find gaps in your understanding, then mark unfamiliar topics on the companion two-sided A4 sheet.

The exam-ready answer paragraphs provide a framework for expression; they do not need to be memorized word for word. A short answer can usually follow “definition → principle/workflow → example or comparison → limitation.” A calculation can follow “given quantities → unit conversion → formula → substitution → result/assumptions.” An abbreviation or a handful of technical terms alone is not a complete answer.

### 0.4 Source Identifiers and Page-Number Rules

`[Sxx PDF p.x–y]` always refers to physical PDF pages counted from 1 in a PDF reader; it may differ from the printed footer number. `[Txx time]` identifies a timestamp in the original recording transcript. Long ASR paragraphs can be located only by their existing paragraph-start timestamps; sentence-by-sentence timings are not fabricated. “Explanatory supplement” marks standard background added to clarify a mechanism and does not mean that the lecturer stated it verbatim.

- S00: 00 - Course Information.pdf, 20 pages.
- S01: 01 - Introduction.pdf, 35 pages.
- S02: 02 - Elements of Multimedia Computing.pdf, 22 pages.
- S03: 03 - Example Applications.pdf, 63 pages.
- S04: 04 - Media Sensor and Reproduction - 1.pdf, 49 pages.
- S05: 05 - Media Sensor and Reproduction - 2.pdf, 62 pages.
- T01: 10 September, 19:01, 多媒体-01, 43 minutes 42 seconds.
- T02: 10 September, 19:59, 多媒体-02, 36 minutes 42 seconds.
- T03: 10 September, 20:36, 多媒体-03, 23 minutes 58 seconds.
- T04: 10 September, 21:10, 多媒体-04, 29 minutes 51 seconds.
- T05: 17 September, 19:01, 多媒体-01, 52 minutes 30 seconds.
- T06: 17 September, 20:05, 多媒体-02, 1 hour 18 minutes 19 seconds.
- T07: 24 September, 19:00, 多媒体-01, 2 hours 17 minutes 42 seconds.
- T08: 8 October, 19:45, 多媒体-01, 1 hour 28 minutes 30 seconds.

Automatic meeting summaries are used to locate and cross-check topics. Technical interpretation is based on the slides, original transcripts and necessary corrections. For example, ASR sometimes recognizes candela as camera and CMOS as Simons; these notes use the correct slide terminology. The original transcript files remain unchanged.

### 0.5 Contents

1. Introduction: multimedia definitions, the evolution of communication, experiential environments, and synchronized systems with multiple sources.
2. Elements: experience, information, knowledge, the perceptual cycle, the semantic gap, and system components.
3. Example Applications: audio, image and video enhancement; detection, recognition, reconstruction and retrieval; DIKW.
4. Sensors & Digitization: sensors, limitations, waves, sampling and quantization, sound, and microphones.
5. Sound Reproduction, Speech & Music: loudspeakers, spatial hearing, speech, musical sound, and synthesis.
6. Light, Imaging & Vision: optical quantities, image formation, cameras, displays, the human eye, and color.
7. Worked Calculations: complete formulas, units, substitutions and results.
8. Integrated Short Answers and Comparisons: answer structures for examination revision.
9. Source Inventory, Recording Locations and Final Coverage Checks.
## 1. Introduction: What Problems Does Multimedia Computing Solve?

### 1.1 Defining Multimedia: Why “Music and Pictures” Is an Incomplete Answer

**Definition.** Multimedia combines several media to communicate task-relevant information to a user through one or more sensory channels. Common media include text, graphics, photographs, sound, animation and video. They can stimulate sight and hearing, with possible extensions to touch, smell and taste. Using several media does not require stimulating several senses simultaneously: text and photographs primarily address vision but are still different media forms.

**Why combine media?** Every sense and medium reveals only part of reality. A recording of a sentence may preserve the tone of voice while omitting who spoke and in what setting. Text alone can also lose intonation, actions and the surrounding scene. The slides illustrate this with an instruction that is easy to misinterpret. Once the context identifies the speaker as a dentist, the reader can understand it as part of a dental examination. The lesson is to supply evidence required by the task that one medium does not provide; simply increasing the number of media is not the objective.

**Why are audio and video so common?** Humans have strong visual and auditory analysis capabilities and rely heavily on them in everyday activity. Cameras, microphones, displays and loudspeakers can already capture and reproduce these signal types relatively conveniently, so many current multimedia systems are built around audio and visual data. The slides describe taste, smell and touch as harder to acquire and reproduce. This should be understood as a difference in implementation difficulty and prevalence, not a claim that these senses can never be represented digitally.

**Exam-ready answer.** “Multimedia combines several media to deliver relevant information through one or more sensory modalities. A single medium provides only partial evidence, whereas complementary media can reduce ambiguity and communicate an event more completely. For example, text describing an instruction becomes much clearer when the associated visual scene and context identify the speaker as a dentist.”

Source: [S01 PDF p.2–7]. Page 3 introduces a demonstration video. These notes retain its teaching question, “Is audio alone enough?”, without inventing details unavailable in the provided material.

### 1.2 Computing and Multimedia Computing: From Signals to Relevant Information

**What is computing?** The course treats computing as a goal-oriented activity that uses, benefits from, or creates computing machinery. It includes much more than arithmetic. A system may acquire, store, compress, transmit, analyze, select and present data; these operations should serve a task.

**What does multimedia computing do?** It uses signals produced by different sensors, integrates the parts relevant to the current problem, and selects appropriate media for presenting the result. Its two goals are sharing information about experiences and extracting knowledge from experiences. Recording audio and video acquires material. Aligning the audio with slides, locating the segment in which the lecturer explains a concept, and helping a student understand that concept demonstrate information organization and a task objective.

**Media and modalities.** A medium is a form in which information is carried, such as text, images or video. A sensory modality is a perceptual channel, such as vision or hearing. **Explanatory supplement:** a video stream can consist solely of an image sequence. What people commonly call a video file often packages a video track and an audio track in one container. This does not justify defining video strictly as “sound plus images.”

**Exam-ready answer.** “Multimedia computing acquires signals from multiple sources, integrates and processes the relevant evidence in the context of a task, and presents useful information through suitable media. Its goals include sharing experiences and extracting knowledge from them. Its output should be relevant information or insight, rather than merely an unorganized collection of files.”

Source: [S01 PDF p.8, 32–34].

### 1.3 Three Dimensions of Communication: Time, Space and Addressee Invariance

The course compares communication technologies using three questions: can information be preserved and replayed across **time**, transmitted to distant locations across **space**, and delivered to a larger or different set of **addressees**? Here, invariance is a teaching term for reducing a particular temporal, spatial or audience constraint. It does not mean that transmission has no loss or delay.

1. **Across time.** Recordings, writing and photographs allow people to receive a record after an event has ended. An absent student reviewing a lecture recording later is an example of temporal separation. Storage media, encoding formats and available playback equipment support it.
2. **Across space.** Telephones, radio and network meetings connect people at different locations. They require signal encoding, a communication channel and a receiving endpoint. Sending a physical letter also crosses space, although its speed differs from real-time communication.
3. **Across addressees.** Printing, broadcasting and online publication reduce the cost of delivering the same content to many people. This dimension concerns distribution scale and whether receivers can select content according to their interests.

**How to answer a comparison.** First explain which signal an invention converts into a communicable form. Then ask whether it can be saved for later, sent to distant places, and received by many people. Do not merely memorize “telephone = space” without the reason: a conventional telephone extends the range of natural spoken communication, but does not automatically create a persistent record for future replay.

Source: [S01 PDF p.9–16].

### 1.4 The Evolution of Communication: Which Constraint Did Each Invention Reduce?

**Spoken language.** People produce continuous sounds with their speech organs and use a shared language to describe complex facts. Without recording or remote communication channels, speaker and listener generally need to be close in time and space, and the audience is limited. Speech is natural and direct, but the sound is transient.

**Written language.** Developing from forms such as drawings, writing preserves language and descriptions of experience as symbols. Information can therefore outlast an individual's immediate memory and lifetime. Early stone tablets were cumbersome; paper and ink improved portability and made records easier to move between locations. The crucial transition is from fleeting sound to a durable, transportable record.

**Printing.** Repeatable document copying enables mass distribution, reduces manual copying costs and improves consistency between copies. The slides use Gutenberg's printing technology around 1440 as a historical example. The point is the relationship between mechanical reproduction and mass communication; it is not a claim about the world's earliest printing technology.

**Telegraph and telephone.** Telegraphy encodes symbolic information into signals suited to long-distance channels and substantially reduces message delivery time. Telephony carries natural speech to distant people without requiring each utterance to be rewritten as text. The slides identify communication across space as the principal breakthrough for both. Whether a telegraph preserves a paper tape or a telephone records a call depends on additional storage functions.

**Radio.** Wireless distribution delivers sound to many receivers simultaneously, reducing audience-size constraints and supporting real-time mass communication. **Movies and television** engage sight and hearing together, communicate scenes more naturally and can evoke emotions effectively. Movie content is recorded in advance and can be shown repeatedly. Television's characteristic historical role is live broadcasting across locations; recording the broadcast additionally supports later replay.

**Recording media, digital media and networks.** Magnetic tape, optical discs and hard disks allow sound and images to be preserved, copied and distributed. Digitization also enables machines to edit, enhance, search and analyze those records. Distribution can use physical copies, copying over wires or the Internet. In addition to extending distribution, the Internet allows searching, on-demand access and personalized selection, enabling receivers to explore information actively.

**Exam-answer framework.** “Communication technology progressed by reducing constraints on time, space and audience. Writing and recording preserve information across time; telegraphy and telephony extend it across space; printing and broadcasting increase the audience. Digital media enable machine processing, while the Internet combines remote distribution with interactive and personalized access.”

Source: [S01 PDF p.10–16].

### 1.5 How Computers Became Everyday Multimedia Devices: Bottlenecks and Changes

**The 1960s example.** The slides use the IBM 1620 to illustrate large early computers with very limited storage, paper-tape or punched-card input/output, and software such as assembly language and Fortran. Some arithmetic operations were implemented using lookup tables. Its resources and interaction methods were far removed from present-day continuous audio/video processing. The machine-specific details provide historical context; they do not imply that every early computer lacked an arithmetic unit.

**Before the 1990s.** Four interacting limitations restricted the widespread adoption of audio/video computing: CPU processing power, storage capacity, network bandwidth and processing algorithms. Even if a sensor could acquire a signal, a computer might be unable to store it, process it quickly enough or transmit it. The slides illustrate this with PCs that had low CPU clock rates, small memories and disks, low resolution and limited colors. Applications were still largely text-based.

**The early to mid-1990s.** Improvements in CPUs, memory, graphics modes and disks, combined with sound cards, CD-ROMs and multimedia software, made sound, images and games common PC capabilities. The slides illustrate stages in this transition using 386/486 processors, Pentium, Windows 95, stereo sound and media players. The important development was the joint maturation of hardware, software and distribution media; no single CPU independently “invented multimedia.”

**The late 1990s and the twenty-first century.** Once multimedia capabilities became standard, manufacturers no longer needed to label a machine a “multimedia computer.” Research into speech, audio, image and video processing, compression and recognition nevertheless continued, driven by telephony, broadcasting and entertainment. Mobile devices then placed cameras, microphones, displays, networks and diverse sensors alongside users, supporting acquisition at any time and communication from many locations.

**Exam-ready answer.** “Multimedia became practical through joint advances in processing power, memory and storage, communication bandwidth, algorithms and software. Early machines could not economically handle the size and real-time demands of audio and video. As these constraints weakened, multimedia became standard on PCs and later on mobile devices.”

**Limits of the historical examples.** Specifications under “before 1990s” are illustrative examples, not upper limits for every computer throughout that period. The statement about mobile devices replacing PCs describes a development trend, not the disappearance of PCs. On p.20, the text and picture give inconsistent brand names for the same Presario machine; that inconsistency should not be memorized as a technical fact.

Source: [S01 PDF p.17–22].

### 1.6 Multiple Sensors in Mobile Devices: What Evidence Does Each Provide?

A phone is more than a smaller computer. Its camera captures light to form images and video; its microphone captures variations in sound pressure; GPS provides geographic position; a magnetometer supports direction estimation; an accelerometer measures acceleration; and a gyroscope measures angular velocity. A proximity sensor detects nearby objects, and an ambient-light sensor supports brightness adjustment. Some devices also provide pressure, temperature and humidity measurements. A touchscreen captures contact locations and gestures, while a fingerprint sensor acquires fingerprint features for identity-related tasks.

**Why combine them?** GPS alone may provide a position without identifying the direction the user faces. Combining location, orientation and camera information supports more meaningful navigation and augmented reality. Accelerometers and gyroscopes supply complementary evidence for orientation estimation; camera imagery alone should not automatically be treated as a reliable motion state. Devices can also directly measure quantities that humans cannot measure precisely through their senses, such as latitude and longitude. Those readings still need interpretation.

**Explanatory supplement: distinguish the categories in the diagram.** The slide's phone illustration also includes Bluetooth, NFC and a voice processor. Bluetooth and NFC are primarily communication technologies, while the voice processor is a processing module. Every item in the illustration should not automatically be called a physical sensor. Nor does the diagram imply that every phone contains temperature and humidity sensors.

**Exam-ready answer.** “A mobile multimedia device combines capture, sensing, computation, communication and presentation. Cameras and microphones capture visual and acoustic content; GPS and inertial sensors provide location and motion context. Integrating complementary measurements supports tasks such as navigation that cannot be solved reliably using one signal alone.”

Source: [S01 PDF p.22–24; the sensor illustration on p.23 has been visually checked].

### 1.7 How Applications Drive Technology: Co-evolution of Tasks, Data and Devices

The slides describe a progression in which applications drive technology. Numerical computation requires arithmetic processing; business data processing drives alphanumeric processing, databases and servers; documents, spreadsheets, email and the WWW drive personal computers, graphical interaction and networking; social networks, photography, instant messaging and sharing drive mobile communications, audio/video processing and location services.

The implication is that system capabilities should be derived from the task to be solved. Video sharing requires compression, storage, wireless bandwidth and playback as well as a camera. Navigation requires road data, route computation and an output that a driver can understand as well as GPS. The slides leave future applications, technologies and devices as open questions; a prediction about a particular product should not be presented as an established course conclusion.

**Exam-ready answer.** “Applications drive computing technology by imposing new data, processing and interaction requirements. Numerical computation emphasized arithmetic; business systems emphasized structured data and databases; multimedia sharing emphasized sensing, compression, networking and mobile devices. A multimedia design should therefore begin with the application objective and derive the required technologies.”

Source: [S01 PDF p.24].

### 1.8 Five Properties of Emerging Applications: Why One Static Table Is Insufficient

**First, spatiotemporal data and live streams are normal.** Data has a time and place of acquisition as well as values, and it changes continuously. Examples include bus locations, traffic video and temperature/humidity sequences. Ignoring timestamps may incorrectly combine observations from different moments into a single state.

**Second, the whole event matters.** An isolated frame, temperature reading or order record supplies only partial information. Systems need to correlate multiple sources to interpret a complete event and situation. For example, understanding traffic congestion may require speed, location, time and visual evidence.

**Third, users want information and insights.** Users usually want to know where congestion is occurring and which route they should take, rather than inspect the raw data from every device. As far as possible, results should not require users to understand every data format and sensor source. Internally, however, the system still needs provenance and reliability information to interpret the evidence correctly.

**Fourth, only relevant information is useful.** Transmitting more data does not automatically provide more help. Relevance depends on the user's current task and context. A learner seeking the derivation of a formula should be shown the associated explanation and board work, rather than every frame of the entire lecture.

**Fifth, exploratory browsing is important.** Users can begin with an overview, zoom into a region, select a time interval and follow an event while gradually refining their question. This differs from requiring a precise relational query at the outset. The slides identify exploration as an important mode of interaction in emerging applications; they do not claim that SQL or database queries have become useless.

**Exam-ready answer.** “Emerging applications involve live spatiotemporal streams, require a holistic view of events, and prioritize task-relevant insights over isolated media. They support exploratory browsing because users often refine their interests while interacting with the data. Therefore, systems must correlate multiple sources and present useful information in context.”

Source: [S01 PDF p.25–26].

### 1.9 Three E-commerce Questions: Changing Information and Expected Computing Results

The slides use three e-commerce questions to show that possessing a database does not by itself define a computing task. **How many orders were processed between two regions?** This is normally a statistical count with specified regions, a time interval and a business counting rule. Without a time limit, “how many” has no stable interpretation. **Which parts of the world are experiencing rapid sales growth?** This requires comparing sales across periods and possibly normalizing for population, baseline size or seasonality, with results showing geographic distributions and trends. **What is the hottest item now?** This first requires defining popularity in terms of sales volume, revenue, searches, growth rate or a combined metric, and then keeping the result up to date.

The questions differ in how quickly information changes, whether several dimensions must be combined, whether the output is a number or a trend/ranking, and whether live insight is required. **Explanatory supplement:** rapid growth can mean a large absolute increase or a high growth rate. A product with a small baseline and a high growth rate is not necessarily the one with the largest total sales. The system must therefore interpret the question's meaning and context instead of merely returning records.

**Exam-ready answer.** “An order-count query produces a value for a defined region and time interval. A growth query compares periods and regions to reveal change. A ‘hottest item now’ query requires an explicit popularity criterion and up-to-date data. The expected result and the temporal nature of the information determine the processing and presentation required.”

Source: [S01 PDF p.26–27; the discussion of growth rates and metric definitions is an explanatory supplement].

### 1.10 Experiential Environments: Perceiving and Exploring Data Directly

**Definition.** An experiential environment lets users use their senses directly to observe data and information associated with an event, then interact naturally according to their particular interests in that event. Its goal is to improve human-machine synergy. Humans are good at conceptual, perceptual and contextual judgments; computers are good at large-scale, repetitive and precise mathematical and logical processing. Their strengths should cooperate within the task.

**Property 1: direct and intuitive.** Users should quickly understand the overall event being presented and continue exploring through familiar actions, without first learning many unfamiliar commands. Slide examples include swiping photographs, tapping application icons and using body movement with Kinect. The action should have an understandable relationship to its task result; a graphical interface alone does not guarantee intuitiveness.

**Property 2: the same query and presentation spaces.** Users express a query or modification in the same environment in which they view the result, and immediately see the resulting relationships. A spreadsheet illustrates this: changing a displayed value updates formula results and charts. Here the slides use WYSIWYG to emphasize consistency between querying and presentation, extending beyond similarity between an editing view and a printed page.

**Property 3: account for user state and context.** The system considers the user's task, existing knowledge, situation and current state to support perceptual analysis and exploration. Games combine audio, video and tactile feedback so that actions and events occur in a coherent virtual environment. **Explanatory supplement:** navigation should account for a user who is driving, prioritizing timely, concise spoken instructions and route cues rather than complex tables that demand sustained reading.

**Exam-ready answer.** “An experiential environment enables users to observe and explore event-related information directly through their senses. It should be direct and intuitive, keep query and presentation in the same interaction space, and account for user state and context. This combines human perceptual and conceptual abilities with computer processing, improving human-machine synergy.”

Source: [S01 PDF p.28–32; the navigation example is an explanatory supplement].

### 1.11 A Formal Multimedia-Computing Framework: S, M and F

Assume that multiple sensors in a physical environment produce synchronized data streams **S₁,…,Sₙ**. These streams may belong to **K data types**, such as image sequences, audio and motion-detector readings. The number of sensors/streams, n, differs from the number of data types, K: several cameras can generate multiple streams of the same visual type.

Each stream has **Mᵢ, its metadata**, such as time, location, device parameters and manual annotations. The system extracts one or more **Fᵢⱼ feature streams** from stream i, with j identifying a particular feature stream. Examples include image motion, audio spectral features and activity intensity from a motion sensor. Different input streams need not supply the same number of features. **Explanatory supplement:** features are useful representations derived from raw data, while metadata describes the data itself and its acquisition conditions. Their sources and roles differ and should not be conflated.

Remember the workflow as **environment → synchronized source streams S and metadata M → feature streams F → integration and processing in the task context → insights required by the user → user feedback as a new input → further processing**. The user is not only a passive receiver at the end. Queries, selections and feedback can become input streams, allowing the results to evolve with the task.

**How does this differ from monomedia processing?** Computer vision may focus on visual evidence, while audio processing may focus on sound. This course emphasizes exploiting correlations between partial observations from multiple sources to obtain more complete information in the context of a problem. Placing unrelated videos and music in the same folder does not achieve that integration. Multiple sources need not all use different media: video from several viewpoints can provide complementary evidence.

**Exam-ready answer.** “Let Sᵢ be a synchronized sensor stream, Mᵢ its metadata, and Fᵢⱼ its j-th feature stream. A multimedia system extracts features and integrates correlated evidence from these streams in the problem context to generate useful insights. User feedback can be treated as another input stream. The central task is the combination of partial information, rather than isolated processing of one medium.”

Source: [S01 PDF p.33–34].

### 1.12 Recovering a Travel Route from Photo Metadata: From Records to Insight

A photograph's content is its image, such as people, buildings or scenery. It may also carry metadata including capture time, latitude and longitude, camera model and exposure settings. Sorting photographs from one trip by time and plotting their locations on a map can reveal the travel route. This illustrates “metadata as input, insight as output”: the raw fields contain isolated times and positions, while the route organizes them into an understandable sequence of events.

**Explanatory supplement:** locations without timestamps usually do not reliably establish the order of travel. When GPS is absent, manual location tags or other sources may be needed. Missing GPS, incorrect clocks or metadata removed during export can affect the result; not every photograph necessarily contains a complete travel trace. Recovering a route may also require no individual identification of every object in every photograph, illustrating the principle of processing only relevant information.

**Exam-ready answer.** “Photo metadata such as capture time and GPS coordinates provides context beyond the pixels. Sorting the photos by time and mapping their locations can reveal a travel route. The system transforms isolated metadata into event-level insight, illustrating task-specific multimedia integration.”

Source: [S01 PDF p.35; the map, photograph and metadata illustration have been visually checked].

## 2. Elements of Multimedia Computing: Experience, Perception, Meaning and Systems

### 2.1 The System Objective and Two Challenges: Correlation and Holistic Information

The objective of a multimedia system is to process different data types as **one correlated set of streams**, producing the information and knowledge needed to solve a problem. Merely storing data on the same computer does not make it correlated. The system must determine whether sources concern the same event, which time intervals correspond, which objects they describe, and what question they can answer together.

**Challenge 1: discovering correlations.** The slides and classroom recording explain that microphone audio and computer slide images in a lecture recording come from different devices. Their timelines must be aligned to establish which slide or action an explanation concerns. If device clocks differ or drift over time, their timestamps cannot simply be assumed identical; synchronization or correction is needed.

**Challenge 2: combining partial evidence into a whole.** Classroom comfort depends on humidity and other conditions as well as temperature. A temperature measurement and an image showing whether a person is wearing a mask answer different questions; together they can support a particular screening decision. Vehicles also need to relate several viewpoints and motion information to interpret their surroundings. The comfortable temperature range and number of cameras mentioned in class are examples, not universal standards or minimum specifications.

**Exam-ready answer.** “The objective is to process different streams as one correlated set representing the information needed for a problem. The main challenges are discovering cross-stream correlations and combining partial evidence from disparate sources into a holistic interpretation in context. A lecture recording, for example, must align audio and slide images so that the explanation refers to the correct visual material.”

Source: [S02 PDF p.2; first recording on 2026-09-10 at 19:01, paragraphs beginning 00:18:53, 00:22:24, 00:24:33, 00:25:16, 00:26:40 and 00:28:03]. These timestamps identify paragraph starts in the original transcript. An untimed sentence within a long paragraph is not assigned a fabricated exact time or presented as a precisely located verbatim quotation.

### 2.2 The Relationship Between Experience, Information, Knowledge and Communication

**Experience** means directly observing or participating in events. Attending a class, for example, includes hearing explanations, seeing board work, asking questions, interacting and experiencing emotions at that time. People develop knowledge of the world as they accumulate and connect experiences. **Information** is an abstract and efficient representation of experience, such as “this class explained that perception requires prior knowledge.” It reduces the burden of communication but leaves out some experiential details.

**Knowledge** consists of the understanding, structures and regularities people form from experiences and information. **Explanatory supplement:** data comprises recorded symbols or measurements; relating it to context and existing knowledge makes meaningful questions answerable. Data, information and knowledge are not determined simply by file extensions. The same recording is sampled data for a device, may communicate a definition to a student, and may provide a new basis for reasoning to someone who already understands that definition.

**Communication** is the process of sharing experiences and information, allowing participants to be separated in time and space. What we usually transmit, however, is a selected and encoded description or sensory record. We cannot give a receiver the sender's complete subjective experience unchanged. The slides therefore emphasize the loss of part of the act of experiencing during communication.

**Exam-ready answer.** “Experience is direct observation of or participation in events. Information is an abstract and efficient representation communicated about those experiences. Knowledge develops as experiences and information are accumulated and related. Communication allows sharing across time and space, but the representation does not reproduce the sender's complete act of experiencing.”

Source: [S02 PDF p.3–6; the explanation of data layers is an explanatory supplement]. The original DIKW-pyramid slide is [S03 PDF p.61] and should be reviewed together with the applications chapter.

### 2.3 Why Relevant Experience Helps Understanding: Masks, Trains and Cultural Gestures

The slides show a masked passenger sitting in a largely empty MTR train. Knowing its pixels and object names may not explain why the photograph is significant. Someone with relevant epidemic experience may connect the mask, empty carriage and travel behavior to interpret the risks and social circumstances. The classroom discussion compares a situation in 2003 with the epidemic experience students acquired later. The point is that **shared experience helps interpret information**. The image alone cannot rigorously establish a unique capture year or event; additional context is required.

The lecture also uses cultural differences in number gestures to show that the same movement may have different meanings in different regions. Switching modalities does not automatically remove ambiguity. When people replace an unfamiliar spoken language with gestures, the gestures themselves still depend on shared conventions.

**How to address this.** Provide examples and context relevant to the receiver, establish a shared dictionary, and explain how symbols map to what they represent. Where necessary, photographs, text, time and location can supply complementary cues. The goal is to provide missing conditions for understanding, rather than merely accumulate more media.

**Exam-ready answer.** “Effective communication depends on relevant prior experience and shared conventions. The same image or gesture can lead to different interpretations when receivers have different backgrounds. Multimedia and contextual explanations can provide complementary cues, while an agreed dictionary establishes the intended meanings of symbols.”

Source: [S02 PDF p.4–7; the MTR photograph on p.5 has been visually checked; first recording on 2026-09-10 at 19:01, the long paragraph beginning 00:28:03 includes examples concerning breakfast, food in Hong Kong, the MTR and cultural gestures]. This paragraph has no finer-grained timestamps, so exact timings are not invented for individual examples.

### 2.4 Dictionaries and Percepts: Shared Vocabulary Beyond a Language Dictionary

The core of a **dictionary** is **a collection of symbols and their meanings agreed by the communicating parties**. It links the signs a receiver encounters to the content the sender intends. A natural-language dictionary records words. Dictionaries in computer systems may contain codes, terms, keys and associated values. Compression algorithms may also use mappings between repeated patterns and shorter codes. These applications share a mapping idea, but their specific mechanisms should not be treated as one identical algorithm.

In multimedia, a basic perceptual element is called a **percept**; visual examples include lines, curves and shapes. A system attempts to form higher-level object interpretations from these local patterns and their relationships. For example, a circular outline together with the relative arrangement of eyes, a nose and a mouth can help a person interpret a simple drawing as a face. An isolated circle alone does not establish a face; organization and a prior model are also needed.

**Explanatory supplement: percept, feature and object.** A feature often denotes a computable representation, such as edge orientation, color distribution or a local descriptor. A percept emphasizes a unit of sensory organization and interpretation. An object is a higher-level entity such as a person or car. Terminology varies between research fields, but an examination answer should at least explain the hierarchy from local signal patterns to semantic objects. A pixel should not be equated with a complete object.

**Exam-ready answer.** “A dictionary is an agreed mapping between symbols and meanings. In multimedia, percepts such as lines, curves and shapes act as basic perceptual elements that can be organized into recognizable patterns. Shared mappings and prior models make it possible to interpret sensory data rather than merely transmit uninterpreted symbols.”

Source: [S02 PDF p.7; second recording on 2026-09-10 at 19:59, 00:00:00–00:03:11; the terminology hierarchy is an explanatory supplement].

### 2.5 Objects and Events: Representing a Dynamic World

An **object** models a relatively stable entity and its attributes, such as a person, vehicle or junction. Attributes may include color, identity, position or current state. “Static components” means that objects provide an entity-level structure; it does not imply that an object can never move or its attributes can never change. An **event** models changes in relationships or states over time, such as a person entering a room, a vehicle crossing a stop line, or a passenger joining a queue.

Audio and video are inherently temporal. Sound records changes in acoustic properties, while video records changes in a visual scene. Understanding them therefore requires asking what happened, when it happened and who was involved, as well as what is present. Detecting a person describes an object. Judging that the person is entering a restricted area involves position, a spatial relationship and temporal change, and is therefore an event-level interpretation.

**Explanatory supplement: the hospital-queue example.** Objects may include patients, a queue and service counters. Events may include joining the queue, beginning a consultation and leaving. The number of people in one frame describes the current state; predicting waiting time also requires arrival rates, service speed and changes over time. People naturally reason about tasks through objects and events, so systems need representations that can align with these concepts.

**Exam-ready answer.** “Objects model the relatively stable entities and properties of a scene, whereas events model changes in object states or relationships over time. Audio and video are dynamic signals, so object descriptions alone are insufficient. A surveillance system must distinguish the presence of a person from an event such as that person entering a restricted area.”

Source: [S02 PDF p.8; second recording on 2026-09-10 at 19:59, 00:09:42–00:10:23 and 00:14:38–00:16:45; the restricted-area example is an explanatory supplement].

### 2.6 Programming Paradigms: Classroom Discussion of Procedures, Objects and Functions

The lecturer uses programming paradigms to illustrate how machine representations can become closer to human descriptions of a task. **Procedural programming** breaks a task into steps, procedures and control flow: for example, reading a list, comparing elements, swapping positions and repeating until sorting is complete. Its focus is how to execute the task step by step. C, BASIC and Pascal are language examples mentioned in class.

**Object-oriented programming** organizes state and behavior into objects. A class defines the attributes and methods of a category of objects, and interactions between objects express system behavior. A vehicle may have speed and position as state and acceleration and turning as methods. C++, Java and C# are classroom examples. A program can combine paradigms, and a language such as Python cannot be assigned absolutely to only one paradigm.

In its precise sense, **functional programming** emphasizes function application and composition, often preferring immutable data and fewer side effects. **Explanatory supplement and correction:** the classroom comparison links functional programming and AI coding with “describe what is wanted and let the system decide the details.” This is an analogy to help explain a declarative tendency, not a rigorous definition of functional programming. Calling a sorting function does not imply that an AI must invent a sorting algorithm at runtime. Generating programs through natural-language AI interaction is another interaction method and still requires checking requirements and results.

**Exam-ready answer.** “Procedural programming organizes computation as explicit steps and control flow. Object-oriented programming organizes state and behavior into interacting objects and classes. Functional programming emphasizes function application and composition, often with immutable data and fewer side effects. These paradigms provide different ways to represent a task; object-based modeling is particularly intuitive for describing entities and interactions.”

Source: [second recording on 2026-09-10 at 19:59, 00:10:23–00:23:56; the precise functional-programming definition and discussion of multiple paradigms are explanatory supplements]. This section supplements the slides with recording content; S02 does not list these programming-paradigm details.

### 2.7 Perception: Interpreting Signals to Recover Meaningful Information

**Perception** is the process of understanding sensory signals to recover useful information. Its inputs are sensory signals; its outputs are information relevant to an application context. A camera producing pixels or a microphone producing sample values performs acquisition. Identifying a pedestrian in the scene or determining what was said interprets the signal. Sensor acquisition supports a perception system but is not complete semantic understanding.

The course relationship can be remembered as **signal/data + existing knowledge + context → interpretation/information**. This is a conceptual relationship, not numerical addition. Without relevant models and conventions, a system may have abundant data but no way to know which differences matter to the task. Existing knowledge without new evidence also does not guarantee an understanding of the current environment.

The slides compare perception to constrained hypothesis generation and testing: a system proposes possible interpretations, then checks which one the current evidence supports. The phrase “controlled hallucination” emphasizes that prior models participate in constructing interpretations; it does not license arbitrary invention. Meaningful judgments must be constrained by external signals, and contradictory evidence should cause revision of a hypothesis.

**Exam-ready answer.** “Perception is the process of interpreting sensory signals to recover useful information in an application context. It requires both incoming evidence and relevant prior knowledge. The system generates possible interpretations and evaluates which is best supported by the data; therefore, the same signal can be interpreted differently under different knowledge or context.”

Source: [S02 PDF p.9–10; second recording on 2026-09-10 at 19:59, 00:23:56–00:29:23].

### 2.8 Two Visual Examples: Why the Same Image Can Be Seen Differently

**Faces and a vase.** A black-and-white outline can be seen as two faces in profile looking at each other or as a white vase between them. The pixels remain unchanged; what changes is the organization of figure and ground, the focus of attention and the object interpretation being applied. Perception does not label pixels through a simple one-to-one mapping: one signal may support several higher-level models.

**The Dalmatian.** Another high-contrast black-and-white image may appear disorganized without a cue. Once an observer knows to look for a dog, the relevant patches are easier to organize into a dog's outline. The cue supplies prior knowledge, while the input supplies evidence for or against the interpretation. A helpful cue is not necessarily a true cue; if a dog is absent, the interpretation still requires checking against the evidence.

**Exam-ready answer.** “The face–vase figure demonstrates that figure-ground organization and prior interpretation can produce different percepts from the same pixels. The Dalmatian example shows that prior knowledge helps organize ambiguous local patterns into an object. Both illustrate the interaction of bottom-up sensory evidence and top-down knowledge in perception.”

Source: [S02 PDF p.11–13, images visually checked; second recording on 2026-09-10 at 19:59, 00:29:23–00:32:24; the terms bottom-up and top-down are explanatory supplements].

### 2.9 Neisser's Perceptual Cycle: Three Components and the Correct Arrow Directions

Neisser's perceptual cycle treats perception as an active, continuing process rather than a single pass from incoming data to an answer. The **schema**, or environmental model, contains the system's existing knowledge, expectations and current model of the environment; it determines what to look for next. **Exploration** comprises observations or actions guided by that model, such as turning the head, moving a camera, zooming into an area or querying another source. The **environment/available information** supplies new samples, which in turn modify the schema.

Remember the three arrows accurately: **schema directs exploration; exploration samples the environment; environmental information modifies schema**. In other words, the model guides exploration, exploration acquires environmental samples, and environmental evidence updates the model. The new model guides the next exploration, forming a closed loop. Exploration may pause when sufficient evidence has been obtained for the task, the goal changes, or no new evidence is available. Evidence should not be selected only because it supports the initial guess.

**Explanatory supplement: looking for an object in a picture.** An observer may first suspect that an outline is a face and direct attention to possible eye and nose positions. A plausible arrangement strengthens that interpretation; contradictory detail supports changing it. A map user who inspects a region, zooms into a congestion point, checks live images and revises a route also illustrates active sampling and updating.

**Exam-ready answer.** “In Neisser's perceptual cycle, the schema directs exploration, exploration samples the environment, and available information modifies the schema. Perception is therefore active and iterative: prior knowledge guides what to inspect, while new evidence updates the model. The updated model then guides further exploration.”

Source: [S02 PDF p.14; second recording on 2026-09-10 at 19:59, 00:32:59–00:35:36; third recording on 2026-09-10 at 20:36, 00:00:31–00:03:07].

### 2.10 Wine or Soy Sauce: Context Can Help or Mislead

The slides show an advertisement at Mei Foo Station. A person holds a dark bottle with food displayed on a table. It may suggest wine paired with a meal, or the cooking, flavor and bottle context may suggest soy sauce. The brand, label, shape, text and arrangement supply evidence for further examination. At the beginning of the next recording, the lecturer continues discussing the process of making an initial guess and then seeking evidence.

The image illustrates **how prior knowledge, local cues and environmental context jointly generate hypotheses**. Product identification in this advertisement does not need to be learned as merchandise knowledge for an examination. The important explanation is to propose candidate interpretations, inspect details that distinguish them, and revise the model when evidence conflicts. Context is not an infallible label: prominent food or advertising words can initially lead the observer toward an incorrect conclusion.

**Exam-ready answer.** “Context creates expectations that guide the interpretation of ambiguous visual content. In the wine/soy-sauce example, bottle appearance, food, text and brand information provide different clues. The observer should compare these clues and update the hypothesis when evidence is inconsistent, illustrating the perceptual cycle and the possibility of contextual bias.”

Source: [S02 PDF p.15–16, advertisement visually checked; second recording on 2026-09-10 at 19:59, from 00:35:36 onward; third recording at 20:36, 00:00:07–00:03:07].

### 2.11 Four Classes of System Problems: Representation, Presentation, System Support and Integration

**First, how can data be represented compactly?** Raw audio and video are large, while storage and bandwidth are limited. Appropriate representations, encoding and compression are needed. An answer must consider both size and retained information. Very small data that no longer preserves essential recognition cues may fail the task.

**Second, how should large amounts of data be presented?** Showing everything at once increases cognitive load. Information should be organized around the task, use suitable media and support navigation and exploration. A long lecture recording can combine chapters, a timeline, subtitles and slides so that students can locate a definition without replaying the entire recording from the beginning.

**Third, how should system issues arising from heterogeneous data be handled?** Sources can differ in format, sampling rate, data rate and clock, while networks impose bandwidth limits and varying delays. Capture, buffering, communication, processing, synchronization and output must be coordinated. **Explanatory supplement:** placing video frames and audio samples in the same array does not automatically solve synchronization or real-time playback.

**Fourth, how can streams be combined into the required information?** The system must select task-relevant sources and features, establish relationships between them, and then infer the result. For example, spoken words may refer to “here,” while the image identifies the formula being indicated. One source alone may be insufficiently explicit.

**Exam-ready answer.** “Multimedia design addresses compact representation, effective presentation, system support for heterogeneous streams, and information integration. Compression must respect storage and bandwidth limits; presentation must communicate the intended information; the system must handle formats, timing and processing; integration must combine the relevant evidence for the task.”

Source: [S02 PDF p.17; third recording on 2026-09-10 at 20:36, paragraphs beginning 00:03:07 and 00:04:22 discuss bandwidth and compression; the concrete elaborations are explanatory supplements].

### 2.12 The Semantic Gap: Machine Representations and Human Meaning

Conventional digital systems encode data as bits and bytes and organize it into representations such as arrays, lists, tables, images, audio or video. Users describe the world through objects, events, intentions and tasks, such as “a person crossing the road dangerously” or “find the part of the lecture explaining the sampling theorem.” No natural one-to-one correspondence connects low-level pixel values to these concepts.

The **semantic gap** is the difference between the information a machine can extract from perceptual data and the interpretation a user gives to the same data in a particular situation. It concerns more than a difference between binary values and words: it separates low-level measurements and features from higher-level meaning. Finding a red region does not establish whether it is a traffic sign, clothing or lighting. Recognizing a face does not automatically establish the event in which that person is participating.

**How can the gap be reduced?** Within a task context, combine content features, metadata such as time and place, object relationships, evidence from multiple sources, existing models and user feedback to form more meaningful representations progressively. **Explanatory supplement:** learned models can improve semantic interpretation, but this does not justify claiming that multimodal AI has eliminated every semantic gap. Goals, culture and missing evidence can still produce different interpretations of an event.

**Exam-ready answer.** “The semantic gap is the difference between information that a machine can extract from perceptual data and the interpretation a user gives to the same data in a particular situation. Computers use low-level representations and features, whereas users reason about objects, events and intentions. Multimedia computing reduces the gap by combining content, context, prior knowledge and correlated sources.”

Source: [S02 PDF p.18–19; third recording on 2026-09-10 at 20:36, 00:10:10–00:14:30].

### 2.13 Content, Context and Metadata: What Is Present and How It Is Interpreted

**Content** is the acquired media and signal data, such as the pixels in a photograph or waveform in a recording. **Context** consists of interrelated conditions surrounding acquisition and interpretation, including capture time, location, equipment, event, user task and environment. **Metadata** is data about data. It may preserve some context, as EXIF records can preserve time, camera settings and possibly GPS information for a photograph.

The three concepts should not be equated. A photograph's GPS field is metadata that can indicate location as context. A user's task of recovering a travel route is also context but may not be stored in the photograph's EXIF. Not all metadata supplies semantic background: file size describes the file, but does not establish what its scene means. The slides emphasize using content and context together. Pixel analysis alone is insufficient, and tags should not replace examination of the actual content.

**Example.** A crowd photograph can mean different things when captured at a concert, a station evacuation or a graduation ceremony. Time, location, sound, preceding and following video, and the user's question can help distinguish the events. Photo-management software also uses metadata to create understandable organization by grouping albums according to time and location.

**Exam-ready answer.** “Content is the acquired media data, while context is the set of related conditions in which the data is acquired or interpreted. Metadata is data about the data and may encode contextual parameters such as time and location. Combining content with context helps resolve ambiguity and supports a more accurate interpretation.”

Source: [S02 PDF p.20–21, photo-management and EXIF illustration visually checked; third recording on 2026-09-10 at 20:36, 00:14:30–00:17:58; the crowd example is an explanatory supplement].

### 2.14 Five Components of a Multimedia System: From Acquisition to Output

**Capture devices.** Cameras, video recorders and microphones provide audio/visual input; keyboards, mice and touchscreens provide user input; pressure sensors provide physical measurements. Inputs need not come only from on-site hardware. **Explanatory supplement:** obtaining previously acquired sensor data through an HTTP interface also provides a system input, but an API is not itself a sensor that converts a physical quantity into a signal.

**Storage devices.** Hard disks, flash storage and optical discs preserve media and metadata. Memory buffers support stream processing, while databases support organization and retrieval. Storage enables later use and accommodates mismatches in processing speeds, although permanent retention is not mandatory for every real-time system.

**Communication networks.** Local networks, 4G/5G, Bluetooth and RF carry data from acquisition to processing or output endpoints. The design must account for required distance, data rate and latency. Networks with different names are not automatically interchangeable, and a system should not assume that a network always transfers all data instantaneously without loss.

**Computer systems.** Workstations, servers and DSPs perform decoding, filtering, compression, feature extraction, fusion, analysis and control. DSP stands for digital signal processor and is suited to signal-processing tasks. A separate DSP chip is not required in every multimedia system.

**Output devices.** LCD and other displays provide visual output; loudspeakers provide auditory output; vibration motors and haptic feedback provide tactile output. The presentation should convey the information the user needs. A row of raw numbers is not necessarily more effective than an image, graph or spoken cue.

**Complete pipeline example: a mobile call.** The microphone converts speech into an electrical signal, analog-to-digital conversion produces digital samples, and a processor encodes and temporarily stores them. The network transfers the data to the other party, where the receiver buffers and decodes it and drives a loudspeaker. A lecture-recording system similarly synchronizes microphone audio with slide images, stores the result for later revision, and may simultaneously send sound to classroom speakers.

**Exam-ready answer.** “A multimedia system includes capture, storage, communication, computation and output. Capture devices obtain sensory and user-input data; storage preserves or buffers it; networks transfer it; computer systems process and integrate it; output devices present the result to human senses. The components must work together with appropriate timing and data representations.”

Source: [S02 PDF p.22; third recording on 2026-09-10 at 20:36, 00:16:55–00:23:07; the explicit treatment of ADC and buffer functions is an explanatory supplement].

### 2.15 A Classroom Distinction: Face Detection, Recognition and System Levels

**Face detection** asks whether faces are present, where they are and how many there are, typically returning locations or regions. **Face recognition** asks who a person is or whether the face matches a known identity. The lecturer first explains detection using eyes, a nose, a mouth and their plausible arrangement, then uses distances between facial parts as an intuitive example of identity-related features. This illustrates the transition from image data to information about people.

**Explanatory supplement:** distances between facial parts are an accessible teaching example of features. They vary with pose, camera distance, expression and imaging conditions. Images of the same person are not guaranteed to have exactly identical pixel distances, and different people are not guaranteed to have different values. Modern systems may use learned feature representations. The point here is the hierarchy **raw data → features → task judgment**, not memorizing an oversimplified recognition algorithm.

**Exam-ready answer.** “Detection locates instances of a class, such as finding faces in an image. Recognition uses distinguishing features to identify an instance or match it to an identity. Both require converting raw sensory data into task-relevant representations, but their questions and outputs differ.”

Source: [second recording on 2026-09-10 at 19:59, 00:01:27–00:09:42; S02 PDF p.7–10 supplies the dictionary, object and perception framework; the discussion of modern methods and distance limitations is an explanatory supplement].

### 2.16 Page-by-Page Coverage Check for the First Two Slide Decks

Throughout this checklist, “p.” means the **physical page number** counted from 1 by a PDF reader. The printed footers in S02 skip numbers: for example, PDF p.6 has footer 7, and PDF p.22 has footer 24. This does not mean that PDF pages are missing.

- **S01 p.1:** course and chapter title page; no additional concept.
- **S01 p.2–7:** narrow interpretations of multimedia; whether audio or text alone is sufficient; the dentist context; the five senses; and the prominence of audio and vision. See 1.1.
- **S01 p.8:** computing, multimedia computing, sharing experiences and extracting knowledge. See 1.2.
- **S01 p.9:** communication across time, space and addressees. See 1.3.
- **S01 p.10–16:** spoken and written language, paper, printing, telegraph, telephone, radio, movies/television, storage, digital media, the Internet and the invariance summary. See 1.3–1.4.
- **S01 p.17–22:** computer and multimedia development from the 1960s to the twenty-first century, resource bottlenecks, PCs and mobile devices. See 1.5.
- **S01 p.23:** mobile-device sensor illustration. See 1.6; the text in the image has been checked.
- **S01 p.24:** applications driving technologies and devices. See 1.7.
- **S01 p.25–26:** spatiotemporal streams, holistic perspectives, relevant information and exploration in emerging computing applications. See 1.8.
- **S01 p.27:** different computing requirements for e-commerce order counts, regional growth and popular products. See 1.9.
- **S01 p.28:** experiential environments and human-machine synergy. See 1.10.
- **S01 p.29–31:** the three properties of intuitiveness, shared query/presentation space, and user state/context. See 1.10.
- **S01 p.32:** multimedia technology as the implementation of experiential systems. See 1.2 and 1.10.
- **S01 p.33–34:** synchronized S streams, M metadata, F feature streams, integration, user feedback, and the relationship between multimedia and monomedia. See 1.11.
- **S01 p.35:** recovering a travel route from photograph metadata. See 1.12; the image has been checked.
- **S02 p.1:** course and chapter title page; no additional concept.
- **S02 p.2:** system objective, discovery of correlations and combination of partial evidence. See 2.1.
- **S02 p.3–4:** experience, information, knowledge, communication and loss of the act of experiencing. See 2.2.
- **S02 p.5–6:** the masked-passenger MTR photograph and the significance of shared experience. See 2.3; the image has been checked.
- **S02 p.7:** dictionaries, program mappings, compression dictionaries and percepts. See 2.4.
- **S02 p.8:** objects, events and the dynamic nature of media. See 2.5.
- **S02 p.9–10:** the definition of perception, signals and existing knowledge, and hypothetical interpretations. See 2.7.
- **S02 p.11–13:** the vase/two faces, the Dalmatian and the effect of a cue. See 2.8; the images have been checked.
- **S02 p.14:** the three arrows in Neisser's perceptual cycle. See 2.9.
- **S02 p.15–16:** the wine/soy-sauce advertisement at Mei Foo. See 2.10; the image has been checked.
- **S02 p.17:** four problems concerning representation, presentation, heterogeneous systems and information integration. See 2.11.
- **S02 p.18–19:** machine representations, human abstractions and the semantic gap. See 2.12.
- **S02 p.20–21:** content, context, metadata and EXIF. See 2.13; the image has been checked.
- **S02 p.22:** the five component groups: capture, storage, networking, computation and output. See 2.14.
- **Supplementary material from the 10 September recordings:** parameters and units, clock synchronization, temperature/humidity, multisensor integration, shared experience, cultural gestures, programming paradigms, and face detection/recognition. See 2.1, 2.3, 2.6, 2.15 and the later sections on digital-media parameters.

### 2.17 Statements That Should Not Be Memorized Incorrectly

1. **Page/deck numbers and recordings do not identify a teaching session one to one.** S01 and S02 are slide-deck identifiers; the 10 September recording already discusses S02. These notes are organized by topic/deck, so the identifiers should not automatically be treated as particular Lecture dates in the timetable.
2. **Programming-paradigm discussion contains ASR errors and spoken simplifications.** One transcript passage labels C as object-oriented, immediately followed by discussion distinguishing C++/Java from procedural languages. Use the established concepts: C is commonly procedural; C++/Java commonly support object-based modeling; Python and other languages can support several paradigms. Functional programming does not mean that AI automatically implements everything for the user.
3. **Facial distances are not strictly invariant.** Relationships between facial features illustrate feature extraction. Distances in an image can change and do not form an infallible identity code.
4. **The physical explanation of binary computing is simplified.** The recording describes digital circuits as open/closed or 0/1. More precisely, distinguishable physical states represent logical values. A circuit does not have only two mathematical voltage values, and binary computing does not imply that no other computing system can exist. This historical aside should not replace the course's main discussion of data representation.
5. **Context and priors can introduce bias.** The masked-passenger photograph, advertisement, face–vase figure and Dalmatian illustrate checking interpretations against evidence. They do not establish that possessing prior knowledge necessarily reveals the truth.
6. **Old hardware and predictions about new devices provide background.** A sample configuration is not an upper limit for every machine of its period. A trend toward mobile devices does not imply that all PCs have already been replaced.
7. **Some long recording paragraphs lack finer-grained timestamps.** Use the existing paragraph-start time to locate a passage; do not infer exact timings for the lecturer's words from the total recording duration. These notes retain verifiable paragraph timings and explicitly mark explanatory extensions as explanatory supplements.
## 3. Application Examples: Turning Sound, Images and Video into Information That Can Be Processed, Retrieved and Used for Decisions

This chapter covers all 63 PDF pages of S03, Example Applications, and incorporates explanations from the final recording segment on September 10 and the September 17 classes. Slide references use the actual PDF page numbers; recording timestamps are relative to the start of each recording segment. The slides provide applications and methods. The answer templates below are study examples written from those materials, not questions announced by the teacher. Formulas or implementation explanations marked “Interpretive supplement” explain mechanisms and should not be mistaken for details that the slides explicitly require students to memorize.

### 3.1 The Common Method in This Chapter: Represent the Data, Then Design the Processing Pipeline

Sources: [S03 PDF p.1–2, 21–22, 55–63]; classroom supplements: 2026-09-10 21:10 segment 00:00:49–00:01:54; 2026-09-17 20:05 segment 00:27:53–00:41:14 (the system-level summary at the end of this long transcript segment), 00:58:55–end.

Every example can be understood through the same system questions: **What data comes in → what problem or useful pattern does it contain → what representation, features or model are used → how is it processed or compared → what comes out → under what conditions can it fail?** For example, microphone waveforms can be used to remove noise, produce text, identify a song or generate a compressed bitstream. Camera images can be enhanced, stabilized, used to identify people, used to count line crossings or searched for vehicles. The same input can support different tasks, and those tasks require different pipelines.

After the gait example, the teacher specifically emphasized understanding the methodology and system data flow rather than implementing every image-segmentation, neural-network or signal-processing algorithm in this course. In revision, you should be able to explain what each module solves, what input it needs and what it passes to the next module. Knowing an algorithm's name without being able to describe its input and output is not yet understanding the application.

**Answer template:** “When designing a multimedia application, first identify the task and media types, establish a representation that a computer can process, and then perform the necessary preprocessing, feature extraction and model matching to produce the required output. The system must account for sensors, noise, temporal and spatial resolution, and human perceptual limitations. Incorrect inputs or representations can make later algorithms produce incorrect results.”

### 3.2 Classroom Supplement: How Sound, Images, Color, Transparency and Video Are Stored in a Computer

Sources: [S03 PDF p.9, 20, 22–24] provides the application context; the specific representations and calculations in this section mainly come from the 2026-09-17 19:01 segment 00:01:11–00:20:39 and the 20:05 segment 00:00:20–00:11:37. The numerical examples below have been checked mathematically; incorrectly recognized numbers in the transcript are not reproduced.

**Sound is one-dimensional data that varies with time.** A microphone converts sound-pressure variations into an electrical signal, and A/D conversion turns it into a sequence of numerical samples. This can be written as `x[0], x[1], …`. With a fixed sampling interval, the sample index and sampling rate determine time, so a separate timestamp need not be stored for every sample. The teacher first used a two-column table of temperatures measured at 17:00, 18:00 and 19:00 as an analogy, then replaced temperature with sound pressure/amplitude. Computers process measured values; they do not inherently know whether those values mean “cold,” “hot” or a particular emotion. Rules and models establish that meaning.

**An image is a two-dimensional array of pixels.** With `W` pixels horizontally and `H` vertically, it contains `W×H` pixels. Pixel means picture element: each pixel stores brightness or color at a location. Spatial resolution determines how densely space is sampled; bit depth determines how many values can be distinguished at each location. Increasing bit depth does not directly increase the pixel count, and increasing the pixel count does not guarantee better optical sharpness or lower noise.

**Grayscale and RGB.** A `b`-bit grayscale pixel has `2^b` encodable levels: 1 bit gives 2 levels, and 8 bits gives 256. An 8-bit grayscale representation usually uses 0 for black and 255 for white. An RGB color pixel stores red, green and blue channels separately. At 8 bits per channel, each pixel uses 24 bits and has `256³=16,777,216` possible encoded combinations. In `#RRGGBB`, each pair of hexadecimal characters represents a channel value from 0 to 255; for example, `#FF0000` is pure red.

**Shape and transparency.** The stored canvas can remain rectangular while an additional mask identifies foreground pixels. A binary mask can use 0/1, whereas continuous alpha can represent different transparency levels. Adding an 8-bit alpha channel to 8-bit-per-channel RGB produces the common 32-bit RGBA representation. **Correction: alpha represents coverage/opacity, not window stacking order or z-order. Not every image needs alpha, and not every color image uses 32 bits.** The teacher discussed these concepts together through examples of multiple windows and irregular shapes; distinguish them in an answer.

**Raw-data-size formulas.** Ignoring headers, compression, row padding and additional metadata:

- Static-image bits: `W×H×bits_per_pixel`; divide by 8 for bytes.
- Raw-video bits per second: `W×H×bits_per_pixel×FPS`; multiply by duration for the total.
- Raw PCM audio bits per second: `sampling_rate×bits_per_sample×channels`.

A `4×4` image with 32 bits per pixel uses `16×32=512 bit=64 byte`. Each pixel uses `32 bit=4 byte`; the whole image must not be mistaken for 4 bytes. One Full HD `1920×1080` RGBA frame uses `8,294,400 byte≈8.29 MB≈7.91 MiB`. At 30 FPS, raw video needs approximately `248.832 MB/s`, or `1.990656 Gbit/s`. This explains why video systems need compression, appropriate coding and storage management.

**Video is a sequence of images organized in time.** FPS means frames per second. The 24, 25 and 30 FPS values are classroom examples, not mandatory settings for every video. Spatial resolution, bit depth, frame rate and compressed bitrate describe different dimensions. The class discussed format names including HD `1280×720`, Full HD `1920×1080` and 4K. The “K” in 4K approximately refers to four thousand horizontal pixels; consumer UHD is commonly `3840×2160`, but the specific standard should follow the question. **Correction: 1280×720 is a common 720p HD format and should not be described as the standard DVD resolution.**

**Answer template:** “An image can be regarded as a pixel matrix with H rows and W columns. RGB stores color at each location, and alpha can additionally represent transparency. Uncompressed data size equals the number of pixels times bits per pixel; video additionally multiplies this by frame rate and duration. Resolution, bit depth and frame rate respectively control spatial, numerical and temporal sampling precision and cannot substitute for one another.”

### 3.3 Active Noise-Cancelling Headphones, In-Car Cancellation and Multiple Microphones: Noise Processing at Different Locations

Sources: [S03 PDF p.3–7]; classroom: 2026-09-10 21:10 segment 00:01:54–00:19:58 (the final long paragraph also covers multiple microphones, EQ and ASR); recap in the 2026-09-17 19:01 segment 00:37:30–end.

**Active noise cancellation, ANC, in headphones.** The inputs are microphone measurements of ambient noise and the music originally intended for playback; the output sent to the ears is music plus “anti-noise.” Sound consists of waves that can superpose. If the anti-noise arriving at the ear has approximately the same amplitude as the original noise but the opposite phase, their pressure variations cancel. Ideally, `n(t)+[-n(t)]≈0`, leaving the desired music `s(t)` as the main audible signal. The slide diagram shows ambient noise → microphone → noise-cancelling circuitry that inverts the waveform → headphone speaker producing a compensating sound → cancellation with the original noise near the ear.

**Why put a microphone on a headphone?** The microphone measures the environmental sound to be cancelled, while the speaker generates the compensating sound: they serve input and output roles respectively. Interpretive supplement: practical systems must estimate acoustic paths and processing delay. Simply multiplying an audio recording by −1 does not guarantee cancellation of every sound at every location. Persistent, more predictable low-frequency noise is generally better suited to ANC; rapidly varying and high-frequency noise is harder to compensate precisely. Passive isolation physically obstructs sound, while ANC produces an additional sound wave.

**Noise cancellation in cars/buses.** The slide diagram includes engine noise, microphones at several cabin locations, an ECU, an audio system/woofer, and engine-speed information. Cabin noise is measured, a processing system generates anti-noise, and the audio system plays it to reduce engine sound in target regions. The teacher used cars and double-decker buses to explain that speakers can participate in noise control as well as announcements. This illustrates the principle; it does not establish that all buses or every car model is equipped with such a system.

**Dual-microphone call-noise reduction.** A main microphone near the mouth captures relatively strong speech plus noise; another microphone captures more ambient noise as a reference. The processor estimates and suppresses the noise in the main channel, producing clearer speech for the remote listener or ASR. The slide's `Subtract → Amplify` sequence is a conceptual illustration. Interpretive supplement: noise recorded at different positions has timing and amplitude differences, so practical systems generally require matching/adaptive processing. Blindly subtracting two channels that both contain speech can also damage the speech.

**Why use three, four or even more microphones?** Different phone-holding positions, speakerphone meetings and speaking directions change the pickup conditions. Multiple channels provide directional and spatial information that can improve far-field pickup, noise separation and coverage. Microphone directionality describes the response to sound arriving from different directions; different uses need different arrangements. The historical article on S03 p.7 also lists trade-offs involving always-on wake-word power, size, acoustic overload capability and distant-voice pickup. Its old iPhone and Echo microphone counts are examples from that period, not specifications of current devices.

**Answer template:** “ANC headphones use a microphone to obtain ambient noise, estimate the anti-phase compensation needed at the ear, and play it through a speaker so that pressure variations cancel at the target location. Phone-call noise reduction often uses a reference microphone to estimate noise in the main channel and clean the digital speech. The former improves the listener's acoustic field; the latter improves audio being transmitted or recognized. Multiple microphones can also exploit directional and positional differences to improve pickup.”

### 3.4 Digital Audio Equalizer, EQ

Source: [S03 PDF p.8]; classroom: 2026-09-10 21:10 segment 00:12:21–00:19:58 (the EQ explanation within this long transcript paragraph), and the recap in the 2026-09-17 19:01 segment 00:37:30–end.

An EQ takes audio as input and produces audio with altered relative strengths of frequency components. It divides the audible frequency range into bands, sets gain or attenuation independently for each band, and combines the result. The slides give an approximate 20 Hz–20 kHz range, more than 200 bands for some high-end systems, and example adjustment ranges from ±6 dB to ±24 dB. These band counts and ranges are product examples, not fixed parts of the definition of EQ.

Reducing low frequencies and boosting high frequencies, or doing the reverse, changes timbre. Bass Booster emphasizes bass; Classical, Jazz, R&B and Rock presets are predefined sets of band gains. They do not automatically turn a song into another musical genre; they alter the spectral balance heard by the listener. An ordinary volume control approximately changes overall amplitude together, while EQ can modify separate frequency bands independently.

**Limitations/common mistakes.** EQ cannot unconditionally distinguish speech from noise in the same frequency band. If both noise and desired content occupy a band, attenuating it also removes desired content. Large boosts may increase noise, clipping or distortion (interpretive supplement). Do not confuse EQ with ANC's waveform cancellation in the previous section. The teacher used selective retention/suppression across frequency as an analogy, but the two mechanisms are not identical.

**Answer template:** “A digital equalizer divides audio into frequency bands and applies independent gain or attenuation to control their relative strengths, such as bass and treble. A preset is a set of band-gain settings. EQ changes the spectrum and timbre, whereas ordinary volume control mainly adjusts the overall level.”

### 3.5 Speech-to-Text / Automatic Speech Recognition, ASR

Source: [S03 PDF p.9]; classroom: 2026-09-10 21:10 segment 00:12:21–00:25:01 (including traditional ASR and the transition to Shazam); recap in the 2026-09-17 19:01 segment 00:37:30–end.

**Input, output and purpose.** The input is a human speech waveform, and the output is text consisting of words/sentences. The system must infer linguistic units from continuous sound affected by noise, accent and speaking rate. This differs from speaker recognition, which identifies who is speaking, and from translation, which converts text or meaning into another language.

**The traditional pipeline in the slides:**

1. Microphone pickup and A/D: turn continuous sound into digital audio.
2. Noise reduction and normalization: reduce environmental interference and normalize level/feature scale so that recording-level differences have less influence on matching.
3. Short-time segmentation: divide long speech into short windows suitable for local analysis. The slide mentions hundredths/thousandths of a second; the main point is short-time processing, not cutting every letter into an equal-duration piece.
4. Feature/phoneme matching: compare acoustic patterns in short segments against known phonemes. Approximately 40 phonemes for English is the slide's rough estimate; the actual count varies with accent and phonological classification.
5. Statistical language decoding: combine phonemes and use a statistical model to infer the most likely words and sentences. When sounds are similar, context can help determine the more plausible word sequence.

**Classroom supplement.** The teacher used older systems that required reading a long passage so the computer could adapt to a speaker's voice and accent to explain training. The acoustic pattern of “apple” illustrated the mapping from waveform/spectrum to symbols. The transcript renders this as “the spectrum of each letter”; follow the slides and correct it to **acoustic units/phonemes, not pronouncing letters one by one**. Modern systems can learn more complex features, but recording quality still affects the result. Scattered spoken accuracy figures do not establish one accuracy rate for all systems.

**Limitations/common mistakes.** Homophones, connected speech, accents, background sounds and out-of-vocabulary content can create ambiguity. Cleaning a signal does not mean understanding its semantics, and converting sound to text does not guarantee that the sentence is factually correct. With unclear audio, even a powerful downstream model may suffer from “garbage in, garbage out.”

**Answer template:** “Traditional speech-to-text first digitizes sound, reduces noise and normalizes the signal, then extracts short-time acoustic patterns and identifies phonemes. Statistical acoustic/language models decode the phoneme sequence into the most likely words and sentences. Acoustic matching addresses what the sound resembles, while the language model helps determine which word sequences are plausible.”

### 3.6 Shazam: Audio Fingerprints, Spectral Peaks and Time Alignment

Sources: [S03 PDF p.10–14], including the constellation maps and matching-peak histograms on p.11–14; classroom: 2026-09-10 21:10 segment 00:19:58–00:29:51 (Shazam is introduced in the latter part of the long opening paragraph); 2026-09-17 19:01 segment 00:00:00–00:01:11.

**Task.** A short recording of music is the input; candidate songs, associated titles/artists and match scores are the output. The slide uses a roughly 10-second sample as an example. The idea does not require uploading the entire song, and it does not mean transcribing lyrics and then searching the lyrics.

**Key representation.** A spectrogram has time on the horizontal axis, frequency on the vertical axis and intensity indicating energy at each time-frequency location. Prominent local peaks are selected to form a sparse constellation map. An audio fingerprint is a compact representation of stable, discriminative acoustic structure, used for comparison with songs already in a database.

**Offline indexing → online query:**

1. Compute fingerprints for each catalog song, store associations with the song ID and within-song time, and build an index.
2. Apply the same processing to the query recording to obtain its short-segment peaks/fingerprint.
3. Because the query may begin in the middle of a song, its time origin is unknown; matching must allow a time shift.
4. The diagrams on p.12–14 move the red query constellation across the blue database constellation and count matching peaks at each offset.
5. At the correct position, many peaks align simultaneously, producing a prominent peak in the matching histogram. This supports the song identity and segment position. Random noise is less likely to create many consistent matches at one common offset.

The slides describe robustness to noise, room reverberation, equalization and overlapping sounds. This means tolerance of some interference, not guaranteed recognition under any distortion. Interpretive supplement: sparse peaks/relative structure are generally more stable than comparing raw waveforms sample by sample, and a database index reduces the cost of fully comparing every catalog song. The slides illustrate peak matching under temporal translation; they do not require memorizing a precise hash format without supporting material.

**The teacher's emphasis: index before retrieval.** A library first creates records, identifiers and location associations for newly arrived books so readers can find them efficiently by keyword or number. Similarly, a song's searchable representation must be added to the system before it becomes a candidate. Collecting recordings without a fingerprint index does not by itself provide efficient content retrieval. ISBN was the teacher's analogy; actual retrieval features need not be globally unique identifiers like ISBNs and can instead be compared by similarity.

**Answer template:** “Shazam extracts prominent peaks from a short music sample's time-frequency spectrum to form a fingerprint and compares it with a pre-indexed music catalog. Since the sample can begin anywhere in a song, matching seeks a consistent time offset. Many aligned peaks at one offset support the correct candidate song. Stable sparse features and indexing permit efficient retrieval under some noise and reverberation.”

### 3.7 One Route to Audio Compression: An LPC Vocoder Transmits Parameters of a Speech-Production Model

Sources: [S03 PDF p.15–16], particularly the physiological speech-production and electronic vocoder block diagrams on p.16; classroom: 2026-09-17 19:01 segment 00:20:39–00:32:04.

**Why is compression possible?** Raw waveforms contain many samples. If a short speech segment can be approximated by a simplified generation model, its parameters can be transmitted and the receiver can reconstruct it using the same model instead of receiving every waveform sample. The teacher compared this with “sending a score/standard notes and coefficients rather than an entire recording” and stressed a shared representation convention. This analogy explains compression; it does not mean all speech is literally encoded as seven musical notes.

**A source–filter view of human speech.** Airflow provides energy. Voiced sounds contain excitation from periodic vocal-fold vibration; unvoiced sounds can be approximated using noise-like excitation. The mouth, nasal cavity and articulators form vocal-tract resonances that shape the speech spectral envelope. The slide's physiological description is simplified. A more accurate statement is that airflow drives vocal-fold and vocal-tract processes; do not use “the epiglottis directly produces all sound” as a standard definition.

**LPC, linear predictive coding, vocoder.** Vocoder comes from voice + coder. For each short speech segment, the encoder estimates: (1) coefficients describing vocal-tract filtering; (2) energy/gain; (3) pitch; and (4) voiced/unvoiced state. After these parameters are transmitted, the decoder chooses periodic/tone excitation or noise excitation according to the state, sets pitch and energy, and passes it through a variable vocal-tract filter to synthesize speech. The p.16 diagram includes voiced/unvoiced decision, tone/noise generator, fundamental frequency, filter coefficients and variable filter.

Interpretive supplement: the “prediction” in LPC can be understood as approximating a sample by a weighted combination of preceding samples; the estimated coefficients can also represent a simplified vocal-tract filter model. The exam focus is the relationship between model and parameters. LPC should not simply be defined as “removing frequencies that cannot be heard”; that belongs to the psychoacoustic route in the next section.

**Uses, advantages and limitations.** The slides relate GSM speech coding to the LPC framework. The main advantage is that speech fitting this model can be represented using relatively few parameters. It assumes a speech-generation model, so it may not suit complex music or arbitrary environmental sounds; synthesis quality depends on model and parameter accuracy. In response to p.16's “What is the other use of this vocoder?”, speech synthesis or altering pitch/vocal-tract parameters to produce voice effects can be explained from the mechanism. This is an interpretive supplement derived from the diagram; the slide provides no single official answer.

**Answer template:** “An LPC vocoder approximates speech as the output of an excitation source passed through a vocal-tract filter. The encoder estimates energy, pitch, voiced/unvoiced state and filter coefficients and transmits these parameters. The decoder generates the corresponding excitation and filters it to reconstruct speech. It reduces data by exploiting speech-production structure, making it suitable for speech without assuming that the same model fits all music.”

### 3.8 Another Route: MPEG Audio Exploits Hearing Limitations and Masking

Sources: [S03 PDF p.17–20], including the ear/frequency-distribution diagrams on p.18 and hearing-threshold/masking curves on p.19; classroom: 2026-09-17 19:01 segment 00:32:04–00:52:30.

**Why does hearing matter to coding?** Environmental pressure changes vibrate the eardrum. Middle-ear mechanical structures transmit these changes to the cochlea, where fluid and sensory structures turn mechanical activity into neural signals. Different cochlear positions respond to different frequencies; the classroom video associates the base with higher frequencies and the apex with lower frequencies. Hearing is not equally sensitive to every frequency and intensity. The slide's statement that the ear “senses the spectrogram” is an intuitive analogy for frequency analysis, not a claim that the ear stores a digital spectrogram image.

**Audible range and threshold.** The slides use approximately 20 Hz–20 kHz as a common range for young human listeners; actual hearing varies by person and conditions. Even within this range, a sound must reach the threshold for its frequency to be audible. The p.19 threshold curve shows that audibility depends on both frequency and intensity, not simply the presence of a frequency.

**Frequency masking / simultaneous masking.** A strong sound in one band can make a weaker sound inaudible even though that weaker sound would be audible alone. The strong sound raises the effective threshold in nearby frequencies, placing the weak signal below the masking threshold. A loud instrument masking weaker nearby-frequency components at the same time is an example. Do not write that any loud sound removes all other frequencies.

**Temporal masking.** For a short time after a strong sound stops, certain weaker sounds remain difficult to hear. The slide emphasizes post-masking and supplies no universally applicable duration in seconds. The recording uses a gunshot as an intuitive example; do not equate prolonged hearing impairment after an intense sound with the precise short-time psychoacoustic masking mechanism used in audio coding.

**The lossy idea in MPEG Audio.** A psychoacoustic model estimates which components or quantization noise will be less noticeable under current listening conditions. Fewer bits are allocated to such parts, while more perceptible content receives priority. The original waveform generally cannot be recovered exactly sample by sample, so this is lossy compression. The goal is perceived quality at a given bitrate. Interpretive supplement: practical coding can vary quantization precision by band rather than completely deleting every masked note. Psychoacoustic decisions are primarily coding functions; do not claim that all microphone hardware automatically refuses to capture masked sounds.

**The three Layers and the slide's MP3 pipeline.** Layer I is the basic scheme (with DCC digital tapes as the slide example); Layer II adds more advanced bit allocation; Layer III adds hybrid filters. MP3 means MPEG Audio Layer III. **Layers I/II/III are not MPEG versions MPEG-1/2/3, and an MP3 does not have to store three complete audio tracks successively.**

The p.20 summary is: process groups of 1152 samples → divide into 32 frequency bands → estimate masking with a psychoacoustic model → allocate representational precision/coding resources → use variable-length coding to exploit statistical redundancy. `1152/44100≈0.0261 s`, so “about 26 ms” assumes a 44.1 kHz sampling rate; it is not fixed for every sampling rate. Assigning shorter codes to more frequent symbols explains intuitively why variable-length coding can save data (interpretive supplement).

**Comparison and answer template:** “LPC mainly exploits a speech-production model, replacing many waveform samples with excitation and vocal-tract parameters. MPEG Audio mainly exploits a human-perception model, reducing information that is difficult to notice because of hearing thresholds and frequency/temporal masking, then exploiting coding redundancy to reduce bitrate. The two obtain compression opportunities from how sound is produced and what sound needs to be preserved respectively.”

### 3.9 Image Enhancement: HDR, Night Mode, Multi-Frame Fusion and Super-Resolution

Sources: [S03 PDF p.22–24]; classroom: 2026-09-17 20:05 segment 00:11:37–00:24:44. The longer HDR and low-resolution-fusion explanations come from the recording; slides p.23 and p.24 specifically show Night Mode and Deep Fusion.

**What does HDR, high dynamic range, address?** If a scene contains very bright and dark regions, the sensor's single-exposure recording range can be insufficient. Exposure for highlights may leave shadows without detail; exposure for shadows may saturate highlights. Multi-exposure HDR captures complementary images at different settings, aligns them and combines short-exposure highlight information with long-exposure shadow information to represent a fuller brightness range, then maps it to a displayable range. The final tone/display-mapping point is an interpretive supplement. “Dynamic” here concerns the brightness range, not a requirement that objects move.

**Night Mode.** In low light, a short exposure can reduce motion trails but captures less light and may be noisy. A long exposure collects more light but is more vulnerable to camera/subject movement. The p.23 method captures multiple frames at different shutter speeds and intelligently combines them to balance shadow detail and motion blur. Its input is a set of low-light photographs; its output is an enhanced image balancing detail and noise. It is not simply multiplying the brightness of the entire image, which would also amplify noise and cannot recover already lost detail.

**The historical Deep Fusion example.** Page 24 cites the 2019 iPhone 11 Pro/Pro Max example: nine images in total, consisting of four short exposures, one long exposure and four additional images, blended to optimize detail and low noise. The important concept is complementary information across frames. Nine is the number in that product example, not a fixed count for every multi-frame algorithm or something that must be extrapolated to other phones.

**Classroom supplement: multi-frame super-resolution.** When spatial sampling is too sparse, tiny details are not adequately represented in one low-resolution image. The teacher used 2×2 versus 4×4 grids and distant satellite targets to illustrate this. Different viewpoints or small shifts between frames provide complementary samples, which can be registered and reconstructed into a finer representation. Both this and HDR combine multiple observations to overcome limits of one measurement, but HDR primarily improves brightness range while super-resolution primarily improves spatial detail.

**Limitations/common mistakes.** Frames must correspond to the same scene structure. Motion, occlusion and registration errors can create ghosting. Merely averaging cannot guarantee true recovery of information missing or saturated in every frame. Pixel count, HDR, low noise and sharpness are different measures. “Intelligent fusion” does not mean unconditional creation of real detail.

**Answer template:** “Multi-frame enhancement gathers complementary observations, aligns them and selects or fuses useful information. HDR combines exposures to preserve highlight and shadow detail; Night Mode balances light collection and motion blur; multi-frame super-resolution uses different sampling positions to add spatial detail. Scene motion and incorrect registration can create artifacts in all of these approaches.”

### 3.10 Retinex: An Example of Brightness/Color Enhancement

Source: [S03 PDF p.25]. The page only gives the name Retinex and a before/after port-image comparison. The explanation below is an interpretive supplement, not an attempt to turn one slide image into algorithmic details explicitly taught by the teacher.

Retinex combines the concepts retina and cortex in its name. It refers to a family of enhancement ideas that separate illumination effects from object reflectance to improve visibility under uneven lighting. The input is an image that is dark, low in contrast or unevenly illuminated; the output makes local detail/contrast and color appearance easier to observe. In the slide, the original port image is dull, while structures are clearer after enhancement.

**Mechanism as an interpretive supplement:** approximate observed brightness by `I(x,y)=R(x,y)L(x,y)`, where `R` is reflectance and `L` illumination. Estimate slowly varying illumination and reduce its influence to emphasize reflectance structure. Logarithms turn the product into `log I=log R+log L`, but the slide does not require a particular filter or multi-scale formula.

**Limitations/common mistakes.** Enhancement does not guarantee absolutely true colors or recovery of detail absent from the original observation. Excessive processing can amplify shadow noise or produce halos and unnatural appearance. Unlike multi-exposure HDR, Retinex can process illumination/reflectance in one image; it does not necessarily require nine photographs.

**Answer template:** “Retinex is an image-enhancement approach that uses illumination–reflectance separation to reduce the influence of uneven lighting and improve the visibility of shadows, local contrast and color. It improves presentation but remains limited by the information and noise in the original image.”

### 3.11 Video Stabilization: Estimate Camera Motion, Then Compensate the Frames

Source: [S03 PDF p.26]; classroom: 2026-09-17 20:05 segment 00:24:44–00:27:53, plus the summary in the long 00:27:53–00:41:14 segment.

**Input and output.** The input is video shaken by handheld operation, drones or moving ships; the output has smoother changes of viewpoint between frames. The main target is unwanted camera movement, not making every person or vehicle in the scene stop moving.

**Classroom pipeline.** Find corners or other trackable feature points in successive frames. Compare positions of corresponding background features to estimate overall camera movement upward/downward/left/right and so on. Apply opposite compensation to make the background more stable over time. Interpretive supplement: one may first smooth the estimated camera path and warp frames onto the smoothed path, preserving intentional smooth panning. Electronic stabilization often requires cropping at the image edges.

**Limitations/common mistakes.** If all tracked features belong to independently moving foreground objects, their motion may be mistaken for camera movement. Occlusion, little texture, large motion and perspective differences can destabilize the estimate. Inter-frame stabilization differs from intra-frame deblurring: positioning each frame steadily does not guarantee removal of long-exposure trails.

**Answer template:** “Video stabilization tracks features across successive frames, estimates global motion caused by the camera and geometrically compensates the frames to obtain a smoother trajectory. It mainly corrects camera shake between frames; motion deblurring instead addresses trails accumulated during the exposure of an individual frame.”

### 3.12 Motion Blur and Deblurring

Sources: [S03 PDF p.27–30]; classroom: 2026-09-17 20:05 segment 00:27:53–00:41:14 (one continuous long transcript paragraph).

**Why does blur occur?** An image sensor accumulates light over an exposure interval, rather than taking a measurement of zero duration. If the camera or object moves appreciably during that interval, the same structure contributes at multiple positions, creating a trail. Page 27 separately illustrates global camera motion and rapid foreground motion. The teacher used table tennis, sports and a moving minibus as examples. A shorter exposure helps freeze motion but collects less light, requiring consideration of lighting, aperture and sensitivity settings.

**Three capture parameters.** The teacher mentioned exposure time, aperture and ISO. Exposure time controls the accumulation interval; aperture controls incoming light and affects depth of field; ISO is an imaging gain/sensitivity setting. **Correction: increasing ISO in a digital camera generally does not cause the sensor itself to capture more photons.** Frame rate and exposure time are also different. High-speed video often needs both an adequate frame rate and short exposures; a stated FPS alone does not prove the absence of blur.

**Why is one global motion not always sufficient?** Page 28 explicitly states that different portions of one object may have different velocities relative to the camera. Foreground and background can also move differently, making blur spatially non-uniform. Image displacement can differ between a minibus's upper section, body and lower section. A single translation/single blur kernel may therefore not explain the entire image.

**Be able to explain every module in the p.29 diagram:**

1. **Blurred video frames:** multiple blurred frames provide temporal evidence of motion.
2. **Foreground extraction → foreground mask:** isolate the moving foreground to be processed and create a region mask, reducing background interference in estimation and recovery.
3. **Segmentation & corner detection → extracted corners:** use region information to segment and find trackable corners/features within the foreground.
4. **Feature tracking with HBMA → tracked corners:** the module labelled HBMA establishes correspondence for the same features across frames. The slides do not expand the abbreviation, so no expansion is invented here.
5. **Motion estimation:** use feature trajectories to estimate object motion/velocity and possible local differences.
6. **Calculated blur kernel:** use motion during exposure to estimate how pixels have been spread out.
7. **Deblurring → deblurred result:** recover a sharper foreground using the blur model. Page 30 shows improvements in local details such as vehicle markings and route text.

Interpretive supplement: the common model `blurred ≈ sharp * kernel + noise` explains estimating a kernel before recovery. Inversion is limited by noise and information loss, so perfect recovery of a number plate or text cannot be guaranteed. The asterisk here means convolution, not pixelwise multiplication.

**Answer template:** “Motion blur is caused by camera or subject movement during exposure and accumulates different instantaneous positions within one frame. Deblurring may isolate the moving foreground, track corners to estimate motion, infer a blur kernel and recover the image using that kernel. Different objects, or different parts of one object, can have different relative velocities, so one global motion model is not always sufficient.”

### 3.13 Face Detection, Recognition and Features: Distinguish the Tasks First

Sources: [S03 PDF p.31, 35–49]; classroom: 2026-09-17 20:05 segment 00:41:14–00:47:30.

**Face detection** takes a whole image and outputs the presence and locations/regions of faces; it asks whether a face is present and where. **Face recognition** takes a face or its features and outputs identity matching/similarity; it asks who the person is or whether two faces belong to the same person. **Tracking** maintains temporal associations for the same target across frames. **3D reconstruction** infers three-dimensional geometry and appearance from observed images. A system may connect these modules, but their outputs differ.

**Early hand-designed features.** First locate eyes, nose, mouth and other components, then form a feature vector using positions, inter-eye distance, and eye-to-nose/mouth distances. Similar feature vectors support a possible same-person match. However, expressions, pose, projection, occlusion and similar appearance can change or confuse these values. The same person's mouth geometry can differ between smiling and anger; twins also illustrate that similar features need not be unique. Finding two eyes is not equivalent to proving an identity.

**Answer template:** “Detection localizes faces, recognition compares identities, tracking maintains temporal associations, and reconstruction creates a 3D representation. Early hand-designed recognition features describe facial geometry or texture, but pose, expression and occlusion affect them, motivating more robust models and matching.”

### 3.14 Haar Features, AdaBoost and Scanning: The Viola–Jones Idea

Source: [S03 PDF p.31], including rectangular-feature illustrations and the diagram rejecting candidate windows stage by stage; classroom: 2026-09-17 20:05 segment 00:41:14–00:46:26.

**What is a Haar-like feature?** Differences between sums of intensities in neighboring light/dark rectangles describe local structures. For example, the eye region is often darker than the cheek below it, while the bridge of the nose differs in brightness from adjacent regions. The input is a candidate image window, and the output is a set of numerical features. One feature provides only weak evidence of a face. The slide states that these features can be computed efficiently. Using an integral image to calculate rectangular sums rapidly is common implementation background (interpretive supplement), but the slide does not derive its formula.

**The role of AdaBoost.** It selects and combines many weak features/classifiers to form a stronger classifier, rather than assuming one rectangular template can reliably judge every face. The lower-right p.31 diagram also shows successive tests: a subwindow is rejected as soon as a stage labels it non-face, and only windows passing all stages are labelled face. This cascade prevents most background windows from receiving all the expensive later processing. Combining weak learners and arranging a cascade are related but distinct structures; explain them separately.

**How are faces found throughout an image?** Scan candidate windows at different positions and scales, or rescale the image, to accommodate faces of different apparent sizes. Extract features and classify every candidate. Scanning addresses unknown location, scale search addresses unknown size, and the classifier judges whether a window resembles a face.

**Limitations/common mistakes.** Lighting, occlusion, strong profile views and face-like textures can produce false detections or misses. Haar is a feature representation; AdaBoost is a learning/combination method; sliding windows search candidate locations. Their names are not interchangeable. This page presents a classical method, not a claim that every modern face detector still uses it.

**Answer template:** “A Viola–Jones-style detector scans windows over positions and scales, computes efficient Haar rectangular contrast features, uses AdaBoost to combine weak classifiers, and rejects most non-face windows early through a cascade. It outputs face locations rather than directly identifying people.”

### 3.15 Head Models, Tracking and Tripwire People Counting

Sources: [S03 PDF p.32–34], particularly the q₁–q₈ control points and left-to-right viewing contours on p.33, and the line-crossing screenshots on p.34; classroom: 2026-09-17 20:05 segment 00:48:11–00:50:56.

**Model-based head tracking.** A continuous video is the input; head locations, contours and trajectories are the output. A deformable head contour is defined by control points and fitted to image edges. Changing q₁–q₈ yields different head shapes and side-view appearances from left to right. The model and location are updated in consecutive frames to maintain association with the same head.

**Tripwire counting.** Draw a virtual line at an entrance/exit. When a tracked head trajectory crosses it, record one passage; opposite directions can support separate entering/leaving counts. Page 34 also captures head images at crossing time. Unlike counting detected heads independently in every frame, tracking prevents a person visible in ten frames from being counted ten times. Direction handling and duplicate suppression are interpretive implementation details, but they explain why a tracker is needed.

**Limitations of model-based methods.** Hats, occlusion, crowded scenes and head-like bags create ambiguity. The teacher used face graphics on clothes and a backpack held in front as examples of why a head-like appearance does not prove a real person is present. Tracks may also exchange identities after mutual occlusion. A counting system must consider detection, temporal association and crossing events together.

**Answer template:** “Head tracking fits a deformable shape model to heads in video and maintains trajectories across frames. Tripwire counting combines a virtual line with those trajectories and triggers a count when the same target crosses it. Head-like non-head objects, occlusion and broken tracks can cause false detections, missed counts or duplicates.”

### 3.16 3D Face Reconstruction: Why Transform a Profile into a Frontal Face?

Sources: [S03 PDF p.35–37, 43–46]; related classroom discussion: 2026-09-17 20:05 segment 00:46:26–00:52:22 on model-based methods.

**Problem and objective.** The demonstration software on p.35 compares frontal faces successfully, while the profile-to-frontal comparison on p.36 fails. Different viewpoints change a face's 2D projection, visible regions and scale, while some features become self-occluded. This describes a pose limitation of the demonstrated system; **it does not mean every face-recognition algorithm in every period only supports frontal faces.**

**Complete input and output.** Given a non-frontal face image, estimate the person's 3D facial shape, camera pose and surface texture, then render a standardized frontal image. Feed that frontal image to a recognition system that favors frontal faces and compare it with the registered gallery. Reconstruction outputs geometry/texture or a normalized image; identity matching remains a subsequent recognition task.

**Remember the four-stage p.37 pipeline:** `Facial feature detection → 3D modeling → Pose estimation → Texture map rebuilding`. These stages respectively ask: Where are the key facial features in the image? What is the person's 3D facial shape? What is the face/camera orientation? How can the observed appearance be mapped onto the surface and rendered from other views? The following four sections explain each submodule.

**Answer template:** “A profile differs from a registered frontal image in pose and visible regions. Localize facial features, fit a personalized 3D model, estimate pose, rebuild texture and render a frontal view to reduce pose-related mismatch. This is an input-normalization strategy; it cannot guarantee the true detail of unobserved regions or error-free recognition.”

### 3.17 3D Reconstruction Module One: AAM Facial-Feature Localization and Multiple View Models

Source: [S03 PDF p.38].

An **active appearance model, AAM**, fits deformable facial shape and appearance patterns to an input image, locating detailed landmarks such as eyebrows, eyes, nose, mouth and face contour. Its task is not to output identity first, but to supply reliable 2D feature locations for later 3D fitting.

The slides use three appearance models: frontal, half-profile and profile. Each model is fitted to the input, the residual error—the disagreement between model prediction and observation—is compared, and the model with the smallest residual is adopted. This is necessary because the visible structure differs between frontal and profile views; a model suited only to frontal faces cannot readily explain a complete profile.

**Input → processing → output:** face image → independently adjust the location/shape/appearance of the three AAMs to fit → calculate residuals → select the minimum → output the selected model and landmarks. Interpretive supplement: this compares fitting quality. The lowest residual does not automatically establish the person's identity. Occlusion, extreme pose, blur or inadequate model coverage can make even the best available fit wrong.

**Answer template:** “The feature-detection stage fits frontal, half-profile and profile AAMs separately to the input face, compares their fitting/reconstruction residuals and selects the lowest-error model to locate landmarks. Multiple view models provide suitable structural constraints as visible facial features change with pose, supplying 2D correspondences for personalized 3D modeling.”

### 3.18 3D Reconstruction Module Two: Meshes, Individual Shape Modification and Texture Coordinates

Sources: [S03 PDF p.39–40].

**A 3D mesh represents geometry.** Vertices specify 3D positions, and facets connect neighboring vertices to form a surface. The p.39 example has 6292 vertices and 6152 facets. These describe the selected model's detail, not a fixed number of vertices naturally present in a human face. The frontal/profile models on p.40 show how a base shape can be adjusted to represent different individuals' head contours and facial geometry.

**How is the model personalized?** Eyes, nose, mouth and contour correspondences from the preceding stage constrain a generic 3D face so that its shape better fits the individual. Interpretive supplement: adjust a small set of shape parameters or vertex locations to bring projected model features closer to observed landmarks. The mesh captures protrusions and facial shape, rather than simply pasting a photo onto a flat board.

**A texture map represents surface appearance.** It stores facial colors/details in a 2D image. Texture coordinates, commonly called UV coordinates, determine which position in that image corresponds to each location on the 3D surface. Geometry says where the surface is; texture says what it looks like; texture coordinates connect them. Changing color alone does not alter how far the nose protrudes, and changing the mesh alone does not automatically supply skin, eyebrow and other color details.

**Answer template:** “The modeling stage adjusts a generic facial mesh to the individual using input landmarks. Vertices and facets represent geometry; a 2D texture map represents skin and facial appearance; texture coordinates map its colors onto 3D facets. Together these enable rendering of the person's face from different angles.”

### 3.19 3D Reconstruction Module Three: Pose Estimation

Source: [S03 PDF p.41].

Pose estimation asks how the 3D model must be placed relative to the camera to reproduce the observed 2D feature positions. The inputs are 2D facial landmarks and the corresponding 3D model; the outputs are orientation and transformation parameters that align model and image. The slide first shows key locations on the generic mesh, then overlays it on an actual profile, illustrating the need to rotate and position the model correctly.

**Process as an interpretive supplement:** establish 2D-to-3D feature correspondences → adjust rotation, location and projection scale → minimize disagreement between projected model points and observed points → estimate the input pose. Pose describes the person's current orientation; geometry describes the person's facial shape. Both can alter a 2D contour, but they have different meanings. Turning one's head should not be interpreted as changing the underlying face shape.

**Why is it necessary?** Without knowing whether the input is frontal or profile, texture could be sampled onto the wrong surface regions, and the reconstructed frontal face could be skewed or misaligned. Uncertainty in the camera model and 3D shape also limits pose precision.

**Answer template:** “Pose estimation aligns projections of 3D model landmarks with observed 2D landmarks to estimate the model's rotation and position/scale relative to the camera. It separates individual geometry from current viewing direction and provides the alignment needed for correct texture sampling and standardized frontal rendering.”

### 3.20 3D Reconstruction Module Four: Texture Rebuilding, Filling, Rendering and Recognition

Sources: [S03 PDF p.42–46].

**Read the p.42 diagram module by module.** Texture, texture coordinates and the 3D mesh work together in rendering to produce a facial image. Mapping observed image colors onto the model leaves missing data on the side of a profile facing away from the camera. Fill & Interpolation supplies such regions, and postprocessing reduces discontinuities in seams, color/tone and appearance to produce a more complete result. The slide is a pipeline illustration, not a prescription of one interpolation formula. A particular neural generation technique should not be presented as the original slide content.

**Definitions that can be used directly:** Rendering generates a 2D image from 3D geometry, texture and viewpoint. Filling/interpolation supplies usable values for unobserved or sparsely sampled regions. Postprocessing improves the consistency of reconstructed boundaries, brightness or appearance. Interpolation/model completion is not direct observation, so true moles, scars or fine texture on the hidden side are not guaranteed to be recovered.

**The application chain on p.43–45.** Page 43 shows frontal and other reconstructed views from photographs of different people. Page 44 passes a profile through Face Reconstruction to obtain a frontal face. Page 45 feeds this reconstructed frontal face into the original recognition software, which successfully matches the registered frontal image in the example. Therefore describe “reconstruct, then recognize,” not “reconstruction is automatically identity verification.”

**How to read the p.46 results.** In four examples, similarities between the non-frontal face and the frontal gallery image are `0.7714, 0.3341, 0.1151, 0.0000`; after reconstruction, they are `0.8720, 0.5469, 0.6988, 0.8474`. These are per-example similarity scores from the demonstration system, indicating a closer match after normalization. **They are not general recognition accuracies such as 87.20%, nor performance estimates from a large statistical sample.** Different software may also use different score scales and thresholds.

**Answer template:** “Texture rebuilding maps observed facial colors onto the personalized 3D model, completes unobserved regions and postprocesses appearance before rendering a standardized frontal view. This reduces pose mismatch with the frontal gallery and raises similarity in the examples. Completed regions still rely on model inference, and similarity scores must not be treated as accuracy rates or proof that every profile can be recognized.”

### 3.21 Face-Recognition Limitations, Face ID and the Move from Hand-Designed to Learned Features

Sources: [S03 PDF p.47–49]; classroom: 2026-09-17 20:05 segment 00:50:56–00:55:47.

**Two different glasses examples.** Page 47 describes specially designed spectacle frames that make an automatic face-recognition system miss the wearer or misidentify them as someone else. This illustrates deliberately chosen appearance changes manipulating model features. Page 48 instead describes how ordinary changes such as wearing glasses affect human recognition of unfamiliar faces. One concerns a targeted perturbation of an automatic system, the other a limitation in human unfamiliar-face perception. Do not merge them into “all glasses defeat all recognition systems.”

**The Face ID example on p.49.** The images identify components including a dot projector, infrared camera, flood illuminator, ambient-light/proximity sensors and a front camera. The principle can be understood as actively projecting structured light and observing the face to obtain geometry/depth cues beyond a normal 2D color photograph, then using them in matching. The page illustrates the combination of optical sensors and algorithms in a product; it does not establish all specifications of a generation, its accuracy or absolute spoof resistance. Interpretive supplement: depth can help distinguish a real 3D face from a flat photograph, but actual attack resistance depends on the complete system.

**The teacher's summary of technical development.** One class of approaches relies on hand-designed facial/geometric features. Another fits deformable shapes, appearance models or 3D models, using their constraints to tolerate some expression and pose variation. A third learns features and matching representations from large samples through deep networks. The distinction is how much feature design is specified manually versus learned from data, not that later methods no longer use features. Neural networks still require suitable data, training and evaluation. Approximate classroom percentages do not justify fixed claims that a generation has 40% or 90% accuracy.

**Answer template:** “Face-recognition reliability depends on pose, illumination, occlusion, appearance changes and feature design. Model-based methods use geometric/appearance constraints for stability; learning methods learn stronger features from samples; active depth sensing adds geometry unavailable in an ordinary photograph. Appearance perturbations and unseen conditions can still cause errors, so evaluation must specify the system and conditions.”

### 3.22 Human Gait Recognition and Bag-of-Gait

Sources: [S03 PDF p.50–54]; classroom: 2026-09-17 20:05 segment 00:55:47–00:59:08.

**What is gait, and why can it identify a person?** Gait is the time-varying pattern of the body and limbs during walking, a behavioral biometric. Even when a face is unclear, body shape, stride and arm-swing rhythm may suggest a familiar person. Page 50 uses the KGB/gunslinger-gait news example for intuition; it is not rigorous proof that every individual in a group can be identified by one arm posture. Page 51 emphasizes that whole-body silhouette motion may still provide evidence at long range and low resolution, when the face occupies very few pixels.

**Codebooks and codewords.** Page 52 presents 16 representative silhouette postures as codewords forming a “walking-posture dictionary.” A video is first segmented into person silhouettes, then each frame is compared with the representative postures and encoded as features. The six-entry illustration on p.53 shows a frame matching codeword 2 and producing `010000`. This illustrates conversion from image to vector; it does not mean every gait system uses six bits or exactly 16 dimensions.

**Interpretive supplement: a sequence-level Bag-of-Gait representation.** Accumulate/count posture classes over a sequence to form a comparable feature vector, with stored representations for people in the database. A query trajectory is encoded in the same way, then vector similarities yield identity candidates. A pure bag representation weakens or discards some exact temporal ordering, so the illustration should not be claimed to preserve all motion order. Page 54 shows a tracking/recognition demonstration interface, confirming a cross-frame application rather than a single-face comparison.

**Limitations/common mistakes.** Viewpoint, walking speed, clothing, carried bags, injury, occlusion and foreground-segmentation quality can change appearance. Potential usefulness at low resolution does not mean arbitrarily few pixels suffice for unique identification. Gait describes dynamic behavior; faces and fingerprints mainly supply appearance/physiological cues. These cues can complement one another rather than necessarily replacing each other.

**Answer template:** “Gait recognition uses silhouettes and movement patterns during walking as biometric evidence. Segment the person, match silhouettes to a posture codebook, encode the sequence into a Bag-of-Gait feature vector and compare it with a database. It is useful at a distance when facial resolution is low, but viewpoint, clothing, carried objects and segmentation errors affect it.”

### 3.23 Video Retrieval: Coding, Segmentation, Tracking, Features, Indexing and Queries

Sources: [S03 PDF p.55–59]; classroom: the continuous retrieval discussion in the 2026-09-17 20:05 segment 00:59:08–end.

**Task.** The inputs are a video collection and a retrieval request; outputs are relevant clips, object records or time locations containing similar people, vehicles or other objects. Saving compressed video alone does not make the system know when a particular red minibus appeared. Searchable content representations must be extracted and linked to the source video.

**The complete p.55 data flow:**

1. **Video source → H.264/MPEG-4 encoder → compressed video streams:** the coding/storage branch preserves the media while reducing storage/transmission size.
2. **Motion vectors and background model → moving object segmentation:** motion information and a background model help separate moving foreground objects. Compressed motion vectors provide cues but should not automatically be equated with complete physical object velocities (interpretive supplement).
3. **Tracking:** associate detections of the same object across frames to form a trajectory, avoid treating every frame appearance as a new object, and obtain path/direction information.
4. **Feature extraction for each tracked object:** extract descriptions such as color, edges/shape, size and path for each trajectory.
5. **DB:** store features/metadata, object or track identifiers, and time/location associations needed to return to the original video.
6. **Retrieval request → DB matching → results:** turn the request into comparable features, match them against the indexed database and return relevant content.

**The indexing diagram on p.56.** For a boxed person in video, extract metadata including Color Distribution, Edge Feature, Size and Path, then store it in an indexed metadata database. The lower diagram, `VIDEO DATA → ANALYTICS METADATA → INSIGHTS`, expresses the progression from raw images to searchable descriptions to higher-level understanding. **Compression and indexing serve different purposes: compression reduces the bytes used to preserve media; indexing organizes representations for queries.** They cooperate and do not substitute for each other.

**Two computable features on p.57.** A color histogram counts the distribution of colors such as red, yellow, blue, purple and green. An edge-orientation histogram counts edge directions such as 0°, 45°, 90° and 135°, providing coarse structural information. Combining them in a vector describes both similarity of color and similarity of contour orientation. Interpretive supplement: histograms weaken exact spatial arrangement, so objects with similar color proportions but different layouts may be confused; lighting and viewpoint also change features.

**Query examples on p.58–59.** Object photographs, such as minibuses or pedestrians, can be queries; the slides also show hand-drawn shape/color queries for vehicles and people. Query and stored objects are turned into comparable features, then similar candidates are returned. Pixel-for-pixel equality is unnecessary; rankings reflect the selected features and similarity measure. Many objects are red, so color alone does not guarantee finding a particular vehicle. Shape, trajectory and other information can be combined.

**Correspondence with Shazam.** Shazam indexes audio time-frequency peaks, while video retrieval indexes object appearance/motion features. Both first represent and index collection items, then convert a query to the same representation for comparison. The teacher's account of modern systems learning stronger features describes a change in representation acquisition; the process “index → query representation → similarity/matching → return content” remains.

**Answer template:** “Content-based video retrieval first segments and tracks objects, extracts color, edge, size and path features for each trajectory, and indexes metadata linked to original video times and locations. A query image or sketch receives comparable feature processing; database similarity matching and ranking return relevant object clips. Performance depends on discriminative features and reliable segmentation/tracking.”

### 3.24 A Metaverse Interview: An Integrated Real-Time 3D Avatar System

Source: [S03 PDF p.60]; classroom: the VR/reconstruction discussion after retrieval in the 2026-09-17 20:05 segment 00:59:08–end.

The slide uses a virtual interview between Lex Fridman and Mark Zuckerberg to show remote participants communicating through digital 3D appearances. Rather than only transmitting 2D camera video, the system can use a person's 3D model and reflect current expressions and movements on the avatar. It combines face/head capture, geometry and texture reconstruction, motion estimation, network transmission and rendering.

**Data flow as an interpretive supplement.** Build the person's model → capture face/head dynamics in real time → extract states or parameters needing updates → send them over the network → render the corresponding motion on the other side's shared model while synchronizing audio. A static personal model and a time-varying state jointly represent the interaction. The slide gives no complete communication protocol or precise latency. An approximate spoken 30–40 ms figure in the recording must not be treated as an end-to-end product performance guarantee.

**Answer template:** “Real-time 3D avatar communication first needs a renderable personal model, then continuous estimation of expression and head movement, transmission of dynamic state, and updates/rendering at the receiver synchronized with audiovisual output. It connects sensing, analysis, modeling, transmission, synchronization and presentation. Latency and model realism influence communication quality.”

### 3.25 DIKW: How Data Becomes Information, Knowledge and Action

Source: [S03 PDF p.61]; classroom: the DIKW and customer-service examples after the metaverse discussion in the 2026-09-17 20:05 segment 00:59:08–end.

**Data.** These are observations such as sensor readings, raw audio, video, locations and transactions. They may be structured numbers or unorganized multimedia content. Data Acquisitions forms the bottom layer; merely accumulating observations does not directly produce sound decisions.

**From Data to Information.** The slide lists data tagging, cleansing and correlations: label fields/events with meaning, address errors/duplicates or missing values, connect related observations, and organize them into interpretable structures. Reporting, dashboards and business analytics present trends, statistics or event information. For example, “six complaints about the same issue in a model within a week” is easier to interpret than six unlabelled recordings.

**Knowledge.** Identify patterns, relationships and clues to causes in information, supporting prediction, insights and decision making. Knowing that complaints concentrate in a region/function, or that a vibration pattern often precedes equipment failure, organizes information into useful understanding. Correlation alone does not establish causation (interpretive supplement); domain knowledge and further checks are needed.

**Wisdom.** Combine knowledge with objectives, cost, risk and the actual situation to choose an action. The slide places prescriptive analytics at the top. Prediction asks what may happen; prescriptive analysis asks what should be done. Moving between levels is not renaming files, nor does arbitrary input data automatically determine one correct action.

**The complete classroom customer-service example:** call recordings are Data. Remove noise, perform speech-to-text and analyze tone/emotion to identify complaint content and signs of dissatisfaction. Tag and aggregate by product model, function and time to produce Information about recurring problems. Infer a fault pattern/risk requiring investigation from concentrated complaints to form Knowledge. Reporting it and notifying the product/management team to investigate or adjust products/services is action supported by that knowledge. Notification is part of the classroom example, not an instruction for this study material to execute automatically.

**Why is domain knowledge necessary?** Audio, images, temperatures and stock prices have different sampling structures and meanings. Being digital does not justify identical cleansing and analysis. The teacher repeatedly emphasized that ignoring media representation and business meaning before feeding an analysis system creates garbage in, garbage out, ultimately producing incorrect decisions.

**Answer template:** “DIKW describes the progression from observations to action: Data consists of raw records; tagging, cleaning and correlation provide contextualized Information; patterns, explanations and predictions form Knowledge; choosing measures in light of objectives and circumstances represents Wisdom. In customer service, recordings are transcribed and tagged into complaint statistics, concentrated fault clues are identified, and these support investigation or product improvements.”

### 3.26 Everyday Analytics and Smart Cities: Transferring the Chapter's Methods to Real Situations

Sources: [S03 PDF p.62–63]; classroom: the multimedia, phone-sensor and urban-sensing examples in the latter part of the 2026-09-17 20:05 segment 00:59:08–end.

**Classify all p.62 examples rather than merely memorizing company names.** This figure illustrates which decisions data supports in different fields; it does not mean the class supplied a separate algorithm for every industry:

- Caterpillar: track equipment, improve utilization, manage fuel and maintenance costs. Union Pacific: predict impending failures. The pattern is equipment-condition data → risk/efficiency information → maintenance or operational action.
- Hospitals: analysis related to infections in premature infants. The pattern is monitoring/clinical data → abnormality or risk indications. This is a course application example, not diagnostic advice.
- Google Maps: travel time and live traffic. Airlines: peak-demand rates and safety issues. McDonald's: drive-through wait time. The pattern is spatiotemporal/operational data → workload, delay or risk estimates → scheduling and service improvement.
- Baseball: relate in-game activity to statistics. The pattern is actions/events → comparable performance metrics.
- Facebook: friend recommendations. Netflix: recommendations from history. Grocery stores: coupons based on history. Consumer sales: loyalty cards and customer history. Anheuser Busch: product trends. The pattern is behavioral history/relationships → preferences/associations → recommendations or marketing.
- Morgan Stanley: investment insights and risk patterns. Banks and State Farm: fraud detection. Utility companies: rates based on demand. The pattern is time-series/transaction/demand data → patterns and anomalies → risk/resource management.

**The complete smart-city chain.** Distributed sensors collect environmental, traffic, infrastructure and human-activity observations. Networks carry them to a platform, where cleaning, integration and analysis support monitoring, warnings and control actions. Examples include acoustic water-pipe leak detection, gas monitoring, wind-speed measurement, bridge-vibration monitoring and road/traffic video analytics. Page 63 uses Mario/the plumber and a traditional listening tool to introduce the change from a person visiting a location to listen to continuous sensor capture. The point is turning physical phenomena into analyzable data.

**A smartphone as a small integrated example.** Microphones sense sound, ambient-light sensors measure illumination, and motion sensors measure orientation/movement. The system maps inputs to volume, noise reduction, brightness, rotation or interaction outputs. A city expands the same sensing → analysis → action loop across locations, media types and infrastructure. It does not put all urban signals through one image algorithm.

**Limitations/common mistakes.** Sensor coverage and accuracy, temporal/spatial alignment, missing data and misinterpretation affect conclusions. Detecting an anomaly is not knowing every cause; issuing warnings does not guarantee predicting every event. Non-audiovisual sensor data such as temperature, wind speed and vibration can also enter a broadly defined multi-source media system.

**Answer template:** “A smart city connects distributed sensing, networking, data management and analysis in a loop: collect observations of traffic, environment and infrastructure; clean and fuse them according to media and business meaning; extract states/anomalies; then warn or control. Acoustic pipe-leak detection digitizes pipe sounds, analyzes abnormal patterns and locates areas for inspection, illustrating acquisition → information → knowledge → action.”

### 3.27 Comparison Answers That Transfer Across This Chapter

Source: synthesis of [S03 PDF p.2–63]. The questions below are study exercises, not announced questions.

**Q: Why are HDR, super-resolution, stabilization and deblurring not synonyms, even though all can improve image quality?**

A: HDR addresses a scene's brightness range exceeding what one exposure records. Super-resolution addresses insufficient spatial sampling. Stabilization addresses unwanted inter-frame camera displacement. Deblurring addresses trails accumulated during an exposure. They can be combined, but their input defects, estimated parameters and dimensions of improvement differ.

**Q: How can any application be described using one common answer structure?**

A: State its input and objective, then representation, core processing, output and limitations. For example: “Video retrieval takes video and a query image, segments and tracks objects, extracts color/edge/path features and builds an index. The query is represented with the same features and similarity returns object clips. Lighting, occlusion or weak features can degrade performance.” This is more complete than listing “segmentation, tracking, DB.”

**Q: Why distinguish audio, images and video once all raw data becomes bits?**

A: Bits are a shared low-level encoding, but organization and physical meaning differ: audio is primarily a 1D time sequence, images are 2D spatial samples, and video is an image sequence over time. Effective filtering, features, compression and models must preserve the corresponding structure and domain meaning. Ignoring these differences damages information or produces incorrect conclusions.

**Q: What distinguishes hand-designed features, model-based methods and deep learning?**

A: Hand-designed features specify measurements such as eye–nose distances, color or edges. Model-based methods use deformable shape/appearance constraints to explain observations. Deep learning learns complex representations and prediction parameters from examples. All still require appropriate input, representation and evaluation. Learning features changes how features are obtained; it does not eliminate them.

**Q: Where does human perception actually affect system design?**

A: EQ changes perceived spectral balance; psychoacoustic compression uses hearing thresholds and masking to prioritize perceptible content with limited bits; image enhancement improves visibility in shadows or uneven lighting; real-time avatar latency, synchronization and appearance influence communication. Outputs serve perceptual objectives, so evaluation cannot be limited to whether numerical samples remain identical to the originals.

### 3.28 S03 Page-by-Page Coverage Checklist

This checklist uses actual PDF page numbers and includes pages consisting only of images/demonstrations. The cover and repeated outlines are included so that omissions can be checked.

- p.1: application chapter cover and topic; see 3.1.
- p.2: outline of five audio-application categories; see 3.3–3.8.
- p.3: headphone ANC input, anti-phase output and cancellation diagram; see 3.3.
- p.4: in-car architecture with microphones, engine information, ECU and audio cancellation; see 3.3.
- p.5: dual-microphone speech/environmental-noise reference and subtraction illustration; see 3.3.
- p.6: question about additional microphones and the old-phone example; see 3.3.
- p.7: historical article on far-field pickup, background sound, power, overload point, size and additional microphones; see 3.3.
- p.8: EQ definition, bands, gain ranges and presets; see 3.4.
- p.9: A/D, noise reduction/normalization, short-time segmentation, phonemes and statistical conversion to words; see 3.5.
- p.10: Shazam, approximately 10-second queries, spectrograms, peaks and robustness; see 3.6.
- p.11–14: database/query constellation maps, temporal shifting and matching-peak counts; see 3.6.
- p.15: LPC vocoder and physiological speech production; see 3.7.
- p.16: vocoder parameters, tone/noise excitation, variable filter, GSM and the question about other uses; see 3.7.
- p.17–18: MPEG Audio and ear-structure/frequency-response illustrations; see 3.8.
- p.19: hearing threshold, frequency masking and temporal masking; see 3.8.
- p.20: three audio Layers, 1152 samples, 32 bands, psychoacoustics and variable-length coding; see 3.8.
- p.21: recap of audio-application categories; see 3.3–3.8.
- p.22: outline of eight image/video processing and analysis categories; see 3.9–3.23.
- p.23: Night Mode multi-frame processing at different shutter speeds; see 3.9. HDR is supplemented from the associated recording.
- p.24: historical nine-frame Deep Fusion example; see 3.9. Super-resolution is a classroom supplement.
- p.25: Retinex enhancement of a port scene; see 3.10. The specific illumination/reflectance formula is marked as an interpretive supplement.
- p.26: video-stabilization example; see 3.11.
- p.27: blur caused by global camera movement versus fast-moving objects; see 3.12.
- p.28: different relative velocities in different parts of an object; see 3.12.
- p.29: foreground, segmentation/corners, HBMA tracking, motion estimation, blur kernel and deblurring pipeline; see 3.12.
- p.30: before/after recovery of minibus details; see 3.12.
- p.31: Haar, AdaBoost, cascade and position/scale scanning; see 3.13–3.14.
- p.32: multi-person head detection/trajectory demonstration; see 3.15.
- p.33: q₁–q₈ contour model and left/right viewpoints; see 3.15.
- p.34: tripwire people counting and head captures; see 3.15.
- p.35–36: successful frontal matching and difficulties with profiles; see 3.16.
- p.37: four-stage reconstruction pipeline; see 3.16.
- p.38: three view-specific AAMs and minimum-residual selection; see 3.17.
- p.39: 6292 vertices/6152 facets, texture map and texture coordinates; see 3.18.
- p.40: personalized facial-model modification; see 3.18.
- p.41: aligning a 3D model to profile pose; see 3.19.
- p.42: texture rebuilding, rendering, filling/interpolation and postprocessing; see 3.20.
- p.43: reconstructed people and alternative views; see 3.20.
- p.44–45: profile frontalization followed by recognition; see 3.16 and 3.20.
- p.46: gallery similarities before/after reconstruction for four cases; see 3.20.
- p.47: specially designed glasses interfering with an automatic system; see 3.21.
- p.48: glasses affecting human recognition of unfamiliar faces; see 3.21.
- p.49: Face ID structured light, infrared/illumination and multiple sensing components; see 3.21.
- p.50–51: gait as a biometric and low-resolution silhouette sequences; see 3.22.
- p.52–53: 16-posture codebook and Bag-of-Gait vector illustration; see 3.22.
- p.54: gait-tracking demonstration interface; see 3.22.
- p.55: video coding/storage, motion/background, segmentation, tracking, features and DB/query flow; see 3.23.
- p.56: object color, edges, size and path metadata, plus the indexing pyramid; see 3.23.
- p.57: color and edge-orientation histograms; see 3.23.
- p.58–59: retrieval using photographs and drawn shapes/colors; see 3.23.
- p.60: the Lex Fridman/Mark Zuckerberg virtual interview; see 3.24.
- p.61: DIKW, acquisition, tagging, cleansing, correlation, reporting, predictive/prescriptive analysis; see 3.25.
- p.62: all everyday-analytics fields in the figure; see 3.26.
- p.63: Mario/the plumber, acoustic leak-listening tools and smart-city sensing systems; see 3.26.

### 3.29 Transcript/Slide Ambiguities and Boundaries of Interpretation

- **“Voice/noise cancellation” and “phase/face shift” recognition errors:** several words are mistranscribed in the September 10 recording. Follow p.3–7 and read them as noise cancellation and phase shift; “face” in face detection genuinely means a face.
- **“Works” should be “words”:** p.9's “map phonemes to works” is an obvious typo for mapping phonemes to words. The recording's alphabet example is simplified and must not equate phonemes with letters.
- **“High speed/ISBN/ID” confusion:** “high speed” appears several times in the September 10 library analogy, but context concerns book identifiers/indexing. Do not accept the mistranscribed words literally.
- **“MPEG/impact,” “gait/gate,” “mesh/mission” and “gain/game”:** correct these using slide terminology. “Gate” is not the term for walking behavior, and “gain” should not be understood as a game.
- **Frequency values:** the September 17 transcript mixes 2 Hz/200 Hz/20 Hz with 20 kHz. This chapter uses the approximate 20 Hz–20 kHz range consistent with the slides and standard concepts, without claiming it is fixed for every person.
- **Hearing mechanism:** p.17 simplifies high/low-frequency sensitivity as differences in hair length. Understand the cochlea's frequency selectivity along its length rather than treating an individual cell's hair length as the sole determining factor.
- **Where masking operates:** a component being inaudible to a human does not mean a microphone cannot capture it. MPEG encoders allocate data using a perceptual model; coding logic must not all be attributed to the microphone.
- **RGBA/bit calculations:** the recording mixes alpha with stacking order and misrecognizes some 4×4 and Full HD numbers. Section 3.2 recomputes them using the correct transparency interpretation and multiplication.
- **HD/DVD:** “DVD 1280×720” in the recording is not a correct format definition; 1280×720 is common HD 720p.
- **Audio Layers and versions:** Layers I/II/III are audio coding layers; MP3 is Layer III, not a supposed MPEG-3. About 26 ms corresponds to 1152 samples at approximately 44.1 kHz.
- **Similarity versus accuracy:** p.46's per-example similarities are not statistical recognition accuracies. Approximate classroom ASR/face “generation accuracy” figures lack datasets and conditions and are not used as quantitative conclusions.
- **Scope of old products/demonstrations:** the 2016 microphone article, 2019 nine-frame Deep Fusion case, frontal-only demonstration software and Face ID component image are slide examples, not universal current-product specifications.
- **Implementations not expanded in the materials:** Retinex equations, the LPC prediction interpretation, convolution-kernel model, precise alpha definition and duplicate suppression in tracking are marked as interpretive supplements to explain principles, not additional teacher-announced scope. The slides do not expand HBMA on p.29 or give one unique answer to the other-vocoder-use question on p.16; this uncertainty is retained.
## 4. Sensors, Digitization, and Sound Acquisition: Complete Coverage of S04

This chapter follows S04, “Media Sensor and Reproduction - Part 1”, PDF p.1–49. Classroom additions come from the complete transcript dated 2026-09-24. Slide content, classroom examples, and additional explanatory derivations are distinguished below. The audio transcripts are ASR output: technical terms and units have been checked against the slides and mathematical relationships. Misrecognized words must not be treated as new concepts.

### 4.1 What Is a Sensor? Turning the Physical World into Usable Signals

**Definition.** A sensor measures a physical quantity and converts it into a signal that a person or machine can use. For example, a microphone measures changes in air pressure and produces an electrical signal; a camera's photosensitive elements convert incident light into charge or voltage; a temperature sensor converts temperature into a reading. Sensors are the entry point from the physical world into the information-processing part of a multimedia system. [S04 PDF p.2–4]

**Do not skip the intermediate steps.** A common acquisition chain is `physical quantity → analog electrical signal from the sensor → conditioning/amplification → A/D digitization → computer analysis`. A sensor does not necessarily output digital values directly, and “being able to measure sound” is not equivalent to “understanding what was said”. The former is transduction/sensing; the latter additionally requires feature extraction, models, and semantic interpretation. The lecturer illustrated this distinction by contrasting people's feelings of “hot” or “cold” with a machine's need for specific numerical values. (2026-09-24 transcript 00:06:43–00:23:39)

The slides identify three groups by purpose; these categories can overlap:

- **Imitating human senses.** Touch, sight, hearing, smell, and taste correspond to the skin, eyes, ears, nose, and tongue. Cameras and microphones are the principal mature multimedia input devices.
- **Measuring life/health.** Weight, body temperature, heart rate, ECG, and movement do not necessarily correspond to a separate one of the traditional five senses.
- **Measuring physical facts about the environment.** Acceleration, rotation, geographical position, radiation, and altitude allow computers to acquire quantities that humans cannot sense directly, precisely, or reliably.

**Exam-ready answer.** “A sensor measures a physical quantity and converts it into a usable signal. Multimedia systems use microphones to acquire sound and cameras to acquire light, then digitize and analyze these signals. Sensors bridge the physical environment and computer representations, while interpretation requires additional processing.”

### 4.2 Touch: Resistance, Capacitance, Force Detection, and Actuators

The skin is the human organ of touch; artificial tactile sensors convert contact, pressure, and related quantities into signals. Touch position, contact area, and applied force are different measured quantities and should not all be loosely described as “sensing pressure”. [S04 PDF p.5–7]

**Resistive touch: additional explanation of the mechanism.** Two conducting films are initially separated. Pressure brings them into contact, and a controller estimates position from the resulting voltage/resistance relationships. Actual pressure is normally required. A finger, gloved hand, or suitable stylus can trigger it, making it appropriate for some industrial and point-of-sale settings. Multitouch capability depends on the implementation; traditional structures have weaker support for multitouch. An experience with a particular shop terminal does not establish that every resistive touchscreen is entirely incapable of multitouch.

**Capacitive touch: additional explanation of the mechanism.** A conducting finger approaching or touching an electrode array changes local self-capacitance or mutual capacitance, enabling the controller to locate the contact. Light touch is sufficient, and the technique is commonly used for multitouch gestures such as pinch-to-zoom. Ordinary insulating gloves weaken coupling; water may cause false touches or affect positioning. Wet-finger/glove support depends on device design. The primary measurement is a capacitance change, not necessarily the finger's applied pressure.

**3D Touch / force sensing.** This adds a “how hard” dimension beyond position, mapping light and firm presses to different commands, such as previewing and opening. Force detection must not be equated directly with ordinary capacitive positioning; the slide demonstrates an additional input dimension. [S04 PDF p.6]

**An actuator provides feedback.** A sensor is an input device, while an actuator produces output. A phone's vibration module or Taptic Engine converts an electrical signal into mechanical motion to provide haptic feedback. A brief vibration after touch detection confirms that an action occurred. The interaction loop is `finger action → sensor → control logic → actuator → skin perception`. [S04 PDF p.7; 2026-09-24 transcript 00:23:39–00:26:40]

**Answer to a comparison question.** Resistive touch relies on pressing conductive layers together, whereas capacitive touch relies on capacitance changes. They therefore differ in required contact force, the effects of gloves/water, and how multitouch is implemented. The actuator generates vibration feedback; do not answer that the sensor itself generates that vibration.

### 4.3 Vision Extends Beyond Taking a Photograph: Perception, Memory, and Binocular Disparity

**Artificial visual input.** A camera uses photoelectric conversion to turn incident light into electrical signals; the slides identify CCD and CMOS sensors. Photosensitive elements form an array. A greater pixel count generally permits higher spatial sampling resolution, but actual detail also depends on the lens, noise, pixel size, exposure, and processing. Pixel count alone is insufficient. [S04 PDF p.8; the detailed S05 camera comparison appears in a later chapter]

**The “spot the difference” classroom experiment.** Comparing two pictures requires object identification, analysis of spatial relationships, storing the previous picture in short-term memory, comparison, and recording/pointing out difference locations. The slides use the roles of the occipital, parietal, and frontal lobes to show that vision involves multiple processing stages. Understand this functional decomposition rather than assigning the entire complex task to one exclusive brain region. [S04 PDF p.9–11; 2026-09-24 transcript 00:29:05–00:32:21]

**Binocular vision.** The left and right eyes view the same object from slightly different positions, producing disparity between the retinal projections. The brain establishes correspondences between the two views and uses them to perceive depth. Even a single screen image can use repeated texture/correspondences in a stereogram to induce a fused depth percept. Thus “two-dimensional input” and “perceiving three dimensions” are different concepts. [S04 PDF p.12–15]

**How to view a stereogram.** The slides suggest first bringing the image close to the nose, where the eyes cannot focus normally on its surface, then slowly moving it away while keeping the gaze as though looking behind it. Another method is to focus on a location about half a metre behind the image. Different stereograms can require parallel viewing or crossed viewing; the phrase “cross eyes” in the classroom transcript must not replace the specific method demonstrated in the slides in every case. The learning point is binocular disparity and perceptual fusion, not an obligation to see the hidden image successfully. [S04 PDF p.13–15; 2026-09-24 transcript 00:32:21–00:34:34]

**Exam-ready answer.** Visual perception involves acquiring light signals, identifying content, analyzing spatial relationships, and incorporating memory. Different projections in the two eyes can supply depth cues. Increasing a camera's pixel count therefore improves only part of the input and does not automatically provide visual understanding.

### 4.4 Hearing Sensors: Dynamic and Condenser Microphones

A microphone is an acoustic sensor that converts sound-pressure changes into electrical signals. Pressure moves a diaphragm; different microphones use different transduction mechanisms to convert this mechanical displacement into changes in voltage, current, or capacitance. [S04 PDF p.16–17, 43]

**Dynamic microphone.** The diaphragm moves a coil within a magnetic field, and changing magnetic flux induces a voltage: electromagnetic induction. A typical passive moving-coil transducer itself does not require an external power supply, is mechanically robust, and suits applications such as stage use, vocals, and high sound-pressure levels. The statement that the microphone “needs no power” applies only to this passive transduction mechanism: a wireless transmitter or additional preamplifier may still require power. [S04 PDF p.16; mechanism and classroom explanation: 2026-09-24 transcript 00:35:01–00:38:12]

**Condenser microphone.** The diaphragm and a fixed backplate form a capacitor. Sound pressure changes the plate spacing and hence capacitance; biasing and electronic circuitry produce an electrical signal. The simplified relationship is `C = εA/d`: changing separation d changes C. Common condenser microphones need power for polarization and/or internal circuitry, such as phantom power or a battery. An electret contains permanently polarized material, but its internal impedance-conversion circuit normally still needs power. Common designs offer high sensitivity and good transient response, making them suitable for detailed acquisition. Whether they are “better” depends on the task, noise, and model, rather than price or the two categories alone. [S04 PDF p.16–17; additional explanation; 2026-09-24 transcript 00:37:55–00:43:40]

**How to answer a selection/comparison question.** Both receive sound pressure and output electrical signals. A dynamic microphone uses induction from relative motion in a magnetic field, whereas a condenser uses capacitance changes between the diaphragm and backplate. Transduction principle and directionality are independent dimensions: a dynamic microphone is not necessarily cardioid, and a condenser is not necessarily omnidirectional.

### 4.5 Other Senses, Health Sensors, and Environmental Sensors

**Smell and taste.** The slides emphasize the complexity of their chemical/physical mechanisms; this course concentrates on sight and hearing. A suitable revision statement is that human smell/taste is difficult to reproduce in a general-purpose way. Do not treat the p.18 statement that “no artificial noses and tongues” exist as permanently true. Electronic noses/tongues can detect particular chemicals or patterns, while still falling short of reproducing the full human experience. [S04 PDF p.18; clarification of the scope of the slide statement]

**Sensing in other species.** Temperature, gravity, magnetic fields, humidity, and infrared are slide examples. Some animals sense ranges different from ours, and artificial systems can measure these quantities through appropriate sensors. Multimedia should not be understood only within human sight/hearing limits, because machines can capture information outside human sensory ranges. [S04 PDF p.19]

**Life/health-related sensors.** [S04 PDF p.20–21]

- A weight sensor measures mass/weight. The standard BMI relationship is `BMI = weight in kg / (height in m)²`. Age and sex can affect health interpretation, but are not required inputs to the standard BMI formula. Do not copy the implication that BMI calculation itself must include age and sex.
- A temperature sensor measures body temperature; a noise sensor monitors exposure to loud environments; a heart-rate sensor estimates heartbeats per minute.
- ECG measures the heart's electrical activity and can support rhythm analysis. It is more than a single “heart-rate number”, and one measured quantity cannot automatically establish every health conclusion.
- A movement sensor measures acceleration/activity. Combined with heart rate and personal parameters, this can estimate energy expenditure. “Calories burned” is a model estimate rather than a physical quantity measured directly by an accelerometer.
- In the Care-on-Call example for older people, wearable devices continuously collect status information, with abnormalities triggering notifications or a call response. The point is the combination of multiple sensors, continuous monitoring, event detection, and a service workflow. Memorizing every product detail of one illustrative device is unnecessary. (2026-09-24 transcript 00:43:40–00:46:02)

**Environmental sensors.** [S04 PDF p.22]

- An **accelerometer** measures acceleration/specific force. The direction of gravity can help estimate static tilt, and periodic walking patterns can support step counting. It does not directly measure GPS position.
- A **gyroscope** measures angular velocity. Integration can estimate angular change, although drift may accumulate. “Accelerometers concern translational acceleration; gyroscopes concern rotation” is the basic distinction.
- A **GPS receiver** estimates position from satellite positioning information; it does not measure rotational motion.
- A **radiation sensor** measures radiation. An **altimeter** measures/estimates altitude; for example, a barometric altimeter uses the relationship between atmospheric pressure and altitude.
- People can experience **spatial disorientation**, for example in aircraft. Instruments provide independent measurements and can be more reliable than subjective sensations. This does not mean that an objective sensor is error-free; the following section explains its limitations.

**Exam-ready answer.** Combining sensors for different physical quantities expands observation coverage, reduces ambiguities of a single sense, and supports applications such as health monitoring and positioning. Final conclusions about activity, health, or state usually require a model for interpretation rather than merely reading one sensor value.

### 4.6 Sensor Limitations: Dynamic Range, Offset, Nonlinearity, and Hysteresis

**Dynamic range.** This is the range between the smallest and largest useful input magnitudes. Below the detectable lower limit, noise overwhelms the signal; above the upper limit, the output may saturate or clip. When the highlight-to-shadow range in a photograph is too large, exposing for shadows can lose highlights, while exposing for highlights can lose shadows. HDR can combine different exposures/multiple sensors to capture complementary ranges, followed by alignment and fusion. Object motion and sensor differences can complicate this fusion. [S04 PDF p.23; 2026-09-24 transcript 00:49:03–00:55:10]

**Do not confuse two different meanings of “range”.** An 8-bit encoding supplies 256 digital codes, but the true dynamic range of a physical sensor is not equivalent to being able to capture only “0–120 or 120–240”. Such numbers were used as classroom intuition. More precisely, the noise floor, saturation ceiling, exposure, and encoding mapping jointly determine how much actual scene brightness detail is retained.

**Offset / bias.** The output is nonzero when the input is zero. In the linear model `y = kx + b`, b is the offset and k is the sensitivity/gain. With known calibration parameters, use `x = (y−b)/k` to recover the input. Examples include a residual black level when light is blocked or a zero-point measurement error without the target input. A phone consuming battery power on standby is not a precise definition of sensor offset; define it as nonzero output at zero input in an examination. [S04 PDF p.24; 2026-09-24 transcript 00:50:29–00:55:54]

**Nonlinearity.** Equal increments in input do not produce proportionate/equal increments in output. For example, a microphone may distort at high sound pressure, so a single k no longer converts output back into pressure correctly. Restricting the operational range or using a calibration curve may help. Distinguish a non-flat frequency response from a nonlinear amplitude relationship: they produce different forms of coloration/distortion. [S04 PDF p.24; 2026-09-24 transcript 00:55:10–00:57:15]

**Hysteresis.** Output depends on the present input and on the history leading to that input. Sweeping input upwards and downwards follows different response paths. The same input can produce different outputs, and conversely one output may correspond to different input states. For example, a pressure sensor may not retrace its loading curve when pressure is released. Hysteresis should not be defined merely as “slow response” or “long-term drift”. [S04 PDF p.24; 2026-09-24 transcript from 00:57:15]

**Variation with time/temperature: drift, additional explanation.** The lecturer also noted that changes in operating temperature can change a device's response curve. Calibration, temperature compensation, and periodic rechecking help control shifts. Thermal drift and hysteresis may be related but are distinct terms. Slide p.24 places “Sensor Response Deviation over time” near hysteresis; define the concepts separately rather than substituting one for the other.

**A complete application-answer pattern.** Name the limitation, state its effect, and propose a measure. For example: “Input exceeding a camera's dynamic range causes clipped highlights and lost shadow detail. Multi-exposure HDR/multisensor fusion can extend capture range, with registration and motion handling required.” Merely saying that sensors have limitations and should be replaced by more expensive ones does not explain the mechanism.

### 4.7 From LEGO to Signals: Sinusoids and Frequency-Domain Analysis

The lecturer used a LEGO house as an analogy: many complex structures can be built from a small collection of standard bricks. Likewise, complex sensor outputs can be represented/analyzed through sine/cosine components with different frequencies, amplitudes, and phases. The figures on p.26–27 juxtapose a complex waveform and several simple periodic components. The central ideas are **decomposition and composition**; the course does not require a complete Fourier-transform derivation here. [S04 PDF p.25–30; 2026-09-24 transcript 00:57:15–01:18:19]

A basic waveform can be written as `x(t) = A cos(2πft + φ)`:

- **Amplitude A:** The maximum magnitude relative to the centre line. For sound waves it relates to sound-pressure strength. Perceived loudness also depends on frequency and the auditory system, so A must not be equated with a linear scale of “felt volume”.
- **Frequency f:** The number of cycles per second, measured in Hz; the period is `T = 1/f`. For tones with a clear periodic structure, fundamental frequency relates to pitch.
- **Phase φ:** The waveform's position in its cycle at the chosen time origin. It determines how peaks and troughs align during superposition. Two waves with equal frequency and amplitude and a phase difference of π can cancel when superposed at the same location.

**Geometric interpretation.** Project a point undergoing uniform circular motion onto an axis. Its position over time traces a sinusoid. Increasing the circle radius changes A, rotating faster changes f, and changing the initial angle changes φ. [S04 PDF p.28–30]

**Time domain and frequency domain.** The time domain asks, “What is the amplitude at this time?” The frequency domain asks, “Which frequencies are present, with what strengths/phases?” A flute and piano sharing a fundamental frequency can have different harmonic strengths in the frequency domain and therefore sound different. General nonperiodic signals can be described using continuous spectra/appropriate transforms. It is not a universal law that every finite waveform is represented exactly by only a few integer-multiple harmonics. (Additional clarification)

**Exam-ready answer.** Fourier analysis decomposes a complex signal into sinusoidal frequency components. Each component is specified by amplitude, frequency and phase; analyzing these components helps filtering, recognition and synthesis. The LEGO analogy illustrates how different signals can share basic building blocks while differing in their combinations.

### 4.8 Digitization: Which Axes Do Sampling and Quantization Discretize?

**Digitization requires more explanation than “turning a signal into 0s and 1s”.** An analog signal is continuous in both time and amplitude; a computer generally requires discretization along both dimensions. [S04 PDF p.31–33]

1. **Sampling discretizes the time axis.** Read the signal every `Ts = 1/fs` seconds to obtain `x[n] = x(nTs)`. fs is the number of samples per second, measured in samples/s or Hz. A higher fs provides more samples in the same interval and raises the upper limit of frequencies that can be retained.
2. **Quantization discretizes the amplitude axis.** Map each sample to a finite set of representable levels. n bits provide `L = 2^n` codes: 8 bits give 256 levels, 16 bits give 65,536, and 24 bits give 16,777,216. Binary coding then stores those levels.

**Quantization error/noise.** This is the difference between the quantized value and the original sample value. Fewer levels give a coarser amplitude scale and more easily lose weak detail. For uniform quantization over a full-scale range R, a common approximate step is `Δ = R/2^n`. With nearest-neighbour rounding and no overload, `|e| ≤ Δ/2`. If the code-value convention includes both endpoints, the denominator may instead be `2^n−1`. Follow the question's definition rather than mixing the formulas. (The equations are an additional explanation.)

**Why is digital representation relatively resistant to distortion?** Within the margin where disturbances do not cause incorrect 0/1 decisions at the receiver, digital data can be regenerated, copied, and checked. Small disturbances accumulate in analog copying. However, sampling, quantization, compression, packet loss, and overflow can all lose information, so “digitization is lossless and never distorts” is incorrect. [S04 PDF p.31–33]

**The file-size calculation explicitly practised in class.** For raw uncompressed PCM data:

`bitrate = fs × n × C` (bit/s)

`size(bits) = fs × n × C × duration`; `size(bytes) = size(bits)/8`

C is the number of channels. For example, 5 s of mono audio, one sample per second, and 4 bits per sample requires `5×1×4 = 20 bit`. This is the lecturer's small example explaining “number of samples multiplied by bits per sample”, rather than a practical audio configuration. (2026-09-24 transcript 01:24:02–01:29:24)

**Practical numerical examples.** Uncompressed PCM at 44.1 kHz, 16 bits, stereo has `44100×16×2 = 1,411,200 bit/s`. One minute requires `10,584,000 bytes ≈ 10.584 MB ≈ 10.094 MiB`, excluding the header. At 48 kHz, 24 bits, mono, 10 s requires `48000×24×1×10/8 = 1,440,000 bytes`. Compressed formats such as MP3/AAC are normally estimated from encoded bitrate multiplied by duration; the PCM formula is not directly the compressed file size.

**Common confusions.** Sampling rate is the number of samples per second; bit depth is the number of bits per sample; bitrate is the number of bits per second. Increasing fs does not replace greater bit depth in reducing quantization step size, and increasing bit depth does not solve aliasing from insufficient temporal sampling. Raising either generally increases storage and transmission requirements. [S04 PDF p.33; 2026-09-24 transcript 01:30:44–01:41:47]

### 4.9 Nyquist, Aliasing, and 44.1 kHz: Distinguishing the Two Frequency Terms

Let B Hz be the highest analog frequency to be retained. Ideal band-limited sampling requires `fs > 2B`. For a specified fs, the **Nyquist frequency is fs/2**. The **Nyquist rate is 2B**, the sampling-rate boundary determined by signal bandwidth. The classroom transcript sometimes calls the latter the Nyquist frequency as well. In an examination, explicitly defining both quantities and writing both formulas is clearest. [S04 PDF p.33–34; 2026-09-24 transcript 01:41:47–01:52:18]

**Why more than twice the highest frequency?** With insufficient sampling, different analog frequencies can produce identical sample sequences and cannot be uniquely reconstructed. This is aliasing. Denser interpolation of already acquired samples cannot restore the original lost information.

**Why is `fs = 2B` not a universal guarantee?** For `x(t) = A cos(2πBt + φ)`, if `Ts = 1/(2B)`, then `x[n] = A cos(πn + φ) = A(−1)^n cosφ`. When `φ = π/2`, every sample is 0 although the original wave is clearly nonzero. Different amplitude/phase combinations can also give the same sequence. Slide p.34 uses this effect to motivate a strict inequality and explain phase ambiguity at the boundary. The original slide's trigonometric identity does not retain A consistently in all terms; A is kept here to avoid confusion.

**An aliasing example: additional calculation.** At fs=32 kHz, an 18 kHz component folds into an observable lower-frequency component at `|18−32|=14 kHz`. Low-pass filtering only after sampling cannot separate it by original frequency, because the 18 kHz content has already mixed into 14 kHz.

**Anti-aliasing filter: additional engineering explanation.** Low-pass filter before the ADC to attenuate components outside the target bandwidth/near the Nyquist boundary sufficiently, and then sample. Real filters are not ideal brick walls and require a transition band. Practical fs is therefore often higher than the theoretical 2B boundary. DAC playback also requires appropriate reconstruction processing; “connecting sample points with straight lines” is not a substitute for the complete reconstruction principle.

**How to interpret 44.1 kHz.** fs=44.1 kHz gives Nyquist=22.05 kHz. It accommodates the audible audio bandwidth commonly targeted while allowing filtering space near the upper audio limit. Slide p.35 gives 12 Hz–22 kHz, whereas p.49 gives 20 Hz–22 kHz; approximately 20 Hz–20 kHz is a common teaching convention, with individual and age-related variation. The lecturer used `2×22 kHz≈44 kHz` to explain the relationship between sampling and hearing range. Do not reduce the complete historical origin of 44.1 kHz to “only 22 kHz plus a 0.1 kHz tolerance”. Nor should one infer that a real 44.1 kHz system perfectly retains full-amplitude content all the way to 22.05 kHz without filter margin. [S04 PDF p.35, 49; 2026-09-24 transcript 01:47:12–01:50:26]

**Do 48/96 kHz let people hear ultrasound?** Higher fs can facilitate some recording, digital processing, filtering, or research outside human audible ranges, while increasing storage and computation. It does not extend the physiological upper limit of human hearing. A higher fs alone does not establish that perceived audio quality must improve. [S04 PDF p.49]

**Three questions and answers.**

- To retain 5 kHz, how should fs be chosen? Answer: The theoretical boundary is 10 kHz; the safe condition is fs>10 kHz, with the real filter transition band considered.
- With fs=8 kHz, what is the upper limit of the ideal representable frequency range? Answer: Nyquist is 4 kHz, and the practical usable bandwidth should be lower. It is not an 8 kHz audio bandwidth.
- If the highest frequency is 6 kHz and fs=12 kHz is specified, is reconstruction guaranteed unconditionally? Answer: This is the boundary, with phase/endpoint issues. State the strict condition fs>12 kHz and band-limiting assumptions explicitly.

### 4.10 Physical Properties of Sound: Pressure Waves, Propagation Speed, and Wavelength

The common form of sound in air/liquids is a longitudinal mechanical pressure wave. Local compression and rarefaction propagate through the medium while its particles mainly oscillate around equilibrium positions. Sound requires a medium and cannot propagate in a vacuum, unlike light, which needs no material medium. [S04 PDF p.35]

Slide examples give approximately **343 m/s** in dry air at 20°C and **1482 m/s** in water at 20°C. Speed depends on the medium and conditions. Mach 1 means the local speed of sound, not a fixed 343 m/s in every medium. The transcript's “millimeters per second” is a recognition error and must be corrected to the slide's m/s. (2026-09-24 transcript from 01:53:50)

Wave speed, frequency, and wavelength satisfy `v = fλ` (additional explanation). For example, a 1 kHz sound wave in air has wavelength approximately `343/1000 = 0.343 m`; at 100 Hz it is about 3.43 m. Frequency describes the repetition rate, not how much faster the sound travels. High and low tones propagate at approximately the same speed in the same approximately nondispersive medium.

**Exam-ready answer.** Sound is a mechanical pressure wave that propagates through a material medium. Frequency relates to pitch, while amplitude relates to sound pressure; phase affects how waves combine. The speed depends on the medium and temperature, and sound cannot travel through a vacuum.

### 4.11 Sound Pressure Level, dB, and dBA

**Definition of SPL.** Sound pressure level is `Lp = 20 log10(p_rms / p_ref) dB = 10 log10(p_rms² / p_ref²) dB`. p_rms is RMS sound pressure. The usual reference is `p_ref=20 μPa` in air and `1 μPa` in water. dB expresses a logarithmic ratio relative to a reference; do not simply say “the pressure is 60 dB” while ignoring the reference and measurement conditions. [S04 PDF p.36]

**Why does the pressure formula use 20?** In comparable sound fields, intensity relates to squared pressure, so `10log(p²/p_ref²)=20log(p/p_ref)`. Use 10log for direct power/intensity ratios and 20log for pressure/amplitude ratios. First identify the physical quantity supplied by the question.

**Short calculations.** If p=0.02 Pa, `p/p_ref=1000`, so SPL=60 dB. Doubling pressure adds `20log10 2≈6.02 dB`; doubling intensity under the corresponding conditions adds about 3.01 dB. A level of 0 dB SPL means that pressure equals the reference, not an absence of sound. Adding two coherent same-frequency signals also depends on phase; the sources' dB values cannot simply be added arithmetically.

**Subjective loudness is not physical pressure.** Human auditory response has an approximately logarithmic character and unequal frequency sensitivity. Low- and mid-frequency sounds with the same SPL need not seem equally loud. Pressure is therefore not a linear scale of subjective loudness. [S04 PDF p.36–37]

**A-weighting.** Apply frequency-dependent weights during measurement, reducing contributions from frequency regions to which the ear is less sensitive, especially low frequencies. The result is written dBA or dB(A) and is used to approximate auditory sensitivity more closely. This is frequency weighting, not a conversion of dB “from logarithmic to linear”, nor a subtraction of one identical constant from every frequency. If processing separate bands, their combined level must still follow energy relationships rather than ordinary addition of band dB values. [S04 PDF p.37; 2026-09-24 transcript 01:55:17–01:59:43]

**Exam-ready answer.** SPL measures a logarithmic ratio of RMS sound pressure to a reference pressure. A-weighted SPL additionally weights frequency components to approximate the ear's unequal frequency sensitivity; equal unweighted SPL does not necessarily mean equal perceived loudness.

### 4.12 Echo, Reverberation, Interference, and Active Noise Cancellation

**Echo.** A sound reflection arrives after the direct sound as a distinct/delayed copy, for example from a valley or the bottom of a well. The slides use approximately 0.1 s as an empirical delay for distinguishing a reflection from the original. This is not an identical fixed boundary for all sounds, environments, and people. Even when a listener hears no separate echo, a delayed copy can still impair machine recognition. [S04 PDF p.38]

**Reverberation.** Many reflections in an enclosed space overlap densely in time, with energy gradually decaying as the environment absorbs it, producing a tail. It is not merely another word for a clear, isolated echo. The tail blends adjacent phonemes and changes features and temporal boundaries, complicating ASR, source localization, and content analysis. Absorption, changing the distance between the microphone and talker, and dereverberation can help control it. (The remedies are additional explanations.) [S04 PDF p.39; 2026-09-24 transcript 01:59:43–02:01:32]

**Calculating reflected path length: additional explanation.** An extra propagation delay of 0.1 s corresponds to an additional air path of approximately `343×0.1=34.3 m`. If a person faces a wall and the additional round-trip path is approximated as 2d, then `d≈17.15 m`. These are different path definitions; do not identify the 34.3 m path directly with person-to-wall distance.

**Interference.** Two or more waves superpose at the same place and time. In-phase components reinforce one another, giving constructive interference; antiphase components weaken one another, giving destructive interference. Equal-frequency, equal-amplitude waves in opposite phase can ideally cancel at a target location. Real sound is often multifrequency, moving, and multipath, so a single fixed delay cannot perfectly cancel every frequency at every position. [S04 PDF p.40]

**Active noise cancellation, ANC.** A microphone measures environmental noise, the system estimates the antiphase signal required at the ear, and a loudspeaker reproduces it so that noise amplitude decreases at that location. Continuous, predictable low-frequency noise, such as engine noise, is generally more suitable. High frequencies, transients, position changes, and processing delay make control harder. This is not the deletion of an audio track from a file. Passive isolation instead blocks/absorbs sound through materials, a different mechanism. (Additional application explanation; 2026-09-24 transcript 01:16:17–01:18:00 and from 02:01:32; the 9/10 recording also includes noise-cancellation examples.)

**Comparison answer.** Echo is a delayed reflected copy; reverberation is the dense buildup and decay of many reflections; interference is the addition of waves and may increase or decrease their resultant amplitude. All can change the captured signal, but destructive interference can also be deliberately used for noise cancellation.

### 4.13 Early Recording: Mechanical Storage and Reproduction

A cylinder phonograph first engraves pressure-induced mechanical vibration into tinfoil wrapped around a rotating cylinder. During playback, a stylus follows the groove, converting its variations back into mechanical vibration and then sound through the mechanical structure/horn. The learning point is that **recording stores a time-varying quantity in some persistent form, while reproduction converts it back into perceptible variation**. Recording was not always digital or even based on electrical signals. [S04 PDF p.41]

A music box uses pins or other mechanical structures on a cylinder to pluck tuned teeth in a prescribed sequence, playing preset music. It demonstrates mechanical encoding and automated performance; it is not an equivalent device for recording an arbitrary complete waveform. The lecturer used it as an intuitive analogy for mechanical storage and reproduction. (2026-09-24 transcript from 02:02:05) [S04 PDF p.42]

### 4.14 Microphone Directionality: Reading and Selecting Polar Patterns

**Directionality.** Keep source sound pressure constant and vary the source direction relative to the microphone; the output can change. A polar pattern shows relative sensitivity at different arrival angles. Typically 0° is directly in front and 180° directly behind. On a dB-labelled polar plot, an inward position indicates a weaker response. Real directionality also varies with frequency, so one plot describes only particular conditions. [S04 PDF p.43–46]

- **Omnidirectional:** Ideally similar pickup in every direction. Suitable for people around a table or retaining ambient sound, but directionality itself does not reject surrounding noise/reverberation. A quiet studio is the slide example, not a restriction that omnidirectional microphones can be used only in studios.
- **Cardioid:** Sensitive in front with maximum rear rejection; the slide specifies 180°. Suitable for a lecturer/single presenter, reducing rear audience sound or loudspeaker spill. Both level and tonal quality can change if the source moves off-axis.
- **Supercardioid:** Narrower frontal coverage, but with a rear pickup lobe. Maximum rejection is away from directly behind. The slide gives approximately 120°; ideal patterns and particular models may have different angles, so placement should follow the measured polar plot. Do not interpret it as quieter than a cardioid at every rear angle.
- **Shotgun:** Highly directional, commonly using an interference-tube structure to cancel some off-axis sounds. Useful for targeted acquisition, but its performance varies with frequency/environment and does not eliminate all background sound at a distance.
- **Bidirectional / figure-eight, classroom addition:** Sensitive in front and behind, with side rejection; useful for a face-to-face interview. This comes from the lecturer's discussion of interviewing people on opposite sides, rather than an extra product omitted from p.45 that must be memorized separately.

**The lecturer emphasized matching the situation.** An omnidirectional microphone/array can suit a round-table meeting, a directional microphone can suit a single lecturer, and an interview must cover both host and guest. Coverage angle, noise-source position, frequency response, and related parameters matter, rather than simply choosing the most expensive item. A microphone pointed incorrectly may perform worse than a cheaper one selected appropriately. (2026-09-24 transcript from 02:02:05, later continuous discussion)

**Exam-ready answer.** A polar pattern describes microphone sensitivity as a function of arrival angle, normally relative to its on-axis response. An omnidirectional pattern suits sources around a table, whereas a cardioid helps isolate a presenter by attenuating sound from the rear. The appropriate pattern depends on source and noise geometry and varies with frequency.

### 4.15 Frequency Response, Gain, and Clipping: Captured Audio Can Still Be Unusable

**Ideal versus real behaviour.** An ideal microphone produces voltage proportional to pressure over the target frequency and pressure ranges, without arbitrarily changing the relative strengths of frequency components. Real microphones approximate this only over particular frequency/amplitude ranges. Slide p.46 also shows different frequency responses for different arrival angles. Frequency response describes sensitivity as a function of frequency. “Flat” means approximately even response within the target band, not a waveform that is always a straight line. [S04 PDF p.46]

**Excessive gain.** Analog output is amplified before entering the ADC. If preamplification/the ADC input exceeds full scale, peaks are cut off into flat tops, causing clipping/distortion. Lowering the volume later cannot restore the missing peak shape; it only makes the already clipped waveform smaller. [S04 PDF p.47]

**Insufficient gain.** The useful signal occupies only a small fraction of the ADC range. Weak variations can quantize to the same code, producing poorer signal-to-noise performance; substantial amplification later also amplifies the noise floor. Tiny variations can map to zero/the same level, but not every small signal necessarily becomes entirely zero. Appropriate gain uses the available range well while leaving headroom for unexpected peaks.

**Applying the parameters when choosing a microphone.** Consider the target band, polar pattern, permitted sound pressure/dynamic range, self-noise, output interface and power, front-end gain, and physical placement together. A high sampling rate cannot repair audio already clipped in the analog front end, nor remove every background sound captured by unsuitable directionality. [S04 PDF p.43–49]

### 4.16 AES42 Digital Microphones: Standardization and Limitations

The slides introduce AES42 digital output, using a standardized digital connection to supply acquisition data to an audiovisual backend. An example device supports configurable polar pattern, low-cut filtering at examples of 40/80/120 Hz, gain from unity to +63 dB, and mute. Understand digital transmission, interface compatibility, and configurable parameters. The options/numerical ranges illustrate particular equipment and are not capabilities that every digital microphone must provide in full. [S04 PDF p.48]

**What does low-cut mean?** It attenuates low-frequency energy to help reduce footsteps, wind/vibration, and air-conditioning rumble. The 40/80/120 Hz choices are different cutoff settings. A higher cutoff may remove more wanted low-frequency content. It does not mean “allow only 40 Hz to pass”. (Additional explanation)

**A precise reading of “No interference problem”.** Earlier digitization and a shorter vulnerable analog chain can reduce analog-cable interference and gain inconsistencies. A digital interface still faces practical issues such as analog front-end noise, overload, clocking, and transmission errors. Do not state that digital microphones have absolutely no noise or interference. AES42 compatibility is also not the only selection criterion or an automatic guarantee of best sound quality.

**One-sentence examination answer.** A digital microphone integrates conversion and uses a standardized digital interface, reducing some problems of analog signal transmission and enabling supported remote controls. Its quality still depends on the acoustic transducer, analog front end, sampling, gain settings and implementation.

## 5. Sound Reproduction, Speech, and Music: S05 PDF p.1–20

This section covers every page of the sound portion of S05. The available 2026-10-08 recording starts partway through a speech-recognition example and verifies some explanations for p.12–20. No separate, complete corresponding classroom segment for p.2–11 was found in the available recordings. Those pages are therefore explained from the complete slides and explicitly marked additional explanations; the document does not claim to have captured all the lecturer's original words for them.

### 5.1 Loudspeakers: Turning Electrical Signals Back into Pressure Waves

A speaker is the most common device for sound reproduction. Its conversion direction is the reverse of a microphone: an electrical signal drives diaphragm motion, pushing the surrounding medium to form pressure waves received by the ears. In a typical moving-coil loudspeaker, current through a voice coil in a magnetic field produces force and moves the diaphragm: “electrical → mechanical motion → sound”. A microphone instead follows “sound → mechanical motion → electrical”. Not every microphone/speaker is directly interchangeable in structure or efficiency. [S05 PDF p.2; the structural mechanism is an additional explanation]

Speakers also have directionality: the level received varies with direction and frequency. The figure's set of polar plots changes shape across six frequencies, showing why listener seats, speaker orientation, and coverage influence the result. Supplying the same file does not guarantee identical spectra and sound pressure at every seat.

**Exam-ready answer.** A loudspeaker converts electrical signal variations into diaphragm motion and pressure waves. It is the reproduction counterpart of a microphone and has frequency-dependent directionality, so placement affects the sound reaching a listener.

### 5.2 Speaker Characteristics: Power, Impedance, Frequency Range, and Crossover

**Rated power, W.** This relates to permitted electrical input and thermal/mechanical capacity. The slide simplifies it as the maximum input before damage. A precise answer should distinguish continuous/peak ratings and test conditions. Rated power does not fully describe loudness: sound pressure also depends on sensitivity, distance, frequency, enclosure, and distortion limits. A 100 W label does not imply that the speaker is louder or clearer than a 50 W speaker in every situation. [S05 PDF p.3]

**Impedance, Ω.** This is the AC load presented to the amplifier and normally varies with frequency. Nominal impedance helps assess amplifier compatibility. For example, a load below the amplifier's permitted impedance can draw excessive current. Impedance is measured in ohms, not Hz, mm, or watts, and is not simply the voice coil's fixed DC resistance at every frequency.

**Frequency range / response, Hz.** These describe the band the system reproduces under specified tolerances/conditions and the relative output at each frequency. An approximately flat response across a band means the speaker changes the original relative frequency strengths less. Upper/lower limits without a permitted deviation are insufficient to compare sound quality adequately.

**Crossover frequencies, Hz.** These are the handover regions where the input spectrum is divided among drivers. A low-pass filter supplies low frequencies to a woofer and a high-pass filter supplies high frequencies to a tweeter; a three-way system adds a middle band for a midrange driver. Real filters have slopes and overlapping responses. Amplitude, phase, and directionality must be handled at the crossover rather than imagining that every wave is mechanically severed at one exact point. [S05 PDF p.3–4]

### 5.3 Why Speakers Use Woofers, Tweeters, Subwoofers, and Enclosures

**Division of work among drivers.** Producing adequate pressure at low frequencies generally requires substantial air displacement, favouring larger diaphragms/greater excursion. High-frequency reproduction requires rapid response and control of radiation direction, favouring smaller, lighter diaphragms. The slide offers the intuitive explanation that a larger diaphragm has greater mass and suits low frequencies. The complete physics also involves area, excursion, resonance, stiffness, efficiency, and high-frequency beaming. Do not answer simply that large objects can only move slowly and small objects can only move quickly. [S05 PDF p.4; additional clarification]

**Units in the slide figure.** The 69 mm subwoofer, 40 mm drivers, and 20 mm super tweeters are driver dimensions in the example speaker, not crossover frequencies of “69 Hz, 40 Hz, and 20 Hz”. A passive radiator has no separately driven voice-coil input: pressure within the enclosure makes it vibrate, helping shape low-frequency output. It is not automatically another independent channel.

**The primary purpose of an enclosure.** Pressure produced by the two sides of a diaphragm is opposite in phase. If rear sound travels around to the front, it can cancel frontal radiation, particularly at low frequencies, reducing output. The enclosure separates front/rear radiation and controls rear acoustic energy. Sealed, vented/passive-radiator, and other designs also affect low-frequency response and resonance. An enclosure is more than a protective box. [S05 PDF p.5]

**Exam-ready answer.** A multiway loudspeaker divides frequencies among drivers suited to different bands. Large low-frequency drivers move more air, while smaller high-frequency drivers handle high-frequency radiation. The enclosure controls rear radiation and reduces front–rear cancellation, especially at low frequencies.

### 5.4 Surround Sound: What Do 5.1, 6.1, and 7.1 Mean?

Surround sound reproduces multiple channels positioned around the listener, providing directional and enveloping sound for a more realistic, engaging experience. [S05 PDF p.6]

- **5.1:** Five main channels, usually front left/right, centre, and surround left/right, plus one low-frequency-effects channel, LFE.
- **6.1:** The illustrated configuration adds a rear-centre channel to a similar arrangement.
- **7.1:** This commonly expands surround coverage into left/right side surrounds and left/right rear surrounds, together with three front channels and LFE. Follow the diagram's stated layout in a question.

`.1` denotes a bandwidth-limited LFE channel, not “0.1 of a loudspeaker”. The physical number of subwoofers need not equal the number of LFE channels in the soundtrack. Channels organize independent audio signals; drivers count physical hardware. Do not mix the two. (Additional explanation)

### 5.5 Virtual Surround: Recreating Directional Cues with ITD, ILD, and HRTF

Physical 5.1/6.1/7.1 installations can be difficult because of space, wiring, and placement. Virtual surround therefore aims to simulate a multispeaker enveloping effect with fewer physical devices. The slides list two configurations: 2.1 using two front speakers and a subwoofer, and digital sound projection using a strip of small drivers. [S05 PDF p.7]

**ILD, Interaural Level Difference.** A source closer to one ear, together with the head's acoustic shadow, produces different received levels at the two ears. The brain uses this difference to help determine left/right direction.

**ITD, Interaural Time Difference.** Different propagation distances to the ears produce arrival-time/phase differences. The brain uses these differences to help determine direction. This is distinct from the cue of one ear receiving a louder sound.

**HRTF, Head-Related Transfer Function.** The head, pinnae, torso, and related anatomy produce direction-dependent filtering, reflections, and delays. Pinna-related spectral shapes help distinguish front/back and up/down, resolving ambiguities left by ITD/ILD alone. HRTF is more than a change in loudness caused by an ear reflection: it describes the complete direction-dependent transfer from source to ear. [S05 PDF p.8]

**Implementation idea.** Apply filters, relative gains, and delays for the intended virtual source direction so the two ears receive approximately the cues expected from that direction. The listener may then perceive sound outside the actual speaker positions. A soundbar may also use an array and room reflections to form beams. Listener position, room reflections, left/right crosstalk, and mismatch with individual ear geometry can reduce performance. There is no guarantee that every seat experiences the equivalent of physical 7.1. (The implementation and limitations are additional explanations.)

**Exam-ready answer.** Virtual surround recreates spatial hearing cues with fewer physical loudspeakers. ITD is the interaural arrival-time difference, ILD is the level difference, and HRTF describes direction-dependent filtering by the head and ears. Appropriate delays, gains and filters can make the listener perceive a virtual direction, subject to listener and room conditions.

### 5.6 Speech Production: Fundamental Frequency, Vocal Tract, and Phonemes Are Different Concepts

**Basic production process: additional explanation.** Airflow from the lungs supplies energy. During voiced production, the vocal folds vibrate approximately periodically, supplying a fundamental and harmonics. Vocal-tract shape, including the tongue, lips, and oral cavity, changes resonances and gives phonemes different spectra. This is the source–filter intuition: source periodicity relates to pitch; filter resonances relate to formants. [S05 PDF p.9–10]

**Reference ranges in the slides.** The main information band of normal speech is approximately 80 Hz–5 kHz. Example pitch ranges are 120–160 Hz for adult men and 220–330 Hz for women/children. Vowel energy can extend to several kHz, and fricatives/sibilants have higher-frequency energy. These are illustrative/typical values, not fixed physiological limits for everyone. A person's 150 Hz fundamental does not mean that their entire speech contains only 150 Hz or needs a sampling rate of only 300 Hz.

**Preserve the level-measurement conditions.** The p.9 example is measured about 60 cm from the mouth: normal speech is approximately 60 dBA, with illustrative male/female yelling levels of about 76/68 dBA. Distance, speaker, and environment alter the readings. Do not memorize these as universal maxima. If a question concerns only speech mechanisms, these illustrative levels need not become the principal conclusion.

**Phoneme.** A basic speech unit capable of distinguishing word meaning in a language. Phoneme inventories differ among languages. The slides give examples by airflow-production mechanism: [S05 PDF p.10]

- **Stop consonants:** Airflow is first blocked and then released, as in English /p/, /t/, and /k/.
- **Fricative consonants:** Airflow through a narrow passage creates turbulence, as in /f/ and /v/. The slides subsequently discuss high-frequency sibilants such as /s/.
- **Approximants:** The tract narrows, but turbulence is weaker, as in /w/ and /r/.
- **Aspirates / breath-related examples:** The slide uses word-initial /h/, emphasizing an audible exhalation component. Do not conflate the linguistic feature of aspiration with every detail of the classification of /h/ here.
- **Vowels:** The tract is relatively open and airflow is not substantially blocked, as in /a/, /e/, /i/, and /o/. Mouth shape/tongue position still changes tract resonances; vowels do not imply the absence of filtering.

**Exam-ready answer.** Speech consists of phonemes produced by different configurations of the vocal apparatus. Voiced excitation contributes a fundamental frequency and harmonics, while the vocal tract shapes resonant energy bands. Stops, fricatives, approximants and vowels differ in how airflow is obstructed or allowed to pass.

### 5.7 Spectrograms, Formants, and Speech-Recognition Cues

**How to read a spectrogram.** Time is usually the horizontal axis and frequency the vertical axis; colour/brightness indicates energy at a frequency within a short time window. It combines temporal localization and frequency distribution. An ordinary spectrum showing one segment's frequency composition cannot directly replace a time-varying spectrogram. Short-time Fourier analysis is a common way to generate one; that method is an additional explanatory detail. [S05 PDF p.12–13]

**Formants.** Vocal-tract resonances concentrate energy in particular frequency regions. In vowels, these often appear as sustained/varying bright bands in the spectrogram, labelled F1, F2, and so on. They depend on tract shape and differ from **F0, the fundamental frequency** of vocal-fold vibration. The same vowel at a different pitch can change F0 while retaining similar resonance patterns; different vowels at the same pitch can have different formants. Do not call every harmonic a separate formant.

**Typical recognition cues from the slides.** [S05 PDF p.12]

- Voiced phonemes often show regular harmonics and concentrated resonance-energy bands.
- Stops often show a short silence/low-energy closure followed by a relatively broadband burst.
- Fricative/breath-related components often form continuous, diffuse noise-energy clouds, with prominent high-frequency energy in some fricatives.
- The slide's statement that unvoiced speech “has no formants” is a simplification for recognizing typical patterns. Noise excitation can also be filtered by the vocal tract; it is not an absolute rule that every real unvoiced segment completely lacks resonance traces.

**ASR mechanism framework.** Acquire and preprocess the signal, split it into frames/extract features, recognize acoustic/phoneme/word sequences through models, and combine linguistic context to output text. The lecturer compared spectrogram patterns with face feature vectors: similarity among patterns from the same kind of pronunciation can support classification, rather than requiring point-by-point identity of raw waveforms. (2026-10-08 transcript 00:00:01–00:01:16)

**Limitations.** A phoneme varies across people, accents, speaking rates, and contextual coarticulation. The same word can also have different pronunciations. The slide's “unique pattern for each phoneme” should therefore mean statistically distinguishable features, not a permanent, nonoverlapping barcode.

**Exam-ready answer.** A spectrogram shows how energy at each frequency changes over time. Formants are vocal-tract resonance bands that help distinguish voiced phonemes, while stops may show a burst after a closure and fricatives may show noise-like energy. Recognition compares such patterns with learned models and context rather than expecting identical raw waveforms.

### 5.8 Why Noise and Narrowband Telephony Make ASR Harder

**Noise does more than add to the signal.** In noisy surroundings, people increase loudness, change pitch, and lengthen/adjust syllables. A recognizer trained in quiet conditions therefore faces both additional background noise and changed speaking behaviour, creating a train–test mismatch. Reverberation, multiple speakers, and microphone response also change features. [S05 PDF p.14]

**Telephone sampling limitations.** Traditional narrowband telephony commonly uses 8 kHz sampling, giving Nyquist=4 kHz and a real speech bandwidth generally narrower than that. Distinctions involving high-frequency fricative/sibilant cues are weakened. Do not say that 8 kHz sampling preserves frequencies up to 8 kHz, or infer from an adult fundamental of only a few hundred Hz that all speech detail is retained. [S05 PDF p.14]

The slides/transcript mention very high-frequency components of /s/, /f/, and similar sounds, potentially above 20 kHz. A precise answer is that some distinguishing cues contain high-frequency energy that recording-bandwidth limits can remove. Do not state that these sounds exist entirely above 20 kHz and are therefore never audible to humans. Parts remain audible on the telephone, although distinguishing them can become harder. (2026-10-08 transcript 00:01:16–00:04:34)

**The whole-word spelling remedy.** Replace similar-sounding letter names with more distinguishable full words, for example “Alpha/Alfa, Bravo, Charlie…”. Increased redundancy and acoustic differences reduce mishearing. The slide also lists Beta, Frankie, Sugar, and other examples, a mixed illustrative vocabulary that should not be relabelled verbatim as the official NATO phonetic alphabet. If asked for the principle, explain replacing easily confused isolated letters with whole words; arguing about the particular spelling-alphabet version is unnecessary.

**Ways to improve recognition: additional explanation.** Training/adaptation on varied and noisy conditions, better microphone placement/arrays, noise reduction and dereverberation, greater effective speech bandwidth, and linguistic context can all help. Lost high-frequency physical information is not guaranteed to be faithfully restored simply because a model is “smarter”.

**Exam-ready answer.** Noise changes both the recorded signal and the speaker's articulation, creating a mismatch for a recognizer trained in quiet conditions. Narrowband sampling removes high-frequency cues important for some consonants. Whole-word spelling increases redundancy, while suitable capture and robust training improve recognition.

### 5.9 TTS, Dictation, NLP, and Actionable Intelligence

**Speech synthesizer / Text-to-Speech.** TTS converts text into audible speech, handling textual reading, pronunciation, rhythm/stress, and related issues before generating a waveform. The slide's Nuance example illustrates multilingual TTS support; it is not a requirement to memorize an old developer URL. [S05 PDF p.11]

**Dictation → NLP → action.** Dictation/ASR converts sound into text. Natural Language Processing interprets intent, entities, and context. Actionable intelligence turns that interpretation into an executable action. For example, after hearing “Remind me to submit the assignment at nine tomorrow”, the system transcribes the request, parses the time and task, and creates a reminder. Correct ASR text does not guarantee correct intent interpretation; execution also requires application interfaces and rules. This is the capability chain illustrated by the p.15 title. Speech recognition alone is not a complete intelligent assistant. [S05 PDF p.15; the pipeline example is an additional explanation]

### 5.10 Music: Pitch, Fundamental, Harmonic, Overtone, and Partial

Studying general properties of music signals supports audio compression, instrument detection, and music manipulation/synthesis. [S05 PDF p.16]

**Pitch** is perceived tonal height. For common periodic musical tones, it is mainly associated with the fundamental frequency F0/f0. F0 is not loudness. Increasing amplitude mainly affects loudness, whereas increasing the fundamental mainly raises pitch. Different instruments can produce the same pitch.

**A harmonic** is a frequency component at an integer multiple of the fundamental. If f0=440 Hz, 440 is the first harmonic/fundamental, 880 the second harmonic, 1320 the third, and 1760 the fourth.

**An overtone** is a partial above the fundamental. In a purely harmonic series, the first overtone is the second harmonic, not the first harmonic. **A partial** is any frequency component forming a complex sound; it need not be an integer multiple of the fundamental. For example, some percussion instruments have inharmonic partials. Do not replace this qualification with the claim that every overtone must occur at an integer multiple.

**Example.** The lecturer compared instruments playing middle C: they share approximately the same fundamental, about 262 Hz in the figure, but have different spectral structures beyond that fundamental, allowing their instruments to be distinguished. The A4=440 Hz table on p.16 and the middle C≈262 Hz figures on p.17 are separate examples. Do not label all of them “middle C=440 Hz”. (2026-10-08 transcript 00:05:02, 00:09:17–00:11:12) [S05 PDF p.16–17]

### 5.11 Timbre: Why Sounds Can Differ at the Same Pitch

**Timbre** is the sound quality that lets us distinguish different sources of sound production. The slides emphasize two types of cues: [S05 PDF p.17]

1. **Spectrum:** Which frequency components are present and their amplitudes. A flute is an example closer to fundamental-dominated sound, whereas a piano/trumpet has different harmonic proportions. Their waveforms and spectra therefore differ.
2. **Time envelope:** How overall level rises, falls, sustains, and disappears over time. Even with the same average spectrum, a different onset process can make a sound perceptually distinct.

“Same pitch”, “same loudness”, and “same timbre” are three different statements. For example, piano and trumpet middle C can share F0 while differing in harmonic strengths and attack/decay, retaining pitch but sounding different. An instrument recognizer that estimates only F0 loses many distinguishing features.

**Exam-ready answer.** Two instruments can play the same note because they share a fundamental frequency, while sounding different because their harmonic/partial spectra and temporal envelopes differ. Pitch is mainly associated with the perceived fundamental, whereas timbre describes these source-specific qualities.

### 5.12 The Four ADSR Stages: What Does Each Letter Control?

ADSR describes typical amplitude evolution using a piecewise envelope: [S05 PDF p.17, 19]

- **Attack:** From onset to peak. A fast attack resembles the sharp onset of a strike/pluck; a slow attack resembles a soft synthesized sound gradually entering.
- **Decay:** The decrease from the initial peak to the sustain portion.
- **Sustain:** The level maintained while sound production/the note is held. In common synthesizers, sustain primarily denotes a level, whereas A/D/R usually denote durations. This does not mean every real instrument has a strictly constant-volume stage.
- **Release:** The descent to zero after excitation stops/the key is released. A short release ends quickly, whereas a long release produces a tail.

**Drawing it in an examination.** Put time on the horizontal axis and amplitude on the vertical axis. Draw rising A, falling D, held S, and finally falling R. Mark the point where the key is released/excitation stops. Do not confuse release with the decline immediately after the attack peak; that decline is decay.

**Limitations.** ADSR is a useful parametric approximation, not an exact four-line fit for every real instrument. A piano naturally decays even while the key is held; guitar plucking, sustained violin bowing, and a held wind-instrument tone have different envelopes. The lecturer used guitar excitation–vibration–disappearance to explain this temporal process. (2026-10-08 transcript from 00:11:12)

### 5.13 Three Instrument Groups and Their Excitation Methods

**String instruments.** Vibrating strings produce sound. Plucking, bowing, striking, and other excitation methods change overtone composition and envelope. A plucked guitar and continuously bowed violin can have different timbres even at the same pitch. A piano strikes strings with hammers, illustrating that “striking as excitation” and “strings as the primary vibrating body” are different classification perspectives. [S05 PDF p.18]

**Wind instruments.** Blowing excites an air column/resonator. Tube length, holes, and excitation structures affect available resonance frequencies and spectral shape. Flutes, clarinets, and other instruments can share a fundamental while differing in harmonic distributions.

**Percussion instruments.** Striking, shaking, rubbing, scraping, and related actions excite a membrane, plate, or other structure. Some have definite pitch; others contain many partials that are not integer multiples. Do not describe all percussion as random noise with no frequency structure.

**Application.** Instrument detection needs spectral, temporal, and transient cues. Synthesis can model the vibrating body/excitation and temporal envelope. The three groups help explain sound-production mechanisms; simply memorizing three names is insufficient.

### 5.14 Music Synthesis: Generating Instrument-Like Sound from Parameters

The slides introduce physical modelling, harmonics and waveform envelopes, and incorporating original instrument samples. [S05 PDF p.19–20]

**Component-based intuition.** Generate waves of different shapes/frequencies, shown as sine, square, sawtooth, and triangle waves, combine them in suitable proportions to create a fundamental and harmonics, and apply ADSR to change amplitude over time. A simplified additive-synthesis expression is `x(t)=e(t) Σ Ak cos(2πk f0 t+φk)`, where e(t) is the envelope and Ak controls the kth harmonic strength. Square and sawtooth waves already contain multiple harmonics: their spectra differ as well as their visible shapes. (The formula is an additional explanation.)

**Physical modelling.** Simulate the dynamics of strings, tubes, membranes, excitation, and damping so that parameters correspond to the mechanisms of real sound sources. This is a different modelling route from manually adding a few sine waves. The slide lists these related ideas closely as an overview; they should not be mistaken for exact synonyms.

**Sampling / wavetable.** Record real instrument segments, organize them by pitch, velocity, or other parameters, and play, transpose, or join them to produce output. Strictly, a wavetable is a table-addressable waveform/cycle or sequence of such waveforms; it is not synonymous with every complete sample library. The shared idea is using stored real/synthetic waveforms rather than calculating all physical behaviour from scratch each time. (The terminology refinement is an additional explanation.)

**Hatsune Miku example.** Slide p.20 uses Hatsune Miku to illustrate singing synthesis: original pronunciation material can be organized and processed to produce new singing. Understand the relationships among sampling, pitch/duration/concatenation, and synthesis. Do not infer that the character personally sang every generated song in full, or treat the example as a requirement to master every internal algorithm of that software. (2026-10-08 transcript 00:11:12–00:15:56)

**Exam-ready answer.** Music synthesis generates sound using signal models, physical models or stored waveforms/samples. Fundamental frequency sets the intended pitch, the relative spectral components shape timbre, and an envelope such as ADSR controls its time evolution. Combining these controls can produce different instrument-like sounds.

### 5.15 Integrated Answer Examples for Acoustics, Speech, and Music

**Question: If a recording is too quiet, will increasing the sampling rate solve it?** Answer: Generally no. A low level means the useful signal does not use the ADC range sufficiently. Check microphone placement, sensitivity, and preamplifier gain. Increasing fs adds temporal samples without directly amplifying quantized amplitude or restoring front-end SNR. Use suitable gain with headroom. Greater bit depth can reduce quantization step size but cannot remove existing analog noise either.

**Question: Why do a piano and a flute sound different at the same 262 Hz?** Answer: A shared fundamental gives similar pitch. Different relative harmonic/partial strengths and the temporal forms of attack, decay, sustain, and release produce different timbres. Equal F0 does not mean equal complete spectra.

**Question: How should one microphone be chosen for an entire conference table and another for a lecture?** Answer: Since sources around a table arrive from many directions, an omnidirectional microphone or suitably covering array is appropriate. For a lecture, a correctly oriented cardioid can emphasize the presenter and reduce rear interference. Also check frequency response, distance, sound pressure, room reflections, and gain; superiority cannot be inferred only from price or the dynamic/condenser category.

**Question: Why can two front speakers create the impression of a source behind the listener?** Answer: Hearing depends on interaural time/level differences and HRTF spectral cues. Virtual surround recreates these differences for a target direction, potentially using arrays/room reflections as well. Performance depends on position, room, and individual HRTFs. Few physical speakers do not imply an absence of spatial audio cues.

**Question: Why are isolated letters easy to mishear over the phone, while whole-word spelling is more reliable?** Answer: Narrowband transmission/sampling weakens some high-frequency consonant cues. Noise and pronunciation variation add confusion. Replacing isolated letters with more distinct, redundant full words reduces errors. Explain information and bandwidth rather than claiming that telephones remove all consonants.

### 4–5 Page-by-Page Sound Coverage Check and Corrections

The following is a writing checklist to detect omissions where a heading might otherwise lack explanation. It is not a lecturer-published list of examination topics.

- **S04 p.1–4:** Title; sensor definition; three purpose groups; five senses. See 4.1.
- **S04 p.5–7:** Touch, resistive/capacitive/pressure sensing, 3D Touch, actuator/Taptic. See 4.2.
- **S04 p.8–11:** Artificial visual input, CCD/CMOS, resolution, and identification/spatial/memory/action elements of “spot the difference”. See 4.3.
- **S04 p.12–15:** Binocular vision, stereogram methods and illustrations. See 4.3.
- **S04 p.16–17:** Ears, microphones, dynamic/condenser mechanisms, and product illustrations. See 4.4. Product rankings/models are not treated as general knowledge.
- **S04 p.18–22:** Smell/taste, other species, health sensors, older-person care, environmental sensors, and spatial disorientation. See 4.5.
- **S04 p.23–24:** Dynamic range, offset, nonlinearity, and hysteresis. See 4.6.
- **S04 p.25–30:** LEGO analogy, waveform decomposition, and sinusoidal projection of circular motion. See 4.7.
- **S04 p.31–33:** Sampling, quantization, error, bit depth, and sampling rate. See 4.8–4.9.
- **S04 p.34:** Nyquist boundary, phase counterexample, and different analog waves with the same samples. See 4.9. The original equation figure was inspected.
- **S04 p.35:** Mechanical sound waves, media, sound speed, and reference hearing ranges. See 4.9–4.10.
- **S04 p.36–37:** Original SPL formula, reference pressure, subjective nonlinearity, and A-weighting. See 4.11. The original equation figure was inspected.
- **S04 p.38–40:** Echo, reverberation, and interference. See 4.12.
- **S04 p.41–42:** Mechanical recording on a tinfoil cylinder and the eighteen-note music box. See 4.13.
- **S04 p.43–46:** Microphone definition/diaphragm, directionality, polar plots, four directional patterns, and frequency response/angles. See 4.14–4.15. The polar and frequency-response figures were inspected.
- **S04 p.47–49:** Amplification, clipping, weak signals, AES42, configurable parameters, hearing range, and 44.1/48/96 kHz. See 4.9 and 4.15–4.16.
- **S05 p.1–5:** Title, speaker mechanism/directionality, power/impedance/crossover/frequency range, dimension figure, and enclosure. See 5.1–5.3.
- **S05 p.6–8:** 5.1/6.1/7.1, virtual surround, 2.1/arrays, and ILD/ITD/HRTF. See 5.4–5.5.
- **S05 p.9–10:** Reference speech/pitch/level values, five production groups, and phonemes. See 5.6.
- **S05 p.11–15:** TTS example, spectrogram/formants, illustrations, ASR limitations/whole-word spelling, and the NLP/action chain. See 5.7–5.9.
- **S05 p.16–18:** Music-processing objectives, F0, harmonic/partial/overtone table, timbre/spectrum/ADSR, and instrument groups. See 5.10–5.13.
- **S05 p.19–20:** Synthesis approaches, four waveforms, ADSR diagram, and Hatsune Miku. See 5.14.

**Ambiguities explicitly corrected in this rewrite.** ① Distinguish Nyquist frequency=fs/2 from Nyquist rate=2B. ② fs=2B does not unconditionally guarantee reconstruction for every boundary-phase case. ③ The slides' 12/20 Hz and 20/22 kHz hearing limits are different approximations; 44.1 kHz is not a human audible frequency. ④ Do not insert age/sex into the basic BMI formula. ⑤ Do not define offset through standby battery consumption. ⑥ Distinguish hysteresis from drift. ⑦ The 0.1 s echo value is an empirical scale. ⑧ The SPL reference is not absolute silence, and dBA does not make a logarithmic scale linear. ⑨ Supercardioids have a rear lobe, and 120° is the slide's approximation. ⑩ AES42 does not guarantee freedom from all interference, and example setting ranges do not describe every standards-compliant device. ⑪ For speakers, mm measures dimensions, Hz frequency, Ω impedance, and W power. ⑫ Voice F0 is not the highest speech frequency, and formants are not F0/individual harmonics. ⑬ Partials can be inharmonic; the first overtone in a harmonic series is the second harmonic. ⑭ Sustain usually denotes a held level, and physical modelling/additive synthesis/sampling/wavetables are not exact synonyms. These clarifications preserve both the slides' simplifications and precise definitions.
## 6. Light, Image Capture, Displays and Human Vision (S05 PDF p.21–62)

### 6.1 What Is Light? Amplitude, Frequency, Phase and Polarization

**Light is an electromagnetic wave.** The slides use an approximate visible wavelength range of 400–780 nm. Human sensitivity falls gradually near the boundaries; they are not hard limits identical for everyone. The speed of light in vacuum is `c = 299,792,458 m/s ≈ 3.00×10^8 m/s`. Wave speed, frequency and wavelength satisfy `v = fλ`, or `c = fλ` in vacuum. A shorter wavelength therefore means a higher frequency. For example, light of wavelength 600 nm has a vacuum frequency of approximately `3×10^8 / (600×10^-9) = 5×10^14 Hz`.

A single-wave model helps distinguish three quantities: amplitude describes the magnitude of electric-field variation; frequency/wavelength relates to color; phase describes progress through a cycle. **Precision note: light intensity is related to the square of electric-field amplitude. Amplitude cannot be treated directly as lux, and mixed light does not necessarily have one unique wavelength.** White light normally combines multiple wavelengths; the eye's response to the spectrum also determines the resulting color experience.

**Coherence** describes whether the phase relationship between waves remains stable. The many emission processes in an ordinary light source generally do not maintain stable mutual phase relationships; the slides call this non-coherent. A laser is a typical coherent-light example. Coherence does not mean zero phase difference between every wave at every location; the important property is an ordered, stable relative phase relationship. Ordinary imaging and human vision generally detect time-averaged intensity rather than directly reading the electromagnetic wave's instantaneous phase.

**Polarization** concerns the orientation of a light wave's electric-field oscillation. Unpolarized light has no fixed orientation relationship; a polarizer selectively transmits particular polarization components. Polarized sunglasses can suppress some reflected glare; LCDs combine liquid crystals and polarizers to control transmission; stereoscopic cinema can deliver differently polarized images to the two eyes.

**Common confusion:** separating left/right images with different colored filters is anaglyph stereoscopy; separating them with different polarization directions is polarized stereoscopy. The classroom ASR's mention of “blue/green glasses” is not a definition of polarization. Color and polarization are different optical properties.

**Answer template: Why do wavelength, phase and polarization matter?** Wavelength is associated with spectral color; phase relationships determine coherence and interference; polarization describes the orientation of the electric field and can be used to filter light or separate the left-eye and right-eye images.

Sources: [S05 PDF p.21–23]; [T08 00:16:29–00:22:25]. The wave-speed and squared-amplitude relationships are interpretive supplements.

### 6.2 Candela, Lumen and Lux: Direction, Total Output and Per-Unit-Area Illumination

These three units answer different questions and are not interchangeable.

- **Luminous intensity, candela (cd):** how much visible luminous flux a source emits per unit solid angle in a particular direction. It is useful for directionality and the strength of emission along a direction. It is not the illuminance actually received by an observer or surface.
- **Luminous flux, lumen (lm):** the total visible-light output over a specified angular range or all directions. When buying a bulb, lumens compare light output more directly than electrical power alone; different technologies can produce similar lumens with different power consumption.
- **Illuminance, lux (lx):** the luminous flux incident on a receiving surface per unit area. It describes desk lighting, shooting conditions and the environment associated with a camera's minimum-illumination specification. It is not the camera's quantum efficiency or intrinsic sensitivity itself.

**Solid angle, steradian (sr):** a two-dimensional angle in radians measures arc length relative to a circle's radius; a three-dimensional solid angle measures covered area on a sphere. With the sphere's center as the vertex, a covered spherical area `A` and radius `r` give `Ω = A/r²`; a complete sphere subtends `4π sr`. The area must be on the spherical surface. A small planar receiving surface normal to the rays can be used as an approximation.

Slide relationships: `1 lm = 1 cd·sr`; for uniform intensity over the angular region, `Φv = Iv Ω`. A source uniformly emitting 1 cd in every direction has total flux `4π lm`. For uniform illuminance, `E = Φv/A`, so `1 lx = 1 lm/m²`. In general, total source flux requires integration over the directional intensity distribution; an arbitrary directional cd value cannot unconditionally be multiplied by `4π`.

**Complete calculation from the diagram on slide p.26:** a small `50 mm × 50 mm` sensor is 2 m from a point source, faces it normally, and receives 0.1 W. Convert the area: `A = 0.05×0.05 = 0.0025 m²`. The approximate solid angle is `Ω = A/r² = 0.0025/4 = 0.000625 sr`. Radiant intensity is `Ie = P/Ω = 0.1/0.000625 = 160 W/sr`. **This is a radiometric answer in W/sr, not candela.** Conversion to cd requires the spectrum and weighting by human spectral sensitivity; watts alone are insufficient. This example is easy to miss in text-only extraction.

**Slide p.29 example:** 1000 lm spread uniformly over 1 m² gives 1000 lx; the same flux over 10 m² gives 100 lx. Equal lumens do not mean equal lux when the illuminated areas differ.

Slide p.27 gives the monochromatic-light explanation of candela: at `540×10^12 Hz`, a radiant intensity of `1/683 W/sr` in the specified direction corresponds to 1 cd. The 683 factor and specified frequency connect photometry with human visual sensitivity. In an exam explanation, distinguish the three quantities first; do not define total energy, illuminance and directional intensity as the same thing.

**Illustrative illuminance levels in the slides:** moonlight may be about 1 lx, an office about 320–500 lx, a television studio about 1000 lx, and strong midday sunlight about 130,000 lx. These are contextual estimates affected by weather, surface orientation, distance and obstruction. They refer to illuminance on a receiving surface. The slide's simplified phrase about the Moon “emitting lux” must not be taken to mean lux measures a source's total output.

**Answer template: Compare cd, lm and lx.** Candela measures luminous intensity in a particular direction; lumen measures luminous flux over a solid angle or all directions; lux measures the flux incident per unit area. Their relationships are `lm = cd·sr` and `lx = lm/m²`. The same lumen output can give different lux values when spread over different areas.

Sources: [S05 PDF p.24–29]; [T08 00:24:18–00:35:08]. The transcript repeatedly recognizes candela as “camera” and lumen as “woman”; both are corrected using the slide terminology.

### 6.3 Reflection and Refraction: How a Camera Forms an Image

**Reflection:** light reaches a surface and returns into the original medium. The incident ray, reflected ray and surface normal lie in one plane. The angle of reflection equals the angle of incidence, both measured from the normal. Specular reflection preserves a definite direction; diffuse reflection distributes light over multiple directions because of microscopic surface orientations. A concave mirror can converge suitably directed rays, whereas a convex mirror provides a wider field of view. Do not assign the same geometric action to every mirror shape.

**Refraction:** light changes propagation speed when entering another transparent medium, usually changing direction as well. Across a stationary interface, frequency remains unchanged while wavelength changes with speed. Lenses and eyes use refraction to focus rays from different directions onto an imaging surface. Interpretive supplement: `n1 sinθ1 = n2 sinθ2` and `n = c/v`. At normal incidence, speed can change without a directional change; entering a new medium does not always mean the ray must bend.

**Why this matters to computer vision:** transparent objects refract the background, and mirror-like objects reflect the environment. Pixel colors and contours therefore need not directly represent the object's own material or location. Detection and 3D reconstruction methods assuming opaque, approximately diffuse surfaces may fail on glass, mirrors and highlights. Conversely, graphics rendering must model reflection and refraction to make synthetic scenes look natural.

**Answer template: How does refraction help image formation?** A lens changes ray directions at its surfaces because light travels at different speeds in different media. Properly shaped lens surfaces bring rays from a scene point toward the corresponding image location, forming a focused image on the film, electronic sensor or retina.

Sources: [S05 PDF p.30–32]; [T08 00:36:02–00:40:58].

### 6.4 From Camera Obscura to Digital Images: Projection, Recording and Two Aspects of Image Formation

A **camera obscura** projects an external scene into a dark enclosure through an aperture or optical arrangement. It can form an image but does not inherently contain a recording medium that preserves it. Early photosensitive paper and film preserve images through light-induced chemical changes; the slides use silver-chloride-coated paper darkening under light as an example. A digital camera converts light into electrical signals, then digitizes, processes, encodes and stores them.

Image formation answers two distinct questions: **geometry determines where a scene point projects; optics/physics determines the brightness and color at that position.** An object's image position depends on camera pose, lens and distance; pixel values also depend on illumination, surface reflectance, occlusion, exposure and sensor response. Altering the lighting can change an object's pixel brightness substantially without changing its geometric position.

**An interpretive perspective-projection model:** using a virtual upright image plane equivalent to the actual inverted image, a point `(X,Y,Z)` in camera coordinates projects as `x = fX/Z`, `y = fY/Z`. Here `f` is focal length and coordinate units must be consistent. An actual image plane on the opposite side of the optical center produces a sign reversal. An equally sized object farther away projects smaller because projected size scales with `1/Z`. Projection maps a 3D point to a 2D location and loses depth information; one image generally cannot uniquely determine actual depth directly.

**Three exposure controls and their trade-offs (classroom supplement):** aperture changes light entry and depth of field; a longer exposure generally accumulates more light but increases motion-blur risk; higher ISO/output gain brightens the output and may amplify noise without creating more already captured photons. More pixels alone do not ensure better low-light photographs.

Sources: [S05 PDF p.33–36]; [T08 00:36:32–00:42:06]. The projection formula interprets the p.36 diagram. Exposure trade-offs are interpretive supplements connected to the low-light examples in S03.

### 6.5 CCD and CMOS: Comparing Light Sensing and Readout Structures

Both use pixelated semiconductor photosensor arrays to convert incident light into charge or electrical signals. In a typical **CCD, charge-coupled device**, accumulated pixel charges are transferred successively through shift registers to output amplification and charge-to-voltage conversion circuitry. A typical active-pixel **CMOS, complementary metal-oxide-semiconductor**, structure performs conversion near each pixel, supports row/column selection and readout, and more readily integrates control circuits onto the sensor.

The slide table compares successive charge transfer versus direct addressing; charge-to-voltage conversion after readout versus within the pixel; whole-frame versus row-sequential exposure/readout; sensitivity; and off-chip versus on-chip control circuits. These structural differences help explain trade-offs in integration, readout, noise and cost.

Specifically, the exposure row on p.38 states single frame/field exposure for CCD and single frame/line sequential exposure for CMOS. The latter includes different whole-frame or line-sequential arrangements; do not memorize “CMOS must expose one row at a time.”

**Precision note:** the slide's summary that CCD has better low-light performance while CMOS is less sensitive is not a universal ranking across all generations and chips. Pixel size, quantum efficiency, read noise, manufacturing technology and the complete system also affect performance. CMOS must not always be equated with rolling shutter, nor CCD with the absence of every scanning-related issue under all conditions. Interpretive supplement: row-sequential exposure/readout records a moving subject at different times in different rows and can cause rolling-shutter distortion.

**Answer template: Compare CCD and CMOS sensors.** Both convert light into electronic signals with a pixel array. A typical CCD transfers accumulated charges through shift registers to an output amplifier, whereas a typical CMOS sensor supports pixel addressing and local conversion with integrated control circuitry. Their performance depends on implementation; low-light quality cannot be judged from the family name alone.

Sources: [S05 PDF p.37–38]; [T08 00:42:06–00:46:17].

### 6.6 Pixels, Resolution, Aspect Ratio and Frame Rate

A **pixel** is a discrete sampling location in a digital image, which contains `width W × height H` pixels. Megapixels are `MP = WH/10^6`; for example, `1920×1080 = 2,073,600 ≈ 2.07 MP`. More pixels usually provide denser spatial sampling, but resolvable detail also depends on lens quality, noise, focus, motion blur and other factors.

**Aspect ratio**, `W:H`, describes shape rather than pixel count. `640×480` is 4:3; `1280×720`, `1920×1080` and `3840×2160` are 16:9. Two images can share an aspect ratio while having different resolutions, or have similar pixel counts but different shapes. **Do not claim that every modern phone/computer screen must be 16:9.** The slides compare common formats.

**Video** is a sequence of images ordered in time. **FPS, frames per second**, states how many frames are recorded/displayed each second and describes temporal sampling density, while resolution describes spatial sampling density. Higher FPS generally represents rapid motion more continuously but does not automatically sharpen each individual frame. Exposure duration also differs from frame interval: at 30 fps, the frame interval is approximately 33.3 ms, but each frame can still use a 1/1000 s exposure. Video normally also includes audio, timestamps and coding/container information.

**How to use the slide numbers:** “photos up to 32 MP, video up to 16 MP” on p.40 belongs to the device-example context, not a theoretical limit of digital imaging. Transcript statements such as “DVD is 1280×720” and “Full HD is 1920×1020” are unreliable. Use 720p=`1280×720`, Full HD=`1920×1080`, and common UHD 4K=`3840×2160` as format examples. Other standards also use the term 4K; if a question provides explicit width and height, calculate from those values.

Sources: [S05 PDF p.39–40]; [T08 00:46:17–00:53:13]. Complete data-size examples appear in the later calculation chapter.

### 6.7 Stereo Cameras, Multiple Cameras, ToF, Folded Optics and Hand Tracking

**Stereo camera:** two cameras separated by a baseline view the same scene from different positions. The difference between corresponding object positions in the left/right images is disparity. Given the camera geometry, matched points and triangulation estimate depth. The basic pipeline is calibration/alignment, left/right correspondence matching, disparity calculation and conversion to depth. Interpretive supplement: in an ideal parallel stereo model, `Z = fB/d`, with baseline `B` and disparity `d`. When `f` and `d` both use pixels, `Z` and `B` share a length unit. Smaller disparity generally means greater distance; incorrect correspondence, occlusion and textureless regions affect the result.

**Why a phone has multiple cameras:** different focal lengths and fields of view cover ultrawide, main-camera and telephoto needs; stereo or other auxiliary sensors can support depth estimation and background blur. Images may be fused with appropriate calibration and algorithms. More lenses do not automatically mean summed pixel counts or better pictures: viewpoints, exposure, color and alignment differ between cameras.

**Time-of-Flight, ToF, sensor:** actively emits a known light signal and measures the reflected light's delay or modulation-phase change to estimate distance and form a depth map. The p.44 diagram shows active near-infrared illumination → pixel-array reception → A/D and depth processing → depth/amplitude map → application. Interpretive supplement: for direct round-trip timing, `Z = cΔt/2`. Division by 2 accounts for outward and return travel; a 20 ns round trip gives approximately 3 m. Indirect ToF estimates distance from modulation phase; not every device directly times individual pulses. Reflectivity, multipath, strong ambient light and measurement range affect results.

**Folded optics / periscope optical path:** prisms or reflective elements redirect the optical path so that a longer path fits within the phone's plane, accommodating thinness while supporting a longer equivalent focal length. This changes optical layout; software enlargement of a low-detail image is not optical telephoto imaging.

**Leap Motion:** the slides use it as an example of contactless hand/gesture sensing. The diagram includes infrared illumination and multiple infrared cameras; hand observations are processed into spatial hand/finger poses that drive interaction or a virtual-hand display. Sensing is the measured input, while the virtual hand on screen is the processed result. It is not directly placing the real hand inside the screen. Occlusion and effective sensing range limit tracking.

**Answer template: Stereo vs ToF.** Stereo estimates depth from geometric disparity between different viewpoints, while ToF actively illuminates the scene and estimates distance from the returned light's timing or modulation phase. Stereo relies on reliable correspondence; ToF is sensitive to illumination, reflections and multipath effects.

Sources: [S05 PDF p.41–46]; [T08 00:53:13–00:55:20]. Algorithms and formulas interpret the diagrams; sections that merely illustrate devices are not expanded into detailed hardware specifications that were not taught.

### 6.8 Additive and Subtractive Color: Why Displays Differ from Paper

**Additive color:** active sources emit different colored light, which combines in the eye to produce color. Zero RGB components produce black; an appropriate combination of all three produces white at the specified white point and sufficient output. Displays commonly work this way.

**Subtractive color:** ambient light reaches a surface; pigments/ink selectively absorb some light and the remainder reflects to the eye. Without illumination, paper cannot display like a self-emissive screen. Printing commonly uses cyan, magenta and yellow plus black, K, for more stable and economical blacks and detail. More ink generally means less reflected light, the opposite direction to adding RGB emissions.

**E Ink, a classroom example:** typical electronic-ink displays in Kindle-like readers mainly modulate reflected light, unlike self-emissive OLED. A reader with a front light adds illumination to its display surface. Therefore, a reader appearing bright in the dark does not prove that every pixel emits light like an OLED pixel.

**Application question: Why does a printed image look different from the display?** The display combines emitted light, whereas printed paper selectively absorbs and reflects ambient light. They have different primaries, gamut, white points, illumination and device response. Therefore the same numeric-looking color description is not enough to guarantee the same appearance across the two devices.

Sources: [S05 PDF p.47]; [T08 color explanation after 00:55:20, E Ink example at 00:59:51].

### 6.9 CRT, LCD, OLED, Autostereoscopic Displays and the “Hologram” Example

**CRT, cathode-ray tube:** an electron gun emits a beam, a deflection system controls the scanning location, and the beam excites phosphors on the screen. Beam intensity controls brightness at the corresponding location; color CRTs use the appropriate colored phosphor structures. The image forms through scanning and phosphor emission, not simply a set of independent miniature lamps.

**LCD, liquid-crystal display:** a typical transmissive LCD uses a backlight, polarizers, a liquid-crystal layer and color filters. An electric field alters liquid-crystal orientation, controlling transmission through the crystals and polarizers to produce subpixel brightness. The liquid crystal mainly modulates light rather than emitting it. The slide compares TN and IPS arrangements to illustrate different molecular/electric-field geometries and control methods.

**OLED, organic light-emitting diode:** an electric current drives an organic layer to emit light, with individually controlled pixels. The AM in AMOLED means active matrix, the driving arrangement. Unlike a typical LCD, OLED needs no shared backlight and can create black by turning the relevant pixels off. Interpretive supplement: this permits high contrast, but the structure alone does not prove lower power in every image or identical lifetime across devices.

**Autostereoscopic display:** the slide uses a parallax barrier to route light from different pixels to the left and right eyes, providing distinct views and stereoscopic depth without glasses. The limitation is the set of preferred viewing positions, or sweet spots. Moving outside the required angles can cause blur, crosstalk or incorrect views, and some spatial resolution/brightness may be sacrificed.

**The “3D Hologram” example:** p.52 shows the Gatebox virtual-character display. The page supplies no wavefront-recording or interference-reconstruction algorithm. Understand it as an example of presenting a virtual character through a visually three-dimensional interface; the marketing term alone does not prove holographic reconstruction in the strict physical sense. Interpretive supplement: strict holography records and reconstructs optical wave information and should be distinguished from ordinary 2D video/reflection demonstrations that appear to float.

**The classroom VR/AR distinction:** VR primarily places the user in a computer-generated virtual environment; AR overlays virtual information on perception of the real environment. These are modes of presentation and interaction, not a single panel material. LCD and OLED can both serve different virtual/augmented display systems. [T08 01:03:39–01:04:07]

**Answer template: Compare LCD and OLED.** A typical LCD modulates a backlight using liquid crystals and polarizers; an OLED pixel emits light when electrically driven. The key distinction is light modulation versus per-pixel light emission. Autostereoscopic presentation is a separate question about routing different views to the two eyes.

Sources: [S05 PDF p.48–52]; [T08 display-device discussion approximately 00:59–01:04]. The working-principle explanations interpret the device diagrams in the slides.

### 6.10 Three Main Parts of the Eye, and Cones/Rods

The **iris** adjusts pupil size to control incoming light; the **lens** participates in focusing; the **retina** contains photoreceptors that convert light through physiological processes into signals used by the nervous system and carried along the optic nerve to the brain. The camera analogy is useful: iris/pupil controls light entry, the eye's optical system corresponds to a lens, and the retina to a photosampling array. Subsequent interpretation by the brain is not simply storing a photograph.

**Cones and photopic vision:** the slides estimate about 6–7 million cones, with high density near the fovea. They support color and fine detail in bright conditions. High central density and less pooling of signals support spatial acuity. Interpretive supplement: color depends mainly on comparing responses of cones with different spectral sensitivities; one “red pixel” does not accept only one exact red wavelength.

**Rods and scotopic vision:** the slides estimate approximately 75–150 million rods, abundant away from the foveal center. They are highly sensitive in dim light and mainly provide brightness/overall-scene information, not the same color detail as cones. Pooling multiple receptors into downstream pathways improves sensitivity but sacrifices precise spatial localization. This is an explanatory simplification, not a complete neural wiring diagram.

**Read the distribution plot:** cones have very high density at the center; this is not where rods are most numerous. The optic disc lacks photoreceptors, producing the physiological blind spot. “Rods are uniformly distributed across the retina” and “more total cells automatically mean higher spatial resolution” are both incorrect answers.

**Answer template: Compare cones and rods.** Cones support color and fine-detail vision under bright conditions and are densely concentrated near the fovea. Rods are more sensitive in dim light, are abundant away from the foveal center, and provide coarser, largely achromatic information. Greater pooling improves sensitivity at the cost of spatial detail.

Sources: [S05 PDF p.53–55]; [T08 01:04:55–01:12:15]. Counts are slide estimates, not exact totals applying to every individual.

### 6.11 Foveal Acuity, Eye Movements and Foveated Rendering

**Know the slide's foveal estimate:** approximate the roughly 1.5 mm-diameter fovea as a `1.5 mm × 1.5 mm` square array. At about `150,000 cones/mm²`, this gives `1.5×1.5×150,000 = 337,500 ≈ 337,000` receptors. This is a **square approximation** used for the camera-array analogy, not a circular-area formula. A circle of diameter 1.5 mm would give a different result. The slide also compares this raw sample count with a roughly 5 mm×5 mm medium-resolution CCD, but equal receptor counts do not make the complete visual system and camera equivalent.

**Why the eyes continually move while viewing a scene:** the highest spatial acuity occupies only a small central region. Saccades bring important objects into central vision, fixations collect local information, and the brain integrates a scene using task and prior knowledge. Different tasks produce different eye-movement paths on p.57, showing that observation is not a uniform scan of every pixel. Task/prior knowledge influences sample locations, corresponding to the Neisser perceptual cycle.

**Foveated rendering, a classroom supplement:** eye tracking estimates gaze location, keeps high rendering resolution there and uses lower detail in the periphery. It exploits non-uniform vision to reduce computation, bandwidth or energy while preserving perceived quality. It may change only rendering sample density, without rearranging physical display pixels. Accurate, low-latency tracking is essential; otherwise eye movement exposes low-detail areas or blurred boundaries.

**Answer template: Why is eye tracking useful in VR?** It estimates the gaze location so that the system can allocate high rendering quality to the foveal region and reduce peripheral work. This exploits the non-uniform spatial acuity of human vision to save computation and energy while preserving perceived detail near fixation.

Sources: [S05 PDF p.56–57]; [T08 01:14:22–01:20:57].

### 6.12 Subjective Brightness, Background Contrast and Brightness Adaptation

**Physical intensity differs from perceived brightness.** The slides relate subjective brightness to a logarithmic response to incoming intensity, emphasizing that perception is not simply linear. The three central squares on p.58 can have the same physical gray level but look different against black, gray and white backgrounds. Visual interpretation therefore depends on relative contrast and surroundings. The center pixel value alone cannot predict appearance in every context.

**Brightness adaptation:** the visual system changes its overall sensitivity to operate over a wide range of illumination. The slides give an overall adaptation range on the order of `10^10`. **It cannot resolve this entire range simultaneously in one fixed adaptation state.** Moving from a bright to a dark place requires time to adapt. A wide adaptation capability does not mean an unlimited dynamic range at one instant.

**Relation to HDR:** a sensor has a limited dynamic range within one exposure. Bright signals saturate, while dark ones are limited by noise; multi-exposure HDR combines records suited to highlights and shadows. Human overall brightness adaptation and camera HDR are different mechanisms that can be compared. They should not be merged into a claim that the eye naturally records every possible brightness in one snapshot.

**Answer template: Why can the same grey patch look different?** Perceived brightness depends on local contrast, context and the viewer's adaptation state, rather than the patch's physical intensity alone. The visual system can adapt across a large overall intensity range, but cannot operate over that full range simultaneously.

Sources: [S05 PDF p.58–59]; [T08 01:20:57–01:23:58].

### 6.13 RGB(A), CMYK and YUV: Why Change Color Space?

**RGB** represents color with red, green and blue emitted-light components and suits displays. **RGBA** adds alpha for transparency/coverage; alpha is neither a fourth visible-light color nor layer stacking order. **CMYK** describes printing inks and suits subtractive output. Devices, paper and illumination differ in reproducible color range, or gamut. Different triangles/regions in the slide's CIE diagram represent different device/color-space gamuts, not one identical RGB triangle that every device can reproduce exactly.

**YUV** separates a luminance-related component from two color-difference components. Slide p.60 gives the following matrix relationships, retaining its notation and coefficients:

```text
Y′ = 0.299R + 0.587G + 0.114B
U  = -0.14713R - 0.28886G + 0.436B
V  = 0.615R - 0.51499G - 0.10001B

R = Y′ + 1.13983V
G = Y′ - 0.39465U - 0.58060V
B = Y′ + 2.03211U
```

**Interpretive supplement:** `Y′` in these coding formulas is luma, a brightness-related signal combining nonlinear/gamma-encoded components, and should be distinguished from physical luminance. The slides abbreviate the inputs as R/G/B. Digital formats using YCbCr may have different scaling, offsets and standard coefficients. The U/V coefficients above must not be applied directly to every YCbCr file.

Why does compression use such a representation? Vision is generally more sensitive to spatial luma detail than chroma detail. Separation lets the encoder preserve more luma information while reducing chroma sampling or precision, saving data while trying to preserve perceived quality. **A color-space transform alone does not automatically compress:** a reversible linear transform with unchanged sample count and bit depth need not reduce data. Chroma subsampling, quantization or other coding is also needed.

Interpretive example: when R=G=B, U/V are approximately zero and grayscale is mainly represented by Y′. For an unpadded 8-bit 4:2:0 YCbCr image, the average is about 12 bit/pixel, approximately half of 24-bit RGB. This is an example for one sampling format, not a claim that every YUV representation naturally halves data.

**Answer template: Why separate luminance-related and chrominance information?** The separation allows the encoder to preserve spatial detail in the luma component while representing chroma more coarsely, exploiting the visual system's differing sensitivity to those components. A color transform alone does not reduce the number of bits; subsampling, quantization or coding is also required.

Sources: [S05 PDF p.60]; [T08 01:23:58–01:26:19]. The YUV matrix comes from the formulas in the slide figure; distinctions between luma/physical luminance and the specific 4:2:0 format are interpretive supplements.

### 6.14 True Tone: Adjusting Display White to the Environment

The white appearance of paper depends on ambient illumination's color temperature. A screen with a fixed white point can look unusually blue or yellow in some settings. **True Tone**-style displays adjust white point/color appearance using ambient light, aiming for a more natural, paper-like appearance under different illumination. The slides compare the same tablet in cool and warm lighting.

This addresses the relationship between environment and visual adaptation. **It is not increased pixel count, sharpening, HDR or automatic camera-noise removal.** Nor does it guarantee identical standard color-calibration results in every environment. Interpretive supplement: automatic environmental adaptation and fixed-reference displays have different objectives in color-production work that requires a strict white point.

**Answer template: What is the idea behind True Tone?** It adjusts the display's white point and color appearance according to ambient illumination, aiming for a more consistent perceived appearance as lighting changes.

Sources: [S05 PDF p.61–62]; [T08 01:26:19–01:27:37].

### Page-by-Page Coverage Checklist for This Part

- S05 p.21–23: visible light, electromagnetic waves, light speed, coherence and polarization → 6.1.
- p.24–29: cd/lm/lx, sr, the monochromatic-light definition, light-source power comparison and illuminance versus area, including the 160 W/sr calculation in the p.26 diagram → 6.2.
- p.30–32: specular/diffuse reflection, concave/convex mirrors, refraction and image formation, transparent/reflective objects → 6.3.
- p.33–36: camera obscura, photosensitive recording media, geometric/physical image formation and the perspective model → 6.4.
- p.37–38: CCD/CMOS structure and comparison → 6.5.
- p.39–40: resolution diagrams, aspect ratio, still images/video, FPS and illustrative device limits → 6.6.
- p.41: stereo depth → 6.7; p.42–43: multiple phone cameras → 6.7; p.44: ToF active illumination and depth maps → 6.7; p.45: folded optics → 6.7; p.46: Leap Motion → 6.7.
- p.47: additive/subtractive color, RGB/CMYK → 6.8.
- p.48–50: CRT, LCD, OLED/AMOLED → 6.9; p.51: autostereoscopic parallax barriers and sweet spots → 6.9; p.52: Gatebox display example → 6.9.
- p.53: eye structure → 6.10; p.54–55: cone/rod counts, distribution and functions, plus the blind spot in the diagram → 6.10.
- p.56: foveal receptor estimate → 6.11; p.57: task-dependent eye movements → 6.11.
- p.58: subjective brightness and background contrast → 6.12; p.59: brightness adaptation and its non-simultaneous overall range → 6.12.
- p.60: gamut and forward/inverse YUV matrices → 6.13; p.61–62: True Tone and environmental comparisons → 6.14.
## 7. Worked Calculations: Formulas, Substitution, and Answers

This chapter brings together calculations from the slides, classroom discussions of parameters, and figures. Examples explicitly marked as “additional explanation” are intended to practise the same principles; they must not be interpreted as questions officially released by the lecturer.

### 7.1 Bits, Bytes, Unit Prefixes, and Bit Depth

`1 byte = 8 bits`. Lowercase b commonly denotes bit, while uppercase B denotes byte. `Mb/s` means million bits per second, whereas `MB` means million bytes; `1 MB = 10^6 B`, and `1 MiB = 2^20 B = 1,048,576 B`. If a question does not specify the convention, at least state that decimal MB is being used to avoid confusing units. A bit depth of n bits can represent `2^n` distinct codewords: 8 bits provide 256 levels, 10 bits provide 1024 levels, and 16 bits provide 65,536 levels.

For RGB with 8 bits per channel, each pixel requires `3×8 = 24 bit = 3 byte`; RGBA with 8 bits per channel requires 32 bits per pixel. **8-bit/channel does not mean that an entire colour pixel uses only 8 bits.** However, indexed colour, grayscale, floating-point images, and specific pixel formats may differ. Calculate according to the format given in the question rather than applying 32 bits to every case.

Sources: [T01 00:03:06–00:09:50, discussion of parameters and units; T05 00:01:11–00:20:39; T06 00:00:20–00:11:37, additional discussion of image representation].

### 7.2 Quantization Step and Quantization Error: An Additional Worked Example

Suppose the input operating range is 0–2 V and uniform 8-bit quantization is used. If the range is defined as 256 equal-width intervals, the quantization step is `Δ = 2/256 = 0.0078125 V = 7.8125 mV`. With rounding to the nearest representative quantization value, the maximum error within the interior intervals is approximately `Δ/2 = 3.90625 mV`. An input outside the permitted range causes saturation/clipping; this is no longer merely a small rounding error from quantization.

Some questions define both endpoints as reconstruction values, giving `(Vmax−Vmin)/(2^n−1)`. Check the convention in the question before calculating; neither formula can be declared universally correct to the exclusion of the other. Increasing bit depth improves amplitude resolution, while increasing sampling rate increases the density of temporal samples. Their effects differ.

Source: [S04, sampling/quantization pages]; the numerical example is an additional explanation.

### 7.3 Nyquist, Aliasing, and a Counterexample

**Question 1: If the highest frequency is B=18 kHz, how should the sampling rate be chosen?** Under ideal band-limited conditions, the Nyquist rate is `2B = 36 ksample/s`. In practice, choose `fs > 36 ksample/s` and leave a transition band for the anti-aliasing filter. For example, 44.1 or 48 ksample/s could be considered, depending on the system requirements. Do not write that an 18 kHz signal needs only 18k samples per second.

**Question 2: What is the Nyquist frequency when fs=44.1 kHz?** `fs/2 = 22.05 kHz`. Distinguish the Nyquist frequency, half the sampling rate determined by the sampling system, from the Nyquist rate, twice the highest frequency determined by the target signal bandwidth.

**Question 3: What happens when a 23 kHz tone is sampled at 44.1 kHz?** Since 23 kHz is above 22.05 kHz, sampling without appropriate filtering can fold it into an aliased component at `|44.1−23| = 21.1 kHz`. The digital samples can no longer uniquely establish whether the original was 23 kHz or an alias. Merely increasing the playback sampling rate afterwards cannot recover the lost information. This numerical example is an additional explanation.

**Why is fs=2B not a universally safe condition?** Consider `x(t)=sin(2πBt)`. If `fs=2B` and sampling starts at zero phase, then `x[n]=sin(πn)=0`: every sample is zero, so the amplitude cannot be recovered. This demonstrates the importance of boundary conditions, phase, and the strict band-limiting assumptions. Practical systems use filtering and margin instead of relying on the boundary case.

**The correct interpretation of 44.1 kHz:** Half the sampling rate is 22.05 kHz. A target audio bandwidth of approximately 20 kHz is usually used to explain the available margin. The slides also describe human hearing as extending to 22 kHz, but this does not mean that 44.1 kHz provides a generous filter transition band above 22 kHz.

Source: [S04, sampling theorem and aliasing pages]; the phase counterexample and numerical aliasing example explain the conditions.

### 7.4 Data Rate and File Size of Uncompressed PCM Audio

Formulas: `bitrate = fs × bits/sample × channels`; `bytes = fs × bits/sample × channels × duration / 8`. Assume all samples are packed using the specified number of bits, excluding file headers, alignment, and metadata.

**Example: 44.1 kHz, 16 bit/sample, stereo, 60 seconds.**

1. Convert the sampling rate to `44,100 sample/s/channel`.
2. The bit rate is `44,100×16×2 = 1,411,200 bit/s = 1.4112 Mb/s`.
3. The total size is `1,411,200×60/8 = 10,584,000 B`.
4. This is `10.584 MB`, or approximately `10.09 MiB`.

**Explanation of the answer:** Both stereo channels must be stored. Sampling rate is not the total number of bits per second. Renaming a file to MP3 does not compress it; the actual compressed size depends on the encoding settings.

Sources: [S04, principles of digitization; classroom framework for parameter calculations]; the complete numerical PCM example is an additional explanation.

### 7.5 Raw Image Size: RGB and RGBA

Formula: `bytes = W × H × bits/pixel / 8`.

**1920×1080, RGB, 8 bits per channel:** There are `2,073,600` pixels, each requiring `24 bit=3 B`. The total is `2,073,600×3 = 6,220,800 B = 6.2208 MB ≈ 5.93 MiB`.

**The same dimensions, RGBA, 8 bits per channel:** Each pixel requires `32 bit=4 B`, giving `8,294,400 B = 8.2944 MB ≈ 7.91 MiB`. Alpha is a transparency-related value; it does not automatically divide the image into “4 layers”.

For formats such as JPEG and PNG, the file extension alone does not determine the actual size. Compression ratio depends on content, quality, encoding, and metadata. The classroom discussion compares uncompressed pixel representations with photo files. In an examination, first state that the calculation concerns raw pixel data.

Sources: [T05 00:01:11–00:20:39; T06 00:00:20–00:11:37, discussions of image representation, RGBA, and size calculations].

### 7.6 Raw Video Data: Space Multiplied by Time

Formulas: `raw bitrate = W × H × bpp × fps`; `bytes = W × H × bpp × fps × seconds / 8`. If audio is present, add the audio-track data separately. The following example excludes audio, encoding headers, and container overhead.

**Example: 1920×1080, RGB 24bpp, 30fps, 60s.** Each frame requires `6,220,800 B`. The total frame count is `30×60=1800`, and the total size is `6,220,800×1800 = 11,197,440,000 B = 11.19744 GB`. The raw bit rate is `1920×1080×24×30 = 1,492,992,000 bit/s ≈ 1.493 Gb/s`.

**Why does video need compression?** One minute of raw data already exceeds 11 GB, so direct transmission would require very high bandwidth. Spatial redundancy, interframe redundancy, and visual sensitivity offer opportunities for compression. **Compressed files can still have different sizes at the same resolution and FPS**, because their compressed bit rates, encoders, and content complexity differ.

Sources: [T05/T06, discussions of video sequences and bit rate; S05 PDF p.39–40]; the 60s numerical calculation is an additional explanation.

### 7.7 Calculating File Size from a Compressed Bit Rate

Formula: `bytes ≈ bitrate(bit/s) × seconds / 8`.

**Example 1: An 8 Mb/s video lasting 10 minutes.** `8×10^6×600/8 = 600,000,000 B = 600 MB`. If 8 Mb/s describes only the video track, remember to add audio and container overhead. If it is the total bit rate, do not add audio a second time.

**Example 2: A 128 kb/s audio clip lasting 3 minutes.** `128,000×180/8 = 2,880,000 B = 2.88 MB`.

**Example 3: For two videos of equal duration at 5 Mb/s and 10 Mb/s, must the second be twice as clear?** Under otherwise equal conditions, the size is approximately doubled, but perceived image quality does not increase linearly with bit rate. Resolution, coding efficiency, noise, and motion also affect quality. For variable-bit-rate material, estimate using the average total bit rate rather than the instantaneous peak.

Sources: [T01, discussion of bit rate and duration calculations; S03, video parameters].

### 7.8 Sound Wavelength, SPL, and Reflection Distance

**Wave relationship:** `v=fλ`. Taking the speed of sound in air as `343 m/s` and frequency as 440 Hz gives a wavelength of `λ=343/440≈0.780 m`. If sound speed changes, the wavelength at the same frequency also changes. Pitch relates to frequency; do not confuse sound speed, loudness, and pitch.

**SPL:** `Lp = 20 log10(prms/pref)`, with the reference pressure in air `pref=20 μPa=2×10^-5 Pa`. For `prms=0.2 Pa`, the ratio is `10,000`, giving SPL=`20×4 = 80 dB`. Doubling sound pressure adds `20log10(2)≈6.02 dB`; under appropriately comparable conditions with the same impedance, doubling power/intensity corresponds to `10log10(2)≈3.01 dB`. **Do not replace 20 with 10 in the pressure-ratio formula.**

**Additional explanation of echoes:** If the source and receiver are close together and sound travels to a plane wall and back, a round-trip delay of 0.1s corresponds to `d=vt/2=343×0.1/2=17.15 m`. Division by 2 is required for the round trip; do not divide by 2 for a one-way propagation question. Whether a reflection is heard as a separate echo also depends on content and environment. The 0.1s value is only the classroom's approximate perceptual threshold.

Sources: [S04, acoustics, SPL, and echo pages]; the specific numerical calculations are additional explanations.

### 7.9 Optical Calculations: sr, lm, lx, ToF, and Stereo

**Luminous flux and direction:** For a source with uniform intensity of 2 cd over 3 sr, the flux is `Φ=2×3=6 lm`. If the 2 cd intensity is constant in every direction, the flux over the entire sphere is `2×4π=8π lm`. These are different assumptions; do not automatically multiply every value in cd by 4π.

**Illuminance:** If 1000 lm is distributed uniformly over 10 m², `E=1000/10=100 lx`; over only 1m², the value is 1000lx. If the real distribution is nonuniform, this is an average.

**Radiant-intensity example in the slide figure:** A 50mm×50mm receiving surface is 2m from the source and receives 0.1W. Then `Ω≈0.05²/2²=0.000625sr`, and `Ie=0.1/Ω=160W/sr`. The unit is W/sr, not cd. Without spectral information and visual weighting, the values cannot be directly converted.

**ToF, additional explanation:** For a round-trip delay of 20ns, `Z=cΔt/2=(3×10^8)(20×10^-9)/2=3m`.

**Parallel stereo, additional explanation:** With focal length 800pixel, baseline 0.1m, and disparity 20pixel, `Z=fB/d=800×0.1/20=4m`. The pixel units of focal length and disparity cancel. Do not mistake the focal length of 800 for 800m. Smaller disparity generally indicates greater depth.

Sources: [S05 PDF p.25–29, 41, 44].

### 7.10 Foveal Receptor Count and Colour Transformation

**Fovea:** Using the square approximation in the slides gives `1.5mm×1.5mm×150,000/mm²=337,500≈337,000`. If the question requires the slide model, use the square area rather than silently substituting a circular area. This estimate compares local receptor counts; it does not establish that the entire human eye is equivalent to a 0.337MP camera.

**YUV transformation:** Using the slide matrix with R=1 and G=B=0 gives `Y′=0.299`, `U=-0.14713`, and `V=0.615`. The inverse transformation approximately recovers red; rounded coefficients can introduce small errors. When R=G=B=0.5, Y′≈0.5 and U≈V≈0, showing that achromatic gray does not need strong chrominance signals. Before using the equations, check whether the inputs are normalized and which standard and range apply.

Sources: [S05 PDF p.56, 60]; the numerical colour substitutions are additional explanations.

## 8. Integrated Short-Answer, Comparison, and Design Questions: Model Answers

These questions organize relationships in the materials that are suitable for short answers; they do not predict the actual examination questions. Earlier chapters provide fuller mechanisms and English answer templates. This chapter practises organizing answers across topics.

### 8.1 How to Answer: “Design a Classroom Multimedia Recording and Retrieval System”

**Model answer:** Use cameras to capture the lecturer and board, microphones to acquire sound, and slides or screen sharing to provide a clear instructional content stream. Record unified or convertible timestamps for all streams, handle differences between device clocks and transmission delays, and ensure that speech, images, and slide events correspond in time. Apply suitable sampling, quantization, encoding, buffering, and storage, while retaining metadata such as lecture session, speaker, time, and slide page. Processing modules can perform speech transcription, keyword/image-feature extraction, and indexing. A query should first match against the index and then return the corresponding interval, rather than scanning every recording word by word for each query. The output should support synchronized playback, chapter navigation, and searchable notes. Noise, recognition errors, interrupted streams, clock drift, and data volume are limitations to evaluate. This answer connects the five modules of capture, storage, network, processing, and output instead of merely proposing “an AI summary”.

Basis: [S01–S02, system framework; S03, retrieval; S04, digitization].

### 8.2 How to Answer: “Why Fuse Multiple Sources Instead of Only Improving One Sensor's Accuracy?”

**Model answer:** Improved accuracy reduces measurement error for a particular physical quantity, while multisource fusion provides complementary evidence at different semantic levels. Their functions differ. No matter how accurate a temperature sensor becomes, it cannot determine humidity on its own. GPS alone may not determine camera orientation, requiring attitude and visual information. Before fusion, address temporal alignment, consistent coordinates/units, and reliability. Treating observations from different times as simultaneous can produce an incorrect interpretation of an event. Fusion does not guarantee absolute truth either: the system should preserve uncertainty and keep updating its model with new evidence.

Basis: [S01, new applications and S/M/F framework; S02, correlation/holistic information; T01/T02, classroom examples].

### 8.3 How to Connect the Semantic Gap, Perceptual Cycle, and Context in One Answer

**Model answer:** Sensors provide low-level data such as pixels and waveforms, whereas people need meaning about objects, events, and purposes. The difference is the semantic gap. Existing schemata help people propose interpretations and decide where to direct attention; new sensory evidence then modifies the schemata. This is Neisser's perceptual cycle. Context and metadata supply clues such as time, place, and task, helping the same signal yield more relevant information. Prior knowledge can also mislead, so interpretations require further observation rather than treating a first impression as truth. Multimedia systems aim to reduce the gap by combining complementary signals, context, and the task.

Basis: [S02 PDF p.3–21].

### 8.4 How to Answer: “Are ANC, EQ, and Speech Recognition the Same Task?”

**Model answer:** All three process audio, but their objectives and outputs differ. ANC estimates environmental noise and generates a suitable antiphase signal at a target location to reduce noise through destructive interference. EQ applies frequency-dependent gains or attenuation to change the spectrum/timbre without automatically understanding speech. ASR infers linguistic units and text from sound. High-quality acquisition and noise reduction may help recognition, but reducing noise does not mean that words have already been recognized. ANC depends on delay, phase, spatial position, and changes in noise. EQ modifications can also damage sounds that should be preserved.

Basis: [S03, audio applications; S04, interference and acquisition; S05, speech].

### 8.5 How to Answer: “Why Does Shazam Not Need to Listen to Every Song from the Beginning?”

**Model answer:** During database ingestion, the system extracts audio fingerprints for tracks and builds an index. At query time, it extracts comparable fingerprints from a short clip, uses hashing/index lookup to find candidate tracks, and checks whether multiple features match at a consistent time offset. Strong local time-frequency features and their relative relationships help match clips with unknown starting positions and some noise, with robustness depending on the implementation. Fast queries are enabled by organizing the library before the query, rather than comparing every complete original waveform only when a question is asked. Query-by-humming and matching a clip of an original recording are also distinct tasks.

Basis: [S03, Shazam pages; T04/T05, explanations of indexing].

### 8.6 How to Answer: “What Different Principles Underlie LPC and MPEG Audio Compression?”

**Model answer:** LPC is based on a model of speech production. Prediction/vocal-tract parameters and excitation information provide a compact representation from which speech can be approximately reconstructed, primarily exploiting the structure of speech signals. MPEG audio coding can use the ear's frequency and temporal masking to reduce precision or bit allocation for less noticeable components, while also exploiting other coding redundancy. The former emphasizes a generative/predictive model and the latter perceptual coding, although real standards can combine several techniques. Frequency masking occurs when a strong sound masks weaker sounds in neighbouring frequency bands; temporal masking makes weaker sounds near a strong sound in time harder to perceive. This does not justify arbitrarily removing every sound that is momentarily difficult to hear.

Basis: [S03, LPC, MPEG, and masking pages].

### 8.7 How to Distinguish HDR, Video Stabilization, and Deblurring

**Model answer:** HDR addresses lost highlight/shadow information caused by limited dynamic range, usually combining exposures or other complementary recordings. Stabilization estimates and compensates for the camera's global motion across frames, making the image trajectory steadier. Deblurring attempts to reverse blur caused by motion during exposure or other mechanisms. Video may be stabilized while each frame still contains exposure-related motion trails. Multi-exposure fusion with motion requires alignment and ghost handling. Compensation for global camera motion does not necessarily restore every independently moving object. The algorithms address different problems; “making the picture clearer” does not explain their mechanisms.

Basis: [S03, image/video enhancement pages].

### 8.8 How to Distinguish Detection, Recognition, Tracking, 3D Reconstruction, and Retrieval

**Model answer:** Detection determines whether a target is present and where it is. Identity recognition determines who the target is or which identity it matches. Tracking associates target observations over time into trajectories. 3D reconstruction recovers shape/geometry and possibly texture, enabling presentation from new viewpoints. Retrieval returns relevant items from an organized collection according to a query or features. The tasks can share features and form a pipeline: for example, detect a face, track it across frames, and select clear images for identity comparison. A box drawn around a face does not by itself establish that identity recognition has been completed.

Basis: [S03, Haar, head tracking, 3D face, gait, and video-indexing pages; T02/T06].

### 8.9 How to Answer: “Why Do a Piano and a Violin Sound Different When Playing the Same Middle C?”

**Model answer:** They can share approximately the same fundamental frequency and therefore the same pitch. Their different vibration and resonance mechanisms produce different relative harmonic strengths, while their attack, decay, sustain, and release envelopes also differ. These differences produce different timbres. In frequency terms, their fundamental/overtone composition differs; in time terms, their ADSR and other dynamic features differ. Storing only a fundamental-frequency value can indicate pitch but cannot fully reconstruct the true instrument timbre. A synthesizer must additionally model waveform, harmonics, and envelope, or use sampling/physical models.

Basis: [S05 PDF p.15–20; T08 00:05:02, 00:09:17–00:15:56].

### 8.10 How to Answer: “How Can Human Vision Inspire Compression, HDR, and VR Optimization?”

**Model answer:** Human vision has different spatial sensitivity to luminance and chrominance, allowing coding to retain more luminance detail and reduce some colour information. High detail resolution at the fovea and lower resolution in the periphery motivate eye-tracked foveated rendering in VR. Perceived brightness depends on background contrast and adaptation, so image presentation and displays must consider subjective effects. Camera multi-exposure HDR and visual adaptation can both be discussed in relation to wide lighting ranges, but their mechanisms differ; the eye does not simultaneously perceive an unlimited dynamic range. Using perceptual limitations must preserve information required by the task. Medical/measurement applications may use different quality criteria from general entertainment imagery.

Basis: [S05 PDF p.53–62; S03, HDR].

### 8.11 Fourteen Concept Pairs or Groups to Distinguish Immediately

1. **Signal vs information:** A signal consists of measured/encoded values; information is a meaningful interpretation incorporating semantics and context.
2. **Media vs modality:** Media are forms of information, while modalities are sensory channels. Multiple media can be presented through the same sense.
3. **Content vs context vs metadata:** Content is the media itself; context supplies conditions for interpretation; metadata is data describing data and can record part of the context.
4. **Object vs event:** An object is an entity with attributes; an event concerns changes in states and relationships over time.
5. **Accuracy vs resolution:** Accuracy concerns closeness to the true value; resolution concerns the smallest distinguishable change. More scale divisions do not guarantee freedom from bias.
6. **Sampling vs quantization:** Sampling makes an independent variable such as time or space discrete; quantization maps continuous amplitudes to a finite set of levels. They are not interchangeable.
7. **Nyquist rate vs Nyquist frequency:** These are 2B and fs/2, respectively, viewed from the signal and the sampling system.
8. **Frequency vs amplitude vs phase:** These describe repetition rate, magnitude, and relative position within a cycle, respectively, and are associated with pitch, sound pressure, and superposition relationships.
9. **Echo vs reverberation vs interference:** These mean a separable delayed reflection, dense decaying reflections, and wave superposition, respectively.
10. **Loudness vs pitch vs timbre:** Perceived strength, perceived tonal height, and sound quality depend on different principal factors.
11. **Resolution vs FPS vs bitrate:** These describe spatial sample count, temporal sampling density, and encoded data per unit time.
12. **cd vs lm vs lx:** These measure directional luminous intensity, luminous flux, and flux per unit area at a receiving surface.
13. **RGB vs CMYK vs YUV:** These correspond to additive light, subtractive printing, and a representation separating luma-related and chrominance components.
14. **Cones vs rods:** Cones support bright-light colour/detail and high central resolution; rods support dim-light sensitivity and more general peripheral information.

### 8.12 Final Checks When Writing an Answer

- Does the definition identify what is being measured/processed, instead of only naming a device?
- Does the process include its input, core steps, and output? For retrieval, does it explain offline/ingestion-stage indexing?
- Does a comparison use common dimensions, such as acquisition principle, output, operating conditions, and limitations?
- Do numerical answers distinguish bit/byte, k/M prefixes, per-channel/per-pixel quantities, and one-way/round-trip distances?
- Are the conditions behind claims such as “higher”, “faster”, or “better” stated, avoiding the promotion of examples into absolute rules?
- Are lecturer examples, slide facts, additional explanations, and inferred examination topics distinguished?

## 9. Source Inventory, Lookup Paths, and Completeness Check

### 9.1 Original Slide Files and Page Counts

The original PDFs S00–S05 are in the course directory's Slides folder. References to p. in this document use physical PDF page numbers. S02 has jumps in its printed footer numbering; these must not be mistaken for missing physical pages. Page-by-page coverage checklists appear near the end of each slide set's discussion, including notes identifying title pages and video-introduction pages. Key formulas and processes embedded in figures have been incorporated into the main text.

### 9.2 Looking Up the Eight Recordings

- T01: `Transcripts/artifact-多媒体-01-obcnxzjs37165o216vrd19lx/transcript.txt`.
- T02: `Transcripts/artifact-多媒体-02-obcnxz2z26vl7c86iw194s83/transcript.txt`.
- T03: `Transcripts/artifact-多媒体-03-obcnx1n21qx2y87q95zk937g/transcript.txt`.
- T04: `Transcripts/artifact-多媒体-04-obcnx2la973g92y18fx6rek3/transcript.txt`.
- T05: `Transcripts/artifact-多媒体-01-obcn3sqjs2kzm7114n94lg5e/transcript.txt`.
- T06: `Transcripts/artifact-多媒体-02-obcn3t8a59263c8w6t3312q2/transcript.txt`.
- T07: `Transcripts/artifact-多媒体-01-obcn8l41ae3e23k112c2t4jm/transcript.txt`.
- T08: `Transcripts/artifact-多媒体-01-obcnh787mag6242rp5i573lz/transcript.txt`.

These paths are relative to the local Exam-Prep folder. They remain in the Feishu cloud document to identify sources; they do not imply that clicking them provides access to files on this computer. `Transcripts/INDEX.md` includes the corresponding dates, durations, and clickable local links. The original transcripts contain approximately 47,000 recognized words. They are still the raw automatic recognition output, not manually corrected, verbatim official lecture scripts.

### 9.3 Main Corrections and Additions in This Rewrite

The previous version was only an overview. This rewrite adds the roles of communication technologies, the S/M/F system framework, every arrow in the perceptual cycle, experiential environments, mechanisms of individual applications, the 3D face-reconstruction pipeline, gait and video indexing, sensor/audio/video device structures, acoustic/music/optical/visual principles, directly usable model answers, and complete calculations. The radiant-intensity example in a slide figure, forward/inverse YUV transformations, and the foveal estimate are also explained separately.

Potentially misleading points are explicitly qualified: Quiz weighting, limitations of higher pixel counts, RGB/RGBA formats, the two Nyquist terms, the 44.1kHz boundary, pressure versus power in dB calculations, cd/lm/lx, generalizations about CCD/CMOS, polarization versus colour-filter stereoscopy, LCD versus OLED, and brightness adaptation versus simultaneous dynamic range. Recording content absent from the available materials and unviewed external demonstrations are not reconstructed through speculation and attributed to the lecturer.

**Companion quick reference:** `COMP7503-Cheat-Sheet-A4-Duplex-English.pdf` is the English two-page PDF for printing on both sides of one A4 sheet. It retains definitions, formulas, mechanisms, processes, and answer cues across all chapters; use this long document for complete explanations. The earlier `Cheat-Sheet-A4-Duplex.md` and `COMP7503-Cheat-Sheet-A4-Duplex.pdf` remain the Chinese companions.
