db = db.getSiblingDB('mydatabase'); // Switch to the 'mydatabase' database

db.createCollection('mycollection'); // Create a collection named 'mycollection'

db.mycollection.insertMany([
<<<<<<< HEAD
  { name: "Alice", age: 30},
  { name: "Bob", age: 25},
  { name: "Charlie", age: 35}
=======
  { name: "Alice", age: 30 },
  { name: "Bob", age: 25 },
  { name: "Charlie", age: 35 }
>>>>>>> MODULE_AI
]);