async function getRate() {
  const from = document.getElementById('from').value;
  const to = document.getElementById('to').value;
  const url = `https://api.apilayer.com/exchangerates_data/convert?from=${from}&to=${to}&amount=1`;

  try {
    const response = await fetch(url, {
      method: "GET",
      headers: {
        "apikey": "1vjRDhBAvR8DKY4fWNL1DCH9WMpH4lZt"
      }
    });

    const data = await response.json();

    if (data.success) {
      document.getElementById('result').innerText =
        `1 ${from} = ${data.result.toFixed(2)} ${to}`;
    } else {
      document.getElementById('result').innerText =
        'Помилка: ' + (data.error?.info || 'Невідома помилка');
    }
  } catch (error) {
    console.error(error);
    document.getElementById('result').innerText = 'Помилка з’єднання з API';
  }
}
