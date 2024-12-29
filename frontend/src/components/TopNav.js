import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";

const TopNav = () => {
    const [hoveredLink, setHoveredLink] = useState(null);
    const [hoveredLogo, setHoveredLogo] = useState(false);
    const [windowWidth, setWindowWidth] = useState(window.innerWidth);
    const [isMenuOpen, setIsMenuOpen] = useState(false);

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

    const toggleMenu = () => setIsMenuOpen((prev) => !prev);

    const handleMouseEnter = (link) => setHoveredLink(link);
    const handleMouseLeave = () => setHoveredLink(null);
    const handleLogoMouseEnter = () => setHoveredLogo(true);
    const handleLogoMouseLeave = () => setHoveredLogo(false);

    return (
        <div style={styles.container}>
            <div style={styles.navbar}>
                <div style={styles.navbarContent}>
                    {/* 로고 */}
                    <Link
                        to="/"
                        style={{
                            ...styles.logo,
                            fontSize: `${getFontSize(2)}rem`,
                            ...(hoveredLogo ? styles.logoHover : {}),
                        }}
                        onMouseEnter={handleLogoMouseEnter}
                        onMouseLeave={handleLogoMouseLeave}
                    >
                        eXflu;
                    </Link>

                    {/* 햄버거 메뉴 버튼 */}
                    {windowWidth < 768 && (
                        <button onClick={toggleMenu} style={styles.hamburger}>
                            ☰
                        </button>
                    )}

                    {/* 네비게이션 링크 */}
                    {(windowWidth >= 768 || isMenuOpen) && (
                        <div
                            style={{
                                ...styles.navLinks,
                                flexDirection: windowWidth < 768 ? "column" : "row", // 모바일에서 세로 정렬
                                gap: getGap(),
                                position: windowWidth < 768 ? "absolute" : "static",
                                top: windowWidth < 768 ? "70px" : "unset",
                                right: windowWidth < 768 ? "10px" : "unset",
                                backgroundColor: windowWidth < 768 ? "#fffaea" : "transparent",
                                padding: windowWidth < 768 ? "10px" : "unset",
                                boxShadow:
                                    windowWidth < 768 ? "0px 4px 8px rgba(0, 0, 0, 0.1)" : "none",
                                borderRadius: windowWidth < 768 ? "5px" : "none",
                                zIndex: 1000,
                                justifyContent: windowWidth >= 768 ? "center" : "flex-start", // PC에서 중앙 정렬
                            }}
                        >
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
                            <a
                                href="https://www.instagram.com/exflu.adi/?igsh=YXhyZzQ0NzdycDZ6"
                                target="_blank"
                                rel="noopener noreferrer"
                                style={styles.icon}
                            >
                                <img
                                    src="https://img.icons8.com/ios-glyphs/30/000000/instagram-new.png"
                                    alt="Instagram"
                                    style={{
                                        width: `${getFontSize(2.5)}rem`,
                                        height: `${getFontSize(2.5)}rem`,
                                    }}
                                />
                            </a>
                        </div>
                    )}
                </div>
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
        flexWrap: "wrap",
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
    hamburger: {
        fontSize: "1.5rem",
        background: "none",
        border: "none",
        cursor: "pointer",
        padding: "5px",
    },
};

export default TopNav