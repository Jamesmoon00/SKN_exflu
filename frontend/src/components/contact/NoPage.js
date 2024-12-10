import React, { useState } from "react";
import login from "../../assets/img/Login.png";
import google from "../../assets/icons/googleLogin.png";
 
const NoPage = () => {
    const [isMobile, setIsMobile] = useState(window.innerWidth <= 768); // 모바일 여부 상태
    const [isHovered, setIsHovered] = useState(false); // hover 상태 관리
    const handleGoogleLogin = () => {
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
                <img
                    src={google}
                    alt=""
                    style={{
                        ...styles.loginImage,
                        width: isMobile ? "50%" : "30%",
                        opacity: isHovered ? 0.4 : 1, // hover 상태에 따라 투명도 변경
                        transition: "opacity 0.3s ease-in-out", // 부드러운 효과
                    }}
                    onMouseEnter={() => {
                        console.log("Hovered"); // 확인용
                        setIsHovered(true); // hover 상태 변경
                    }}
                    onMouseLeave={() => {
                        console.log("Not Hovered"); // 확인용
                        setIsHovered(false); // hover 상태 해제
                    }}
                    onClick={handleGoogleLogin}
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
    loginImage: {
        cursor: "pointer", // 마우스 커서 변경
        transition: "opacity 0.3s ease-in-out", // 부드러운 효과
    },
};

export default NoPage;
