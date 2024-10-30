document.getElementById("summarize-btn").addEventListener("click", () => {
    chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
      chrome.scripting.executeScript({
        target: { tabId: tabs[0].id },
        func: extractEmailContent
      }, (results) => {
        const emailContent = results[0].result;
        chrome.runtime.sendMessage({ content: emailContent }, (response) => {
          document.getElementById("summary").textContent = response.summary;
        });
      });
    });
  });
  
  // Function to extract email body content
  function extractEmailContent() {
    return document.querySelector("div[role='main']").innerText;  // Modify selector if needed
  }
  