/**
 * AJANTA: ECHOES IN OCHRE — MAIN CONTROLLER
 * Orchestrates modules, DOM readiness, and runtime diagnostics
 */

import { initNavigation } from './navigation.js';
import { initStoryProgress } from './story-progress.js';
import { initAnimations } from './animations.js';

document.addEventListener('DOMContentLoaded', () => {
  try {
    initNavigation();
  } catch (err) {
    console.error('Error initializing navigation:', err);
  }

  try {
    initStoryProgress();
  } catch (err) {
    console.error('Error initializing story progress:', err);
  }

  try {
    initAnimations();
  } catch (err) {
    console.error('Error initializing animations:', err);
  }

  console.info('Ajanta: Echoes in Ochre successfully initialized.');
});
