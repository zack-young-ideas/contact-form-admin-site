import React, { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.tsx'

const domContainer = document.getElementById('dashboard-modal');
let twoFactorAuth = domContainer.getAttribute('data-two-factor-auth');
const twoFactorAuthLink = domContainer.getAttribute(
  'data-two-factor-auth-link'
);
if (twoFactorAuth === undefined) {
  twoFactorAuth = false;
}
let verifyEmail = domContainer.getAttribute('data-verify-email');
const verifyEmailLink = domContainer.getAttribute(
  'data-verify-email-link'
);
if (verifyEmail === undefined) {
  verifyEmail = false;
}

createRoot(domContainer).render(
  <StrictMode>
    <App
      twoFactorAuth={twoFactorAuth}
      twoFactorAuthLink={twoFactorAuthLink}
      verifyEmail={verifyEmail}
      verifyEmailLink={verifyEmailLink}
    />
  </StrictMode>,
)
