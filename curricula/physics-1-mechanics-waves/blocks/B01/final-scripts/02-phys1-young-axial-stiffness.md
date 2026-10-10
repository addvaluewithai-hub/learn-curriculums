# B01 — Final connected script 02 | Young's Modulus and Hooke's Law

- **Issued lesson ID:** phys1-young-axial-stiffness
- **Curriculum order:** 802 | **English title:** Young's Modulus and Axial Stiffness
- **Stage:** 03, finalized lesson boundary/connected editorial script; not Scenes or publication.
- **Source locators:** phys1-main-scan PDF p.8 = printed pp.126–127; clearer phys1-elasticity-closeup PDF p.1 = printed p.125 for three elastic moduli; printed pp.130–131 exercises are only source of application themes.
- **Objectives:** O1 formulate Y=stress/strain and axial extension under assumptions; O2 distinguish Y from axial k=YA/L0; O3 predict geometric effects and solve unfamiliar SI-unit questions.
- **Prerequisites:** Lesson phys1-solid-structure-stress-strain; stress, strain, SI area/length conversions.
- **Authored:** every number and new engineering scenario is original practice. Model clarifications are supplemental teaching, not verbatim book transcription.
- **Non-spoken:** headings, Attempt/Feedback markers and source notes are editorial boundaries, not Scenes.

## نص الشرح المتصل

آخر مرة عرفنا نفرّق بين حاجتين: Stress بيحكي متوسط القوة على مساحة المقطع في حالة شد محوري مبسطة، وStrain بيحكي مقدار الاستطالة مقارنة بالطول الأصلي. لكن كمهندسين ده لسه نص الإجابة. لو هنعمل قضيب في ماكينة، مش كفاية نقول عليه شد مقداره ألف نيوتن؛ لازم نعرف هل هيتغير طوله جزء صغير من الملّيمتر ولا أكتر. وعلشان نتوقع ده، هنحتاج خاصية من خواص المادة.

تخيل قضيبين من أبعاد متطابقة اتشدوا بالقوة نفسها، لكن كل واحد مصنوع من مادة مختلفة. ممكن التغير النسبي في الطول يبقى مختلف. في الجزء المرن الخطي، يعني بنفترض علاقة تناسب تقريبية بين Stress وStrain ضمن حمل صغير مناسب، بنسمي ثابت التناسب Young's Modulus. في صفحات المصدر رمزه Y، وهتلاقيه كمان E في مراجع هندسية. وهنستخدم Y هنا علشان يكون متسقًا مع الكتاب.

إحنا بنتكلم عن **قضيب مستقيم منتظم مساحة المقطع، قوة الشد على محوره، وتغير صغير في الطول**. تحت الشروط دي، Young's modulus = Stress/Strain. بمعنى Y = (F/A)/(ΔL/L0). لو ضربنا في المقلوب هنكتب Y = F L0/(A ΔL). ولو عايزين نستخرج الاستطالة هنرتبها: ΔL = F L0/(Y A). رياضيا نفس العلاقة مكتوبة تلات صور. اختار الصورة حسب المطلوب، لكن متنساش الفروض قبل الحساب.

الوحدات هنا اختبار للفهم. F بالنيوتن وA بالمتر المربع، فـStress بوحدة Pa. وStrain بلا وحدة، يبقى Y بوحدة Pa برضه. لكن كون Y وStress ليهم نفس الوحدة مش معناه إنهم نفس الكمية. Stress بيحكي التحميل الفعلي، أما Y بيحكي استجابة **المادة** في النطاق المرن الخطي. Y أعلى يعني عند نفس Stress هنلاقي Strain أصغر، لكن ده وصف للصلابة المرنة مش مقياس مباشر لإجهاد الكسر أو الأمان الإنشائي.

هنشتغل أولًا على معنى العوامل بدل الرقم. في ΔL = F L0/(Y A)، لو القوة زادت للضعف وكل حاجة تانية ثابتة في نفس النطاق، الاستطالة تتضاعف. لو الطول الأصلي اتضاعف، الاستطالة كمان تتضاعف. لو مساحة المقطع اتضاعفت، الاستطالة تنخفض للنصف. ولو المادة معامل Y بتاعها أكبر للضعف، الاستطالة أقل للنصف. مفيش قانون جديد في كل جملة؛ ده تفسير العلاقة.

وأهم تحذير في الوحدات: واحد ملّيمتر يساوي 0.001 متر، لكن واحد ملّيمتر مربع يساوي 0.000001 متر مربع. تحويل المساحة مختلف عن تحويل الطول، لأننا بنربّع عامل التحويل. لما تلاقي A بالـmm² وY بالـPa، الأفضل تحول للمتر المربع قبل ما تعمل الحساب، علشان وحدات الإجابة تطلع بالمتر.

تعال نحل مثال إرشادي من تأليفنا. قضيب طوله 2 متر، مساحة مقطعه الأصلي 2 × 10⁻⁴ متر مربع، عليه قوة شد محورية 1000 نيوتن، ومعامل Young في فرض المسألة 10¹¹ باسكال. عايزين الاستطالة. نكتب ΔL = F L0/(Y A)، يعني 1000 × 2 على 10¹¹ × 2 × 10⁻⁴. الناتج 10⁻⁴ متر، أو 0.1 ملّيمتر. نقدر نتحقق بطريقة تانية: Stress = 1000/0.0002 = 5 × 10⁶ Pa. Strain = Stress/Y = 5 × 10⁻⁵. اضرب الانفعال في الطول 2 متر، هترجع لنفس الاستطالة.

طيب، لو فكرنا في القضيب كعنصر بيقاوم الشد، هل يشبه نابضًا؟ في النطاق ده نعم، من ناحية العلاقة بين **مقدار القوة** و**مقدار الاستطالة**. نكتب F = k ΔL. الكتاب بيذكر Hooke's Law عند النقطة دي. ومن معادلة Young، هنلاقي k = Y A/L0. لاحظ إن k بتاع العنصر المحوري بيتأثر بنوع المادة وبأبعاده كمان، ووحدته Newton per metre أو N/m، بخلاف Y اللي وحدته Pascal.

يعني لو صنعنا قضيبين من نفس المادة ونفس مساحة المقطع، لكن واحد أطول، الاتنين لهم نفس Y ما دمنا بنقارن خواص المادة في الظروف نفسها. إنما k للقضيب الأطول أقل، لأنه عند نفس القوة هيتمدد أكتر. دي كلمة مهمة: **material modulus** مقابل **effective axial stiffness of a component**. لا تخلطهم، ولا تتخيل إن كل جسم حقيقي يمكن اعتباره نابضًا واحدًا بنفس k مهما كان اتجاه التحميل.

ممكن تكون شوفت في النابض قوة الاسترجاع مكتوبة بإشارة سالبة: F_restoring = −kx. السالب هنا يصف اتجاه قوة الاسترجاع المعاكس للإزاحة؛ إنما في مسائل شد القضيب اللي بنحسب فيها **مقادير** القوة والاستطالة بنكتب F = k ΔL. الاختلاف مش تناقض، هو فرق بين اتجاه متجه ومقدار موجب.

قبل مسألة الامتحان، افتكر إننا ما نقدرش نستخدم الصيغ دي لو الجسم خرج عن الاستجابة الخطية أو حصل له تشوه دائم كبير. المسألة لازم تصرّح أو تسمح نفترض سلوكًا مرنًا خطيًا، وهنعتبر القضيب موحد المقطع والتحميل محوريًا. لو كانت الحالة فيها انحناء أو قص أو تغيير كبير في المساحة، يبقى محتاجين نموذج مختلف.

## [Attempt 01 — مسألة كمية مستقلة]

**English exam question:** A uniform rod has original length 0.80 m and cross-sectional area 4 × 10⁻⁴ m². Under a tensile load of 400 N it extends by 0.40 mm in the linear elastic range. Calculate the average tensile stress, axial engineering strain, Young's modulus and effective axial stiffness k.

بالعربي: الطول 0.80 متر، المساحة أربعة في عشرة أس سالب أربعة متر مربع، القوة أربعمائة نيوتن، والاستطالة 0.40 ملّيمتر. احسب Stress وStrain وY وk، مع وحدة كل كمية. سيب لنفسك وقت كفاية للخطوات قبل سماع الإجابة.

## [Feedback 01 — بعد المحاولة فقط]

**English model answer:** Stress = 400/(4 × 10⁻⁴) = 1 × 10⁶ Pa. Strain = 0.00040/0.80 = 5 × 10⁻⁴. Young's modulus Y = (10⁶)/(5 × 10⁻⁴) = 2 × 10⁹ Pa. Axial stiffness k = 400/0.00040 = 1 × 10⁶ N/m.

أولًا حولنا 0.40 ملّيمتر إلى 0.00040 متر. من القوة والمساحة طلع الإجهاد مليون باسكال. ومن تغير الطول والطول الأصلي طلع انفعال بلا وحدة. لما قسمنا الإجهاد على الانفعال طلع معامل يونج اتنين مليار باسكال. وأخيرًا k = قوة على استطالة، فوحدته نيوتن لكل متر. جرّب تراجع k باستخدام Y A/L0، هتلاقيه نفس الناتج.

## [Attempt 02 — انتقال مستقل للمقارنة]

**English exam question:** Rod A and rod B have identical materials and cross-sectional areas. B is twice as long as A. The same small axial tensile force acts on both. Which rod extends more? Do they have different Young's moduli? Which rod has larger effective axial stiffness?

بالعربي: نفس المادة ونفس المقطع ونفس القوة، لكن القضيب B ضعف طول A. رتبهم في الاستطالة، وقول إذا Y يختلف، وقارن k. بدون تعويض أرقام.

## [Feedback 02 — بعد المحاولة فقط]

**English model answer:** B extends twice as much as A; their Young's moduli are equal; A has twice B's effective axial stiffness.

لأن ΔL بيتناسب مع L0، الأطول يتمدد ضعف الأقصر. Y مش بيتغير مع طول الجسم في نفس المادة وظروف الاختبار. لكن k يتناسب عكسيًا مع L0، فالقضيب الأقصر له ضعف الصلابة المحورية. الفرق بين خاصية المادة وخاصية العنصر هو الإجابة الأساسية.

## خاتمة وربط

دلوقتي نقدر نبدأ من Stress وStrain ونوصل لـYoung's modulus، ونستخدمه في حساب استطالة قضيب، ونستخرج منه k. اتعلمنا كمان نفحص الوحدات ونميّز بين المادة والعنصر. بس مش كل قوة بتشتغل على محور القضيب. لو أثرت قوة موازية لوجه بلوك، ممكن تغير شكل الجسم من غير استطالة محورية أساسية، وده موضوع الدرس التالي: Shear.

## Editor-only coverage / review
- O1 → definition, derivation, worked example, Attempt 01; O2 → Hooke/k, Attempt 01/02; O3 → interpretation, units, Attempt 02.
- All numerical values explicitly authored; textbook printed p.127 supplies the topic/formula sequence only.
- Independent academic approval and audio listening untested; no Scenes.
