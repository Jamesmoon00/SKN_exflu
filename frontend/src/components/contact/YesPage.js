import React from "react";
import SideCard from "./ContactSidecard";
import question from "../../assets/img/question.png";
import Snowfall from "react-snowfall";

const YesPage = () => {
    const questions = [
        {
            question: "어떤 제품군 / 분야를 홍보하고 싶으신가요?",
            options: ["전자제품", "의류", "식품", "기타"],
        },
        {
            question: "예상 금액대를 선택해주세요.",
            options: ["10만원 이하", "10만원 ~ 50만원", "50만원 ~ 100만원", "100만원 이상"],
        },
        {
            question: "원하고자 하는 인플루언서의 메인 활동 플랫폼을 선택해주세요.",
            options: ["인스타그램", "유튜브", "틱톡", "블로그"],
        },
        {
            question: "원하고자 하는 홍보 이벤트를 선택해주세요.",
            options: ["리뷰", "이벤트 진행", "홍보 영상 제작", "기타"],
        },
        {
            question: "원하고자 하는 인플루언서의 성별을 입력해주세요.",
            options: ["남성", "여성", "무관"],
        },
    ];

    return (
        <div style={styles.container}>
            {/* Side Card UI */}
            <SideCard />

            {/* 질문 폼 */}
            <div style={styles.post}>
                <Snowfall
                    color="white" // 눈 색상
                    snowflakeCount={150} // 눈송이 개수
                    style={{ zIndex: 9999 }} // 눈이 모든 요소 위에 표시되도록 설정
                />
                <div style={styles.postHeader}>
                    <img src={question} alt="" style={styles.questionImage} />
                </div>
                <div style={styles.contentLine}></div>
                <form style={styles.form}>
                    {questions.map((item, index) => (
                        <div key={index} style={styles.question}>
                            <label style={styles.label}>{`Q${index + 1}. ${item.question}`}</label>
                            <select style={styles.select}>
                                {item.options.map((option, idx) => (
                                    <option key={idx} value={option}>
                                        {option}
                                    </option>
                                ))}
                            </select>
                        </div>
                    ))}
                </form>
                <div style={styles.buttoncontainer}>
                    <button type="submit" style={styles.submitButton}>
                        등록
                    </button>
                </div>
            </div>
        </div>
    );
};

const styles = {
    container: {
        display: "flex",
        marginLeft: "45px",
        marginRight: "40px",
        backgroundColor: "#fffaea",
        minHeight: "100vh",
        justifyContent: "space-between", // 좌우 요소 간 여백 균일화
    },
    post: {
        flex: "2.5",
        background: "linear-gradient(180deg, #FFEFB8 0%, #FFFDF7 25%)",
        marginTop: "30px",
        marginLeft: "40px",
     
        borderRadius: "10px",
        padding: "30px 30px 30px",
        boxShadow: "0 4px 8px rgba(0, 0, 0, 0.1)",
        marginBottom: "30px",
        overflow: "auto",
    },
    postHeader: {
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        marginBottom: "20px",
    },
    questionImage: {
        width: "40%",
        justifyContent: "center",
        
    },
    form: {
        display: "flex",
        flexDirection: "column",
        gap: "15px",
       
    },
    question: {
        display: "flex",
        flexDirection: "column",
        gap: "10px",
        marginBottom: "30px"
    },
    label: {
        fontSize: "1rem",
        color: "#6d4c41",
    },
    select: {
        width: "80%",
        padding: "10px",
        borderRadius: "10px",
        border: "1px solid #ddd",
        fontSize: "1rem",
        backgroundColor: "#fff",
        cursor: "pointer",
       
        marginLeft: "20px"
    },
    submitButton: {
        boxSizing: "border-box", // 수정: "box-sizing"의 오타 수정
        width: "80px",
        height: "40px",
        background: "#FBE5A2",
        border: "1px solid #F5E4AE",
        boxShadow: "0px 4px 4px rgba(0, 0, 0, 0.25)",
        borderRadius: "15px",
        cursor: "pointer", // 추가: 버튼 클릭 가능 커서

    },
    contentLine: {
        height: "2px",
        backgroundColor: "#F1D1A3",
        marginBottom: "40px"
    },
    buttoncontainer:{
        display: "flex",
        flexDirection: "column",
        alignItems: "center", // 모든 자식 요소를 가로 중앙 정렬
    }
};

export default YesPage;
