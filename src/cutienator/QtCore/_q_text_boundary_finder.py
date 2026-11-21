"""
QTextBoundaryFinder binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/qtextboundaryfinder.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from . import QTextBoundaryFinderBoundaryReason
from . import QTextBoundaryFinderBoundaryType


class QTextBoundaryFinder(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTextBoundaryFinder: a plain Python object standing
  in front of one C++ QTextBoundaryFinder.

  C++ hands a QTextBoundaryFinder around as a copy, so every C++
  QTextBoundaryFinder behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QTextBoundaryFinder that has a ritual and that
  Python can call so far, 11 names in all: 'isValid', 'type', 'string',
  'toStart', 'toEnd', 'position', 'setPosition', 'toNextBoundary',
  'toPreviousBoundary', 'isAtBoundary', 'boundaryReasons'. It can be made
  from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTextBoundaryFinder::~QTextBoundaryFinder()': the destructor:
    Python removes its C++ QTextBoundaryFinder by it, and has no other use
    for it.
  - Qt's 'QTextBoundaryFinder::QTextBoundaryFinder(BoundaryType type, const
    QChar *chars, qsizetype length, unsigned char *buffer, qsizetype
    bufferSize)': takes a number to change where it is.
  - Qt's 'QTextBoundaryFinder::QTextBoundaryFinder(BoundaryType type,
    QStringView str, unsigned char *buffer, qsizetype bufferSize)': takes a
    number to change where it is.

  What has no ritual
  ------------------

  4 of the 21 functions Qt declares: 4 takes or gives a type that cannot be
  passed yet.

  What to expect
  --------------

  - The C++ QTextBoundaryFinder is created at the first use, not by
    'QTextBoundaryFinder(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QTextBoundaryFinder back gives a copy the ritual made
    for Python, in a new cute QTextBoundaryFinder.
  """

  #  The enums Qt writes inside QTextBoundaryFinder, and the names Qt has for
  #  the combinations of its flags enums.
  BoundaryReason = QTextBoundaryFinderBoundaryReason
  BoundaryReasons = QTextBoundaryFinderBoundaryReason
  BoundaryType = QTextBoundaryFinderBoundaryType

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextBoundaryFinder'

  #  Qt's '~QTextBoundaryFinder()'. Naming it makes this a value class:
  #  Python owns every C++ QTextBoundaryFinder behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QTextBoundaryFinderD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool QTextBoundaryFinder::isValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextboundaryfinder.html#isValid
    """
    #  bool QTextBoundaryFinder::isValid() const
    return self.uglySide.call('ritual_ZNK19QTextBoundaryFinder7isValidEv')

  def type(self) -> BoundaryType:
    """
    Calls Qt's 'BoundaryType QTextBoundaryFinder::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextboundaryfinder.html#type

    Returns
    -------

    BoundaryType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'BoundaryType(number)'
      gives.
    """
    #  BoundaryType QTextBoundaryFinder::type() const
    return QTextBoundaryFinder.BoundaryType(self.uglySide.call(
        'ritual_ZNK19QTextBoundaryFinder4typeEv',
    ))

  def string(self) -> str:
    """
    Calls Qt's 'QString QTextBoundaryFinder::string() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextboundaryfinder.html#string

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextBoundaryFinder::string() const
    return self.uglySide.call('ritual_ZNK19QTextBoundaryFinder6stringEv')

  def position(self) -> int:
    """
    Calls Qt's 'qsizetype QTextBoundaryFinder::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextboundaryfinder.html#position
    """
    #  qsizetype QTextBoundaryFinder::position() const
    return self.uglySide.call('ritual_ZNK19QTextBoundaryFinder8positionEv')

  def isAtBoundary(self) -> bool:
    """
    Calls Qt's 'bool QTextBoundaryFinder::isAtBoundary() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextboundaryfinder.html#isAtBoundary
    """
    #  bool QTextBoundaryFinder::isAtBoundary() const
    return self.uglySide.call(
        'ritual_ZNK19QTextBoundaryFinder12isAtBoundaryEv',
    )

  def boundaryReasons(self) -> BoundaryReasons:
    """
    Calls Qt's 'BoundaryReasons QTextBoundaryFinder::boundaryReasons()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextboundaryfinder.html#boundaryReasons

    Returns
    -------

    BoundaryReasons
      The value standing for the combination Qt gave back.
    """
    #  BoundaryReasons QTextBoundaryFinder::boundaryReasons() const
    return QTextBoundaryFinder.BoundaryReasons(self.uglySide.call(
        'ritual_ZNK19QTextBoundaryFinder15boundaryReasonsEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setPosition(self, position: int) -> None:
    """
    Calls Qt's 'void QTextBoundaryFinder::setPosition(qsizetype position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextboundaryfinder.html#setPosition

    Parameters
    ----------

    position : int
      Passed on as it is.
    """
    #  void QTextBoundaryFinder::setPosition(qsizetype position)
    self.uglySide.call(
        'ritual_ZN19QTextBoundaryFinder11setPositionEx', position,
    )

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
    Notes what was given, for Qt's
    'QTextBoundaryFinder::QTextBoundaryFinder()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextboundaryfinder.html#QTextBoundaryFinder
    """
    #  QTextBoundaryFinder::QTextBoundaryFinder()
    self._noteCreation(QTextBoundaryFinder, lambda: Rituals.call(
        'ritual_ZN19QTextBoundaryFinderC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QTextBoundaryFinder) -> None:
    """
    Notes what was given, for Qt's
    'QTextBoundaryFinder::QTextBoundaryFinder(const QTextBoundaryFinder
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextboundaryfinder.html#QTextBoundaryFinder

    Parameters
    ----------

    other : QTextBoundaryFinder
      Passed on as a value: Qt reads the C++ QTextBoundaryFinder, which stays
      Python's own.
    """
    #  QTextBoundaryFinder::QTextBoundaryFinder(const QTextBoundaryFinder
    #      &other)
    self._noteCreation(QTextBoundaryFinder, lambda: Rituals.call(
        'ritual_ZN19QTextBoundaryFinderC1ERKS_', self._valueOf(other),
    ))

  @overload(BoundaryType, str)
  def __init__(self, type: BoundaryType, string: str) -> None:
    """
    Notes what was given, for Qt's
    'QTextBoundaryFinder::QTextBoundaryFinder(BoundaryType type, const
    QString &string)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextboundaryfinder.html#QTextBoundaryFinder

    Parameters
    ----------

    type : BoundaryType
      Passed on as its number.

    string : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  QTextBoundaryFinder::QTextBoundaryFinder(BoundaryType type, const
    #      QString &string)
    self._noteCreation(QTextBoundaryFinder, lambda: Rituals.call(
        'ritual_ZN19QTextBoundaryFinderC1ENS_12BoundaryTypeERK7QString',
        type.value, string,
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

  def toStart(self) -> None:
    """
    Calls Qt's 'void QTextBoundaryFinder::toStart()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextboundaryfinder.html#toStart
    """
    #  void QTextBoundaryFinder::toStart()
    self.uglySide.call('ritual_ZN19QTextBoundaryFinder7toStartEv')

  def toEnd(self) -> None:
    """
    Calls Qt's 'void QTextBoundaryFinder::toEnd()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextboundaryfinder.html#toEnd
    """
    #  void QTextBoundaryFinder::toEnd()
    self.uglySide.call('ritual_ZN19QTextBoundaryFinder5toEndEv')

  def toNextBoundary(self) -> int:
    """
    Calls Qt's 'qsizetype QTextBoundaryFinder::toNextBoundary()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextboundaryfinder.html#toNextBoundary
    """
    #  qsizetype QTextBoundaryFinder::toNextBoundary()
    return self.uglySide.call(
        'ritual_ZN19QTextBoundaryFinder14toNextBoundaryEv',
    )

  def toPreviousBoundary(self) -> int:
    """
    Calls Qt's 'qsizetype QTextBoundaryFinder::toPreviousBoundary()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextboundaryfinder.html#toPreviousBoundary
    """
    #  qsizetype QTextBoundaryFinder::toPreviousBoundary()
    return self.uglySide.call(
        'ritual_ZN19QTextBoundaryFinder18toPreviousBoundaryEv',
    )
