import "./App.css";
import React, { useState, useEffect } from "react";
import BlogItemList from "./BlogList";
// import Card from "react-bootstrap/Card";
import axios from "axios";

function App() {
  const [tag, setTag] = useState("");

  const [BlogList, setBlogs] = useState();

  useEffect(() => {
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
      {/* <h5>You can search blogs by tag</h5> */}
      {/* <CardTemplate /> */}
      <br/>
  
      <BlogItemList blogList={BlogList} />
    </div>
  );
}

export default App;



// function SearchBlogByTag() {
//   const [tag, setTag] = useState("");
//   function handleSearch(e) {
//     e.preventDefault();
//     const res = fetch("http://127.0.0.1:8000/tag/" + String(tag));
//     const data = res.json;
//     console.log(data);
//     return data.map((blog, index) => (
//       <div key={index}>
//         <h2>{blog.name}</h2>
//         <h3>{blog.date}</h3>
//         <h3>{blog.title}</h3>
//         <h3>{blog.short_description}</h3>
//         <h3>{blog.response}</h3>
//         <h3>{blog.read_time}</h3>
//       </div>
//     ));

//   }

//   return (
//     <form onSubmit={handleSearch}>
//       <input
//         type="text"
//         name="tag"
//         value={tag}
//         onChange={(e) => setTag(e.target.value)}
//       />
//       <button>Search</button>
//     </form>
//   );
// }

// function FinalBlogList(){
//   return BlogList.map((blog, index) => (
//     <div key={index}>
//       <h2>{blog.name}</h2>
//       {/* <h3>{blog.date}</h3>
//       <h3>{blog.title}</h3>
//       <h3>{blog.short_description}</h3>
//       <h3>{blog.response}</h3>
//       <h3>{blog.read_time}</h3> */}
//     </div>
//   ));
// }
