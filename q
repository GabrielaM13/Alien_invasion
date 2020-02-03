[35mdiff --git a/settings.py b/settings.py[m
[35mindex 28f63cf..38d4599 100644[m
[35m--- a/settings.py[m
[35m+++ b/settings.py[m
[36m@@ -25,9 +25,12 @@[m [mclass Settings:[m
         self.alien_down_speed = 10 [m
 [m
         # How quickly the game speeds up[m
[31m-        self.speed_up_scale = 1.5[m
[32m+[m[32m        self.speed_up_scale = 2.0[m
         self.initialize_dynamic_settings()[m
 [m
[32m+[m[32m        # How quickly the alien point values increase[m
[32m+[m[32m        self.score_scole = 1.5[m
[32m+[m
     def _get_relative_path(self, path):[m
         base_path = os.path.dirname(__file__)[m
         relative_path = os.path.join(base_path, path)[m
[36m@@ -46,7 +49,8 @@[m [mclass Settings:[m
         self.alien_points = 50[m
 [m
     def increase_speed(self):[m
[31m-        """ Increade speed settings """[m
[32m+[m[32m        """ Increade speed settings and alien point values """[m
         self.ship_speed *= self.speed_up_scale[m
         self.bullet_speed *= self.speed_up_scale[m
[31m-        self.alien_speed *= self.speed_up_scale[m
\ No newline at end of file[m
[32m+[m[32m        self.alien_speed *= self.speed_up_scale[m
[32m+[m[32m        self.alien_points = int(self.alien_points * self.score_scole)[m
\ No newline at end of file[m
