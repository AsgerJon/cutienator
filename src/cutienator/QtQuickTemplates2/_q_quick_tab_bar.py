"""
QQuickTabBar binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicktabbar_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickTabBar to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtGui import QAccessible
from ..QtQuick import QQuickItem
from . import QQuickContainer

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QRectF
  from ..QtGui import QFont, QWheelEvent
  from . import QQuickTabBarAttached
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']
  QWheelEvent = WAIT['QWheelEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickTabBar(QQuickContainer):
  """
  The cute side of Qt's QQuickTabBar: a plain Python object standing in front
  of one C++ QQuickTabBar.

  It is built on the cute 'QQuickContainer', as Qt's QQuickTabBar is built on
  Qt's QQuickContainer, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickTabBar that has a ritual and that Python can
  call so far, 16 names in all: 'metaObject', 'tr', 'position',
  'setPosition', 'qmlAttachedProperties', 'positionChanged', 'updatePolish',
  'componentComplete', 'geometryChange', 'isContent', 'itemAdded',
  'itemMoved', 'itemRemoved', 'wheelEvent', 'defaultFont', 'accessibleRole'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickTabBar::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickTabBar::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickTabBar::qt_qmlMarker_attached()': one of Qt's own inner
    workings.
  - Qt's 'QQuickTabBarPrivate *QQuickTabBar::d_func()': gives
    'QQuickTabBarPrivate', which has no cute class yet.
  - Qt's 'const QQuickTabBarPrivate *QQuickTabBar::d_func() const': gives
    'QQuickTabBarPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 26 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickTabBar is created at the first use, not by
    'QQuickTabBar(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickTabBar.
  - Qt tells when it has removed the C++ QQuickTabBar. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickTabBar, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Position(CuteNum):
    """
    The enum 'QQuickTabBar::Position' of Qt, with the 2 names Qt gives in it.
    """

    Header = Kee[int](0)
    Footer = Kee[int](1)

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
    Calls Qt's 'QString QQuickTabBar::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktabbar.html#tr

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
    #  QString QQuickTabBar::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QQuickTabBar2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def qmlAttachedProperties(
      object: Optional[QObject],
  ) -> Optional[QQuickTabBarAttached]:
    """
    Calls Qt's 'QQuickTabBarAttached
    *QQuickTabBar::qmlAttachedProperties(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktabbar.html#qmlAttachedProperties

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickTabBarAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickTabBarAttached *QQuickTabBar::qmlAttachedProperties(QObject
    #      *object)
    address = Rituals.call(
        'ritual_ZN12QQuickTabBar21qmlAttachedPropertiesEP7QObject',
        CuteMixin._addressOf(object, 'QObject'),
    )
    from . import QQuickTabBarAttached
    return QQuickTabBarAttached._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickTabBar'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickTabBar::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktabbar.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickTabBar::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QQuickTabBar10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def position(self) -> Position:
    """
    Calls Qt's 'Position QQuickTabBar::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktabbar.html#position

    Returns
    -------

    Position
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Position(number)' gives.
    """
    #  Position QQuickTabBar::position() const
    return QQuickTabBar.Position(self.uglySide.call(
        'ritual_ZNK12QQuickTabBar8positionEv',
    ))

  @overload(QQuickItem)
  @overload(NoneType)
  def isContent(self, item: Optional[QQuickItem]) -> bool:
    """
    Calls Qt's 'bool QQuickTabBar::isContent(QQuickItem *item) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktabbar.html#isContent

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickTabBar::isContent(QQuickItem *item) const
    ritual = 'ritual_ZNK12QQuickTabBar9isContentEP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QQuickTabBar9isContentEP10QQuickItem'
    return self.uglySide.call(ritual, self._addressOf(item))

  def defaultFont(self) -> QFont:
    """
    Calls Qt's 'QFont QQuickTabBar::defaultFont() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktabbar.html#defaultFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickTabBar::defaultFont() const
    ritual = 'ritual_ZNK12QQuickTabBar11defaultFontEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QQuickTabBar11defaultFontEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def accessibleRole(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QQuickTabBar::accessibleRole() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktabbar.html#accessibleRole

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QQuickTabBar::accessibleRole() const
    ritual = 'ritual_ZNK12QQuickTabBar14accessibleRoleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QQuickTabBar14accessibleRoleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Position)
  def setPosition(self, position: Position) -> None:
    """
    Calls Qt's 'void QQuickTabBar::setPosition(Position position)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktabbar.html#setPosition

    Parameters
    ----------

    position : Position
      Passed on as its number.
    """
    #  void QQuickTabBar::setPosition(Position position)
    self.uglySide.call(
        'ritual_ZN12QQuickTabBar11setPositionENS_8PositionE', position.value,
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
    Notes what was given, for Qt's 'QQuickTabBar::QQuickTabBar(QQuickItem
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquicktabbar.html#QQuickTabBar

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickTabBar::QQuickTabBar(QQuickItem *parent)
    self._noteCreation(QQuickTabBar, lambda: Rituals.call(
        'ritual_ZN12QQuickTabBarC1EP10QQuickItem', self._addressOf(parent),
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

  def positionChanged(self) -> None:
    """
    Calls Qt's 'void QQuickTabBar::positionChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktabbar.html#positionChanged
    """
    #  void QQuickTabBar::positionChanged()
    self.uglySide.call('ritual_ZN12QQuickTabBar15positionChangedEv')

  def updatePolish(self) -> None:
    """
    Calls Qt's 'void QQuickTabBar::updatePolish()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktabbar.html#updatePolish
    """
    #  void QQuickTabBar::updatePolish()
    ritual = 'ritual_ZN12QQuickTabBar12updatePolishEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickTabBar12updatePolishEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickTabBar::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicktabbar.html#componentComplete
    """
    #  void QQuickTabBar::componentComplete()
    ritual = 'ritual_ZN12QQuickTabBar17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickTabBar17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QQuickTabBar::geometryChange(const QRectF &newGeometry,
    const QRectF &oldGeometry)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktabbar.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickTabBar::geometryChange(const QRectF &newGeometry, const
    #      QRectF &oldGeometry)
    ritual = 'ritual_ZN12QQuickTabBar14geometryChangeERK6QRectFS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickTabBar14geometryChangeERK6QRectFS2_'
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  @overload(int, QQuickItem)
  @overload(int, NoneType)
  def itemAdded(self, index: int, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickTabBar::itemAdded(int index, QQuickItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktabbar.html#itemAdded

    Parameters
    ----------

    index : int
      Passed on as it is.

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTabBar::itemAdded(int index, QQuickItem *item)
    ritual = 'ritual_ZN12QQuickTabBar9itemAddedEiP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickTabBar9itemAddedEiP10QQuickItem'
    self.uglySide.call(ritual, index, self._addressOf(item))

  @overload(int, QQuickItem)
  @overload(int, NoneType)
  def itemMoved(self, index: int, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickTabBar::itemMoved(int index, QQuickItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktabbar.html#itemMoved

    Parameters
    ----------

    index : int
      Passed on as it is.

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTabBar::itemMoved(int index, QQuickItem *item)
    ritual = 'ritual_ZN12QQuickTabBar9itemMovedEiP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickTabBar9itemMovedEiP10QQuickItem'
    self.uglySide.call(ritual, index, self._addressOf(item))

  @overload(int, QQuickItem)
  @overload(int, NoneType)
  def itemRemoved(self, index: int, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickTabBar::itemRemoved(int index, QQuickItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktabbar.html#itemRemoved

    Parameters
    ----------

    index : int
      Passed on as it is.

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTabBar::itemRemoved(int index, QQuickItem *item)
    ritual = 'ritual_ZN12QQuickTabBar11itemRemovedEiP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickTabBar11itemRemovedEiP10QQuickItem'
    self.uglySide.call(ritual, index, self._addressOf(item))

  @overload(QWheelEvent)
  @overload(NoneType)
  def wheelEvent(self, event: Optional[QWheelEvent]) -> None:
    """
    Calls Qt's 'void QQuickTabBar::wheelEvent(QWheelEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicktabbar.html#wheelEvent

    Parameters
    ----------

    event : Optional[QWheelEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickTabBar::wheelEvent(QWheelEvent *event)
    ritual = 'ritual_ZN12QQuickTabBar10wheelEventEP11QWheelEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQuickTabBar10wheelEventEP11QWheelEvent'
    self.uglySide.call(ritual, self._addressOf(event))
