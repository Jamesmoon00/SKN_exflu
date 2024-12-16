import React, { useState, useEffect} from "react";
import SideCard from "./ContactSidecard";
import question from "../../assets/img/question.png";
import Snowfall from "react-snowfall";
import { useNavigate } from 'react-router-dom';
import "@fontsource/lexend-deca"; // npm에서 제공하는 경우
import axios from "axios";
import Loading from "./components/Loading";
const YesPage = () => {
    const navigate = useNavigate(); // useNavigate 훅 사용
    
    const [showSideCard, setShowSideCard] = useState(true);
    const [isMobile, setIsMobile] = useState(window.innerWidth <= 768);
    const [isLoading, setIsLoading] = useState(false);
    const [formData, setFormData] = useState({
        biz_name: "",
        biz_mail: "",
        biz_address: "",
        biz_phone: "",
        biz_manager: "",
        category_id: 999,
        products_categories: "",
        price: "",
        main_platform: "",
        event_type: "",
        charactor_type: "",
    });
    console.log(question[0].question);
    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setFormData({
            ...formData,
            [name]: value ,
        });
    };

    // 드롭다운 필드 업데이트
    const handleSelectChange = (field, value) => {
        setFormData((prevData) => ({
            ...prevData,
            [field]: value,
        }));
    };


    // 데이터 제출 핸들러
    const handleSubmit = async () => {
        console.log("전송할 데이터:", JSON.stringify(formData, null, 2)); // 디버그용
        setIsLoading(true);
        try {
            const response = await axios.post(
                `${process.env.REACT_APP_SERVER_URL}bizinfo/insert`,
                formData,
                {
                    headers: {
                        "Content-Type": "application/json", // JSON 요청임을 명시
                    },
                }
            );
            
            console.log("Response:", response.data);
            navigate("/solution", {state: response.data}); // '/solution'은 Solution.js가 연결된 라우트 경로
            
        } catch (error) {
            console.error("데이터 전송 중 오류:", error);
    
            // 서버 응답 내용 확인
            if (error.response) {
                console.error("서버 응답 데이터:", error.response.data);
                console.error("상태 코드:", error.response.status);
                console.error("헤더:", error.response.headers);
            }
            alert("데이터 전송 실패: " + (error.response?.data?.message || "알 수 없는 오류"));
        } finally {
            setIsLoading(false);
        }
    };
    
    useEffect(() => {
        const handleResize = () => {
            setShowSideCard(window.innerWidth > 1000); // 768px 이하일 때 SideCard 숨김
            setIsMobile(window.innerWidth <= 768); 
        };

        handleResize(); // 초기 크기 설정
        window.addEventListener("resize", handleResize); // 리사이즈 이벤트 추가
        return () => window.removeEventListener("resize", handleResize); // 이벤트 제거
    }, []);
    console.log("1",typeof formData.biz_name);
    console.log("2",typeof formData.biz_mail);
    console.log("3",typeof formData.biz_address);
    console.log("4",typeof formData.biz_phone);
    console.log("5",typeof formData.biz_manager);
    console.log("6",typeof formData.category_id);
    console.log("7",typeof formData.price);
    console.log("8",typeof formData.main_platform);
    console.log("9",typeof formData.event_type);
    console.log("10",typeof formData.charactor_type);
    
    
    
    if (isLoading) {
        // 로딩 화면 표시
        return (
            <Loading />
        );
    }
    
    return (
        <div
            style={{
                ...styles.container,
                marginLeft: showSideCard ? "45px" : "0", // SideNav가 없으면 marginLeft를 0으로 설정
            }}
        >
            {/* Side Card UI */}
            {showSideCard && <SideCard />}

            {/* 질문 폼 */}
            <div
                style={{
                    ...styles.post,
                    flex: showSideCard ? "2.5" : "3.5", // SideCard가 없을 때 너비 확장
                    marginLeft : isMobile ? "25px" : "40px",
                    marginRight : isMobile ? "-20px" : "0px",
                    marginTop : isMobile ? "20px" : "30px",
                    padding : isMobile ? "20px 10px 10px" : "30px 30px 30px",
                    marginBottom : isMobile ? "15px" : "30px"
                }}
            >
                <Snowfall
                    color="white" // 눈 색상
                    snowflakeCount={150} // 눈송이 개수
                    style={{ zIndex: 9999 }} // 눈이 모든 요소 위에 표시되도록 설정
                />
                
                <div style={styles.section}>Section 1. Bussiness Info</div>
                <div style={styles.sectionLine}></div>
                <form style={styles.form}>
                    <div style={styles.question}>
                        <label style={styles.label}>Q1. 기업명을 입력해주세요.</label>
                        <input
                            type="text"
                            name="biz_name"
                            value={formData.biz_name}
                            onChange={handleInputChange}
                            style={styles.input}
                            required
                        />
                    </div>
                    <div style={styles.question}>
                        <label style={styles.label}>Q2. 기업 메일 주소를 입력해주세요.</label>
                        <input
                            type="email"
                            name="biz_mail"
                            value={formData.biz_mail}
                            onChange={handleInputChange}
                            style={styles.input}
                            required
                        />
                    </div>
                    <div style={styles.question}>
                        <label style={styles.label}>Q3. 기업 주소를 입력해주세요.</label>
                        <input
                            type="address"
                            name="biz_address"
                            value={formData.biz_address}
                            onChange={handleInputChange}
                            style={styles.input}
                            required
                        />
                    </div>
                    <div style={styles.question}>
                        <label style={styles.label}>Q4. 담당자 연락처를 입력해주세요.</label>
                        <input
                            type="tel"
                            name="biz_phone"
                            value={formData.biz_phone}
                            onChange={handleInputChange}
                            style={styles.input}
                            required
                        />
                    </div>
                    <div style={styles.question}>
                        <label style={styles.label}>Q5. 담당자명을 입력해주세요.</label>
                        <input
                            type="text"
                            name="biz_manager"
                            value={formData.biz_manager}
                            onChange={handleInputChange}
                            style={styles.input}
                            required
                        />
                    </div>
                </form>
                <div style={{...styles.section, background: "linear-gradient(90deg, #A57451 0%, #CDAC7F 33.9%, #E1C897 63.4%, #F5E4AE 100%)"}}>Section 2. Marketing style</div>
                <div style={{...styles.sectionLine, background: "linear-gradient(90deg, #A57451 0%, #CDAC7F 33.9%, #E1C897 63.4%, #F5E4AE 100%)"}}></div>
                    {/* {questions.map((item, index) => (
                        <div key={index} style={styles.question}>
                            <label style={styles.label}>{`Q${index + 1}. ${item.question}`}</label>
                            <select 
                                style={styles.select}
                                value={formData[`Q${index + 1}`]} // formData에서 해당 질문의 값 가져오기
                                onChange={(e) => handleSelectChange(item.field, e.target.value)} // 선택값 변경
                            >
                                {item.options.map((option, idx) => (
                                    <option key={idx} value={option}>
                                        {option}
                                    </option>
                                ))}
                            </select>
                        </div>
                    ))} */}
                    <div style={styles.question}>
                    <label style={styles.label}>Q1. 어떤 제품군 / 분야를 홍보하고 싶으신가요?</label>
                    <select
                        style={styles.select}
                        value={formData.products_categories}
                        onChange={(e) => handleSelectChange("products_categories", e.target.value)}
                    >
                        <option value="선택">선택</option>
                        <option value="전자제품">전자제품</option>
                        <option value="의류">의류</option>
                        <option value="식품">식품</option>
                        <option value="기타">기타</option>
                    </select>
                </div>
                <div style={styles.question}>
                    <label style={styles.label}>Q2. 예상 금액대를 선택해주세요.</label>
                    <select
                        style={styles.select}
                        value={formData.price}
                        onChange={(e) => handleSelectChange("price", e.target.value)}
                    >
                        <option value="선택">선택</option>
                        <option value="10만원 이하">10만원 이하</option>
                        <option value="10만원 ~ 50만원">10만원 ~ 50만원</option>
                        <option value="50만원 ~ 100만원">50만원 ~ 100만원</option>
                        <option value="100만원 이상">100만원 이상</option>
                    </select>
                </div>
                <div style={styles.question}>
                    <label style={styles.label}>Q3. 원하고자 하는 인플루언서의 메인 활동 플랫폼을 선택해주세요.</label>
                    <select
                        style={styles.select}
                        value={formData.main_platform}
                        onChange={(e) => handleSelectChange("main_platform", e.target.value)}
                    >
                        <option value="선택">선택</option>
                        <option value="인스타그램">인스타그램</option>
                        <option value="유튜브">유튜브</option>
                        <option value="틱톡">틱톡</option>
                        <option value="블로그">블로그</option>
                    </select>
                </div>
                <div style={styles.question}>
                    <label style={styles.label}>Q4. 원하고자 하는 홍보 이벤트를 선택해주세요.</label>
                    <select
                        style={styles.select}
                        value={formData.event_type}
                        onChange={(e) => handleSelectChange("event_type", e.target.value)}
                    >
                        <option value="선택">선택</option>
                        <option value="리뷰">리뷰</option>
                        <option value="이벤트 진행">이벤트 진행</option>
                        <option value="홍보 영상 제작">홍보 영상 제작</option>
                        <option value="기타">기타</option>
                    </select>
                </div>
                <div style={styles.question}>
                    <label style={styles.label}>Q5. 원하고자 하는 인플루언서의 성별을 입력해주세요.</label>
                    <select
                        style={styles.select}
                        value={formData.charactor_type}
                        onChange={(e) => handleSelectChange("charactor_type", e.target.value)}
                    >
                        <option value="선택">선택</option>
                        <option value="남성">남성</option>
                        <option value="여성">여성</option>
                        <option value="무관">무관</option>
                    </select>
                </div>
                
                <div style={styles.buttoncontainer}>
                    <button type="button" style={styles.submitButton} onClick={handleSubmit}>
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
      
        minHeight: "100vh",
        justifyContent: "space-between", // 좌우 요소 간 여백 균일화
    },
    sideCard: {
        width: "25%",
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
 
   
    form: {
        display: "flex",
        flexDirection: "column",
        gap: "15px",
       
    },
    question: {
        display: "flex",
        flexDirection: "column",
        gap: "15px",
        marginBottom: "70px"
    },
    label: {
        fontSize: "1.1rem",
        color: "#6d4c41",
        fontWeight: "500"
        
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
    },
    input: {
        width: "77%",
        padding: "10px",
        borderRadius: "10px",
        border: "1px solid #ddd",
        fontSize: "1rem",
        backgroundColor: "#fff",
        cursor: "pointer",
       
        marginLeft: "20px"
    },
    section: {
        fontFamily: "'Lexend Deca', sans-serif",
        fontSize: "2rem",
        background: "linear-gradient(90deg, #A57451 0%, #CDAC7F 33.9%, #E1C897 63.4%, #F5E4AE 100%)",
        WebkitBackgroundClip: "text",
        WebkitTextFillColor: "transparent",
       
 
        lineHeight: "1.5", // 줄 간격 설정
     
        
    },
    sectionLine: {
        height: "3px",
        width: "100%",
        background: "linear-gradient(90deg, #A57451 0%, #CDAC7F 33.9%, #E1C897 63.4%, #F5E4AE 100%)",
        marginBottom: "20px"

    },
    loadingContainer: {
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        minHeight: "100vh",
        backgroundColor: "#fffaea",
    },
    
    loadingSpinner: {
        width: "50px",
        height: "50px",
        border: "5px solid #f3f3f3",
        borderTop: "5px solid #6d4c41",
        borderRadius: "50%",
        animation: "spin 1s linear infinite",
    },
    loadingText: {
        marginTop: "20px",
        fontSize: "1.2rem",
        color: "#6d4c41",
    },
};

export default YesPage;
