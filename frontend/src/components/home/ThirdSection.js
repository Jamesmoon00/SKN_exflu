import React from "react"
import Eddyfilm from "../../assets/img/eddy_list.png"
const ThirdSection = () => {
    return (
        <>
            <div style={styles.container}>
                {/* 하단 이미지 */}
            <div style={styles.imageContainer}>
                <img src={Eddyfilm} alt="Character Scene" style={styles.image} />
            </div>
            </div>
        </>
    );
}

const styles = {
    container: {
        display: "flex",
        justifyContent: "flex-start",
        alignItems: "flex-end",
        height: "100vh",
        background: "linear-gradient(to bottom, #FFFAEA, #FFEFB9)",
        
    },
    imageContainer: {
        // height: "20%", // 하단 이미지 높이
        
        width: "100%",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        backgroundColor: "black", // 검은색 배경
    },
    image: {
        width: "100%", // 이미지 너비를 부모 요소에 맞춤
        height: "100%", // 이미지 높이를 부모 요소에 맞춤
        objectFit: "cover", // 이미지가 잘리지 않고 꽉 차도록 설정
    },
}
export default ThirdSection