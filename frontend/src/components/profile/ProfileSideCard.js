import React from "react";
import profileImage from "../../assets/img/dailyEddy2.png";

const ProfileSideCard = () => {
    return (
        <div style={styles.sidebar}>
                <img src={profileImage} alt="Profile" style={styles.profileImage} />
                <h2 style={styles.blogTitle}>Eddy</h2>
                <p style={styles.description}>친구들! 나에 대해서 소개할께!😛😛</p>
        </div>
    )
}

const styles = {
    sidebar: {
        marginTop: "30px",
        marginBottom: "30px",
        borderRadius: "10px",
        padding: "40px",
        boxShadow: "0px 4px 4px rgba(0, 0, 0, 0.1)",
        background: "linear-gradient(180deg, #FFEFB8 0%, #FFFDF7 85%)",
        textAlign: "center",
        // borderRight: "2px solid #F1D1A3"
    
      
    },
    profileImage: {
        width: "250px",
        height: "250px",
   
        objectFit: "cover",
        marginBottom: "15px",
        // marginTop:"50px",
        borderRadius: "100%"
    },
    blogTitle: {
        fontSize: "1.5rem",
        fontWeight: "bold",
        marginBottom: "10px",
        color: "#3F201F",
    },
    description: {
        fontSize: "0.9rem",
        color: "#555",
    },
}

export default ProfileSideCard;