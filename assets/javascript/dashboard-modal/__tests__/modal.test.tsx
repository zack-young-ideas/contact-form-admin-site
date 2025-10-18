import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import '@testing-library/jest-dom/vitest';
import App from '../App.tsx';

test("doesn't display modal by default", () => {
  render(<App twoFactorAuth={false} verifyEmail={false} />);

  const modalTitle = screen.queryByRole('heading');

  expect(modalTitle).toBeNull();
});

test('displays modal if twoFactorAuth is true', async () => {
  render(<App twoFactorAuth={true} verifyEmail={false} />);

  expect(screen.queryByRole('heading')).toBeVisible();
});

test('displays modal if verifyEmail is true', async () => {
  render(<App twoFactorAuth={false} verifyEmail={true} />);

  expect(screen.queryByRole('heading')).toBeVisible();
});

test("user can close modal by clicking 'X' button", async () => {
  render(<App twoFactorAuth={true} verifyEmail={false} />);

  const modalTitle = screen.queryByRole('heading');

  expect(modalTitle).toBeVisible();

  await userEvent.click(screen.getByTestId('x-button'));

  expect(modalTitle).not.toBeVisible();
});

test("user can close modal by clicking 'Skip' button", async () => {
  render(<App twoFactorAuth={true} verifyEmail={false} />);

  const modalTitle = screen.queryByRole('heading');

  expect(modalTitle).toBeVisible();

  await userEvent.click(screen.getByRole('button', { name: 'Skip' }));

  expect(modalTitle).not.toBeVisible();
});
