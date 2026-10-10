import {cueIsVisible, visibleQuestionParts, type VisualProps} from '@learn/lesson-runtime';
type Extras = {spec?: {params?: {heading?: string; kind?: string; formula?: string; firstCue?: string}}};
export default function ConceptBoard(props: VisualProps) {
  const {frame, fps, recording, layout, phase, question, answer} = props;
  const meta = (props as VisualProps & Extras).spec?.params ?? {};
  const portrait = layout === 'portrait';
  const ready = meta.firstCue ? cueIsVisible(recording, meta.firstCue, frame, fps) : false;
  const reading = question ? visibleQuestionParts(question, recording, frame, fps) : [];
  const feedback = answer?.parts?.filter(part => frame * 1000 / fps >= part.atMs) ?? [];
  const questionPhase = Boolean(question) && phase !== 'feedback';
  const kind = meta.kind ?? 'concept';
  return <div dir="rtl" style={{boxSizing:'border-box',width:'100%',height:'100%',
    background:'#0b1625',color:'#f2f7ff',display:'flex',flexDirection:'column',
    justifyContent:'center',alignItems:'stretch',gap:portrait?16:22,
    padding:portrait?'8% 7%':'6% 8%',fontFamily:'system-ui, sans-serif'}}>
    <div style={{fontSize:portrait?15:18,color:'#a4c6d8',letterSpacing:1}}>
      PHYSICS I — {kind.toUpperCase()}
    </div>
    <div style={{fontSize:portrait?29:40,fontWeight:700,lineHeight:1.3}}>
      {questionPhase?'سؤال مستقل':phase==='feedback'?'نفهم الإجابة':(meta.heading ?? 'فكّر في الفكرة')}
    </div>
    {!question && <div aria-hidden style={{height:portrait?105:145,display:'flex',
      justifyContent:'center',alignItems:'center',gap:portrait?13:22,
      border:'1px solid #31516b',borderRadius:18,background:'#122940'}}>
      {['●','↔','▱'].map((symbol,i)=><span key={i} style={{fontSize:portrait?44:62,
        transform:i===2?'skew(-12deg)':'none',color:i===1?'#f7c777':'#8bdacf'}}>{symbol}</span>)}
    </div>}
    {questionPhase ? <div style={{fontSize:portrait?19:25,lineHeight:1.6,
       direction:'ltr',textAlign:'start',overflowWrap:'anywhere'}}>
       {reading.map((part,i)=><p key={i} dir={/[؀-ۿ]/.test(part.text)?'rtl':'ltr'}>{part.text}</p>)}
      </div> :
     phase==='feedback'?<div style={{fontSize:portrait?19:24,lineHeight:1.55,
        overflowWrap:'anywhere'}}>{feedback.map((part,i)=><p key={i}>{part.text}</p>)}</div>:
     <div style={{fontSize:portrait?25:34,fontWeight:600,lineHeight:1.5}}>
       {ready ? (meta.formula || 'افهم التحميل ونوع التشوّه قبل القانون') : 'لاحظ الرسمة مع الشرح'}
     </div>}
    <div style={{fontSize:portrait?14:17,color:'#b6d0de'}}>
      {questionPhase?'السؤال والشرح فقط — الإجابة بعد المحاولة':phase==='feedback'?'الإجابة ظهرت بعد إرسال المحاولة':'كل فكرة تظهر مع بداية شرحها'}
    </div>
  </div>;
}
