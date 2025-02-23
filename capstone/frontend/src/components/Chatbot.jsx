import { useState, useRef, useEffect } from "react";
import { FaRobot } from "react-icons/fa";
import axios from "axios";

export default function Chatbot() {
  const [message, setMessage] = useState("");
  const [messages, setMessages] = useState(() => {
    const savedMessages = localStorage.getItem("chat_messages");
    const savedExpiry = localStorage.getItem("chat_messages_expiry");
    const currentTime = new Date().getTime();

    if (savedMessages && savedExpiry) {
      const parsedMessages = JSON.parse(savedMessages);
      const expiry = JSON.parse(savedExpiry);
      
      // Check if the messages are expired
      if (currentTime > expiry) {
        localStorage.removeItem("chat_messages");
        localStorage.removeItem("chat_messages_expiry");
        return [];
      }
      return parsedMessages || [];
    }
    return [];
  });
  const [loading, setLoading] = useState(false);
  const chatContainerRef = useRef(null);
  const MESSAGE_LIFETIME = 1000 * 60; // 30 secs per question

  useEffect(() => {
    if (messages.length > 0) {
      const savedExpiry = localStorage.getItem("chat_messages_expiry");
      if (!savedExpiry) {
        // Set the expiration time only if it's not already set in localStorage
        const expirationTime = new Date().getTime() + MESSAGE_LIFETIME;
        localStorage.setItem("chat_messages_expiry", JSON.stringify(expirationTime));
      }
    }
    
    if (chatContainerRef.current) {
      chatContainerRef.current.scrollTop = chatContainerRef.current.scrollHeight;
    }

    localStorage.setItem("chat_messages", JSON.stringify(messages));
  }, [messages]);

  const sendMessage = async () => {
    if (!message.trim()) return;
    const newMessages = [...messages, { text: message, type: "user" }];
    setMessages(newMessages);
    setMessage("");

    setLoading(true);
    try {
      const response = await axios.post("https://localhost:8000/chatbot/infer", {
        question: message,
      });
      const botReply = response.data.answer || "ขออภัย ฉันไม่เข้าใจคำถามของคุณ";
      setMessages((prev) => [...prev, { text: botReply, type: "bot" }]);
    } catch (error) {
      setMessages((prev) => [...prev, { text: "เกิดข้อผิดพลาดในการเชื่อมต่อ AI", type: "bot" }]);
    }
    setLoading(false);
  };

  return (
    <>
      <button
        className="fixed bottom-6 right-6 bg-blue-600 text-white p-3 rounded-full shadow-lg flex items-center justify-center"
        onClick={() => document.getElementById("chatbot-modal").showModal()}
      >
        <FaRobot className="text-2xl" />
      </button>

      <dialog id="chatbot-modal" className="modal">
        <div className="modal-box bg-gray-900 text-white w-[600px] max-w-2xl">
          <div className="flex justify-between items-center bg-gray-900 px-4 py-3 rounded-t-lg">
            <h4 className="text-lg font-semibold">ChatKMITL - Ask a question</h4>
            <form method="dialog">
              <button className="text-2xl text-gray-400 hover:text-white">x</button>
            </form>
          </div>

          <div ref={chatContainerRef} className="p-4 h-[300px] overflow-y-auto">
            {messages.map((msg, index) => (
              <div key={index} className={`mb-2 ${msg.type === "user" ? "text-right" : "text-left"}`}>
                <div className={`inline-block px-3 py-2 rounded-lg break-words max-w-[80%] text-left ${
                  msg.type === "user" ? "bg-blue-500 text-white" : "bg-gray-700"
                }`}
                style={{ whiteSpace: "pre-line" }}
                >
                  {msg.text}
                </div>
              </div>
            ))}
            {loading && (
              <div>
                <span className="loading loading-spinner loading-lg">AI กำลังพิมพ์ </span>
              </div>
            )}
          </div>

          <div className="flex px-4 py-3 border-t border-gray-700">
            <input
              type="text"
              placeholder="Ask anything"
              value={message}
              onChange={(e) => setMessage(e.target.value)}
              onKeyDown={(e) => e.key === "Enter" && sendMessage()}
              className="flex-1 bg-gray-800 text-white px-3 py-2 rounded-l-lg focus:outline-none"
            />
            <button
              onClick={sendMessage}
              className="bg-blue-500 text-white px-4 py-2 rounded-r-lg"
            >
              Ask AI
            </button>
          </div>

          <div className="text-center text-gray-500 text-sm py-2">
            © Copyright 2025, The Jolf Team.
          </div>
        </div>
      </dialog>
    </>
  );
}
