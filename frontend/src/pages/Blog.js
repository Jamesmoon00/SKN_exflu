import React from "react";
import profileImage from "../assets/img/eddy_blog.png";
import Write from "../components/Write.js";

const Blog = () => {
    return (
        <div style={styles.container}>
            {/* 왼쪽 사이드바 */}
            <div style={styles.sidebar}>
                <img src={profileImage} alt="Profile" style={styles.profileImage} />
                <h2 style={styles.blogTitle}>Eddy's Blog</h2>
                <p style={styles.description}>This is a description..</p>
            </div>

            {/* 오른쪽 게시글 리스트 */}
            <div style={styles.blogList}>
                <div style={styles.blogHeader}>
                    <p style={styles.postCount}>목록</p>
                    <div style={styles.postHeader}>
                        <span>글 제목</span>
                        <span>작성일</span>
                    </div>
                </div>
            </div>
            {/* <Write /> */}
        </div> // 모든 내용을 하나의 최상위 요소로 감쌈
    );
};


// 스타일
const styles = {
    container: {
        display: "flex",
        // padding: "20px",
        backgroundColor: "#fffaea",
        height: "100vh",
        // boxSizing: "border-box",
    },
    sidebar: {
        marginTop: "30px",
        // flex: "1",
        backgroundColor: "#fffdf7",
        borderRadius: "10px",
        padding: "30px",
        boxShadow: "0 4px 8px rgba(0, 0, 0, 0.1)",
        textAlign: "center",
        marginBottom: "30px"
    
    },
    profileImage: {
        width: "100%",
        marginTop: "40px",
        width: "250px",
        height: "250px",
        borderRadius: "50%",
        objectFit: "cover",
        marginBottom: "15px",
    },
    blogTitle: {
        fontSize: "1.5rem",
        fontWeight: "bold",
        marginBottom: "10px",
        marginTip: "30px"
    },
    description: {
        fontSize: "0.9rem",
        color: "#555",
    },
    blogList: {
        flex: "3",
        marginLeft: "40px",
        width: "100%"
    },
    blogHeader: {
        borderBottom: "2px solid #f5e4ae",
        paddingBottom: "10px",
        marginBottom: "20px",
        width: "100%"
    },
    postCount: {
        marginTop: "30px",
        fontSize: "1rem",
        marginBottom: "5px",
    },
    postHeader: {
        display: "flex",
        justifyContent: "space-between",
        fontSize: "0.9rem",
        color: "#555",
    },
    postList: {
        borderTop: "1px solid #f5e4ae",
        width:"100px"
    },
    postItem: {
        display: "flex",
        justifyContent: "space-between",
        padding: "10px 0",
        borderBottom: "1px solid #f5e4ae",
        fontSize: "0.9rem",
    },
    pagination: {
        marginTop: "20px",
        display: "flex",
        justifyContent: "center",
    },
    pageButton: {
        backgroundColor: "#f5e4ae",
        border: "none",
        borderRadius: "5px",
        padding: "5px 10px",
        fontSize: "0.9rem",
        cursor: "pointer",
    },
};

export default Blog;
