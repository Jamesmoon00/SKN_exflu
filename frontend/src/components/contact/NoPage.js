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
        try {
            console.log("Google Token:", credentialResponse.credential); // Google OAuth Token 확인

            // 백엔드로 토큰 전송
            const response = await axios.post(`${process.env.REACT_APP_SERVER_URL}auth/google/`, 
                {token: credentialResponse.credential},
                {withCredentials: true 
            });

            console.log("Logged in user:", response.data);

            // 토큰 저장 (예: localStorage)
            localStorage.setItem("authToken", response.data.token);

            // 결과 보고서 페이지로 이동
            navigate("/contact");
        } catch (error) {
            console.error("Error during login:", error);
            alert("로그인 실패!");
        }
    };

    return (
        <GoogleOAuthProvider clientId={process.env.REACT_APP_GOOGLE_CLIENT_ID}>
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
        </GoogleOAuthProvider>
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
