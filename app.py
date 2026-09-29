import os
from flask import Flask, render_template_string

app = Flask(__name__)

FULL_WEBSITE_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nepali Global Connect</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #f8fafc; color: #1e293b; line-height: 1.6; }
        
        /* Navigation Bar */
        navbar { background: #0f172a; color: white; padding: 1rem 2rem; display: flex; justify-content: space-between; align-items: center; position: sticky; top: 0; z-index: 100; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); }
        .logo { font-size: 1.4rem; font-weight: bold; color: #f87171; display: flex; align-items: center; gap: 8px; }
        .nav-links { display: flex; gap: 20px; align-items: center; }
        .nav-links a { color: #cbd5e1; text-decoration: none; font-weight: 500; font-size: 0.95rem; transition: color 0.2s; }
        .nav-links a:hover { color: white; }
        .auth-btns { display: flex; gap: 10px; }
        .btn { padding: 8px 16px; border-radius: 6px; text-decoration: none; font-weight: 600; font-size: 0.9rem; border: none; cursor: pointer; transition: 0.2s; }
        .btn-login { background: transparent; color: white; border: 1px solid #475569; }
        .btn-login:hover { background: #334155; }
        .btn-signup { background: #dc2626; color: white; }
        .btn-signup:hover { background: #b91c1c; }

        /* Hero Section */
        .hero { background: linear-gradient(135deg, #1e3a8a 0%, #0f172a 100%); color: white; text-align: center; padding: 4rem 1rem; }
        .hero h1 { font-size: 2.8rem; margin-bottom: 1rem; }
        .hero p { font-size: 1.2rem; color: #93c5fd; max-width: 600px; margin: 0 auto 2rem; }

        /* Main Container */
        .container { max-width: 1100px; margin: 0 auto; padding: 2rem 1rem; }
        .section-title { font-size: 1.8rem; color: #0f172a; margin-bottom: 1.5rem; text-align: center; border-bottom: 3px solid #dc2626; display: inline-block; padding-bottom: 5px; }
        .section-box { background: white; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); margin-bottom: 2.5rem; }

        /* National Anthem Section */
        .anthem-card { background: #f1f5f9; border-left: 5px solid #dc2626; padding: 1.5rem; border-radius: 8px; text-align: center; }
        .anthem-lyrics { font-size: 1.05rem; line-height: 1.8; color: #334155; font-style: italic; margin: 1rem 0; white-space: pre-line; }
        audio { width: 100%; max-width: 500px; margin-top: 10px; }

        /* Jobs Section */
        .jobs-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; margin-top: 1rem; }
        .job-card { border: 1px solid #e2e8f0; padding: 1.5rem; border-radius: 8px; transition: transform 0.2s; }
        .job-card:hover { transform: translateY(-4px); box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1); }
        .job-card h3 { color: #1e3a8a; margin-bottom: 0.5rem; }
        .job-card .country { background: #dbeafe; color: #1e40af; padding: 3px 8px; border-radius: 4px; font-size: 0.8rem; font-weight: bold; }

        /* Subscribe Form */
        .subscribe-form { display: flex; gap: 10px; max-width: 500px; margin: 1rem auto 0; }
        .subscribe-form input[type="email"] { flex: 1; padding: 12px; border: 1px solid #cbd5e1; border-radius: 6px; font-size: 1rem; }

        /* Footer */
        footer { background: #0f172a; color: #94a3b8; text-align: center; padding: 1.5rem; margin-top: 3rem; font-size: 0.9rem; }
    </style>
</head>
<body>

    <!-- Navbar -->
    <navbar>
        <div class="logo">🇳🇵 Nepali Global Connect</div>
        <div class="nav-links">
            <a href="#anthem">National Anthem</a>
            <a href="#jobs">Jobs Abroad</a>
            <a href="#subscribe">Subscribe</a>
        </div>
        <div class="auth-btns">
            <a href="#" class="btn btn-login" onclick="alert('Login Portal Coming Soon!')">Log In</a>
            <a href="#" class="btn btn-signup" onclick="alert('Sign Up Portal Coming Soon!')">Sign Up</a>
        </div>
    </navbar>

    <!-- Hero Section -->
    <div class="hero">
        <h1>Welcome to Nepali Global Connect</h1>
        <p>Connecting Nepalese Community Worldwide – Jobs, Culture & Opportunities</p>
        <a href="#jobs" class="btn btn-signup" style="padding: 12px 24px; font-size: 1rem;">Explore International Jobs</a>
    </div>

    <div class="container">

        <!-- National Anthem Section -->
        <div id="anthem" class="section-box">
            <div style="text-align: center;"><h2 class="section-title">🇳🇵 National Anthem (Sayau Thunga)</h2></div>
            <div class="anthem-card">
                <p class="anthem-lyrics">
                सयौं थुँगा फूलका हामी, एउटै माला नेपाली।
                सार्वभौम भई फैलिएका, मेची-महाकाली॥
                प्रकृतिका कोटि-कोटि सम्पदाको आञ्चल,
                वीरहरूका रगतले स्वतन्त्र र अटल॥
                ज्ञानभूमि, शान्तिभूमि तराई, पहाड, हिमाल,
                अखण्ड यो प्यारा हाम्रो मातृभूमि नेपाल॥
                </p>
                <p><b>Play Audio:</b></p>
                <audio controls>
                    <source src="https://upload.wikimedia.org/wikipedia/commons/d/c8/Sayaun_Thunga_Phool Ka_national_anthem_of_Nepal.ogg" type="audio/ogg">
                    Your browser does not support audio playback.
                </audio>
            </div>
        </div>

        <!-- International Jobs Section -->
        <div id="jobs" class="section-box">
            <div style="text-align: center;"><h2 class="section-title">🌍 International Opportunities</h2></div>
            <p style="text-align: center; color: #64748b; margin-bottom: 1.5rem;">Explore employment and study application options abroad</p>
            
            <div class="jobs-grid">
                <div class="job-card">
                    <span class="country">Japan 🇯🇵</span>
                    <h3 style="margin-top: 10px;">SSW & Student Visas</h3>
                    <p style="font-size: 0.9rem; color: #475569;">Apply for language schools, working visa opportunities & skill tests.</p>
                    <button class="btn btn-signup" style="width: 100%; margin-top: 15px;" onclick="alert('Application form opening soon!')">Apply Now</button>
                </div>

                <div class="job-card">
                    <span class="country">Gulf Countries 🇦🇪 🇶🇦</span>
                    <h3 style="margin-top: 10px;">Skilled & Technical Work</h3>
                    <p style="font-size: 0.9rem; color: #475569;">Verified demand letters for Dubai, Qatar, Saudi Arabia & Kuwait.</p>
                    <button class="btn btn-signup" style="width: 100%; margin-top: 15px;" onclick="alert('Application form opening soon!')">Apply Now</button>
                </div>

                <div class="job-card">
                    <span class="country">Europe / Malta 🇲🇹 🇭🇺</span>
                    <h3 style="margin-top: 10px;">Seasonal & Hospitality Jobs</h3>
                    <p style="font-size: 0.9rem; color: #475569;">Work permits in Malta, Croatia, Romania & Poland.</p>
                    <button class="btn btn-signup" style="width: 100%; margin-top: 15px;" onclick="alert('Application form opening soon!')">Apply Now</button>
                </div>
            </div>
        </div>

        <!-- Subscribe Section -->
        <div id="subscribe" class="section-box" style="text-align: center; background: #eff6ff; border: 1px solid #bfdbfe;">
            <h2 style="color: #1e40af;">📩 Stay Updated</h2>
            <p style="color: #1e3a8a; margin-top: 5px;">Subscribe to get the latest foreign job alerts and community news directly to your inbox.</p>
            
            <form class="subscribe-form" onsubmit="event.preventDefault(); alert('Thank you for subscribing!');">
                <input type="email" placeholder="Enter your email address" required>
                <button type="submit" class="btn btn-signup">Subscribe</button>
            </form>
        </div>

    </div>

    <!-- Footer -->
    <footer>
        <p>&copy; 2026 Nepali Global Connect. All rights reserved.</p>
    </footer>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(FULL_WEBSITE_HTML)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
