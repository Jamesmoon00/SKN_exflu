import React from "react";


const NoPage = () => {
    
    return (
        <div style={styles.container}>
            Nopage
        </div>
    );
}

const styles = {
    container: {
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        backgroundColor: "#fffaea",
        height: "100vh",
        boxSizing: "border-box",
        flexDirection: "column",
    },
};

export default NoPage;
