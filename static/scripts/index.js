/*
const foodCardTemplate = document.querySelector("[data-food-template]")
const foodCardContainer = document.querySelector("[data-food-cards-container]")
const searchInput = document.querySelector("[data-search]")

let foods = []

searchInput.addEventListener("input", e => {
  const value = e.target.value.toLowerCase()
  foods.forEach(food => {
    const isVisible =
      food.name.toLowerCase().includes(value) ||
      food.intro.toLowerCase().includes(value)
    food.element.classList.toggle("hide", !isVisible)
  })
})

fetch("/static/scripts/foods.json")
  .then(res => res.json())
  .then(data => {
    foods = data.map(food => {
      const card = foodCardTemplate.content.cloneNode(true).children[0]
      const header = card.querySelector("[data-header]")
      const body = card.querySelector("[data-body]")
      header.textContent = food.name
      body.textContent = food.intro
      foodCardContainer.append(card)
      return { name: food.name, intro: food.intro, element: card }
    })
  })
*/

const initApp = () => {
    const searchBar = document.getElementById("searchBar");
    const datalist = document.getElementById("food");
    const showSearchBarButton = document.getElementById("showSearchBar");

    searchBar.addEventListener("change", function() {
      const selectedValue = searchBar.value.trim();
      let isMatch = false;

  // Check if the selected value matches any option in the datalist
  for (const option of datalist.options) {
    if (option.value === selectedValue) {
      isMatch = true;
      break;
    }
  }

  if (isMatch) {
    // Redirect to the corresponding page based on the selected value
    const redirectUrl = `/${selectedValue.toLowerCase()}`; // Assuming URLs are lowercase
    window.location.href = redirectUrl;
  } else {
    // Handle case where selection doesn't match any option (optional)
    // You can display an error message or clear the search bar here
    console.warn("Selected value does not match any option in the datalist");
  }
});

// Optional: Handle click on the show search bar button (assuming it reveals the search bar)
showSearchBarButton.addEventListener("click", function() {
  // Implement logic to show/hide the search bar
  // You can use CSS classes or other methods to control visibility
});



    const hamburgerBtn = document.getElementById("hamburger-button");
    const mobileMenu = document.getElementById("mobile-menu");
    const messageSubmit = document.getElementById("messageSubmit");
    const textName = document.getElementById("name");
    const textEmail = document.getElementById("email");
    const textMessage = document.getElementById("message");

    const toggleMenu = () => {
        mobileMenu.classList.toggle('hidden')
        mobileMenu.classList.toggle('flex')
        hamburgerBtn.classList.toggle('toggle-btn')
    }

    // Mock Message System
    const submitAMessage = () => {
        if (textName.value && textMessage.value && textEmail.value) {
            alert('Thank you for your message!');
        }
        else {
            alert('Please Enter the Required fields');
        }
    }

    hamburgerBtn.addEventListener('click', toggleMenu)
    mobileMenu.addEventListener('click', toggleMenu)
    messageSubmit.addEventListener('click', submitAMessage);
}

document.addEventListener('DOMContentLoaded', initApp);

