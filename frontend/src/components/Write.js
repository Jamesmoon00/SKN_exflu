import React, {useState} from "react"
import profileImage from "../assets/img/eddy_profile.png";
import bombImage from "../assets/img/bomb_eddy.png";
import hearticon from "../assets/icons/heart.png";
import comment from "../assets/icons/comment.png";
const Write = () => {
    const [comments, setComments] = useState([]); // 댓글 리스트 상태
    const [writer, setWriter] = useState(""); // 작성자 입력 상태
    const [content, setContent] = useState(""); // 댓글 내용 입력 상태

    // 댓글 추가 핸들러
    const handleAddComment = () => {
        if (!writer || !content) {
            alert("작성자와 내용을 입력해주세요!");
            return;
        }
        const newComment = {
            id: comments.length + 1,
            writer,
            content,
        };
        setComments([...comments, newComment]);
        setWriter("");
        setContent("");
    };
    return (
        <div style={styles.container}>
            <div style={styles.post}>
                <div style={styles.postHeader}>
                    <img src={profileImage} alt="" style={styles.profileImage} />
                    <div style={styles.authorInfo}>
                        <p style={styles.authorName}>Eddy</p>
                        <p style={styles.postDate}>2024-11-15</p>
                    </div>
                </div>

                <div style={styles.Imagecontainer}>
                    <img src={bombImage} alt="Character Scene" style={styles.image} />

                </div>

                <div style={styles.contentbox}>
                    <p style={styles.content}>오늘 뽀로로🐧한테 골탕먹이려다가 폭탄맞음;;;;;</p>
                    <button style={styles.button}>
                        <div style={styles.buttonContent}>
                            <img src={hearticon} alt="heart icon" style={styles.icon} />
                            <p style={styles.text}>100</p>
                        </div>
                    </button>
                </div>

                <div style={styles.commentHeader}>
                        <img src={comment} alt="comment icon" style={styles.commentword} />
                        <p style={styles.commentHeaderText}>comment</p> 
                        
                </div>
                <div style={styles.contentLine}></div>
                
                {/* 댓글 리스트 */}
                <div>
                    {comments.map((comment) => (
                        <div key={comment.id} style={styles.commentItem}>
                            <p>
                                <strong>{comment.writer}</strong>: {comment.content}
                            </p>
                        </div>
                    ))}
                </div>

                {/* 댓글 작성 폼 */}
                <div style={styles.commentForm}>
                    
                    <input
                            type="text"
                            placeholder="작성자"
                            value={writer}
                            onChange={(e) => setWriter(e.target.value)}
                            style={styles.input}
                    />
                    <input
                            type="text"
                            placeholder="댓글 내용을 입력하세요"
                            value={content}
                            onChange={(e) => setContent(e.target.value)}
                            style={styles.textarea} 
                    />
                    

                </div>
                <div style={styles.commnetaddButton}>
                    <button onClick={handleAddComment} style={styles.submitButton}>
                        <p style={styles.buttontext}>등록</p>
                    </button>
                </div>
                
                
            </div>
        </div>
    );
}
const styles = {
    container: {
        alignItems: "center",
        display: "flex",
        flexDirection: "column", // 세로 방향 정렬
        // marginLeft: "30px",
        // marginRight: "30px",
        backgroundColor: "#fffaea",
        minHeight: "100vh",
        width: "100%",
        flex: 1,
        filter: `
            0px 2px 15px rgba(212, 165, 98, 0.9), 
            0px 4px 30px rgba(212, 165, 98, 0.7)
        `,
        overflow: "auto"
       
    },
    post: {
        width: "90%",
        marginTop: "30px",
        flex: 3,
        backgroundColor: "#fffdf7",
        borderRadius: "10px",
        padding: "30px 30px 30px",
        boxShadow:  `
        0px 2px 15px rgba(212, 165, 98, 0.3), 
        0px 4px 30px rgba(212, 165, 98, 0.2)
        `,
        // textAlign: "left",
        marginBottom: "30px",
        overflow: "auto"
    },

    profileImage: {
        width: "60px",
        height: "60px",
        borderRadius: "10%",
        objectFit: "cover",
        marginBottom: "20px",
    },
    authorInfo: {
        flex: "1",
        marginTop:"-20px",
        marginLeft: "10px",
    },
    authorName: {
        fontSize: "1rem",
        fontWeight: "bold",
        marginBottom: "0px"
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
        marginTop: "20px"
    },
    image: {
        
        // marginTop: "20px",
        boxShadow: `
        0px 2px 15px rgba(212, 165, 98, 0.2), 
        0px 4px 30px rgba(212, 165, 98, 0.1)
        `,
        
    },
    contentbox: {
        display: "flex",
        flexDirection: "column", // 세로 방향 정렬
        alignItems: "flex-start", // 좌측 정렬
        marginTop: "20px", // 상단 여백
        height: "100px",
     
    },
    content: {
        fontSize: "1.2rem",
        wordWrap: "break-word",
    },
    button: {
        display: "flex",
        alignItems: "center", // 세로 가운데 정렬
        justifyContent: "center", // 가로 정렬
        padding: "5px 10px", // 버튼 내부 여백
        border: "1px solid #FFF2F1", // 버튼 테두리
        borderRadius: "10px", // 둥근 버튼
        backgroundColor: "#FFF2F1", // 버튼 배경색
        cursor: "pointer",
        transition: "all 0.3s ease-in-out", // 부드러운 전환
        filter: "drop-shadow(0px 4px 6px rgba(0, 0, 0, 0.2))",
       
    },
    buttonContent: {
        display: "flex",
        alignItems: "center", // 아이콘과 텍스트를 세로 가운데 정렬
        gap: "5px", // 아이콘과 텍스트 간격
    },
    icon: {
        width: "40px", // 아이콘 너비
        height: "40px", // 아이콘 높이
    },
    text: {
        fontSize: "1.5rem", // 텍스트 크기
       
        color: "#000", // 텍스트 색상
        margin: 0, // 기본 여백 제거
    },

    
    
    
    commentword: {
        width: "25px",
        height: "25px",
        marginLeft: "5px"
        
    },
    commentHeader: {
        display: "flex",
        alignItems: "center",
        marginBottom: "-15px",
        marginTop: '50px',
        gap: "5px",
       
    },
    commentHeaderText: {
        fontSize: "1.5rem",
     
        color: "#F1D1A3",
        marginLeft: "10px"
    },
    contentLine: {
        height: "1px",
        backgroundColor: "#F1D1A3",
       
    },

    commentForm: {
        justifyContent: "center",
        alignItems: "center",
        textAlign: "center",
        marginTop: "30px"
      
    },

    input: {
        width: "1300px",
        height: "38px",
        marginBottom: "20px",
        borderRadius: "10px"
    },
    textarea: {
        width: "1300px",
        height: "100px",
        borderRadius: "10px"
    },
    commnetaddButton: {
        justifyContent: "center",
        alignItems: "center",
        textAlign: "center",
    },
    submitButton: {
        marginTop: "20px",
        border: "1px solid #FFF2F1", // 버튼 테두리
        borderRadius: "10px", // 둥근 버튼
        backgroundColor: "#FBE5A2", // 버튼 배경색
        justifyContent: "center", // 가로 중앙 정렬
        alignItems: "flex-end", // 세로 중앙 정렬
        width:"100px",
        height: "45x",

       
        
       
    },
    buttontext: {
        text: "1.4rem",
        textAlign: "center",
        color: "white"
       
    }
    
    
    
    
    
}
export default Write;