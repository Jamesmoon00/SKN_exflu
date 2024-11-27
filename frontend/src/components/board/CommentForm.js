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
            marginTop: "20px",
            border: "1px solid #FFF2F1",
            borderRadius: "15px",
            backgroundColor: "#FBE5A2",
            justifyContent: "center",
            alignItems: "flex-end",
            width: "100px",
            height: "45px",
            boxShadow: "0 4px 8px rgba(0, 0, 0, 0.1)",
        },
        buttontext: {
            textAlign: "center",
            color: "white",
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
            <button onClick={onSubmit} style={styles.submitButton}>
                <p style={styles.buttontext}>등록</p>
            </button>
        </div>
    );
};

export default CommentForm;
