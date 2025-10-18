import React, { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import '@testing-library/jest-dom/vitest';
import App from '../App.tsx';

test("doesn't display modal by default", () => {
  render(<App
    twoFactorAuth={false}
    twoFactorAuthLink={'http://localhost:5173/two-factor-auth'}
    verifyEmail={false}
    verifyEmailLink={'http://localhost:5173/verify-email'}
  />);

  const modalTitle = screen.queryByRole('heading');

  expect(modalTitle).toBeNull();
});

test("user can close modal by clicking 'X' button", async () => {
  render(<App
    twoFactorAuth={true}
    twoFactorAuthLink={'http://localhost:5173/two-factor-auth'}
    verifyEmail={false}
    verifyEmailLink={'http://localhost:5173/verify-email'}
  />);

  const modalTitle = screen.queryByRole('heading');

  expect(modalTitle).toBeVisible();

  await userEvent.click(screen.getByTestId('x-button'));

  expect(modalTitle).not.toBeVisible();
});

test("user can close modal by clicking 'Skip' button", async () => {
  render(<App
    twoFactorAuth={true}
    twoFactorAuthLink={'http://localhost:5173/two-factor-auth'}
    verifyEmail={false}
    verifyEmailLink={'http://localhost:5173/verify-email'}
  />);

  const modalTitle = screen.queryByRole('heading');

  expect(modalTitle).toBeVisible();

  await userEvent.click(screen.getByRole('button', { name: 'Skip' }));

  expect(modalTitle).not.toBeVisible();
});

test('displays proper content when two-factor auth is required', async () => {
  render(<App
    twoFactorAuth={true}
    twoFactorAuthLink={'http://localhost:5173/two-factor-auth'}
    verifyEmail={false}
    verifyEmailLink={'http://localhost:5173/verify-email'}
  />);

  expect(screen.getByRole('heading')).toHaveTextContent(
    'Enable Two-Factor Authentication'
  );

  expect(screen.getByTestId('modal-content')).toHaveTextContent(
    'You have not enabled two-factor authentication.'
  );

  expect(screen.getByText('Enable Now')).toHaveAttribute(
    'href',
    'http://localhost:5173/two-factor-auth'
  );
});

test('displays proper content when email verification required', async () => {
  render(<App
    twoFactorAuth={false}
    twoFactorAuthLink={'http://localhost:5173/two-factor-auth'}
    verifyEmail={true}
    verifyEmailLink={'http://localhost:5173/verify-email'}
  />);

  expect(screen.getByRole('heading')).toHaveTextContent(
    'Verify Your Email Address'
  );

  expect(screen.getByTestId('modal-content')).toHaveTextContent(
    'You have not verified your email address.'
  );

  expect(screen.getByText('Enable Now')).toHaveAttribute(
    'href',
    'http://localhost:5173/verify-email'
  );
});

test('displays two-factor auth content first', async () => {
  render(<App
    twoFactorAuth={true}
    twoFactorAuthLink={'http://localhost:5173/two-factor-auth'}
    verifyEmail={true}
    verifyEmailLink={'http://localhost:5173/verify-email'}
  />);

  const modalTitle = screen.queryByRole('heading');

  expect(modalTitle).toHaveTextContent('Enable Two-Factor Authentication');

  expect(screen.getByTestId('modal-content')).toHaveTextContent(
    'You have not enabled two-factor authentication.'
  );

  expect(screen.getByText('Enable Now')).toHaveAttribute(
    'href',
    'http://localhost:5173/two-factor-auth'
  );

  await userEvent.click(screen.getByRole('button', { name: 'Skip' }));

  expect(modalTitle).toHaveTextContent('Verify Your Email Address');

  expect(screen.getByTestId('modal-content')).toHaveTextContent(
    'You have not verified your email address.'
  );

  expect(screen.getByText('Enable Now')).toHaveAttribute(
    'href',
    'http://localhost:5173/verify-email'
  );

  await userEvent.click(screen.getByRole('button', { name: 'Skip' }));

  expect(modalTitle).not.toBeVisible();
});
