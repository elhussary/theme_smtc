{
    "name": "SMTC Theme",
    "summary": "Professional Swiss Manufacturing Theme",
    "description": "Precision engineering corporate theme for Swiss-type CNC manufacturing.",
    "version": "1.0",
    "category": "Theme/Website",
    "sequence": 100,
    "author": "Soft Mission",
    "license": "LGPL-3",
    "depends": ["website","theme_common"],
    "data": [
        "data/generate_primary_template.xml",
        "data/ir_asset.xml",

        # Snippets
        "views/snippets_registry.xml",
        "views/snippets/s_smtc_hero.xml",
        "views/snippets/s_smtc_badges.xml",
        "views/snippets/s_smtc_highlights.xml",
        "views/snippets/s_smtc_industries.xml",
        "views/snippets/s_smtc_cta.xml",
        "views/snippets/s_smtc_stats.xml",
        "views/snippets/s_smtc_about_history.xml",
        "views/snippets/s_smtc_mission_vision.xml",
        "views/snippets/s_smtc_capabilities.xml",
        "views/snippets/s_smtc_quality.xml",
        "views/snippets/s_smtc_contact_info.xml",
        "views/snippets/s_smtc_quote_form.xml",

        # Pages
        "views/pages/quote.xml",
        "views/pages/about.xml",
        "views/pages/capabilities.xml",
        "views/pages/industries.xml",
        "views/pages/contact.xml",
        "views/layout.xml",
    ],
    "images": ["static/description/cover.png"],
    "configurator_snippets": {
        "homepage": ["s_smtc_hero", "s_smtc_badges", "s_smtc_highlights", "s_smtc_industries", "s_smtc_cta"],
    },
    "application": False,
    "installable": True,
}
