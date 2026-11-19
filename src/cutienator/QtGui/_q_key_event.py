"""
QKeyEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtGui/qevent.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from ..QtCore import Qt
from ..QtCore import QEvent
from ._q_input_event import QInputEvent
from ._q_key_sequence import QKeySequence

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class QKeyEvent(QInputEvent):
  """
  The cute side of Qt's QKeyEvent: a plain Python object standing in front of
  one C++ QKeyEvent.

  It is built on the cute 'QInputEvent', as Qt's QKeyEvent is built on Qt's
  QInputEvent, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QKeyEvent that has a ritual and that Python can call
  so far, 10 names in all: 'clone', 'key', 'matches', 'modifiers', 'text',
  'isAutoRepeat', 'count', 'nativeScanCode', 'nativeVirtualKey',
  'nativeModifiers'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QKeyEvent::~QKeyEvent()': the destructor: Python never removes a
    C++ QKeyEvent.
  - Qt's 'QKeyEvent::QKeyEvent(Type type, int key, Qt::KeyboardModifiers
    modifiers, quint32 nativeScanCode, quint32 nativeVirtualKey, quint32
    nativeModifiers, const QString &text, bool autorep, quint16 count, const
    QInputDevice *device)': names 'QInputDevice', which has no cute class
    yet.
  - Qt's 'QKeyCombination QKeyEvent::keyCombination() const': gives
    'QKeyCombination', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 18 functions Qt declares: 2 protected; 2 forbidden.

  What to expect
  --------------

  - The C++ QKeyEvent is created at the first use, not by 'QKeyEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QKeyEvent.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QKeyEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def clone(self) -> Optional[QKeyEvent]:
    """
    Calls Qt's 'QKeyEvent *QKeyEvent::clone() const'.

    Qt's own words: https://doc.qt.io/qt-6/qkeyevent.html#clone

    Returns
    -------

    Optional[QKeyEvent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QKeyEvent *QKeyEvent::clone() const
    address = self.uglySide.call('ritual_ZNK9QKeyEvent5cloneEv')
    return QKeyEvent._cuteAt(address)

  def key(self) -> int:
    """
    Calls Qt's 'int QKeyEvent::key() const'.

    Qt's own words: https://doc.qt.io/qt-6/qkeyevent.html#key
    """
    #  int QKeyEvent::key() const
    return self.uglySide.call('ritual_ZNK9QKeyEvent3keyEv')

  @overload(QKeySequence.StandardKey)
  def matches(self, key: QKeySequence.StandardKey) -> bool:
    """
    Calls Qt's 'bool QKeyEvent::matches(QKeySequence::StandardKey key)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qkeyevent.html#matches

    Parameters
    ----------

    key : QKeySequence.StandardKey
      Passed on as its number.
    """
    #  bool QKeyEvent::matches(QKeySequence::StandardKey key) const
    return self.uglySide.call(
        'ritual_ZNK9QKeyEvent7matchesEN12QKeySequence11StandardKeyE',
        key.value,
    )

  def modifiers(self) -> Qt.KeyboardModifiers:
    """
    Calls Qt's 'Qt::KeyboardModifiers QKeyEvent::modifiers() const'.

    Qt's own words: https://doc.qt.io/qt-6/qkeyevent.html#modifiers

    Returns
    -------

    Qt.KeyboardModifiers
      The value standing for the combination Qt gave back.
    """
    #  Qt::KeyboardModifiers QKeyEvent::modifiers() const
    return Qt.KeyboardModifiers(self.uglySide.call(
        'ritual_ZNK9QKeyEvent9modifiersEv',
    ))

  def text(self) -> str:
    """
    Calls Qt's 'QString QKeyEvent::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qkeyevent.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QKeyEvent::text() const
    return self.uglySide.call('ritual_ZNK9QKeyEvent4textEv')

  def isAutoRepeat(self) -> bool:
    """
    Calls Qt's 'bool QKeyEvent::isAutoRepeat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qkeyevent.html#isAutoRepeat
    """
    #  bool QKeyEvent::isAutoRepeat() const
    return self.uglySide.call('ritual_ZNK9QKeyEvent12isAutoRepeatEv')

  def count(self) -> int:
    """
    Calls Qt's 'int QKeyEvent::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qkeyevent.html#count
    """
    #  int QKeyEvent::count() const
    return self.uglySide.call('ritual_ZNK9QKeyEvent5countEv')

  def nativeScanCode(self) -> int:
    """
    Calls Qt's 'quint32 QKeyEvent::nativeScanCode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qkeyevent.html#nativeScanCode
    """
    #  quint32 QKeyEvent::nativeScanCode() const
    return self.uglySide.call('ritual_ZNK9QKeyEvent14nativeScanCodeEv')

  def nativeVirtualKey(self) -> int:
    """
    Calls Qt's 'quint32 QKeyEvent::nativeVirtualKey() const'.

    Qt's own words: https://doc.qt.io/qt-6/qkeyevent.html#nativeVirtualKey
    """
    #  quint32 QKeyEvent::nativeVirtualKey() const
    return self.uglySide.call('ritual_ZNK9QKeyEvent16nativeVirtualKeyEv')

  def nativeModifiers(self) -> int:
    """
    Calls Qt's 'quint32 QKeyEvent::nativeModifiers() const'.

    Qt's own words: https://doc.qt.io/qt-6/qkeyevent.html#nativeModifiers
    """
    #  quint32 QKeyEvent::nativeModifiers() const
    return self.uglySide.call('ritual_ZNK9QKeyEvent15nativeModifiersEv')

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

  @overload(QEvent.Type, int, Qt.KeyboardModifiers)
  @overload(QEvent.Type, int, Qt.KeyboardModifiers, str)
  @overload(QEvent.Type, int, Qt.KeyboardModifiers, str, bool)
  @overload(QEvent.Type, int, Qt.KeyboardModifiers, str, bool, int)
  def __init__(
      self,
      type: QEvent.Type,
      key: int,
      modifiers: Qt.KeyboardModifiers,
      text: str = '',
      autorep: bool = False,
      count: int = 1,
  ) -> None:
    """
    Notes what was given, for Qt's 'QKeyEvent::QKeyEvent(Type type, int key,
    Qt::KeyboardModifiers modifiers, const QString &text, bool autorep,
    quint16 count)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qkeyevent.html#QKeyEvent

    Parameters
    ----------

    type : QEvent.Type
      Passed on as its number.

    key : int
      Passed on as it is.

    modifiers : Qt.KeyboardModifiers
      Passed on as its number.

    text : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    autorep : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    count : int
      Passed on as it is. May be left out, as in Qt: it is then 1.
    """
    #  QKeyEvent::QKeyEvent(Type type, int key, Qt::KeyboardModifiers
    #      modifiers, const QString &text, bool autorep, quint16 count)
    self._noteCreation(QKeyEvent, lambda: Rituals.call(
        'ritual_ZN9QKeyEventC1EN6QEvent4TypeEi6QFlagsIN2Qt16KeyboardModifie'
        'rEERK7QStringbt',
        type.value, key, modifiers.value, text, autorep, count,
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
