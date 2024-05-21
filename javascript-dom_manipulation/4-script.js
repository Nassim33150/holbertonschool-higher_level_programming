document.addEventListener('DOMContentLoaded', () => {
  const addItem = document.querySelector('#add_item');
  const itemList = document.querySelector('.my_list');

  addItem.addEventListener('click', () => {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    itemList.appendChild(newItem);
  });
});
