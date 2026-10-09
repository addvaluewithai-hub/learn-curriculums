import {AbsoluteFill} from "remotion";
import {cueIsVisible, visibleQuestionParts, type VisualProps} from "@learn/lesson-runtime";

// Stage 04 provisional, data-driven concept board. Actual SDK compilation and 320px/browser
// review remain untested until the later runtime gate.
type BoardParams = {mode?: string; topic?: string; focus?: string; primaryUnitId?: string; feedbackOnly?: boolean};
type SpecProps = VisualProps & {spec?: {params?: BoardParams}};
const LABELS: Record<string, [string,string,string]> = {
  forces:["↑ Support","↓ Gravity","Two distinct interactions"],
  motion:["Statics: equilibrium","Dynamics: accelerating motion","Classify the question"],
  model:["Real object","Idealized model","Check the assumptions"],
  particle:["Real sensor","Particle • position","Dimensions negligible for this task"],
  rigid:["Bracket / Door","Rigid Body","Geometry kept, deformation neglected"],
  contact:["Small contact patch","Concentrated Force","Conditional global approximation"],
  balanced:["← F","F →","Net external force"],
  acceleration:["Net force ΣF","Mass m","Acceleration a"],
  interaction:["A pushes B →","← B pushes A","Forces on different bodies"],
  gravity:["mass m₁  •","r  ↔  •  mass m₂","Gravitational dependence"],
  weight:["Mass (kg)","g (m/s²)","Weight (N)"],
  fps:["SI • kg / N","FPS • slug / lbf","Mass is not force"],
  dimensions:["Mass kg","Acceleration m/s²","Force N"],
  length:["ft","× m/ft","m"],
  forceunit:["lbf","× N/lbf","N"],
  question:["Read the prompt","Think independently","Submit before feedback"]
};
export default function ConceptBoard(props: VisualProps) {
  const {frame, fps, recording, layout, phase, question, answer} = props;
  const params = (props as SpecProps).spec?.params ?? {};
  const portrait = layout === "portrait";
  const mode = String(params.mode ?? "model");
  const labels = LABELS[mode] ?? LABELS.model;
  const revealed = params.primaryUnitId ? cueIsVisible(recording, String(params.primaryUnitId), frame, fps) : false;
  const questionParts = question ? visibleQuestionParts(question, recording, frame, fps) : [];
  const answerParts = phase === "feedback" ? (answer?.parts?.filter(part => frame * 1000 / fps >= part.atMs) ?? []) : [];
  const showQuestion = phase === "question-reading" || phase === "question-attempt";
  const topic = String(params.topic ?? "Engineering Mechanics");
  const card = (value: string, i: number) => (
    <div key={i} style={{padding:portrait?"12px 14px":"18px 24px",border:"1px solid #41718a",
      background:"#173e55",borderRadius:20,textAlign:"center",fontWeight:700,fontSize:portrait?19:26,
      minWidth:0,overflowWrap:"anywhere",flex:1}}>{value}</div>
  );
  return <AbsoluteFill style={{background:"#071e30",color:"#f4fbff",
      fontFamily:"system-ui, sans-serif",padding:portrait?22:34,display:"flex",flexDirection:"column",
      gap:portrait?16:22,boxSizing:"border-box"}}>
    <div style={{fontSize:portrait?17:23,opacity:.86,fontWeight:700,overflowWrap:"anywhere"}}>{topic}</div>
    {showQuestion ? <>
      <div style={{fontSize:portrait?15:20,color:"#a5dfe7"}}>Question • Answer after your attempt</div>
      <div style={{flex:1,display:"flex",flexDirection:"column",justifyContent:"center",gap:16}}>
        {questionParts.map((part,i)=><div key={i} dir={part.language==="ar"?"rtl":"ltr"}
          style={{borderRadius:16,background:"#173e55",padding:portrait?14:22,
            fontSize:portrait?20:26,lineHeight:1.55,overflowWrap:"anywhere"}}>{part.text}</div>)}
      </div>
      <div style={{fontSize:portrait?14:18,opacity:.85}}>Submit your written attempt to unlock feedback</div>
    </> : phase==="feedback" ? <>
      <div style={{color:"#a5dfe7",fontSize:portrait?18:24}}>Feedback after submission</div>
      <div style={{flex:1,display:"flex",flexDirection:"column",gap:16,justifyContent:"center"}}>
        {answerParts.map((part,i)=><div key={i} dir={part.language==="ar"?"rtl":"ltr"}
          style={{background:"#173e55",borderRadius:16,padding:portrait?15:24,
            fontSize:portrait?19:25,lineHeight:1.55,overflowWrap:"anywhere"}}>{part.text}</div>)}
      </div>
    </> : <>
      <div style={{flex:1,display:"flex",flexDirection:portrait?"column":"row",
        justifyContent:"center",alignItems:"stretch",gap:portrait?12:24,minHeight:0}}>
        {labels.slice(0,2).map(card)}
      </div>
      <div style={{background:"#12364b",border:"1px solid #406a84",borderRadius:16,
        padding:portrait?15:23,minHeight:portrait?100:90,fontSize:portrait?22:29,fontWeight:650,
        display:"flex",alignItems:"center",justifyContent:"center",textAlign:"center",
        opacity:revealed?1:0.25,overflowWrap:"anywhere"}}>
        {revealed ? String(params.focus ?? labels[2]) : "· · ·"}
      </div>
    </>}
  </AbsoluteFill>;
}
