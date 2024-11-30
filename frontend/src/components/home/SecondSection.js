import React, { useState } from "react";
import Eddy from "../../assets/img/eddy.png";
import Snowfall from "react-snowfall";

const SecondSection = () => {
    const [hoveredCard, setHoveredCard] = useState(null);

    return (
        <div style={styles.container}>
            {/* 눈 내리는 효과 */}
            <Snowfall
                color="white"
                snowflakeCount={150}
                style={{ zIndex: 9999 }}
            />

            {/* 캐릭터 이미지 */}
            <img src={Eddy} alt="Character" style={styles.image} />

            {/* 카드 레이아웃 */}
            <div style={styles.cardsContainer}>
                {["profile", "blog", "contact"].map((title, index) => (
                    <div
                        key={index}
                        style={
                            hoveredCard === index
                                ? { ...styles.card, ...styles.cardHover }
                                : styles.card
                        }
                        onMouseEnter={() => setHoveredCard(index)}
                        onMouseLeave={() => setHoveredCard(null)}
                    >
                        <div style={styles.cardContent}>
                            <h3 style={styles.cardTitle}>{title}</h3>
                            <p style={styles.cardDescription}>
                                이 공간은 설명 부분입니다.
                            </p>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};

const styles = {
    container: {
        display: "flex",
        justifyContent: "flex-start",
        alignItems: "flex-end",
        width: "100%",
        height: "100vh",
        background: "linear-gradient(to bottom, #FFEFB9, #FFFAEA)",
        padding: "20px",
    },
    image: {
        display: "flex",
        width: "400px",
        height: "auto",
        marginLeft: "20px",
        marginBottom: "10px",
        filter: "drop-shadow(0px 5px 10px rgba(255, 239, 184, 0.9))",
    },
    cardsContainer: {
        marginBottom: "250px",
        display: "flex",
        justifyContent: "space-evenly",
        alignItems: "center",
        width: "80%",
    },
    card: {
        width: "300px",
        height: "400px",
        backgroundColor: "#FFFEF9",
        borderRadius: "15px",
        filter: `drop-shadow(0px 6px 20px rgba(249, 217, 120, 0.6)) 
        drop-shadow(0px 4px 10px rgba(255, 247, 222, 0.8))`, // 그림자에 linear gradient 느낌 구현
        backdropFilter: "blur(3px)", // layer blur
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        textAlign: "center",
        transition: "transform 0.3s ease-in-out",
        position: "relative", // 카드 내부 요소의 상대 위치 기준
        overflow: "hidden", // 스케일링 시 요소가 넘치지 않도록 처리
    },
    cardHover: {
        transform: "scale(1.05)", // 카드 전체 크기 확대
    },
    cardContent: {
        position: "absolute", // 카드 내부 컨텐츠를 고정
        top: "10px", // 카드 내부에서 위쪽으로 고정
        left: "0",
        right: "0",
        bottom: "10px",
        display: "flex",
        flexDirection: "column",
        justifyContent: "center", // 제목과 설명을 중앙 정렬
        alignItems: "center",
    },
    cardTitle: {
        fontSize: "1.5rem",
        fontWeight: "bold",
        marginBottom: "10px",
        marginTop: "-200px"
    },
    cardDescription: {
        fontSize: "1rem",
        color: "#555",
    },
};

export default SecondSection;