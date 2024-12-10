import React, {useState, useEffect} from "react";



const CommentList = ({ comments, onDelete }) => {
    
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
    const [isMobile, setIsMobile] = useState(window.innerWidth <= 768); 
    useEffect(() => {
        const handleResize = () => {
            
            setIsMobile(window.innerWidth <= 768); // 화면 크기 변경에 따라 모바일 여부 업데이트
        };

        handleResize();
        window.addEventListener("resize", handleResize);
        return () => window.removeEventListener("resize", handleResize);
    }, []);
    return (
        <div>
            {comments.map((comment) => (
                <div key={comment.id} style={{...styles.commentItem,
                    padding : isMobile ? "14px 10px" : "17px 30px"
                }}>
                    <div style={styles.commentText}>
                        <strong>{comment.writer}</strong>
                        <p style={styles.commentContent}>{comment.content}</p>
                    </div>
                    <button
                        style={styles.editButton}
                        onClick={() => onDelete(comment.id, comment.writer, comment.password)}
                    >
                        삭제 하기
                    </button>
                </div>
            ))}
        </div>
    );
};

export default CommentList;
