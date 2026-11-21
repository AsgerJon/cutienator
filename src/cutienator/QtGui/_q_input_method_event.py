"""
QInputMethodEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtGui/qevent.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from ..QtCore import QEvent
from . import QInputMethodEventAttributeType

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class QInputMethodEvent(QEvent):
  """
  The cute side of Qt's QInputMethodEvent: a plain Python object standing in
  front of one C++ QInputMethodEvent.

  It is built on the cute 'QEvent', as Qt's QInputMethodEvent is built on
  Qt's QEvent, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QInputMethodEvent that has a ritual and that Python
  can call so far, 6 names in all: 'clone', 'setCommitString',
  'preeditString', 'commitString', 'replacementStart', 'replacementLength'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QInputMethodEvent::~QInputMethodEvent()': the destructor: Python
    never removes a C++ QInputMethodEvent.

  What has no ritual
  ------------------

  6 of the 14 functions Qt declares: 2 protected; 2 forbidden; 2 takes or
  gives a type that cannot be passed yet.

  What to expect
  --------------

  - The C++ QInputMethodEvent is created at the first use, not by
    'QInputMethodEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QInputMethodEvent.
  """

  #  The enums Qt writes inside QInputMethodEvent, and the names Qt has for
  #  the combinations of its flags enums.
  AttributeType = QInputMethodEventAttributeType

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QInputMethodEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QInputMethodEvent]:
    """
    Calls Qt's 'QInputMethodEvent *QInputMethodEvent::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qinputmethodevent.html#clone

    Returns
    -------

    Optional[QInputMethodEvent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QInputMethodEvent *QInputMethodEvent::clone() const
    address = self.uglySide.call('ritual_ZNK17QInputMethodEvent5cloneEv')
    return QInputMethodEvent._cuteAt(address)

  def preeditString(self) -> str:
    """
    Calls Qt's 'const QString &QInputMethodEvent::preeditString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qinputmethodevent.html#preeditString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString &QInputMethodEvent::preeditString() const
    return self.uglySide.call(
        'ritual_ZNK17QInputMethodEvent13preeditStringEv',
    )

  def commitString(self) -> str:
    """
    Calls Qt's 'const QString &QInputMethodEvent::commitString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qinputmethodevent.html#commitString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  const QString &QInputMethodEvent::commitString() const
    return self.uglySide.call(
        'ritual_ZNK17QInputMethodEvent12commitStringEv',
    )

  def replacementStart(self) -> int:
    """
    Calls Qt's 'int QInputMethodEvent::replacementStart() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qinputmethodevent.html#replacementStart
    """
    #  int QInputMethodEvent::replacementStart() const
    return self.uglySide.call(
        'ritual_ZNK17QInputMethodEvent16replacementStartEv',
    )

  def replacementLength(self) -> int:
    """
    Calls Qt's 'int QInputMethodEvent::replacementLength() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qinputmethodevent.html#replacementLength
    """
    #  int QInputMethodEvent::replacementLength() const
    return self.uglySide.call(
        'ritual_ZNK17QInputMethodEvent17replacementLengthEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  @overload(str, int)
  @overload(str, int, int)
  def setCommitString(
      self,
      commitString: str,
      replaceFrom: int = 0,
      replaceLength: int = 0,
  ) -> None:
    """
    Calls Qt's 'void QInputMethodEvent::setCommitString(const QString
    &commitString, int replaceFrom, int replaceLength)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qinputmethodevent.html#setCommitString

    Parameters
    ----------

    commitString : str
      Passed on as it is: a QString is made of it for the call.

    replaceFrom : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    replaceLength : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QInputMethodEvent::setCommitString(const QString &commitString,
    #      int replaceFrom, int replaceLength)
    self.uglySide.call(
        'ritual_ZN17QInputMethodEvent15setCommitStringERK7QStringii',
        commitString, replaceFrom, replaceLength,
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
    Notes what was given, for Qt's 'QInputMethodEvent::QInputMethodEvent()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qinputmethodevent.html#QInputMethodEvent
    """
    #  QInputMethodEvent::QInputMethodEvent()
    self._noteCreation(QInputMethodEvent, lambda: Rituals.call(
        'ritual_ZN17QInputMethodEventC1Ev',
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
