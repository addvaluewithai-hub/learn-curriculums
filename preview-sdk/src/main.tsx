import { createRoot } from "react-dom/client";
import { App } from "./App";
import "./style.css";
import "@learn/lesson-runtime/style.css";

createRoot(document.getElementById("root")!).render(<App />);
