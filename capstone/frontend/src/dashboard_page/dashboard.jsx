import React, { useEffect, useState } from "react";
import Label from "./components/stats/Label";
import { Navbar, Footer } from "./components/main_pages";
import { Linechart, Piechart, Barchart, Radarchart } from "./components/charts";
import { Chatbot } from "./components/button";
import "./styles/global.css";

const Dashboard = () => {
  const [dashboardData, setDashboardData] = useState(null);

  useEffect(() => {
    fetch("http://localhost:8000/dashboard/data")
      .then((response) => response.json())
      .then((data) => setDashboardData(data))
      .catch((error) => console.error("Error fetching data: ", error));
  }, []);

  // สมมติว่า dashboardData มีข้อมูลดังนี้:
  // {
  //   totalChats: number,
  //   uniqueUsers: number,
  //   averageSessionDuration: number, // นาที
  //   botResponseSuccessRate: number, // %
  //   peakUsageTime: string,
  //   aiAccuracy: number, // %
  //   unansweredQueries: number,
  //   topQuestions: array of strings,
  //   responseTime: string,
  //   apiErrors: number,
  //   userSatisfactionScore: number, // %
  //   userFeedback: array of strings
  // }

  return (
    <div className="min-h-screen bg-gray-100">
      <Navbar />
      <div className="flex">
        <main className="flex-1 p-6">
          {/* Overview & Summary */}
          <section className="mb-8">
            <h2 className="text-2xl font-bold mb-4">ภาพรวมและสรุปผล</h2>
            <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
              <div className="bg-white shadow-md rounded-xl p-4 text-center">
                <p className="text-gray-500">จำนวนแชททั้งหมด</p>
                <h2 className="text-xl font-bold text-purple-700">
                  {dashboardData?.totalChats || 0}
                </h2>
              </div>
              <div className="bg-white shadow-md rounded-xl p-4 text-center">
                <p className="text-gray-500">ค่าเฉลี่ยเวลาการสนทนา (นาที)</p>
                <h2 className="text-xl font-bold text-purple-700">
                  {dashboardData?.averageSessionDuration || 0}
                </h2>
              </div>
              <div className="bg-white shadow-md rounded-xl p-4 text-center">
                <p className="text-gray-500">อัตราการตอบกลับสำเร็จของบอท (%)</p>
                <h2 className="text-xl font-bold text-purple-700">
                  {dashboardData?.botResponseSuccessRate || 0}%
                </h2>
              </div>
            </div>
          </section>

          {/* User Engagement */}
          <section className="mb-8">
            <h2 className="text-2xl font-bold mb-4">การมีส่วนร่วมของผู้ใช้</h2>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div className="bg-white shadow-md rounded-xl p-4 text-center">
                <p className="text-gray-500">เวลาที่มีผู้ใช้เยอะที่สุด</p>
                <h2 className="text-xl font-bold text-purple-700">
                  {dashboardData?.peakUsageTime || "N/A"}
                </h2>
              </div>
              
            </div>
          </section>

          {/* Chatbot Performance */}
          <section className="mb-8">
            <h2 className="text-2xl font-bold mb-4">ประสิทธิภาพของแชทบอท</h2>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
              <div className="bg-white shadow-md rounded-xl p-4 text-center">
                <p className="text-gray-500">อัตราความแม่นยำของ AI</p>
                <h2 className="text-xl font-bold text-green-600">
                  {dashboardData?.aiAccuracy || 0}%
                </h2>
              </div>
              <div className="bg-white shadow-md rounded-xl p-4 text-center">
                <p className="text-gray-500">
                  จำนวนข้อความที่ Chatbot ตอบไม่ได้
                </p>
                <h2 className="text-xl font-bold text-red-600">
                  {dashboardData?.unansweredQueries || 0}
                </h2>
              </div>
             
            </div>
          </section>

          {/* Technical Metrics */}
          <section className="mb-8">
            <h2 className="text-2xl font-bold mb-4">
              ตัวชี้วัดทางเทคนิค
            </h2>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div className="bg-white shadow-md rounded-xl p-4 text-center">
                <p className="text-gray-500">อัตราความล่าช้าในการตอบกลับ</p>
                <h2 className="text-xl font-bold text-orange-600">
                  {dashboardData?.responseTime || "N/A"}
                </h2>
              </div>
              <div className="bg-white shadow-md rounded-xl p-4 text-center">
                <p className="text-gray-500">
                  ข้อผิดพลาดของ API/ระบบเชื่อมต่อ
                </p>
                <h2 className="text-xl font-bold text-red-600">
                  {dashboardData?.apiErrors || 0}
                </h2>
              </div>
            </div>
          </section>

          {/* Sentiment Analysis */}
          <section className="mb-8">
            <h2 className="text-2xl font-bold mb-4">
              การวิเคราะห์อารมณ์ของผู้ใช้
            </h2>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
              <div className="bg-white shadow-md rounded-xl p-4 text-center">
                <p className="text-gray-500">อัตราความพึงพอใจของผู้ใช้</p>
                <h2 className="text-xl font-bold text-green-600">
                  {dashboardData?.userSatisfactionScore || 0}%
                </h2>
              </div>
              <div className="bg-white shadow-md rounded-xl p-4">
                <p className="text-gray-500">
                  คำติชมและฟีดแบ็กจากผู้ใช้
                </p>
                <ul className="list-disc list-inside mt-2">
                  {dashboardData?.userFeedback?.length > 0 ? (
                    dashboardData.userFeedback.map((feedback, idx) => (
                      <li key={idx}>{feedback}</li>
                    ))
                  ) : (
                    <li>N/A</li>
                  )}
                </ul>
              </div>
              <div className="bg-white shadow-md rounded-xl p-4">
                <p className="text-gray-500">คำถามที่พบบ่อย</p>
                <ul className="list-disc list-inside mt-2">
                  {dashboardData?.topQuestions?.length > 0 ? (
                    dashboardData.topQuestions.map((q, idx) => (
                      <li key={idx}>{q}</li>
                    ))
                  ) : (
                    <li>N/A</li>
                  )}
                </ul>
              </div>
            </div>
          </section>

          {/* Charts Summary */}
          <section className="mb-8">
            <h2 className="text-2xl font-bold mb-4">กราฟแสดงผล</h2>
            <div className="grid grid-cols-4 grid-rows-2 gap-3">
              <div className="bg-white rounded-2xl shadow-lg p-4 h-[450px]">
                <Barchart />
              </div>
              <div className="bg-white rounded-2xl shadow-lg p-4 h-[300px]">
                <Piechart />
              </div>

            </div>
          </section>
        </main>
      </div>
      <Chatbot />
      <Footer />
    </div>
  );
};

export default Dashboard;
