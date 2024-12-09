import React from "react";
import { BrowserRouter as Router, Routes, Route, Link,Navigate} from "react-router-dom";
import TopNav from "./components/TopNav";
import Home from "./pages/Home"
import Profile from "./pages/Profile"
import Blog from "./pages/Blog"
import ContactUs from "./pages/ContactUs"
import YesorNo from "./components/contact/YesorNo"
import Report from "./components/contact/Report"
import Write from "./components/Write";
// 각 페이지 컴포넌트
// 로그인 여부를 관리하는 상태 예제
const isAuthenticated = () => {
  return !!localStorage.getItem("authToken"); // 예: 토큰 저장 여부 확인
};

// PublicRoute: 로그인 없이 접근 가능
const PublicRoute = ({ children }) => {
  return children;
};

// PrivateRoute: 로그인 필요
const PrivateRoute = ({ children }) => {
  return isAuthenticated() ? children : <Navigate to="/contact/result?response=no/report" replace />;
};
function App() {
  return (
    <Router>
      <div style={styles.container}>
        {/* 네비게이션 바 */}
        <TopNav />

        {/* 라우트 설정 */}
        <div style={styles.pageContent}>
          <Routes>
            {/* 로그인 필요한 페이지 */}
            <Route
                    path="/report"
                    element={
                        <PrivateRoute>
                            <Report />
                        </PrivateRoute>
                    }
            />
            <Route path="/" element={<Home />} />
            <Route path="/profile" element={<Profile />} />
            <Route path="/blog" element={<Blog />} />
            <Route path="/blog/:id" element={<Write />} />
            <Route path="/blog/eee" element={<Write />} />
            <Route path="/contact" element={<ContactUs />} />
            <Route path="/contact/result/" element={<YesorNo />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}





// 스타일 수정
const styles = {
  
  container: {
    display: "flex",
    flexDirection: "column",
    backgroundColor: "#fffaea",
    overflowX: "hidden", // 가로 스크롤 방지
  },
  
  pageContent: {
    minHeight: "100vh",
    // padding: "0 40px",
    
    width: "100%", // 네비게이션 바와 동일한 폭
    boxSizing: "border-box",
  },
};



export default App