import {cueIsVisible, visibleQuestionParts, type VisualProps} from '@learn/lesson-runtime';
type Extras = {spec?: {params?: {heading?: string;kind?: string;formula?: string;firstCue?: string}}};
export default function ConceptBoard(props: VisualProps) {
  const {frame,fps,recording,layout,phase,question,answer} = props;
  const meta = (props as VisualProps & Extras).spec?.params ?? {};
  const portrait = layout==='portrait';
  const unlocked = meta.firstCue ? cueIsVisible(recording, meta.firstCue, frame, fps) : false;
  const reading = question ? visibleQuestionParts(question, recording, frame, fps) : [];
  const answers = answer?.parts?.filter(part => frame*1000/fps >= part.atMs) ?? [];
  const asking = Boolean(question) && phase!=='feedback';
  return <div dir="rtl" style={{background:'#0b1727',color:'#f5faff',width:'100%',height:'100%',boxSizing:'border-box',
    padding:portrait?'9% 7%':'6% 8%',display:'flex',flexDirection:'column',justifyContent:'center',gap:portrait?16:23,
    fontFamily:'system-ui, sans-serif'}}>
    <div style={{fontSize:portrait?15:19,color:'#a4d3e2'}}>PHYSICS I — {meta.kind?.toUpperCase() ?? 'CONCEPT'}</div>
    <div style={{fontSize:portrait?30:42,fontWeight:750,lineHeight:1.27}}>
      {asking?'جرّب تحل':phase==='feedback'?'نفسّر الإجابة':(meta.heading||'إيه نوع التشوّه؟')}</div>
    {!question && <svg viewBox="0 0 420 160" role="img" aria-label="توضيح نوع التشوّه" style={{width:'100%',height:portrait?126:168,
      border:'1px solid #41647b',borderRadius:16,background:'#12293e'}}>
       {meta.kind==='bulk'||meta.kind==='pressure'?
        <><rect x="148" y="42" width="116" height="85" rx="18" fill="#3b7c9b" stroke="#8be0ed" strokeWidth="4"/>
        <path d="M205 8 V34 M205 152 V137 M95 82 H140 M314 82 H270" stroke="#f7c477" strokeWidth="6" strokeLinecap="round"/>
        <path d="M193 25 L205 38 L217 25 M193 145 L205 132 L217 145 M132 71 L145 82 L132 93 M280 71 L267 82 L280 93" fill="none" stroke="#f7c477" strokeWidth="5"/></>:
        <><path d="M128 125 L275 125 L306 49 L159 49 Z" fill="#2b657d" stroke="#8be0ed" strokeWidth="4"/>
        <path d="M143 47 L308 47" stroke="#fff1ba" strokeWidth="5"/>
        <path d="M215 23 H327" stroke="#f7c477" strokeWidth="6" strokeLinecap="round"/>
        <path d="M316 12 L336 23 L316 34" fill="none" stroke="#f7c477" strokeWidth="6"/>
        <path d="M98 133 H330" stroke="#84bdc9" strokeWidth="4"/></>}
      </svg>}
    {asking ? <div dir="ltr" style={{fontSize:portrait?19:25,lineHeight:1.55,overflowWrap:'anywhere'}}>
       {reading.map((part,i)=><p key={i} dir={/[؀-ۿ]/.test(part.text)?'rtl':'ltr'}>{part.text}</p>)}</div> :
      phase==='feedback'?
       <div style={{fontSize:portrait?19:24,lineHeight:1.5,overflowWrap:'anywhere'}}>
         {answers.map((part,i)=><p key={i}>{part.text}</p>)}</div>:
       <div style={{fontSize:portrait?25:37,fontWeight:650}}>
         {unlocked?(meta.formula||'لاحظ اتجاه الحمل ومسار التشوّه'):'تابع الرسم مع الصوت'}</div>}
    <div style={{fontSize:portrait?14:17,color:'#b8d0df'}}>
      {asking?'الإجابة لا تظهر قبل التسليم':phase==='feedback'?'Feedback بعد محاولة الطالب':'المعلومة تظهر عند عبارة الشرح المرتبطة بها'}
    </div>
  </div>;
}
