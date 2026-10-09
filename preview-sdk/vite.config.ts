import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  publicDir: ".generated/public",
  resolve: {
    dedupe: [
      "react",
      "react-dom",
      "remotion",
      "@remotion/player",
      "@learn/lesson-runtime",
    ],
  },
  server: { host: "127.0.0.1", fs: { allow: [".."] } },
});
