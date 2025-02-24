fetch("https://mempool.space/api/mempool")
  .then(response => response.json())
  .then(data => {
    console.log(`Current Mempool Transactions: ${data.count}`);
    console.log(`Total Mempool Size: ${data.vsize} vBytes`);
  })
  .catch(error => console.error("Error fetching mempool data:", error));
