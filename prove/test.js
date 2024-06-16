const array1 = [1, 2, 3, 4, 5];
const array2 = [
  { Id: 1, name: "asd" },
  { Id: 5, name: "asd" },
  { Id: 7, name: "asd" },
  { Id: 11, name: "asd" },
];

const filteredArray = array2.filter((el) => array1.includes(el.Id));

console.log(filteredArray);
