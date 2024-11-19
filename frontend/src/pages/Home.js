import React, { useState, useEffect } from "react";
import FirstSection from "../components/FirstSection";
import SecondSection from "../components/SecondSection";
import ThirdSection from "../components/ThirdSection";

const Home = () => {
    const [activeSection, setActiveSection] = useState(0); // 현재 활성화된 화면 (0: 첫 화면)

    useEffect(() => {
        const handleScroll = () => {
        const scrollY = window.scrollY;
        const windowHeight = window.innerHeight;
        // 스크롤 위치에 따라 activeSection 변경
        if (scrollY < windowHeight * 0.5) {
          setActiveSection(0); // 첫 번째 화면
        } else if (scrollY < windowHeight * 1.5) {
          setActiveSection(1); // 두 번째 화면
        } else {
          setActiveSection(2); // 세 번째 화면
        }
        };

        window.addEventListener("scroll", handleScroll);

        return () => {
        window.removeEventListener("scroll", handleScroll);
        };
    }, []);

    return (
        <div style={styles.container}>
            <div
                style={{
                    ...styles.section,
                    animation: "fadeIn 1s ease-in-out",
                }}
                key={activeSection} // Section이 바뀔 때마다 키를 변경해 애니메이션을 적용
            >
            
                {activeSection === 0 && <FirstSection />}
                {activeSection === 1 && <SecondSection />}
                {activeSection === 2 && <ThirdSection />}
            </div>
        </div>
    );
};
const styles = {
    container: {
        width: "100%",
        height: "300vh", // 총 화면 높이를 크게 설정
        // backgroundColor: "#ffffff",
    },
    section: {
        position: "sticky",
        top: 0,
        height: "100vh", // 한 화면에 꽉 차게 설정
        // display: "flex",
        width: "95%",
        justifyContent: "center",
        alignItems: "center",
    },
}
// CSS 애니메이션 추가
const styleSheet = document.styleSheets[0];
styleSheet.insertRule(
    `@keyframes fadeIn {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }`,
    styleSheet.cssRules.length
);

export default Home