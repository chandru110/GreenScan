/**
* Template Name: Valera
* Template URL: https://bootstrapmade.com/valera-free-bootstrap-theme/
* Updated: Aug 07 2024 with Bootstrap v5.3.3
* Author: BootstrapMade.com
* License: https://bootstrapmade.com/license/
*/

(function() {
  "use strict";

  /**
   * Apply .scrolled class to the body as the page is scrolled down
   */
  function toggleScrolled() {
    const selectBody = document.querySelector('body');
    const selectHeader = document.querySelector('#header');
    if (!selectHeader.classList.contains('scroll-up-sticky') && !selectHeader.classList.contains('sticky-top') && !selectHeader.classList.contains('fixed-top')) return;
    window.scrollY > 100 ? selectBody.classList.add('scrolled') : selectBody.classList.remove('scrolled');
  }

  document.addEventListener('scroll', toggleScrolled);
  window.addEventListener('load', toggleScrolled);

  /**
   * Mobile nav toggle
   */
  const mobileNavToggleBtn = document.querySelector('.mobile-nav-toggle');

  function mobileNavToogle() {
    document.querySelector('body').classList.toggle('mobile-nav-active');
    mobileNavToggleBtn.classList.toggle('bi-list');
    mobileNavToggleBtn.classList.toggle('bi-x');
  }
  mobileNavToggleBtn.addEventListener('click', mobileNavToogle);

  /**
   * Hide mobile nav on same-page/hash links
   */
  document.querySelectorAll('#navmenu a').forEach(navmenu => {
    navmenu.addEventListener('click', () => {
      if (document.querySelector('.mobile-nav-active')) {
        mobileNavToogle();
      }
    });

  });

  document.getElementById("consumerBtn").addEventListener("click", function() {
    // Show consumer form and hide retailer form
    document.getElementById("consumerFields").style.display = "block";
    document.getElementById("retailerFields").style.display = "none";
  
    // Change button styles to reflect the active form
    this.classList.add("btn-primary");
    this.classList.remove("btn-secondary");
    document.getElementById("retailerBtn").classList.remove("btn-primary");
    document.getElementById("retailerBtn").classList.add("btn-secondary");
  });
  
  document.getElementById("retailerBtn").addEventListener("click", function() {
    // Show retailer form and hide consumer form
    document.getElementById("consumerFields").style.display = "none";
    document.getElementById("retailerFields").style.display = "block";
  
    // Change button styles to reflect the active form
    this.classList.add("btn-primary");
    this.classList.remove("btn-secondary");
    document.getElementById("consumerBtn").classList.remove("btn-primary");
    document.getElementById("consumerBtn").classList.add("btn-secondary");
  });
  document.getElementById("consumerBtn").addEventListener("click", function() {
    document.getElementById("consumerFields").style.display = "block";
    document.getElementById("retailerFields").style.display = "none";
  
    // Toggle button styles
    this.classList.add("btn-primary");
    this.classList.remove("btn-secondary");
    document.getElementById("retailerBtn").classList.remove("btn-primary");
    document.getElementById("retailerBtn").classList.add("btn-secondary");
  });
  
  document.getElementById("retailerBtn").addEventListener("click", function() {
    document.getElementById("consumerFields").style.display = "none";
    document.getElementById("retailerFields").style.display = "block";
  
    // Toggle button styles
    this.classList.add("btn-primary");
    this.classList.remove("btn-secondary");
    document.getElementById("consumerBtn").classList.remove("btn-primary");
    document.getElementById("consumerBtn").classList.add("btn-secondary");
  });
    
  document.getElementById("feedbackForm").addEventListener("submit", function(event) {
    event.preventDefault();
  
    // Get form values
    const userName = document.getElementById("userName").value;
    const userEmail = document.getElementById("userEmail").value;
    const userFeedback = document.getElementById("userFeedback").value;
  
    // Basic validation
    if (userName && userEmail && userFeedback) {
      // Optional: Handle feedback submission, e.g., send to server
      console.log("Feedback submitted:", { name: userName, email: userEmail, feedback: userFeedback });
  
      // Clear form fields
      document.getElementById("feedbackForm").reset();
  
      // Display a success message
      alert("Thank you for your feedback!");
    } else {
      // Display an error message
      alert("Please fill out all fields before submitting.");
    }
  });
  // Initialize PureCounter if it's being used for the animations
const pureCounter = new PureCounter({
  // Optional configurations, if any
});
// Get both buttons
const consumerBtn = document.getElementById('consumerBtn');
const retailerBtn = document.getElementById('retailerBtn');

// Add event listeners for each button
consumerBtn.addEventListener('click', function() {
    // Make Consumer button orange and Retailer button grey
    consumerBtn.classList.remove('grey-button');
    consumerBtn.classList.add('orange-button');
    retailerBtn.classList.remove('orange-button');
    retailerBtn.classList.add('grey-button');
});

retailerBtn.addEventListener('click', function() {
    // Make Retailer button orange and Consumer button grey
    retailerBtn.classList.remove('grey-button');
    retailerBtn.classList.add('orange-button');
    consumerBtn.classList.remove('orange-button');
    consumerBtn.classList.add('grey-button');
});

document.addEventListener('DOMContentLoaded', function() {
  const form = document.getElementById('contactForm');
  const loading = form.querySelector('.loading');
  const errorMessage = form.querySelector('.error-message');
  const sentMessage = form.querySelector('.sent-message');

  form.addEventListener('submit', function(event) {
    event.preventDefault();

    loading.style.display = 'block';
    errorMessage.style.display = 'none';
    sentMessage.style.display = 'none';

    // Simulate form submission with a timeout
    setTimeout(function() {
      loading.style.display = 'none';
      sentMessage.style.display = 'block';
    }, 2000);
  });
});

  

  /**
   * Toggle mobile nav dropdowns
   */
  document.querySelectorAll('.navmenu .toggle-dropdown').forEach(navmenu => {
    navmenu.addEventListener('click', function(e) {
      e.preventDefault();
      this.parentNode.classList.toggle('active');
      this.parentNode.nextElementSibling.classList.toggle('dropdown-active');
      e.stopImmediatePropagation();
    });
  });

  /**
   * Preloader
   */
  const preloader = document.querySelector('#preloader');
  if (preloader) {
    window.addEventListener('load', () => {
      preloader.remove();
    });
  }

  /**
   * Scroll top button
   */
  let scrollTop = document.querySelector('.scroll-top');

  function toggleScrollTop() {
    if (scrollTop) {
      window.scrollY > 100 ? scrollTop.classList.add('active') : scrollTop.classList.remove('active');
    }
  }
  scrollTop.addEventListener('click', (e) => {
    e.preventDefault();
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });

  window.addEventListener('load', toggleScrollTop);
  document.addEventListener('scroll', toggleScrollTop);

  /**
   * Animation on scroll function and init
   */
  function aosInit() {
    AOS.init({
      duration: 600,
      easing: 'ease-in-out',
      once: true,
      mirror: false
    });
  }
  window.addEventListener('load', aosInit);

  /**
   * Initiate Pure Counter
   */
  new PureCounter();

  /**
   * Init swiper sliders
   */
  function initSwiper() {
    document.querySelectorAll(".init-swiper").forEach(function(swiperElement) {
      let config = JSON.parse(
        swiperElement.querySelector(".swiper-config").innerHTML.trim()
      );

      if (swiperElement.classList.contains("swiper-tab")) {
        initSwiperWithCustomPagination(swiperElement, config);
      } else {
        new Swiper(swiperElement, config);
      }
    });
  }

  window.addEventListener("load", initSwiper);

  /**
   * Initiate glightbox
   */
  const glightbox = GLightbox({
    selector: '.glightbox'
  });

  /**
   * Init isotope layout and filters
   */
  document.querySelectorAll('.isotope-layout').forEach(function(isotopeItem) {
    let layout = isotopeItem.getAttribute('data-layout') ?? 'masonry';
    let filter = isotopeItem.getAttribute('data-default-filter') ?? '*';
    let sort = isotopeItem.getAttribute('data-sort') ?? 'original-order';

    let initIsotope;
    imagesLoaded(isotopeItem.querySelector('.isotope-container'), function() {
      initIsotope = new Isotope(isotopeItem.querySelector('.isotope-container'), {
        itemSelector: '.isotope-item',
        layoutMode: layout,
        filter: filter,
        sortBy: sort
      });
    });

    isotopeItem.querySelectorAll('.isotope-filters li').forEach(function(filters) {
      filters.addEventListener('click', function() {
        isotopeItem.querySelector('.isotope-filters .filter-active').classList.remove('filter-active');
        this.classList.add('filter-active');
        initIsotope.arrange({
          filter: this.getAttribute('data-filter')
        });
        if (typeof aosInit === 'function') {
          aosInit();
        }
      }, false);
    });

  });

  /**
   * Frequently Asked Questions Toggle
   */
  document.querySelectorAll('.faq-item h3, .faq-item .faq-toggle').forEach((faqItem) => {
    faqItem.addEventListener('click', () => {
      faqItem.parentNode.classList.toggle('faq-active');
    });
  });

  /**
   * Correct scrolling position upon page load for URLs containing hash links.
   */
  window.addEventListener('load', function(e) {
    if (window.location.hash) {
      if (document.querySelector(window.location.hash)) {
        setTimeout(() => {
          let section = document.querySelector(window.location.hash);
          let scrollMarginTop = getComputedStyle(section).scrollMarginTop;
          window.scrollTo({
            top: section.offsetTop - parseInt(scrollMarginTop),
            behavior: 'smooth'
          });
        }, 100);
      }
    }
  });
  document.addEventListener("DOMContentLoaded", function() {
    const navLinks = document.querySelectorAll('.navmenu a');

    // Add a click event to each navigation link
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            // Remove the 'active' class from all links
            navLinks.forEach(nav => nav.classList.remove('active'));

            // Add the 'active' class to the clicked link
            this.classList.add('active');
        });
    });
});

  /**
   * Navmenu Scrollspy
   */
  let navmenulinks = document.querySelectorAll('.navmenu a');

  function navmenuScrollspy() {
    navmenulinks.forEach(navmenulink => {
      if (!navmenulink.hash) return;
      let section = document.querySelector(navmenulink.hash);
      if (!section) return;
      let position = window.scrollY + 200;
      if (position >= section.offsetTop && position <= (section.offsetTop + section.offsetHeight)) {
        document.querySelectorAll('.navmenu a.active').forEach(link => link.classList.remove('active'));
        navmenulink.classList.add('active');
      } else {
        navmenulink.classList.remove('active');
      }
    })
  }
  window.addEventListener('load', navmenuScrollspy);
  document.addEventListener('scroll', navmenuScrollspy);

})();