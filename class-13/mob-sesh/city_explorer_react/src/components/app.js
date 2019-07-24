import React from 'react';
import Header from './header.js';
import SearchForm from './search-form.js';
import SearchResults from './search-results.js';
import Map from './map.js';

class App extends React.Component {
  
  constructor(props) {
    super(props);
    this.state = {
      // Mock data
      location: {
        "search_query": "barcelona",
        "formatted_query": "Barcelona, Spain",
        "latitude": 41.3850639,
        "longitude": 2.1734035
        },
        yelp_result_data: []
    };
  }

  searchEntered = query => {
    // use that query to hit API
  }

  render() {
    return (
      <>
        <Header />
        <SearchForm handleSubmit={this.searchEntered}  />
        <Map />
        <SearchResults />
      </>
    );
  }
}

export default App;
