import type {CSSProperties} from "react";
import {AbsoluteFill} from "remotion";
import {cueIsVisible, visibleQuestionParts, type VisualProps} from "@learn/lesson-runtime";

type Params={title?:string;mode?:string;anchors?:string[]};
function HeatPistons({portrait}:{portrait:boolean}) {
  return <div style={{display:"flex",gap:portrait?12:44,justifyContent:"center",alignItems:"end"}}>
    {[{t:"200 K",v:"0.5 L",h:84},{t:"400 K",v:"1.0 L",h:145}].map((x,i)=>
      <div key={i} style={{display:"grid",gap:9,justifyItems:"center"}}>
        <b style={{color:"#f3d999"}}>{x.t}</b>
        <div style={{height:160,display:"flex",alignItems:"end"}}>
          <div style={{width:portrait?80:105,height:x.h,background:"#265475",
            border:"3px solid #90bcee",borderRadius:"0 0 14px 14px"}}/></div>
        <b>{x.v}</b></div>)}
  </div>;
}
export default function CharlesBoard(props:VisualProps) {
  const {spec,recording,frame,fps,layout,phase,question,answer}=props;
  const params=spec.params as Params,portrait=layout==="portrait";
  const mode=params.mode??"heat-piston",anchors=params.anchors??[];
  const show=(n:number)=>!!anchors[n]&&cueIsVisible(recording,anchors[n],frame,fps);
  const prompts=question?visibleQuestionParts(question,recording,frame,fps):[];
  const results=answer?.parts?.filter(part=>frame*1000/fps>=part.atMs)??[];
  const box:CSSProperties={background:"#203752",borderRadius:14,padding:portrait?15:20,overflowWrap:"anywhere"};
  const fs=portrait?20:24;
  return <AbsoluteFill style={{background:"#0d2134",color:"#f5f9ff",padding:portrait?24:40,
    fontFamily:"Tahoma, Arial, sans-serif",overflow:"hidden"}}>
    <div style={{fontSize:16,color:"#a6cfef"}}>Chemistry · Charles's Law</div>
    {phase==="question-reading"||phase==="feedback"?
      <div style={{display:"grid",gap:15,marginTop:28}}>{(phase==="feedback"?results:prompts).map((part,i)=>
        <div key={i} dir={part.language==="ar"?"rtl":"ltr"} style={{...box,fontSize:fs,lineHeight:1.5}}>{part.text}</div>)}</div>:
      <div style={{display:"grid",gap:portrait?15:24,marginTop:20}}>
        <b style={{fontSize:fs+1}}>{params.title??"Charles's Law"}</b>
        {mode==="heat-piston"&&show(0)?<HeatPistons portrait={portrait}/>:null}
        {mode==="heat-piston"&&show(1)?<div style={{...box,fontSize:fs}}>P fixed: V ∝ T (Kelvin)</div>:null}
        {mode==="kelvin-table"&&show(0)?<div style={{...box,fontSize:fs}}>V₁ / T₁ = V₂ / T₂</div>:null}
        {mode==="kelvin-table"&&show(1)?<div style={{...box,fontSize:fs}}>50°C → 323.15 K · 75°C → 348.15 K</div>:null}
        {mode==="kelvin-table"&&show(2)?<div style={{...box,fontSize:fs}}>21.5 × 348.15 / 323.15 ≈ 23.16 mL</div>:null}
        {mode==="rearrange-temperature"&&show(0)?<div style={{...box,fontSize:fs}}>T₂ = T₁ × V₂/V₁</div>:null}
        {mode==="rearrange-temperature"&&show(1)?<div style={{...box,fontSize:fs}}>K = °C + 273.15 · °C = K − 273.15</div>:null}
        {mode==="recap"&&show(0)?<div style={{...box,fontSize:fs}}>Boyle: T fixed, P ↔ V inverse</div>:null}
        {mode==="recap"&&show(1)?<div style={{...box,fontSize:fs}}>Charles: P fixed, V ↔ T(K) direct</div>:null}
        {mode==="recap"&&show(2)?<div style={{...box,fontSize:fs}}>Next: pressure and temperature at fixed volume</div>:null}
      </div>}
  </AbsoluteFill>;
}
