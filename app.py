from flask import Flask
app = Flask(__name__)

HTML = """
<!doctype html>
<html lang='es'>
<head>
  <meta charset='utf-8'>
  <meta name='viewport' content='width=device-width, initial-scale=1'>
  <title>Proyecto Final IRIC</title>
  <style>
    :root{
      --bg1:#0b2237; /* azul oscuro */
      --bg2:#3a5fe4; /* azul brillante */
      --card:#ffffff;
      --accent:#00d1b2; /* verde-azulado */
    }
    html,body{height:100%;margin:0}
    body{
      font-family:system-ui,-apple-system,Segoe UI,Roboto,Ubuntu,"Helvetica Neue",Arial;
      background: linear-gradient(135deg, var(--bg1), var(--bg2));
      display:flex; align-items:center; justify-content:center;
      color:#111;
    }
    .card{
      background:var(--card);
      width:min(780px, 92vw);
      border-radius:20px;
      box-shadow:0 10px 30px rgba(0,0,0,.25);
      padding:28px 32px;
      text-align:center;
    }
    .pill{
      display:inline-block;
      padding:.35rem .8rem;
      border-radius:999px;
      background:rgba(58,95,228,.12);
      color:#3a5fe4;
      font-weight:600;
      letter-spacing:.5px;
      margin-bottom:8px;
    }
    h1{
      font-size:56px;
      margin:.2rem 0 .6rem;
      letter-spacing:1px;
      color:#0b2237;
    }
    h1 .accent{ color: var(--accent); }
    p{ margin:.25rem 0; font-size:18px; }
    .footer{
      margin-top:16px; font-size:14px; color:#666;
    }
    .btn{
      margin-top:16px;
      display:inline-block;
      text-decoration:none;
      padding:.7rem 1.1rem;
      border-radius:12px;
      border:1px solid rgba(0,0,0,.08);
      background:#f7f9fc;
      transition:transform .08s ease, box-shadow .2s ease;
    }
    .btn:hover{ transform:translateY(-1px); box-shadow:0 6px 16px rgba(0,0,0,.10); }
  </style>
</head>
<body>
  <main class="card" role="main" aria-label="Tarjeta principal de examen">
    <span class="pill">Proyecto Final IRIC</span>
    <h1><span class="accent">EXAMEN</span></h1>
    <p><strong>Materia:</strong> DevOps</p>
    <p><strong>Profesor:</strong> NOMBRE_PROFESOR</p>
    <p><strong>Alumno:</strong> TU_NOMBRE</p>
    <a class="btn" href="/">Refrescar</a>
    <div class="footer">Flask + Docker + CI/CD</div>
  </main>
</body>
</html>
"""

@app.route("/")
def home():
    return HTML

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
