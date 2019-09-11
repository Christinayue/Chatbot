import React, { Component } from "react";
//import Button from "@material-ui/core/Button";
//import jQuery from 'jquery';
import Grid from "@material-ui/core/Grid";
import Paper from "@material-ui/core/Paper";
import axios from "axios";
import "./chatbot.css"
import { List } from "@material-ui/core";

class Dashboard extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      name: '',
      result: null,
    }
  }
  /**
   * Get weather data using api key from apixu.com
   * using given dataMode and city
   * @param {*} dataMode can be current and forecast
   * @param {*} city
   */

  handleChange = event => {
    this.setState({ name: event.target.value });
  }

  handleSubmit = event => {
    event.preventDefault();
    const user = {
      name: this.state.name
    };
    axios.post(`http://0.0.0.0:5001/v1/ask/` + user.name, { headers: { 'accept': 'application/json' } })
      .then(res => {
        console.log(res.data.length);
        //console.log(res.data);
        const result = res.data;
        //this.setState(result);
        //console.log(result);
        this.setState({ result: result.valueOf() });
      })
    /*axios.post(`http://0.0.0.0:5001/v1/ask/` + user.name, { headers: { 'accept': 'application/json' } })
      .then(res => {
        console.log(res.data.length);
        //console.log(res.data);
        const result = res.data[0];
        console.log(result);
        this.setState({ result: result });


      })*/
  }
  render() {
    var sen = ""
    var datalist = []
    //console.log(this.state.result)
    if (this.state.result != null) {
      if (typeof (this.state.result) == String) {
        sen = "";
        datalist = [];
      }
      else if (this.state.result[0] != null && this.state.result[0]['id'] != null) {
        //console.log(this.state.result)
        sen = ""
        for (var a in this.state.result) {
          //console.log(this.state.result[a])
          datalist.push(this.state.result[a]);
        }
      }
      else {
        sen = this.state.result;
        datalist = []
      }
    }
    else {
      sen = ""
      datalist = []
    }
    var List = [];
    const p = sen.split(" ");
    for (var a in p) {
      List.push(p[a]);
    }
    ;


    return (
      <div className="display" >
        <Grid container justify="center" alignItems="center">
          <Grid item>
            <h2>Chatbot</h2>
            <form className="Form" onSubmit={this.handleSubmit}>

              <label className="FormLabel">
                message:
              <input className="FormInput" type="text" name="name" onChange={this.handleChange} />
              </label>
              <button className="Button" type="submit">Add</button>
            </form>
          </Grid>
          <Grid item className="Response">
            <Paper >
              <div > <p>Chatbot:</p>{sen}





              </div>
              <div>
                <ul>
                  {
                    datalist.map(function (username) {
                      return <li>timeslotid:{username['id']},  timeslot status: {username['status']},  time: {username['time']}</li>
                    })
                  }
                </ul>
              </div>

            </Paper>

          </Grid>

        </Grid>



      </div >


    )
  }
}
export default Dashboard;


