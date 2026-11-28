"""
QQuickScrollIndicator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickscrollindicator_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickScrollIndicator to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from ..QtGui import QAccessible
from ..QtQuick import QQuickItem
from . import QQuickControl

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QTouchEvent
  from . import QQuickScrollIndicatorAttached
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QTouchEvent = WAIT['QTouchEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickScrollIndicator(QQuickControl):
  """
  The cute side of Qt's QQuickScrollIndicator: a plain Python object standing
  in front of one C++ QQuickScrollIndicator.

  It is built on the cute 'QQuickControl', as Qt's QQuickScrollIndicator is
  built on Qt's QQuickControl, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickScrollIndicator that has a ritual and that
  Python can call so far, 26 names in all: 'metaObject', 'tr',
  'qmlAttachedProperties', 'size', 'position', 'isActive', 'setActive',
  'orientation', 'setOrientation', 'isHorizontal', 'isVertical',
  'minimumSize', 'setMinimumSize', 'visualSize', 'visualPosition', 'setSize',
  'setPosition', 'sizeChanged', 'positionChanged', 'activeChanged',
  'orientationChanged', 'minimumSizeChanged', 'visualSizeChanged',
  'visualPositionChanged', 'touchEvent', 'accessibleRole'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickScrollIndicator::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickScrollIndicator::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickScrollIndicator::qt_qmlMarker_attached()': one of Qt's
    own inner workings.
  - Qt's 'QQuickScrollIndicatorPrivate *QQuickScrollIndicator::d_func()':
    gives 'QQuickScrollIndicatorPrivate', which has no cute class yet.
  - Qt's 'const QQuickScrollIndicatorPrivate *QQuickScrollIndicator::d_func()
    const': gives 'QQuickScrollIndicatorPrivate', which has no cute class
    yet.

  What has no ritual
  ------------------

  4 of the 36 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickScrollIndicator is created at the first use, not by
    'QQuickScrollIndicator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickScrollIndicator.
  - Qt tells when it has removed the C++ QQuickScrollIndicator. Every call on
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
    Calls Qt's 'QString QQuickScrollIndicator::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscrollindicator.html#tr

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
    #  QString QQuickScrollIndicator::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QQuickScrollIndicator2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def qmlAttachedProperties(
      object: Optional[QObject],
  ) -> Optional[QQuickScrollIndicatorAttached]:
    """
    Calls Qt's 'QQuickScrollIndicatorAttached
    *QQuickScrollIndicator::qmlAttachedProperties(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollindicator.html#qmlAttachedProperties

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickScrollIndicatorAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickScrollIndicatorAttached
    #      *QQuickScrollIndicator::qmlAttachedProperties(QObject *object)
    address = Rituals.call(
        'ritual_ZN21QQuickScrollIndicator21qmlAttachedPropertiesEP7QObject',
        CuteMixin._addressOf(object, 'QObject'),
    )
    from . import QQuickScrollIndicatorAttached
    return QQuickScrollIndicatorAttached._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickScrollIndicator'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickScrollIndicator::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollindicator.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickScrollIndicator::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickScrollIndicator10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def size(self) -> float:
    """
    Calls Qt's 'qreal QQuickScrollIndicator::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscrollindicator.html#size
    """
    #  qreal QQuickScrollIndicator::size() const
    return self.uglySide.call('ritual_ZNK21QQuickScrollIndicator4sizeEv')

  def position(self) -> float:
    """
    Calls Qt's 'qreal QQuickScrollIndicator::position() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollindicator.html#position
    """
    #  qreal QQuickScrollIndicator::position() const
    return self.uglySide.call('ritual_ZNK21QQuickScrollIndicator8positionEv')

  def isActive(self) -> bool:
    """
    Calls Qt's 'bool QQuickScrollIndicator::isActive() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollindicator.html#isActive
    """
    #  bool QQuickScrollIndicator::isActive() const
    return self.uglySide.call('ritual_ZNK21QQuickScrollIndicator8isActiveEv')

  def orientation(self) -> Qt.Orientation:
    """
    Calls Qt's 'Qt::Orientation QQuickScrollIndicator::orientation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollindicator.html#orientation

    Returns
    -------

    Qt.Orientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.Orientation(number)'
      gives.
    """
    #  Qt::Orientation QQuickScrollIndicator::orientation() const
    return Qt.Orientation(self.uglySide.call(
        'ritual_ZNK21QQuickScrollIndicator11orientationEv',
    ))

  def isHorizontal(self) -> bool:
    """
    Calls Qt's 'bool QQuickScrollIndicator::isHorizontal() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollindicator.html#isHorizontal
    """
    #  bool QQuickScrollIndicator::isHorizontal() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickScrollIndicator12isHorizontalEv',
    )

  def isVertical(self) -> bool:
    """
    Calls Qt's 'bool QQuickScrollIndicator::isVertical() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollindicator.html#isVertical
    """
    #  bool QQuickScrollIndicator::isVertical() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickScrollIndicator10isVerticalEv',
    )

  def minimumSize(self) -> float:
    """
    Calls Qt's 'qreal QQuickScrollIndicator::minimumSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollindicator.html#minimumSize
    """
    #  qreal QQuickScrollIndicator::minimumSize() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickScrollIndicator11minimumSizeEv',
    )

  def visualSize(self) -> float:
    """
    Calls Qt's 'qreal QQuickScrollIndicator::visualSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollindicator.html#visualSize
    """
    #  qreal QQuickScrollIndicator::visualSize() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickScrollIndicator10visualSizeEv',
    )

  def visualPosition(self) -> float:
    """
    Calls Qt's 'qreal QQuickScrollIndicator::visualPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollindicator.html#visualPosition
    """
    #  qreal QQuickScrollIndicator::visualPosition() const
    return self.uglySide.call(
        'ritual_ZNK21QQuickScrollIndicator14visualPositionEv',
    )

  def accessibleRole(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QQuickScrollIndicator::accessibleRole()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollindicator.html#accessibleRole

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QQuickScrollIndicator::accessibleRole() const
    ritual = 'ritual_ZNK21QQuickScrollIndicator14accessibleRoleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QQuickScrollIndicator14accessibleRoleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setActive(self, active: bool) -> None:
    """
    Calls Qt's 'void QQuickScrollIndicator::setActive(bool active)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollindicator.html#setActive

    Parameters
    ----------

    active : bool
      Passed on as it is.
    """
    #  void QQuickScrollIndicator::setActive(bool active)
    self.uglySide.call(
        'ritual_ZN21QQuickScrollIndicator9setActiveEb', active,
    )

  @overload(Qt.Orientation)
  def setOrientation(self, orientation: Qt.Orientation) -> None:
    """
    Calls Qt's 'void QQuickScrollIndicator::setOrientation(Qt::Orientation
    orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollindicator.html#setOrientation

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  void QQuickScrollIndicator::setOrientation(Qt::Orientation
    #      orientation)
    self.uglySide.call(
        'ritual_ZN21QQuickScrollIndicator14setOrientationEN2Qt11Orientation'
        'E',
        orientation.value,
    )

  @overload(float)
  def setMinimumSize(self, minimumSize: float) -> None:
    """
    Calls Qt's 'void QQuickScrollIndicator::setMinimumSize(qreal
    minimumSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollindicator.html#setMinimumSize

    Parameters
    ----------

    minimumSize : float
      Passed on as it is.
    """
    #  void QQuickScrollIndicator::setMinimumSize(qreal minimumSize)
    self.uglySide.call(
        'ritual_ZN21QQuickScrollIndicator14setMinimumSizeEd', minimumSize,
    )

  @overload(float)
  def setSize(self, size: float) -> None:
    """
    Calls Qt's 'void QQuickScrollIndicator::setSize(qreal size)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickscrollindicator.html#setSize

    Parameters
    ----------

    size : float
      Passed on as it is.
    """
    #  void QQuickScrollIndicator::setSize(qreal size)
    self.uglySide.call('ritual_ZN21QQuickScrollIndicator7setSizeEd', size)

  @overload(float)
  def setPosition(self, position: float) -> None:
    """
    Calls Qt's 'void QQuickScrollIndicator::setPosition(qreal position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollindicator.html#setPosition

    Parameters
    ----------

    position : float
      Passed on as it is.
    """
    #  void QQuickScrollIndicator::setPosition(qreal position)
    self.uglySide.call(
        'ritual_ZN21QQuickScrollIndicator11setPositionEd', position,
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
  @overload(QQuickItem)
  @overload(NoneType)
  def __init__(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickScrollIndicator::QQuickScrollIndicator(QQuickItem *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollindicator.html#QQuickScrollIndicator

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickScrollIndicator::QQuickScrollIndicator(QQuickItem *parent)
    self._noteCreation(QQuickScrollIndicator, lambda: Rituals.call(
        'ritual_ZN21QQuickScrollIndicatorC1EP10QQuickItem',
        self._addressOf(parent),
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

  def sizeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickScrollIndicator::sizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollindicator.html#sizeChanged
    """
    #  void QQuickScrollIndicator::sizeChanged()
    self.uglySide.call('ritual_ZN21QQuickScrollIndicator11sizeChangedEv')

  def positionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickScrollIndicator::positionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollindicator.html#positionChanged
    """
    #  void QQuickScrollIndicator::positionChanged()
    self.uglySide.call('ritual_ZN21QQuickScrollIndicator15positionChangedEv')

  def activeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickScrollIndicator::activeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollindicator.html#activeChanged
    """
    #  void QQuickScrollIndicator::activeChanged()
    self.uglySide.call('ritual_ZN21QQuickScrollIndicator13activeChangedEv')

  def orientationChanged(self) -> None:
    """
    Calls Qt's 'void QQuickScrollIndicator::orientationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollindicator.html#orientationChanged
    """
    #  void QQuickScrollIndicator::orientationChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickScrollIndicator18orientationChangedEv',
    )

  def minimumSizeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickScrollIndicator::minimumSizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollindicator.html#minimumSizeChanged
    """
    #  void QQuickScrollIndicator::minimumSizeChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickScrollIndicator18minimumSizeChangedEv',
    )

  def visualSizeChanged(self) -> None:
    """
    Calls Qt's 'void QQuickScrollIndicator::visualSizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollindicator.html#visualSizeChanged
    """
    #  void QQuickScrollIndicator::visualSizeChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickScrollIndicator17visualSizeChangedEv',
    )

  def visualPositionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickScrollIndicator::visualPositionChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollindicator.html#visualPositionChanged
    """
    #  void QQuickScrollIndicator::visualPositionChanged()
    self.uglySide.call(
        'ritual_ZN21QQuickScrollIndicator21visualPositionChangedEv',
    )

  @overload(QTouchEvent)
  @overload(NoneType)
  def touchEvent(self, event: Optional[QTouchEvent]) -> None:
    """
    Calls Qt's 'void QQuickScrollIndicator::touchEvent(QTouchEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickscrollindicator.html#touchEvent

    Parameters
    ----------

    event : Optional[QTouchEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickScrollIndicator::touchEvent(QTouchEvent *event)
    ritual = 'ritual_ZN21QQuickScrollIndicator10touchEventEP11QTouchEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QQuickScrollIndicator10touchEventEP11QTouchEvent')
    self.uglySide.call(ritual, self._addressOf(event))
