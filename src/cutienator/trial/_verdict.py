"""Verdict is what a Judge found when it heard one Trial."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import signal
from typing import TYPE_CHECKING

from worktoy.waitaminute import MissingVariable

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import List, Optional, Tuple

  Run = Tuple[Optional[int], str, str]


class Verdict:
  """
  What a 'Judge' found when it heard one 'Trial': how the C++ half and
  the Python half each ended, what each printed, and whether they agree.

    verdict = judge.hear(trial)
    verdict.passed()      # True when the three below are all True
    verdict.ranInCpp()    # the C++ half ran to its end
    verdict.functions()   # the Python half ran to its end
    verdict.isAsInCpp()   # both halves printed the same lines
    print(verdict)        # the whole story, in words

  Terms
  -----

  - A half is one of the two programs written from a trial: the C++ one,
    run against Qt itself, or the Python one, run against cutienator.
  - A return code is the number a program ends with. 0 means it ran to
    its end. A negative number means it was killed, as -6 when Qt
    aborts and -11 when a bad address is touched. None means it had to
    be stopped for taking too long.

  You provide
  -----------

  Nothing. A 'Judge' fills a verdict in, through 'setTrialName',
  'setCppRun' and 'setPythonRun'. You read it.

  What to expect
  --------------

  - A half that crashed is a verdict that did not pass, never an
    exception: asking how it went is always safe.
  - 'isAsInCpp' is True only when both halves ran to their end. A half
    that died halfway is not 'the same' as anything.
  - Reading a verdict a 'Judge' has not filled in raises
    'MissingVariable'.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def _describeEnd(returnCode: Optional[int]) -> str:
    """Says in words how a program with that return code ended."""
    if returnCode is None:
      return 'was stopped for taking too long'
    if returnCode == 0:
      return 'ran to its end'
    if returnCode < 0:
      try:
        name = signal.Signals(-returnCode).name
      except ValueError:
        name = 'signal %d' % -returnCode
      return 'was killed (%s)' % name
    return 'ended with an error (return code %d)' % returnCode

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables

  #  Fallback Variables

  #  Private Variables
  __trial_name__ = None  # type: Optional[str]
  __cpp_run__ = None  # type: Optional[Run]
  __python_run__ = None  # type: Optional[Run]

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getTrialName(self) -> str:
    """
    Gives the name of the trial this verdict is about.

    Filled in by the 'Judge', from the trial's own name.

    Raises
    ------

    MissingVariable
      No 'Judge' has filled this verdict in.
    """
    if self.__trial_name__ is None:
      raise MissingVariable(self, '__trial_name__', str)
    return self.__trial_name__

  def getCppRun(self) -> Run:
    """
    Gives how the C++ half went.

    Filled in by the 'Judge', after it ran the C++ program.

    Returns
    -------

    Run
      A 'Tuple[Optional[int], str, str]': the return code, what the
      program printed, and what it complained about.

    Raises
    ------

    MissingVariable
      No 'Judge' has filled this verdict in.
    """
    if self.__cpp_run__ is None:
      raise MissingVariable(self, '__cpp_run__', tuple)
    return self.__cpp_run__

  def getPythonRun(self) -> Run:
    """
    Gives how the Python half went.

    Filled in by the 'Judge', after it ran the Python program.

    Returns
    -------

    Run
      A 'Tuple[Optional[int], str, str]': the return code, what the
      program printed, and what it complained about. A Python error
      shows here as return code 1 with the traceback as the complaint.

    Raises
    ------

    MissingVariable
      No 'Judge' has filled this verdict in.
    """
    if self.__python_run__ is None:
      raise MissingVariable(self, '__python_run__', tuple)
    return self.__python_run__

  def getDifferences(self) -> List[Tuple[int, str, str]]:
    """
    Gives the lines the two halves printed differently.

    Worked out from what the 'Judge' filled in.

    Returns
    -------

    List[Tuple[int, str, str]]
      One entry per differing line: its number counted from 1, what C++
      printed there, and what Python printed there. A line only one half
      printed shows as '' for the other. It is empty when they agree.
    """
    cppLines = self.getCppRun()[1].splitlines()
    pythonLines = self.getPythonRun()[1].splitlines()
    differences = []
    for index in range(max(len(cppLines), len(pythonLines))):
      cppLine = cppLines[index] if index < len(cppLines) else ''
      pythonLine = pythonLines[index] if index < len(pythonLines) else ''
      if cppLine != pythonLine:
        differences.append((index + 1, cppLine, pythonLine))
    return differences

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setTrialName(self, trialName: str) -> None:
    """Called by the 'Judge' with the name of the trial it heard."""
    self.__trial_name__ = trialName

  def setCppRun(
      self,
      returnCode: Optional[int],
      printed: str,
      complained: str,
  ) -> None:
    """
    Called by the 'Judge' with how the C++ half went.

    Parameters
    ----------

    returnCode : Optional[int]
      What the program ended with, or None when it was stopped for
      taking too long.

    printed : str
      Everything the program printed.

    complained : str
      Everything the program wrote to its error stream.
    """
    self.__cpp_run__ = (returnCode, printed, complained)

  def setPythonRun(
      self,
      returnCode: Optional[int],
      printed: str,
      complained: str,
  ) -> None:
    """
    Called by the 'Judge' with how the Python half went.

    Parameters
    ----------

    returnCode : Optional[int]
      What the program ended with, or None when it was stopped for
      taking too long.

    printed : str
      Everything the program printed.

    complained : str
      Everything the program wrote to its error stream.
    """
    self.__python_run__ = (returnCode, printed, complained)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def __str__(self) -> str:
    """Tells the whole verdict in words, over several lines."""
    cppCode, cppPrinted, cppComplained = self.getCppRun()
    pythonCode, _, pythonComplained = self.getPythonRun()
    lines = [
        '%s  %s' % ('PASSED' if self.passed() else 'FAILED',
                    self.getTrialName()),
        '  the C++ half %s' % self._describeEnd(cppCode),
        '  the Python half %s' % self._describeEnd(pythonCode),
    ]
    if cppComplained.strip():
      lines.append('  C++ complained:')
      lines.extend('    %s' % s for s in cppComplained.splitlines())
    if pythonComplained.strip():
      lines.append('  Python complained:')
      lines.extend('    %s' % s for s in pythonComplained.splitlines())
    if self.isAsInCpp():
      count = len(cppPrinted.splitlines())
      lines.append('  both printed the same %d lines' % count)
    elif self.ranInCpp() and self.functions():
      lines.append('  they printed differently:')
      for number, cppLine, pythonLine in self.getDifferences():
        lines.append('    line %d, C++   : %s' % (number, cppLine))
        lines.append('    line %d, Python: %s' % (number, pythonLine))
    return '\n'.join(lines)

  def __repr__(self) -> str:
    """Gives one line: passed or failed, and the name of the trial."""
    if self.__trial_name__ is None:
      return '<%s not filled in yet>' % type(self).__name__
    word = 'passed' if self.passed() else 'failed'
    clsName = type(self).__name__
    return "<%s: '%s' %s>" % (clsName, self.__trial_name__, word)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def ranInCpp(self) -> bool:
    """
    Says whether the C++ half ran to its end.

    When this is False the trial itself is at fault, not cutienator:
    the steps ask Qt for something Qt does not do.
    """
    return self.getCppRun()[0] == 0

  def functions(self) -> bool:
    """
    Says whether the Python half ran to its end: the cute classes exist,
    took the calls, and nothing crashed.
    """
    return self.getPythonRun()[0] == 0

  def isAsInCpp(self) -> bool:
    """
    Says whether Python behaved as C++ did: both halves ran to their
    end, and printed the same lines.
    """
    if not (self.ranInCpp() and self.functions()):
      return False
    return self.getCppRun()[1] == self.getPythonRun()[1]

  def passed(self) -> bool:
    """Says whether the trial passed: 'isAsInCpp' is True."""
    return self.isAsInCpp()
