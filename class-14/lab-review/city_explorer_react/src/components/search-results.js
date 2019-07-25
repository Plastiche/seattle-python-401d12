import React from 'react';
import Trails from './trails.js'
import Events from './events.js'
import Movies from './movies.js'
import Forecasts from './forecasts.js'
import Reviews from './reviews.js'

export default props => (
    <>
        <Forecasts data={props.forecasts} />
        <Events data={props.events} />
        <Reviews data={props.reviews} />
        <Movies data={props.movies} />
        <Trails data={props.trails} />
    </>
)