import React from "react";

const CommentForm = ({ writer, password, content, onWriterChange, onPasswordChange, onContentChange, onSubmit }) => {
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

    return (
        <div style={styles.commentForm}>
            <input
                type="text"
                placeholder="  작성자"
                value={writer}
                onChange={onWriterChange}
                style={styles.input}
            />
            <input
                type="text"
                placeholder="  비밀번호"
                value={password}
                onChange={onPasswordChange}
                style={styles.input}
            />
            <input
                type="text"
                placeholder="  댓글 내용을 입력하세요"
                value={content}
                onChange={onContentChange}
                style={styles.textarea}
            />

            <button onClick={onSubmit} type="submit" style={styles.submitButton}>
                등록
            </button>
     
            
        </div>
    );
};

export default CommentForm;
