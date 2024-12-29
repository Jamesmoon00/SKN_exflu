import React, { useState, useEffect } from "react";
import logoImage from "../../assets/img/2nd_logo.png";
import Snowfall from "react-snowfall";

const FirstSection = () => {
    const [windowWidth, setWindowWidth] = useState(window.innerWidth); // 화면 너비 상태

    useEffect(() => {
        // 윈도우 크기 변경 이벤트 감지
        const handleResize = () => {
            setWindowWidth(window.innerWidth);
        };
        window.addEventListener("resize", handleResize);
        return () => {
            window.removeEventListener("resize", handleResize);
        };
    }, []);

    // 동적으로 글자 크기를 반환하는 함수
    const getFontSize = (baseSize) => {
        if (windowWidth < 768) return baseSize * 0.8; // 768px 이하일 때 20% 축소
        if (windowWidth < 480) return baseSize * 0.6; // 480px 이하일 때 40% 축소
        return baseSize;
    };

    return (
        <div style={styles.container}>
            {/* 눈 내리는 효과 */}
            <Snowfall
                color="white" // 눈 색상
                snowflakeCount={150} // 눈송이 개수
                style={{ zIndex: 9999 }} // 눈이 모든 요소 위에 표시되도록 설정
            />

            {/* 로고 섹션 */}
            <section style={styles.logoSection}>
                <img src={logoImage} alt="eXflu" style={styles.logoImage} />
            </section>

            {/* 설명 섹션 */}
            <section style={styles.descriptionSection}>
                <h2
                    style={{
                        ...styles.animatedText,
                        fontSize: `${getFontSize(2.5)}rem`, // 동적으로 글자 크기 설정
                    }}
                >
                    AI influencer
                </h2>
                <p
                    style={{
                        ...styles.description,
                        fontSize: `${getFontSize(1)}rem`, // 동적으로 글자 크기 설정
                    }}
                >
                    AI 인플루언서 마케팅 대행 웹 서비스
                </p>
            </section>
        </div>
    );
};

const styles = {
    container: {
        position: "relative",
        width: "100%",
        height: "100vh",
        overflowX: "hidden", // 가로 스크롤 방지
        backgroundColor: "#fffaea",
        background: "linear-gradient(to bottom, #FFFAEA, #FFEFB9)",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center", // 수직 및 수평 중앙 정렬
    },
    logoSection: {
        marginBottom: "20px",
        display: "flex",
        justifyContent: "center",
    },
    logoImage: {
        width: "50%",
        height: "auto",
        display: "block",
    },
    descriptionSection: {
        textAlign: "center",
    },
    animatedText: {
        fontWeight: "bold",
        margin: "5px 0",
        animation: "colorChange 3s infinite", // 애니메이션 적용
    },
    description: {
        color: "#555",
        margin: 0,
    },
};
const globalStyle = `
@keyframes colorChange {
    0% { color: #CD9167; }
    25% { color: #CD9167; } 
    50% { color: #CD9167; }
    75% { color: #A57451; }
    100% { color: #856044; }
}`;

const addGlobalStyle = () => {
    const style = document.createElement("style");
    style.textContent = globalStyle;
    document.head.appendChild(style);
};

addGlobalStyle();
export default FirstSection;
