import React from "react";
import { useLocation } from "react-router-dom";
import YesPage from "./YesPage.js"
import NoPage from "./NoPage.js"
const YesorNo = () => {
    const location = useLocation(); // 현재 URL 정보 가져오기
    const queryParams = new URLSearchParams(location.search); // 쿼리 문자열 파싱
    const response = queryParams.get("response"); // response 값 읽기

    return (
        <div>
            {response === "yes" ? (
                <YesPage />
            ) : (
                <NoPage />
            )}
        </div>
    );
};



export default YesorNo
