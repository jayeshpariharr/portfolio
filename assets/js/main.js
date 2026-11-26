/**
 * Jayesh Parihar — Portfolio Main Script
 * Lightweight vanilla JS for theme toggling, mobile navigation, and TOC highlighting.
 * No external dependencies.
 */

(function () {
  'use strict';

  // --------------------------------------------------------------------------
  // Theme Management (prefers-color-scheme + manual toggle)
  // --------------------------------------------------------------------------
  const THEME_STORAGE_KEY = 'jayesh_portfolio_theme';
  const root = document.documentElement;
  const themeToggleBtn = document.getElementById('theme-toggle');

  function getSystemTheme() {
    return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches
      ? 'dark'
      : 'light';
  }

  function applyTheme(theme) {
    if (theme === 'dark') {
      root.setAttribute('data-theme', 'dark');
    } else if (theme === 'light') {
      root.setAttribute('data-theme', 'light');
    } else {
      root.removeAttribute('data-theme');
    }
    updateThemeToggleUI();
  }

  function getCurrentTheme() {
    return root.getAttribute('data-theme') || getSystemTheme();
  }

  function updateThemeToggleUI() {
    if (!themeToggleBtn) return;
    const currentTheme = getCurrentTheme();
    const isDark = currentTheme === 'dark';
    
    themeToggleBtn.setAttribute('aria-label', isDark ? 'Switch to light mode' : 'Switch to dark mode');
    themeToggleBtn.title = isDark ? 'Switch to light mode' : 'Switch to dark mode';
    
    // Moon / Sun SVGs
    if (isDark) {
      themeToggleBtn.innerHTML = `
        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
          <circle cx="12" cy="12" r="5"></circle>
          <line x1="12" y1="1" x2="12" y2="3"></line>
          <line x1="12" y1="21" x2="12" y2="23"></line>
          <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
          <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
          <line x1="1" y1="12" x2="3" y2="12"></line>
          <line x1="21" y1="12" x2="23" y2="12"></line>
          <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
          <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
        </svg>
      `;
    } else {
      themeToggleBtn.innerHTML = `
        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
          <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
        </svg>
      `;
    }
  }

  if (themeToggleBtn) {
    themeToggleBtn.addEventListener('click', function () {
      const current = getCurrentTheme();
      const nextTheme = current === 'dark' ? 'light' : 'dark';
      localStorage.setItem(THEME_STORAGE_KEY, nextTheme);
      applyTheme(nextTheme);
    });
  }

  // Listen to system theme changes if no explicit user override
  if (window.matchMedia) {
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function () {
      if (!localStorage.getItem(THEME_STORAGE_KEY)) {
        updateThemeToggleUI();
      }
    });
  }

  // Initialize theme from storage
  const savedTheme = localStorage.getItem(THEME_STORAGE_KEY);
  if (savedTheme) {
    applyTheme(savedTheme);
  } else {
    updateThemeToggleUI();
  }

  // --------------------------------------------------------------------------
  // Mobile Navigation Toggle
  // --------------------------------------------------------------------------
  const mobileToggle = document.getElementById('mobile-nav-toggle');
  const siteNav = document.getElementById('site-nav');

  if (mobileToggle && siteNav) {
    mobileToggle.addEventListener('click', function () {
      const isOpen = siteNav.classList.toggle('is-open');
      mobileToggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
      mobileToggle.setAttribute('aria-label', isOpen ? 'Close navigation menu' : 'Open navigation menu');
    });

    // Close when link is clicked
    siteNav.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        siteNav.classList.remove('is-open');
        mobileToggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  // --------------------------------------------------------------------------
  // Table of Contents Active Link Highlighting (Case Studies)
  // --------------------------------------------------------------------------
  const tocLinks = document.querySelectorAll('.case-toc-link');
  const caseSections = document.querySelectorAll('.case-section');

  if (tocLinks.length > 0 && caseSections.length > 0 && 'IntersectionObserver' in window) {
    const observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            const id = entry.target.getAttribute('id');
            tocLinks.forEach(function (link) {
              if (link.getAttribute('href') === '#' + id) {
                link.classList.add('active');
              } else {
                link.classList.remove('active');
              }
            });
          }
        });
      },
      {
        rootMargin: '-20% 0px -70% 0px'
      }
    );

    caseSections.forEach(function (section) {
      observer.observe(section);
    });
  }

  // --------------------------------------------------------------------------
  // Resume Preview Modal (Read before downloading)
  // --------------------------------------------------------------------------
  const resumeModal = document.getElementById('resume-modal');
  const resumeTriggers = document.querySelectorAll('.js-open-resume');
  const resumeCloseBtn = document.getElementById('resume-modal-close');
  const resumeCancelBtn = document.getElementById('resume-modal-cancel');
  let previouslyFocusedElement = null;

  function openResumeModal(e) {
    if (e) e.preventDefault();
    if (!resumeModal) return;
    previouslyFocusedElement = document.activeElement;
    resumeModal.classList.add('is-open');
    resumeModal.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
    if (resumeCloseBtn) {
      resumeCloseBtn.focus();
    }
  }

  function closeResumeModal() {
    if (!resumeModal) return;
    resumeModal.classList.remove('is-open');
    resumeModal.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
    if (previouslyFocusedElement && typeof previouslyFocusedElement.focus === 'function') {
      previouslyFocusedElement.focus();
    }
  }

  resumeTriggers.forEach(function (btn) {
    btn.addEventListener('click', openResumeModal);
  });

  if (resumeCloseBtn) {
    resumeCloseBtn.addEventListener('click', closeResumeModal);
  }
  if (resumeCancelBtn) {
    resumeCancelBtn.addEventListener('click', closeResumeModal);
  }

  if (resumeModal) {
    resumeModal.addEventListener('click', function (e) {
      if (e.target === resumeModal) {
        closeResumeModal();
      }
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && resumeModal.classList.contains('is-open')) {
        closeResumeModal();
      }
    });
  }

  // --------------------------------------------------------------------------
  // Hero Background Motion Video & Toggle
  // --------------------------------------------------------------------------
  const heroVideo = document.getElementById('hero-bg-video');
  const motionToggleBtn = document.getElementById('motion-toggle');

  if (heroVideo && motionToggleBtn) {
    const motionLabel = motionToggleBtn.querySelector('.motion-toggle-label');
    const prefersReducedMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    function setMotionState(shouldPlay) {
      if (shouldPlay) {
        heroVideo.play().then(function() {
          motionToggleBtn.classList.remove('is-paused');
          motionToggleBtn.setAttribute('aria-label', 'Pause background motion');
          if (motionLabel) motionLabel.textContent = 'Motion ON';
        }).catch(function() {
          // Autoplay policy or low battery mode
        });
      } else {
        heroVideo.pause();
        motionToggleBtn.classList.add('is-paused');
        motionToggleBtn.setAttribute('aria-label', 'Play background motion');
        if (motionLabel) motionLabel.textContent = 'Motion OFF';
      }
    }

    if (prefersReducedMotion) {
      setMotionState(false);
    } else {
      setMotionState(true);
    }

    motionToggleBtn.addEventListener('click', function() {
      const isPaused = heroVideo.paused;
      setMotionState(isPaused);
    });
  }
})();
