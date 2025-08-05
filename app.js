let prompts = [];

async function loadPrompts() {
  const res = await fetch('prompts/combined_prompts.json');
  prompts = await res.json();
  renderPrompts(prompts);
}

function renderPrompts(data) {
  const container = document.getElementById('promptContainer');
  container.innerHTML = '';
  data.forEach((item) => {
    const card = document.createElement('div');
    card.className = 'prompt-card';
    card.innerHTML = `
      <h3>${item.task}</h3>
      <p><strong>Prompt:</strong> ${item.prompt}</p>
      <p><strong>Expected Output:</strong> ${item.expected_output}</p>
    `;
    container.appendChild(card);
  });
}

document.getElementById('search').addEventListener('input', (e) => {
  const keyword = e.target.value.toLowerCase();
  const filtered = prompts.filter(p =>
    p.prompt.toLowerCase().includes(keyword) ||
    p.expected_output.toLowerCase().includes(keyword)
  );
  renderPrompts(filtered);
});

document.getElementById('taskFilter').addEventListener('change', (e) => {
  const task = e.target.value;
  const filtered = task === 'all' ? prompts : prompts.filter(p => p.task === task);
  renderPrompts(filtered);
});

loadPrompts();
