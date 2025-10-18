import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.tsx'

createRoot(document.getElementById('dashboard-modal')).render(
  <StrictMode>
    <App />
  </StrictMode>,
)
