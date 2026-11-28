"""
QQmlConnections binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlMeta/6.12.0/QtQmlMeta/private/qqmlconnections_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQmlConnections to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject
from ..QtQml import QQmlParserStatus

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlConnections(QObject, QQmlParserStatus):
  """
  The cute side of Qt's QQmlConnections: a plain Python object standing in
  front of one C++ QQmlConnections.

  It is built on the cute 'QObject', as Qt's QQmlConnections is built on Qt's
  QObject, and has everything that class has. It is built on the cute
  'QQmlParserStatus' as well, as Qt's QQmlConnections is built on Qt's
  QQmlParserStatus too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlConnections that has a ritual and that Python
  can call so far, 15 names in all: 'metaObject', 'tr', 'target',
  'setTarget', 'isEnabled', 'setEnabled', 'ignoreUnknownSignals',
  'setIgnoreUnknownSignals', 'classBegin', 'componentComplete',
  'targetChanged', 'enabledChanged', 'connectSignals',
  'connectSignalsToMethods', 'connectSignalsToBindings'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlConnections::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQmlConnections::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlConnectionsPrivate *QQmlConnections::d_func()': gives
    'QQmlConnectionsPrivate', which has no cute class yet.
  - Qt's 'const QQmlConnectionsPrivate *QQmlConnections::d_func() const':
    gives 'QQmlConnectionsPrivate', which has no cute class yet.
  - Qt's 'QQmlConnections::~QQmlConnections()': the destructor: Python never
    removes a C++ QQmlConnections.

  What has no ritual
  ------------------

  2 of the 23 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQmlConnections is created at the first use, not by
    'QQmlConnections(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlConnections.
  - Qt tells when it has removed the C++ QQmlConnections. Every call on the
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
    Calls Qt's 'QString QQmlConnections::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlconnections.html#tr

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
    #  QString QQmlConnections::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QQmlConnections2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlConnections'

  #  Qt's QQmlConnections is built on more than one class. The part of a C++
  #  QQmlConnections that belongs to a class after the first begins somewhere
  #  inside the object, and the ritual named for that class gives where; see
  #  'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus': 'ritual_cast_QQmlConnections_QQmlParserStatus',
  }

  #  A C++ QQmlConnections Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlConnections'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlConnections::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlconnections.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlConnections::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QQmlConnections10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def target(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QQmlConnections::target() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlconnections.html#target

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QQmlConnections::target() const
    address = self.uglySide.call('ritual_ZNK15QQmlConnections6targetEv')
    return QObject._cuteAt(address)

  def isEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQmlConnections::isEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlconnections.html#isEnabled
    """
    #  bool QQmlConnections::isEnabled() const
    return self.uglySide.call('ritual_ZNK15QQmlConnections9isEnabledEv')

  def ignoreUnknownSignals(self) -> bool:
    """
    Calls Qt's 'bool QQmlConnections::ignoreUnknownSignals() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlconnections.html#ignoreUnknownSignals
    """
    #  bool QQmlConnections::ignoreUnknownSignals() const
    return self.uglySide.call(
        'ritual_ZNK15QQmlConnections20ignoreUnknownSignalsEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QObject)
  @overload(NoneType)
  def setTarget(self, a0: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQmlConnections::setTarget(QObject *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlconnections.html#setTarget

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlConnections::setTarget(QObject *a0)
    self.uglySide.call(
        'ritual_ZN15QQmlConnections9setTargetEP7QObject',
        self._addressOf(a0, 'QObject'),
    )

  @overload(bool)
  def setEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQmlConnections::setEnabled(bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlconnections.html#setEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQmlConnections::setEnabled(bool enabled)
    self.uglySide.call('ritual_ZN15QQmlConnections10setEnabledEb', enabled)

  @overload(bool)
  def setIgnoreUnknownSignals(self, ignore: bool) -> None:
    """
    Calls Qt's 'void QQmlConnections::setIgnoreUnknownSignals(bool ignore)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlconnections.html#setIgnoreUnknownSignals

    Parameters
    ----------

    ignore : bool
      Passed on as it is.
    """
    #  void QQmlConnections::setIgnoreUnknownSignals(bool ignore)
    self.uglySide.call(
        'ritual_ZN15QQmlConnections23setIgnoreUnknownSignalsEb', ignore,
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QQmlConnections::QQmlConnections(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlconnections.html#QQmlConnections

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlConnections::QQmlConnections(QObject *parent)
    self._noteCreation(QQmlConnections, lambda: Rituals.call(
        'ritual_ZN15QQmlConnectionsC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQmlConnections::classBegin()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlconnections.html#classBegin
    """
    #  void QQmlConnections::classBegin()
    ritual = 'ritual_ZN15QQmlConnections10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQmlConnections10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQmlConnections::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlconnections.html#componentComplete
    """
    #  void QQmlConnections::componentComplete()
    ritual = 'ritual_ZN15QQmlConnections17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQmlConnections17componentCompleteEv'
    self.uglySide.call(ritual)

  def targetChanged(self) -> None:
    """
    Calls Qt's 'void QQmlConnections::targetChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlconnections.html#targetChanged
    """
    #  void QQmlConnections::targetChanged()
    self.uglySide.call('ritual_ZN15QQmlConnections13targetChangedEv')

  def enabledChanged(self) -> None:
    """
    Calls Qt's 'void QQmlConnections::enabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlconnections.html#enabledChanged
    """
    #  void QQmlConnections::enabledChanged()
    self.uglySide.call('ritual_ZN15QQmlConnections14enabledChangedEv')

  def connectSignals(self) -> None:
    """
    Calls Qt's 'void QQmlConnections::connectSignals()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlconnections.html#connectSignals
    """
    #  void QQmlConnections::connectSignals()
    self.uglySide.call('ritual_ZN15QQmlConnections14connectSignalsEv')

  def connectSignalsToMethods(self) -> None:
    """
    Calls Qt's 'void QQmlConnections::connectSignalsToMethods()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlconnections.html#connectSignalsToMethods
    """
    #  void QQmlConnections::connectSignalsToMethods()
    self.uglySide.call(
        'ritual_ZN15QQmlConnections23connectSignalsToMethodsEv',
    )

  def connectSignalsToBindings(self) -> None:
    """
    Calls Qt's 'void QQmlConnections::connectSignalsToBindings()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlconnections.html#connectSignalsToBindings
    """
    #  void QQmlConnections::connectSignalsToBindings()
    self.uglySide.call(
        'ritual_ZN15QQmlConnections24connectSignalsToBindingsEv',
    )
