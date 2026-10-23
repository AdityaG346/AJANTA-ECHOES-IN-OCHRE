/**
 * AJANTA: ECHOES IN OCHRE — STORY PROGRESS MODULE
 * Observes narrative scenes and updates progress bar, labels, and header badge
 */

export function initStoryProgress() {
  const sceneElements = document.querySelectorAll('.story-scene');
  const labelElement = document.getElementById('current-scene-label');
  const nameElement = document.getElementById('current-scene-name');
  const progressBar = document.getElementById('story-progress-bar');
  const headerSceneText = document.getElementById('header-scene-text');
  const progressTrack = document.querySelector('.progress-track');

  if (!sceneElements.length) return;

  const totalScenes = sceneElements.length;

  const updateProgressUI = (sceneNum, sceneTitle) => {
    const formattedNum = String(sceneNum).padStart(2, '0');
    const totalFormatted = String(totalScenes).padStart(2, '0');
    const percentage = Math.round((sceneNum / totalScenes) * 100);

    if (labelElement) {
      labelElement.textContent = `SCENE ${formattedNum} / ${totalFormatted}`;
    }

    if (nameElement && sceneTitle) {
      nameElement.textContent = sceneTitle;
    }

    if (progressBar) {
      progressBar.style.width = `${percentage}%`;
    }

    if (progressTrack) {
      progressTrack.setAttribute('aria-valuenow', String(percentage));
    }

    if (headerSceneText) {
      headerSceneText.textContent = `SCENE ${formattedNum} / ${totalFormatted}`;
    }
  };

  // IntersectionObserver to detect scenes entering viewport
  const observerOptions = {
    root: null,
    rootMargin: '-30% 0px -40% 0px',
    threshold: [0.1, 0.5]
  };

  const sceneObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const sceneNum = parseInt(entry.target.getAttribute('data-scene'), 10) || 1;
        const sceneTitle = entry.target.getAttribute('data-title') || '';
        updateProgressUI(sceneNum, sceneTitle);
      }
    });
  }, observerOptions);

  sceneElements.forEach((scene) => sceneObserver.observe(scene));

  // Also update header indicator when outside the story section
  const storySection = document.getElementById('story');
  const ajantaSection = document.getElementById('ajanta');
  const reimaginedSection = document.getElementById('reimagined');
  const sourcesSection = document.getElementById('sources');
  const heroSection = document.getElementById('hero');

  const sectionHeaderObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting && headerSceneText) {
        const id = entry.target.id;
        if (id === 'hero') {
          headerSceneText.textContent = 'OVERVIEW';
        } else if (id === 'ajanta') {
          headerSceneText.textContent = 'AJANTA HERITAGE';
        } else if (id === 'reimagined') {
          headerSceneText.textContent = 'REFLECTION';
        } else if (id === 'sources') {
          headerSceneText.textContent = 'SOURCES & CREDITS';
        }
      }
    });
  }, { rootMargin: '-20% 0px -50% 0px' });

  if (heroSection) sectionHeaderObserver.observe(heroSection);
  if (ajantaSection) sectionHeaderObserver.observe(ajantaSection);
  if (reimaginedSection) sectionHeaderObserver.observe(reimaginedSection);
  if (sourcesSection) sectionHeaderObserver.observe(sourcesSection);
}
