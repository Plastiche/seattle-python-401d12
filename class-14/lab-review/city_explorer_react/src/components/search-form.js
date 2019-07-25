import React, { Component } from 'react';

export default class SearchForm extends Component {

    constructor(props) {
        super(props);
        this.state = {
            query: ''
        }
    }

    handleInput = event => {
        this.setState({
            query : event.target.value
        });
    }

    handleSubmit = event => {
        event.preventDefault()
        this.props.handleSearch(this.state.query);
    }

    render() {
        return (
            <form onSubmit={this.handleSubmit}>
                <input value={this.state.query} onChange={this.handleInput} />
                <button>search</button>
            </form>
        )
    }
}