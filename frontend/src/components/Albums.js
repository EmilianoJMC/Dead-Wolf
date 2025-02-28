import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Player from './Player';
import './Albums.css';

const Albums = () => {
    const [albums, setAlbums] = useState([]);

    useEffect(() => {
        axios.get('/api/albums/')
            .then(response => setAlbums(response.data))
            .catch(error => console.error(error));
    }, []);

    return (
        <div className="albums">
            {albums.map(album => (
                <div key={album.id} className="album">
                    <h3>{album.title}</h3>
                    <p>{album.artist}</p>
                    <ul>
                        {album.musicas.map(music => (
                            <li key={music.id}>
                                {music.title}
                                <Player src={music.file_path} />
                            </li>
                        ))}
                    </ul>
                </div>
            ))}
        </div>
    );
};

export default Albums;
