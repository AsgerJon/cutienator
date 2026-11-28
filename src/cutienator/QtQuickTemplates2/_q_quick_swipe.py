"""
QQuickSwipe binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickswipe_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickSwipe to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QQuickSwipeDelegate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtQml import QQmlComponent
  from ..QtQuick import QQuickItem, QQuickTransition
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlComponent = WAIT['QQmlComponent']
  QQuickItem = WAIT['QQuickItem']
  QQuickTransition = WAIT['QQuickTransition']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickSwipe(QObject):
  """
  The cute side of Qt's QQuickSwipe: a plain Python object standing in front
  of one C++ QQuickSwipe.

  It is built on the cute 'QObject', as Qt's QQuickSwipe is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickSwipe that has a ritual and that Python can
  call so far, 37 names in all: 'metaObject', 'tr', 'position',
  'setPosition', 'isComplete', 'setComplete', 'left', 'setLeft', 'behind',
  'setBehind', 'right', 'setRight', 'leftItem', 'setLeftItem', 'behindItem',
  'setBehindItem', 'rightItem', 'setRightItem', 'close', 'isEnabled',
  'setEnabled', 'transition', 'setTransition', 'open', 'positionChanged',
  'completeChanged', 'leftChanged', 'behindChanged', 'rightChanged',
  'leftItemChanged', 'behindItemChanged', 'rightItemChanged', 'completed',
  'opened', 'closed', 'enabledChanged', 'transitionChanged'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickSwipe::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickSwipe::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickSwipe::qt_qmlMarker_anonymous()': one of Qt's own inner
    workings.
  - Qt's 'QQuickSwipePrivate *QQuickSwipe::d_func()': gives
    'QQuickSwipePrivate', which has no cute class yet.
  - Qt's 'const QQuickSwipePrivate *QQuickSwipe::d_func() const': gives
    'QQuickSwipePrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 47 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickSwipe is created at the first use, not by
    'QQuickSwipe(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickSwipe.
  - Qt tells when it has removed the C++ QQuickSwipe. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
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
    Calls Qt's 'QString QQuickSwipe::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipe.html#tr

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
    #  QString QQuickSwipe::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QQuickSwipe2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickSwipe'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickSwipe::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipe.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickSwipe::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QQuickSwipe10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def position(self) -> float:
    """
    Calls Qt's 'qreal QQuickSwipe::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipe.html#position
    """
    #  qreal QQuickSwipe::position() const
    return self.uglySide.call('ritual_ZNK11QQuickSwipe8positionEv')

  def isComplete(self) -> bool:
    """
    Calls Qt's 'bool QQuickSwipe::isComplete() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipe.html#isComplete
    """
    #  bool QQuickSwipe::isComplete() const
    return self.uglySide.call('ritual_ZNK11QQuickSwipe10isCompleteEv')

  def left(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQuickSwipe::left() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipe.html#left

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQuickSwipe::left() const
    address = self.uglySide.call('ritual_ZNK11QQuickSwipe4leftEv')
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  def behind(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQuickSwipe::behind() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipe.html#behind

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQuickSwipe::behind() const
    address = self.uglySide.call('ritual_ZNK11QQuickSwipe6behindEv')
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  def right(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQuickSwipe::right() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipe.html#right

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQuickSwipe::right() const
    address = self.uglySide.call('ritual_ZNK11QQuickSwipe5rightEv')
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  def leftItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickSwipe::leftItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipe.html#leftItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickSwipe::leftItem() const
    address = self.uglySide.call('ritual_ZNK11QQuickSwipe8leftItemEv')
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

  def behindItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickSwipe::behindItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipe.html#behindItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickSwipe::behindItem() const
    address = self.uglySide.call('ritual_ZNK11QQuickSwipe10behindItemEv')
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

  def rightItem(self) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickSwipe::rightItem() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipe.html#rightItem

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickSwipe::rightItem() const
    address = self.uglySide.call('ritual_ZNK11QQuickSwipe9rightItemEv')
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

  def isEnabled(self) -> bool:
    """
    Calls Qt's 'bool QQuickSwipe::isEnabled() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipe.html#isEnabled
    """
    #  bool QQuickSwipe::isEnabled() const
    return self.uglySide.call('ritual_ZNK11QQuickSwipe9isEnabledEv')

  def transition(self) -> Optional[QQuickTransition]:
    """
    Calls Qt's 'QQuickTransition *QQuickSwipe::transition() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipe.html#transition

    Returns
    -------

    Optional[QQuickTransition]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTransition *QQuickSwipe::transition() const
    address = self.uglySide.call('ritual_ZNK11QQuickSwipe10transitionEv')
    from ..QtQuick import QQuickTransition
    return QQuickTransition._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setPosition(self, position: float) -> None:
    """
    Calls Qt's 'void QQuickSwipe::setPosition(qreal position)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipe.html#setPosition

    Parameters
    ----------

    position : float
      Passed on as it is.
    """
    #  void QQuickSwipe::setPosition(qreal position)
    self.uglySide.call('ritual_ZN11QQuickSwipe11setPositionEd', position)

  @overload(bool)
  def setComplete(self, complete: bool) -> None:
    """
    Calls Qt's 'void QQuickSwipe::setComplete(bool complete)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipe.html#setComplete

    Parameters
    ----------

    complete : bool
      Passed on as it is.
    """
    #  void QQuickSwipe::setComplete(bool complete)
    self.uglySide.call('ritual_ZN11QQuickSwipe11setCompleteEb', complete)

  @overload(QQmlComponent)
  @overload(NoneType)
  def setLeft(self, left: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void QQuickSwipe::setLeft(QQmlComponent *left)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipe.html#setLeft

    Parameters
    ----------

    left : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSwipe::setLeft(QQmlComponent *left)
    self.uglySide.call(
        'ritual_ZN11QQuickSwipe7setLeftEP13QQmlComponent',
        self._addressOf(left),
    )

  @overload(QQmlComponent)
  @overload(NoneType)
  def setBehind(self, behind: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void QQuickSwipe::setBehind(QQmlComponent *behind)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipe.html#setBehind

    Parameters
    ----------

    behind : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSwipe::setBehind(QQmlComponent *behind)
    self.uglySide.call(
        'ritual_ZN11QQuickSwipe9setBehindEP13QQmlComponent',
        self._addressOf(behind),
    )

  @overload(QQmlComponent)
  @overload(NoneType)
  def setRight(self, right: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void QQuickSwipe::setRight(QQmlComponent *right)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipe.html#setRight

    Parameters
    ----------

    right : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSwipe::setRight(QQmlComponent *right)
    self.uglySide.call(
        'ritual_ZN11QQuickSwipe8setRightEP13QQmlComponent',
        self._addressOf(right),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setLeftItem(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickSwipe::setLeftItem(QQuickItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipe.html#setLeftItem

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSwipe::setLeftItem(QQuickItem *item)
    self.uglySide.call(
        'ritual_ZN11QQuickSwipe11setLeftItemEP10QQuickItem',
        self._addressOf(item),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setBehindItem(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickSwipe::setBehindItem(QQuickItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipe.html#setBehindItem

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSwipe::setBehindItem(QQuickItem *item)
    self.uglySide.call(
        'ritual_ZN11QQuickSwipe13setBehindItemEP10QQuickItem',
        self._addressOf(item),
    )

  @overload(QQuickItem)
  @overload(NoneType)
  def setRightItem(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickSwipe::setRightItem(QQuickItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipe.html#setRightItem

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSwipe::setRightItem(QQuickItem *item)
    self.uglySide.call(
        'ritual_ZN11QQuickSwipe12setRightItemEP10QQuickItem',
        self._addressOf(item),
    )

  @overload(bool)
  def setEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QQuickSwipe::setEnabled(bool enabled)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipe.html#setEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QQuickSwipe::setEnabled(bool enabled)
    self.uglySide.call('ritual_ZN11QQuickSwipe10setEnabledEb', enabled)

  @overload(QQuickTransition)
  @overload(NoneType)
  def setTransition(self, transition: Optional[QQuickTransition]) -> None:
    """
    Calls Qt's 'void QQuickSwipe::setTransition(QQuickTransition
    *transition)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipe.html#setTransition

    Parameters
    ----------

    transition : Optional[QQuickTransition]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSwipe::setTransition(QQuickTransition *transition)
    self.uglySide.call(
        'ritual_ZN11QQuickSwipe13setTransitionEP16QQuickTransition',
        self._addressOf(transition),
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

  @overload(QQuickSwipeDelegate)
  @overload(NoneType)
  def __init__(self, control: Optional[QQuickSwipeDelegate]) -> None:
    """
    Notes what was given, for Qt's
    'QQuickSwipe::QQuickSwipe(QQuickSwipeDelegate *control)', which is called
    at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipe.html#QQuickSwipe

    Parameters
    ----------

    control : Optional[QQuickSwipeDelegate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickSwipe::QQuickSwipe(QQuickSwipeDelegate *control)
    self._noteCreation(QQuickSwipe, lambda: Rituals.call(
        'ritual_ZN11QQuickSwipeC1EP19QQuickSwipeDelegate',
        self._addressOf(control),
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

  def close(self) -> None:
    """
    Calls Qt's 'void QQuickSwipe::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipe.html#close
    """
    #  void QQuickSwipe::close()
    self.uglySide.call('ritual_ZN11QQuickSwipe5closeEv')

  @overload(QQuickSwipeDelegate.Side)
  def open(self, side: QQuickSwipeDelegate.Side) -> None:
    """
    Calls Qt's 'void QQuickSwipe::open(QQuickSwipeDelegate::Side side)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipe.html#open

    Parameters
    ----------

    side : QQuickSwipeDelegate.Side
      Passed on as its number.
    """
    #  void QQuickSwipe::open(QQuickSwipeDelegate::Side side)
    self.uglySide.call(
        'ritual_ZN11QQuickSwipe4openEN19QQuickSwipeDelegate4SideE',
        side.value,
    )

  def positionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSwipe::positionChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipe.html#positionChanged
    """
    #  void QQuickSwipe::positionChanged()
    self.uglySide.call('ritual_ZN11QQuickSwipe15positionChangedEv')

  def completeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSwipe::completeChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipe.html#completeChanged
    """
    #  void QQuickSwipe::completeChanged()
    self.uglySide.call('ritual_ZN11QQuickSwipe15completeChangedEv')

  def leftChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSwipe::leftChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipe.html#leftChanged
    """
    #  void QQuickSwipe::leftChanged()
    self.uglySide.call('ritual_ZN11QQuickSwipe11leftChangedEv')

  def behindChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSwipe::behindChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipe.html#behindChanged
    """
    #  void QQuickSwipe::behindChanged()
    self.uglySide.call('ritual_ZN11QQuickSwipe13behindChangedEv')

  def rightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSwipe::rightChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipe.html#rightChanged
    """
    #  void QQuickSwipe::rightChanged()
    self.uglySide.call('ritual_ZN11QQuickSwipe12rightChangedEv')

  def leftItemChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSwipe::leftItemChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipe.html#leftItemChanged
    """
    #  void QQuickSwipe::leftItemChanged()
    self.uglySide.call('ritual_ZN11QQuickSwipe15leftItemChangedEv')

  def behindItemChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSwipe::behindItemChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipe.html#behindItemChanged
    """
    #  void QQuickSwipe::behindItemChanged()
    self.uglySide.call('ritual_ZN11QQuickSwipe17behindItemChangedEv')

  def rightItemChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSwipe::rightItemChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipe.html#rightItemChanged
    """
    #  void QQuickSwipe::rightItemChanged()
    self.uglySide.call('ritual_ZN11QQuickSwipe16rightItemChangedEv')

  def completed(self) -> None:
    """
    Calls Qt's 'void QQuickSwipe::completed()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipe.html#completed
    """
    #  void QQuickSwipe::completed()
    self.uglySide.call('ritual_ZN11QQuickSwipe9completedEv')

  def opened(self) -> None:
    """
    Calls Qt's 'void QQuickSwipe::opened()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipe.html#opened
    """
    #  void QQuickSwipe::opened()
    self.uglySide.call('ritual_ZN11QQuickSwipe6openedEv')

  def closed(self) -> None:
    """
    Calls Qt's 'void QQuickSwipe::closed()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipe.html#closed
    """
    #  void QQuickSwipe::closed()
    self.uglySide.call('ritual_ZN11QQuickSwipe6closedEv')

  def enabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSwipe::enabledChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipe.html#enabledChanged
    """
    #  void QQuickSwipe::enabledChanged()
    self.uglySide.call('ritual_ZN11QQuickSwipe14enabledChangedEv')

  def transitionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSwipe::transitionChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipe.html#transitionChanged
    """
    #  void QQuickSwipe::transitionChanged()
    self.uglySide.call('ritual_ZN11QQuickSwipe17transitionChangedEv')
