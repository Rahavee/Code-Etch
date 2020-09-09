const btn = document.querySelector("#gay");

btn.addEventListener("click", runMyShittyPythonScript);


function runMyShittyPythonScript() {
fetch("http://localhost:5000/run")
.then(response => response.json())
.then(json => console.log(json.status))
}
