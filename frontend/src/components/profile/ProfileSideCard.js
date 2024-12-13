import React, {useState} from "react";
import profileImage from "../../assets/img/eddy.png";

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
       
        borderRadius: "10px",
        padding: "40px",
       
        textAlign: "center",
      
    },
    profileImage: {
        width: "250px",
        height: "auto",
   
        objectFit: "cover",
        marginBottom: "15px",
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