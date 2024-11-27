import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";

const TopNav = () => {
    const [hoveredLink, setHoveredLink] = useState(null); // 현재 호버된 링크
    const [hoveredLogo, setHoveredLogo] = useState(false); // 로고 호버 상태
    const [hoveredIcon, setHoveredIcon] = useState(false); // 아이콘 호버 상태
    const [windowWidth, setWindowWidth] = useState(window.innerWidth); // 화면 너비 상태

    // 화면 크기 변경 감지
    useEffect(() => {
        const handleResize = () => setWindowWidth(window.innerWidth);
        window.addEventListener("resize", handleResize);
        return () => window.removeEventListener("resize", handleResize);
    }, []);

    // 동적으로 크기 반환
    const getFontSize = (baseSize) => {
        if (windowWidth < 768) return baseSize * 0.8;
        if (windowWidth < 480) return baseSize * 0.6;
        return baseSize;
    };

    const getGap = () => {
        if (windowWidth < 768) return "20px"; // 모바일 환경에서 간격 축소
        return "80px"; // PC 환경에서 간격 유지
    };

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
            <div style={styles.navbar}>
                <div style={styles.navbarContent}>
                    {/* 로고 */}
                    <Link
                        to="/"
                        style={{
                            ...styles.logo,
                            fontSize: `${getFontSize(2)}rem`, // 동적으로 글자 크기 설정
                            ...(hoveredLogo ? styles.logoHover : {}),
                        }}
                        onMouseEnter={handleLogoMouseEnter}
                        onMouseLeave={handleLogoMouseLeave}
                    >
                        eXflu;
                    </Link>

                    {/* 네비게이션 링크 */}
                    <div style={{ ...styles.navLinks, gap: getGap() }}>
                        {["profile", "blog", "contact"].map((text) => (
                            <Link
                                key={text}
                                to={`/${text}`}
                                style={{
                                    ...styles.link,
                                    fontSize: `${getFontSize(1.2)}rem`,
                                    ...(hoveredLink === text ? styles.linkHover : {}),
                                }}
                                onMouseEnter={() => handleMouseEnter(text)}
                                onMouseLeave={handleMouseLeave}
                            >
                                {text}
                            </Link>
                        ))}
                    </div>

                    {/* 아이콘 */}
                    <a
                        href="https://www.instagram.com"
                        target="_blank"
                        rel="noopener noreferrer"
                        style={{
                            ...styles.icon,
                            ...(hoveredIcon ? styles.iconHover : {}),
                        }}
                        onMouseEnter={handleIconMouseEnter}
                        onMouseLeave={handleIconMouseLeave}
                    >
                        <img
                            src="https://img.icons8.com/ios-glyphs/30/000000/instagram-new.png"
                            alt="Instagram"
                            style={{
                                ...styles.iconsize,
                                width: `${getFontSize(2.5)}rem`,
                                height: `${getFontSize(2.5)}rem`,
                            }}
                        />
                    </a>
                </div>
                {/* 가로선 */}
                <div style={styles.contentLine}></div>
            </div>
        </div>
    );
};

const styles = {
    container: {
        width: "100%",
    },
    navbar: {
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        backgroundColor: "#fffaea",
        padding: "5px 0",
        width: "100%",
        boxSizing: "border-box",
        position: "relative",
    },
    navbarContent: {
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
        width: "95%",
        boxSizing: "border-box",
        flexWrap: "wrap", // 줄바꿈 허용
    },
    contentLine: {
        width: "95%",
        height: "1.5px",
        backgroundColor: "#F1D1A3",
        boxShadow: `
            0px 2px 15px rgba(212, 165, 98, 0.9), 
            0px 4px 30px rgba(212, 165, 98, 0.7)
        `,
        position: "absolute",
        bottom: 0,
    },
    logo: {
        fontSize: "2rem",
        fontWeight: "bold",
        textDecoration: "none",
        color: "#000",
        transition: "all 0.3s ease-in-out",
        background: "linear-gradient(to bottom, #3F201F, #A57451)",
        WebkitBackgroundClip: "text",
        WebkitTextFillColor: "transparent",
    },
    logoHover: {
        fontSize: "2.4rem",
        color: "lightgray",
    },
    navLinks: {
        display: "flex",
        alignItems: "center",
    },
    link: {
        textDecoration: "none",
        color: "#000",
        padding: 5,
        fontSize: "1.2rem",
        transition: "all 0.3s ease-in-out",
    },
    linkHover: {
        fontSize: "1.4rem",
        color: "#A57451",
        fontWeight: "bold",
    },
    icon: {
        display: "flex",
        alignItems: "center",
        transition: "all 0.3s ease-in-out",
    },
    iconHover: {
        transform: "scale(1.1)",
    },
    iconsize: {
        marginTop: "5px",
    },
};

export default TopNav;
