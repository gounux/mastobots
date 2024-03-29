import random
from typing import Tuple

from botbeings import SuperBotBeing

ACTIONS = [
    "is looking for a new",
    "is hiring a new",
    "is offering a position as a",
    "is opening a position as a",
]

COMPANY_A = [
    "Boston",
    "McKinsey",
    "Kearney",
    "Allen",
    "Hamilton",
    "Bridgespan",
    "Clarkston",
    "Massachusetts",
    "Chicago",
    "Bain",
    "Deloitte",
    "Lazarre",
    "Keystone",
    "Müller&Müller",
    "Dupond&Dupond",
    "London",
]

COMPANY_B = [
    "Consulting",
    "Business",
    "Lead",
    "Engineering",
    "Technology",
    "Blockchain",
    "Management",
    "Systems",
    "Incorporated",
    "Intelligence",
    "Economic",
    "Sourcing",
    "Talent",
    "Insight",
]

COMPANY_C = [
    "Group",
    "Network",
    "Associates",
    "Firm",
    "Office",
    "Partners",
    "Consultants",
    "Advisors",
    "Incorporated",
    "Company",
    "E-Services",
    "E-Businesses",
    "Strategies",
    "Strategists",
    "Vision",
    "Advances",
]

JOBTITLE_A = [
    "Lead",
    "Senior",
    "Direct",
    "Corporate",
    "Dynamic",
    "Future",
    "Product",
    "National",
    "Regional",
    "District",
    "Central",
    "Global",
    "Relational",
    "Customer",
    "Investor",
    "Dynamic",
    "International",
    "Legacy",
    "Forward",
    "Interactive",
    "Internal",
    "Human",
    "Chief",
    "Principal",
]

JOBTITLE_B = [
    "Solutions",
    "Program",
    "Brand",
    "Security",
    "Research",
    "Marketing",
    "Directives",
    "Implementation",
    "Integration",
    "Functionality",
    "Response",
    "Paradigm",
    "Tactics",
    "Identity",
    "Markets",
    "Group",
    "Resonance",
    "Applications",
    "Optimization",
    "Operations",
    "Infrastructure",
    "Intranet",
    "Communications",
    "Web",
    "Branding",
    "Quality",
    "Assurance",
    "Impact",
    "Mobility",
    "Ideation",
    "Data",
    "Creative",
    "Configuration",
    "Accountability",
    "Interactions",
    "Factors",
    "Usability",
    "Metrics",
    "Team",
    "Transformation",
]

JOBTITLE_C = [
    "Supervisor",
    "Associate",
    "Executive",
    "Liason",
    "Officer",
    "Manager",
    "Engineer",
    "Specialist",
    "Director",
    "Coordinator",
    "Administrator",
    "Architect",
    "Analyst",
    "Designer",
    "Planner",
    "Synergist",
    "Orchestrator",
    "Technician",
    "Developer",
    "Producer",
    "Consultant",
    "Assistant",
    "Facilitator",
    "Agent",
    "Representative",
    "Strategist",
]

MISSION_ADVERBS = [
    "appropriately",
    "assertively",
    "authoritatively",
    "collaboratively",
    "compellingly",
    "competently",
    "completely",
    "continually",
    "conveniently",
    "credibly",
    "distinctively",
    "dramatically",
    "dynamically",
    "efficiently",
    "energistically",
    "enthusiastically",
    "fungibly",
    "globally",
    "holisticly",
    "interactively",
    "intrinsically",
    "monotonectally",
    "objectively",
    "phosfluorescently",
    "proactively",
    "professionally",
    "progressively",
    "quickly",
    "rapidiously",
    "seamlessly",
    "synergistically",
    "uniquely",
]

MISSION_VERBS = [
    "actualize",
    "administrate",
    "aggregate",
    "architect",
    "benchmark",
    "brand",
    "build",
    "cloudify",
    "communicate",
    "conceptualize",
    "coordinate",
    "create",
    "cultivate",
    "customize",
    "deliver",
    "deploy",
    "develop",
    "dinintermediate disseminate",
    "drive",
    "embrace",
    "e-enable",
    "empower",
    "enable",
    "engage",
    "engineer",
    "enhance",
    "envisioneer",
    "evisculate",
    "evolve",
    "expedite",
    "exploit",
    "extend",
    "fabricate",
    "facilitate",
    "fashion",
    "formulate",
    "foster",
    "generate",
    "grow",
    "harness",
    "impact",
    "implement",
    "incentivize",
    "incept",
    "incubate",
    "initiate",
    "innovate",
    "integrate",
    "iterate",
    "leverage existing",
    "leverage other's",
    "maintain",
    "matrix",
    "maximize",
    "mesh",
    "monetize",
    "morph",
    "myocardinate",
    "negotiate",
    "network",
    "optimize",
    "onboard",
    "orchestrate",
    "parallel task",
    "plagiarize",
    "pontificate",
    "predominate",
    "procrastinate",
    "productivate",
    "productize",
    "promote",
    "provide access to",
    "pursue",
    "recaptiualize",
    "reconceptualize",
    "redefine",
    "re-engineer",
    "reintermediate",
    "reinvent",
    "repurpose",
    "restore",
    "revolutionize",
    "right-shore",
    "scale",
    "seize",
    "simplify",
    "strategize",
    "streamline",
    "supply",
    "syndicate",
    "synergize",
    "synthesize",
    "target",
    "transform",
    "transition",
    "underwhelm",
    "unleash",
    "utilize",
    "visualize",
    "whiteboard",
]

MISSION_ADJECTIVES = [
    "24/7",
    "24/365",
    "accurate",
    "adaptive",
    "agile",
    "alternative",
    "an expanded array of",
    "assertive",
    "B2B",
    "B2C",
    "backend",
    "backward-compatible",
    "best-of-breed",
    "bijective",
    "bleeding-edge",
    "bricks-and-clicks",
    "business",
    "clicks-and-mortar",
    "client-based",
    "client-centered",
    "client-centric",
    "client-focused",
    "cloud-based",
    "cloud-centric",
    "cloudified",
    "collaborative",
    "compelling",
    "competitive",
    "cooperative",
    "corporate",
    "cost effective",
    "covalent",
    "cross functional",
    "cross-media",
    "cross-platform",
    "cross-unit",
    "customer directed",
    "customer minded",
    "customized",
    "cutting-edge",
    "data-minded",
    "data-focused",
    "distinctive",
    "distributed",
    "diverse",
    "dynamic",
    "e-business",
    "economically sound",
    "effective",
    "efficient",
    "elastic",
    "emerging",
    "empowered",
    "enabled",
    "end-to-end",
    "enterprise",
    "enterprise-wide",
    "equity invested",
    "error-free",
    "ethical",
    "excellent",
    "exceptional",
    "extensible",
    "extensive",
    "flexible",
    "focused",
    "frictionless",
    "front-end",
    "fully researched",
    "fully tested",
    "functional",
    "functionalized",
    "fungible",
    "future-proof",
    "global",
    "go forward",
    "goal-oriented",
    "granular",
    "high standards in",
    "high-payoff",
    "hyperscale",
    "high-quality",
    "highly efficient",
    "holistic",
    "human centered",
    "human focused",
    "impactful",
    "inexpensive",
    "innovative",
    "insightful",
    "installed base",
    "integrated",
    "interactive",
    "interdependent",
    "intermandated",
    "interoperable",
    "intuitive",
    "just in time",
    "key",
    "lead",
    "leading-edge",
    "lean",
    "leveraged",
    "long-term high-impact",
    "low-risk high-yield",
    "magnetic",
    "maintainable",
    "market positioning",
    "market-driven",
    "mission-critical",
    "multidisciplinary",
    "multifunctional",
    "multimedia based",
    "next-generation",
    "on-demand",
    "one-to-one",
    "optimal",
    "orthogonal",
    "out-of-the-box",
    "pandemic",
    "parallel",
    "performance based",
    "plug-and-play",
    "premier",
    "premium",
    "principle-centered",
    "proactive",
    "process-centric",
    "professional",
    "progressive",
    "prospective",
    "quality",
    "real-time",
    "reliable",
    "resource-sucking",
    "resource-maximizing",
    "resource-leveling",
    "revolutionary",
    "robust",
    "scalable",
    "seamless",
    "stand-alone",
    "standardized",
    "standards compliant",
    "state of the art",
    "sticky",
    "strategic",
    "superior",
    "sustainable",
    "synergistic",
    "tactical",
    "team building",
    "team driven",
    "technically sound",
    "timely",
    "top-line",
    "transparent",
    "turnkey",
    "ubiquitous",
    "unique",
    "user-centric",
    "user friendly",
    "value-added",
    "vertical",
    "viral",
    "virtual",
    "visionary",
    "web-enabled",
    "wireless",
    "world-class",
    "worldwide",
]

MISSION_NOUNS = [
    "action items",
    "adoption",
    "AI",
    "alignments",
    "applications",
    "architectures",
    "bandwidth",
    "benefits",
    "best practices",
    "blockchain",
    "catalysts for change",
    "channels",
    "clouds",
    "collaboration and idea-sharing",
    "communities",
    "content",
    "convergence",
    "core competencies",
    "customer service",
    "data",
    "deliverables",
    "e-business",
    "e-commerce",
    "e-markets",
    "e-platforms",
    "e-tailers",
    "e-services",
    "experiences",
    "expertise",
    "functionalities",
    "fungibility",
    "growth strategies",
    "human capital",
    "ideas",
    "imperatives",
    "infomediaries",
    "information",
    "infrastructures",
    "initiatives",
    "innovation",
    "inputs",
    "intellectual capital",
    "interfaces",
    "internal or 'organic' sources",
    "KPI",
    "leadership",
    "leadership skills",
    "manufactured products",
    "markets",
    "materials",
    "meta-services",
    "methodologies",
    "methods of empowerment",
    "metrics",
    "mindshare",
    "models",
    "networks",
    "niches",
    "niche markets",
    "nosql",
    "opportunities",
    "outputs",
    "'outside the box' thinking",
    "outsourcing",
    "paradigms",
    "partnerships",
    "platforms",
    "portals",
    "potentialities",
    "process improvements",
    "processes",
    "products",
    "quality vectors",
    "relationships",
    "resources",
    "results",
    "ROI",
    "scenarios",
    "schemas",
    "scrums",
    "services",
    "solutions",
    "sources",
    "sprints",
    "strategic theme areas",
    "storage",
    "supply chains",
    "synergy",
    "systems",
    "technologies",
    "technology",
    "testing procedures",
    "total linkage",
    "users",
    "value",
    "vortals",
    "web-readiness",
    "web services",
    "wins",
    "virtualization",
]

TOOLS = [
    "Windowbe",
    "Dildows",
    "MS Office 1664",
    "MS Office 420",
    "MS Office Processional",
    "MS PowpowPoint",
    "MS Axcel",
    "MS Weird",
    "MS Excess",
    "MS Meats",
    "MS Visual Ouzo",
    "CanetteVa",
    "CanetteVa Flatform",
    "CanetteVa Floud",
    "Adaube OutDesign",
    "Adaube Filloustrator",
    "Adaube Creative Floud",
    "Adaube Processional",
    "Trellol",
    "Failsforce",
    "Failsforce Flatform",
    "Failsforce MyKarting Cloud",
    "Failsforce Data MyKarting",
    "Failsforce Floud Processional",
    "Failsforce Lightning Floud",
    "Failsforce Productivity Floud",
    "SPA",
    "Slakatack",
    "PrordWess",
    "Gogole",
    "Gogole Flatform",
    "Gogole Floud",
    "Gogole for Processionals",
    "Azamone Zeb Vertices",
    "Azamone Zeb Vertices Flatform",
    "Azamone Zeb Vertices Floud",
    "Azamone Zeb Vertices Karting Services",
    "PasSage",
    "J'ira",
    "J'ira Flatform",
    "J'ira Offline Floud",
    "J'ira Processional MyKarting",
    "ZoomZoomZen",
    "ZoomZoomZen Processional",
    "Jean-Marc GIS",
    "Jean-Marc GIS Flatform",
    "Jean-Marc GIS Floud",
    "Jean-Marc GIS KartingPlace",
    "Jean-Marc GIS Tata Science",
    "Jean-Marc GIS Offline Cloud",
]

MAIL_USERS = [
    "jobs",
    "careers",
    "sourcing",
    "hiring",
    "recruitments",
]

MAIL_DOMAINS = [
    "com",
    "business",
    "mgmt",
    "insights",
    "strat",
    "bs",
    "shop",
    "in",
]

TOOT_TEMPLATE = """📢 {initials} ({company}) {action} {jobtitle} !

👉 Your missions:

⚡ {mission_1}
⚡ {mission_2}
⚡ {mission_3}
⚡ {mission_4}

📝 {xp} years x.p.
🙋 {qualities}
💻 {tools}

👉 ✉️ {mailuser}@{domain}.{maildomain}

#jobs #career"""


class JobsBotBeing(SuperBotBeing):
    def run(self, action: str = "default") -> None:
        toot = self.generate_toot(self.max_toot_length)
        if not self.dryrun:
            self.mastodon.status_post(toot)
        self.logger.info(f'Tooted: "{toot}" (length: {len(toot)})')

    def generate_toot(self, max_length: int) -> str:
        company, initials = self.generate_company()
        jobtitle = self.generate_jobtitle()

        toot = TOOT_TEMPLATE.format(
            initials=initials,
            company=company,
            action=random.choice(ACTIONS),
            jobtitle=jobtitle,
            mission_1=self.generate_mission(),
            mission_2=self.generate_mission(),
            mission_3=self.generate_mission(),
            mission_4=self.generate_mission(),
            xp=random.choice(["3+", "5+", "8+", "25+"]),
            qualities=", ".join(random.sample(MISSION_ADJECTIVES, k=4)),
            tools=", ".join(random.sample(TOOLS, k=4)),
            mailuser=random.choice(MAIL_USERS),
            domain=initials.lower().replace(" ", "-"),
            maildomain=random.choice(MAIL_DOMAINS),
        )
        if len(toot) > max_length:
            return self.generate_toot(max_length)
        return toot

    @staticmethod
    def generate_company() -> Tuple[str, str]:
        a, b, c = (
            random.choice(COMPANY_A),
            random.choice(COMPANY_B),
            random.choice(COMPANY_C),
        )
        return f"{a} {b} {c}", f"{a[0]}{b[0]}{c[0]}"

    @staticmethod
    def generate_jobtitle() -> str:
        return f"{random.choice(JOBTITLE_A)} {random.choice(JOBTITLE_B)} {random.choice(JOBTITLE_C)}"

    @staticmethod
    def generate_mission() -> str:
        return f"{random.choice(MISSION_ADVERBS)} {random.choice(MISSION_VERBS)} {random.choice(MISSION_ADJECTIVES)} {random.choice(MISSION_NOUNS)}"
