import React from "react";
import Eddy from "../assets/img/eddy.png";
import Confetti from "react-confetti";
import Snowfall from "react-snowfall";
const SecondSection = () => {
    return (
        <>
            <div style={styles.container}>
            {/* 눈 내리는 효과 */}
                <Snowfall
                    color="white" // 눈 색상
                    snowflakeCount={150} // 눈송이 개수
                    style={{ zIndex: 9999 }} // 눈이 모든 요소 위에 표시되도록 설정
                />
                {/* <Confetti
                    width={window.innerWidth} // 화면 가로 크기
                    height={window.innerHeight} // 화면 세로 크기
                    numberOfPieces={50} // 꽃가루 조각 개수
                    gravity={0.1} // 꽃가루 떨어지는 속도
                /> */}
                <img
                    src={Eddy}
                    alt="Character"
                    style={styles.image}
                />
            </div>
        </>
    );
};

const styles = {
    container: {
        display: "flex",
        justifyContent: "flex-start", // 가로 정렬: 왼쪽 정렬
        alignItems: "flex-end", // 세로 정렬: 아래쪽 정렬
        height: "100vh", // 한 화면에 꽉 차도록 설정
      
        padding: "20px", // 여백 추가
    },
    image: {
        width: "400px", // 이미지 크기
        height: "auto",
        marginLeft:"40px",
        marginBottom: "10px",
     
    },
};

export default SecondSection;
