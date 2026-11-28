"""
QQuickToolTipAttachedPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktooltip_p_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickToolTipAttachedPrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtQml import QQml
from ..QtQuick import QtPrivate
from . import QQuickToolTip

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject
  from . import QQuickToolTipAttached
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QObject = WAIT['QObject']
  QQuickToolTipAttached = WAIT['QQuickToolTipAttached']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickToolTipAttachedPrivate(QtPrivate.QQuickAttachedPropertyPropagatorPrivate):
  """
  The cute side of Qt's QQuickToolTipAttachedPrivate: a plain Python object
  standing in front of one C++ QQuickToolTipAttachedPrivate.

  It is built on the cute
  'QtPrivate::QQuickAttachedPropertyPropagatorPrivate', as Qt's
  QQuickToolTipAttachedPrivate is built on Qt's
  QtPrivate::QQuickAttachedPropertyPropagatorPrivate, and has everything that
  class has.

  What exists
  -----------

  Every function of Qt's QQuickToolTipAttachedPrivate that has a ritual and
  that Python can call so far, 13 names in all: 'q_func', 'instance', 'get',
  'maybeSetVisibleImplicitly', 'setVisible', 'isVisibleExplicitlySet',
  'setDelay', 'isDelayExplicitlySet', 'setTimeout', 'isTimeoutExplicitlySet',
  'inheritPolicy', 'propagatePolicy', 'warnIfAttacheeIsNotAnItem'. None can
  be made from Python: one comes out of a function of another class that
  gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickToolTipAttached *QQuickToolTipAttachedPrivate::q_func()
    const': takes in Python what 'QQuickToolTipAttached
    *QQuickToolTipAttachedPrivate::q_func()' takes.

  What has no ritual
  ------------------

  1 of the 15 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QQuickToolTipAttachedPrivate is created at the first use, not by
    'QQuickToolTipAttachedPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickToolTipAttachedPrivate.
  - Each name of Qt's QQuickToolTipAttachedPrivate that has no cute function
    yet, 'calculateTimeout', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QQuickToolTipAttached)
  @overload(NoneType)
  def get(
      toolTipAttached: Optional[QQuickToolTipAttached],
  ) -> Optional[QQuickToolTipAttachedPrivate]:
    """
    Calls Qt's 'QQuickToolTipAttachedPrivate
    *QQuickToolTipAttachedPrivate::get(QQuickToolTipAttached
    *toolTipAttached)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktooltipattachedprivate.html#get

    Parameters
    ----------

    toolTipAttached : Optional[QQuickToolTipAttached]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickToolTipAttachedPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickToolTipAttachedPrivate
    #      *QQuickToolTipAttachedPrivate::get(QQuickToolTipAttached
    #      *toolTipAttached)
    address = Rituals.call(
        'ritual_ZN28QQuickToolTipAttachedPrivate3getEP21QQuickToolTipAttach'
        'ed',
        CuteMixin._addressOf(toolTipAttached),
    )
    return QQuickToolTipAttachedPrivate._cuteAt(address)

  @staticmethod
  @overload(QObject, bool)
  @overload(NoneType, bool)
  def maybeSetVisibleImplicitly(
      attachee: Optional[QObject],
      visible: bool,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickToolTipAttachedPrivate::maybeSetVisibleImplicitly(const QObject
    *attachee, bool visible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktooltipattachedprivate.html

    Parameters
    ----------

    attachee : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    visible : bool
      Passed on as it is.
    """
    #  void QQuickToolTipAttachedPrivate::maybeSetVisibleImplicitly(const
    #      QObject *attachee, bool visible)
    Rituals.call(
        'ritual_ZN28QQuickToolTipAttachedPrivate25maybeSetVisibleImplicitly'
        'EPK7QObjectb',
        CuteMixin._addressOf(attachee, 'QObject'), visible,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickToolTipAttachedPrivate'

  #  A C++ QQuickToolTipAttachedPrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickToolTipAttachedPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def instance(self, create: bool) -> Optional[QQuickToolTip]:
    """
    Calls Qt's 'QQuickToolTip *QQuickToolTipAttachedPrivate::instance(bool
    create) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktooltipattachedprivate.html#instance

    Parameters
    ----------

    create : bool
      Passed on as it is.

    Returns
    -------

    Optional[QQuickToolTip]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickToolTip *QQuickToolTipAttachedPrivate::instance(bool create)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK28QQuickToolTipAttachedPrivate8instanceEb', create,
    )
    return QQuickToolTip._cuteAt(address)

  def isVisibleExplicitlySet(self) -> bool:
    """
    Calls Qt's 'bool QQuickToolTipAttachedPrivate::isVisibleExplicitlySet()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktooltipattachedprivate.html
    """
    #  bool QQuickToolTipAttachedPrivate::isVisibleExplicitlySet() const
    return self.uglySide.call(
        'ritual_ZNK28QQuickToolTipAttachedPrivate22isVisibleExplicitlySetEv',
    )

  def isDelayExplicitlySet(self) -> bool:
    """
    Calls Qt's 'bool QQuickToolTipAttachedPrivate::isDelayExplicitlySet()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktooltipattachedprivate.html
    """
    #  bool QQuickToolTipAttachedPrivate::isDelayExplicitlySet() const
    return self.uglySide.call(
        'ritual_ZNK28QQuickToolTipAttachedPrivate20isDelayExplicitlySetEv',
    )

  def isTimeoutExplicitlySet(self) -> bool:
    """
    Calls Qt's 'bool QQuickToolTipAttachedPrivate::isTimeoutExplicitlySet()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktooltipattachedprivate.html
    """
    #  bool QQuickToolTipAttachedPrivate::isTimeoutExplicitlySet() const
    return self.uglySide.call(
        'ritual_ZNK28QQuickToolTipAttachedPrivate22isTimeoutExplicitlySetEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool, QQml.PropertyUtils.State)
  def setVisible(
      self,
      visible: bool,
      propertyState: QQml.PropertyUtils.State,
  ) -> None:
    """
    Calls Qt's 'void QQuickToolTipAttachedPrivate::setVisible(bool visible,
    QQml::PropertyUtils::State propertyState)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktooltipattachedprivate.html#setVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.

    propertyState : QQml.PropertyUtils.State
      Passed on as its number.
    """
    #  void QQuickToolTipAttachedPrivate::setVisible(bool visible,
    #      QQml::PropertyUtils::State propertyState)
    self.uglySide.call(
        'ritual_ZN28QQuickToolTipAttachedPrivate10setVisibleEbN4QQml13Prope'
        'rtyUtils5StateE',
        visible, propertyState.value,
    )

  @overload(int, QQml.PropertyUtils.State)
  def setDelay(
      self,
      delay: int,
      propertyState: QQml.PropertyUtils.State,
  ) -> None:
    """
    Calls Qt's 'void QQuickToolTipAttachedPrivate::setDelay(int delay,
    QQml::PropertyUtils::State propertyState)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktooltipattachedprivate.html#setDelay

    Parameters
    ----------

    delay : int
      Passed on as it is.

    propertyState : QQml.PropertyUtils.State
      Passed on as its number.
    """
    #  void QQuickToolTipAttachedPrivate::setDelay(int delay,
    #      QQml::PropertyUtils::State propertyState)
    self.uglySide.call(
        'ritual_ZN28QQuickToolTipAttachedPrivate8setDelayEiN4QQml13Property'
        'Utils5StateE',
        delay, propertyState.value,
    )

  @overload(int, QQml.PropertyUtils.State)
  def setTimeout(
      self,
      timeout: int,
      propertyState: QQml.PropertyUtils.State,
  ) -> None:
    """
    Calls Qt's 'void QQuickToolTipAttachedPrivate::setTimeout(int timeout,
    QQml::PropertyUtils::State propertyState)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktooltipattachedprivate.html#setTimeout

    Parameters
    ----------

    timeout : int
      Passed on as it is.

    propertyState : QQml.PropertyUtils.State
      Passed on as its number.
    """
    #  void QQuickToolTipAttachedPrivate::setTimeout(int timeout,
    #      QQml::PropertyUtils::State propertyState)
    self.uglySide.call(
        'ritual_ZN28QQuickToolTipAttachedPrivate10setTimeoutEiN4QQml13Prope'
        'rtyUtils5StateE',
        timeout, propertyState.value,
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

  def q_func(self) -> Optional[QQuickToolTipAttached]:
    """
    Calls Qt's 'QQuickToolTipAttached
    *QQuickToolTipAttachedPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktooltipattachedprivate.html#q_func

    Returns
    -------

    Optional[QQuickToolTipAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickToolTipAttached *QQuickToolTipAttachedPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN28QQuickToolTipAttachedPrivate6q_funcEv',
    )
    from . import QQuickToolTipAttached
    return QQuickToolTipAttached._cuteAt(address)

  @overload(QQuickToolTip.Policy)
  def inheritPolicy(self, policy: QQuickToolTip.Policy) -> None:
    """
    Calls Qt's 'void
    QQuickToolTipAttachedPrivate::inheritPolicy(QQuickToolTip::Policy
    policy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktooltipattachedprivate.html#inheritPolicy

    Parameters
    ----------

    policy : QQuickToolTip.Policy
      Passed on as its number.
    """
    #  void QQuickToolTipAttachedPrivate::inheritPolicy(QQuickToolTip::Policy
    #      policy)
    self.uglySide.call(
        'ritual_ZN28QQuickToolTipAttachedPrivate13inheritPolicyEN13QQuickTo'
        'olTip6PolicyE',
        policy.value,
    )

  def propagatePolicy(self) -> None:
    """
    Calls Qt's 'void QQuickToolTipAttachedPrivate::propagatePolicy()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktooltipattachedprivate.html#propagatePolicy
    """
    #  void QQuickToolTipAttachedPrivate::propagatePolicy()
    self.uglySide.call(
        'ritual_ZN28QQuickToolTipAttachedPrivate15propagatePolicyEv',
    )

  @overload(str)
  def warnIfAttacheeIsNotAnItem(self, functionName: str) -> bool:
    """
    Calls Qt's 'bool
    QQuickToolTipAttachedPrivate::warnIfAttacheeIsNotAnItem(const QString
    &functionName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktooltipattachedprivate.html

    Parameters
    ----------

    functionName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQuickToolTipAttachedPrivate::warnIfAttacheeIsNotAnItem(const
    #      QString &functionName)
    return self.uglySide.call(
        'ritual_ZN28QQuickToolTipAttachedPrivate25warnIfAttacheeIsNotAnItem'
        'ERK7QString',
        functionName,
    )

  @staticmethod
  def calculateTimeout(*__, **_) -> Never:
    """
    Qt's 'int QQuickToolTipAttachedPrivate::calculateTimeout(const QString
    &text)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'qt_quicktooltipattachedprivate_short_timeout'.
    """
    raise NotImplementedError(
        "'QQuickToolTipAttachedPrivate.calculateTimeout' has no cute "
        "function yet. Qt's 'int "
        "QQuickToolTipAttachedPrivate::calculateTimeout(const QString "
        "&text)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'qt_quicktooltipattachedprivate_short_timeout'.")
