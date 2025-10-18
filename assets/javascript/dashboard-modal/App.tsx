import React, { useState } from 'react'

function App({
  twoFactorAuth,
  twoFactorAuthLink,
  verifyEmail,
  verifyEmailLink,
}: {
  twoFactorAuth: boolean,
  twoFactorAuthLink: string,
  verifyEmail: boolean,
  verifyEmailLink: string,
}) {
  const twoFactorAuthHeading = 'Enable Two-Factor Authentication';
  const twoFactorAuthText = (
    'You have not enabled two-factor authentication. It is '
    + 'strongly recommended you do this now.'
  );
  const verifyEmailHeading = 'Verify Your Email Address';
  const verifyEmailText = (
    'You have not verified your email address. It is '
    + 'strongly recommended you do this now.'
  );

  const [display, setDisplay] = useState(twoFactorAuth || verifyEmail);
  const [heading, setHeading] = useState(
    twoFactorAuth ?
    twoFactorAuthHeading :
    verifyEmailHeading
  );
  const [content, setContent] = useState(
    twoFactorAuth ?
    twoFactorAuthText :
    verifyEmailText
  );
  const [link, setLink] = useState(
    twoFactorAuth ?
    twoFactorAuthLink :
    verifyEmailLink
  );

  const hideModal = () => {
    setDisplay(false);
  }

  const skip = () => {
    if (verifyEmail && (content !== verifyEmailText)) {
      setHeading(verifyEmailHeading);
      setContent(verifyEmailText);
      setLink(verifyEmailLink);
    } else{
      setDisplay(false);
    }
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
            <h2>{heading}</h2>
            <button
              className="btn-close close-modal-button"
              data-testid="x-button"
              onClick={hideModal}
            >
            </button>
          </div>
          <div className="modal-body">
            <p data-testid="modal-content">{content}</p>
          </div>
          <div className="modal-footer">
            <button
              className="btn btn-secondary close-modal-button"
              onClick={skip}
            >
              Skip
            </button>
            <a
              className="btn btn-primary"
              href={link}
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
