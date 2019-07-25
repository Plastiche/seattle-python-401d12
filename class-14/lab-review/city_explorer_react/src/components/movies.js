import React from 'react';

export default props => (
    <div>
        <h2>Movies</h2>
        <ul>
            {props.data.map(movie => (
                <li key={movie.image_url}>{movie.title}</li>
            ))}
        </ul>
    </div>
)