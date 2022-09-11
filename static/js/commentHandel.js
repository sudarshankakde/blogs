
window.document.getElementById('body_content').querySelectorAll('img').forEach((e)=>{
    e.classList.add('img-fluid');
})

const copyButtonLabel = "Copy Code";

// you can use a class selector instead if you, or the syntax highlighting library adds one to the 'pre'. 
let blocks = document.querySelectorAll("pre");

blocks.forEach((block) => {
  // only add button if browser supports Clipboard API
  if (navigator.clipboard) {
    let button = document.createElement("button");
    button.classList.add('button-copy');
    button.innerText = copyButtonLabel;
    button.addEventListener("click", copyCode);
    block.appendChild(button);
  }
});

async function copyCode(event) {
  const button = event.srcElement;
  const pre = button.parentElement;
  let code = pre.querySelector("code");
  let text = code.innerText;
  await navigator.clipboard.writeText(text);

  button.innerText = "Code Copied!";

  setTimeout(()=> {
    button.innerText = copyButtonLabel;
  },3000)
}