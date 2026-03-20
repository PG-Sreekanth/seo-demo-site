# Milleth Organic - Premium Static Website

This repository contains the complete, production-ready static website for **Milleth Organic**.

## Features
- **5 Custom Pages**: Home, Products, About, Journal (Blog), Contact
- **Premium Design System**: Organic color palette, elegant typography (Cormorant Garamond + DM Sans), subtle SVG noise textures for an earthy feel
- **Animations**: CSS-only smooth scroll-reveal animations via IntersectionObserver, hover micro-interactions, pure JS count-up animations
- **SEO Optimized**: Unique meta descriptions, canonical tags, OpenGraph data, and comprehensive Schema.org JSON-LD structured data on every page
- **Responsive**: Fully responsive mobile-first grid layout serving desktop, tablet, and mobile seamlessly
- **Zero Dependencies**: Built with 100% Vanilla HTML, CSS, and JS. No build tools, no npm, no frameworks required.

## Local Development
To run this website locally:
1. Clone this repository or download the files.
2. The website uses standard HTML/CSS. However, to avoid local file protocol (`file://`) restrictions, it's best to run a local development server.
   - If you have Python installed, run: `python -m http.server 8000`
   - If you have Node.js installed, run: `npx serve` or `npx live-server`
3. Open your browser and navigate to the provided local URL (e.g., `http://localhost:8000`).

## Deployment to GitHub Pages
This project is carefully structured to be deployed to GitHub Pages instantly and without any build steps.

1. Create a new repository on your GitHub account.
2. Push all the files (`css/`, `js/`, `images/`, and all `.html` files) to the `main` branch.
3. In your GitHub repository, navigate to **Settings** > **Pages**.
4. Under "Build and deployment", select **Deploy from a branch**.
5. Select the `main` branch and `/ (root)` folder.
6. Click **Save**.
7. GitHub will deploy your site in a couple of minutes and provide a live URL (e.g., `https://username.github.io/reponame/`).

> **Note on SEO URLs**: The HTML files currently contain canonical URLs pointing to `https://milleth.in/`. If you are deploying to a different domain, make sure to find and replace `https://milleth.in/` with your actual domain in the `<head>` of all HTML files.
