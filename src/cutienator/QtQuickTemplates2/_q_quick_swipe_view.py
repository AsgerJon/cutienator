"""
QQuickSwipeView binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickswipeview_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickSwipeView to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from ..QtGui import QAccessible
from ..QtQuick import QQuickItem
from . import QQuickContainer

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QRectF
  from . import QQuickSwipeViewAttached
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QRectF = WAIT['QRectF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickSwipeView(QQuickContainer):
  """
  The cute side of Qt's QQuickSwipeView: a plain Python object standing in
  front of one C++ QQuickSwipeView.

  It is built on the cute 'QQuickContainer', as Qt's QQuickSwipeView is built
  on Qt's QQuickContainer, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickSwipeView that has a ritual and that Python
  can call so far, 17 names in all: 'metaObject', 'tr',
  'qmlAttachedProperties', 'isInteractive', 'setInteractive', 'orientation',
  'setOrientation', 'isHorizontal', 'isVertical', 'interactiveChanged',
  'orientationChanged', 'componentComplete', 'geometryChange', 'itemAdded',
  'itemMoved', 'itemRemoved', 'accessibleRole'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickSwipeView::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickSwipeView::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickSwipeView::qt_qmlMarker_attached()': one of Qt's own
    inner workings.
  - Qt's 'QQuickSwipeViewPrivate *QQuickSwipeView::d_func()': gives
    'QQuickSwipeViewPrivate', which has no cute class yet.
  - Qt's 'const QQuickSwipeViewPrivate *QQuickSwipeView::d_func() const':
    gives 'QQuickSwipeViewPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 27 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickSwipeView is created at the first use, not by
    'QQuickSwipeView(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickSwipeView.
  - Qt tells when it has removed the C++ QQuickSwipeView. Every call on the
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
    Calls Qt's 'QString QQuickSwipeView::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipeview.html#tr

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
    #  QString QQuickSwipeView::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QQuickSwipeView2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def qmlAttachedProperties(
      object: Optional[QObject],
  ) -> Optional[QQuickSwipeViewAttached]:
    """
    Calls Qt's 'QQuickSwipeViewAttached
    *QQuickSwipeView::qmlAttachedProperties(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswipeview.html#qmlAttachedProperties

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickSwipeViewAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickSwipeViewAttached
    #      *QQuickSwipeView::qmlAttachedProperties(QObject *object)
    address = Rituals.call(
        'ritual_ZN15QQuickSwipeView21qmlAttachedPropertiesEP7QObject',
        CuteMixin._addressOf(object, 'QObject'),
    )
    from . import QQuickSwipeViewAttached
    return QQuickSwipeViewAttached._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickSwipeView'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickSwipeView::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipeview.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickSwipeView::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QQuickSwipeView10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isInteractive(self) -> bool:
    """
    Calls Qt's 'bool QQuickSwipeView::isInteractive() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipeview.html#isInteractive
    """
    #  bool QQuickSwipeView::isInteractive() const
    return self.uglySide.call('ritual_ZNK15QQuickSwipeView13isInteractiveEv')

  def orientation(self) -> Qt.Orientation:
    """
    Calls Qt's 'Qt::Orientation QQuickSwipeView::orientation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipeview.html#orientation

    Returns
    -------

    Qt.Orientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.Orientation(number)'
      gives.
    """
    #  Qt::Orientation QQuickSwipeView::orientation() const
    return Qt.Orientation(self.uglySide.call(
        'ritual_ZNK15QQuickSwipeView11orientationEv',
    ))

  def isHorizontal(self) -> bool:
    """
    Calls Qt's 'bool QQuickSwipeView::isHorizontal() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipeview.html#isHorizontal
    """
    #  bool QQuickSwipeView::isHorizontal() const
    return self.uglySide.call('ritual_ZNK15QQuickSwipeView12isHorizontalEv')

  def isVertical(self) -> bool:
    """
    Calls Qt's 'bool QQuickSwipeView::isVertical() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipeview.html#isVertical
    """
    #  bool QQuickSwipeView::isVertical() const
    return self.uglySide.call('ritual_ZNK15QQuickSwipeView10isVerticalEv')

  def accessibleRole(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QQuickSwipeView::accessibleRole() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswipeview.html#accessibleRole

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QQuickSwipeView::accessibleRole() const
    ritual = 'ritual_ZNK15QQuickSwipeView14accessibleRoleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QQuickSwipeView14accessibleRoleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setInteractive(self, interactive: bool) -> None:
    """
    Calls Qt's 'void QQuickSwipeView::setInteractive(bool interactive)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswipeview.html#setInteractive

    Parameters
    ----------

    interactive : bool
      Passed on as it is.
    """
    #  void QQuickSwipeView::setInteractive(bool interactive)
    self.uglySide.call(
        'ritual_ZN15QQuickSwipeView14setInteractiveEb', interactive,
    )

  @overload(Qt.Orientation)
  def setOrientation(self, orientation: Qt.Orientation) -> None:
    """
    Calls Qt's 'void QQuickSwipeView::setOrientation(Qt::Orientation
    orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswipeview.html#setOrientation

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  void QQuickSwipeView::setOrientation(Qt::Orientation orientation)
    self.uglySide.call(
        'ritual_ZN15QQuickSwipeView14setOrientationEN2Qt11OrientationE',
        orientation.value,
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
    'QQuickSwipeView::QQuickSwipeView(QQuickItem *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswipeview.html#QQuickSwipeView

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickSwipeView::QQuickSwipeView(QQuickItem *parent)
    self._noteCreation(QQuickSwipeView, lambda: Rituals.call(
        'ritual_ZN15QQuickSwipeViewC1EP10QQuickItem',
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

  def interactiveChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSwipeView::interactiveChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswipeview.html#interactiveChanged
    """
    #  void QQuickSwipeView::interactiveChanged()
    self.uglySide.call('ritual_ZN15QQuickSwipeView18interactiveChangedEv')

  def orientationChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSwipeView::orientationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswipeview.html#orientationChanged
    """
    #  void QQuickSwipeView::orientationChanged()
    self.uglySide.call('ritual_ZN15QQuickSwipeView18orientationChangedEv')

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickSwipeView::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswipeview.html#componentComplete
    """
    #  void QQuickSwipeView::componentComplete()
    ritual = 'ritual_ZN15QQuickSwipeView17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickSwipeView17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QQuickSwipeView::geometryChange(const QRectF
    &newGeometry, const QRectF &oldGeometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswipeview.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickSwipeView::geometryChange(const QRectF &newGeometry, const
    #      QRectF &oldGeometry)
    ritual = 'ritual_ZN15QQuickSwipeView14geometryChangeERK6QRectFS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickSwipeView14geometryChangeERK6QRectFS2_'
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  @overload(int, QQuickItem)
  @overload(int, NoneType)
  def itemAdded(self, index: int, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickSwipeView::itemAdded(int index, QQuickItem
    *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipeview.html#itemAdded

    Parameters
    ----------

    index : int
      Passed on as it is.

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSwipeView::itemAdded(int index, QQuickItem *item)
    ritual = 'ritual_ZN15QQuickSwipeView9itemAddedEiP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickSwipeView9itemAddedEiP10QQuickItem'
    self.uglySide.call(ritual, index, self._addressOf(item))

  @overload(int, QQuickItem)
  @overload(int, NoneType)
  def itemMoved(self, index: int, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickSwipeView::itemMoved(int index, QQuickItem
    *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipeview.html#itemMoved

    Parameters
    ----------

    index : int
      Passed on as it is.

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSwipeView::itemMoved(int index, QQuickItem *item)
    ritual = 'ritual_ZN15QQuickSwipeView9itemMovedEiP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickSwipeView9itemMovedEiP10QQuickItem'
    self.uglySide.call(ritual, index, self._addressOf(item))

  @overload(int, QQuickItem)
  @overload(int, NoneType)
  def itemRemoved(self, index: int, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickSwipeView::itemRemoved(int index, QQuickItem
    *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickswipeview.html#itemRemoved

    Parameters
    ----------

    index : int
      Passed on as it is.

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSwipeView::itemRemoved(int index, QQuickItem *item)
    ritual = 'ritual_ZN15QQuickSwipeView11itemRemovedEiP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickSwipeView11itemRemovedEiP10QQuickItem'
    self.uglySide.call(ritual, index, self._addressOf(item))
