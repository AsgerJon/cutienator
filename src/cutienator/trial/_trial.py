"""Trial is one test, written once and run in C++ and in Python."""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
from __future__ import annotations

import keyword
from typing import TYPE_CHECKING

from worktoy.waitaminute import MissingVariable, TypeException

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Dict, List, Optional, Tuple

  Step = Tuple[str, str, str, Tuple[Optional[str], ...]]


class Trial:
  """
  One test, written once as a list of steps. A 'Judge' runs it twice: in
  C++ against Qt itself, and in Python against the cute classes. Each
  run prints one line per expectation, and the two must print the same.

    trial = Trial()
    trial.setName('QObject: parent and setParent')
    trial.make('mother', 'QObject')
    trial.make('child', 'QObject')
    trial.expectNothing('child', 'parent')
    trial.call('child', 'setParent', 'mother')
    trial.expectSame('child', 'parent', 'mother')

  Terms
  -----

  - A step is one thing to do, said without saying how either language
    does it: make an object, call a method, or expect an answer.
  - An object name is the name a 'make' step gives the object it makes,
    as 'mother'. Later steps refer to the object by that name.
  - An expectation is a step that prints one line, ending in 'true' or
    'false'. 'expectSame' and 'expectNothing' are the expectations.

  You provide
  -----------

  - 'setName': what the trial is called in reports. Required.
  - The steps, in the order they are to run, through 'make', 'call',
    'expectSame' and 'expectNothing'.

  What to expect
  --------------

  - A trial runs nothing. It only holds its steps; a 'Judge' runs them.
  - A wrong step is refused when it is written, not when it is run: an
    object name used before it is made, made twice, or not usable as a
    name in both C++ and Python.
  - Whether a class has the method a step names is not checked here.
    That shows when the 'Judge' runs the trial.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def getLabel(
      objectName: str,
      methodName: str,
      otherName: Optional[str],
  ) -> str:
    """
    Gives the words an expectation prints before 'true' or 'false'.

    Both halves of a trial print this same label, which is what lets
    their lines be compared.

    Parameters
    ----------

    objectName : str
      The object the method is called on, as 'child'.

    methodName : str
      The method, as 'parent'.

    otherName : Optional[str]
      The object the answer is expected to be, or None for no object.

    Returns
    -------

    str
      As 'child.parent() is mother', or 'child.parent() is nothing'.
    """
    other = 'nothing' if otherName is None else otherName
    return '%s.%s() is %s' % (objectName, methodName, other)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  Words C++ keeps for itself, which no object or method can be named.
  __cpp_words__ = (
      'auto', 'bool', 'break', 'case', 'catch', 'char', 'class', 'const',
      'continue', 'default', 'delete', 'do', 'double', 'else', 'enum',
      'explicit', 'extern', 'false', 'float', 'for', 'friend', 'goto',
      'if', 'inline', 'int', 'long', 'namespace', 'new', 'nullptr',
      'operator', 'private', 'protected', 'public', 'return', 'short',
      'signed', 'sizeof', 'static', 'struct', 'switch', 'template',
      'this', 'throw', 'true', 'try', 'typedef', 'typename', 'union',
      'unsigned', 'using', 'virtual', 'void', 'volatile', 'while',
  )

  #  Fallback Variables

  #  Private Variables
  __trial_name__ = None  # type: Optional[str]
  __trial_steps__ = None  # type: Optional[List[Step]]
  __class_of__ = None  # type: Optional[Dict[str, str]]

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def getName(self) -> str:
    """
    Gives what this trial is called in reports.

    Provided by you, through 'setName'. Nothing fills it in for you.

    Raises
    ------

    MissingVariable
      'setName' has not been called on this trial.
    """
    if self.__trial_name__ is None:
      raise MissingVariable(self, '__trial_name__', str)
    return self.__trial_name__

  def getSteps(self) -> Tuple[Step, ...]:
    """
    Gives the steps in the order they were written.

    Provided by you, through 'make', 'call', 'expectSame' and
    'expectNothing'. It is empty when none of them was called.

    Returns
    -------

    Tuple[Step, ...]
      Each step is a 'Tuple[str, str, str, Tuple[Optional[str], ...]]'
      of four entries. The first says which kind of step it is:

      'make': the object name, its class name, and nothing more.
      'call': the object name, the method name, and the arguments.
      'same': the object name, the method name, and the one object the
      answer is expected to be.
      'nothing': the object name, the method name, and nothing more.

      An argument is an object name, or None for no object.
    """
    return (*(self.__trial_steps__ or ()),)

  def getClassNames(self) -> Tuple[str, ...]:
    """
    Gives each class the 'make' steps name, once, in order of first use.

    Worked out from the steps you wrote. A 'Judge' uses it to know which
    Qt headers and which cute classes the two programs need.
    """
    classNames = []
    for kind, _, className, _ in self.getSteps():
      if kind == 'make' and className not in classNames:
        classNames.append(className)
    return (*classNames,)

  def getClassOf(self, objectName: str) -> str:
    """
    Gives the class name a 'make' step gave an object.

    Raises
    ------

    LookupError
      No 'make' step has made an object of that name.
    """
    try:
      return (self.__class_of__ or dict())[objectName]
    except KeyError as keyError:
      infoSpec = """No step has made an object named '%s' yet. A 'make'
      step must come first."""
      info = ' '.join((infoSpec % (objectName,)).split())
      raise LookupError(info) from keyError

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setName(self, name: str) -> None:
    """
    Tells the trial what it is called in reports.

    Required before a 'Judge' can hear the trial. Calling it again
    replaces the name. Two trials heard together need different names,
    since their programs are filed under them.

    Parameters
    ----------

    name : str
      Any text, as 'QObject: parent and setParent'. It holds at least
      one letter or digit.

    Raises
    ------

    TypeException
      'name' is not text.

    ValueError
      'name' holds no letter or digit.
    """
    if not isinstance(name, str):
      raise TypeException('name', name, str)
    if not any(letter.isalnum() for letter in name):
      infoSpec = """The name of a trial holds at least one letter or
      digit, but received '%s'."""
      raise ValueError(' '.join((infoSpec % name).split()))
    self.__trial_name__ = name

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def __str__(self) -> str:
    """Gives the name, when set, and how many steps are written."""
    clsName = type(self).__name__
    count = len(self.getSteps())
    if self.__trial_name__ is None:
      return '<%s with no name yet, of %d steps>' % (clsName, count)
    return "<%s '%s' of %d steps>" % (clsName, self.__trial_name__, count)

  __repr__ = __str__

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @classmethod
  def _requireWord(cls, word: object, what: str) -> str:
    """
    Refuses text that cannot be a name in both C++ and Python.

    Parameters
    ----------

    word : object
      What was given as a name.

    what : str
      What the name is for, as 'objectName', used in the refusal.

    Returns
    -------

    str
      'word' itself.

    Raises
    ------

    TypeException
      'word' is not text.

    ValueError
      'word' is no plain name, or one of the two languages keeps it for
      itself, as 'class' or 'new'.
    """
    if not isinstance(word, str):
      raise TypeException(what, word, str)
    plain = word.isidentifier() and word.isascii()
    kept = keyword.iskeyword(word) or word in cls.__cpp_words__
    if not plain or kept:
      infoSpec = """A name must be usable in both C++ and Python: plain
      letters, digits and underscores, not starting with a digit, and no
      word either language keeps for itself. Received '%s' for '%s'."""
      raise ValueError(' '.join((infoSpec % (word, what)).split()))
    return word

  def _addStep(
      self,
      kind: str,
      objectName: str,
      word: str,
      others: Tuple[Optional[str], ...],
  ) -> None:
    """Writes one step down after those written before."""
    if self.__trial_steps__ is None:
      self.__trial_steps__ = []
    self.__trial_steps__.append((kind, objectName, word, others))

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

  def make(self, objectName: str, className: str) -> None:
    """
    Writes the step: make a new object of a class, with no arguments.

    In C++ this becomes 'QObject *mother = new QObject();' and in Python
    'mother = QObject()'.

    Parameters
    ----------

    objectName : str
      The name later steps refer to the object by, as 'mother'. It has
      not been used by an earlier 'make' step of this trial.

    className : str
      The class, by the name it has in both Qt and cutienator, as
      'QObject'.

    Raises
    ------

    TypeException
      A name is not text.

    ValueError
      A name is not usable in both C++ and Python, or the object name
      was made before.
    """
    self._requireWord(objectName, 'objectName')
    self._requireWord(className, 'className')
    if self.__class_of__ is None:
      self.__class_of__ = dict()
    if objectName in self.__class_of__:
      infoSpec = """An object named '%s' was made by an earlier step. Each
      object needs a name of its own."""
      raise ValueError(' '.join((infoSpec % objectName).split()))
    self.__class_of__[objectName] = className
    self._addStep('make', objectName, className, ())

  def call(
      self,
      objectName: str,
      methodName: str,
      *argumentNames: Optional[str],
  ) -> None:
    """
    Writes the step: call a method on an object, for what it does. What
    it returns is ignored; an expectation is the step that looks.

    In C++ this becomes 'child->setParent(mother);' and in Python
    'child.setParent(mother)'.

    Parameters
    ----------

    objectName : str
      The object to call the method on, by the name its 'make' step
      gave it.

    methodName : str
      The method, by the name it has in both Qt and cutienator.

    *argumentNames : Optional[str]
      What is passed, one entry per argument, or none at all. Each is
      the name of an object made by an earlier step, or None to pass no
      object: 'nullptr' in C++, 'None' in Python. Numbers and text
      cannot be passed yet.

    Raises
    ------

    LookupError
      An object name was not made by an earlier step.

    TypeException
      A name is not text.

    ValueError
      The method name is not usable in both C++ and Python.
    """
    self.getClassOf(objectName)
    self._requireWord(methodName, 'methodName')
    for argumentName in argumentNames:
      if argumentName is not None:
        self.getClassOf(argumentName)
    self._addStep('call', objectName, methodName, (*argumentNames,))

  def expectSame(
      self,
      objectName: str,
      methodName: str,
      otherName: str,
  ) -> None:
    """
    Writes the expectation: a method called with no arguments answers
    with one particular object, the very same one, not a copy.

    When run it prints one line, as 'child.parent() is mother: true'.
    In C++ the check is 'child->parent() == mother', and in Python
    'child.parent() is mother'.

    Parameters
    ----------

    objectName : str
      The object to call the method on, by the name its 'make' step
      gave it.

    methodName : str
      The method, by the name it has in both Qt and cutienator.

    otherName : str
      The object the answer is expected to be, by the name its 'make'
      step gave it. For no object, use 'expectNothing'.

    Raises
    ------

    LookupError
      An object name was not made by an earlier step.

    TypeException
      A name is not text.

    ValueError
      The method name is not usable in both C++ and Python.
    """
    self.getClassOf(objectName)
    self._requireWord(methodName, 'methodName')
    self.getClassOf(otherName)
    self._addStep('same', objectName, methodName, (otherName,))

  def expectNothing(self, objectName: str, methodName: str) -> None:
    """
    Writes the expectation: a method called with no arguments answers
    with no object at all.

    When run it prints one line, as 'child.parent() is nothing: true'.
    In C++ the check is 'child->parent() == nullptr', and in Python
    'child.parent() is None'.

    Parameters
    ----------

    objectName : str
      The object to call the method on, by the name its 'make' step
      gave it.

    methodName : str
      The method, by the name it has in both Qt and cutienator.

    Raises
    ------

    LookupError
      The object name was not made by an earlier step.

    TypeException
      A name is not text.

    ValueError
      The method name is not usable in both C++ and Python.
    """
    self.getClassOf(objectName)
    self._requireWord(methodName, 'methodName')
    self._addStep('nothing', objectName, methodName, ())
