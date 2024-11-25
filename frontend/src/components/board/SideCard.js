import React, {useState} from "react";
import profileImage from "../../assets/img/eddy_blog.png";

const SideCard = () => {
    return (
        <div style={styles.sidebar}>
                <img src={profileImage} alt="Profile" style={styles.profileImage} />
                <h2 style={styles.blogTitle}>Eddy's Blog</h2>
                <p style={styles.description}>Welcome to my blog!</p>
        </div>
    )
}

const styles = {
    sidebar: {
        marginTop: "30px",
        backgroundColor: "#fffdf7",
        borderRadius: "10px",
        padding: "40px",
        boxShadow: "0 4px 8px rgba(0, 0, 0, 0.1)",
        textAlign: "center",
        marginBottom: "30px"
    },
    profileImage: {
        width: "250px",
        height: "250px",
        borderRadius: "50%",
        objectFit: "cover",
        marginBottom: "15px",
    },
    blogTitle: {
        fontSize: "1.5rem",
        fontWeight: "bold",
        marginBottom: "10px",
    },
    description: {
        fontSize: "0.9rem",
        color: "#555",
    },
}

export default SideCard