function sendData() {
  const baseUrl = window.location;

  const newsText = document.getElementById("newsText");

  // Check if the news text null or empty
  if (newsText.value === null || newsText.value === "") {
    alert("Please enter news text");

    return;
  }

  algorithm = ["svm", "knn", "bayes"];
  algorithm.forEach((alg) => {
    const result = `
          <div class="d-flex mt-5 justify-content-center">
            <div class="spinner-border text-primary" role="status">
              <span class="visually-hidden">Loading...</span>
            </div>
          </div>
        `;

    document.getElementById(`${alg}-result`).innerHTML = result;
  });

  const type = {
    method: "POST", // *GET, POST, PUT, DELETE, etc.
    credentials: "same-origin", // include, *same-origin, omit
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ news: newsText.value }), // body data type must match "Content-Type" header
  };

  algorithm.forEach((alg) => {
    const url = new URL(`${alg}`, baseUrl).href;

    fetch(url, type)
      .then((res) => res.json())
      .then((data) => {
        console.log(data);

        const result = `
          <h4>${data.time}</h4>
          <h5>${data.result}</h5>
        `;

        document.getElementById(`${alg}-result`).innerHTML = result;
      })
      .catch((_) => {
        console.error("Error: happend");

        alert(`${alg} failed`);
      });
  });
}

function uploadFile() {
  const file = document.getElementById("newsFile").files[0];

  if (file.name.split(".").pop() !== "txt") {
    alert("File must be a .txt file");

    return;
  }

  const reader = new FileReader();
  reader.addEventListener("load", (event) => {
    const content = event.target.result;

    const newsText = document.getElementById("newsText");

    newsText.value = content;
  });

  reader.readAsText(file);
}
