import {AbsoluteFill} from "remotion";
import {cueIsVisible, visibleQuestionParts, type VisualProps} from "@learn/lesson-runtime";

type BoardParams = {title?: string; mode?: string; anchor?: string};
type SourceProps = VisualProps & {spec?: {params?: BoardParams}; visual?: {params?: BoardParams}};

// Source-grounded preview component. Display is derived from the recording frame,
// never from timers or assumed audio timings; feedback is locked to its phase.
export default function BoyleBoard(props: VisualProps) {
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
      <strong style={{fontSize:scale}}>{params.title ?? "Boyle"}</strong>
      {reveal ? <div style={{display:"flex",gap:14,marginTop:18,alignItems:"end",justifyContent:"center"}}>
  {[{p:"1 atm",v:"1.0 L",h:140},{p:"2 atm",v:"0.5 L",h:90}].map((x,i)=><div key={i} style={{textAlign:"center",flex:1,maxWidth:160}}>
    <div style={{color:"#f6d791",fontWeight:700}}>{x.p}</div>
    <div style={{height:155,display:"flex",alignItems:"end",justifyContent:"center"}}><div style={{border:"3px solid #89bbeb",width:82,height:x.h,background:"#244d78",borderRadius:"0 0 12px 12px",position:"relative"}}><div style={{height:8,background:"#e3edf9",position:"absolute",width:"100%",top:0}}/></div></div>
    <b>{x.v}</b></div>)}</div> : <div style={{marginTop:22,color:"#a9d6fc",fontSize:isPortrait?16:18}}>The visual builds with the spoken concept.</div>}
    </div>}
  </AbsoluteFill>;
}
