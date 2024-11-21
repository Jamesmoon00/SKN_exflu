import React, { useEffect, useState } from "react";
import logoImage from "../../assets/img/2nd_logo.png"

import Snowfall from "react-snowfall";
// 각 페이지 컴포넌트
// const Home = () => <div>Home Page</div>;
const FirstSection = () => {
    const [opacity, setOpacity] = useState(0); // 초기 투명도

    useEffect(() => {
        // 페이지 로드 시 점진적으로 투명도를 높이는 애니메이션
        const interval = setInterval(() => {
            setOpacity((prevOpacity) => {
                if (prevOpacity >= 1) {
                    clearInterval(interval); // 애니메이션 완료 후 중지
                    return 1;
                }
                return prevOpacity + 0.05; // 투명도 증가
            });
        }, 50); // 50ms마다 실행
        return () => clearInterval(interval); // 클린업 함수
    }, []);
    return (
        <>
            <div style={styles.container}>
                {/* 눈 내리는 효과 */}
                <Snowfall
                    color="white" // 눈 색상
                    snowflakeCount={150} // 눈송이 개수
                    style={{ zIndex: 9999 }} // 눈이 모든 요소 위에 표시되도록 설정
                />

                {/* 로고 섹션 */}
                <section style={styles.logoSection}>
                    <img src={logoImage} alt="eXflu" style={{ ...styles.logoImage, opacity }} />
                </section>

                {/* 설명 섹션 */}
                <section style={styles.descriptionSection}>
                    <h2 style={styles.animatedText}>AI influencer</h2>
                    <p style={styles.description}>
                    This is a description. this is a description
                    </p>
                </section>
            </div>
        </>
        
    );
}

const styles = {
    container: {
        position: "relative",
        width: "100%",
        height: "100vh",
        overflow: "hidden", // 눈송이가 컨테이너 밖으로 나가지 않도록 설정
        backgroundColor: "#fffaea",
        background: "linear-gradient(to bottom, #FFFAEA, #FFEFB9)",
    },
    logoSection: {
        marginTop: "80px",
        display: "flex"
    },
    logoImage: {
        width: "700px",
        height: "auto",
        display: "block",
        margin: "0 auto",
        alignItems: "center",
        transition: "opacity 3s ease-in-out",
       
    },
    bannerSection: {
        marginTop: "100px",
        position: "absolute",
        width:"100%",
    
    },
    bannerImage: {
        width: "100%",
        height: "auto",
        objectFit: "cover",
        height: "auto",
        bottom: "0px",
        opacity: 0.8, 
    },
    descriptionSection: {
        marginTop: "70px",
        textAlign: "center",
    },
    animatedText: {
        fontSize: "2.5rem",
        fontWeight: "bold",
        margin: "5px 0",
        animation: "colorChange 3s infinite", // 애니메이션 적용
    },
    description: {
        fontSize: "1rem",
        color: "#555",
        margin: 0,
    },
};

// 애니메이션 스타일 추가
// #DE9D9B : 죽은 연한 팥색
// #D09593 : 연보라
// #BF8D8B : 하늘
// #B88887 : 민트
// #9B706E
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
export default FirstSection