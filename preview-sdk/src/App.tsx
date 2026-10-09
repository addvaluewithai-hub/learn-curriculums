import { lazy, Suspense, useState } from "react";
import { runtimeVersion, type LessonLayout } from "@learn/lesson-runtime/core";
import catalog from "../.generated/catalog.json";
import type { Entry } from "./loadLesson";

const entries: Entry[] = catalog.entries;
const PreviewLesson = lazy(() => import("./PreviewLesson"));
export function App() {
  const [selected, setSelected] = useState(entries[0]?.key ?? "");
  const [layout, setLayout] = useState<LessonLayout | "auto">("auto");
  const entry = entries.find((item) => item.key === selected);
  if (runtimeVersion !== catalog.sdk.version)
    return (
      <p role="alert">
        إصدار المحرك مختلف عن نسخة المعاينة. شغّل npm ci وأعد تجهيزها.
      </p>
    );
  return (
    <main>
      <header className="preview-header">
        <h1>معاينة المناهج</h1>
        <p>
          مساحة مراجعة مؤقتة بصوت وبورد وأسئلة. النشر واعتماد المحتوى خطوة
          منفصلة.
        </p>
        <span>المحرك {runtimeVersion}</span>
      </header>
      {entries.length === 0 ? (
        <p role="status">
          لسه مفيش دروس في curricula. ابدأ التأليف؛ المعاينة تشتغل بعد اكتمال
          التسجيلات والتوقيتات والمكونات.
        </p>
      ) : (
        <div className="picker">
          <label>
            الدرس{" "}
            <select
              value={selected}
              onChange={(event) => setSelected(event.target.value)}
            >
              {entries.map((item) => (
                <option key={item.key} value={item.key}>
                  {item.curriculumId} · {item.order}.{" "}
                  {item.title ?? item.lessonId}
                  {item.ready ? "" : " — يحتاج تجهيز"}
                </option>
              ))}
            </select>
          </label>
          <label>
            العرض{" "}
            <select
              value={layout}
              onChange={(event) =>
                setLayout(event.target.value as typeof layout)
              }
            >
              <option value="auto">حسب الشاشة</option>
              <option value="landscape">كمبيوتر 16:9</option>
              <option value="portrait">موبايل 9:16</option>
            </select>
          </label>
        </div>
      )}
      {entry ? (
        <Suspense fallback={<p role="status">بنحمّل المحرك…</p>}>
          <PreviewLesson
            key={entry.key}
            entry={entry}
            layout={layout === "auto" ? undefined : layout}
          />
        </Suspense>
      ) : null}
    </main>
  );
}
