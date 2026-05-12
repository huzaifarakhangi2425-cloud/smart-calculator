# Hosting + Domain + OAuth (Google) Plan

## Information gathered
- Project is a Node/Express server serving static files from `public/` and API endpoints:
  - `GET /api/products`
  - `GET /api/categories`
  - `GET /api/health`
- `public/index.html` is a single-page UI calling `/api/*` from the same origin.
- `public/sw.js` is currently a placeholder (service worker not registered in the HTML).
- `package.json` has only `dev` and `start` scripts; no production build step.
- No existing OAuth/domain configuration found in the current code.

## Plan (approved by user after confirmation)
1) Make the app production-friendly
   - Add `helmet` for security headers.
   - Add request logging in production.
   - Ensure correct caching headers for static assets.

2) Add Google OAuth “Continue with Google”
   - Install and configure `passport` + `passport-google-oauth20`.
   - Add routes:
     - `GET /auth/google`
     - `GET /auth/google/callback`
     - `GET /auth/me` (returns logged-in user)
     - (optional) `POST /auth/logout`
   - Add a login button + UI state in `public/index.html`.

3) Hosting best option (user preference)
   - Use Vercel for fastest domain setup if possible.
   - If Express server must run as-is, use Render/Fly.io (Node server).
   - Add production server entry and environment variable mapping.

4) Custom domain (DNS)
   - Configure A/AAAA/CNAME depending on provider.
   - Add HTTPS certificate automatically via provider.

5) Gmail requirement interpretation
   - Implement Google sign-in (OAuth) as confirmed by user.
   - (Do not configure email sending unless requested.)

## Dependent files to edit
- `package.json`
- `server.js`
- `public/index.html`
- Potentially `public/sw.js` (only if we decide to register it)

## Follow-up steps
- Install deps (`npm i`)
- Create OAuth credentials in Google Cloud Console.
- Add env vars (client id/secret, callback URL) in hosting provider.
- Run locally: `npm run start`.
- Deploy and verify Google login end-to-end.


