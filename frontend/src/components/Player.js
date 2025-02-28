import React from 'react';
import './Player.css';

const Player = ({ src }) => {
    return (
        <div className="player">
            <audio controls src={src} />
        </div>
    );
};

export default Player;
