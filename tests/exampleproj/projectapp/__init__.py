# Raise an Exception on evaluation to ensure
# that the apps aren't actually being imported
# anywhere during staticfile processing.
raise IOError("exampleproj.projectapp.__init__ was imported")
