import React, { useState, useEffect } from "react";
import FirstSection from "../components/home/FirstSection";
import ThirdSection from "../components/home/ThirdSection";

const Home = () => {
    const [activeSection, setActiveSection] = useState(0); // 현재 활성화된 섹션 (0: 첫 번째)

    useEffect(() => {
        const handleScroll = () => {
            const scrollY = window.scrollY;
            const windowHeight = window.innerHeight;

            // 스크롤 위치에 따라 activeSection 변경
            if (scrollY < windowHeight * 0.8) {
                setActiveSection(0); // 첫 번째 섹션
            } else if (scrollY >= windowHeight * 0.8 && scrollY < windowHeight * 1.8) {
                setActiveSection(1); // 두 번째 섹션
            } else if (scrollY >= windowHeight * 1.8) {
                setActiveSection(2); // 세 번째 섹션
            }
        };

        window.addEventListener("scroll", handleScroll);
        return () => window.removeEventListener("scroll", handleScroll);
    }, []);

    return (
        <div style={styles.container}>
            {/* 모든 섹션을 렌더링하고 활성화된 섹션에 애니메이션 적용 */}
            <div
                style={{
                    ...styles.section,
                    opacity: activeSection === 0 ? 1 : 0,
                    transform: activeSection === 0 ? "translateY(0)" : "translateY(20px)",
                    transition: "opacity 0.5s ease, transform 0.5s ease",
                }}
            >
                <FirstSection />
            </div>
            <div
                style={{
                    ...styles.section,
                    opacity: activeSection === 1 ? 1 : 0,
                    transform: activeSection === 1 ? "translateY(0)" : "translateY(20px)",
                    transition: "opacity 0.5s ease, transform 0.5s ease",
                }}
            >
                <ThirdSection />
            </div>
            {/* <div
                style={{
                    ...styles.section,
                    opacity: activeSection === 2 ? 1 : 0,
                    transform: activeSection === 2 ? "translateY(0)" : "translateY(20px)",
                    transition: "opacity 0.5s ease, transform 0.5s ease",
                }}
            >
                <ThirdSection />
            </div> */}
        </div>
    );
};

const styles = {
    container: {
        width: "100%",
        height: "200vh", // 전체 높이 설정 (각 섹션 100vh씩 3배)
        overflowX: "hidden", // 가로 스크롤 방지
        overflowY: "hidden", // 세로 스크롤 방지 (필요 시 추가)
    },
    section: {
        position: "sticky",
        top: 0,
        height: "100vh", // 한 화면을 가득 채우도록 설정
        width: "100%",
        display: "flex", // 섹션 내용 가운데 정렬
        justifyContent: "center",
        alignItems: "center",
    },
};

export default Home;
