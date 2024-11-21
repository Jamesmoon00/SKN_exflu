import React, { useState } from "react";
import { Link } from "react-router-dom";

const TopNav = () => {
    const [hoveredLink, setHoveredLink] = useState(null); // 현재 호버된 링크
    const [hoveredLogo, setHoveredLogo] = useState(false); // 로고 호버 상태
    const [hoveredIcon, setHoveredIcon] = useState(false); // 아이콘 호버 상태

    const handleMouseEnter = (link) => {
        setHoveredLink(link); // 호버된 링크 설정
    };

    const handleMouseLeave = () => {
        setHoveredLink(null); // 호버 해제
    };

    const handleLogoMouseEnter = () => {
        setHoveredLogo(true); // 로고 호버
    };

    const handleLogoMouseLeave = () => {
        setHoveredLogo(false); // 로고 호버 해제
    };

    const handleIconMouseEnter = () => {
        setHoveredIcon(true); // 아이콘 호버
    };

    const handleIconMouseLeave = () => {
        setHoveredIcon(false); // 아이콘 호버 해제
    };

    return (
        <div style={styles.container}>
            {/* 네비게이션 바 */}
            <div style={styles.navbar}>
                <div style={styles.navbarContent}>
                    <Link
                        to="/"
                        style={hoveredLogo ? { ...styles.logo, ...styles.logoHover } : styles.logo}
                        onMouseEnter={handleLogoMouseEnter}
                        onMouseLeave={handleLogoMouseLeave}
                    >
                        exFlu;
                    </Link>
                    <div style={styles.navLinks}>
                        {["profile", "blog", "contact "].map((text) => (
                            <Link
                                key={text}
                                to={`/${text.replace(/\s/g, "-")}`}
                                style={
                                    hoveredLink === text
                                        ? { ...styles.link, ...styles.linkHover }
                                        : styles.link
                                }
                                onMouseEnter={() => handleMouseEnter(text)}
                                onMouseLeave={handleMouseLeave}
                            >
                                {text}
                            </Link>
                        ))}
                    </div>
                    <a
                        href="https://www.instagram.com"
                        target="_blank"
                        rel="noopener noreferrer"
                        style={hoveredIcon ? { ...styles.icon, ...styles.iconHover } : styles.icon}
                        onMouseEnter={handleIconMouseEnter}
                        onMouseLeave={handleIconMouseLeave}
                    >
                        <img
                            src="https://img.icons8.com/ios-glyphs/30/000000/instagram-new.png"
                            alt="Instagram" style={styles.iconsize}
                        />
                    </a>
                </div>
                {/* 가로선 */}
                <div style={styles.navbarLine}></div>
            </div>
        </div>
    );
};
const styles = {
    navbar: {
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        backgroundColor: "#fffaea",
        padding: "5px 0", // 패딩을 줄여 높이를 얇게 조정
        width: "100%",
        height: "70px", // 네비게이션 바의 높이 축소
        boxSizing: "border-box",
        position: "relative", // 선 고정을 위한 부모 요소 설정
    },
    navbarContent: {
    
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
        width: "95%",
        maxWidth: "1600px",
        boxSizing: "border-box",
        height: "50px", // 내용 높이를 축소하여 더 얇게
    },
    navbarLine: {
        width: "95%",
        maxWidth: "1600px",
        height: "1px", // 선의 두께를 줄여 더 깔끔하게
        boxShadow: `
            0px 2px 15px rgba(212, 165, 98, 0.9), 
            0px 4px 30px rgba(212, 165, 98, 0.7)
        `,
        backgroundColor: "#F1D1A3",
        position: "absolute",
        bottom: 0,
    },
    logo: {
        fontSize: "2rem", // 로고 크기를 줄여 네비바 높이에 맞춤
        fontWeight: "bold",
        textDecoration: "none",
        color: "#000",
        transition: "all 0.3s ease-in-out",
        background: "linear-gradient(to bottom, #3F201F, #A57451)", // 그라데이션 효과
        WebkitBackgroundClip: "text", // 텍스트에만 적용
        WebkitTextFillColor: "transparent", // 텍스트 내부를 투명하게
    },
    logoHover: {
        fontSize: "2.4rem", // 호버 시 크기 조금만 증가
        color: "lightgray",
    },
    navLinks: {
        display: "flex",
        gap: "50px", // 링크 간 간격을 줄여 간결하게
        alignItems: "center",
    },
    link: {
        textDecoration: "none",
        color: "#000",
        padding: 5, // 패딩을 줄여 높이 최적화
        fontSize: "1.2rem", // 글씨 크기를 줄여 균형 맞춤
        transition: "all 0.3s ease-in-out",
        marginRight: "20px"
    },
    linkHover: {
        fontSize: "1.4rem",
        color: "#A57451",
        fontWeight: "bold",
    },
    icon: {
        width: "45px",
        height: "40px",
        display: "flex",
        alignItems: "center",
        transition: "all 0.3s ease-in-out",
    },
    iconHover: {
        transform: "scale(1.1)", // 호버 시 크기 살짝만 증가
        fontSize: "2rem"
    },
    iconsize: {
        marginTop: "5px",
        width: "40px"
    }
};


export default TopNav;
