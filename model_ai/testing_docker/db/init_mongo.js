db = db.getSiblingDB('mydatabase'); // Switch to the 'mydatabase' database

db.createCollection('mycollection'); // Create a collection named 'mycollection'

db.mycollection.insertMany([
  { name: "mongo data" },
]);