import React, { Component } from 'react';
import '../scss/app.scss';
import Header from './header.js';
import Map from './map.js';
import SearchForm from './search-form';
import SearchResults from './search-results.js';
import superagent from 'superagent';

class App extends Component {

  constructor(props) {
    super(props);
    this.state = {
      location: null,
      forecasts: []
    }
  }
  handleSearch = async query => {

    this.setState({
      location : null,
      forecasts : [],
      movies : [],
      events : [],
      reviews : [],
      trails : []
    });

    const url = 'https://jb-flask-hello-world.onrender.com';

    const locationData = await superagent.get(`${url}/location?data=${query}`);

    const location = {
      search_query : locationData.body.search_query,
      formatted_query : locationData.body.formatted_query,
      latitude : locationData.body.latitude,
      longitude : locationData.body.longitude,
    }

    const queryString = `data[formatted_query]=${location.formatted_query}&data[latitude]=${location.latitude}&data[longitude]=${location.longitude}&data[search_query]=${location.search_query}`;
    
    const forecasts = await superagent.get(`${url}/weather?${queryString}`);

    const movies = await superagent.get(`${url}/movies?${queryString}`);

    const reviews = await superagent.get(`${url}/yelp?${queryString}`);

    const trails = await superagent.get(`${url}/trails?${queryString}`);

    const events =  await superagent.get(`${url}/events?${queryString}`);

    this.setState({
      location, 
      forecasts : forecasts.body, 
      movies : movies.body,
      events : events.body,
      reviews : reviews.body,
      trails : trails.body

     });
  }
  
  render() {
    return (
      <>
        <Header/>
        <SearchForm handleSearch={this.handleSearch} />
        {this.state.location &&
          <>
            <Map latitude={this.state.location.latitude} longitude={this.state.location.longitude} />
            <SearchResults 
              forecasts={this.state.forecasts} 
              movies={this.state.movies}
              reviews={this.state.reviews}
              events={this.state.events}
              trails={this.state.trails}
            />
          </>
        }
      </>
    );
  }
}

export default App;
