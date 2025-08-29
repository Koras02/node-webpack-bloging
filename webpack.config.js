const path = require("path");

module.exports = {
  entry: "./src/index.js", // 브라우저 시작점
  output: {
    filename: "bundle.js", // Bundle JS
    path: path.resolve(__dirname, "dist"), // 웹팩 결과물 위치 저장
  },
  mode: "development",
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/, // node_modules는 제외
        use: {
          loader: "babel-loader",
          options: {
            presets: ["@babel/preset-env"],
          },
        },
      },
    ],
  },
};
