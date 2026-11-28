"""
QQuickKeyEvent binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickevents_p_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickKeyEvent to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
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


class QQuickKeyEvent(QObject):
  """
  The cute side of Qt's QQuickKeyEvent: a plain Python object standing in
  front of one C++ QQuickKeyEvent.

  It is built on the cute 'QObject', as Qt's QQuickKeyEvent is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickKeyEvent that has a ritual and that Python can
  call so far, 12 names in all: 'metaObject', 'tr', 'reset', 'key', 'text',
  'modifiers', 'isAutoRepeat', 'count', 'nativeScanCode', 'isAccepted',
  'setAccepted', 'matches'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickKeyEvent::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickKeyEvent::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickKeyEvent::qt_qmlMarker_uncreatable()': one of Qt's own
    inner workings.
  - Qt's 'void QQuickKeyEvent::reset(const QKeyEvent &ke)': takes a type
    Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 19 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickKeyEvent is created at the first use, not by
    'QQuickKeyEvent(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickKeyEvent.
  - Qt tells when it has removed the C++ QQuickKeyEvent. Every call on the
    cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuickKeyEvent::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickkeyevent.html#tr

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
    #  QString QQuickKeyEvent::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QQuickKeyEvent2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickKeyEvent'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickKeyEvent::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickkeyevent.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickKeyEvent::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QQuickKeyEvent10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def key(self) -> int:
    """
    Calls Qt's 'int QQuickKeyEvent::key() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickkeyevent.html#key
    """
    #  int QQuickKeyEvent::key() const
    return self.uglySide.call('ritual_ZNK14QQuickKeyEvent3keyEv')

  def text(self) -> str:
    """
    Calls Qt's 'QString QQuickKeyEvent::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickkeyevent.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickKeyEvent::text() const
    return self.uglySide.call('ritual_ZNK14QQuickKeyEvent4textEv')

  def modifiers(self) -> int:
    """
    Calls Qt's 'int QQuickKeyEvent::modifiers() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickkeyevent.html#modifiers
    """
    #  int QQuickKeyEvent::modifiers() const
    return self.uglySide.call('ritual_ZNK14QQuickKeyEvent9modifiersEv')

  def isAutoRepeat(self) -> bool:
    """
    Calls Qt's 'bool QQuickKeyEvent::isAutoRepeat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickkeyevent.html#isAutoRepeat
    """
    #  bool QQuickKeyEvent::isAutoRepeat() const
    return self.uglySide.call('ritual_ZNK14QQuickKeyEvent12isAutoRepeatEv')

  def count(self) -> int:
    """
    Calls Qt's 'int QQuickKeyEvent::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickkeyevent.html#count
    """
    #  int QQuickKeyEvent::count() const
    return self.uglySide.call('ritual_ZNK14QQuickKeyEvent5countEv')

  def nativeScanCode(self) -> int:
    """
    Calls Qt's 'quint32 QQuickKeyEvent::nativeScanCode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickkeyevent.html#nativeScanCode
    """
    #  quint32 QQuickKeyEvent::nativeScanCode() const
    return self.uglySide.call('ritual_ZNK14QQuickKeyEvent14nativeScanCodeEv')

  @overload(QKeySequence.StandardKey)
  def matches(self, key: QKeySequence.StandardKey) -> bool:
    """
    Calls Qt's 'bool QQuickKeyEvent::matches(QKeySequence::StandardKey key)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickkeyevent.html#matches

    Parameters
    ----------

    key : QKeySequence.StandardKey
      Passed on as its number.
    """
    #  bool QQuickKeyEvent::matches(QKeySequence::StandardKey key) const
    return self.uglySide.call(
        'ritual_ZNK14QQuickKeyEvent7matchesEN12QKeySequence11StandardKeyE',
        key.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setAccepted(self, accepted: bool) -> None:
    """
    Calls Qt's 'void QQuickKeyEvent::setAccepted(bool accepted)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickkeyevent.html#setAccepted

    Parameters
    ----------

    accepted : bool
      Passed on as it is.
    """
    #  void QQuickKeyEvent::setAccepted(bool accepted)
    self.uglySide.call('ritual_ZN14QQuickKeyEvent11setAcceptedEb', accepted)

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
    Notes what was given, for Qt's 'QQuickKeyEvent::QQuickKeyEvent()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickkeyevent.html#QQuickKeyEvent
    """
    #  QQuickKeyEvent::QQuickKeyEvent()
    self._noteCreation(QQuickKeyEvent, lambda: Rituals.call(
        'ritual_ZN14QQuickKeyEventC1Ev',
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

  @overload(QEvent.Type, int, Qt.KeyboardModifiers)
  @overload(QEvent.Type, int, Qt.KeyboardModifiers, str)
  @overload(QEvent.Type, int, Qt.KeyboardModifiers, str, bool)
  @overload(QEvent.Type, int, Qt.KeyboardModifiers, str, bool, int)
  def reset(
      self,
      type: QEvent.Type,
      key: int,
      modifiers: Qt.KeyboardModifiers,
      text: str = '',
      autorep: bool = False,
      count: int = 1,
  ) -> None:
    """
    Calls Qt's 'void QQuickKeyEvent::reset(QEvent::Type type, int key,
    Qt::KeyboardModifiers modifiers, const QString &text, bool autorep,
    ushort count)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickkeyevent.html#reset

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
    #  void QQuickKeyEvent::reset(QEvent::Type type, int key,
    #      Qt::KeyboardModifiers modifiers, const QString &text, bool
    #      autorep, ushort count)
    self.uglySide.call(
        'ritual_ZN14QQuickKeyEvent5resetEN6QEvent4TypeEi6QFlagsIN2Qt16Keybo'
        'ardModifierEERK7QStringbt',
        type.value, key, modifiers.value, text, autorep, count,
    )

  def isAccepted(self) -> bool:
    """
    Calls Qt's 'bool QQuickKeyEvent::isAccepted()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickkeyevent.html#isAccepted
    """
    #  bool QQuickKeyEvent::isAccepted()
    return self.uglySide.call('ritual_ZN14QQuickKeyEvent10isAcceptedEv')
