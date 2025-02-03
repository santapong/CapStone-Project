import "../components/styles/Banner.css";

export default function Banner() {
  return (
    <section className="banner">
      <div className="banner-content">
        <img src="https://via.placeholder.com/800x300" alt="Student Group" />
        <h2>เปิดให้บริการแล้ววันนี้!!</h2>
        <p>ยื่นขอเอกสารทรานสคริปต์ในรูปแบบอิเล็กทรอนิกส์ <br /> สะดวก รวดเร็ว ปลอดภัย คลิกเลย!</p>
        <a href="#" className="btn-primary">คลิกที่นี่เพื่อเข้าสู่เว็บไซต์</a>
      </div>
    </section>
  );
}
