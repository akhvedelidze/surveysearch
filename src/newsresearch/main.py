#!/usr/bin/env python
import sys
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
        'topic': 'In the State, have steps been taken to monitor and prevent acts of torture and cruel, inhuman and degrading treatment or punishment ?',
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


