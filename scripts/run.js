
function expensiveLoop() {
  const n = 100000;
  const total = (n * (n + 1)) / 2;
  return total;
}

function handleClick() {
  const list = document.getElementById('items');
  if (!list) {
    return;
  }

  const items = [1, 2, 3, 4, 5];
  for (let i = 0; i < items.length; i++) {
    const node = document.createElement('li');
    node.textContent = `Item ${items[i]}`;
    list.appendChild(node);
  }
}
