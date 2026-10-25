import re


# ==============================================================================
# PATH TRAVERSAL & OBFUSCATION (encoding, unicode)
# ==============================================================================
TRAV_HARD = re.compile(
    r"("
    r"\.\./|\.\.\\|"                     # ../ ..\
    r"%2e%2e|%252e%252e|"               # URL-encode и Double URL-encode
    r"\.\.%2f|\.\.%5c|%2e%2e%2f|%2e%2e%5c|" # / and .
    r"%c0%ae%c0%ae|%e0%80%ae%e0%80%ae|" # Overlong UTF-8 for .
    r"%c1%1c|%c0%af|%c1%9c|%c0%5c|"     # Overlong UTF-8 for (/,\)
    r"%uff0e|%uff0f|%uff3c|"             # Full-width Unicode (., /, \)
    r"\u2215|\u2044|\u2571|\u29f8|"     # Math and Unicode-/
    r"\u2216|\u2572|"                   # Unicode reverse /
    r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}" # Block IP
    r")", 
    re.I
)


# ==============================================================================
# SENSITIVE PATHS & CONFIGURATIONS (file, log, backup)
# ==============================================================================
TRAV_PATHS = re.compile(
    r"("
    # Linux/Unix system files and directory
    r"/etc/(passwd|shadow|group|hosts|issue|hostname|resolv\.conf|fstab|modules)|"
    r"/etc/cron\.|/etc/init\.d/|/etc/nginx/|/etc/apache2/|/etc/ssh/|"
    r"/proc/(self|net|sys|mounts|partitions|version|cmdline|environ)|"
    r"/var/log/(nginx|apache2|httpd|auth|syslog|messages|secure)|"
    r"/root/\.(bash_|ssh|git|aws|config)|/home/[^/]+/\.(bash_|ssh|git|aws)|"
    r"/dev/(null|stdout|stderr|zero|urandom)|"
    
    # Windows system files (catalogs Windows, System32, SysWOW64)
    r"(boot|win)\.ini|\bntuser\.dat|\bSAM\b|\bSYSTEM\b|\bSECURITY\b|"
    r"[a-z]:\\windows\\|[a-z]:\\winnt\\|system32|syswow64|"
    r"/windows/win\.ini|/windows/system32|"
    
    # Secrets, tokens, conf frimework
    r"\.env(\.local|\.development|\.production|\.bak|\.old)?\b|"
    r"(config|settings|database|credentials|secrets?|token|shadow|access_key)\.(yml|yaml|json|ini|php|xml|bak)|"
    r"\b(wp-config|config\.inc)\.php|"
    r"\.(aws/credentials|dockercfg|npmrc|gitconfig)\b|"
    
    # Backup, logs, DB
    r"\.(bak|old|backup|temp|tmp|swp|git|svn|hg|bz2|gz|tar|zip|rar|sql|db|sqlite|log)\b|"
    
    # CTF security A/D [TEST]
    r"flag(\.txt)?\b|\bfl4g\b|\bctf\b|[{}]"

    # Web / another
    r"WEB-INF/(web\.xml|classes|lib)|META-INF/|"
    r"\.htaccess|\.htpasswd"
    r")",
    re.I
)





# Joomla / Drupal......