import React from 'react';
import { AbsoluteFill } from 'remotion';
import { cueIsVisible, type VisualProps } from '@learn/lesson-runtime';

// Stage 04 editable visual component; unrendered until media/timing review.
// Storyboards in scenes/*.json define the independent responsive intention.
const panels = [
  { cue: "S01-U01", label: "جسر الكسر الجبري والدرجة والمجال", note: "ابدأ من: فاكر لما كنت بتجمع كسرين بمقامين مختلفين؟ أول حاجة بتجيب المقام المشترك، وبعدين" },
  { cue: "S01-U02", label: "جسر الكسر الجبري والدرجة والمجال", note: "ثم راجع: أول حاجة بتجيب المقام المشترك، وبعدين تجمع البسطين وتطلع بكسر واحد" },
  { cue: "S02-U01", label: "جسر الكسر الجبري والدرجة والمجال", note: "ابدأ من: إزاي نعرف إن دي نفس القيمة؟ نرجع للعملية اللي بتعرفها: وحّد المقامين. البسط" },
  { cue: "S02-U02", label: "جسر الكسر الجبري والدرجة والمجال", note: "ثم راجع: نرجع للعملية اللي بتعرفها: وحّد المقامين" },
  { cue: "S03-U01", label: "جسر الكسر الجبري والدرجة والمجال", note: "ابدأ من: لما يبقى عندك بسط ومقام كل واحد فيهم Polynomial، والمقام مش كثيرة الحدود" },
  { cue: "S03-U02", label: "جسر الكسر الجبري والدرجة والمجال", note: "ثم راجع: لاحظ كلمة «نسبة»: طول ما المقام عند قيمة معينة بيساوي صفر، الكسر غير" },
  { cue: "S04-U01", label: "جسر الكسر الجبري والدرجة والمجال", note: "ابدأ من: بص على مثال الكتاب: إكس تربيع على إكس تربيع زائد اتنين. ده Improper" },
  { cue: "S04-U02", label: "جسر الكسر الجبري والدرجة والمجال", note: "ثم راجع: ده Improper لأن درجة البسط ودرجة المقام اتنين" },
  { cue: "S05-U01", label: "جسر الكسر الجبري والدرجة والمجال", note: "ابدأ من: خلينا نعمل اختبارين صغيرين، مش حفظ. الأول عن رجوع الكسور بعضها لبعض، والتاني" },
  { cue: "S05-U02", label: "جسر الكسر الجبري والدرجة والمجال", note: "ثم راجع: الأول عن رجوع الكسور بعضها لبعض، والتاني عن الدرجات اللي بتحدد أول خطوة" },
  { cue: "S08-U01", label: "جسر الكسر الجبري والدرجة والمجال", note: "ابدأ من: إذن فكرة Partial Fractions هي العملية العكسية لتوحيد المقامات، وإن أي مساواة بنكتبها" },
  { cue: "S08-U02", label: "جسر الكسر الجبري والدرجة والمجال", note: "ثم راجع: واتعلمنا المصطلحات Polynomial وDegree وRational Fraction، والفرق بين Proper وImproper" },
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
