import {AbsoluteFill} from "remotion";
import {cueIsVisible, visibleQuestionParts, type VisualProps} from "@learn/lesson-runtime";

type BoardParams = {title?: string; mode?: string; anchor?: string};
type SourceProps = VisualProps & {spec?: {params?: BoardParams}; visual?: {params?: BoardParams}};

// Source-grounded preview component. Display is derived from the recording frame,
// never from timers or assumed audio timings; feedback is locked to its phase.
export default function MatterBoard(props: VisualProps) {
  const {frame, fps, recording, layout, phase, question, answer} = props;
  const p = props as SourceProps;
  const params = p.spec?.params ?? p.visual?.params ?? {};
  const isPortrait = layout === "portrait";
  const reveal = params.anchor ? cueIsVisible(recording, params.anchor, frame, fps) : false;
  const qParts = question ? visibleQuestionParts(question, recording, frame, fps) : [];
  const feedbackParts = answer?.parts?.filter((part) => frame * 1000 / fps >= part.atMs) ?? [];
  const isQuestion = phase === "question-reading" || phase === "attempt";
  const isFeedback = phase === "feedback";
  const scale = isPortrait ? 20 : 24;
  return <AbsoluteFill style={{background:"#0d1b2d",color:"#f2f7ff",padding:isPortrait?24:38,fontFamily:"Arial,sans-serif",overflow:"hidden"}}>
    <div style={{fontSize:isPortrait?16:20,color:"#a9d6fc"}}>First-Year Engineering · Chemistry</div>
    {isQuestion ? <div style={{display:"flex",flexDirection:"column",gap:14,marginTop:30}}>
      <strong style={{fontSize:scale}}>Your turn · حاول بنفسك</strong>
      {qParts.map((part, i)=><div key={i} dir={part.language==="ar"?"rtl":"ltr"} style={{fontSize:scale,lineHeight:1.45,padding:12,background:"#20354f",borderRadius:12}}>{part.text}</div>)}
      <span style={{color:"#a9d6fc",fontSize:16}}>Answer remains hidden until submission</span>
    </div> : isFeedback ? <div style={{display:"flex",flexDirection:"column",gap:14,marginTop:24}}>
      <strong style={{fontSize:scale}}>Feedback · التفسير</strong>
      {feedbackParts.map((part, i)=><div key={i} dir={part.language==="ar"?"rtl":"ltr"} style={{fontSize:scale,lineHeight:1.45,padding:12,background:"#20354f",borderRadius:12}}>{part.text}</div>)}
    </div> : <div style={{marginTop:24}}>
      <strong style={{fontSize:scale}}>{params.title ?? "Matter"}</strong>
      {reveal ? <div style={{display:"flex",gap:12,justifyContent:"space-around",alignItems:"end",height:isPortrait?180:210,marginTop:18}}>
  {["Solid","Liquid","Gas"].map((name,i)=><div key={name} style={{flex:1,maxWidth:180,background:"#17304e",borderRadius:16,padding:12,textAlign:"center"}}>
    <div style={{height:78,border:"2px solid #80b8ec",borderTop:0,borderRadius:"0 0 14px 14px",display:"flex",flexWrap:"wrap",alignContent:i===2?"space-around":"end",justifyContent:"center",gap:5,padding:6}}>
    {Array.from({length:9},(_,j)=><span key={j} style={{width:12,height:12,borderRadius:i===0?3:99,background:i===0?"#9dc2f6":i===1?"#76e0d4":"#f6d791"}}/> )}</div><b style={{fontSize:isPortrait?17:20}}>{name}</b></div>)}
 </div> : <div style={{marginTop:22,color:"#a9d6fc",fontSize:isPortrait?16:18}}>The visual builds with the spoken concept.</div>}
    </div>}
  </AbsoluteFill>;
}
