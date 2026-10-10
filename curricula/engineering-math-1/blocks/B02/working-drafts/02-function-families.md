# B02 Stage 01 provisional working draft B — إزاي نتعرف على عائلة الدالة من شكلها وقاعدتها؟
**Stage:** B02 **Stage 02** — critically revised complete connected provisional draft; **no final ID, final boundary, scenes, audio or human academic approval**.
**Source:** `abd-el-salam-math-i-scan`, printed pp. 25–35 (PDF pp. 16–21).
**Prerequisites:** function/domain/range (working draft A), graph axes and basic trigonometry.
**Working objectives:** distinguish algebraic families, trig and real exponential/log functions; use rational/tangent/log domain restrictions; identify graph transformations and transfer to unseen examples.
**Authored examples:** all classroom examples and exam questions here are original teaching material.
**Legacy provenance:** Derived **verbatim in teaching/assessment body** from historical `curricula/engineering-math-1/working-drafts/02-function-families.md` (previous curriculum-wide AI Stage 02 revision). Historical original is **frozen for audit**, while THIS B02-scoped copy is the sole active Stage 01 draft; no retroactive B02 gate approval is claimed. The current turn did not conduct a new Stage 02 critique.
**Verified source scope:** printed 25–35 / PDF 16–21. On 2026-10-10 the conversation-mounted original PDF was reopened; SHA-256 matches the source manifest. Its future private retrieval is still unresolved at the user's request.
**B01 prerequisite bridge:** B02 A domain/range plus B01 denominator exclusion; angles/trigonometry brief bridge.
**Deliberately deferred:** monotonicity, formal limits.
**Teaching boundary:** Label B and order A→E are **provisional**; no stable B02 lesson ID or scene may be created until Stage 03 after a separate human gate.
**Source discrepancy (non-spoken):** printed textbook p. **34**, PDF image p. **20 right**, appears to reverse the domain and range of a real exponential $a^x$. The accompanying graph and independently verified mathematical rule imply domain $\mathbb R$, range $(0,\infty)$ for $a>0$, $a\ne1$; for $a=1$ the range is $\{1\}$. This is a **source erratum candidate**, not wording to quote as correct; faculty/source sign-off untested.
**Active B02 Stage 02 critique:** `../reviews/STAGE_02_CRITIQUE.md`; this is independent of the earlier combined historical report.

## Complete connected spoken draft
المرة اللي فاتت فهمنا يعني إيه دالة، وفرقنا بين المجال والمدى. دلوقتي عندنا دالتين: واحدة رسمها خط مستقيم، والتانية منحنى عامل زي حرف يو. الاتنين دوال، بس كل واحدة بتحكي نوعًا مختلفًا من العلاقة بين إكس وواي. لما نعرف **Function family** أو عائلة الدالة، نقدر نتوقع حاجات عن الرسم حتى قبل ما نرسمه نقطة بنقطة.

نبدأ بالخط المستقيم. لو $f(x)=2x+1$، كل ما تزود إكس واحد، الناتج يزيد اتنين. الرسم خط مستقيم، واسمه **Linear function**. العدد اللي قدام إكس بيأثر في ميل الخط، والثابت بيحدد مكان تقاطعه مع محور واي. لو شلت الثابت وبقت (2x)، الخط هيمر بنقطة الأصل؛ لكن مش كل خط لازم يمر بالأصل. أول ما تشوف صورة إكس من الدرجة الأولى ومعاها ثابت، اسأل: هل هتكون خطية؟

بعد كده $g(x)=x^2$. لما نحسب عند سالب اتنين واتنين، الاتنين يطلعوا أربعة، فالرسم متناظر حول محور واي، وعامل زي حرف يو. ده مثال على **Power function** وكمان **Polynomial function**. متعدد الحدود ممكن يجمع حدود من درجات مختلفة، زي إكس تكعيب ناقص اتنين إكس زائد واحد. كل حد فيه قوة صحيحة غير سالبة لإكس، والنتيجة لسه Polynomial. رسم إكس تكعيب يختلف عن رسم إكس تربيع؛ فمش أي Polynomial لازم يكون على شكل يو. والمصدر بيعرض نماذج من القوى والدرجات عشان نميز أشكالها.

طيب خلينا نشوف كسر فيه إكس: $r(x)=1/x$. دي **Rational function** لأنها نسبة بين كثيرتي حدود، ولازم أي قيمة تخلي المقام صفر تتشال من المجال. عند إكس يساوي صفر مفيش قيمة. فرعي الرسم بيقربوا من المحورين من غير ما يقاطعوهم في المثال ده. اسم الخط اللي الرسم بيقرب منه في الحالة دي **Asymptote**؛ مش كل دالة كسرية لازم تاخد نفس الرسم. ركز على فكرة الممنوع في المجال الأول، وبعدين ادرس سلوك الرسم.

في نوع تاني مرتبط بالزوايا. لو عندك نقطة بتلف حوالين دائرة، ارتفاعها بيتغير بشكل متكرر: يطلع وينزل ثم يرجع لنفس الارتفاع بعد دورة. ده اللي بنشوفه في دالة $y=\sin x$، أو **Sine function**. دالة $y=\cos x$ كمان دورية، **Periodic**، لكن بدايتها مختلفة. والظل $\tan x$ ليه قيم إكس ممنوعة لما كوساين إكس يساوي صفر؛ عشان كده رسمه فيه فروع منفصلة. وجود جيب أو جيب تمام أو ظل يقول لك إنك في **Trigonometric functions**، وده مهم لما نوصل للنهايات.

تعال نربط ده بمجال كل دالة بدل ما نحفظ الرسمة. ساين وكوساين يقبلوا أي زاوية حقيقية لو قسناها بالراديان. لكن تان إكس يساوي ساين إكس على كوساين إكس، وده معناه إن كوساين إكس لازم ما يكونش صفر. بيحصل الصفر عند $x=\frac\pi2+k\pi$، وكي هنا عدد صحيح. دي نفس قاعدة المقام الممنوع في درس المتباينات الكسرية، وهنستعملها في امتحاننا.

نوع تالت: $y=2^x$. هنا إكس موجود في الأس نفسه، مش مجرد $x^2$. دي **Exponential function**. كل ما تزود إكس واحد، القيمة تتضاعف في المثال ده، والنواتج موجبة، ولا تساوي صفر. الأساس في الشكل ده موجب ومش بيساوي واحد في الاستخدام العام للدوال الأسية. مقابلها الدالة $y=\log_2 x$، وهي **Logarithmic function**. السؤال اللي بتجاوب عنه: اتنين مرفوعة لأنهي قوة عشان تطلع إكس؟ بالتالي المدخل إكس في اللوغاريتم لازم يكون موجب، و$\log_2 1=0$، و$\log_2 8=3$. لاحظ إن المجال هنا أهم من إنك تحفظ شكل منحنى فقط.

قبل ما نقارن الرسمين: في الدالة الأسية $2^x$ إكس يقدر يكون أي عدد حقيقي، حتى السالب، لكن الناتج يفضل موجب. أما في اللوغاريتم $\log_2x$ فلازم إكس نفسه يكون موجب. والأساس في اللوغاريتم لازم يكون موجب ومختلف عن واحد. فرق المجال ده يهم أكتر من شكل المنحنى المحفوظ.

لو كتبنا الشكل العام $a^x$ والأساس $a>0$، فكل عدد حقيقي يصلح لإكس والأس دايمًا يدي ناتج موجب. لما الأساس أكبر من واحد، زي اتنين، الدالة بتزيد. ولما الأساس بين صفر وواحد، زي نص، بتقل. وفي الحالتين طالما الأساس مش واحد، المدى هو الأعداد الموجبة كلها. أما لو الأساس واحد بالضبط، فالدالة ثابتة على الواحد ومدىها $\{1\}$. ده توضيح رياضي للحالة الخاصة، ومش معناه إننا نقلنا تصنيف المجال والمدى حرفيًا من سطر الكتاب المختلف عليه.

دلوقتي نربط الخطوط ببعضها. لو بدلنا $x^2$ بـ $(x-2)^2$، نقطة القاع هتتحرك ناحية اليمين إلى إكس تساوي اتنين. ولو ضفنا ثلاثة خارج التربيع، القاع هيطلع لفوق ثلاثة. الفكرة دي اسمها **Graph transformation**. التفصيل ده جسر تفسيري مننا عشان نفهم الرسومات، مش تمرين منقول حرفيًا من الكتاب. ماتعتمدش على الاسم بس؛ اعرف القاعدة والمجال والإشارة والشكل العام.

تخيّل قدامك ثلاث قواعد: $(x^3-1)$، و$(1/(x+4))$، و$(5^x)$. الأولى متعددة حدود، والثانية كسرية وفيها قيمة ممنوعة، والثالثة أسية. مش مطلوب منك تحفظ كل رسمة في الدنيا؛ المطلوب تربط شكل التعبير بالأسئلة اللي لازم تسألها. خلينا نشوف هل تقدر تصنف دوال جديدة بنفسك.

## Independent attempt Q-B1 — heading not spoken
**Question spoken (English):** Classify $f(x)=x^4-3x+2$ and $g(x)=1/(x^2-9)$. State every excluded real input for $g$.
**Question spoken (Arabic support):** صنّف الدالتين، وحدد قيم إكس الحقيقية المستبعدة من مجال الدالة اللي فيها كسر.
**Attempt:** written; do not show classification or excluded values before answer.

### Post-attempt feedback B1 — separate spoken text
**Model answer (English):** $f$ is polynomial; $g$ is rational, and $x=3$ and $x=-3$ are excluded.
**Feedback spoken:** الأولى كثيرة حدود لأن كل قوى إكس فيها أعداد صحيحة غير سالبة. الثانية نسبة كثيرتي حدود. المقام إكس تربيع ناقص تسعة يساوي صفر عند ثلاثة وسالب ثلاثة، فالاتنين خارج المجال، حتى لو الرسم محتاج حسابات أكتر.

## Independent attempt Q-B2 — heading not spoken
**Question spoken (English):** Which family contains $h(x)=\log_3(x-2)$? State its real domain.
**Question spoken (Arabic support):** الدالة لوغاريتم أساس ثلاثة لإكس ناقص اتنين، تنتمي لأي عائلة؟ وما مجالها الحقيقي؟
**Attempt:** written; do not display a number line before attempt.

### Post-attempt feedback B2 — separate spoken text
**Model answer (English):** Logarithmic; domain $x>2$, or $(2,\infty)$.
**Feedback spoken:** دي دالة لوغاريتمية. أي حاجة داخل اللوغاريتم لازم تكون أكبر من صفر، يعني إكس ناقص اتنين أكبر من صفر، وبالتالي إكس أكبر من اتنين. مش بنسمح بالصفر هنا، حتى لو هو مسموح جوه الجذر التربيعي في بعض الدوال.

## Independent attempt Q-B3 — separate graph-transfer question
**Question spoken (English):** Relative to the graph of $y=x^2$, where is the vertex of $y=(x+3)^2-2$? State whether the parabola opens upward or downward.
**Question spoken (Arabic support):** بالنسبة لمنحنى واي تساوي إكس تربيع، فين رأس منحنى واي تساوي إكس زائد تلاتة الكل تربيع ناقص اتنين، وهل فتحة المنحنى لفوق ولا لتحت؟
**Attempt:** written; show no shifted vertex until submission.

### Post-attempt feedback B3 — separate spoken text
**Model answer (English):** Vertex $(-3,-2)$; the parabola opens upward.
**Feedback spoken:** اللي جوه التربيع إكس زائد تلاتة معناه إن القاع اتحرك تلات وحدات شمال، والناقص اتنين خارج التربيع نزّله وحدتين. عشان كده الرأس عند سالب تلاتة وسالب اتنين، وبما إن معامل التربيع موجب، المنحنى مفتوح لفوق. ده تطبيق على قراءة الرسم مش مجرد تصنيف اسم الدالة.

## Independent attempt Q-B4 — separate family/domain-range transfer
**Question spoken (English):** Classify $f(x)=\sin x$ and $g(x)=3^x$. For real $x$, state the domain of $f$ and the range of $g$.
**Question spoken (Arabic support):** صنّف ساين إكس وتلاتة أس إكس، وبعدها اكتب مجال ساين إكس ومدى تلاتة أس إكس لما إكس عدد حقيقي.
**Attempt:** written; do not expose the families or domain/range until response.

### Post-attempt feedback B4 — separate spoken text
**Model answer (English):** $f$ is trigonometric with domain $\mathbb R$; $g$ is exponential with range $(0,\infty)$.
**Feedback spoken:** ساين إكس دالة مثلثية وتقبل أي زاوية حقيقية بوحدة متفقة. تلاتة أس إكس دالة أسية، ومهما كانت إكس موجبة أو سالبة الناتج يفضل موجب، ومش بيساوي صفر. لذلك مدى الدالة الأسية هنا كل الأعداد الموجبة فقط. السؤال بيختبر إنك تربط العائلة بالمجال والمدى، مش الاسم وحده.

## Independent attempt Q-B5 — unseen tangent-domain assessment
**Question spoken (English):** In radians, find all excluded real values of $x$ in $h(x)=\tan(2x)$, and explain why they are excluded.
**Question spoken (Arabic support):** بالراديان، حدد كل قيم إكس الممنوعة من مجال تان اتنين إكس، واشرح ليه القيم دي ممنوعة.
**Attempt:** written; do not show denominator zeros or exclusions before student attempt.

### Post-attempt feedback B5 — separate spoken text
**Model answer (English):** Exclude $x=\frac\pi4+\frac{k\pi}{2}$, $k\in\mathbb Z$, because $\cos(2x)=0$.
**Feedback spoken:** تان اتنين إكس هو ساين اتنين إكس على كوساين اتنين إكس. عشان المقام مايبقاش صفر، لازم نستبعد لما اتنين إكس تساوي باي على اتنين زائد كي باي. نقسم على اتنين فنطلع إكس تساوي باي على أربعة زائد كي باي على اتنين، لكل كي عدد صحيح. تفسير المجال أهم من حفظ نقاط فاضية في رسم التان.

## Closing spoken recap
لما تقابل دالة جديدة، شوف مكان إكس: في حد كثير حدود، في مقام، جوه دالة مثلثية، ولا في الأس، ولا جوه لوغاريتم؟ بعد التصنيف اسأل عن المجال والشكل العام. في الدرس الجاي هنتحرك من شكل الرسم إلى سلوكه: إمتى بيزيد، وإمتى بيقل، وإزاي نقيس اقترابه من نقطة.

## Rough visual ideas (editorial, NOT final storyboard)
Compare a line, parabola, cubic and hyperbola on paired axes; show sine's repeated cycle; place $(2^x)$ beside (log_2 x); show $(x-2)^2+3$ sliding right/up.
