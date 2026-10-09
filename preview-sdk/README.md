# Shared lesson preview

معاينة خفيفة تستخدم @learn/lesson-runtime المنشور من new-learn كحزمة بإصدار مثبت.
لا حسابات، قاعدة بيانات، حفظ تقدم أو نشر طالب. أدوات الإنتاج لا تحتاج تثبيت المعاينة.

## التشغيل من جذر ريبو المناهج

المطلوب للمعاينة فقط: Node.js 24، npm وPython 3.11+.

```bash
npm run preview:setup
npm run preview
```

افتح الرابط المحلي الذي يعرضه Vite. الدروس تُكتشف من curricula دون تعديل فهرس يدوي.
المسودة تظهر مع سبب توقفها؛ التشغيل يحتاج التسجيلات المختارة والتوقيتات والمكونات الفعلية.
بعد تعديل script/media/timing أعد تشغيل الأمر لإعادة تجهيز البيانات؛ مكونات React تدعم HMR.
اختيار 16:9 أو 9:16 يراجع الشكلين، و«حسب الشاشة» يتبع حجم المتصفح.

## تنظيم الفولدر

| المسار | المسؤولية |
| --- | --- |
| package.json + package-lock.json | اعتماد SDK ثابت وبيئة المعاينة فقط |
| sdk-version.json | الإصدار وSHA256 وintegrity ورابط الحزمة المحدد بcommit |
| src | اختيار الدرس وتحميله واستضافة LessonPreview |
| .generated | فهرس وحزم وروابط import وأصول مؤقتة؛ لا تُحرر ولا تدخل Git |
| tests | قبول تقني بمصادر/WAV/timestamps مصطنعة؛ ليس منهجًا حقيقيًا |

المحوّل تحت tools/preview*.py يعيد استخدام فحوص المصنع ولا ينسخ المحرك.
لا يحتاج checkout مجاورًا لـnew-learn، ولا ../learn.

## عقد المكونات

داخل scenes/<Component>.tsx اعمل default export لمكوّن يقبل VisualProps:

```tsx
import {AbsoluteFill} from 'remotion';
import {cueIsVisible, visibleQuestionParts, type VisualProps} from '@learn/lesson-runtime';

export default function Board(props: VisualProps) {
  const {frame, fps, recording, layout, question, answer, phase} = props;
  const parts = question ? visibleQuestionParts(question, recording, frame, fps) : [];
  const answers = answer?.parts?.filter(part => frame * 1000 / fps >= part.atMs) ?? [];
  return <AbsoluteFill>
    {phase === 'question-reading' ? parts.map((part, i) => <p key={i}>{part.text}</p>) :
     phase === 'feedback' ? answers.map((part, i) => <p key={i}>{part.text}</p>) :
     cueIsVisible(recording, 'YOUR_UNIT_ID', frame, fps) ? <p>{layout}</p> : null}
  </AbsoluteFill>;
}
```

استبدل YOUR_UNIT_ID بوحدة فعلية من الاسكربت. كل layout يتصمم داخل المكوّن دون تصغير نص الكمبيوتر فقط.
مفيش قائمة مغلقة للأشكال. params.assetBase يشير لأصول الدرس؛ مثال صورة `${assetBase}/assets/diagram.svg`.
استخدم frame/fps، interpolate أو Remotion hooks؛ لا ساعة مستقلة أو CSS animation للشرح المتزامن.
السؤال والإجابة يحتاجان وحدات كاملة باللغتين وتوقيتات مراجعة؛ النقص يمنع المعاينة بدل التخمين.
reasoning محفوظ في البيانات؛ لو هيتعرض أثناء نطقه، اكتب له وحدة/cue وعرضًا مخصصًا أيضًا.

## المراجعة

راجع الصوت الحقيقي والمصطلحات، التدرج، حدود البورد، السؤال أثناء قراءته، منع الإجابة قبل المحاولة،
submit → feedback → next، pause/replay/seek والأخطاء، في الشكلين وعلى موبايل حقيقي عند قبول الصوت.
نجاح البناء أو fixture CI لا يعتبر مراجعة فعلية لدرس. سجل الأدلة/reviewer في review.json.
في checks.runtime عند passed أضف runtimeVersion وruntimeArtifactHash من sdk-version.json،
واربط sourceHash بالمدخلات الحالية. إعادة كتابة السكريبت/التسجيل/المكون أو ترقية SDK تبطل المراجعة القديمة.
الصادرات تحمل هوية المحرك ومراجعتها، لكنها تظل handoff؛ استيراد المنصة والنشر لم ينفذا هنا.

## تحديث SDK

الحزمة محفوظة في new-learn/distributions باسم وإصدار واضحين؛ package.json يشير لرابط commit ثابت.
لا تستخدم main أو latest كتثبيت. لترقية: راجع نسخة جديدة وmanifest الخاص بها، حدّث الرابط في
اعتماد @learn/lesson-runtime بـnpm install --prefix preview-sdk EXACT_IMMUTABLE_TARBALL_URL،
ثم حدّث sdk-version.json من manifest مع url نفسه، واعمل commit للـlock والmetadata.
شغّل CI وأعد مراجعة الدروس المتأثرة. تحديث واحد لبيئة المعاينة، دون نسخ ملفات المحرك أو تعديل كل درس.
