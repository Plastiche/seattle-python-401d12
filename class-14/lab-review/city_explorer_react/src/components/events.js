import React from 'react';

export default props => (
    <div>
        <h2>Events</h2>
        <ul>
            {props.data.map(event => (
                <li key={event.link}>{event.name}</li>
            ))}
        </ul>
    </div>
)