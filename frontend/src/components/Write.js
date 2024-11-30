import React, { useState, useEffect } from "react";
import profileImage from "../assets/img/eddy_profile.png";
import bombImage from "../assets/img/bomb_eddy.png";
import hearticon from "../assets/icons/heart.png";
import comment from "../assets/icons/comment.png";
import commentwrite from "../assets/icons/write.png";
import SideCard from "./board/SideCard";
import Comment from "./board/CommentList";
import CommentForm from "./board/CommentForm";

const Write = () => {
    const [comments, setComments] = useState([]);
    const [writer, setWriter] = useState("");
    const [password, setPassword] = useState("");
    const [content, setContent] = useState("");
    const [showSideCard, setShowSideCard] = useState(true); // SideCard 표시 여부 상태
    const [isMobile, setIsMobile] = useState(window.innerWidth <= 768); // 모바일 여부 상태
    const handleAddComment = () => {
        if (!writer || !content) {
            alert("작성자와 내용을 입력해주세요!");
            return;
        }
        const newComment = {
            id: comments.length + 1,
            writer,
            password,
            content,
        };
        setComments([...comments, newComment]);
        setWriter("");
        setPassword("");
        setContent("");
    };

    const handleEditComment = (id, writer, password) => {
        const newWriter = prompt("작성자를 입력하세요:", ""); 
        const newPassword = prompt("비밀번호를 입력하세요:", ""); 

        if (newWriter === writer && newPassword === password) {
            setComments((prevComments) =>
                prevComments.filter((comment) => comment.id !== id)
            );
            alert("댓글이 삭제되었습니다.");
        } else {
            alert("작성자와 비밀번호가 일치하지 않습니다.");
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
                        <p style={{...styles.postDate, fontSize: isMobile ? "0.6rem" : "0.8rem"}}>2024-11-15</p>
                    </div>
                </div>
    
                <div style={{...styles.Imagecontainer, marginTop : isMobile ? "0px" : "20px"}}>
                    <img src={bombImage} alt="Character Scene" style={{...styles.image, width: isMobile ? "80%" : "60%"}} />
                </div>
    
                <div style={{...styles.contentbox, marginTop: isMobile ? "5px" : "20px"}}>
                    <p style={{...styles.content , fontSize : isMobile ? "0.9rem" : "1.1rem"}}>
                        오늘 뽀로로🐧한테 골탕먹이려다가 폭탄맞음;;;; 뽀로로뽀로로뽀로로뽀로로
                        
                    </p>
                    <button style={styles.button}>
                        <div style={styles.buttonContent}>
                            <img src={hearticon} alt="heart icon" style={styles.icon} />
                            <p style={styles.text}>100</p>
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
    
                <Comment comments={comments} onEdit={handleEditComment} />
    
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
                    writer={writer}
                    password={password}
                    content={content}
                    onWriterChange={(e) => setWriter(e.target.value)}
                    onPasswordChange={(e) => setPassword(e.target.value)}
                    onContentChange={(e) => setContent(e.target.value)}
                    onSubmit={handleAddComment}
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
        backgroundColor: "#fffaea",
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
        boxShadow: `
        0px 2px 15px rgba(212, 165, 98, 0.2), 
        0px 4px 30px rgba(212, 165, 98, 0.1)
        `,
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