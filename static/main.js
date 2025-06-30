/*--------------------------------------------header----------------------------------------------------------------*/
/*-----popupbox---------*/
// Get popup elements
const popupBox = document.getElementById('popupBox');
const closeBtn = document.getElementById('closeBtn');
const popupTitle = document.getElementById('popupTitle');
const popupForm = document.getElementById('popupForm');
const extraText = document.getElementById('extraText');

// Ensure popup is hidden on page load
if (popupBox) {
  popupBox.style.display = 'none'; // Explicitly hide popup to prevent auto-display
}

// Only run this if the "Login" button exists
const openPopupBtn = document.querySelector('.Login');
if (openPopupBtn) {
  openPopupBtn.onclick = function () {
    popupBox.style.display = 'flex';
    showLoginForm(); // Open login form when button is clicked
  };
}

// Close popup when clicking the ×
if (closeBtn) {
  closeBtn.onclick = function () {
    popupBox.style.display = 'none';
  };
}

// Close popup when clicking outside
window.onclick = function (event) {
  if (event.target == popupBox) {
    popupBox.style.display = 'none';
  }
};

// Show Login form
function showLoginForm() {
  popupTitle.textContent = 'Login';
  popupForm.innerHTML = `
    <input type="email" placeholder="Email ID" required><br>
    <input type="password" placeholder="Password" required><br>
    <button type="submit" class="submit-btn">Login</button>
  `;
  extraText.innerHTML = `Don't have an account? <a href="#" id="switchToRegister">Register here</a>`;
  addSwitchListeners();
}

// Show Register form
function showRegisterForm() {
  popupTitle.textContent = 'Create Your HealthMate Account';
  popupForm.innerHTML = `
    <input type="text" placeholder="Full Name" required><br>
    <input type="email" placeholder="Email ID" required><br>
    <input type="password" placeholder="Password" required><br>
    <input type="password" placeholder="Confirm Password" required><br>
    <button type="submit" class="submit-btn">Register</button>
  `;
  extraText.innerHTML = `Already have an account? <a href="#" id="switchToLogin">Login here</a>`;
  addSwitchListeners();
}

// Toggle between login/register
function addSwitchListeners() {
  const switchToRegister = document.getElementById('switchToRegister');
  const switchToLogin = document.getElementById('switchToLogin');

  if (switchToRegister) {
    switchToRegister.onclick = function (e) {
      e.preventDefault();
      showRegisterForm();
    };
  }

  if (switchToLogin) {
    switchToLogin.onclick = function (e) {
      e.preventDefault();
      showLoginForm();
    };
  }
}



/*--------------------------------------------------about us page-------------------------------------------------------------*/

/*-------aboutUsSlider--------*/
const slides = document.querySelectorAll('.slide');

let currentSlide = 0;
const totalSlides = slides.length;

function showNextSlide() {
  slides[currentSlide].classList.remove('active');

  currentSlide++;
  if (currentSlide >= totalSlides) {
    currentSlide = 0; // Loop back
  }

  slides[currentSlide].classList.add('active');
}

// Auto-slide every 2 seconds (2000 milliseconds)
setInterval(showNextSlide, 2000);


/*-------how it works-------*/
const slider = document.getElementById('stepsSlider');
let scrollAmount = 0;
const stepSpeed = 1; // Move 1px at a time for smooth effect
const resetPoint = slider.scrollWidth / 2; // Half the total width (if duplicated steps)

function autoSlide() {
  scrollAmount += stepSpeed; // Move by 1px
  if (scrollAmount >= resetPoint) {
    scrollAmount = 0; // Reset to beginning
  }
  slider.style.transform = `translateX(-${scrollAmount}px)`;
}

// Move every 10 milliseconds for continuous motion
setInterval(autoSlide, 10);

/------------------------------------------------------------diabeties page-------------------------------------------/
function toggleDropdown(id) {
    const element = document.getElementById(id);
    const isVisible = element.style.display === 'block';
  
    // Hide all others
    document.querySelectorAll('.dropdown-text').forEach(div => {
      div.style.display = 'none';
    });
  
    // Reset all icons
    document.querySelectorAll('.dropdown-icon').forEach(icon => {
      icon.style.transform = 'rotate(0deg)';
    });
  
    // Toggle clicked one
    if (!isVisible) {
      element.style.display = 'block';
      const icon = element.previousElementSibling.querySelector('.dropdown-icon');
      if (icon) icon.style.transform = 'rotate(180deg)';
    }
  }

/*------------------------------------------------------------vitality monitor page-------------------------------------------*/

/*------------------- prediction form handling -------------------*/
const predictForm = document.getElementById("predictForm");

if (predictForm) {
  predictForm.addEventListener("submit", function (e) {
    e.preventDefault();

    const name = document.getElementById("name").value;
    const age = document.getElementById("age").value;
    const month = document.getElementById("month").value;

    console.log(name, age, month); // ✅ Debugging line

    // Send data to server
    fetch("/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ name: name, age: age, month: month }), // Send the form data
    })
      .then((response) => response.json())
      .then((data) => {
        // Handle the prediction result
        document.getElementById("result").innerText =
          "Prediction result: " + data.message;
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  });
}
