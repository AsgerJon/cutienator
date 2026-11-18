"""Judge runs a Trial in C++ and in Python and gives a Verdict."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from typing import TYPE_CHECKING

from worktoy.utilities import maybe
from worktoy.waitaminute import MissingVariable, TypeException

from ..occult import Build, Header, Rituals, SharedObject
from . import Trial, Verdict

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Dict, Optional, Tuple

  Run = Tuple[Optional[int], str, str]


class Judge:
  """
  Hears a 'Trial': writes its steps out as a C++ program and as a Python
  program, runs both, and gives a 'Verdict' comparing them.

    judge = Judge()
    judge.setWorkFolder('/tmp/trials')
    verdict = judge.hear(trial)
    print(verdict)

  Terms
  -----

  - A half is one of the two programs written from a trial: the C++ one,
    run against Qt itself, or the Python one, run against cutienator.
  - The work folder is where the two programs are written, so that they
    can be read afterwards.

  You provide
  -----------

  - 'setWorkFolder': an existing folder for the programs. Required.
  - 'setTimeout': how many seconds a half may run. Optional; without
    it a half may run for 60 seconds.

  Found for you
  -------------

  - 'getPython': the Python running the judge, which runs the Python
    half too.
  - 'getPackageFolder': where the 'cutienator' package is, so that the
    Python half can import it.
  - 'getQtModule' and 'getQtSharedObject': which Qt header and which Qt
    shared object a class named in a trial needs.

  What to expect
  --------------

  - Each half runs in a process of its own. When C++ kills the Python
    half, the judge lives on, and the death shows in the verdict.
  - 'hear' raises only when a trial cannot be run at all: no work
    folder, a class Qt does not have, or a C++ half that does not
    compile. A half that fails or dies is a verdict, not an exception.
  - Hearing a trial again overwrites the programs written before.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def getFileStem(trial: Trial) -> str:
    """
    Gives the file name the programs of a trial are written under.

    Worked out from the name of the trial: its letters and digits in
    lower case, everything else as one underscore. 'QObject: parent and
    setParent' gives 'qobject_parent_and_setparent'.
    """
    letters = [c.lower() if c.isalnum() else ' ' for c in trial.getName()]
    return '_'.join(''.join(letters).split())

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables

  #  Fallback Variables
  __fallback_timeout__ = 60.

  #  Private Variables
  __work_folder__ = None  # type: Optional[str]
  __timeout_seconds__ = None  # type: Optional[float]

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getWorkFolder(self) -> str:
    """
    Gives the folder the two programs of a trial are written to.

    Provided by you, through 'setWorkFolder'. Nothing fills it in for
    you.

    Raises
    ------

    MissingVariable
      'setWorkFolder' has not been called on this judge.
    """
    if self.__work_folder__ is None:
      raise MissingVariable(self, '__work_folder__', str)
    return self.__work_folder__

  def getTimeout(self) -> float:
    """
    Gives how many seconds a half may run before it is stopped.

    Provided by you, through 'setTimeout'. When you never called it,
    this gives 60.
    """
    return maybe(self.__timeout_seconds__, self.__fallback_timeout__)

  def getPython(self) -> str:
    """
    Gives the Python that runs the Python half of a trial.

    Found for you: it is the Python running this judge, so the Python
    half sees the same worktoy and the same cutienator.
    """
    return sys.executable

  def getPackageFolder(self) -> str:
    """
    Gives the folder holding the 'cutienator' package.

    Found for you, from where this module lies. The Python half is run
    with this folder on its path, so 'from cutienator import QObject'
    finds this very cutienator and no other.
    """
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(os.path.dirname(here))

  def getEnvironment(self) -> Dict[str, str]:
    """
    Gives the environment variables both halves are run with.

    Found for you. They are those of this Python, with three changes:
    'PYTHONPATH' starts with the package folder; Qt is told to write its
    messages to the error stream, where the judge reads them, and not to
    the system journal; and Qt draws off screen unless you already said
    otherwise, so no window appears.
    """
    environment = dict(os.environ)
    paths = [self.getPackageFolder()]
    if environment.get('PYTHONPATH'):
      paths.append(environment['PYTHONPATH'])
    environment['PYTHONPATH'] = os.pathsep.join(paths)
    environment['QT_FORCE_STDERR_LOGGING'] = '1'
    environment.setdefault('QT_QPA_PLATFORM', 'offscreen')
    return environment

  def getQtModule(self, className: str) -> str:
    """
    Gives the part of Qt a class belongs to, as 'QtCore' for 'QObject'.

    Found for you, by 'Header.findQtModule', which looks through Qt's
    header folder for the one part holding a header named as the class.

    Raises
    ------

    LookupError
      No part of Qt has a header of that name, so Qt has no such class;
      or more than one has, which is not expected to happen.
    """
    return Header.findQtModule(className)

  def getQtSharedObject(self, className: str) -> str:
    """
    Gives the Qt shared object holding the working code of a class, as
    '/usr/lib/libQt6Core.so.6' for 'QObject'.

    Found for you, from the part of Qt the class belongs to.

    Raises
    ------

    LookupError
      Qt has no class of that name.

    FileNotFoundError
      The shared object is not where it is expected to be.
    """
    module = self.getQtModule(className)
    name = 'lib%s.so.6' % module.replace('Qt', 'Qt6', 1)
    path = os.path.join(Build.getQtSharedObjectFolder(), name)
    if not os.path.isfile(path):
      infoSpec = """The class '%s' belongs to '%s', but there is no Qt
      shared object at '%s'."""
      info = infoSpec % (className, module, path)
      raise FileNotFoundError(' '.join(info.split()))
    return path

  def getCppProgram(self, trial: Trial) -> str:
    """
    Gives the C++ half of a trial, as the text of a whole program.

    Written for you from the steps of the trial. It uses Qt directly
    and nothing of cutienator, which is what makes it the measure.

    Raises
    ------

    LookupError
      A class named in the trial is not a class of Qt.
    """
    lines = [
        '//  Written by cutienator.trial, and written again each time',
        '//  the trial is heard. Changes made here are lost.',
        '//  Trial: %s' % ' '.join(trial.getName().split()),
    ]
    for className in trial.getClassNames():
      module = self.getQtModule(className)
      lines.append('#include <%s/%s>' % (module, className))
    lines.extend((
        '#include <iostream>', '', 'int main() {',
        '  std::cout << std::boolalpha;',
    ))
    for kind, objectName, word, others in trial.getSteps():
      if kind == 'make':
        lines.append('  %s *%s = new %s();' % (word, objectName, word))
      elif kind == 'call':
        passed = ('nullptr' if other is None else other for other in others)
        lines.append('  %s->%s(%s);' % (objectName, word, ', '.join(passed)))
      elif kind in ('same', 'nothing'):
        otherName = others[0] if kind == 'same' else None
        label = Trial.getLabel(objectName, word, otherName)
        other = 'nullptr' if otherName is None else otherName
        lines.append('  std::cout << "%s: "' % label)
        answer = '(%s->%s() == %s)' % (objectName, word, other)
        lines.append('            << %s << "\\n";' % answer)
      else:
        raise ValueError("A step of the unknown kind '%s'." % kind)
    lines.extend(('  return 0;', '}', ''))
    return '\n'.join(lines)

  def getPythonProgram(self, trial: Trial) -> str:
    """
    Gives the Python half of a trial, as the text of a whole program.

    Written for you from the steps of the trial. It uses the cute
    classes of cutienator, as a person would.
    """
    lines = [
        '#  Written by cutienator.trial, and written again each time',
        '#  the trial is heard. Changes made here are lost.',
        '#  Trial: %s' % ' '.join(trial.getName().split()),
        'from __future__ import annotations',
        '',
    ]
    for className in trial.getClassNames():
      lines.append('from cutienator import %s' % className)
    lines.extend((
        '', '',
        'def word(flag: bool) -> str:',
        '  """Spells a truth value the way C++ prints it."""',
        "  return 'true' if flag else 'false'",
        '', '',
    ))
    for kind, objectName, word, others in trial.getSteps():
      if kind == 'make':
        lines.append('%s = %s()' % (objectName, word))
      elif kind == 'call':
        passed = ('None' if other is None else other for other in others)
        lines.append('%s.%s(%s)' % (objectName, word, ', '.join(passed)))
      elif kind in ('same', 'nothing'):
        otherName = others[0] if kind == 'same' else None
        label = Trial.getLabel(objectName, word, otherName)
        other = 'None' if otherName is None else otherName
        answer = 'word(%s.%s() is %s)' % (objectName, word, other)
        lines.append("print('%s:', %s)" % (label, answer))
      else:
        raise ValueError("A step of the unknown kind '%s'." % kind)
    lines.append('')
    return '\n'.join(lines)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setWorkFolder(self, workFolder: str) -> None:
    """
    Tells the judge where to write the two programs of each trial.

    Required before 'hear'. Calling it again replaces the folder. The
    programs stay there afterwards, so that they can be read.

    Parameters
    ----------

    workFolder : str
      The path of a folder that exists. A path may be relative to where
      Python was started; it is kept in full.

    Raises
    ------

    TypeException
      'workFolder' is not text.

    FileNotFoundError
      There is no folder at the path.
    """
    if not isinstance(workFolder, str):
      raise TypeException('workFolder', workFolder, str)
    workFolder = os.path.abspath(workFolder)
    if not os.path.isdir(workFolder):
      infoSpec = """There is no folder at '%s'."""
      raise FileNotFoundError(infoSpec % workFolder)
    self.__work_folder__ = workFolder

  def setTimeout(self, seconds: float) -> None:
    """
    Tells the judge how long a half may run before it is stopped.

    Optional; without it a half may run for 60 seconds. A half that is
    stopped shows in its verdict as stopped, with return code None.

    Parameters
    ----------

    seconds : float
      A number above zero, whole or not.

    Raises
    ------

    TypeException
      'seconds' is not a number.

    ValueError
      'seconds' is zero or less.
    """
    if isinstance(seconds, bool) or not isinstance(seconds, (int, float)):
      raise TypeException('seconds', seconds, int, float)
    if seconds <= 0:
      infoSpec = """A half needs some time to run, but received %s
      seconds."""
      raise ValueError(' '.join((infoSpec % seconds).split()))
    self.__timeout_seconds__ = float(seconds)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def __str__(self) -> str:
    """Says where the judge writes, or that no work folder is set."""
    clsName = type(self).__name__
    if self.__work_folder__ is None:
      return '<%s still waiting for: setWorkFolder>' % clsName
    return "<%s writing to '%s'>" % (clsName, self.__work_folder__)

  __repr__ = __str__

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def _compile(self, trial: Trial, cppFile: str, programFile: str) -> None:
    """
    Turns the C++ half into a program that can be run.

    Raises
    ------

    FileNotFoundError
      'clang++' is not installed.

    RuntimeError
      'clang++' refused the C++ half; its own message is included.
    """
    sharedObjects = []
    for className in trial.getClassNames():
      sharedObject = self.getQtSharedObject(className)
      if sharedObject not in sharedObjects:
        sharedObjects.append(sharedObject)
    command = (
        'clang++', '-std=c++17', '-fPIC', '-O2',
        '-I%s' % Build.getQtHeaderFolder(),
        cppFile, '-o', programFile, *sharedObjects,
    )
    try:
      done = subprocess.run(command, capture_output=True, text=True)
    except FileNotFoundError as fileNotFoundError:
      infoSpec = """The program 'clang++' is needed and is not installed."""
      raise FileNotFoundError(infoSpec) from fileNotFoundError
    if done.returncode:
      infoSpec = """The C++ half of the trial '%s' does not compile, so
      the trial asks Qt for something Qt does not offer. 'clang++' said:
      %s"""
      info = infoSpec % (trial.getName(), done.stderr.strip())
      raise RuntimeError(info)

  def _runHalf(self, *command: str) -> Run:
    """
    Runs one half in a process of its own and gives how it went.

    A half that dies or takes too long raises nothing: that it did is
    what comes back.
    """
    seconds = self.getTimeout()
    try:
      done = subprocess.run(
          command, capture_output=True, text=True, timeout=seconds,
          env=self.getEnvironment(),
      )
    except subprocess.TimeoutExpired as timeoutExpired:
      printed = timeoutExpired.stdout or ''
      if isinstance(printed, bytes):
        printed = printed.decode(errors='replace')
      return None, printed, 'It did not end within %s seconds.' % seconds
    return done.returncode, done.stdout, done.stderr

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

  def findRitualFaults(self) -> Tuple[str, ...]:
    """
    Checks that cutienator's own shared object is built correctly, and
    gives each fault found, in words.

    It compares two lists that must be the same: the rituals 'Rituals'
    lists for Python, and the functions the shared object offers. It
    runs no ritual. Whether every function of a Qt header has a ritual
    is not checked yet; that needs the header to be read by program.

    Returns
    -------

    Tuple[str, ...]
      One sentence per fault. It is empty when the two lists agree.

    Raises
    ------

    FileNotFoundError
      The shared object has not been built, or 'nm' is not installed.
    """
    listed = {*Rituals.getRitualNames()}
    sharedObject = SharedObject(Rituals.getTargetFile())
    offered = {symbol.mangled for symbol in sharedObject.functions()}
    faults = []
    for name in sorted(listed - offered):
      infoSpec = """The ritual '%s' is listed in 'Rituals', but no ritual
      file defines it."""
      faults.append(' '.join((infoSpec % name).split()))
    for name in sorted(offered - listed):
      infoSpec = """The shared object offers '%s', but 'Rituals' does not
      list it, so Python cannot call it."""
      faults.append(' '.join((infoSpec % name).split()))
    return (*faults,)

  def hear(self, trial: Trial) -> Verdict:
    """
    Runs one trial in C++ and in Python and gives the verdict.

    It writes both programs to the work folder, compiles the C++ one,
    and runs each in a process of its own. It takes a few seconds, most
    of it compiling.

    Parameters
    ----------

    trial : Trial
      The trial, with its name set and its steps written.

    Returns
    -------

    Verdict
      How each half ended, what each printed, and whether they agree.

    Raises
    ------

    TypeException
      'trial' is not a 'Trial'.

    MissingVariable
      'setWorkFolder' was not called on this judge, or 'setName' on the
      trial.

    LookupError
      A class named in the trial is not a class of Qt.

    RuntimeError
      The C++ half does not compile: the trial asks Qt for something Qt
      does not offer. What 'clang++' said is included.
    """
    if not isinstance(trial, Trial):
      raise TypeException('trial', trial, Trial)
    stem = os.path.join(self.getWorkFolder(), self.getFileStem(trial))
    cppFile, pythonFile = '%s.cpp' % stem, '%s.py' % stem
    with open(cppFile, 'w') as file:
      file.write(self.getCppProgram(trial))
    with open(pythonFile, 'w') as file:
      file.write(self.getPythonProgram(trial))
    self._compile(trial, cppFile, stem)
    verdict = Verdict()
    verdict.setTrialName(trial.getName())
    verdict.setCppRun(*self._runHalf(stem))
    verdict.setPythonRun(*self._runHalf(self.getPython(), pythonFile))
    return verdict

  def hearAll(self, *trials: Trial) -> Tuple[Verdict, ...]:
    """
    Runs several trials, some at the same time, and gives their
    verdicts in the order the trials were given.

    As many trials run at once as the machine has processors, which is
    several times faster than one by one.

    Parameters
    ----------

    *trials : Trial
      The trials, each with a name of its own.

    Returns
    -------

    Tuple[Verdict, ...]
      One verdict per trial, in the same order.

    Raises
    ------

    ValueError
      Two trials would be written to the same files, since their names
      differ only in punctuation or case.

    Also raises whatever 'hear' raises, for the first trial that cannot
    be run.
    """
    stems = [self.getFileStem(trial) for trial in trials]
    for stem in stems:
      if stems.count(stem) > 1:
        infoSpec = """More than one trial would be written to the files
        named '%s'. Give each trial a name of its own."""
        raise ValueError(' '.join((infoSpec % stem).split()))
    workers = os.cpu_count() or 1
    with ThreadPoolExecutor(max_workers=workers) as pool:
      return (*pool.map(self.hear, trials),)
