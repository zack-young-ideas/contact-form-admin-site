import { useState } from 'react'

function App() {
  return (
    <div
      className="bg-dark bg-opacity-50 modal"
      id="prompt-window"
      style={{ display: 'block' }}
    >
      <div className="modal-dialog">
        <div className="modal-content">
          <div className="modal-header">
            <h2>Enable Two-Factor Authentication</h2>
            <button className="btn-close close-modal-button"></button>
          </div>
          <div className="modal-body">
            <p>
              You have not enabled two-factor authentication. It is
              strongly recommended you do this now.</p>
          </div>
          <div className="modal-footer">
            <button
              className="btn btn-secondary close-modal-button"
            >
              Skip
            </button>
            <a
              className="btn btn-primary"
              href="{% url 'two-factor-auth' %}"
            >
              Enable Now
            </a>
          </div>
        </div>
      </div>
    </div>
  )
}

export default App
