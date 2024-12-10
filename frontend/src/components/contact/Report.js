import React from "react";
import "@fontsource/lexend-deca"; // npm에서 제공하는 경우
import campaign from "../../assets/img/capaignImage.png";
import TableComponent from "./components/Table";
import LineChart from "./components/LineChart";
import BarChart from "./components/Barchart";
import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    BarElement,
    PointElement, // 추가
    LineElement, // 추가
    ArcElement,
    Tooltip,
    Legend,
    Title,
} from "chart.js";

ChartJS.register(CategoryScale, LinearScale, BarElement, PointElement, Title, LineElement, ArcElement, Tooltip, Legend);
const Report = () => {
    const lineData = {
        labels: ["7월", "8월", "9월", "10월", "11월", "12월"],
        datasets: [
            {
             
                label: "매출 추이",
                data: [70, 80, 90, 100, 110, 120],
                borderColor: "#D98077",
                borderWidth: 2,
                tension: 0.4,
                fill: false,
            },
        ],
    };
    const barData = {
        labels: ["인플루언서", "에디"],
        datasets: [
            {
                label: "매출",
                data: [460, 160],
                backgroundColor: "#D98077",
            },
        ],
    };
    console.log(barData);
    
    const tableData = [
        { no: 1, content: "좋아요 1등 게시물", likes: 100, comments: 10 },
        { no: 2, content: "좋아요 2등 게시물", likes: 90, comments: 10 },
        { no: 3, content: "좋아요 3등 게시물", likes: 80, comments: 10 },
        { no: 4, content: "좋아요 4등 게시물", likes: 70, comments: 10 },
        { no: 5, content: "좋아요 5등 게시물", likes: 60, comments: 10 },
    ];

    return (
        <div style={styles.container}>
            <p style={styles.reportTitle}>Bussiness Report</p>
            <div style={styles.gradientLine}></div>

            <div style={styles.overviewContainer}>
                {/* 왼쪽 영역: "1. 개요" */}
                <div style={styles.overviewTitle}>1. 개요</div>

                {/* 오른쪽 영역: 이미지와 설명 */}
                <div style={styles.overview}>
                    <img src={campaign} alt="campaign" style={styles.overviewImg} />
                    <div style={styles.overviewDescription}>
                        <p style={styles.descriptionTitle}>🚀SK Network 부트캠프 홍보 마케팅🚀</p>
                        <p style={styles.descriptionItem}>기간: xxxx.xx.xx ~ xxxx.xx.xx</p>
                        <p style={styles.descriptionItem}>콘텐츠 등록 기간: xxxx.xx.xx ~ xxxx.xx.xx</p>
                        <p style={styles.descriptionItem}>보고서 기준 날짜: xxxx.xx.xx</p>
                        <p style={styles.descriptionItem}>설명: 홍보캠페인 설명부분입니다.</p>
                    </div>
                </div>
            </div>

            {/* 등록 컨텐츠 영역 */}
            <div style={styles.overviewContainer}>
                {/* 왼쪽 영역: "2. 등록 컨텐츠" */}
                <div style={styles.overviewTitle}>2. 등록 컨텐츠</div>

                {/* 오른쪽 영역: 테이블 */}
                <div style={styles.overview}>
                    <div style={styles.tableBox}>
                        <TableComponent data={tableData} />

                    </div>

                </div>
            </div>
            {/* 등록 컨텐츠 영역 */}
            <div style={styles.overviewContainer}>
                {/* 왼쪽 영역: "2. 등록 컨텐츠" */}
                <div style={styles.overviewTitle}>3. 캠페인 성과</div>

                {/* 오른쪽 영역: 차트 넣을것 */}
                <div style={{ ...styles.overview}}>
                    <div style={styles.twoBoxes}>
                        <div style={styles.box}>
                           
                            <BarChart data={barData} />
                        </div>
                        <div style={styles.box}>
                            <LineChart data={lineData} />

                        </div>
                    </div>
                </div>
            </div>

            {/* 등록 컨텐츠 영역 */}
            <div style={styles.overviewContainer}>
                {/* 왼쪽 영역: "2. 등록 컨텐츠" */}
                <div style={styles.overviewTitle}>4. 방문자 분석</div>

                {/* 오른쪽 영역: 조회수 */}
                <div style={{...styles.overview, borderBottom: "0px"}}>
                    {/* 나란히 있는 3개의 버튼 */}
                    <div style={styles.threeButtons}>
                        <div style={{ ...styles.button, backgroundColor: "#FFF3CA" }}>
                            <p style={styles.buttonTitle}>총 조회수</p>
                            <p style={styles.buttonValue}>10,234 회</p>
                        </div>
                        <div style={{ ...styles.button, backgroundColor: "#FFEFB8" }}>
                            <p style={styles.buttonTitle}>평균 조회수</p>
                            <p style={styles.buttonValue}>1,111 회</p>
                        </div>
                        <div style={{ ...styles.button, backgroundColor: "#FBE5A2" }}>
                            <p style={styles.buttonTitle}>평균 체류 시간</p>
                            <p style={styles.buttonValue}>45초</p>
                        </div>
                    </div>


                </div>
            </div>
        </div>
    );
};

const styles = {
    container: {
        display: "flex",
        flexDirection: "column",
        marginLeft: "45px",
        marginRight: "45px",
        backgroundColor: "#fffaea",
        minHeight: "100vh",
    },
    reportTitle: {
        textAlign: "right",
        fontFamily: "'Lexend Deca', sans-serif",
        fontWeight: "400",
        fontSize: "64px",
        background: "linear-gradient(90deg, #3F201F 0%, #724A38 33.9%, #8C5F45 63.4%, #FFEFB8 100%)",
        WebkitBackgroundClip: "text",
        WebkitTextFillColor: "transparent",
        marginTop: "40px",
        marginBottom: "5px",
    },
    gradientLine: {
        height: "3px",
        width: "100%",
        background: "linear-gradient(90deg, #3F201F 0%, #724A38 33.9%, #8C5F45 63.4%, #FFEFB8 100%)",
        borderRadius: "2px",
    },
    overviewContainer: {
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
        marginBottom: "20px",
    },
    overviewTitle: {
        flex: "1",
        textAlign: "center",
        fontFamily: "'Lexend Deca', sans-serif",

    },
    overview: {
        flex: "4",
        display: "flex",
        padding: "30px",
        marginLeft: "20px",
        justifyContent: "flex-start",
        marginBottom: "5px",
        borderBottom: "2px solid #F5E4AE"
    },
    overviewImg: {
        width: "20%",
        borderRadius: "10px",
        boxShadow: "0 4px 8px rgba(0, 0, 0, 0.1)",
        marginRight: "30px",
    },
    overviewDescription: {
        fontFamily: "'Lexend Deca', sans-serif",
        marginLeft: "20px",
    },
    descriptionTitle: {
        fontSize: "25px",
        fontWeight: "bold",
        marginBottom: "10px",
    },
    descriptionItem: {
        marginBottom: "5px",
    },
    tableBox: {
        display: "flex",
        
        flex: "4",
        border: "2px solid #F5E4AE",
        borderRadius: "20px",
        padding: "10px",
        backgroundColor: "#fffdf7",
        boxShadow: "0 4px 8px rgba(0, 0, 0, 0.1)",
        width: "30%",
        marginTop: "-20px"
       
    },
    
    twoBoxes: {
        display: "flex",
        gap: "30px", // 두 박스 간의 간격
        marginTop: "-20px",
        marginLeft: "0px"
    },
    box: {
        flex: "1",
        height: "300px",
        width: "100%",
        backgroundColor: "#fffdf7",
        border: "2px solid #F5E4AE",
        borderRadius: "20px",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        boxShadow: "0 4px 8px rgba(0, 0, 0, 0.1)",
        padding: "30px"
    },
    threeButtons: {
        display: "flex",
        justifyContent: "space-between",
        gap: "40px",
        width: "100%",
        marginTop: "-20px"
    },
    button: {
        flex: "1",
        backgroundColor: "#FBE5A2",
      
        borderRadius: "30px",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        padding: "15px",
        boxShadow: "0 4px 8px rgba(0, 0, 0, 0.1)",
    },
    buttonTitle: {
        fontSize: "16px",
        color: "#333",
        marginBottom: "10px",
        textAlign: "left"
    },
    buttonValue: {
        fontSize: "24px",
        fontWeight: "bold",
        color: "#000",
    },
};

export default Report;
