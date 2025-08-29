const express = require("express");
const path = require("path");

require("dotenv").config();

const app = express();
const PORT = process.env.SERVER_PORT;

// 정적 파일 세팅
app.use("/dist", express.static(path.join(__dirname, "../dist")));

app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "../index.html"));
});

app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
