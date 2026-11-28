"""
Qt3DInput::QKeyEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DInput/qkeyevent.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import Qt, QEvent, QObject
from ..QtGui import QKeySequence

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QKeyEvent(QObject):
  """
  The cute side of Qt's Qt3DInput::QKeyEvent: a plain Python object standing
  in front of one C++ Qt3DInput::QKeyEvent.

  It is built on the cute 'QObject', as Qt's Qt3DInput::QKeyEvent is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DInput::QKeyEvent that has a ritual and that
  Python can call so far, 12 names in all: 'metaObject', 'tr', 'key', 'text',
  'modifiers', 'isAutoRepeat', 'count', 'nativeScanCode', 'isAccepted',
  'setAccepted', 'type', 'matches'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DInput::QKeyEvent::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int Qt3DInput::QKeyEvent::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DInput::QKeyEvent::~QKeyEvent()': the destructor: Python never
    removes a C++ Qt3DInput::QKeyEvent.

  What has no ritual
  ------------------

  3 of the 19 functions Qt declares: 2 not a gap; 1 the compiler refuses its
  ritual as it would be written here.

  What to expect
  --------------

  - The C++ Qt3DInput::QKeyEvent is created at the first use, not by
    'Qt3DInput::QKeyEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DInput::QKeyEvent.
  - Qt tells when it has removed the C++ Qt3DInput::QKeyEvent. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString Qt3DInput::QKeyEvent::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qkeyevent.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DInput::QKeyEvent::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN9Qt3DInput9QKeyEvent2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DInput::QKeyEvent'

  #  A C++ Qt3DInput::QKeyEvent Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DInput_QKeyEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DInput::QKeyEvent::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyevent.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DInput::QKeyEvent::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK9Qt3DInput9QKeyEvent10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def key(self) -> int:
    """
    Calls Qt's 'int Qt3DInput::QKeyEvent::key() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qkeyevent.html#key
    """
    #  int Qt3DInput::QKeyEvent::key() const
    return self.uglySide.call('ritual_ZNK9Qt3DInput9QKeyEvent3keyEv')

  def text(self) -> str:
    """
    Calls Qt's 'QString Qt3DInput::QKeyEvent::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qkeyevent.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DInput::QKeyEvent::text() const
    return self.uglySide.call('ritual_ZNK9Qt3DInput9QKeyEvent4textEv')

  def modifiers(self) -> int:
    """
    Calls Qt's 'int Qt3DInput::QKeyEvent::modifiers() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qkeyevent.html#modifiers
    """
    #  int Qt3DInput::QKeyEvent::modifiers() const
    return self.uglySide.call('ritual_ZNK9Qt3DInput9QKeyEvent9modifiersEv')

  def isAutoRepeat(self) -> bool:
    """
    Calls Qt's 'bool Qt3DInput::QKeyEvent::isAutoRepeat() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyevent.html#isAutoRepeat
    """
    #  bool Qt3DInput::QKeyEvent::isAutoRepeat() const
    return self.uglySide.call(
        'ritual_ZNK9Qt3DInput9QKeyEvent12isAutoRepeatEv',
    )

  def count(self) -> int:
    """
    Calls Qt's 'int Qt3DInput::QKeyEvent::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qkeyevent.html#count
    """
    #  int Qt3DInput::QKeyEvent::count() const
    return self.uglySide.call('ritual_ZNK9Qt3DInput9QKeyEvent5countEv')

  def nativeScanCode(self) -> int:
    """
    Calls Qt's 'quint32 Qt3DInput::QKeyEvent::nativeScanCode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyevent.html#nativeScanCode
    """
    #  quint32 Qt3DInput::QKeyEvent::nativeScanCode() const
    return self.uglySide.call(
        'ritual_ZNK9Qt3DInput9QKeyEvent14nativeScanCodeEv',
    )

  def isAccepted(self) -> bool:
    """
    Calls Qt's 'bool Qt3DInput::QKeyEvent::isAccepted() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyevent.html#isAccepted
    """
    #  bool Qt3DInput::QKeyEvent::isAccepted() const
    return self.uglySide.call('ritual_ZNK9Qt3DInput9QKeyEvent10isAcceptedEv')

  def type(self) -> QEvent.Type:
    """
    Calls Qt's 'QEvent::Type Qt3DInput::QKeyEvent::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qkeyevent.html#type

    Returns
    -------

    QEvent.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QEvent.Type(number)'
      gives.
    """
    #  QEvent::Type Qt3DInput::QKeyEvent::type() const
    return QEvent.Type(self.uglySide.call(
        'ritual_ZNK9Qt3DInput9QKeyEvent4typeEv',
    ))

  @overload(QKeySequence.StandardKey)
  def matches(self, key_: QKeySequence.StandardKey) -> bool:
    """
    Calls Qt's 'bool Qt3DInput::QKeyEvent::matches(QKeySequence::StandardKey
    key_) const'.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qkeyevent.html#matches

    Parameters
    ----------

    key_ : QKeySequence.StandardKey
      Passed on as its number.
    """
    #  bool Qt3DInput::QKeyEvent::matches(QKeySequence::StandardKey key_)
    #      const
    return self.uglySide.call(
        'ritual_ZNK9Qt3DInput9QKeyEvent7matchesEN12QKeySequence11StandardKe'
        'yE',
        key_.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setAccepted(self, accepted: bool) -> None:
    """
    Calls Qt's 'void Qt3DInput::QKeyEvent::setAccepted(bool accepted)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dinput-qkeyevent.html#setAccepted

    Parameters
    ----------

    accepted : bool
      Passed on as it is.
    """
    #  void Qt3DInput::QKeyEvent::setAccepted(bool accepted)
    self.uglySide.call(
        'ritual_ZN9Qt3DInput9QKeyEvent11setAcceptedEb', accepted,
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
    Notes what was given, for Qt's
    'Qt3DInput::QKeyEvent::QKeyEvent(QEvent::Type type, int key,
    Qt::KeyboardModifiers modifiers, const QString &text, bool autorep,
    ushort count)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qt3dinput-qkeyevent.html#QKeyEvent

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
    #  Qt3DInput::QKeyEvent::QKeyEvent(QEvent::Type type, int key,
    #      Qt::KeyboardModifiers modifiers, const QString &text, bool
    #      autorep, ushort count)
    self._noteCreation(QKeyEvent, lambda: Rituals.call(
        'ritual_ZN9Qt3DInput9QKeyEventC1EN6QEvent4TypeEi6QFlagsIN2Qt16Keybo'
        'ardModifierEERK7QStringbt',
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
