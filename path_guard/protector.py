import os
from pathlib import Path

from .signatures import TRAV_HARD, TRAV_PATHS



class SafePathGuard:
    '''
    A simple library to block Path Traversal and LFI attacks.
    It forces all paths to stay inside one main folder.
    '''

    def __init__(self, base_directory: str) -> None:
        '''
        Initializes the guard with a base directory.
        All paths must stay inside this folder!!!
        '''
        self.base_dir = Path(base_directory).resolve()

    def is_safe_path(self, user_input: str) -> bool:
        '''
        Validates whether the user-supplied path is safe and stays within boundaries.
        '''

        # BASE analysis
        if not user_input or not isinstance(user_input, str):
            return False
        
        # Signature analysis
        if TRAV_HARD.search(user_input) or TRAV_PATHS.search(user_input):
            return False

        try:
            # 1. Anti-absolut, remove / \ slashes
            safe_input = user_input.lstrip('/\\')
    
            # 2. Combine paths and resolve all '...' and symlinks
            requested_path = (self.base_dir / safe_input).resolve()
    
            # 3. Check id final path is inside to base directory
            return requested_path.is_relative_to(self.base_dir)
            
        except (OSError, RuntimeError, Exception):
            # Reject the path if any OS resolution error
            return False