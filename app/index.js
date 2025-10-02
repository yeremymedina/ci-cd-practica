const express = require("express");
const app = express();
const port = process.env.PORT || 3000;

app.get("/", (_req, res) => {
  res.send("¡Hola desde CI/CD!");
});

app.listen(port, () => {
  console.log(`App escuchando en http://localhost:${port}`);
});
