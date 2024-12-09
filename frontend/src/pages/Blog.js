import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import SideCard from "../components/board/SideCard";

const Blog = () => {
    const [posts, setPosts] = useState([]); // 게시글 데이터를 저장할 상태
   
    const [showSideCard, setShowSideCard] = useState(true); // SideCard 표시 여부 상태
    const [isMobile, setIsMobile] = useState(window.innerWidth <= 768);
    const navigate = useNavigate();
    const formatDate = (dateString) => {
        if(!dateString) return "";
        return dateString.split("T")[0];
    }

    useEffect(() => {
        // 서버에서 데이터 가져오기
        const fetchPosts = async () => {
            try {
                const response = await axios.get(`${process.env.REACT_APP_SERVER_URL}blog/`); // 서버 API URL
                setPosts(response.data); // 데이터를 상태에 저장
                // console.log(response.data)
            } catch (error) {
                console.error("데이터를 가져오는 중 오류 발생:", error);
            }
        };

        fetchPosts(); // 함수 호출
    }, []); // 컴포넌트가 마운트될 때 한 번 실행

    useEffect(() => {
        const handleResize = () => {
            setShowSideCard(window.innerWidth > 1000); // 768px 이하일 때 SideCard 숨김
            setIsMobile(window.innerWidth <= 768);
        };

        handleResize(); // 초기 크기 설정
        window.addEventListener("resize", handleResize); // 리사이즈 이벤트 추가
        return () => window.removeEventListener("resize", handleResize); // 이벤트 제거
    }, []);
    
    // 게시글 클릭 시 상세 내용 가져오기
    


    return (
        <div
            style={{
                ...styles.container,
                marginLeft: showSideCard ? "45px" : "0", // SideNav가 없으면 marginLeft를 0으로 설정
                marginRight: isMobile ? "25px" : "45px"
            }}
        >
            {/* 왼쪽 사이드바 */}
            {/* SideCard는 showSideCard가 true일 때만 렌더링 */}
            {showSideCard && <SideCard />}
            {/* 오른쪽 게시글 리스트 */}
            <div style={{...styles.blogList,
                marginLeft : isMobile ? "20px" : "40px",
                marginRignt : isMobile ? "-25px" : "0px"
            }}>
                <div style={styles.blogHeader}>
                    <p style={styles.postCount}>✏️목록</p>
                    <div style={styles.postHeader}>
                        <span style={styles.postNum}>번호</span>
                        <span style={styles.postTitle}>글 제목</span>
                        <span style={styles.postDate}>작성일</span>
                    </div>
                </div>
                <div>
                    {posts.length > 0 ? (
                        posts.map((post, index) => (
                            <div
                                key={post.post_id}
                                style={{ ...styles.postItem, cursor: "pointer" }} // 클릭 가능 스타일 추가
                                onClick={() => navigate(`/blog/${post.post_id}`)} // 게시글 상세 페이지로 이동
                            >
                                <span style={styles.postNum}>{index + 1}</span>
                                <span style={styles.postTitle}>{post.title}</span>
                                <span style={styles.postDate}>{formatDate(post.created_at)}</span>
                            </div>
                        ))
                    ) : (
                        <p style={{ textAlign: "center" }}>게시글이 없습니다.</p>
                    )}
                </div>
            </div>

            
        </div>
    );
};

// 스타일
const styles = {
    container: {
        display: "flex",
        marginLeft: "45px",
        marginRight: "45px",
        backgroundColor: "#fffaea",
        height: "100vh",
    },
    sideCard: {
        width: "25%",
    },
    blogList: {
        flex: "2.5",
        marginLeft: "40px",
        width: "100%",
        marginTop: "20px"
    },
    blogHeader: {
        borderBottom: "2px solid #F1D1A3",
        paddingBottom: "10px",
        marginBottom: "0px",
        
  
    },
    postCount: {
        fontSize: "1rem",
        marginBottom: "5px",
    },
    postHeader: {
        display: "flex",
        alignItems: "center",
        fontSize: "0.9rem",
        color: "#555",
        marginTop: "5px"
    },
    postNum: {
        flex: "1",
        textAlign: "left",
    },
    postTitle: {
        flex: "5",
        textAlign: "left",
    },
    postDate: {
        flex: "2",
        textAlign: "right",
    },
    postItem: {
        display: "flex",
        justifyContent: "space-between",
        padding: "12px 10px",
        borderBottom: "1px solid #f5e4ae",
        fontSize: "0.9rem",
        

    },
};

export default Blog;
