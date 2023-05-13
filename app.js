const express = require("express");
const body_parser = require("body-parser");

const app = express();
app.use('view-engine', 'ejs');


app.get("/", (req, resp)=>{
    let today = new Date();

    let options ={
        weekday: "long",
        day: "numeric",
        month: "long"
    };
    var day = today.toLocaleDateString("en-US", options);

    res.render("list", {kindOfDay: day});

});



app.listen(3000, ()=>{console.log("Server Started")});
