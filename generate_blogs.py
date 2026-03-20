import os

template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Milleth Journal</title>
    <meta name="description" content="{desc}">
    <link rel="canonical" href="https://PG-Sreekanth.github.io/seo-demo-site/{filename}">
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>
    <header class="main-nav">
        <div class="container nav-container">
            <a href="index.html" class="logo">Milleth.</a>
            <ul class="nav-links">
                <li><a href="index.html">Home</a></li>
                <li><a href="products.html">Shop Grains</a></li>
                <li><a href="about.html">Our Story</a></li>
                <li><a href="blog.html" class="active">Journal</a></li>
                <li><a href="contact.html">Contact</a></li>
            </ul>
        </div>
    </header>

    <main>
        <section class="page-hero section text-center reveal">
            <div class="container">
                <div class="breadcrumb">
                    <a href="blog.html">&larr; Back to Journal</a>
                </div>
                <h1 style="max-width:800px; margin: 0 auto; line-height: 1.15; padding-top: 1rem;">{title}</h1>
                <p style="margin-top: 1rem; color: var(--clr-sage); font-weight: 500;">{meta}</p>
            </div>
        </section>

        <section class="article-body section no-pt reveal delay-1">
            <div class="container" style="max-width: 800px;">
                <img src="images/hero_millets.png" alt="Blog cover" style="width:100%; height:400px; object-fit:cover; border-radius:12px; margin-bottom:3rem; box-shadow: 0 10px 40px rgba(0,0,0,0.08);">
                <div class="article-content" style="font-size: 1.15rem; color: #444; line-height: 1.8;">
                    {content}
                </div>
            </div>
        </section>
    </main>

    <footer class="main-footer">
        <div class="container">
            <div class="footer-bottom" style="border-top: none;">
                <div class="copyright">&copy; 2026 Milleth Organic. All rights reserved.</div>
                <div class="footer-badges">
                    <span>NPOP Certified</span>
                    <span>•</span>
                    <span>100% Organic</span>
                </div>
            </div>
        </div>
    </footer>
    <script src="js/main.js"></script>
</body>
</html>"""

blogs = [
    {
        "filename": "blog-ragi-dosa.html",
        "title": "Fluffy Ragi Dosa: The Perfect Fermentation Secret",
        "desc": "Master the art of perfectly fermented, crispy and fluffy Ragi (Finger Millet) dosas.",
        "meta": "Recipes • 4 Min Read",
        "content": "<p>Making the perfect Ragi dosa requires understanding the science of fermentation...</p> <p>Unlike rice batter, finger millet has a different starch composition. For the best ferment, soak 2 parts Ragi, 1 part Urad dal, and a pinch of fenugreek separately for 6 hours.</p> <p>Blend them until smooth, combining the batters by hand to introduce the right wild yeast. Let it rest overnight in a warm place. The resulting dosa will be incredibly crispy, retaining its dark, beautiful earthy hue, packing an immense calcium punch for your morning breakfast.</p>"
    },
    {
        "filename": "blog-water-crisis.html",
        "title": "How Ancient Grains Can Save India's Water Crisis",
        "desc": "Exploring the dramatic difference in water footprint between rice and native millets.",
        "meta": "Farming • 5 Min Read",
        "content": "<p>Did you know that producing one kilogram of rice requires roughly 4,000 liters of water? In regions of the Deccan Plateau facing acute groundwater depletion, this is statistically unsustainable.</p><p>Millets, conversely, are miraculous survivors. A crop like pearl millet (Bajra) or sorghum (Jowar) requires less than 30% of the water compared to paddy. They thrive in semi-arid zones, relying gracefully on seasonal monsoons without needing deep bore-well irrigation.</p><p>By choosing millets, you aren't just choosing health; you are actively casting a vote to preserve India's rapidly sinking water tables and supporting farmers who respect the land's natural carrying capacity.</p>"
    },
    {
        "filename": "blog-kodo-millet.html",
        "title": "Brown Rice vs Kodo Millet: Unpacking the Nutrients",
        "desc": "A head-to-head nutritional battle between brown rice and kodo millet.",
        "meta": "Comparisons • 3 Min Read",
        "content": "<p>Brown rice has long been championed as the healthy alternative to white rice. But how does it fare when stacked against a native ancient grain like Kodo Millet?</p><p>While brown rice offers around 3 grams of dietary fiber per 100g, Kodo Millet delivers a staggering 9 grams of dietary fiber. Furthermore, the protein profile of Kodo is far superior, clocking in at 8.3g with a much better array of essential amino acids.</p><p>Crucially, Kodo millet boasts a significantly lower glycemic index. For anyone monitoring their blood sugar, making the switch from brown rice to Kodo is a powerful metabolic upgrade that doesn't compromise on the comforting texture of a hearty grain bowl.</p>"
    },
    {
        "filename": "blog-kids.html",
        "title": "Feeding Kids Millets: 5 Kid-Approved Strategies",
        "desc": "Sneak ancient nutrition into your child's diet without the fuss.",
        "meta": "Lifestyle • 4 Min Read",
        "content": "<p>Transitioning children from refined grains to robust ancient grains can be challenging. Here are our top strategies to make millets kid-friendly.</p><h3 style=\"margin-top:2rem;\">1. The 50/50 Cookie Trick</h3><p>Next time you bake chocolate chip cookies, replace half the all-purpose flour with finely milled Sorghum (Jowar) flour. It adds a subtle nutty sweetness that pairs perfectly with chocolate.</p><h3 style=\"margin-top:2rem;\">2. Supercharged Porridge</h3><p>Instead of oats, boil Ragi flakes in milk, sweeten heavily with dates or jaggery, and top with their favorite fruits.</p><h3 style=\"margin-top:2rem;\">3. The 'Brownie' Dosa</h3><p>Ragi dosas are naturally dark brown. Call them 'Chocolate Dosas' and watch the resistance melt away! It is all about the presentation.</p>"
    }
]

for b in blogs:
    html = template.format(**b)
    with open(b['filename'], 'w', encoding='utf-8') as f:
        f.write(html)
    
blog_html = open('blog.html', 'r', encoding='utf-8').read()
blog_html = blog_html.replace('href="#" class="blog-card small hover-lift reveal delay-1"', 'href="blog-ragi-dosa.html" class="blog-card small hover-lift reveal delay-1"')
blog_html = blog_html.replace('href="#" class="blog-card small hover-lift reveal delay-2"', 'href="blog-water-crisis.html" class="blog-card small hover-lift reveal delay-2"')
blog_html = blog_html.replace('href="#" class="blog-card small hover-lift reveal delay-3"', 'href="blog-kodo-millet.html" class="blog-card small hover-lift reveal delay-3"')
blog_html = blog_html.replace('href="#" class="blog-card small hover-lift reveal delay-4"', 'href="blog-kids.html" class="blog-card small hover-lift reveal delay-4"')
with open('blog.html', 'w', encoding='utf-8') as f:
    f.write(blog_html)

index_html = open('index.html', 'r', encoding='utf-8').read()
index_html = index_html.replace('<a href="blog.html" class="blog-card small hover-lift">\n                            <div class="blog-img" style="background:var(--clr-sand);height:160px;border-radius:12px;"></div>\n                            <div class="blog-meta">Recipes', '<a href="blog-ragi-dosa.html" class="blog-card small hover-lift">\n                            <div class="blog-img" style="background:var(--clr-sand);height:160px;border-radius:12px;"></div>\n                            <div class="blog-meta">Recipes')
index_html = index_html.replace('<a href="blog.html" class="blog-card small hover-lift">\n                            <div class="blog-img" style="background:var(--clr-sand);height:160px;border-radius:12px;"></div>\n                            <div class="blog-meta">Sustainability', '<a href="blog-water-crisis.html" class="blog-card small hover-lift">\n                            <div class="blog-img" style="background:var(--clr-sand);height:160px;border-radius:12px;"></div>\n                            <div class="blog-meta">Sustainability')
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)
