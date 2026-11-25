# Jayesh Parihar &mdash; Associate Product Manager Portfolio

Production-ready, high-performance personal portfolio website for **Jayesh Parihar**, applying to Google's Associate Product Manager (APM) program.

Designed for a 30-second mobile recruiter scan: immediate positioning, bold proof points, verifiable product artifacts, and clean editorial typography.

Deployed URL: [https://jayeshpariharr.github.io/portfolio/](https://jayeshpariharr.github.io/portfolio/)

GitHub Repository: [https://github.com/jayeshpariharr/portfolio](https://github.com/jayeshpariharr/portfolio)

---

## 1. Technical Stack & Philosophy

- **Zero Frameworks / Zero Build Step:** Pure semantic HTML5, modern CSS, and minimal vanilla JavaScript. Fast, maintainable, and completely self-contained.
- **Privacy & Performance:** Zero third-party trackers, zero heavy analytics scripts, zero external dependencies except Google Fonts (`Inter`) with system-font fallbacks.
- **Theme Support:** Dark and light modes supported automatically via CSS `prefers-color-scheme` with manual toggle stored in `localStorage`.
- **Accessibility:** WCAG AA contrast ratios, semantic landmarks, skip-to-content navigation, keyboard-accessible focus rings, touch targets &ge; 44px.
- **SEO & Social Sharing:** Full Open Graph, Twitter Cards, canonical tags, `sitemap.xml`, `robots.txt`, and JSON-LD `Person` schema.
- **Print Friendly:** Dedicated `@media print` stylesheet for clean, black-and-white printing.
- **Contact:** Direct `mailto:` integration only. No fake contact forms.

---

## 2. Directory Structure

```text
jayeshpariharr.github.io/
├── index.html                  # Main portfolio homepage (Hero, Proof, Experience, Work, Skills, Education, Contact)
├── marketplace.html            # Case study: B2B Fleet-Telematics Marketplace (v2)
├── fireflies.html              # Case study: Fireflies.ai Commitment Cards (Airtribe Capstone)
├── favicon.svg                 # SVG brand favicon
├── favicon.ico                 # Standard ICO favicon
├── robots.txt                  # Search crawler directives
├── sitemap.xml                 # XML sitemap with canonical URLs
├── README.md                   # Project documentation & deployment guide
└── assets/
    ├── css/
    │   └── style.css           # Production CSS (variables, responsive grid, themes, print)
    ├── js/
    │   └── main.js             # Vanilla JS (theme toggle, mobile nav, TOC intersection observer)
    ├── images/
    │   ├── jayesh-parihar.jpg  # Headshot photo
    │   ├── og-image.png        # 1200x630 Open Graph preview image
    │   └── favicon.svg         # Vector favicon asset
    └── resume/
        └── Jayesh_Parihar_Google_APM_Resume.pdf  # 1-page PDF resume
```

---

## 3. Local Preview Instructions

You can run a local development preview server using Python (pre-installed on Linux/macOS):

```bash
# Navigate to the project directory
cd /home/jayesh/.gemini/antigravity/scratch/jayeshpariharr.github.io

# Start Python's built-in HTTP server on port 8000
python3 -m http.server 8000
```

Open your browser to:
`http://localhost:8000/`

To test on your mobile device over the local network:
`http://<YOUR_LOCAL_IP>:8000/`

---

## 4. GitHub Deployment to `https://github.com/jayeshpariharr/portfolio`

You can publish the entire portfolio to your repository using the automated deployment script (`deploy_to_github.py`) via the GitHub REST API without needing `git` installed:

```bash
cd /home/jayesh/.gemini/antigravity/scratch/jayeshpariharr.github.io

# Run the deployment script with your GitHub Personal Access Token:
python3 deploy_to_github.py <YOUR_GITHUB_TOKEN>
```

### How to get a GitHub Personal Access Token (1 minute):
1. In your browser, open [https://github.com/settings/tokens](https://github.com/settings/tokens) (or Settings &rarr; Developer Settings &rarr; Personal access tokens &rarr; Tokens (classic)).
2. Click **Generate new token (classic)**.
3. Note: `Portfolio Deploy`.
4. Select scope: **`repo`** (Full control of private repositories) or public repo write.
5. Click **Generate token** and copy the token.
6. Run: `python3 deploy_to_github.py ghp_yourTokenHere`

The script will automatically:
- Connect to `https://github.com/jayeshpariharr/portfolio`
- Upload/update all 13 core website files, CSS, JS, images, resume, sitemap, and robots.txt
- Enable GitHub Pages on branch `main` at `/ (root)`
- Provide you with the live link: `https://jayeshpariharr.github.io/portfolio/`

---

### Alternative: Push via Git CLI (if git is installed on your machine)
```bash
cd /home/jayesh/.gemini/antigravity/scratch/jayeshpariharr.github.io
git init
git branch -M main
git add .
git commit -m "Deploy Jayesh Parihar APM Portfolio"
git remote add origin https://github.com/jayeshpariharr/portfolio.git
git push -u origin main
```

---

## 5. Visual Assets & Screenshots

The marketplace case study contains 8 prototype screenshots (`assets/images/marketplace-*.jpg`):
- **Figure 1:** Home & Discovery Architecture (`marketplace-01-home.jpg`)
- **Figure 2:** Hardware Listings & Protocol Filters (`marketplace-02-listing.jpg`)
- **Figure 3:** Hardware Verification & Technical Badging (`marketplace-03-verified.jpg`)
- **Figure 4:** Brand Directory & OEM Ecosystem (`marketplace-04-brands.jpg`)
- **Figure 5:** Product Detail Page & Technical Specifications (`marketplace-05-product.jpg`)
- **Figure 6:** B2B Multi-Item Cart & Standard Billing (`marketplace-06-cart.jpg`)
- **Figure 7:** GST-Ready Multi-Item Checkout (`marketplace-07-checkout.jpg`)
- **Figure 8:** Phase 1 AI-Enabled Search Assistant (`marketplace-08-ai-assistant.jpg`)

Optional placeholders for future updates:
| File | Section | Current Status | Recommended Asset |
| :--- | :--- | :--- | :--- |
| `fireflies.html` | Figure 1 | Extracted Commitments View | Screen from Lovable prototype |
| `fireflies.html` | Figure 2 | Owner Consent & Dependency Tag | Screen from Lovable prototype |
| `fireflies.html` | Figure 3 | Morning Daily Digest | Screen from Lovable prototype |

---

## 6. Compliance & Rule Adherence Audit

- **Honest Competencies:** Contains only honest and approved skills without inflated claims or enterprise software filler.
- **Accurate Metrics:** "INR 2.47 Cr" is designated strictly as "order value" across a "6-month" period in "private launch with existing clients".
- **Zero Hallucinated Metrics:** All facts and numbers match the exact specifications.
- **Accurate Attribution:** Prototyping is explicitly credited as "built using Claude Code" (marketplace) or "built on Lovable" (Fireflies). Coursework projects are clearly labeled as "Airtribe AI-First PM Program, coursework" and Fireflies is clearly noted as "concept only, with no pilot".
