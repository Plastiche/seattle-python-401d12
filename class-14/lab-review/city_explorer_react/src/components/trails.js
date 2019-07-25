import React from 'react';

export default props => (
    <div>
        <h2>Trails</h2>
        <ul>
            {props.data.map(trail => (
                <li key={trail.trail_url}>{trail.name}</li>
            ))}
        </ul>
    </div>
)