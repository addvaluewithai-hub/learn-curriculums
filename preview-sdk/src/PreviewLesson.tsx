import { useEffect, useState } from "react";
import { LessonPreview, type LessonLayout } from "@learn/lesson-runtime";
import { loadLesson, type Entry } from "./loadLesson";

export default function PreviewLesson({
  entry,
  layout,
}: {
  entry: Entry;
  layout?: LessonLayout;
}) {
  const [loaded, setLoaded] = useState<Awaited<
    ReturnType<typeof loadLesson>
  > | null>(null);
  const [error, setError] = useState("");
  useEffect(() => {
    const controller = new AbortController();
    setLoaded(null);
    setError("");
    loadLesson(entry, controller.signal).then(
      (result) => {
        if (!controller.signal.aborted) setLoaded(result);
      },
      (reason) => {
        if (!controller.signal.aborted)
          setError(String(reason.message ?? reason));
      },
    );
    return () => controller.abort();
  }, [entry]);
  if (error) return <p role="alert">{error}</p>;
  if (!loaded) return <p role="status">بنجهّز المعاينة…</p>;
  return (
    <>
      <details className="provenance">
        <summary>هوية النسخة تحت المراجعة</summary>
        <p>المحرك: {loaded.provenance.runtimeVersion}</p>
        <p>
          المصدر: <code>{loaded.provenance.sourceHash}</code>
        </p>
        <p>نجاح التشغيل هنا يحتاج مراجعة فعلية وتسجيل الأدلة في review.json.</p>
      </details>
      <LessonPreview
        lesson={loaded.lesson}
        registry={loaded.registry}
        layout={layout}
      />
    </>
  );
}
