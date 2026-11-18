"""
The 'cutienator.trial' package confirms that a cute class is built
correctly, functions correctly, and behaves as its C++ original does.

A 'Trial' is one test written once as a list of steps. A 'Judge' runs it
twice, in C++ against Qt itself and in Python against cutienator, and
gives a 'Verdict' saying whether the two agree.

  python -m cutienator.trial    builds what is stale, hears every trial
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

from ._trial import Trial
from ._verdict import Verdict
from ._judge import Judge
from ._q_object_trials import qObjectTrials

__all__ = (
    'Trial',
    'Verdict',
    'Judge',
    'qObjectTrials',
)
