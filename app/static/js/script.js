document.addEventListener("DOMContentLoaded", () => {
  // Auto-hide alerts after 3 seconds
  const alerts = document.querySelectorAll(".alert");
  alerts.forEach(alert => {
    setTimeout(() => {
      alert.classList.remove("show");
      alert.style.opacity = "0";
    }, 3000);
  });

  // Dark Mode toggle
  const toggle = document.getElementById("darkModeToggle");

  function applyDarkMode(isDark) {
    if(isDark) {
      document.body.classList.add("dark-mode");
    } else {
      document.body.classList.remove("dark-mode");
    }
  }

  if (toggle) {
    toggle.addEventListener("click", () => {
      const isDark = !document.body.classList.contains("dark-mode");
      applyDarkMode(isDark);
      localStorage.setItem("darkMode", isDark);
    });

    // Load saved preference
    const savedMode = localStorage.getItem("darkMode");
    applyDarkMode(savedMode === "true");
  }
});


