"""
QMessageLogger binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qlogging.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QDebug

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMessageLogger(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QMessageLogger: a plain Python object standing in
  front of one C++ QMessageLogger.

  What exists
  -----------

  Every function of Qt's QMessageLogger that has a ritual and that Python can
  call so far, 5 names in all: 'debug', 'info', 'warning', 'critical',
  'fatal'. It can be made from Python, in 3 ways; see '__init__'.

  What has no ritual
  ------------------

  29 of the 37 functions Qt declares: 17 takes any number of arguments; 10
  takes or gives a type that cannot be passed yet; 2 forbidden.

  What to expect
  --------------

  - The C++ QMessageLogger is created at the first use, not by
    'QMessageLogger(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMessageLogger.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMessageLogger'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def debug(self) -> QDebug:
    """
    Calls Qt's 'QDebug QMessageLogger::debug() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagelogger.html#debug

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug QMessageLogger::debug() const
    address = self.uglySide.call('ritual_ZNK14QMessageLogger5debugEv')
    from . import QDebug
    return QDebug._cuteOwning(address)

  def info(self) -> QDebug:
    """
    Calls Qt's 'QDebug QMessageLogger::info() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagelogger.html#info

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug QMessageLogger::info() const
    address = self.uglySide.call('ritual_ZNK14QMessageLogger4infoEv')
    from . import QDebug
    return QDebug._cuteOwning(address)

  def warning(self) -> QDebug:
    """
    Calls Qt's 'QDebug QMessageLogger::warning() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagelogger.html#warning

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug QMessageLogger::warning() const
    address = self.uglySide.call('ritual_ZNK14QMessageLogger7warningEv')
    from . import QDebug
    return QDebug._cuteOwning(address)

  def critical(self) -> QDebug:
    """
    Calls Qt's 'QDebug QMessageLogger::critical() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagelogger.html#critical

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug QMessageLogger::critical() const
    address = self.uglySide.call('ritual_ZNK14QMessageLogger8criticalEv')
    from . import QDebug
    return QDebug._cuteOwning(address)

  def fatal(self) -> QDebug:
    """
    Calls Qt's 'QDebug QMessageLogger::fatal() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmessagelogger.html#fatal

    Returns
    -------

    QDebug
      A new cute QDebug around the copy Qt gave back. Python owns it.
    """
    #  QDebug QMessageLogger::fatal() const
    address = self.uglySide.call('ritual_ZNK14QMessageLogger5fatalEv')
    from . import QDebug
    return QDebug._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QMessageLogger::QMessageLogger()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmessagelogger.html#QMessageLogger
    """
    #  QMessageLogger::QMessageLogger()
    self._noteCreation(QMessageLogger, lambda: Rituals.call(
        'ritual_ZN14QMessageLoggerC1Ev',
    ))

  @overload(str, int, str)
  @overload(str, int, NoneType)
  @overload(NoneType, int, str)
  @overload(NoneType, int, NoneType)
  def __init__(
      self,
      file: Optional[str],
      line: int,
      function: Optional[str],
  ) -> None:
    """
    Notes what was given, for Qt's 'QMessageLogger::QMessageLogger(const char
    *file, int line, const char *function)', which is called at the first
    use.

    Qt's own words: https://doc.qt.io/qt-6/qmessagelogger.html#QMessageLogger

    Parameters
    ----------

    file : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    line : int
      Passed on as it is.

    function : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  QMessageLogger::QMessageLogger(const char *file, int line, const char
    #      *function)
    self._noteCreation(QMessageLogger, lambda: Rituals.call(
        'ritual_ZN14QMessageLoggerC1EPKciS1_',
        self._bytesOf(file), line, self._bytesOf(function),
    ))

  @overload(str, int, str, str)
  @overload(str, int, str, NoneType)
  @overload(str, int, NoneType, str)
  @overload(str, int, NoneType, NoneType)
  @overload(NoneType, int, str, str)
  @overload(NoneType, int, str, NoneType)
  @overload(NoneType, int, NoneType, str)
  @overload(NoneType, int, NoneType, NoneType)
  def __init__(
      self,
      file: Optional[str],
      line: int,
      function: Optional[str],
      category: Optional[str],
  ) -> None:
    """
    Notes what was given, for Qt's 'QMessageLogger::QMessageLogger(const char
    *file, int line, const char *function, const char *category)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmessagelogger.html#QMessageLogger

    Parameters
    ----------

    file : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    line : int
      Passed on as it is.

    function : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    category : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.
    """
    #  QMessageLogger::QMessageLogger(const char *file, int line, const char
    #      *function, const char *category)
    self._noteCreation(QMessageLogger, lambda: Rituals.call(
        'ritual_ZN14QMessageLoggerC1EPKciS1_S1_',
        self._bytesOf(file), line, self._bytesOf(function),
        self._bytesOf(category),
    ))

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
