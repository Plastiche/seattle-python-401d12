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
      forecasts: [],
      movies: [],
      events: [],
      reviews: [],
      trails: [],
    }
  }

  async getApiData(baseUrl, location, resourceName) {

    const queryString = `data[formatted_query]=${location.formatted_query}&data[latitude]=${location.latitude}&data[longitude]=${location.longitude}&data[search_query]=${location.search_query}`;

    const fullUrl = `${baseUrl}/${resourceName}?${queryString}`;

    const response = await superagent.get(fullUrl);

    return response.body

  }
  handleSearch = async query => {
    
    const url = 'https://jb-flask-hello-world.onrender.com';

    const locationData = await superagent.get(`${url}/location?data=${query}`);

    const location = {
      search_query : locationData.body.search_query,
      formatted_query : locationData.body.formatted_query,
      latitude : locationData.body.latitude,
      longitude : locationData.body.longitude,
    }

    const forecasts = await this.getApiData(url, location, 'weather');
    const movies = await this.getApiData(url, location, 'movies');
    const events = await this.getApiData(url, location, 'events');
    const trails = await this.getApiData(url, location, 'trails');
    const reviews = await this.getApiData(url, location, 'yelp');

    this.setState({
      location,
      forecasts,
      movies,
      events,
      trails,
      reviews,
    })
  }
  
  render() {
    return (
      <>
        <Header />
        <SearchForm handleSearch={this.handleSearch} />
        {this.state.location && (
          <>
            <Map latitude={this.state.location.latitude} longitude={this.state.location.longitude} />
            <SearchResults 
              forecasts={this.state.forecasts} 
              movies={this.state.movies} 
              events={this.state.events} 
              reviews={this.state.reviews} 
              trails={this.state.trails} 
            />
          </>
        )}
        
      </>
    );
  }
}

export default App;
