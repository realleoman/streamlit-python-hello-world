import { expect, test } from '@playwright/test';

test('page loads without JavaScript errors and shows the app shell', async ({ page }) => {
  const pageErrors: string[] = [];
  page.on('pageerror', (error) => pageErrors.push(error.message));

  await page.goto('/');

  await expect(page.getByRole('heading', { name: 'Hello World' })).toBeVisible();
  await expect(page.getByRole('button', { name: 'Click me' })).toBeVisible();
  expect(pageErrors).toEqual([]);
});

test('clicking the button renders the greeting', async ({ page }) => {
  await page.goto('/');
  await page.getByRole('button', { name: 'Click me' }).click();

  await expect(page.getByText('Hello World').nth(1)).toBeVisible();
});
