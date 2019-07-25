import React from 'react';

export default props => (
    <div>
        <h2>Forecasts</h2>
        <ul>
            {props.data.map(forecast => (
                <li key={forecast.time}>{forecast.forecast}</li>
            ))}
        </ul>
    </div>
)