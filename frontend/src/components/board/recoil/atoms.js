import { atom } from "recoil";

// 좋아요 상태 Atom
export const likeState = atom({
  key: "likeState", // Atom의 고유한 키
  default: JSON.parse(localStorage.getItem("likes")) || {}, // 로컬 스토리지에서 초기 상태 로드
});
