"""
QQuickToolTipAttached binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktooltip_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickToolTipAttached to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin
from ..occult import Rituals
from ..QtCore import QObject
from ..QtQml import QQmlParserStatus
from ..QtQuick import QtPrivate
from . import QQuickToolTip

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QQuickToolTipAttachedPrivate

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickToolTipAttached(QtPrivate.QQuickAttachedPropertyPropagator, QQmlParserStatus):
  """
  The cute side of Qt's QQuickToolTipAttached: a plain Python object standing
  in front of one C++ QQuickToolTipAttached.

  It is built on the cute 'QtPrivate::QQuickAttachedPropertyPropagator', as
  Qt's QQuickToolTipAttached is built on Qt's
  QtPrivate::QQuickAttachedPropertyPropagator, and has everything that class
  has. It is built on the cute 'QQmlParserStatus' as well, as Qt's
  QQuickToolTipAttached is built on Qt's QQmlParserStatus too, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickToolTipAttached that has a ritual and that
  Python can call so far, 25 names in all: 'metaObject', 'tr', 'text',
  'setText', 'delay', 'setDelay', 'timeout', 'setTimeout', 'isVisible',
  'setVisible', 'toolTip', 'policy', 'setVisiblePolicy',
  'resetVisiblePolicy', 'textChanged', 'delayChanged', 'timeoutChanged',
  'visibleChanged', 'policyChanged', 'show', 'hide', 'attachedParentChange',
  'classBegin', 'componentComplete', 'd_func'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickToolTipAttached::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickToolTipAttached::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickToolTipAttached::qt_qmlMarker_anonymous()': one of Qt's
    own inner workings.
  - Qt's 'const QQuickToolTipAttachedPrivate *QQuickToolTipAttached::d_func()
    const': takes in Python what 'QQuickToolTipAttachedPrivate
    *QQuickToolTipAttached::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 34 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickToolTipAttached is created at the first use, not by
    'QQuickToolTipAttached(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickToolTipAttached.
  - Qt tells when it has removed the C++ QQuickToolTipAttached. Every call on
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
    Calls Qt's 'QString QQuickToolTipAttached::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktooltipattached.html#tr

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
    #  QString QQuickToolTipAttached::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QQuickToolTipAttached2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickToolTipAttached'

  #  Qt's QQuickToolTipAttached is built on more than one class. The part of
  #  a C++ QQuickToolTipAttached that belongs to a class after the first
  #  begins somewhere inside the object, and the ritual named for that class
  #  gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus':
          'ritual_cast_QQuickToolTipAttached_QQmlParserStatus',
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickToolTipAttached::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktooltipattached.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickToolTipAttached::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickToolTipAttached10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def text(self) -> str:
    """
    Calls Qt's 'QString QQuickToolTipAttached::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktooltipattached.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickToolTipAttached::text() const
    return self.uglySide.call('ritual_ZNK21QQuickToolTipAttached4textEv')

  def delay(self) -> int:
    """
    Calls Qt's 'int QQuickToolTipAttached::delay() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktooltipattached.html#delay
    """
    #  int QQuickToolTipAttached::delay() const
    return self.uglySide.call('ritual_ZNK21QQuickToolTipAttached5delayEv')

  def timeout(self) -> int:
    """
    Calls Qt's 'int QQuickToolTipAttached::timeout() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktooltipattached.html#timeout
    """
    #  int QQuickToolTipAttached::timeout() const
    return self.uglySide.call('ritual_ZNK21QQuickToolTipAttached7timeoutEv')

  def isVisible(self) -> bool:
    """
    Calls Qt's 'bool QQuickToolTipAttached::isVisible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktooltipattached.html#isVisible
    """
    #  bool QQuickToolTipAttached::isVisible() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickToolTipAttached9isVisibleEv',
    )

  def toolTip(self) -> Optional[QQuickToolTip]:
    """
    Calls Qt's 'QQuickToolTip *QQuickToolTipAttached::toolTip() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktooltipattached.html#toolTip

    Returns
    -------

    Optional[QQuickToolTip]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickToolTip *QQuickToolTipAttached::toolTip() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickToolTipAttached7toolTipEv',
    )
    return QQuickToolTip._cuteAt(address)

  def policy(self) -> QQuickToolTip.Policy:
    """
    Calls Qt's 'QQuickToolTip::Policy QQuickToolTipAttached::policy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktooltipattached.html#policy

    Returns
    -------

    QQuickToolTip.Policy
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuickToolTip.Policy(number)' gives.
    """
    #  QQuickToolTip::Policy QQuickToolTipAttached::policy() const
    return QQuickToolTip.Policy(self.uglySide.call(
        'ritual_ZNK21QQuickToolTipAttached6policyEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setText(self, text: str) -> None:
    """
    Calls Qt's 'void QQuickToolTipAttached::setText(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktooltipattached.html#setText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickToolTipAttached::setText(const QString &text)
    self.uglySide.call(
        'ritual_ZN21QQuickToolTipAttached7setTextERK7QString', text,
    )

  @overload(int)
  def setDelay(self, delay: int) -> None:
    """
    Calls Qt's 'void QQuickToolTipAttached::setDelay(int delay)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktooltipattached.html#setDelay

    Parameters
    ----------

    delay : int
      Passed on as it is.
    """
    #  void QQuickToolTipAttached::setDelay(int delay)
    self.uglySide.call('ritual_ZN21QQuickToolTipAttached8setDelayEi', delay)

  @overload(int)
  def setTimeout(self, timeout: int) -> None:
    """
    Calls Qt's 'void QQuickToolTipAttached::setTimeout(int timeout)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktooltipattached.html#setTimeout

    Parameters
    ----------

    timeout : int
      Passed on as it is.
    """
    #  void QQuickToolTipAttached::setTimeout(int timeout)
    self.uglySide.call(
        'ritual_ZN21QQuickToolTipAttached10setTimeoutEi', timeout,
    )

  @overload(bool)
  def setVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QQuickToolTipAttached::setVisible(bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktooltipattached.html#setVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QQuickToolTipAttached::setVisible(bool visible)
    self.uglySide.call(
        'ritual_ZN21QQuickToolTipAttached10setVisibleEb', visible,
    )

  @overload(QQuickToolTip.Policy)
  def setVisiblePolicy(self, policy: QQuickToolTip.Policy) -> None:
    """
    Calls Qt's 'void
    QQuickToolTipAttached::setVisiblePolicy(QQuickToolTip::Policy policy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktooltipattached.html#setVisiblePolicy

    Parameters
    ----------

    policy : QQuickToolTip.Policy
      Passed on as its number.
    """
    #  void QQuickToolTipAttached::setVisiblePolicy(QQuickToolTip::Policy
    #      policy)
    self.uglySide.call(
        'ritual_ZN21QQuickToolTipAttached16setVisiblePolicyEN13QQuickToolTi'
        'p6PolicyE',
        policy.value,
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
    Notes what was given, for Qt's
    'QQuickToolTipAttached::QQuickToolTipAttached(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktooltipattached.html#QQuickToolTipAttached

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickToolTipAttached::QQuickToolTipAttached(QObject *parent)
    self._noteCreation(QQuickToolTipAttached, lambda: Rituals.call(
        'ritual_ZN21QQuickToolTipAttachedC1EP7QObject',
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

  def resetVisiblePolicy(self) -> None:
    """
    Calls Qt's 'void QQuickToolTipAttached::resetVisiblePolicy()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktooltipattached.html#resetVisiblePolicy
    """
    #  void QQuickToolTipAttached::resetVisiblePolicy()
    self.uglySide.call(
        'ritual_ZN21QQuickToolTipAttached18resetVisiblePolicyEv',
    )

  def textChanged(self) -> None:
    """
    Calls Qt's 'void QQuickToolTipAttached::textChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktooltipattached.html#textChanged
    """
    #  void QQuickToolTipAttached::textChanged()
    self.uglySide.call('ritual_ZN21QQuickToolTipAttached11textChangedEv')

  def delayChanged(self) -> None:
    """
    Calls Qt's 'void QQuickToolTipAttached::delayChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktooltipattached.html#delayChanged
    """
    #  void QQuickToolTipAttached::delayChanged()
    self.uglySide.call('ritual_ZN21QQuickToolTipAttached12delayChangedEv')

  def timeoutChanged(self) -> None:
    """
    Calls Qt's 'void QQuickToolTipAttached::timeoutChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktooltipattached.html#timeoutChanged
    """
    #  void QQuickToolTipAttached::timeoutChanged()
    self.uglySide.call('ritual_ZN21QQuickToolTipAttached14timeoutChangedEv')

  def visibleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickToolTipAttached::visibleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktooltipattached.html#visibleChanged
    """
    #  void QQuickToolTipAttached::visibleChanged()
    self.uglySide.call('ritual_ZN21QQuickToolTipAttached14visibleChangedEv')

  def policyChanged(self) -> None:
    """
    Calls Qt's 'void QQuickToolTipAttached::policyChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktooltipattached.html#policyChanged
    """
    #  void QQuickToolTipAttached::policyChanged()
    self.uglySide.call('ritual_ZN21QQuickToolTipAttached13policyChangedEv')

  @overload(str)
  @overload(str, int)
  def show(self, text: str, ms: int = -1) -> None:
    """
    Calls Qt's 'void QQuickToolTipAttached::show(const QString &text, int
    ms)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktooltipattached.html#show

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    ms : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  void QQuickToolTipAttached::show(const QString &text, int ms)
    self.uglySide.call(
        'ritual_ZN21QQuickToolTipAttached4showERK7QStringi', text, ms,
    )

  def hide(self) -> None:
    """
    Calls Qt's 'void QQuickToolTipAttached::hide()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktooltipattached.html#hide
    """
    #  void QQuickToolTipAttached::hide()
    self.uglySide.call('ritual_ZN21QQuickToolTipAttached4hideEv')

  @overload(
      QtPrivate.QQuickAttachedPropertyPropagator,
      QtPrivate.QQuickAttachedPropertyPropagator,
  )
  @overload(QtPrivate.QQuickAttachedPropertyPropagator, NoneType)
  @overload(NoneType, QtPrivate.QQuickAttachedPropertyPropagator)
  @overload(NoneType, NoneType)
  def attachedParentChange(
      self,
      newParent: Optional[QtPrivate.QQuickAttachedPropertyPropagator],
      oldParent: Optional[QtPrivate.QQuickAttachedPropertyPropagator],
  ) -> None:
    """
    Calls Qt's 'void QQuickToolTipAttached::attachedParentChange(
    QQuickAttachedPropertyPropagator *newParent,
    QQuickAttachedPropertyPropagator *oldParent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktooltipattached.html#attachedParentChange

    Parameters
    ----------

    newParent : Optional[QtPrivate.QQuickAttachedPropertyPropagator]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    oldParent : Optional[QtPrivate.QQuickAttachedPropertyPropagator]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickToolTipAttached::attachedParentChange(
    #      QQuickAttachedPropertyPropagator *newParent,
    #      QQuickAttachedPropertyPropagator *oldParent)
    ritual = (
        'ritual_ZN21QQuickToolTipAttached20attachedParentChangeEPN9QtPrivat'
        'e32QQuickAttachedPropertyPropagatorES2_')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QQuickToolTipAttached20attachedParentChangeEPN9Qt'
          'Private32QQuickAttachedPropertyPropagatorES2_')
    self.uglySide.call(
        ritual, self._addressOf(newParent), self._addressOf(oldParent),
    )

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQuickToolTipAttached::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktooltipattached.html#classBegin
    """
    #  void QQuickToolTipAttached::classBegin()
    ritual = 'ritual_ZN21QQuickToolTipAttached10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QQuickToolTipAttached10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickToolTipAttached::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktooltipattached.html#componentComplete
    """
    #  void QQuickToolTipAttached::componentComplete()
    ritual = 'ritual_ZN21QQuickToolTipAttached17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QQuickToolTipAttached17componentCompleteEv'
    self.uglySide.call(ritual)

  def d_func(self) -> Optional[QQuickToolTipAttachedPrivate]:
    """
    Calls Qt's 'QQuickToolTipAttachedPrivate
    *QQuickToolTipAttached::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktooltipattached.html#d_func

    Returns
    -------

    Optional[QQuickToolTipAttachedPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickToolTipAttachedPrivate *QQuickToolTipAttached::d_func()
    address = self.uglySide.call('ritual_ZN21QQuickToolTipAttached6d_funcEv')
    from . import QQuickToolTipAttachedPrivate
    return QQuickToolTipAttachedPrivate._cuteAt(address)
