import dotenv from "dotenv";
import { ChatOpenAI } from "@langchain/openai";

dotenv.config();

// Dummy keys if not present in the environment
const keys = ["OPENROUTER_API_KEY"];
for (const key of keys) {
  if (!process.env[key]) {
    process.env[key] = `DUMMY_${key}`;
  }
}

const openRouterConfig = {
  apiKey: process.env.OPENROUTER_API_KEY,
  configuration: { baseURL: "https://openrouter.ai/api/v1" },
  temperature: 0,
};

// 1. Fast / structured (Gemini Flash replacement)
export const geminiFlash = new ChatOpenAI({
  modelName: "meta-llama/llama-3.3-70b-instruct",
  ...openRouterConfig
});

// 2. Planner / reasoning (o3Mini replacement)
export const o3Mini = new ChatOpenAI({
  modelName: "deepseek/deepseek-chat",
  ...openRouterConfig
});

// 3. Critic / Judge (Claude Sonnet replacement)
export const claudeSonnet = new ChatOpenAI({
  modelName: "deepseek/deepseek-chat",
  ...openRouterConfig
});
