import React, { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.tsx'

const domContainer = document.getElementById('dashboard-modal');
let twoFactorAuth = domContainer.getAttribute('data-two-factor-auth');
if (twoFactorAuth === undefined) {
  twoFactorAuth = false;
}
let verifyEmail = domContainer.getAttribute('data-verify-email');
if (verifyEmail === undefined) {
  verifyEmail = false;
}

createRoot(domContainer).render(
  <StrictMode>
    <App twoFactorAuth={twoFactorAuth} verifyEmail={verifyEmail} />
  </StrictMode>,
)
