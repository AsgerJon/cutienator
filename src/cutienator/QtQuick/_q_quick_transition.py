"""
QQuickTransition binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquicktransition_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickTransition to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickTransition(QObject):
  """
  The cute side of Qt's QQuickTransition: a plain Python object standing in
  front of one C++ QQuickTransition.

  It is built on the cute 'QObject', as Qt's QQuickTransition is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickTransition that has a ritual and that Python
  can call so far, 17 names in all: 'metaObject', 'tr', 'fromState',
  'setFromState', 'toState', 'setToState', 'reversible', 'setReversible',
  'enabled', 'setEnabled', 'running', 'setReversed', 'fromChanged',
  'toChanged', 'reversibleChanged', 'enabledChanged', 'runningChanged'. It
  can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickTransition::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickTransition::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickTransitionPrivate *QQuickTransition::d_func()': gives
    'QQuickTransitionPrivate', which has no cute class yet.
  - Qt's 'const QQuickTransitionPrivate *QQuickTransition::d_func() const':
    gives 'QQuickTransitionPrivate', which has no cute class yet.
  - Qt's 'QQuickTransition::~QQuickTransition()': the destructor: Python
    never removes a C++ QQuickTransition.
  - Qt's 'QQmlListProperty<QQuickAbstractAnimation>
    QQuickTransition::animations()': gives a type Python has no way to take
    yet.
  - Qt's 'QQuickTransitionInstance
    *QQuickTransition::prepare(QQuickStateOperation::ActionList &actions,
    QList<QQmlProperty> &after, QQuickTransitionManager *end, QObject
    *defaultTarget)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 27 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickTransition is created at the first use, not by
    'QQuickTransition(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickTransition.
  - Qt tells when it has removed the C++ QQuickTransition. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickTransition that has no cute function yet,
    'animations', 'prepare', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QQuickTransition::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktransition.html#tr

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
    #  QString QQuickTransition::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QQuickTransition2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickTransition'

  #  A C++ QQuickTransition Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickTransition'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickTransition::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktransition.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickTransition::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QQuickTransition10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def fromState(self) -> str:
    """
    Calls Qt's 'QString QQuickTransition::fromState() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktransition.html#fromState

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickTransition::fromState() const
    return self.uglySide.call('ritual_ZNK16QQuickTransition9fromStateEv')

  def toState(self) -> str:
    """
    Calls Qt's 'QString QQuickTransition::toState() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktransition.html#toState

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickTransition::toState() const
    return self.uglySide.call('ritual_ZNK16QQuickTransition7toStateEv')

  def reversible(self) -> bool:
    """
    Calls Qt's 'bool QQuickTransition::reversible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktransition.html#reversible
    """
    #  bool QQuickTransition::reversible() const
    return self.uglySide.call('ritual_ZNK16QQuickTransition10reversibleEv')

  def enabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickTransition::enabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktransition.html#enabled
    """
    #  bool QQuickTransition::enabled() const
    return self.uglySide.call('ritual_ZNK16QQuickTransition7enabledEv')

  def running(self) -> bool:
    """
    Calls Qt's 'bool QQuickTransition::running() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktransition.html#running
    """
    #  bool QQuickTransition::running() const
    return self.uglySide.call('ritual_ZNK16QQuickTransition7runningEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setFromState(self, a0: str) -> None:
    """
    Calls Qt's 'void QQuickTransition::setFromState(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktransition.html#setFromState

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickTransition::setFromState(const QString &a0)
    self.uglySide.call(
        'ritual_ZN16QQuickTransition12setFromStateERK7QString', a0,
    )

  @overload(str)
  def setToState(self, a0: str) -> None:
    """
    Calls Qt's 'void QQuickTransition::setToState(const QString &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktransition.html#setToState

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickTransition::setToState(const QString &a0)
    self.uglySide.call(
        'ritual_ZN16QQuickTransition10setToStateERK7QString', a0,
    )

  @overload(bool)
  def setReversible(self, a0: bool) -> None:
    """
    Calls Qt's 'void QQuickTransition::setReversible(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktransition.html#setReversible

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QQuickTransition::setReversible(bool a0)
    self.uglySide.call('ritual_ZN16QQuickTransition13setReversibleEb', a0)

  @overload(bool)
  def setEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickTransition::setEnabled(bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktransition.html#setEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickTransition::setEnabled(bool enabled)
    self.uglySide.call('ritual_ZN16QQuickTransition10setEnabledEb', enabled)

  @overload(bool)
  def setReversed(self, r: bool) -> None:
    """
    Calls Qt's 'void QQuickTransition::setReversed(bool r)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktransition.html#setReversed

    Parameters
    ----------

    r : bool
      Passed on as it is.
    """
    #  void QQuickTransition::setReversed(bool r)
    self.uglySide.call('ritual_ZN16QQuickTransition11setReversedEb', r)

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
    Notes what was given, for Qt's
    'QQuickTransition::QQuickTransition(QObject *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktransition.html#QQuickTransition

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickTransition::QQuickTransition(QObject *parent)
    self._noteCreation(QQuickTransition, lambda: Rituals.call(
        'ritual_ZN16QQuickTransitionC1EP7QObject',
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

  def fromChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTransition::fromChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktransition.html#fromChanged
    """
    #  void QQuickTransition::fromChanged()
    self.uglySide.call('ritual_ZN16QQuickTransition11fromChangedEv')

  def toChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTransition::toChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktransition.html#toChanged
    """
    #  void QQuickTransition::toChanged()
    self.uglySide.call('ritual_ZN16QQuickTransition9toChangedEv')

  def reversibleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTransition::reversibleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktransition.html#reversibleChanged
    """
    #  void QQuickTransition::reversibleChanged()
    self.uglySide.call('ritual_ZN16QQuickTransition17reversibleChangedEv')

  def enabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTransition::enabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktransition.html#enabledChanged
    """
    #  void QQuickTransition::enabledChanged()
    self.uglySide.call('ritual_ZN16QQuickTransition14enabledChangedEv')

  def runningChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTransition::runningChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktransition.html#runningChanged
    """
    #  void QQuickTransition::runningChanged()
    self.uglySide.call('ritual_ZN16QQuickTransition14runningChangedEv')

  @staticmethod
  def animations(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQuickAbstractAnimation>
    QQuickTransition::animations()': gives a type Python has no way to take
    yet.
    """
    raise NotImplementedError(
        "'QQuickTransition.animations' has no cute function yet. Qt's "
        "'QQmlListProperty<QQuickAbstractAnimation> "
        "QQuickTransition::animations()': gives a type Python has no way to "
        "take yet.")

  @staticmethod
  def prepare(*__, **_) -> Never:
    """
    Qt's 'QQuickTransitionInstance
    *QQuickTransition::prepare(QQuickStateOperation::ActionList &actions,
    QList<QQmlProperty> &after, QQuickTransitionManager *end, QObject
    *defaultTarget)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQuickTransition.prepare' has no cute function yet. Qt's "
        "'QQuickTransitionInstance "
        "*QQuickTransition::prepare(QQuickStateOperation::ActionList "
        "&actions, QList<QQmlProperty> &after, QQuickTransitionManager "
        "*end, QObject *defaultTarget)': takes a type Python has no way to "
        "hand over yet.")
