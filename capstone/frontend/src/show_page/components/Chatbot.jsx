import { useState } from "react";
import axios from "axios"; // เรียกใช้ Axios
import "./styles/Chatbot.css";

export default function Chatbot() {
  const [open, setOpen] = useState(false);
  const [messages, setMessages] = useState([
    { text: "สวัสดีค่ะ มีอะไรให้ช่วยไหมคะ?", type: "bot" },
    {
      text: "โปรดเลือกสิ่งที่ต้องการทราบ:",
      type: "bot",
      options: ["หลักสูตร", "สถาบัน", "เกี่ยวกับ"],
    },
  ]);
  const [loading, setLoading] = useState(false);

  const sendMessage = async (text) => {
    if (!text.trim()) return; // ป้องกันการส่งข้อความว่าง

    // เพิ่มข้อความของผู้ใช้ไปยังกล่องแชท
    setMessages([...messages, { text, type: "user" }]);

    // แสดงสถานะกำลังโหลด
    setLoading(true);

    try {
      const response = await axios.post("https://localhost:8000/chatbot/infer", {
        question: text,
      });

      const botReply = response.data.answer || "ขออภัย ฉันไม่เข้าใจคำถามของคุณ";
      setMessages((prev) => [...prev, { text: botReply, type: "bot" }]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        { text: "เกิดข้อผิดพลาดในการเชื่อมต่อ API", type: "bot" },
      ]);
    }

    setLoading(false);
  };

  return (
    <>
      <div className="chatbot-btn" onClick={() => setOpen(!open)}>
        <img src="https://via.placeholder.com/60x60?text=Chat" alt="Chatbot Button" />
      </div>

      {open && (
        <div id="chatModal">
          <div id="chatModal-header">
            <h4>Chatbot</h4>
            <button className="close-btn" onClick={() => setOpen(false)}>×</button>
          </div>
          <div id="chatModal-body">
            {messages.map((msg, index) => (
              <div key={index} className={`message ${msg.type}-message`}>
                {msg.text}
                {msg.options && (
                  <div className="prompt-buttons">
                    {msg.options.map((option, i) => (
                      <button key={i} onClick={() => sendMessage(option)}>
                        {option}
                      </button>
                    ))}
                  </div>
                )}
              </div>
            ))}
            {loading && <div className="bot-message">กำลังพิมพ์...</div>}
          </div>
          <div id="chatModal-footer">
            <input
              type="text"
              placeholder="พิมพ์ข้อความที่นี่..."
              onKeyDown={(e) => e.key === "Enter" && sendMessage(e.target.value)}
            />
            <button onClick={() => sendMessage(document.querySelector("#chatModal-footer input").value)}>ส่ง</button>
          </div>
        </div>
      )}
    </>
  );
}
