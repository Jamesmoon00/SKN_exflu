import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom"; // React Router 훅
import contact from "../assets/img/contactus.png";
import Snowfall from "react-snowfall";

const ContactUs = () => {
    const [hoveredYes, setHoveredYes] = useState(false); // Yes 버튼 호버 상태
    const [hoveredNo, setHoveredNo] = useState(false); // No 버튼 호버 상태
    const navigate = useNavigate(); // 페이지 이동 훅
    const [isMobile, setIsMobile] = useState(window.innerWidth <= 768); // 모바일 여부 상태

    const handleYesClick = () => {
        navigate("/contact/result?response=yes"); // Yes 버튼 클릭 시 쿼리 문자열 추가
    };

    const handleNoClick = () => {
        navigate("/contact/result?response=no"); // No 버튼 클릭 시 쿼리 문자열 추가
    };
    useEffect(() => {
        const handleResize = () => {
         
            setIsMobile(window.innerWidth <= 768); // 화면 크기 변경에 따라 모바일 여부 업데이트
        };

        handleResize();
        window.addEventListener("resize", handleResize);
        return () => window.removeEventListener("resize", handleResize);
    }, []);
    return (
        <div style={styles.container}>
            <Snowfall
                    color="white" // 눈 색상
                    snowflakeCount={150} // 눈송이 개수
                    style={{ zIndex: 9999 }} // 눈이 모든 요소 위에 표시되도록 설정
            />
            <section style={styles.logoSection}>
                <img src={contact} alt="eXflu logo" style={{...styles.logoImage,
                    width: isMobile ? "70%" : "50%"
                }} />
            </section>
            <div style={styles.buttonContainer}>
                <button
                    style={{
                        ...styles.yesButton,
                        backgroundColor: hoveredYes ? "#e6ccb0" : "#f4e1c4", // 호버 시 색상 변경
                        width : isMobile ? "80px" : "100px",
                        height : isMobile ? "40px" : "50px"
                    }}
                    onMouseEnter={() => setHoveredYes(true)} // 호버 상태 활성화
                    onMouseLeave={() => setHoveredYes(false)} // 호버 상태 비활성화
                    onClick={handleYesClick}
                >
                    견적 받기
                </button>
                <button
                    style={{
                        ...styles.noButton,
                        backgroundColor: hoveredNo ? "#f4e1c4" : "#e6ccb0", // 호버 시 색상 변경
                        width : isMobile ? "80px" : "100px",
                        height : isMobile ? "40px" : "50px"
                    
                    }}
                    onMouseEnter={() => setHoveredNo(true)} // 호버 상태 활성화
                    onMouseLeave={() => setHoveredNo(false)} // 호버 상태 비활성화
                    onClick={handleNoClick}
                >
                    결과 보기
                </button>
            </div>
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
        marginBottom: "20px",
        display: "flex",
        justifyContent: "center",
    },
    logoImage: {

        width: "50%",
        height: "auto",
        display: "flex",
    },
    buttonContainer: {
        display: "flex",
        gap: "20px",
        justifyContent: "center",
        alignItems: "center",
        marginTop: "20px",
    },
    yesButton: {
        boxSizing: "border-box", // 수정: "box-sizing"의 오타 수정
        width: "100px",
        height: "50px",
        background: "#FFE8E7",
        border: "0px solid #FFF2F1",
       
        borderRadius: "20px",
        cursor: "pointer", // 추가: 버튼 클릭 가능 커서
        background: "linear-gradient(180deg, rgba(152, 111, 46, 0.5) 0%, rgba(212, 165, 98, 0.5) 100%)",
        color: "#6d4c41",
        boxShadow: "0px 4px 4px rgba(0, 0, 0, 0.25)",
    },
    noButton: {
        boxSizing: "border-box", // 수정: "box-sizing"의 오타 수정
        width: "100px",
        height: "50px",
        background: "#FFE8E7",
        border: "0px solid #FFF2F1",
       
        borderRadius: "20px",
        cursor: "pointer", // 추가: 버튼 클릭 가능 커서
        background: "linear-gradient(180deg, rgba(152, 111, 46, 0.5) 0%, rgba(212, 165, 98, 0.5) 100%)",
        color: "#6d4c41",
        boxShadow: "0px 4px 4px rgba(0, 0, 0, 0.25)",
    },
};

export default ContactUs;
