import React, { useState } from "react";
import axios from "axios";
import { useParams } from "react-router-dom"; // useParams import 추가

const CommentForm = ({ onCommentAdded }) => {
    const { id } = useParams(); // URL에서 게시글 ID 가져오기
    const [writer, setWriter] = useState("");
    const [password, setPassword] = useState("");
    const [content, setContent] = useState("");

    const styles = {
        commentForm: {
            display: "flex",
            flexDirection: "column",
            justifyContent: "center",
            alignItems: "center",
            textAlign: "center",
            marginTop: "30px",
            width: "100%",
        },
        input: {
            width: "95%",
            maxWidth: "1300px",
            height: "40px",
            marginBottom: "10px",
            borderRadius: "10px",
            border: "1px solid #FFFAEA",
        },
        textarea: {
            width: "95%",
            maxWidth: "1300px",
            height: "100px",
            borderRadius: "10px",
            border: "1px solid #FFFAEA",
        },

        submitButton: {
            marginTop: "30px",
            boxSizing: "border-box", // 수정: "box-sizing"의 오타 수정
            width: "80px",
            height: "40px",
            background: "#FBE5A2",
            border: "1px solid #F5E4AE",
            boxShadow: "0px 4px 4px rgba(0, 0, 0, 0.25)",
            borderRadius: "15px",
            cursor: "pointer", // 추가: 버튼 클릭 가능 커서
    
            
        },

    };

    const handleSubmit = async () => {
       
        if (!writer || !content) {
            alert("작성자와 내용을 입력해주세요!");
            return;
        }
    
        try {
            const response = await axios.post(
                `${process.env.REACT_APP_SERVER_URL}blog/comments`,
                {
                    post_id: Number(id), // 현재 게시글 ID
                    comment_name: writer,
                    comment_password: password,
                    comment_content: content,
                },
                {
                    headers: {
                        "Content-Type": "application/json",
                    },
                }
            );
    
            if (response.status === 200) {
                
                alert("댓글이 등록되었습니다!");
                onCommentAdded({
                    id: response.data.comment_id, // 서버에서 생성된 댓글 ID
                    writer: writer,
                    content: content,
                });
                setWriter("");
                setPassword("");
                setContent("");
                
            }
        } catch (error) {
            console.error("댓글 등록 중 오류 발생:", error);
            alert("댓글 등록에 실패했습니다.");
        }
    };
    
    return (
        <div style={styles.commentForm}>
            <input
                type="text"
                placeholder="  작성자"
                value={writer}
                onChange={(e) => setWriter(e.target.value)}
                style={styles.input}
            />
            <input
                type="text"
                placeholder="  비밀번호"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                style={styles.input}
            />
            <input
                type="text"
                placeholder="  댓글 내용을 입력하세요"
                value={content}
                onChange={(e) => setContent(e.target.value)}
                style={styles.textarea}
            />

            <button onClick={handleSubmit} type="submit" style={styles.submitButton}>
                등록
            </button>
     
            
        </div>
    );
};

export default CommentForm;
