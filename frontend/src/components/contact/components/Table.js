import React from "react";

const TableComponent = ({ data }) => {
    const styles = {
        tableBox: {
            display: "flex",
            flex: "4",
            border: "2px solid #F5E4AE",
            borderRadius: "20px",
            padding: "10px",
            backgroundColor: "#fffdf7",
            boxShadow: "0 4px 8px rgba(0, 0, 0, 0.1)",
            width: "30%",
            marginTop: "-20px",
        },
        table: {
            borderCollapse: "collapse",
            width: "100%",
        },
        tableHeader: {
            fontFamily: "'Lexend Deca', sans-serif",
            fontWeight: "bold",
            textAlign: "left",
        },
        tableRow: {
            textAlign: "left",
            padding: "15px 10px",
           
        },
        tableCell: {
            padding: "15px 20px",
        },
    };

    return (

        <table style={styles.table}>
            <thead>
                <tr style={styles.tableHeader}>
                    <th style={styles.tableCell}>No</th>
                    <th style={styles.tableCell}>컨텐츠</th>
                    <th style={styles.tableCell}>좋아요</th>
                    <th style={styles.tableCell}>댓글 수</th>
                </tr>
            </thead>
            <tbody>
                {data.map((row, index) => (
                    <tr key={index} style={styles.tableRow}>
                        <td style={styles.tableCell}>{row.no}</td>
                        <td style={styles.tableCell}>{row.content}</td>
                        <td style={styles.tableCell}>{row.likes}</td>
                        <td style={styles.tableCell}>{row.comments}</td>
                    </tr>
                ))}
            </tbody>
        </table>
      
    );
};

export default TableComponent;
