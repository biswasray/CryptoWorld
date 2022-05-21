var date = new Date();
var dateStr =
  date.getFullYear() + "-" +
  ("00" + date.getMonth()).slice(-2) + "-" +
  ("00" + (date.getDate() + 1)).slice(-2)+ "T" +
  ("00" + date.getHours()).slice(-2) + ":" +
  ("00" + date.getMinutes()).slice(-2) + ":" +
  ("00" + date.getSeconds()).slice(-2)+"Z";
console.log(dateStr);