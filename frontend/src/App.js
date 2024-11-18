import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Home from "./pages/Home"
import Profile from "./pages/Profile"
import Blog from "./pages/Blog"
import ContactUs from "./pages/ContactUs"
// 각 페이지 컴포넌트

function App() {
  return (
    <Router>
      <div style={styles.container}>
        {/* 네비게이션 바 */}
        <div style={styles.navbar}>
          <div style={styles.navbarContent}>
            <Link to="/" style={styles.logo}>eXflu;</Link>
            <div style={styles.navLinks}>
              <Link to="/profile" style={styles.link}>profile</Link>
              <Link to="/blog" style={styles.link}>blog</Link>
              <Link to="/contact-us" style={styles.link}>contact us</Link>
            </div>
            <a
              href="https://www.instagram.com"
              target="_blank"
              rel="noopener noreferrer"
              style={styles.icon}
            >
              <img
                src="https://img.icons8.com/ios-glyphs/30/000000/instagram-new.png"
                alt="Instagram"
              />
            </a>
          </div>
          {/* 가로선 */}
          <div style={styles.navbarLine}></div>
        </div>

        {/* 라우트 설정 */}
        <div style={styles.pageContent}>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/profile" element={<Profile />} />
            <Route path="/blog" element={<Blog />} />
            <Route path="/contact-us" element={<ContactUs />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}





// 스타일 수정
const styles = {
  container: {
    backgroundColor: "#fffaea",
    height: "100vh",
    display: "flex",
    flexDirection: "column",
  },
  navbar: {
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    backgroundColor: "#fffaea",
    padding: "10px 0",
    width: "100%",
  },
  navbarContent: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    width: "95%", // 폭을 조금 더 넓게
    maxWidth: "1600px", // 최대 폭 증가
    padding: "0 8px", // 양쪽 여백 추가
    boxSizing: "border-box", // 패딩 포함 계산
    paddingBottom: 5
  },
  navbarLine: {
    width: "95%", // 가로선 폭을 navbarContent와 동일하게 설정
    maxWidth: "1600px", // 최대 폭 증가
    height: "2px",
    backgroundColor: "#f5e4ae",
  },
  logo: {
    fontSize: "2.5rem",
    fontWeight: "bold",
    textDecoration: "none",
    color: "#000",
  },
  navLinks: {
    display: "flex",
    gap: "90px", // 링크 간 간격 증가
  },
  link: {
    textDecoration: "none",
    color: "#000",
    padding: 10,
    fontSize: "1.5rem",
  },
  icon: {
    display: "flex",
    alignItems: "center",
  },
  pageContent: {
    flex: 1,
    padding: "0 60px",
    width: "95%", // 네비게이션 바와 동일한 폭
    boxSizing: "border-box",
  },
};



export default App