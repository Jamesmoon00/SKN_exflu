import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import { useRecoilState } from "recoil";
import { likeState } from "../components/board/recoil/atoms";
import axios from "axios";
import profileImage from "../assets/img/eddy_profile.png";
import bombImage from "../assets/img/bomb_eddy.png";
import hearticon from "../assets/icons/heart.png";
import comment from "../assets/icons/comment.png";
import commentwrite from "../assets/icons/write.png";
import SideCard from "./board/SideCard";
import CommentList from "./board/CommentList";
import CommentForm from "./board/CommentForm";
import Loading from "./contact/components/Loading";
import ReactMarkdown from "react-markdown"; // react-markdown import


const Write = () => {
    const { id } = useParams(); // URL에서 게시글 ID 가져오기
    const [likes, setLikes]=useState(0);
    const [titles, setTitles] = useState("");
    const [post, setPost] = useState(null); // 게시글 데이터 상태'
    const [date, setDate] = useState("");
    const [comments, setComments] = useState([]);
    const [image, setImage] = useState(bombImage);
    const [showSideCard, setShowSideCard] = useState(true); // SideCard 표시 여부 상태
    const [isMobile, setIsMobile] = useState(window.innerWidth <= 768); // 모바일 여부 상태
    const [isLiked, setIsLiked] = useState(false); // 좋아요 버튼 상태
    const [likeMap, setLikeMap] = useRecoilState(likeState);
    const formatDate = (dateString) => {
        const date = new Date(dateString);
        return `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, "0")}-${String(date.getDate()).padStart(2, "0")}`;
    };

    useEffect(() => {
        // 좋아요 상태 초기화
        if (likeMap[id]) {
            setIsLiked(true);
        }
    }, [id, likeMap]);
    useEffect(() => {
        const fetchPost = async () => {
            try {
                const response = await axios.get(`${process.env.REACT_APP_SERVER_URL}blog/`);
                const postData = response.data.find((item) => item.post_id === parseInt(id)); // 특정 post_id의 데이터 찾기
                
                if (postData) {
                    setPost(postData);
                    // console.log("ddd",response);
                    // console.log("whgd",response.data);
                    // console.log("rere", postData.likes);
                    setTitles(postData.title);
                    setLikes(postData.likes);
                    // image가 null이면 기본 bombImage 사용
                    setImage(postData.image ? postData.image : bombImage);
                    setDate(formatDate(postData.created_at));
                    // console.log("tkwl",postData);
                    // console.log("제목", postData.title);
 
                } else {
                    console.error("게시글을 찾을 수 없습니다.");
                }
            } catch (error) {
                console.error("게시글 데이터를 가져오는 중 오류 발생:", error);
            }
        };

        fetchPost();
    }, [id]);

   
    const handleEditComment = async (post_id) => {
        const inputWriter = prompt("작성자를 입력하세요:", ""); 
        const inputPassword = prompt("비밀번호를 입력하세요:", ""); 

        
        try {
            // 서버에 댓글 삭제 요청
            const response = await axios.delete(`${process.env.REACT_APP_SERVER_URL}blog/comments/${post_id}`, {
                data: {
                    post_id: parseInt(id), // 현재 게시글 ID
                    comment_name: inputWriter, // 댓글 작성자 이름
                    comment_password: inputPassword, // 입력한 비밀번호
                },
            });
            // console.log("dddd",response.data);
            
            if (response.status === 200) {
                // 삭제 성공 시 로컬 상태에서 댓글 삭제
                // 삭제 성공 시 로컬 상태에서 댓글 삭제
                setComments((prevComments) =>
                    prevComments.filter((comment) => 
                        !(comment.writer === inputWriter && comment.id === post_id)
                    )
                );
               
                alert("댓글이 삭제되었습니다.");
            } else {
                alert("비밀번호가 일치하지 않습니다.");
            }
        } catch (error) {
            console.error("댓글 삭제 중 오류 발생:", error);
            alert("댓글 삭제 중 오류가 발생했습니다. 다시 시도해주세요.");
        }
    };
    
    useEffect(() => {
        const handleResize = () => {
            setShowSideCard(window.innerWidth > 1000);
            setIsMobile(window.innerWidth <= 768); // 화면 크기 변경에 따라 모바일 여부 업데이트
        };

        handleResize();
        window.addEventListener("resize", handleResize);
        return () => window.removeEventListener("resize", handleResize);
    }, []);

    useEffect(() => {
        if (!id) {
            console.error("댓글 요청에 필요한 ID가 없습니다.");
            return;
        }
    
        const fetchComments = async () => {
            try {
                const url = `${process.env.REACT_APP_SERVER_URL}blog/comments/${id}`;
                console.log("Fetching comments from:", url);
                const comment = await axios.get(url);
                const mappedComments=comment.data.map(comment => ({
                    id: comment.comment_id,
                    writer: comment.comment_name,
                    content: comment.comment_content,
                }))
                console.log("ddd", mappedComments);
                setComments(mappedComments);
            } catch (error) {
                console.error("댓글 데이터를 가져오는 중 오류 발생:", error);
            }
        };
    
        fetchComments();
    }, [id]);

    
    
    const handleLike = async () => {
        if (isLiked) return;
        try {
            // likes 값 증가
            const updatedLikes = likes + 1;
            setLikes(updatedLikes);
            setIsLiked(true); // 버튼 비활성화
            // 서버에 POST 요청
            await axios.post(`${process.env.REACT_APP_SERVER_URL}blog/${id}/like`, {
                likes: updatedLikes,
            });

            // Recoil 상태 업데이트 및 로컬 스토리지 저장
            setLikeMap((prev) => {
                const updated = { ...prev, [id]: true };
                localStorage.setItem("likes", JSON.stringify(updated)); // 로컬 스토리지에 저장
                return updated;
            });
        } catch (error) {
            console.error("좋아요 업데이트 중 오류 발생:", error);
            // 에러 발생 시 상태값 복구
            setLikes((prevLikes) => prevLikes - 1);
            setIsLiked(false); // 비활성화 상태 복구
        }
    };
    
    return (
        <div
            style={{
                ...styles.container,
                marginLeft: showSideCard ? "45px" : "0", // SideNav가 없으면 marginLeft를 0으로 설정
            }}
        >
            {/* SideCard는 showSideCard가 true일 때만 렌더링 */}
            {showSideCard && <SideCard />}
    
            {/* 게시글 박스 UI */}
            <div
                style={{
                    ...styles.post,
                    flex: showSideCard ? "2.5" : "3.5",
                    fontSize: isMobile ? "0.5rem" : "1rem", // 모바일 환경에서는 폰트 크기 축소
                    padding: isMobile ? "15px 15px" : "30px 30px",
                    marginLeft : isMobile ? "25px" : "40px",
                    marginRight : isMobile ? "-20px" : "0px",
                    marginTop : isMobile ? "20px" : "30px",
                }}
            >
                <div style={{ ...styles.postHeader, fontSize: isMobile ? "0.9rem" : "1rem" }}>
                    <img
                        src={profileImage}
                        alt=""
                        style={{
                            ...styles.profileImage,
                            width: isMobile ? "40px" : "60px",
                            height: isMobile ? "40px" : "60px",
                            marginBottom: isMobile ? "0px" : "20px",
                        }}
                    />
                    <div style={{...styles.authorInfo}}>
                        <p style={{...styles.authorName, fontSize: isMobile ? "0.8rem" : "1rem"}}>Eddy</p>
                        <p style={{...styles.postDate, fontSize: isMobile ? "0.6rem" : "0.8rem"}}>{date}</p>
                    </div>
                </div>
                <div style={styles.title}>{titles}</div>
                <div style={{...styles.Imagecontainer, marginTop : isMobile ? "0px" : "20px"}}>
                    <img src={image} alt="Character Scene" style={{...styles.image, width: isMobile ? "80%" : "50%"}} />
                </div>
    
                <div style={{ ...styles.contentbox, marginTop: isMobile ? "5px" : "20px" }}>
                    {post ? (
                        <ReactMarkdown style={{ ...styles.content, fontSize: isMobile ? "0.9rem" : "1.1rem" }}>
                            {post.content}
                        </ReactMarkdown>
                    ) : (
                        <div
                            style={{
                                ...styles.content,
                                fontSize: isMobile ? "0.9rem" : "1.1rem",
                                color: "#888",
                            }}
                        >
                            <Loading />
                        </div>
                       
                    )}
                    <button style={{ ...styles.button, backgroundColor: isLiked ? "#F0CAC9" : "#FFE8E7"}} onClick={handleLike} disabled={isLiked}>
                        <div style={styles.buttonContent}>
                            <img src={hearticon} alt="heart icon" style={{...styles.icon}} />
                            <p style={styles.text}>{likes}</p>
                        </div>
                    </button>
                </div>
    
                <div style={{...styles.commentHeader, gap: isMobile ? "0px" : "5px"}}>
                    <img src={comment} alt="comment icon" style=
                   {{...styles.commentword, 
                    width: isMobile ? "15px" : "25px",
                    height: isMobile ? "15px" : "25px",
                   
                   }} />
                    <p style={{...styles.commentHeaderText, 
                        fontSize : isMobile ? "1.2rem" : "1.5rem",
                        marginBottom : isMobile ? "25px" : "35px"}}>comment</p>
                </div>
                <div style={styles.contentLine}></div>
    
                <CommentList comments={comments} onDelete={handleEditComment} />
             
                <div style={{...styles.writerHeader, gap : isMobile ? "0px" : "5px"}}>
                    <img src={commentwrite} alt="comment icon" style={{...styles.writerword,
                        width : isMobile ? "20px" : "25px",
                        height : isMobile ? "20px" : "25px"
                    }} />
                    <p style={{...styles.writerHeaderText,
                        fontSize : isMobile ? "1.2rem" : "1.5rem",
                        marginLeft : isMobile ? "5px" : "10px",
                    }}>write</p>
                </div>
                <CommentForm
                    postId={id}
                    onCommentAdded={(newComment) => {
                        console.log("New Comment:", newComment); // 반환 데이터 확인
                        setComments((prev) => [...prev, newComment]);
                    }}
                />


            </div>
        </div>
    );
}    


const styles = {
    container: {
        display: "flex",
        marginLeft: "45px",
        marginRight: "45px",
   
        minHeight: "100vh",
    },
    sideCard: {
        width: "25%",
    },
    post: {
        backgroundColor: "#fffdf7",
        borderRadius: "10px",
        boxShadow: "0 4px 8px rgba(0, 0, 0, 0.1)",
        overflow: "auto",
        marginBottom: "30px"
    },
    profileImage: {
        display: "flex",
        width: "60px",
        height: "60px",
        borderRadius: "10%",
        objectFit: "cover",
        marginBottom: "20px",
    },
    authorInfo: {
        flex: "1",
        marginTop: "-20px",
        marginLeft: "10px",
    },
    title: {
        fontSize: "1.3rem",
        fontWeight: "500"
    },
    authorName: {
       
        fontWeight: "bold",
        marginBottom: "0px",
    },
    postHeader: {
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
        marginBottom: "20px",
    },
    postDate: {
        fontSize: "0.8rem",
        color: "#888",
    },
    ImageContainer: {
        marginTop: "20px",
    },
    image: {
        display: "flex",
        
        width: "60%"
    },
    contentbox: {
        display: "flex",
        flexDirection: "column",
        alignItems: "flex-start",
        marginTop: "20px",
        width: "95%",
        minHeight: "100px",
    },
    content: {
        fontSize: "1.2rem",
        wordWrap: "break-word",
        width: "95%",
    },
    button: {
        boxSizing: "border-box", // 수정: "box-sizing"의 오타 수정
        width: "80px",
        height: "40px",
        background: "#FFE8E7",
        border: "1px solid #FFF2F1",
        boxShadow: "0px 4px 4px rgba(0, 0, 0, 0.25)",
        borderRadius: "15px",
        cursor: "pointer", // 추가: 버튼 클릭 가능 커서
    },
    buttonContent: {
        display: "flex",
        alignItems: "center",
        gap: "5px",
    },
    icon: {
        width: "25px",
        height: "25px",
    },
    text: {
        fontSize: "1rem",
        color: "#000",
        margin: 0,
    },
    commentword: {
        width: "25px",
        height: "25px",
        marginLeft: "5px",
    },
    commentHeader: {
        display: "flex",
        alignItems: "center",
        marginBottom: "-15px",
        marginTop: "20px",
        gap: "5px",
    },
    commentHeaderText: {
        fontSize: "1.5rem",
        color: "#F1D1A3",
        marginLeft: "10px",
    },
    writerword: {
        width: "25px",
        height: "25px",
        marginLeft: "5px",
        marginBottom: '-5px',
    },
    writerHeader: {
        display: "flex",
        alignItems: "center",
        marginBottom: "-30px",
        marginTop: "-5px",
       
        gap: "5px",
    },
    writerHeaderText: {
        fontSize: "1.5rem",
        color: "#F1D1A3",
        marginLeft: "10px",
     
    },
    contentLine: {
        height: "1px",
        backgroundColor: "#F1D1A3",
    },
};

export default Write;