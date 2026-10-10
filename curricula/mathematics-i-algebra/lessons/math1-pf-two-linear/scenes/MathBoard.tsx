import React from 'react';
import { AbsoluteFill } from 'remotion';
import { cueIsVisible, type VisualProps } from '@learn/lesson-runtime';

// Stage 04 editable visual component; unrendered until media/timing review.
// Storyboards in scenes/*.json define the independent responsive intention.
const panels = [
  { cue: "S01-U01", label: "هوية البسط وحساب الثوابت", note: "ابدأ من: في الدرس اللي فات قدرت تعرف صورة تفكيك كسر من تحليل المقام، لكن" },
  { cue: "S01-U02", label: "هوية البسط وحساب الثوابت", note: "ثم راجع: أعمل إيه علشان أعرف قيمتهم؟»" },
  { cue: "S02-U01", label: "هوية البسط وحساب الثوابت", note: "ابدأ من: نمشي على Example 4 في الكتاب، صفحة 4. السؤال: خمسة إكس زائد واحد" },
  { cue: "S02-U02", label: "هوية البسط وحساب الثوابت", note: "ثم راجع: السؤال: خمسة إكس زائد واحد على إكس تربيع ناقص إكس ناقص اتناشر" },
  { cue: "S03-U01", label: "هوية البسط وحساب الثوابت", note: "ابدأ من: خلينا نكتب الكلام ده بوضوح: خمسة إكس زائد واحد، تساوي A مضروبة في" },
  { cue: "S03-U02", label: "هوية البسط وحساب الثوابت", note: "ثم راجع: دي مش مجرد معادلة عند رقم واحد؛ دي Polynomial Identity، هوية كثيرات حدود" },
  { cue: "S04-U01", label: "هوية البسط وحساب الثوابت", note: "ابدأ من: إيه أذكى قيمة نبدأ بيها؟ عايزين نلغي B، وهو مضروب في إكس ناقص" },
  { cue: "S04-U02", label: "هوية البسط وحساب الثوابت", note: "ثم راجع: عايزين نلغي B، وهو مضروب في إكس ناقص أربعة؛ إذن في هوية البسط" },
  { cue: "S05-U01", label: "هوية البسط وحساب الثوابت", note: "ابدأ من: خلص الحساب، لكن لسه ما خلصش التحقق. اكتب الناتج: تلاتة على إكس ناقص" },
  { cue: "S05-U02", label: "هوية البسط وحساب الثوابت", note: "ثم راجع: اكتب الناتج: تلاتة على إكس ناقص أربعة، زائد اتنين على إكس زائد تلاتة" },
  { cue: "S06-U01", label: "هوية البسط وحساب الثوابت", note: "ابدأ من: خلينا نعمل تجربة صغيرة من إعدادنا، مش من الكتاب، علشان تشوف إن الطريقة" },
  { cue: "S06-U02", label: "هوية البسط وحساب الثوابت", note: "ثم راجع: هنفترض A على إكس ناقص واحد زائد B على إكس زائد أربعة" },
  { cue: "S08-U01", label: "هوية البسط وحساب الثوابت", note: "ابدأ من: دلوقتي أنت مش بس بتكتب القالب؛ أنت عرفت إزاي تحلّه وتتحقق منه. اتعلمنا" },
  { cue: "S08-U02", label: "هوية البسط وحساب الثوابت", note: "ثم راجع: اتعلمنا هوية البسط، وفرقنا بينها وبين مجال الكسر، واخترنا قيمًا ذكية علشان نطلع" },
];

export default function MathBoard(props: VisualProps) {
  const { recording, frame, fps, layout, phase } = props;
  const portrait = layout === 'portrait';
  // This component is used for teaching only. Questions use the SDK question board.
  const visible = phase === 'feedback' || phase === 'question-reading'
    ? []
    : panels.filter((p) => cueIsVisible(recording, p.cue, frame, fps));
  const active = visible.length ? visible[visible.length - 1] : null;
  return (
    <AbsoluteFill style={{ backgroundColor: '#0e1826', color: 'white', padding: portrait ? 22 : 48, display: 'flex', flexDirection: 'column', justifyContent: 'center', gap: portrait ? 18 : 28, overflow: 'hidden', fontFamily: 'sans-serif' }}>
      <div style={{fontSize: portrait ? 17 : 24, opacity: .8, letterSpacing: 1}}>Mathematics I · Partial Fractions</div>
      <div style={{height: 3, width: portrait ? '45%' : '25%', backgroundColor: '#67e8f9'}} />
      <div style={{display: 'grid', gridTemplateColumns: portrait ? '1fr' : '1fr 1fr', gap: 18, alignItems: 'center'}}>
        <div style={{fontSize: portrait ? 31 : 45, fontWeight: 700, lineHeight: 1.3, overflowWrap: 'anywhere'}} dir="rtl">
          {active?.label || 'تابع الفكرة خطوة بخطوة'}
        </div>
        <div style={{fontSize: portrait ? 19 : 27, lineHeight: 1.5, padding: portrait ? 16 : 28, backgroundColor: '#17283d', borderRadius: 18, border: '1px solid #37506a'}} dir="rtl">
          {active?.note || 'العناصر تظهر مع الشرح المسموع'}
        </div>
      </div>
      <div style={{fontSize: portrait ? 14 : 17, opacity: .66}} dir="rtl">المعادلات التفصيلية تُعرض في البورد وفق storyboard؛ لا توقيت مفترض قبل التسجيل.</div>
    </AbsoluteFill>
  );
}
