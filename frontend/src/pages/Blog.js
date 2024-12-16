import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import SideCard from "../components/board/SideCard";

const Blog = () => {
    const [posts, setPosts] = useState([]); // 게시글 데이터를 저장할 상태
    const [currentPage, setCurrentPage] = useState(1); // 현재 페이지
    const [pageSize] = useState(12); // 한 페이지당 게시글 수
    const [isMobile, setIsMobile] = useState(window.innerWidth <= 768); // 모바일 여부
    const [showSideCard, setShowSideCard] = useState(true); // SideCard 표시 여부
    const navigate = useNavigate();

    useEffect(() => {
        // 서버에서 데이터 가져오기
        const fetchPosts = async () => {
            try {
                const response = await axios.get(`${process.env.REACT_APP_SERVER_URL}blog/`); // 서버 API URL
                // 최신글 순으로 정렬
                const sortedPosts = response.data.sort(
                    (a, b) => new Date(b.created_at) - new Date(a.created_at)
                );

                setPosts(sortedPosts); // 정렬된 데이터 상태에 저장
                console.log(sortedPosts);
            } catch (error) {
                console.error("데이터를 가져오는 중 오류 발생:", error);
            }
        };

        fetchPosts();
    }, []); // 컴포넌트가 마운트될 때 한 번 실행

    useEffect(() => {
        const handleResize = () => {
            setShowSideCard(window.innerWidth > 1000);
            setIsMobile(window.innerWidth <= 768);
        };

        handleResize();
        window.addEventListener("resize", handleResize);
        return () => window.removeEventListener("resize", handleResize);
    }, []);

    // 현재 페이지에 해당하는 데이터만 가져오기
    const paginatedPosts = posts.slice((currentPage - 1) * pageSize, currentPage * pageSize);

    // 총 페이지 수 계산
    const totalPages = Math.ceil(posts.length / pageSize);

    // 페이지 변경 핸들러
    const handlePageChange = (newPage) => {
        if (newPage >= 1 && newPage <= totalPages) {
            setCurrentPage(newPage);
        }
    };

    return (
        <div
            style={{
                ...styles.container,
                marginLeft: showSideCard ? "45px" : "0",
                marginRight: isMobile ? "25px" : "45px",
            }}
        >
            {showSideCard && <SideCard style={styles.sideCard} />}
            <div
                style={{
                    ...styles.blogList,
                    marginLeft: isMobile ? "20px" : "40px",
                    marginRight: isMobile ? "-25px" : "0px",
                }}
            >
             
                    <div style={styles.blogHeader}>
                        <p style={styles.postCount}>✏️목록</p>
                        <div style={styles.postHeader}>
                            <span style={styles.postNum}>번호</span>
                            <span style={styles.postTitle}>글 제목</span>
                            <span style={styles.postDate}>작성일</span>
                        </div>
                    </div>
                    <div>
                        {paginatedPosts.length > 0 ? (
                            paginatedPosts.map((post, index) => (
                                <div
                                    key={post.post_id}
                                    style={{ ...styles.postItem, cursor: "pointer" }}
                                    onClick={() => navigate(`/blog/${post.post_id}`)}
                                >
                                    <span style={styles.postNum}>
                                        {index + 1 + (currentPage - 1) * pageSize}
                                    </span>
                                    <span style={styles.postTitle}>{post.title}</span>
                                    <span style={styles.postDate}>
                                        {post.created_at.split("T")[0]}
                                    </span>
                                </div>
                            ))
                        ) : (
                            <p style={{ textAlign: "center" }}>게시글이 없습니다.</p>
                        )}
                    </div>
                    {/* 페이지네이션 */}
                    <div style={styles.pagination}>
                        <button
                            onClick={() => handlePageChange(currentPage - 1)}
                            disabled={currentPage === 1}
                            style={styles.pageButton}
                        >
                            이전
                        </button>
                        <span>
                            {currentPage} / {totalPages}
                        </span>
                        <button
                            onClick={() => handlePageChange(currentPage + 1)}
                            disabled={currentPage === totalPages}
                            style={styles.pageButton}
                        >
                            다음
                        </button>
                    </div>
                
            </div>
        </div>
    );
};

const styles = {
    container: {
        display: "flex",
        marginLeft: "45px",
        marginRight: "45px",
        backgroundColor: "#fffaea",
        // minHeight: "100vh",
        flexDirection: "row",
        justifyContent: "flex-start",
        height: "100%", // 부모 컨테이너 높이 맞추기
    },
    sideCard: {
        flex: "1",
        height: "100%",  // 사이드 카드 높이 맞추기
        minHeight: "100vh",
    },
    blogList: {
        flex: "3",
        marginTop: "30px",
        marginBottom: "30px",
        height: "100%",  // 블로그 리스트 높이 맞추기
    },
    post: {
        borderRadius: "10px",
        overflow: "auto",
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
        marginTop: "5px",
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
        padding: "10px 10px",
        borderBottom: "1px solid #f5e4ae",
        fontSize: "0.9rem",
    },
    pagination: {
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        padding: "60px 0px 0px",
        marginTop: "60px",
        gap: "10px",
        marginBottom: "0px"
    },
    pageButton: {
        padding: "5px 10px",
        cursor: "pointer",
        backgroundColor: "#fffaea",
        border: "1px solid #f5e4ae",
        borderRadius: "5px",
        fontSize: "0.9rem",
    },
};

export default Blog;
