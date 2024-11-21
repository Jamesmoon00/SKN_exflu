import React from "react";
import profileImage from "../assets/img/eddy_blog.png";


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
                        <span style={styles.postNum}>번호</span>
                        <span style={styles.postTitle}>글 제목</span>
                        <span style={styles.postDate}>작성일</span>
                    </div>
                </div>
            </div>

           
            
        </div> // 모든 내용을 하나의 최상위 요소로 감쌈
    );
};


// 스타일
const styles = {
    container: {
        display: "flex",
        padding: "40px",
        backgroundColor: "#fffaea",
        height: "100vh",
        // boxSizing: "border-box",
    },
    sidebar: {
        marginTop: "30px",
        // flex: "1",
        backgroundColor: "#fffdf7",
        borderRadius: "10px",
        padding: "40px",
        boxShadow: "0 4px 8px rgba(0, 0, 0, 0.1)",
        textAlign: "center",
        marginBottom: "30px",
        boxShadow: `
        0px 2px 15px rgba(212, 165, 98, 0.3), 
        0px 4px 30px rgba(212, 165, 98, 0.2)
        `,
        
    
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
        flex: "2.5",
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
        alignItems:"center",
        // justifyContent: "space-between",
        fontSize: "0.9rem",
        color: "#555",
    },
    postNum: {
        flex :"1",
        textAlign: "left"
    },
    postTitle: {
        flex: "5",
        textAlign: "left", // 텍스트 중앙 정렬
    },
    postDate: {
        flex: "2",
        textAlign: "right"
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
