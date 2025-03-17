const data = [
    {
      title: "HTML Basics",
      category: "relevance",
      date: "2023-10-01",
      tags: ["HTML", "Beginner"]
    },
    {
      title: "CSS Flexbox Guide",
      category: "relevance",
      date: "2023-11-15",
      tags: ["CSS", "Flexbox"]
    },
    {
      title: "Latest Web Design Trends",
      category: "date",
      date: "2024-01-20",
      tags: ["Trends", "Design"]
    },
    {
      title: "JavaScript Async Patterns",
      category: "relevance",
      date: "2023-12-05",
      tags: ["JavaScript", "Async"]
    },
    {
      title: "2024 Web Dev Updates",
      category: "date",
      date: "2024-02-01",
      tags: ["Trends", "JavaScript"]
    }
  ];
  
  const searchInput = document.getElementById("searchInput");
  const categoryFilter = document.getElementById("categoryFilter");
  const resultsContainer = document.getElementById("resultsContainer");
  const suggestionsBox = document.getElementById("suggestions");
  
  // Extract keywords for autocomplete (titles + tags)
  const keywordSet = new Set();
  data.forEach(item => {
    keywordSet.add(item.title);
    item.tags.forEach(tag => keywordSet.add(tag));
  });
  const keywords = Array.from(keywordSet);
  
  // Filter and display
  function filterResults(query = "", category = "all") {
    const q = query.toLowerCase();
  
    const filtered = data.filter(item => {
      const matchesCategory = category === "all" || item.category === category;
      const matchesSearch =
        item.title.toLowerCase().includes(q) ||
        item.tags.some(tag => tag.toLowerCase().includes(q));
  
      return matchesCategory && matchesSearch;
    });
  
    displayResults(filtered);
  }
  
  function displayResults(results) {
    resultsContainer.innerHTML = "";
  
    if (results.length === 0) {
      resultsContainer.innerHTML = "<p>No results found.</p>";
      return;
    }
  
    results.forEach(item => {
      const div = document.createElement("div");
      div.classList.add("result-item");
      div.innerHTML = `
        <strong>${item.title}</strong><br>
        Category: ${item.category} | Date: ${item.date}
        <div class="tags">
          ${item.tags.map(tag => `<span class="tag" data-tag="${tag}">${tag}</span>`).join('')}
        </div>
      `;
      resultsContainer.appendChild(div);
    });
  
    // Add click events to tags
    document.querySelectorAll(".tag").forEach(tagEl => {
      tagEl.addEventListener("click", () => {
        searchInput.value = tagEl.dataset.tag;
        filterResults(tagEl.dataset.tag, categoryFilter.value);
      });
    });
  }
  
  // Autocomplete
  searchInput.addEventListener("input", () => {
    const value = searchInput.value.toLowerCase();
    suggestionsBox.innerHTML = "";
  
    if (value.length < 1) return;
  
    const matched = keywords.filter(k => k.toLowerCase().includes(value));
    matched.slice(0, 5).forEach(s => {
      const item = document.createElement("div");
      item.className = "suggestion-item";
      item.textContent = s;
      item.addEventListener("click", () => {
        searchInput.value = s;
        suggestionsBox.innerHTML = "";
        filterResults(s, categoryFilter.value);
      });
      suggestionsBox.appendChild(item);
    });
  });
  
  // Hide suggestions on blur
  searchInput.addEventListener("blur", () => {
    setTimeout(() => suggestionsBox.innerHTML = "", 200);
  });
  
  categoryFilter.addEventListener("change", () => {
    filterResults(searchInput.value, categoryFilter.value);
  });
  
  // Initial load
  filterResults();
  