var items = [1, 2, 3, 4, 5];

function handleClick() {
  var list = document.getElementById('items');
  if (!list) {
    return;
  }

  for (var i = 0; i < items.length; i++) {
    var node = document.createElement('li');
    node.textContent = 'Item ' + items[i];
    list.appendChild(node);
  }
}

function expensiveLoop() {
  var total = 0;
  for (var i = 0; i < 100000; i++) {
    total = total + i;
  }
  return total;
}
