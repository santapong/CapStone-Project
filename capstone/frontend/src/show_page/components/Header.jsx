import "./styles/globals.css";

export default function Header() {
  return (
    <header className="Navbar">
      <div className="logo">
        <img src="https://via.placeholder.com/50" alt="Logo" />
        <h1>สำนักทะเบียนและบริการการศึกษา</h1>
      </div>
      <nav>
        <ul>
          <li><a href="#">หลักสูตร</a></li>
          <li><a href="#">สมัครเรียน</a></li>
          <li><a href="#">ตารางเรียน-สอบ</a></li>
          <li><a href="#">ปฏิทินการศึกษา</a></li>
          <li><a href="#">งานทะเบียน</a></li>
          <li><a href="#">บริการ</a></li>
          <li><a href="#">Data Visualization</a></li>
        </ul>
      </nav>
      <div className="login-lang">
        <a href="#">เข้าสู่ระบบ</a>
        <a href="#">ENG</a>
        <a href="#">ไทย</a>
      </div>
    </header>
  );
}
