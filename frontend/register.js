document.getElementById("registerForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const email = document.getElementById("registerEmail").value;
  const password = document.getElementById("registerPassword").value;
  const confirm = document.getElementById("registerConfirm").value;

  if (password !== confirm) {
    alert("Les mots de passe ne correspondent pas ");
    return;
  }

  const res = await fetch("http://localhost:8000/signup", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ email, password })
  });

  const data = await res.json();

  if (res.ok) {
    alert("Compte créé avec succès ");
    // window.location.href = "login.html";
  } else {
    alert("Erreur lors de l’inscription ");
    console.log(data);
  }
});
