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
        scales: {
            y: {
                reverse: true, // Y축 역순 설정
                ticks: {
                    stepSize: 1, // 간격 설정
                    callback: function (value) {
                        return value; // 레이블 그대로 표시
                    },
                    font: {
                        size: 10, // 폰트 크기 조정
                    },
                },
                title: {
                    display: true,
                    text: "순위",
                    rotation: 90, // 레이블 가로로 설정
                    font: {
                        size: 12,
                        weight: "bold",
                    },
                },
            },
        },
    };

    return <Line data={data} options={options} />;
};

export default LineChart;
