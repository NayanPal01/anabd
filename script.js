function navigateTo(page) {
  window.location.href = page;
}

function createStars() {
  const stars = document.getElementById('stars');
  for (let i = 0; i < 100; i++) {
      const star = document.createElement('div');
      star.className = 'star';
      star.style.left = `${Math.random() * 100}vw`;
      star.style.animationDuration = `${Math.random() * 3 + 2}s`;
      stars.appendChild(star);
  }
}

document.addEventListener('DOMContentLoaded', createStars);
