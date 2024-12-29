import React, { useState, useEffect } from "react";
import "@fontsource/lexend-deca"; // npm에서 제공하는 경우
import Eddyfilm from "../../assets/img/eddy_list.png";
import encore from "../../assets/img/encore.png";
import sknetwork from "../../assets/img/sknetwork.png";

const ThirdSection = () => {
    const [showFirstImage, setShowFirstImage] = useState(false);
    const [showSecondImage, setShowSecondImage] = useState(false);

    useEffect(() => {
        // 첫 번째 이미지 나타남
        const firstImageTimeout = setTimeout(() => {
            setShowFirstImage(true);
        }, 500); // 0.5초 후 나타남

        // 두 번째 이미지 나타남
        const secondImageTimeout = setTimeout(() => {
            setShowSecondImage(true);
        }, 1500); // 1.5초 후 나타남

        // 클린업 타이머
        return () => {
            clearTimeout(firstImageTimeout);
            clearTimeout(secondImageTimeout);
        };
    }, []);

    return (
        <>
            <div style={styles.container}>
                <div style={styles.title}>
                    customers
                </div>
                <div style={styles.description}>
                    데이터, AI 분야의 국내 우수기업이 저희 서비스를 이용하고 있습니다.
                </div>
                <div style={styles.companyContainer}>
                    <img
                        src={encore}
                        alt="Company Logo 1"
                        style={{
                            ...styles.companyimage,
                            opacity: showFirstImage ? 0.8 : 0, // 서서히 나타나게 설정
                            transform: showFirstImage ? "translateY(0)" : "translateY(20px)",
                            transition: "opacity 1s ease, transform 1s ease",
                        }}
                    />
                    <img
                        src={sknetwork}
                        alt="Company Logo 2"
                        style={{
                            ...styles.companyimage2,
                            opacity: showSecondImage ? 0.8 : 0, // 서서히 나타나게 설정
                            transform: showSecondImage ? "translateY(0)" : "translateY(20px)",
                            transition: "opacity 1s ease, transform 1s ease",
                        }}
                    />
                </div>
                <img src={Eddyfilm} alt="Character Scene" style={styles.image} />
            </div>
        </>
    );
};

const styles = {
    container: {
        display: "flex",
        flexDirection: "column", // 세로 배치 설정
        justifyContent: "space-between", // 위쪽과 아래쪽에 배치
        alignItems: "center", // 가로 가운데 정렬
        height: "100vh",
        background: "linear-gradient(to bottom, #fff8e1, #f3e5ab, #fff8e1)",
    },
    title: {
        marginTop: "60px",
        fontWeight: "600",
        fontSize: "70px",
        fontFamily: "'Lexend Deca', sans-serif",
        background: "linear-gradient(90deg, #3F201F 0%, #724A38 33.9%, #8C5F45 63.4%,  #8C5F45 100%)",
        WebkitBackgroundClip: "text",
        WebkitTextFillColor: "transparent",
    },
    companyContainer: {
        display: "flex", // 가로 배치 설정
        justifyContent: "center", // 양쪽 끝에 배치
        alignItems: "center", // 세로 가운데 정렬
        width: "80%", // 부모 요소의 너비 설정
    },
    companyimage: {
        width: "30%", // 첫 번째 이미지 크기
        marginBottom: "-100px",
        opacity: 0, // 초기값 0
    },
    companyimage2: {
        width: "40%", // 두 번째 이미지 크기
        opacity: 0, // 초기값 0
    },
    image: {
        width: "100%", // 이미지 너비를 부모 요소에 맞춤
        height: "auto", // 이미지 높이를 부모 요소에 맞춤
        objectFit: "cover", // 이미지가 잘리지 않고 꽉 차도록 설정
    },
    description: {
        color: "#555",
        marginTop: "-149px",
    },
};

export default ThirdSection;
