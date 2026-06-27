import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage = { role: "user", content: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setLoading(true);

    try {
      const response = await axios.post("http://localhost:8000/ask", {
        question: input,
      });
      const aiMessage = {
        role: "assistant",
        content: response.data.answer,
        sources: response.data.sources,
      };
      setMessages((prev) => [...prev, aiMessage]);
    } catch (error) {
      console.error(error);
      setMessages((prev) => [
        ...prev,
        { role: "assistant", content: "Error: could not reach the server." },
      ]);
    }
    setLoading(false);
  };

  const handleKeyPress = (e) => {
    if (e.key === "Enter") sendMessage();
  };

  return (
    <div className="app">
      <h1>🌱 Moderta AI Assistant</h1>
      <div className="chat-window">
        {messages.map((msg, i) => (
          <div key={i} className={`message ${msg.role}`}>
            <strong>{msg.role === "user" ? "You" : "Assistant"}:</strong>
            <p>{msg.content}</p>
            {msg.sources && msg.sources.length > 0 && (
              <small>Sources: {msg.sources.join(", ")}</small>
            )}
          </div>
        ))}
        {loading && <p>Thinking...</p>}
      </div>
      <div className="input-row">
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={handleKeyPress}
          placeholder="Ask about Moderta..."
        />
        <button onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
}

export default App;