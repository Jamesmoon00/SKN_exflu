import React from "react"
import profileImage from "../assets/img/eddy_profile.png";
const Write = () => {
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
                <p>dd</p>
            </div>
        </div>
    );
}
const styles = {
    container: {
        display: "flex",
        marginLeft: "30px",
        backgroundColor: "#fffaea",
        height: "100vh",
        flex: 1
    },
    post: {
        marginTop: "30px",
        flex: 3,
        backgroundColor: "#fffdf7",
        borderRadius: "10px",
        padding: "20px",
        boxShadow: "0 4px 8px rgba(0, 0, 0, 0.1)",
        textAlign: "left",
        marginBottom: "30px"
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
}
export default Write;