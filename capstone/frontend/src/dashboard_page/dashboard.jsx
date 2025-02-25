import React, { useEffect, useState } from "react";
import { Barchart, Piechart } from "./components/charts";

const Dashboard = () => {
  const [dashboardData, setDashboardData] = useState({
    totalChats: 1200,
    uniqueUsers: 450,
    averageSessionDuration: 5.2,
    aiAccuracy: 92.5,
    dailyUsers: [
      { day: "2025-02-20", users: 120 },
      { day: "2025-02-21", users: 150 },
      { day: "2025-02-22", users: 180 },
      { day: "2025-02-23", users: 200 },
      { day: "2025-02-24", users: 250 },
      { day: "2025-02-25", users: 300 }
    ],
    categoryDistribution: [
      { category: "FA", value: 300 },
      { category: "PA", value: 250 },
      { category: "MA", value: 200 },
      { category: "IOT", value: 150 },
      { category: "Other", value: 100 }
    ],
    chatHistory: [
      { model: "GPT-4", prompt: "General", question: "What is AI?", answer: "AI stands for Artificial Intelligence.", time_usage: "1.2s", ask_at: "2025-02-25 10:00" },
      { model: "GPT-4", prompt: "Technical", question: "Explain Neural Networks", answer: "Neural Networks are...", time_usage: "2.5s", ask_at: "2025-02-25 10:05" },
      { model: "GPT-4", prompt: "General", question: "What is AI?", answer: "AI stands for Artificial Intelligence.", time_usage: "1.2s", ask_at: "2025-02-25 10:00" },
      { model: "GPT-4", prompt: "Technical", question: "Explain Neural Networks", answer: "Neural Networks are...", time_usage: "2.5s", ask_at: "2025-02-25 10:05" },
      { model: "GPT-4", prompt: "General", question: "What is AI?", answer: "AI stands for Artificial Intelligence.", time_usage: "1.2s", ask_at: "2025-02-25 10:00" },
      { model: "GPT-4", prompt: "Technical", question: "Explain Neural Networks", answer: "Neural Networks are...", time_usage: "2.5s", ask_at: "2025-02-25 10:05" },
      { model: "GPT-4", prompt: "General", question: "What is AI?", answer: "AI stands for Artificial Intelligence.", time_usage: "1.2s", ask_at: "2025-02-25 10:00" },
      { model: "GPT-4", prompt: "Technical", question: "Explain Neural Networks", answer: "Neural Networks are...", time_usage: "2.5s", ask_at: "2025-02-25 10:05" },
      { model: "GPT-4", prompt: "General", question: "What is AI?", answer: "AI stands for Artificial Intelligence.", time_usage: "1.2s", ask_at: "2025-02-25 10:00" },
      { model: "GPT-4", prompt: "Technical", question: "Explain Neural Networks", answer: "Neural Networks are...", time_usage: "2.5s", ask_at: "2025-02-25 10:05" },
      { model: "GPT-4", prompt: "General", question: "What is AI?", answer: "AI stands for Artificial Intelligence.", time_usage: "1.2s", ask_at: "2025-02-25 10:00" },
      { model: "GPT-4", prompt: "Technical", question: "Explain Neural Networks", answer: "Neural Networks are...", time_usage: "2.5s", ask_at: "2025-02-25 10:05" },
      { model: "GPT-4", prompt: "General", question: "What is AI?", answer: "AI stands for Artificial Intelligence.", time_usage: "1.2s", ask_at: "2025-02-25 10:00" },
      { model: "GPT-4", prompt: "Technical", question: "Explain Neural Networks", answer: "Neural Networks are...", time_usage: "2.5s", ask_at: "2025-02-25 10:05" },
      { model: "GPT-4", prompt: "General", question: "What is AI?", answer: "AI stands for Artificial Intelligence.", time_usage: "1.2s", ask_at: "2025-02-25 10:00" },
      { model: "GPT-4", prompt: "Technical", question: "Explain Neural Networks", answer: "Neural Networks are...", time_usage: "2.5s", ask_at: "2025-02-25 10:05" },
      { model: "GPT-4", prompt: "General", question: "How to learn React?", answer: "Start with React docs...", time_usage: "1.8s", ask_at: "2025-02-25 10:10" }
    ],
    documents: [
      { name: "AI_Whitepaper.pdf", pages: 25, time_usage: "5s", upload_at: "2025-02-24 15:30", ids: "doc12345", embedding_model: "BERT" },
      { name: "AI_Whitepaper.pdf", pages: 25, time_usage: "5s", upload_at: "2025-02-24 15:30", ids: "doc12345", embedding_model: "BERT" },
      { name: "AI_Whitepaper.pdf", pages: 25, time_usage: "5s", upload_at: "2025-02-24 15:30", ids: "doc12345", embedding_model: "BERT" },
      { name: "AI_Whitepaper.pdf", pages: 25, time_usage: "5s", upload_at: "2025-02-24 15:30", ids: "doc12345", embedding_model: "BERT" },
      { name: "AI_Whitepaper.pdf", pages: 25, time_usage: "5s", upload_at: "2025-02-24 15:30", ids: "doc12345", embedding_model: "BERT" },
      { name: "AI_Whitepaper.pdf", pages: 25, time_usage: "5s", upload_at: "2025-02-24 15:30", ids: "doc12345", embedding_model: "BERT" },
      { name: "AI_Whitepaper.pdf", pages: 25, time_usage: "5s", upload_at: "2025-02-24 15:30", ids: "doc12345", embedding_model: "BERT" },
      { name: "AI_Whitepaper.pdf", pages: 25, time_usage: "5s", upload_at: "2025-02-24 15:30", ids: "doc12345", embedding_model: "BERT" },
      { name: "AI_Whitepaper.pdf", pages: 25, time_usage: "5s", upload_at: "2025-02-24 15:30", ids: "doc12345", embedding_model: "BERT" },
      { name: "AI_Whitepaper.pdf", pages: 25, time_usage: "5s", upload_at: "2025-02-24 15:30", ids: "doc12345", embedding_model: "BERT" },
      { name: "AI_Whitepaper.pdf", pages: 25, time_usage: "5s", upload_at: "2025-02-24 15:30", ids: "doc12345", embedding_model: "BERT" },
      { name: "AI_Whitepaper.pdf", pages: 25, time_usage: "5s", upload_at: "2025-02-24 15:30", ids: "doc12345", embedding_model: "BERT" },
      { name: "AI_Whitepaper.pdf", pages: 25, time_usage: "5s", upload_at: "2025-02-24 15:30", ids: "doc12345", embedding_model: "BERT" },
      { name: "AI_Whitepaper.pdf", pages: 25, time_usage: "5s", upload_at: "2025-02-24 15:30", ids: "doc12345", embedding_model: "BERT" },
      { name: "AI_Whitepaper.pdf", pages: 25, time_usage: "5s", upload_at: "2025-02-24 15:30", ids: "doc12345", embedding_model: "BERT" },
      { name: "AI_Whitepaper.pdf", pages: 25, time_usage: "5s", upload_at: "2025-02-24 15:30", ids: "doc12345", embedding_model: "BERT" },
      { name: "AI_Whitepaper.pdf", pages: 25, time_usage: "5s", upload_at: "2025-02-24 15:30", ids: "doc12345", embedding_model: "BERT" },
      { name: "AI_Whitepaper.pdf", pages: 25, time_usage: "5s", upload_at: "2025-02-24 15:30", ids: "doc12345", embedding_model: "BERT" },
      { name: "AI_Whitepaper.pdf", pages: 25, time_usage: "5s", upload_at: "2025-02-24 15:30", ids: "doc12345", embedding_model: "BERT" },
      { name: "AI_Whitepaper.pdf", pages: 25, time_usage: "5s", upload_at: "2025-02-24 15:30", ids: "doc12345", embedding_model: "BERT" },
      { name: "Deep_Learning.pdf", pages: 60, time_usage: "12s", upload_at: "2025-02-24 16:00", ids: "doc67890", embedding_model: "GPT-Embed" }
    ]
  });

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <h2 className="text-3xl font-bold mb-6">Dashboard</h2>
      
      {/* Barchart: จำนวนผู้ใช้งานในแต่ละวัน */}
      <div className="bg-white rounded-lg p-4 shadow-md mb-6">
        <h3 className="text-lg font-bold mb-2">Daily User</h3>
        <Barchart data={dashboardData.dailyUsers} />
      </div>

      {/* Piechart: Category Distribution */}
      <div className="bg-white rounded-lg p-4 shadow-md mb-6">
        <h3 className="text-lg font-bold mb-2">Category</h3>
        <Piechart data={dashboardData.categoryDistribution} />
      </div>
      
      {/* Summary */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-6">
        <div className="bg-white shadow-md rounded-lg p-4 text-center">
          <p className="text-gray-500">จำนวนแชททั้งหมด</p>
          <h2 className="text-xl font-bold text-purple-700">{dashboardData.totalChats}</h2>
        </div>
        <div className="bg-white shadow-md rounded-lg p-4 text-center">
          <p className="text-gray-500">จำนวนผู้ใช้ที่สนทนา</p>
          <h2 className="text-xl font-bold text-purple-700">{dashboardData.uniqueUsers}</h2>
        </div>
        <div className="bg-white shadow-md rounded-lg p-4 text-center">
          <p className="text-gray-500">ค่าเฉลี่ยเวลาการสนทนา (นาที)</p>
          <h2 className="text-xl font-bold text-purple-700">{dashboardData.averageSessionDuration}</h2>
        </div>
        <div className="bg-white shadow-md rounded-lg p-4 text-center">
          <p className="text-gray-500">อัตราความแม่นยำของ AI (%)</p>
          <h2 className="text-xl font-bold text-green-700">{dashboardData.aiAccuracy}%</h2>
        </div>
      </div>
      
      {/* Chathistory Table */}
      <div className="bg-white rounded-lg p-4 shadow-md mb-6 overflow-y-auto max-h-96">
        <h3 className="text-lg font-bold mb-2">Chathistory</h3>
        <table className="table-auto w-full border border-gray-300">
          <thead>
            <tr className="border border-gray-300">
              <th className="p-2 border border-gray-300">Model</th>
              <th className="p-2 border border-gray-300">Prompt</th>
              <th className="p-2 border border-gray-300">Question</th>
              <th className="p-2 border border-gray-300">Answer</th>
              <th className="p-2 border border-gray-300">Time Usage</th>
              <th className="p-2 border border-gray-300">Ask At</th>
            </tr>
          </thead>
          <tbody>
            {dashboardData.chatHistory.map((chat, idx) => (
              <tr key={idx} className="border border-gray-300">
                <td className="p-2 border border-gray-300">{chat.model}</td>
                <td className="p-2 border border-gray-300">{chat.prompt}</td>
                <td className="p-2 border border-gray-300">{chat.question}</td>
                <td className="p-2 border border-gray-300">{chat.answer}</td>
                <td className="p-2 border border-gray-300">{chat.time_usage}</td>
                <td className="p-2 border border-gray-300">{chat.ask_at}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      
      {/* Documents Table */}
      <div className="bg-white rounded-lg p-4 shadow-md overflow-y-auto max-h-96">
        <h3 className="text-lg font-bold mb-2">Documents</h3>
        <table className="table-auto w-full border border-gray-300">
          <thead>
            <tr className="border border-gray-300">
              <th className="p-2 border border-gray-300">Document Name</th>
              <th className="p-2 border border-gray-300">Pages</th>
              <th className="p-2 border border-gray-300">Time Usage</th>
              <th className="p-2 border border-gray-300">Upload At</th>
              <th className="p-2 border border-gray-300">IDs</th>
              <th className="p-2 border border-gray-300">Embedding Model</th>
            </tr>
          </thead>
          <tbody>
            {dashboardData.documents.map((doc, idx) => (
              <tr key={idx} className="border border-gray-300">
                <td className="p-2 border border-gray-300">{doc.name}</td>
                <td className="p-2 border border-gray-300">{doc.pages}</td>
                <td className="p-2 border border-gray-300">{doc.time_usage}</td>
                <td className="p-2 border border-gray-300">{doc.upload_at}</td>
                <td className="p-2 border border-gray-300">{doc.ids}</td>
                <td className="p-2 border border-gray-300">{doc.embedding_model}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Dashboard;
