import {AbsoluteFill} from "remotion";
import {cueIsVisible, visibleQuestionParts, type VisualProps} from "@learn/lesson-runtime";

type BoardParams = {title?: string; mode?: string; anchor?: string};
type SourceProps = VisualProps & {spec?: {params?: BoardParams}; visual?: {params?: BoardParams}};

// Source-grounded preview component. Display is derived from the recording frame,
// never from timers or assumed audio timings; feedback is locked to its phase.
export default function CharlesBoard(props: VisualProps) {
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
      <strong style={{fontSize:scale}}>{params.title ?? "Charles"}</strong>
      {reveal ? <div style={{display:"flex",gap:14,justifyContent:"center",alignItems:"end",marginTop:18}}>
 {[{t:"200 K",v:"0.5 L",h:85},{t:"400 K",v:"1.0 L",h:145}].map((x,i)=><div key={i} style={{flex:1,maxWidth:160,textAlign:"center"}}><b style={{color:"#ffde91"}}>{x.t}</b><div style={{height:160,display:"flex",alignItems:"end",justifyContent:"center"}}><div style={{width:85,height:x.h,border:"3px solid #83b6f1",borderRadius:"0 0 15px 15px",background:"#255579"}}/></div><b>{x.v}</b></div>)}</div> : <div style={{marginTop:22,color:"#a9d6fc",fontSize:isPortrait?16:18}}>The visual builds with the spoken concept.</div>}
    </div>}
  </AbsoluteFill>;
}
