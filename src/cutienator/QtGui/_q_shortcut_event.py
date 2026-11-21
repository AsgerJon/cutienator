"""
QShortcutEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtGui/qevent.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QEvent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QKeySequence, QShortcut
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QKeySequence = WAIT['QKeySequence']
  QShortcut = WAIT['QShortcut']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QShortcutEvent(QEvent):
  """
  The cute side of Qt's QShortcutEvent: a plain Python object standing in
  front of one C++ QShortcutEvent.

  It is built on the cute 'QEvent', as Qt's QShortcutEvent is built on Qt's
  QEvent, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QShortcutEvent that has a ritual and that Python can
  call so far, 4 names in all: 'clone', 'key', 'shortcutId', 'isAmbiguous'.
  It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QShortcutEvent::~QShortcutEvent()': the destructor: Python never
    removes a C++ QShortcutEvent.

  What has no ritual
  ------------------

  4 of the 11 functions Qt declares: 2 protected; 2 forbidden.

  What to expect
  --------------

  - The C++ QShortcutEvent is created at the first use, not by
    'QShortcutEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QShortcutEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QShortcutEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QShortcutEvent]:
    """
    Calls Qt's 'QShortcutEvent *QShortcutEvent::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qshortcutevent.html#clone

    Returns
    -------

    Optional[QShortcutEvent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QShortcutEvent *QShortcutEvent::clone() const
    address = self.uglySide.call('ritual_ZNK14QShortcutEvent5cloneEv')
    return QShortcutEvent._cuteAt(address)

  def key(self) -> QKeySequence:
    """
    Calls Qt's 'const QKeySequence &QShortcutEvent::key() const'.

    Qt's own words: https://doc.qt.io/qt-6/qshortcutevent.html#key

    Returns
    -------

    QKeySequence
      A new cute QKeySequence around the copy Qt gave back. Python owns it.
    """
    #  const QKeySequence &QShortcutEvent::key() const
    address = self.uglySide.call('ritual_ZNK14QShortcutEvent3keyEv')
    from . import QKeySequence
    return QKeySequence._cuteOwning(address)

  def shortcutId(self) -> int:
    """
    Calls Qt's 'int QShortcutEvent::shortcutId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qshortcutevent.html#shortcutId
    """
    #  int QShortcutEvent::shortcutId() const
    return self.uglySide.call('ritual_ZNK14QShortcutEvent10shortcutIdEv')

  def isAmbiguous(self) -> bool:
    """
    Calls Qt's 'bool QShortcutEvent::isAmbiguous() const'.

    Qt's own words: https://doc.qt.io/qt-6/qshortcutevent.html#isAmbiguous
    """
    #  bool QShortcutEvent::isAmbiguous() const
    return self.uglySide.call('ritual_ZNK14QShortcutEvent11isAmbiguousEv')

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

  @overload(QKeySequence, int)
  @overload(QKeySequence, int, bool)
  def __init__(
      self,
      key: QKeySequence,
      id: int,
      ambiguous: bool = False,
  ) -> None:
    """
    Notes what was given, for Qt's 'QShortcutEvent::QShortcutEvent(const
    QKeySequence &key, int id, bool ambiguous)', which is called at the first
    use.

    Qt's own words: https://doc.qt.io/qt-6/qshortcutevent.html#QShortcutEvent

    Parameters
    ----------

    key : QKeySequence
      Passed on as a value: Qt reads the C++ QKeySequence, which stays
      Python's own.

    id : int
      Passed on as it is.

    ambiguous : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  QShortcutEvent::QShortcutEvent(const QKeySequence &key, int id, bool
    #      ambiguous)
    self._noteCreation(QShortcutEvent, lambda: Rituals.call(
        'ritual_ZN14QShortcutEventC1ERK12QKeySequenceib',
        self._valueOf(key), id, ambiguous,
    ))

  @overload(QKeySequence)
  @overload(QKeySequence, QShortcut)
  @overload(QKeySequence, NoneType)
  @overload(QKeySequence, QShortcut, bool)
  @overload(QKeySequence, NoneType, bool)
  def __init__(
      self,
      key: QKeySequence,
      shortcut: Optional[QShortcut] = None,
      ambiguous: bool = False,
  ) -> None:
    """
    Notes what was given, for Qt's 'QShortcutEvent::QShortcutEvent(const
    QKeySequence &key, const QShortcut *shortcut, bool ambiguous)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qshortcutevent.html#QShortcutEvent

    Parameters
    ----------

    key : QKeySequence
      Passed on as a value: Qt reads the C++ QKeySequence, which stays
      Python's own.

    shortcut : Optional[QShortcut]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    ambiguous : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  QShortcutEvent::QShortcutEvent(const QKeySequence &key, const
    #      QShortcut *shortcut, bool ambiguous)
    self._noteCreation(QShortcutEvent, lambda: Rituals.call(
        'ritual_ZN14QShortcutEventC1ERK12QKeySequencePK9QShortcutb',
        self._valueOf(key), self._addressOf(shortcut), ambiguous,
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
