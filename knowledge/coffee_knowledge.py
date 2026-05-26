"""
Coffee Roasting Knowledge Base
================================
Curated knowledge for the Coffee Roasting Companion.
Organized into domains for RAG retrieval.
"""

KNOWLEDGE_BASE = [

    # ═══════════════════════════════════════════════════════════════
    # DOMAIN 1: BEAN ORIGINS & FLAVOR PROFILES
    # ═══════════════════════════════════════════════════════════════

    {
        "id": "origin-001",
        "domain": "origins",
        "title": "Ethiopia - The Birthplace of Coffee",
        "content": """Ethiopia is where coffee originated, and it still produces some of the most distinctive and complex beans in the world. The country grows primarily heirloom Arabica varieties at elevations between 1,500 and 2,200 meters. The two most famous regions are Yirgacheffe and Sidamo. Yirgacheffe beans are known for their floral, tea-like quality with notes of jasmine, bergamot, and lemon. Sidamo beans tend to be more complex and fruity with berry and wine-like characteristics. Harrar, in eastern Ethiopia, produces wild, winey coffees with blueberry notes, especially when naturally processed. Ethiopian coffees are often processed two ways: washed (producing cleaner, brighter, more floral cups) and natural (sun-dried with the cherry intact, producing intensely fruity, berry-forward flavors). For home roasters, Ethiopian beans are best taken to a light or medium-light roast to preserve their delicate origin flavors. They are dense, high-altitude beans, so they can handle a slightly more aggressive heat application in the early stages but need careful attention during development to avoid baking out the floral notes."""
    },
    {
        "id": "origin-002",
        "domain": "origins",
        "title": "Colombia - The Accessible Classic",
        "content": """Colombia is the world's third-largest coffee producer and is known for consistently balanced, approachable Arabica coffee. The country's varied microclimates, from high-altitude mountains to tropical lowlands, create a wide range of flavor profiles. The southern regions of Huila and Nariño produce brighter, more complex cups with pronounced fruit and caramel sweetness. The traditional coffee axis (Antioquia, Caldas, Risaralda) produces rounder, more caramel-forward cups with nutty undertones. Colombian coffees are almost always washed processed, which gives them a clean, bright character. They typically have medium body, mild-to-bright acidity, and notes of caramel, citrus, stone fruit, and nuts. For home roasters, Colombian beans are incredibly forgiving and are an excellent starting point for beginners. They perform well across a wide roast range from light to medium-dark. A City to City+ roast (just past first crack through about 30 seconds after) brings out the best balance of sweetness and acidity."""
    },
    {
        "id": "origin-003",
        "domain": "origins",
        "title": "Brazil - The Bold Foundation",
        "content": """Brazil is the world's largest coffee producer, responsible for roughly one-third of global production. Brazilian beans are known for their low acidity, full body, and smooth, chocolatey, nutty flavor profiles. The most famous growing regions include Minas Gerais (Sul de Minas for citrusy and fruity notes, Cerrado for nutty and chocolatey), Sao Paulo (Mogiana), and Bahia. Brazilian coffees are often naturally processed (dried inside the cherry), which enhances sweetness and body. You will also see pulped natural (honey) processed beans from Brazil, which offer a middle ground between washed brightness and natural sweetness. For home roasters, Brazilian beans are the ultimate comfort roast. They are forgiving, predictable, and delicious across a wide range. They make excellent espresso at a medium to medium-dark roast. A Full City roast (just approaching second crack) brings out deep chocolate and caramel with a smooth, round finish. Brazilian beans are also the backbone of most espresso blends."""
    },
    {
        "id": "origin-004",
        "domain": "origins",
        "title": "Sumatra (Indonesia) - The Earthy Heavyweight",
        "content": """Sumatran coffees from Indonesia are among the most distinctive in the world. They are known for their heavy body, low acidity, and earthy, spicy, herbal flavor profiles with notes of cedar, tobacco, dark chocolate, and sometimes mushroom or wet earth. The unique character comes largely from a processing method called wet hulling (Giling Basah), where the parchment is removed while the beans still have high moisture content. This creates the characteristic blue-green color of Sumatran beans and their distinctive earthy flavor. Key regions include Mandheling, Lintong, and Gayo (Aceh). Gayo coffees tend to be cleaner and more refined than Mandheling. For home roasters, Sumatran beans are interesting because they look and behave differently from most other origins. They are lower density and more irregular in shape. They handle dark roasting well and are one of the few origins that many people prefer at a Full City+ to Vienna roast. The earthiness becomes rich and syrupy at darker roasts rather than bitter."""
    },
    {
        "id": "origin-005",
        "domain": "origins",
        "title": "Guatemala - The Underrated Gem",
        "content": """Guatemala produces some of the most complex and interesting coffees in Central America, yet it is often overlooked in favor of Ethiopian and Colombian beans. The most famous region is Antigua, which produces coffee with a distinctive smoky, chocolatey character due to the volcanic soil. Huehuetenango, at higher altitudes, produces brighter, more fruity and floral cups with stone fruit and wine-like notes. Guatemalan coffees typically have medium-to-full body, bright acidity, and a complex flavor profile that can include chocolate, caramel, nuts, citrus, and spice. Most are washed processed. For home roasters, Guatemalan beans are a step up in complexity from Colombian. They reward careful roasting with layered flavors. A City to City+ roast highlights their complexity, while pushing to Full City brings out more chocolate and smoke."""
    },
    {
        "id": "origin-006",
        "domain": "origins",
        "title": "Kenya - The Bright Showstopper",
        "content": """Kenyan coffees are prized among specialty coffee enthusiasts for their vibrant, wine-like acidity and bold fruit flavors. They often feature notes of blackcurrant, tomato, grapefruit, and tropical fruit with a juicy, almost syrupy body. The most famous varieties are SL28 and SL34, developed by Scott Laboratories in the 1930s and 1940s, which produce intensely flavorful beans. Kenyan coffees are typically washed processed and grown at 1,400 to 2,000 meters. The combination of high altitude, rich volcanic soil, and meticulous processing creates some of the most distinctive coffees in the world. For home roasters, Kenyan beans demand attention. They are best at light to medium roast levels where their complex acidity and fruit character can shine. Over-roasting kills the brightness that makes Kenyan coffee special. They are dense beans so they can take aggressive early heat but need a longer development time after first crack."""
    },
    {
        "id": "origin-007",
        "domain": "origins",
        "title": "Costa Rica - The Clean Precision",
        "content": """Costa Rica is known for producing exceptionally clean, bright, well-balanced coffees. The country banned Robusta coffee cultivation in 1989, so all Costa Rican coffee is Arabica. Key regions include Tarrazu (bright, complex, citrusy), West Valley (honey-sweet, balanced), and Central Valley (clean, classic). Costa Rican coffees are predominantly washed processed, resulting in clean, transparent cups that clearly express their terroir. Honey processed Costa Rican coffees have become increasingly popular, adding body and sweetness while maintaining brightness. For home roasters, Costa Rican beans are excellent for developing precision. They clearly show the difference between a light, medium, and dark roast, making them great training beans. A City roast produces bright, citrusy cups while a City+ brings out more honey and caramel sweetness."""
    },

    # ═══════════════════════════════════════════════════════════════
    # DOMAIN 2: ROASTING SCIENCE & FUNDAMENTALS
    # ═══════════════════════════════════════════════════════════════

    {
        "id": "science-001",
        "domain": "roasting_science",
        "title": "The Three Stages of Coffee Roasting",
        "content": """Every coffee roast moves through three distinct stages: drying, browning (Maillard), and development. Understanding these stages is the key to controlling your roast. DRYING STAGE: Green coffee beans contain 8-12% moisture. The drying stage drives off this moisture and lasts from the start of the roast until the beans turn from green to yellow, typically around 4-8 minutes and 300-330F (150-165C). During this stage, the beans are absorbing heat (endothermic). You want steady, consistent heat application. Too aggressive and the outside dries faster than the inside, leading to tipping and scorching. Too slow and you bake the beans, producing flat, bread-like flavors. BROWNING STAGE (MAILLARD): Once the beans turn yellow, the Maillard reaction begins. This is a complex chemical reaction between amino acids and reducing sugars that creates hundreds of new flavor compounds, the aromas we associate with roasted coffee. The beans turn progressively darker, and you will smell hay, then bread, then something more recognizably coffee-like. This stage typically runs from about 300F to 385F (150C to 196C). DEVELOPMENT STAGE: This begins at first crack and continues until you end the roast. First crack is an audible popping sound caused by steam and CO2 pressure building inside the bean until the cell walls fracture. This is where you decide the final flavor character of your coffee. Development time as a percentage of total roast time (DTR) is a key metric. A DTR of 20-25% is typical for a balanced roast."""
    },
    {
        "id": "science-002",
        "domain": "roasting_science",
        "title": "First Crack and Second Crack Explained",
        "content": """First crack and second crack are the two most important audible milestones in coffee roasting. FIRST CRACK occurs at approximately 385-400F (196-205C). It sounds like popcorn popping, a series of sharp, loud snapping sounds. First crack is caused by steam and CO2 building up inside the bean until the pressure fractures the cell walls. The beans expand in size, shed chaff (silverskin), and become noticeably lighter in color. First crack is exothermic, meaning the beans are now releasing heat rather than absorbing it. This is important because the roast can accelerate rapidly if you do not reduce heat input. First crack typically lasts 1-3 minutes. SECOND CRACK occurs at approximately 435-450F (224-232C). It sounds different from first crack: quieter, more like Rice Krispies snapping or small cracking rather than popping. Second crack is caused by the oils inside the beans breaking through the cell structure and reaching the surface. This is why dark roasted beans look oily. At second crack, the beans are entering dark roast territory. The sugars are heavily caramelized, origin flavors are largely gone, and roast flavors (smoky, bitter, carbon) dominate. Going much beyond second crack risks fire and produces charcoal-flavored coffee. Most home roasters will want to stay between first crack and the very beginning of second crack for the best flavor."""
    },
    {
        "id": "science-003",
        "domain": "roasting_science",
        "title": "The Maillard Reaction in Coffee",
        "content": """The Maillard reaction is the single most important chemical reaction in coffee roasting. It is a complex reaction between amino acids and reducing sugars that begins around 300F (150C) and produces hundreds of new flavor and aroma compounds. The Maillard reaction is responsible for the brown color of roasted coffee, the formation of melanoidins (which contribute body and mouthfeel), and many of the flavors we associate with coffee: caramel, chocolate, nuts, toast, and bread-like notes. The rate of the Maillard reaction depends on temperature, time, and moisture content. Higher temperatures accelerate it, but too fast and you get uneven development. The key insight for home roasters is that the Maillard reaction is where the magic happens. If you rush through this stage, you miss out on flavor development. If you linger too long, you get flat, baked flavors. The sweet spot is a steady, controlled progression through the browning stage with enough time for complex flavors to form but not so much that the beans lose their vibrancy."""
    },
    {
        "id": "science-004",
        "domain": "roasting_science",
        "title": "Caramelization in Coffee Roasting",
        "content": """Caramelization is the thermal decomposition of sugars and occurs at temperatures above 356F (180C) in coffee roasting. Unlike the Maillard reaction (which involves amino acids and sugars together), caramelization is purely about sugar breakdown. As sugars in the coffee bean heat up, they go through stages: first they melt, then they foam and release water vapor, then they begin to break down into hundreds of new compounds including caramel, toffee, butterscotch, and eventually, if pushed too far, bitter and burnt flavors. Green coffee beans contain about 6-9% sucrose (table sugar), plus smaller amounts of glucose and fructose. During roasting, most of this sugar is consumed by caramelization and the Maillard reaction. Light roasts retain more sugar and taste sweeter and brighter. Dark roasts have consumed most of their sugar and taste more bitter and roast-forward. This is why light roast coffee is not sour because it is underroasted; it is bright because the sugars are still present and the acids have not been fully broken down."""
    },
    {
        "id": "science-005",
        "domain": "roasting_science",
        "title": "Understanding Bean Density and Altitude",
        "content": """Bean density is one of the most important factors in determining how to roast a coffee, and it is primarily driven by growing altitude. Coffee grown at higher altitudes (above 1,500 meters) develops more slowly because of cooler temperatures. This slower development allows more complex sugars and acids to form inside the bean, and the bean itself becomes harder and denser. High-density beans (Ethiopian, Kenyan, Colombian from Huila) can handle more aggressive heat application because the dense cellular structure absorbs and conducts heat more evenly. They also benefit from slightly longer total roast times to allow heat to penetrate fully. Low-density beans (Brazilian, Sumatran, lower-altitude origins) are softer and more porous. They absorb heat faster and require gentler treatment. Too much heat too fast will scorch the outside while the inside remains underdeveloped. A practical test: drop a few green beans into a cup of water. Denser beans sink faster. You can also feel the difference when you handle them: dense beans feel harder and are more difficult to bite in half. As a general rule, start with lower charge temperatures and gentler ramp rates for low-density beans, and higher charge temperatures with more aggressive early heat for high-density beans."""
    },

    # ═══════════════════════════════════════════════════════════════
    # DOMAIN 3: ROAST LEVELS & PROFILES
    # ═══════════════════════════════════════════════════════════════

    {
        "id": "roast-001",
        "domain": "roast_levels",
        "title": "Light Roast - Cinnamon to City",
        "content": """Light roasts are stopped at or shortly after the beginning of first crack, at internal bean temperatures of approximately 385-405F (196-207C). At this level, the beans are light brown, have no oil on the surface, and retain the most origin character. Light roasts have the highest acidity (brightness), the most complex and nuanced flavors, and the most caffeine by volume. Common light roast names include Cinnamon Roast (very light, just before first crack, not recommended for most coffees), Light City (at the start of first crack), and City (first crack complete). Flavor characteristics of light roasts include bright acidity, floral notes, fruit (citrus, berry, stone fruit), tea-like body, and delicate sweetness. Light roasts are best for high-quality single-origin coffees where you want to taste the origin, not the roast. Ethiopian, Kenyan, and Costa Rican coffees often shine at light roast levels. The challenge for home roasters is that light roasts are the least forgiving. Underdevelop them and they taste grassy, sour, and unpleasant. The line between a beautiful light roast and an underdeveloped one is thin."""
    },
    {
        "id": "roast-002",
        "domain": "roast_levels",
        "title": "Medium Roast - City+ to Full City",
        "content": """Medium roasts are the sweet spot for most home roasters and most coffee drinkers. They are stopped between the end of first crack and the beginning of second crack, at internal bean temperatures of approximately 410-435F (210-224C). At this level, the beans are medium brown, may have a slight sheen but no visible oil droplets, and balance origin character with developed roast flavors. Common names include City+ (just past first crack), Full City (approaching second crack). Flavor characteristics of medium roasts include balanced acidity and body, caramel and chocolate sweetness, nut and toast notes, and a richer mouthfeel than light roasts. Some origin fruit character remains but it is complemented by roast-developed sweetness. Medium roasts are the most versatile. They work for drip, pour-over, French press, and espresso. They are forgiving to brew and produce a crowd-pleasing cup. For home roasters, medium roasts are where you build your skills. You learn to read the transition from first crack into the quiet period before second crack and develop an ear for the subtle changes in cracking frequency and bean color."""
    },
    {
        "id": "roast-003",
        "domain": "roast_levels",
        "title": "Dark Roast - Full City+ to French",
        "content": """Dark roasts are stopped at or after the beginning of second crack, at internal bean temperatures of approximately 435-465F (224-240C). At this level, the beans are dark brown to nearly black, have visible oil on the surface (more oil = darker roast), and roast flavors dominate over origin character. Common names include Full City+ (beginning of second crack), Vienna (well into second crack), French (end of second crack, very dark), and Italian (past second crack, nearly black). Flavor characteristics of dark roasts include low acidity, heavy body, smoky and bittersweet flavors, dark chocolate, charred wood, and roast-forward character. Origin flavors are mostly gone at this level. Dark roasts are preferred for espresso by some traditions (Italian-style), cold brew, and people who simply prefer bold, strong coffee. For home roasters, dark roasting requires caution. The beans are releasing a lot of oil and gas, the roast is moving fast, and there is a real risk of fire if you go past French roast. The difference between a good dark roast and burnt coffee is about 15-30 seconds. Ventilation is important because dark roasts produce significantly more smoke."""
    },

    # ═══════════════════════════════════════════════════════════════
    # DOMAIN 4: HOME ROASTING METHODS & EQUIPMENT
    # ═══════════════════════════════════════════════════════════════

    {
        "id": "method-001",
        "domain": "home_roasting",
        "title": "Popcorn Popper Roasting",
        "content": """The hot air popcorn popper is the cheapest and most accessible entry point into home roasting. Models like the Nostalgia or West Bend Poppery have been used by home roasters for decades. They work by blowing extremely hot air through a roasting chamber, agitating the beans and providing even heat. To use: add 1/2 cup (about 80-100g) of green beans, turn it on, and watch. The chaff will blow out the top (roast outside or have a bowl to catch it). You will hear first crack at about 3-5 minutes. For a light roast, stop shortly after first crack begins. For a medium roast, let first crack complete. For dark, continue toward second crack but watch carefully because poppers roast fast and aggressively. Advantages: cheap (under $30), fast (5-7 minute roast), surprisingly even roasting, great chaff ejection. Disadvantages: tiny batch size (3-4 oz), very little control over temperature, loud, burns out after 6-12 months of regular use, no way to profile the roast. The popcorn popper is perfect for your first 20-50 roasts while you learn what you like. Once you are hooked, you will want to upgrade."""
    },
    {
        "id": "method-002",
        "domain": "home_roasting",
        "title": "Dedicated Home Roaster Machines",
        "content": """Dedicated home coffee roasters are purpose-built machines that give you significantly more control than a popcorn popper. Popular models include: ENTRY LEVEL ($150-300): FreshRoast SR540/SR800. Fluid bed (hot air) roasters with adjustable fan speed and heat settings. Batch size 4-8 oz. Good visibility, easy chaff collection, and enough control to start developing consistent profiles. The SR800 has a longer roasting chamber and more capacity. MID-RANGE ($300-700): Behmor 2000AB Plus. Drum roaster with 1 lb capacity, programmable profiles, and a built-in smoke suppression system. This is a serious machine that can produce professional-quality results. It is also one of the few home roasters that works well indoors. Gene Cafe CBR-101. Unique off-axis drum design with 300g capacity. Excellent visibility through a glass drum, consistent results, and good smoke management. ENTHUSIAST ($700-2000+): Aillio Bullet R1. This is the home roaster that serious hobbyists aspire to. It is a 1kg capacity drum roaster with real-time data logging (bean temperature, rate of rise, drum temperature), USB connectivity, and community-shared roast profiles through Roast.World software. It is essentially a miniature commercial roaster. Kaldi Fortis/Wide. Manual drum roasters that sit on a gas burner. They give you the most tactile, hands-on roasting experience and produce excellent results, but require more skill and attention."""
    },
    {
        "id": "method-003",
        "domain": "home_roasting",
        "title": "Skillet and Oven Roasting",
        "content": """Before dedicated roasters existed, people roasted coffee in pans and ovens, and you still can. These methods are free (you already own the equipment) and produce surprisingly decent coffee, though with less consistency. CAST IRON SKILLET: Heat a cast iron skillet over medium-high heat. Add a single layer of green beans (about 8 oz max). Stir constantly with a wooden spoon or spatula. You must keep the beans moving or they will scorch on the contact side. You will hear first crack at about 8-12 minutes. This method produces a lot of smoke and chaff so do it outside or under a powerful vent hood. The results are uneven (some beans will be darker than others) but the coffee will taste surprisingly good. OVEN ROASTING: Preheat oven to 450-500F (232-260C). Spread green beans in a single layer on a perforated baking sheet (holes allow airflow). Place on the middle rack. Stir every 2-3 minutes. First crack around 8-12 minutes. Oven roasting is slow and produces a baked, flat roast compared to other methods because the heat transfer is less efficient. Not ideal but it works in a pinch. Both methods are great for a first experiment to see if you enjoy the process before investing in equipment."""
    },
    {
        "id": "method-004",
        "domain": "home_roasting",
        "title": "Where to Buy Green Coffee Beans",
        "content": """Sourcing quality green coffee beans is easier than most people think. Several online retailers specialize in selling green beans to home roasters: Sweet Maria's (sweetmarias.com) is the most established retailer for home roasters in the US. They offer an enormous selection of single-origin beans with detailed cupping notes, roasting recommendations, and educational content. Their beans are high quality and reasonably priced at $6-10 per pound. Happy Mug Coffee (happymugcoffee.com) offers competitive prices, free shipping on orders over $30, and a good selection of origins. They are particularly popular for budget-friendly options. Burman Coffee Traders (burmancoffee.com) is another long-standing retailer with a wide selection. Dean's Beans and Coffee Shrub are also good options. Green beans are significantly cheaper than roasted coffee. Expect to pay $5-9 per pound for good quality single-origin beans, compared to $15-25 per pound for the same quality roasted. Green beans also last much longer than roasted coffee: 6-12 months stored in a cool, dry place versus 2-4 weeks for roasted beans. This is one of the biggest advantages of home roasting: fresher coffee at a fraction of the cost."""
    },

    # ═══════════════════════════════════════════════════════════════
    # DOMAIN 5: TROUBLESHOOTING COMMON ROASTING PROBLEMS
    # ═══════════════════════════════════════════════════════════════

    {
        "id": "trouble-001",
        "domain": "troubleshooting",
        "title": "Underdeveloped Roast (Grassy, Sour, Unpleasant)",
        "content": """An underdeveloped roast is the most common beginner mistake. The coffee tastes grassy, sour (not bright, genuinely unpleasant sour), vegetal, or peanut-like. The body is thin and the aftertaste is astringent. CAUSES: Stopping the roast too early (before first crack is fully complete), rushing through first crack without enough development time, or insufficient heat during the development stage. FIXES: Let first crack complete fully before stopping the roast. A good minimum development time ratio (DTR) is 20% of total roast time. So if your total roast is 10 minutes, spend at least 2 minutes in the development stage after first crack begins. If you are using a popcorn popper, this can be tricky because they roast fast. Try adding slightly more beans to slow the roast down. HOW TO TELL: Break open a roasted bean. If the inside is significantly lighter than the outside, the roast is underdeveloped. A well-roasted bean should have relatively even color from outside to inside, though a slight gradient is normal."""
    },
    {
        "id": "trouble-002",
        "domain": "troubleshooting",
        "title": "Baked Roast (Flat, Dull, Bread-like)",
        "content": """A baked roast is the second most common problem. The coffee tastes flat, dull, papery, or bread-like. It lacks vibrancy, sweetness, and complexity. It is not bitter (like an over-roast) or sour (like an underdeveloped roast). It is just boring. CAUSES: The roast stalled or lost momentum during the browning or development stage. This happens when you reduce heat too aggressively, when the roast takes too long (over 14-15 minutes total for most home roasters), or when the rate of rise (temperature increase over time) drops to near zero or goes flat. FIXES: Maintain momentum throughout the roast. The rate of temperature increase should be declining (slowing down) but never stalling or reversing. If you see or feel the roast losing energy, add heat. Total roast time for most home roasters should be 8-14 minutes. Under 7 is probably too fast (scorching risk). Over 15 is probably too slow (baking risk). Think of the roast like a ball rolling uphill: it should always be moving forward, just gradually slowing down."""
    },
    {
        "id": "trouble-003",
        "domain": "troubleshooting",
        "title": "Scorched or Tipped Beans",
        "content": """Scorching appears as dark spots or burns on the flat surfaces of the beans. Tipping is small black burn marks on the tips or edges. Both are caused by too much direct heat, especially early in the roast when the beans still have high moisture and are less able to distribute heat internally. CAUSES: Charge temperature too high (the initial temperature of the roasting environment when beans are added), heat too aggressive in the drying stage, or insufficient agitation (beans sitting in one spot too long on a hot surface). FIXES: Lower your starting temperature by 10-15 degrees. In drum roasters, make sure the drum is turning and beans are moving. In fluid bed roasters, make sure airflow is sufficient to keep beans circulating. In skillet roasting, stir constantly and never stop. Scorching and tipping are cosmetic in small amounts but affect flavor at scale: they add a burnt, acrid bitterness to the cup."""
    },
    {
        "id": "trouble-004",
        "domain": "troubleshooting",
        "title": "Uneven Roast (Mixed Light and Dark Beans)",
        "content": """An uneven roast means some beans are significantly darker or lighter than others in the same batch. CAUSES: Mixed bean sizes or densities in the batch (some natural variation is normal, but large differences cause problems), inconsistent heat distribution in the roaster, too large a batch size for the roaster, or insufficient agitation. FIXES: Sort your green beans before roasting and remove any that are obviously larger, smaller, or defective (stones, broken beans, insect-damaged). Do not exceed your roaster's recommended batch size. Make sure airflow (in fluid bed roasters) or drum speed (in drum roasters) is adequate. Some unevenness is normal and expected in home roasting, especially with naturally processed beans which tend to vary more in size and density. A small amount of color variation in the finished batch will not significantly affect cup quality."""
    },
    {
        "id": "trouble-005",
        "domain": "troubleshooting",
        "title": "Smoky or Ashy Taste",
        "content": """Coffee that tastes smoky, ashy, or carbon-like has been roasted too far or too fast at the end. CAUSES: Pushing past second crack, letting the development stage go too long or too hot, poor ventilation during roasting (the smoke reabsorbs into the beans), or insufficient cooling after the roast is dropped. FIXES: End the roast earlier. If you are going for a dark roast, stop at the very beginning of second crack, not deep into it. Improve ventilation during roasting: roast outside, use a fan, or use a roaster with built-in smoke management. Cool the beans as fast as possible after dropping. The beans continue to cook for 1-2 minutes after they leave the roaster (called carry-over roasting). Use a colander with a fan blowing through it, or spread them on a cool baking sheet and shake them. Cooling should take no more than 3-4 minutes for a home batch."""
    },

    # ═══════════════════════════════════════════════════════════════
    # DOMAIN 6: BREWING BASICS FOR HOME-ROASTED COFFEE
    # ═══════════════════════════════════════════════════════════════

    {
        "id": "brew-001",
        "domain": "brewing",
        "title": "Rest Period After Roasting",
        "content": """Freshly roasted coffee needs to rest (degas) before it reaches peak flavor. During roasting, CO2 is trapped inside the beans. This CO2 needs time to escape, and it does so rapidly in the first 24-48 hours and then gradually over the next week. Brewing too soon (within 12-24 hours of roasting) produces a bubbly, uneven extraction because the CO2 interferes with water contacting the coffee grounds. The cup will taste sharp, uneven, and the flavors will not be fully developed. For drip and pour-over: rest 3-5 days for light roasts, 2-4 days for medium, 1-3 days for dark. For espresso: rest 7-14 days. Espresso extraction is more sensitive to CO2, and freshly roasted beans will produce an extremely unstable shot with excessive crema and sour, unbalanced flavors. For French press: rest 2-4 days. The immersion method is less sensitive to degassing than pour-over. Peak flavor is typically 5-14 days after roasting for most coffees. After 3-4 weeks, roasted coffee starts to go stale as the aromatic compounds oxidize and dissipate. This is why home roasting is so powerful: you are always drinking coffee within that peak window."""
    },
    {
        "id": "brew-002",
        "domain": "brewing",
        "title": "Grind Size Matters",
        "content": """Grind size is the single most impactful variable in brewing, after the coffee itself. The grind determines how much surface area is exposed to water, which directly controls extraction rate. TOO FINE: Over-extraction. The water pulls too many compounds from the coffee, including bitter and astringent ones. The cup tastes bitter, harsh, and dry. TOO COARSE: Under-extraction. The water cannot pull enough flavor from the coffee. The cup tastes sour, thin, watery, and underdeveloped. GRIND GUIDELINES (from finest to coarsest): Turkish/Ibrik: powder-fine, like flour. Espresso: very fine, like table salt. Moka pot: fine, between espresso and drip. Pour-over (V60, Chemex): medium-fine to medium, like sea salt. Drip machine: medium, like regular sand. French press: coarse, like raw sugar or breadcrumbs. Cold brew: very coarse, like peppercorn chunks. A burr grinder is essential for consistent grind size. Blade grinders chop unevenly, producing a mix of fine dust and large chunks that extract at different rates, making it nearly impossible to dial in a good cup. A decent hand burr grinder (Timemore C2, 1Zpresso Q2) costs $50-80 and will transform your coffee more than any other single purchase."""
    },
    {
        "id": "brew-003",
        "domain": "brewing",
        "title": "Water Temperature and Quality",
        "content": """Water is 98-99% of a cup of coffee, so its quality and temperature matter enormously. TEMPERATURE: The ideal brewing temperature for most coffee is 195-205F (90-96C). This is just off boiling. Boiling water (212F/100C) can over-extract and scald lighter roasts. Below 195F under-extracts. For light roasts, use the higher end (200-205F) because you want more extraction from the denser, less developed beans. For dark roasts, use the lower end (195-200F) because they are more soluble and extract faster. WATER QUALITY: Use filtered water, not distilled and not unfiltered tap. Distilled water has no minerals, which are needed for proper extraction (water needs mineral content to bond with flavor compounds in coffee). Unfiltered tap water may contain chlorine, excess minerals, or off flavors that ruin the cup. The Specialty Coffee Association recommends water with 150mg/L total dissolved solids (TDS), a pH of 7.0, and no chlorine. In practice, a basic Brita or similar carbon filter on your tap water gets you 90% of the way there."""
    },

    # ═══════════════════════════════════════════════════════════════
    # DOMAIN 7: FUN FACTS & COFFEE CULTURE
    # ═══════════════════════════════════════════════════════════════

    {
        "id": "fun-001",
        "domain": "fun_facts",
        "title": "Coffee Cherry to Cup: The Journey",
        "content": """Most people do not realize that coffee beans are actually seeds from a fruit. The coffee cherry is a small, typically red fruit that grows on a shrub or small tree in tropical regions between the Tropics of Cancer and Capricorn (the Bean Belt). Each cherry usually contains two seeds (coffee beans) facing each other flat-side-in. Occasionally a cherry produces just one round seed called a peaberry, which some people believe produces a sweeter, more concentrated cup (others say there is no difference). From cherry to cup, coffee passes through an extraordinary number of hands. It is picked (often by hand for specialty coffee), processed (washed, natural, or honey), dried to about 10-12% moisture, milled to remove the parchment layer, sorted by size and density, graded, exported, imported, roasted, ground, and brewed. A single cup of coffee represents 6-8 months of growing, multiple processing steps across several continents, and the labor of dozens of people. When you roast your own coffee, you are participating in one of the final and most transformative steps of that journey."""
    },
    {
        "id": "fun-002",
        "domain": "fun_facts",
        "title": "The Legend of Kaldi and the Dancing Goats",
        "content": """The most famous origin story of coffee comes from Ethiopia around 850 AD. According to legend, a goat herder named Kaldi noticed that his goats became unusually energetic and danced around after eating the bright red cherries from a particular bush. Curious, Kaldi tried the cherries himself and felt a surge of energy. He brought the cherries to a local monastery, where a monk dismissed them as the devil's work and threw them into a fire. The aroma that rose from the roasting cherries was so enticing that the monks raked the beans from the embers, crushed them, and dissolved them in hot water, creating the first cup of coffee. Whether or not any of this actually happened is debatable, but what is true is that coffee originated in Ethiopia and was first cultivated and traded through Yemen in the 15th century before spreading to the rest of the world. By the 1600s, coffeehouses had become centers of social, intellectual, and political life across Europe and the Middle East."""
    },
    {
        "id": "fun-003",
        "domain": "fun_facts",
        "title": "Processing Methods: Washed vs Natural vs Honey",
        "content": """After coffee cherries are picked, the seeds (beans) need to be separated from the fruit and dried. How this is done has a dramatic effect on flavor. WASHED (WET) PROCESS: The cherry skin and fruit are mechanically removed, then the beans are fermented in water tanks for 12-72 hours to dissolve the remaining mucilage (sticky fruit layer), then washed clean and dried. Washed coffees are clean, bright, and transparent, letting you taste the bean's inherent character. Most Central American, Colombian, Kenyan, and some Ethiopian coffees are washed. NATURAL (DRY) PROCESS: The whole cherry is dried intact in the sun for 2-4 weeks, and the dried fruit is removed later. During drying, the bean sits inside the fermenting fruit, absorbing sugars and flavor compounds. Natural processed coffees are fruity, sweet, heavy-bodied, and sometimes boozy or fermented. Many Ethiopian and Brazilian coffees are natural process. HONEY PROCESS: A hybrid. The skin is removed but some or all of the mucilage is left on the bean during drying. The amount of mucilage left determines the designation: white honey (least), yellow, red, and black honey (most). Honey processed coffees have more body and sweetness than washed but more clarity than naturals. Popular in Costa Rica, El Salvador, and Brazil."""
    },
    {
        "id": "fun-004",
        "domain": "fun_facts",
        "title": "Arabica vs Robusta",
        "content": """There are over 120 species of coffee, but only two matter commercially: Arabica and Robusta. ARABICA (Coffea arabica) accounts for about 60-70% of world production. It is considered the higher-quality species, grown at higher altitudes (600-2,200 meters), with more complex sugars and acids. Arabica has lower caffeine content (1.2-1.5%) and is more susceptible to disease and pests. All specialty coffee is Arabica. When you buy single-origin beans for home roasting, you are buying Arabica. ROBUSTA (Coffea canephora) accounts for about 30-40% of production. It grows at lower altitudes (0-800 meters), is hardier and more disease-resistant, has nearly double the caffeine (2.2-2.7%), and produces a stronger, more bitter, less complex cup. Robusta is used in instant coffee, commercial blends, and Italian-style espresso blends (where a small percentage adds body, crema, and a caffeine kick). Robusta gets a bad reputation, but high-quality robusta (called Fine Robusta) is gaining recognition. For home roasters, you will almost exclusively be roasting Arabica beans."""
    },
    {
        "id": "fun-005",
        "domain": "fun_facts",
        "title": "Decaf: How It Works",
        "content": """Decaffeination happens to green beans before roasting. There are four main methods: SWISS WATER PROCESS: Beans are soaked in hot water to dissolve caffeine. The water is passed through activated charcoal filters that trap caffeine molecules but let flavor compounds through. The flavor-charged water (now caffeine-free) is used to soak the next batch, so flavor loss is minimized. No chemicals used. This is the most common method for specialty decaf. CO2 PROCESS: Liquid CO2 is used as a solvent at high pressure. It selectively dissolves caffeine while leaving most other compounds intact. Produces very clean results but is expensive. METHYLENE CHLORIDE (MC): Beans are soaked in a chemical solvent that bonds to caffeine. The solvent is then removed. The FDA considers this safe because the solvent evaporates well below roasting temperatures, but many specialty roasters avoid it for marketing reasons. ETHYL ACETATE (EA): Also called sugarcane process because EA can be derived from sugarcane. Similar to MC process but considered more natural. For home roasters, look for Swiss Water or CO2 decaf beans. They retain the most flavor. Decaf beans roast slightly faster than caffeinated beans of the same origin because the decaffeination process makes them more porous."""
    },

    # ═══════════════════════════════════════════════════════════════
    # DOMAIN 8: BEGINNER ROADMAP
    # ═══════════════════════════════════════════════════════════════

    {
        "id": "beginner-001",
        "domain": "beginner",
        "title": "Your First Home Roast: Step by Step",
        "content": """Here is how to roast your first batch of coffee at home. You need: green coffee beans (start with a forgiving Brazilian or Colombian from Sweet Maria's or Happy Mug), a hot air popcorn popper (or a skillet), and a metal colander for cooling. STEP 1: Set up outside or in a well-ventilated area. Roasting produces smoke and chaff. STEP 2: Measure about 1/2 cup (80-100g) of green beans. STEP 3: Turn on the popper and add the beans. They should start circulating in the hot air. If they are not moving, you have added too many. STEP 4: Watch and listen. The beans will go from green to yellow (2-3 min), yellow to light brown (4-5 min), and then you will hear first crack, a popping sound like popcorn (5-6 min). STEP 5: Decide when to stop. For your first roast, let first crack complete (the popping becomes less frequent) and then dump the beans immediately. This gives you a City roast, medium-light. STEP 6: Pour the beans into the colander and shake them while a fan blows air through to cool them as fast as possible. They should be cool to touch within 3-4 minutes. STEP 7: Wait. Let the beans rest in an open container (not sealed, CO2 needs to escape) for 12-24 hours minimum, ideally 3-5 days. Then grind, brew, and taste what you made. Congratulations. You just roasted coffee. It will not be perfect but it will be yours, and it will be fresher than anything you can buy in a store."""
    },
    {
        "id": "beginner-002",
        "domain": "beginner",
        "title": "First Five Roasts: What to Learn",
        "content": """Your first five roasts should each teach you something specific. Do not try to optimize everything at once. ROAST 1: Just do it. Follow the step-by-step guide and complete a roast from start to finish. The goal is not perfection. It is completion. ROAST 2: Listen. Focus on hearing first crack clearly. Note when it starts, when it peaks, and when it tapers off. This is the most important skill in roasting. ROAST 3: Compare roast levels. Split your beans into two batches. Roast the first to just after first crack starts (light). Roast the second to when first crack is fully done and 30 seconds beyond (medium). Brew both and taste the difference side by side. ROAST 4: Try a different origin. If you started with Brazilian, try an Ethiopian or Colombian. Notice how different beans behave differently under the same conditions: different crack timing, different color development, different aromas during roasting. ROAST 5: Try going darker. Take a batch to the beginning of second crack (listen for the quieter, crackly sound). This is Full City+, the edge of dark roast territory. Taste it and decide if you prefer this or your earlier lighter roasts. After these five roasts, you will have a basic understanding of the roasting process, your equipment, and your own taste preferences. From here, you can start refining."""
    }
]
