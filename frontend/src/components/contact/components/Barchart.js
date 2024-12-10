// components/BarChart.js
import React from "react";
import { Bar } from "react-chartjs-2";

const BarChart = ({ data }) => {
    const options = {
        responsive: true,
        maintainAspectRatio: false, 
        plugins: {
            title: {
                display: true,
                text: "실제 인플루언서와 단가 비교",
                font: {
                    size: 10,
                    weight: "bold",
                },
                padding: { top: 10, bottom: 20 },
            },
            legend: { position: "bottom" },
        },
    };

    return <Bar data={data} options={options} />;
};

export default BarChart;
