import React from 'react';

export default props => (
    <div>
        <h2>Reviews</h2>
        <ul>
            {props.data.map(review => (
                <li key={review.image_url}>{review.name}</li>
            ))}
        </ul>
    </div>
)