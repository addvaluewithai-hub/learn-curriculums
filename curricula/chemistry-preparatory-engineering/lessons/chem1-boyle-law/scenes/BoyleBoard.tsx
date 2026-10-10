import type {CSSProperties} from "react";
import {AbsoluteFill} from "remotion";
import {cueIsVisible, visibleQuestionParts, type VisualProps} from "@learn/lesson-runtime";

type Params={title?:string;mode?:string;anchors?:string[]};
function Pistons({portrait}:{portrait:boolean}) {
  return <div style={{display:"flex",gap:portrait?12:44,justifyContent:"center",alignItems:"end"}}>
    {[{p:"1 atm",v:"1.0 L",h:140},{p:"2 atm",v:"0.5 L",h:85}].map((x,i)=>
      <div key={i} style={{display:"grid",gap:9,justifyItems:"center"}}>
        <b style={{color:"#f7d695"}}>{x.p}</b>
        <div style={{height:155,display:"flex",alignItems:"end"}}><div style={{width:portrait?80:105,
          height:x.h,border:"3px solid #8ebdf1",background:"#265475",borderRadius:"0 0 13px 13px",
          position:"relative"}}><div style={{position:"absolute",top:0,width:"100%",height:8,background:"#e9f4ff"}}/></div></div>
        <b>{x.v}</b></div>)}
  </div>;
}
function Plot({reciprocal}:{reciprocal:boolean}) {
  const pts=Array.from({length:16},(_,i)=> {
    const x=18+i*11, y=reciprocal?118-i*6:126-120/(1+i*0.22);
    return `${x},${y}`;
  }).join(" ");
  return <div style={{display:"grid",gap:5,justifyItems:"center"}}>
    <svg width="215" height="148" viewBox="0 0 215 148" role="img" aria-label={reciprocal?"Volume versus inverse pressure":"Volume versus pressure"}>
      <line x1="16" y1="130" x2="200" y2="130" stroke="#accded" strokeWidth="3"/>
      <line x1="16" y1="130" x2="16" y2="8" stroke="#accded" strokeWidth="3"/>
      <polyline points={pts} fill="none" stroke="#6ed9d0" strokeWidth="4"/>
      <text x="2" y="16" fill="#f3f8ff" fontSize="15">V</text>
      <text x="176" y="145" fill="#f3f8ff" fontSize="14">{reciprocal?"1/P":"P"}</text>
    </svg>
    <b>{reciprocal?"V ∝ 1/P (straight line)":"V vs P (curve)"}</b>
  </div>;
}
export default function BoyleBoard(props:VisualProps) {
  const {spec,recording,frame,fps,layout,phase,question,answer}=props;
  const params=spec.params as Params;
  const portrait=layout==="portrait",mode=params.mode??"piston";
  const anchors=params.anchors??[];
  const visible=(n:number)=>!!anchors[n]&&cueIsVisible(recording,anchors[n],frame,fps);
  const pparts=question?visibleQuestionParts(question,recording,frame,fps):[];
  const aparts=answer?.parts?.filter(part=>frame*1000/fps>=part.atMs)??[];
  const panel:CSSProperties={padding:portrait?14:20,borderRadius:14,background:"#203650",overflowWrap:"anywhere"};
  const fs=portrait?20:24;
  return <AbsoluteFill style={{background:"#0d2134",color:"#f1f7ff",fontFamily:"Tahoma, Arial, sans-serif",
    padding:portrait?24:40,overflow:"hidden"}}>
    <div style={{fontSize:16,color:"#a5c9ec"}}>Chemistry · Boyle's Law</div>
    {phase==="question-reading"||phase==="feedback"?
      <div style={{marginTop:30,display:"grid",gap:16}}>{(phase==="feedback"?aparts:pparts).map((part,i)=>
        <div key={i} dir={part.language==="ar"?"rtl":"ltr"} style={{...panel,fontSize:fs,lineHeight:1.5}}>{part.text}</div>)}</div>:
      <div style={{display:"grid",gap:portrait?14:23,marginTop:20}}>
        <b style={{fontSize:fs+1}}>{params.title??"Boyle's Law"}</b>
        {mode==="piston"&&visible(0)?<Pistons portrait={portrait}/>:null}
        {mode==="piston"&&visible(1)?<div style={{...panel,fontSize:fs}}>P and V vary; amount of gas and T are fixed</div>:null}
        {mode==="inverse-graph"&&visible(0)?<div style={{...panel,fontSize:fs+2,textAlign:"center"}}>P₁V₁ = P₂V₂</div>:null}
        {mode==="inverse-graph"&&visible(1)?<div style={{display:"flex",flexDirection:portrait?"column":"row",gap:16,justifyContent:"space-around"}}>
          <Plot reciprocal={false}/><Plot reciprocal={true}/></div>:null}
        {mode==="worked-boyle"&&visible(0)?<div style={{...panel,fontSize:fs}}>P₁ 3.500 atm → P₂ 2.500 atm</div>:null}
        {mode==="worked-boyle"&&visible(1)?<div style={{...panel,fontSize:fs}}>V₂ = (3.500 × 18.10) / 2.500 = 25.34 mL</div>:null}
        {mode==="worked-boyle"&&visible(2)?<div style={{...panel,fontSize:fs}}>Pressure doubles: 12 L → 6 L (book answer needs correction)</div>:null}
        {mode==="recap"&&visible(0)?<div style={{...panel,fontSize:fs}}>Constant temperature: Boyle → inverse P–V</div>:null}
        {mode==="recap"&&visible(1)?<div style={{...panel,fontSize:fs}}>Next: constant pressure → Charles's Law</div>:null}
      </div>}
  </AbsoluteFill>;
}
