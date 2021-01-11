import "./App.css";
import React, { useState, useEffect } from "react";
import BlogItemList from "./BlogList";
import axios from "axios";
import { colors } from "@material-ui/core";
// import { w3cwebsocket as W3CWebSocket } from "websocket";
// const client = new W3CWebSocket('ws://127.0.0.1:8001/users');

function App() {
  
  const [tag, setTag] = useState("");
  const [BlogList, setBlogs] = useState();

  useEffect(() => {
    // client.onopen = () => {
    //   console.log('WebSocket Client Connected');
    // };
    // client.onmessage = (message) => {
    //   console.log(message);
    // };

    FetchBlogs();
  }, []);

  async function FetchBlogs() {
    try {
      const res = await axios.get("http://127.0.0.1:8000/tag/blog");
      // await fetch("http://127.0.0.1:8000/tag/blog");

      const data = res.data;
      setBlogs(data);
    } catch (error) {
      console.error(error);
    }
  }

  async function handleSearch(e) {
    e.preventDefault();
    // const res = await axios.post("http://127.0.0.1:8000/api/crawl/",{url: String(tag)});
    const res = await axios.get("http://127.0.0.1:8000/tag/" + String(tag));
    const data = res.data;
    setBlogs(data);
    console.log(data);
  }

  return (
    <div className="App">
      <h1>Medium.com </h1>
      <form onSubmit={handleSearch}>
        <input
          type="text"
          name="tag"
          value={tag}
          onChange={(e) => setTag(e.target.value)}
        />
        <button>Search</button>
      </form>
      <br />

      <BlogItemList blogList={BlogList} />
    </div>
  );
}

export default App;
