#!/usr/bin/env python
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent))
import warnings

from newsresearch.crew import Newsresearch

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    
    
    inputs = {
        'topic': 'what it interpol activity',
        'country': 'benin'
    }
    
    
    
    inputs_array = [
        {
        'topic': 'Does the State specifically criminalize preparatory acts against domestic targets as standalone offences?',
        'country': 'benin'
        },
        {
        'topic': 'Does the State specifically criminalize preparatory acts against foreign targets as standalone offences?',
        'country': 'benin'
        },
         {
        'topic': 'Does the State specifically criminalize acts taken to aid and abet the commission of terrorist acts against domestic targets as standalone offences?',
        'country': 'benin'
        }
    ]
    
    
    Newsresearch().crew().kickoff(inputs=inputs)
   # Newsresearch().crew().kickoff_for_each(inputs=inputs_array)


