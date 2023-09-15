document.querySelector("#postForm").addEventListener("submit", (e) => {
  e.preventDefault();
  const title = document.getElementById("title");
  const content = document.getElementById("content");
  const author = document.getElementById("author");
  console.log(title.value);
  console.log(content.value);
  console.log(author.value);
  createPost(title.value, content.value, author.value);
});


const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;


function createPost(title, content, author) {
  const data = {
    method: "POST",
    headers: {
      "content-type": "application/json",
      "X-CSRFToken": csrftoken, // Aggiungi il token CSRF all'intestazione
    },
    body: JSON.stringify({
      title,
      content,
      author,
    }),
  };
  fetch("/api/posts/create/", data)
    .then((res) => res.json)
    .then((data) => {
      console.log(data);
    })
    .catch((err) => console.log(err));
}

function fetchPostList() {
  fetch("/api/posts")
    .then((res) => res.json())
    .then((data) => {
      renderPosts(data);
    })
    .catch((err) => {
      console.log(err);
    });
}

function renderPosts(data) {
  data.map((post) => {
    renderPost(post);
  });
}

function createNode(element) {
  return document.createElement(element);
}

function append(parent, el) {
  parent.appendChild(el);
}

function renderPost(post) {
  const root = document.getElementById("root");
  const div = createNode("div");
  div.className = "post-item";
  const title = createNode("h2");
  const content = createNode("p");
  // const publishDate = createNode("span");
  // const lastUpdated = createNode("span");
  const br = createNode("br");
  const author = createNode("small");

  author.innerText = `  Written by ${post.author}`;
  title.innerText = post.title;
  append(title, author);

  content.innerText = post.content;
  // publishDate.innerText = `Published: ${new Date(
  //   post.publish_date
  // ).toUTCString()}`;

  // lastUpdated.innerText = `Last updated: ${new Date(
  //   post.updated
  // ).toUTCString()}`;

  append(div, title);
  append(div, content);
  // append(div, publishDate);
  append(div, br);
  // append(div, lastUpdated);
  append(root, div);
}

fetchPostList();
