chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    fetch("http://127.0.0.1:5000/summarize", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ content: message.content })
    })
      .then(response => response.json())
      .then(data => {
        sendResponse({ summary: data.summary });
      })
      .catch(error => console.error("Error:", error));
  
    return true;  // Keeps the message channel open for async response
  });
  