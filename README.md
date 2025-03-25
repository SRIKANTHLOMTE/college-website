# Static Information Website

A simple, elegant static website built with Python (Flask) to display information from files managed by an administrator. The site features a classic design with a black background and gold accents, perfect for showcasing text files and linking to other file types (e.g., PDFs).

## Features
- **Static Site Generation**: Uses Flask and Frozen-Flask to create static HTML files.
- **File-Based Content**: Displays text file contents and links to other files (e.g., PDFs) stored in a `content/` directory.
- **Classy Design**: Black background with gold text and borders for a sophisticated, timeless look.
- **Easy Administration**: Add or update content by placing files in the `content/` folder.

## Project Structure
static-info-website/
├── static/           # CSS and static assets
│   ├── css/
│   │   └── style.css
│   └── content/      # Symlinked content files for static site
├── templates/        # HTML templates
│   ├── base.html
│   └── index.html
├── content/          # Information files (e.g., .txt, .pdf)
│   ├── info1.txt
│   └── doc.pdf
├── app.py            # Main Flask application
├── requirements.txt  # Python dependencies
└── README.md         # This file

text

Collapse

Wrap

Copy

## Prerequisites
- Python 3.x
- pip (Python package manager)

## Setup Instructions
1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/static-info-website.git
   cd static-info-website
Install Dependencies
bash

Collapse

Wrap

Copy
pip install -r requirements.txt
Required packages:
flask
frozen-flask (optional, for static site generation)
Add Content
Place your information files (e.g., .txt, .pdf) in the content/ folder.
Text files will display their contents; other files will be linked.
Run Locally (Dynamic Mode)
bash

Collapse

Wrap

Copy
python app.py
Visit http://127.0.0.1:5000/ to see the site live.
Use this mode for testing and development.
Generate Static Site (Optional)
Uncomment the freezer.freeze() line in app.py and comment out app.run().
Run:
bash

Collapse

Wrap

Copy
python app.py
Static files will be generated in a build/ folder.
Deploy
Upload the build/ folder to a static hosting service (e.g., GitHub Pages, Netlify).
Alternatively, host the dynamic Flask app on a Python-supporting server (e.g., Heroku).
Styling
The site uses a classy design:

Background: Black (#1a1a1a) with a darker header/footer (#0d0d0d).
Text & Accents: Gold (#d4af37) for headings, links, and borders.
Font: Georgia serif for an elegant, traditional feel.
Effects: Subtle shadows and smooth hover transitions.
Customize the styling further in static/css/style.css.

Usage
Adding Content: Drop files into the content/ directory and rerun the app or regenerate the static site.
Tunneling with ngrok (optional):
Install ngrok: ngrok.com/download.
Sign up and get your authtoken: ngrok dashboard.
Authenticate: ngrok config add-authtoken <YOUR_AUTH_TOKEN>.
Tunnel: ngrok http 5000 (assuming Flask runs on port 5000).
Access the public URL provided by ngrok.
Example
Place info1.txt with "Welcome to my site!" in content/.
Run the app or generate the site.
The homepage will show "info1.txt: Welcome to my site!" in a styled list.
Contributing
Feel free to fork this repository, submit issues, or send pull requests with improvements!

License
This project is licensed under the MIT License - see the  file for details (create one if needed).

Acknowledgments
Built with Flask.
Static generation powered by Frozen-Flask.
Inspired by classic web design aesthetics.
text

Collapse

Wrap

Copy

### Customization Tips
- **Repository Name**: Replace `static-info-website` with your actual repository name.
- **Username**: Update `yourusername` in the clone URL to your GitHub username.
- **License**: If you don’t have a `LICENSE` file, either add one (e.g., MIT) or remove that section.
- **Screenshots**: Add a section like `## Screenshots` with images of the site if you want to showcase the design.
- **Contact**: Include your contact info or a link to your profile if desired.

### How to Add to GitHub
1. Create a file named `README.md` in your project root in VS Code.
2. Copy-paste the content above.
3. Save, commit, and push to your GitHub repository:
   ```bash
   git add README.md
   git commit -m "Add README file"
   git push origin main
