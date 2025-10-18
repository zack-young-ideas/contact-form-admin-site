import React, { useState } from 'react'

function App({
  twoFactorAuth,
  verifyEmail,
}: {
  twoFactorAuth: boolean,
  verifyEmail: boolean,
}) {
  const [display, setDisplay] = useState(twoFactorAuth || verifyEmail);

  const hideModal = () => {
    setDisplay(false);
  }

  return (
    <div
      className="bg-dark bg-opacity-50 modal"
      id="prompt-window"
      style={{ display: display ? 'block' : 'none' }}
    >
      <div className="modal-dialog">
        <div className="modal-content">
          <div className="modal-header">
            <h2>Enable Two-Factor Authentication</h2>
            <button
              className="btn-close close-modal-button"
              data-testid="x-button"
              onClick={hideModal}
            >
            </button>
          </div>
          <div className="modal-body">
            <p>
              You have not enabled two-factor authentication. It is
              strongly recommended you do this now.</p>
          </div>
          <div className="modal-footer">
            <button
              className="btn btn-secondary close-modal-button"
              onClick={hideModal}
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
