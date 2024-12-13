import React from 'react';

const Loading = () => {
    const loaderStyle = {
        fontSize: '10px',
        width: '1em',
        height: '1em',
        borderRadius: '50%',
        position: 'relative',
        textIndent: '-9999em',
        animation: 'mulShdSpin 1.1s infinite ease',
        transform: 'translateZ(0)',
    };

    return (
        <>
            <style>
                {`
                    @keyframes mulShdSpin {
                        0%,
                        100% {
                            box-shadow: 0em -2.6em 0em 0em #F1D1A3, 1.8em -1.8em 0 0em rgba(241,209,163, 0.2), 2.5em 0em 0 0em rgba(241,209,163, 0.2), 1.75em 1.75em 0 0em rgba(241,209,163, 0.2), 0em 2.5em 0 0em rgba(241,209,163, 0.2), -1.8em 1.8em 0 0em rgba(241,209,163, 0.2), -2.6em 0em 0 0em rgba(241,209,163, 0.5), -1.8em -1.8em 0 0em rgba(241,209,163, 0.7);
                        }
                        12.5% {
                            box-shadow: 0em -2.6em 0em 0em rgba(241,209,163, 0.7), 1.8em -1.8em 0 0em #F1D1A3, 2.5em 0em 0 0em rgba(241,209,163, 0.2), 1.75em 1.75em 0 0em rgba(241,209,163, 0.2), 0em 2.5em 0 0em rgba(241,209,163, 0.2), -1.8em 1.8em 0 0em rgba(241,209,163, 0.2), -2.6em 0em 0 0em rgba(241,209,163, 0.2), -1.8em -1.8em 0 0em rgba(241,209,163, 0.5);
                        }
                        25% {
                            box-shadow: 0em -2.6em 0em 0em rgba(241,209,163, 0.5), 1.8em -1.8em 0 0em rgba(241,209,163, 0.7), 2.5em 0em 0 0em #F1D1A3, 1.75em 1.75em 0 0em rgba(241,209,163, 0.2), 0em 2.5em 0 0em rgba(241,209,163, 0.2), -1.8em 1.8em 0 0em rgba(241,209,163, 0.2), -2.6em 0em 0 0em rgba(241,209,163, 0.2), -1.8em -1.8em 0 0em rgba(241,209,163, 0.2);
                        }
                        37.5% {
                            box-shadow: 0em -2.6em 0em 0em rgba(241,209,163, 0.2), 1.8em -1.8em 0 0em rgba(241,209,163, 0.5), 2.5em 0em 0 0em rgba(241,209,163, 0.7), 1.75em 1.75em 0 0em #F1D1A3, 0em 2.5em 0 0em rgba(241,209,163, 0.2), -1.8em 1.8em 0 0em rgba(241,209,163, 0.2), -2.6em 0em 0 0em rgba(241,209,163, 0.2), -1.8em -1.8em 0 0em rgba(241,209,163, 0.2);
                        }
                        50% {
                            box-shadow: 0em -2.6em 0em 0em rgba(241,209,163, 0.2), 1.8em -1.8em 0 0em rgba(241,209,163, 0.2), 2.5em 0em 0 0em rgba(241,209,163, 0.5), 1.75em 1.75em 0 0em rgba(241,209,163, 0.7), 0em 2.5em 0 0em #F1D1A3, -1.8em 1.8em 0 0em rgba(241,209,163, 0.2), -2.6em 0em 0 0em rgba(241,209,163, 0.2), -1.8em -1.8em 0 0em rgba(241,209,163, 0.2);
                        }
                        62.5% {
                            box-shadow: 0em -2.6em 0em 0em rgba(241,209,163, 0.2), 1.8em -1.8em 0 0em rgba(241,209,163, 0.2), 2.5em 0em 0 0em rgba(241,209,163, 0.2), 1.75em 1.75em 0 0em rgba(241,209,163, 0.5), 0em 2.5em 0 0em rgba(241,209,163, 0.7), -1.8em 1.8em 0 0em #F1D1A3, -2.6em 0em 0 0em rgba(241,209,163, 0.2), -1.8em -1.8em 0 0em rgba(241,209,163, 0.2);
                        }
                        75% {
                            box-shadow: 0em -2.6em 0em 0em rgba(241,209,163, 0.2), 1.8em -1.8em 0 0em rgba(241,209,163, 0.2), 2.5em 0em 0 0em rgba(241,209,163, 0.2), 1.75em 1.75em 0 0em rgba(241,209,163, 0.2), 0em 2.5em 0 0em rgba(241,209,163, 0.5), -1.8em 1.8em 0 0em rgba(241,209,163, 0.7), -2.6em 0em 0 0em #F1D1A3, -1.8em -1.8em 0 0em rgba(241,209,163, 0.2);
                        }
                        87.5% {
                            box-shadow: 0em -2.6em 0em 0em rgba(241,209,163, 0.2), 1.8em -1.8em 0 0em rgba(241,209,163, 0.2), 2.5em 0em 0 0em rgba(241,209,163, 0.2), 1.75em 1.75em 0 0em rgba(241,209,163, 0.2), 0em 2.5em 0 0em rgba(241,209,163, 0.2), -1.8em 1.8em 0 0em rgba(241,209,163, 0.5), -2.6em 0em 0 0em rgba(241,209,163, 0.7), -1.8em -1.8em 0 0em #F1D1A3;
                        }
                    }
                `}
            </style>
            <div style={styles.container}>
                <span style={loaderStyle}></span>
            </div>
            
        </>
    );
};
const styles= {
    container: {
        display: 'flex',
        justifyContent: 'center', // 수평 중앙 정렬
        alignItems: 'center', // 수직 중앙 정렬
        minHeight: '100vh', // 화면 전체 높이
        backgroundColor: '#fffaea',
    },
}
export default Loading;
