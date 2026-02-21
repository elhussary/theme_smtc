from odoo import models

class ThemeUtils(models.AbstractModel):
    _inherit = 'theme.utils'

    def _theme_theme_smtc_post_copy(self, mod):
        
        # self.enable_view('theme_smtc.smtc_header')
        self.enable_view('theme_smtc.smtc_footer')
        
        # # ضبط الألوان أوتوماتيك لليوزر
        # self.set_theme_variables(mod, {
        #     'color-palettes-name': 'smtc-palette-1',
        #     'font': 'Inter',
        # })