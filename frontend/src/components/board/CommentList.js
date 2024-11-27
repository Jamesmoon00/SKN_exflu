import React, {useState} from "react";



const CommentList = ({ comments, onEdit }) => {
    const styles = {
        commentItem: {
            display: "flex",
            alignItems: "flex-start", // 세로 정렬
            justifyContent: "space-between", // 좌우 배치
            padding: "17px 30px", // 상하 여백
            borderBottom: "1px solid #F1D1A3", // 하단 경계선
            fontSize: "1rem",
            color: "#000", // 텍스트 색상
        },
        commentText: {
            display: "flex",
            flexDirection: "column", // 세로 배치
            flex: 1, // 댓글 내용의 가로 확장
            marginRight: "10px", // 오른쪽 간격
        },
        commentContent: {
            margin: "5px 0 0 0", // 위쪽 여백 추가
            fontSize: "0.9rem",
            color: "#333", // 댓글 내용 색상
        },
        editButton: {
            backgroundColor: "#FBE5A2", // 버튼 배경색
            border: "none", // 테두리 제거
            borderRadius: "10px", // 버튼 둥글기
            padding: "10px 13px", // 버튼 내부 여백
            cursor: "pointer",
            fontSize: "0.9rem",
            color: "#000", // 텍스트 색상
            transition: "background-color 0.3s ease", // 배경색 전환 효과
            boxShadow: "0 4px 8px rgba(0, 0, 0, 0.1)",
            textAlign: "center",
        },
    };

    return (
        <div>
            {comments.map((comment) => (
                <div key={comment.id} style={styles.commentItem}>
                    <div style={styles.commentText}>
                        <strong>{comment.writer}</strong>
                        <p style={styles.commentContent}>{comment.content}</p>
                    </div>
                    <button
                        style={styles.editButton}
                        onClick={() => onEdit(comment.id, comment.writer, comment.password)}
                    >
                        삭제 하기
                    </button>
                </div>
            ))}
        </div>
    );
};

export default CommentList;
