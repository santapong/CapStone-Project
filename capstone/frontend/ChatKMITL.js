// คำถาม-คำตอบตัวอย่าง (สามารถเพิ่ม/แก้ไขได้ตามต้องการ)
// หมายเหตุ: เพิ่ม key "หลักสูตร", "สถาบัน", "เกี่ยวกับ" เพื่อรองรับปุ่ม prompt
const qnaList = {
    "สวัสดี": "สวัสดีค่ะ มีอะไรให้ช่วยไหมคะ?",
    "สมัครเรียน": "ท่านสามารถสมัครเรียนได้ที่เมนู 'สมัครเรียน' หรือ <a href='#'>คลิกที่นี่</a> ค่ะ",
    "ทรานสคริปต์": "ท่านสามารถยื่นขอทรานสคริปต์แบบอิเล็กทรอนิกส์ได้ที่หน้าแรก หรือสอบถามเพิ่มเติมได้ที่สำนักทะเบียนค่ะ",
    "ค่าธรรมเนียม": "ข้อมูลค่าธรรมเนียมการศึกษาสามารถดูได้จากเมนู 'งานทะเบียน' หรือ <a href='#'>คลิกที่นี่</a> ค่ะ",
    // ส่วนของ Prompt 3 ข้อ
    "หลักสูตร": "ที่สถาบันของเรามีหลากหลายหลักสูตรทั้งปริญญาตรี โท เอก สามารถดูรายละเอียดได้ที่เมนู 'หลักสูตร' หรือ <a href='#'>คลิกที่นี่</a> ค่ะ",
    "สถาบัน": "สถาบันเทคโนโลยีพระจอมเกล้า ฯ เป็นสถาบันชั้นนำด้านวิศวกรรมและเทคโนโลยี สอบถามเพิ่มเติมได้ที่หน้า 'เกี่ยวกับเรา' หรือ <a href='#'>คลิกที่นี่</a> ค่ะ",
    "เกี่ยวกับ": "ข้อมูลเกี่ยวกับมหาวิทยาลัย วิสัยทัศน์ พันธกิจ สามารถอ่านเพิ่มเติมได้จากเมนู 'เกี่ยวกับ' ค่ะ",
  };
  
  // สลับแสดง/ซ่อนกล่อง Chatbot
  function toggleChat() {
    const chatModal = document.getElementById('chatModal');
    if (chatModal.style.display === 'none' || chatModal.style.display === '') {
      chatModal.style.display = 'flex'; // เปิด Modal
    } else {
      chatModal.style.display = 'none'; // ปิด Modal
    }
  }
  
  // ส่งข้อความเมื่อกดปุ่ม Enter ในช่องพิมพ์
  function handleKeyPress(event) {
    if (event.key === 'Enter') {
      sendMessage();
    }
  }
  
  // ฟังก์ชันสำหรับส่งข้อความ
  function sendMessage() {
    const userInput = document.getElementById('userInput');
    const text = userInput.value.trim();
    if (!text) return; // ถ้าว่างไม่ทำงาน
  
    // แสดงข้อความของผู้ใช้ในหน้าจอ
    addMessage(text, 'user-message');
  
    // ล้างช่องข้อความ
    userInput.value = '';
  
    // หาและแสดงข้อความตอบกลับจากบอท
    const botReply = getBotResponse(text);
    addMessage(botReply, 'bot-message');
  }
  
  // ฟังก์ชันสร้างข้อความในหน้าจอแชท
  function addMessage(msg, className) {
    const chatBody = document.getElementById('chatModal-body');
    const newMsg = document.createElement('div');
    newMsg.classList.add('message', className);
    newMsg.innerHTML = msg; // .innerHTML เพื่อรองรับลิงก์ได้ (ถ้าใช้)
    chatBody.appendChild(newMsg);
  
    // เลื่อน scroll ลงล่างสุด (กรณีข้อความเยอะ)
    chatBody.scrollTop = chatBody.scrollHeight;
  }
  
  // ฟังก์ชันค้นหาข้อความตอบกลับใน qnaList
  function getBotResponse(userText) {
    // แปลงข้อความเป็นตัวพิมพ์เล็ก
    const userTextLower = userText.toLowerCase();
  
    // ลองค้นหาคีย์เวิร์ดใน qnaList
    for (const key in qnaList) {
      // ตรวจสอบโดยตัดช่องว่าง และใช้ includes เพื่อค้นหาแบบง่าย
      if (userTextLower.includes(key.toLowerCase())) {
        return qnaList[key];
      }
    }
  
    // ถ้าไม่เจอ
    return "ขออภัย ฉันไม่เข้าใจคำถามของคุณ ลองพิมพ์อย่างอื่นดูนะคะ";
  }
  
  // เมื่อผู้ใช้คลิกปุ่ม Prompt
  function promptSelected(selectedText) {
    // แสดงข้อความที่ user เลือกในหน้าจอ (เสมือนเป็น user-message)
    addMessage(selectedText, 'user-message');
  
    // จากนั้นให้บอทตอบ
    const botReply = getBotResponse(selectedText);
    addMessage(botReply, 'bot-message');
  }
  