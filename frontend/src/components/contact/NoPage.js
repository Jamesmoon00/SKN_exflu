import React, { useState } from "react";
import axios from "axios";
import { GoogleOAuthProvider, GoogleLogin } from "@react-oauth/google";
import { useNavigate } from "react-router-dom"; // React Router 사용
import login from "../../assets/img/Login.png";
import google from "../../assets/icons/googleLogin.png";

const NoPage = () => {
    const navigate = useNavigate(); // 페이지 이동 함수
    const [isMobile, setIsMobile] = useState(window.innerWidth <= 768); // 모바일 여부 상태
    const [isHovered, setIsHovered] = useState(false); // hover 상태 관리

    const handleLoginSuccess = async (credentialResponse) => {
        // 백엔드 Google OAuth 시작점으로 리다이렉트
        window.location.href = "https://backdocsend.jamesmoon.click/auth/google";
    };

    return (
        
        <div style={styles.container}>
            <section style={styles.logoSection}>
                <img
                    src={login}
                    alt="eXflu logo"
                    style={{
                        ...styles.logoImage,
                        width: isMobile ? "70%" : "50%",
                    }}
                />
            </section>
            <section style={styles.loginSection}>
                <GoogleLogin
                    onSuccess={handleLoginSuccess} // 로그인 성공 처리
                    onError={() => alert("로그인 실패!")}
                />
            </section>
        </div>
       
    );
};

const styles = {
    container: {
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        width: "100%",
        height: "100vh",
        overflow: "hidden",
        background: "linear-gradient(to bottom, #fff8e1, #f3e5ab, #fff8e1)",
        backgroundColor: "#fffaea",
    },
    logoSection: {
        marginBottom: "50px",
        display: "flex",
        justifyContent: "center",
    },
    logoImage: {
        width: "50%",
        height: "auto",
        display: "flex",
    },
    loginSection: {
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
    },
};

export default NoPage;
