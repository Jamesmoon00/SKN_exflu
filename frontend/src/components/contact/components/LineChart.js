// components/LineChart.js
import React from "react";
import { Line } from "react-chartjs-2";

const LineChart = ({ data }) => {
    const options = {
        responsive: true,
        maintainAspectRatio: false, 
        plugins: {
            title: {
                display: true,
                text: "네이버 뱅킹 변화 그래프",
                font: {
                    size: 10,
                    weight: "bold",
                },
                padding: { top: 10, bottom: 20 },
            },
            legend: { position: "bottom" },
        },
    };

    return <Line data={data} options={options} />;
};

export default LineChart;
