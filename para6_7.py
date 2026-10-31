import warnings

warnings.simplefilter("ignore", SyntaxWarning)
warnings.simplafilter("always", ImportWarning)

warnings.warn("Warning, no code here", SyntaxWarning)
warnings.warn("Warning< module not import", ImportWarning)