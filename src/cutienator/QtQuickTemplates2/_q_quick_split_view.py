"""
QQuickSplitView binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquicksplitview_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickSplitView to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from ..QtGui import QAccessible
from ..QtQuick import QQuickItem
from . import QQuickContainer

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QRectF, QVariant
  from ..QtGui import QHoverEvent
  from ..QtQml import QQmlComponent
  from . import QQuickSplitViewAttached
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QHoverEvent = WAIT['QHoverEvent']
  QQmlComponent = WAIT['QQmlComponent']
  QRectF = WAIT['QRectF']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickSplitView(QQuickContainer):
  """
  The cute side of Qt's QQuickSplitView: a plain Python object standing in
  front of one C++ QQuickSplitView.

  It is built on the cute 'QQuickContainer', as Qt's QQuickSplitView is built
  on Qt's QQuickContainer, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickSplitView that has a ritual and that Python
  can call so far, 23 names in all: 'metaObject', 'tr', 'orientation',
  'setOrientation', 'isResizing', 'handle', 'setHandle', 'isContent',
  'qmlAttachedProperties', 'saveState', 'restoreState', 'orientationChanged',
  'resizingChanged', 'handleChanged', 'componentComplete', 'hoverMoveEvent',
  'hoverLeaveEvent', 'childMouseEventFilter', 'geometryChange', 'itemAdded',
  'itemMoved', 'itemRemoved', 'accessibleRole'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickSplitView::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickSplitView::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickSplitView::qt_qmlMarker_attached()': one of Qt's own
    inner workings.
  - Qt's 'QQuickSplitView::~QQuickSplitView()': the destructor: Python never
    removes a C++ QQuickSplitView.
  - Qt's 'QQuickSplitView::QQuickSplitView(QQuickSplitViewPrivate &dd,
    QQuickItem *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'QQuickSplitViewPrivate *QQuickSplitView::d_func()': gives
    'QQuickSplitViewPrivate', which has no cute class yet.
  - Qt's 'const QQuickSplitViewPrivate *QQuickSplitView::d_func() const':
    gives 'QQuickSplitViewPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 35 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickSplitView is created at the first use, not by
    'QQuickSplitView(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickSplitView.
  - Qt tells when it has removed the C++ QQuickSplitView. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickSplitView, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class VersionMarkers(CuteNum):
    """
    The enum 'QQuickSplitView::VersionMarkers' of Qt, with the 1 names Qt
    gives in it.
    """

    VersionMarker = Kee[int](255)

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
    Calls Qt's 'QString QQuickSplitView::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksplitview.html#tr

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
    #  QString QQuickSplitView::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QQuickSplitView2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def qmlAttachedProperties(
      object: Optional[QObject],
  ) -> Optional[QQuickSplitViewAttached]:
    """
    Calls Qt's 'QQuickSplitViewAttached
    *QQuickSplitView::qmlAttachedProperties(QObject *object)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksplitview.html#qmlAttachedProperties

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickSplitViewAttached]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickSplitViewAttached
    #      *QQuickSplitView::qmlAttachedProperties(QObject *object)
    address = Rituals.call(
        'ritual_ZN15QQuickSplitView21qmlAttachedPropertiesEP7QObject',
        CuteMixin._addressOf(object, 'QObject'),
    )
    from . import QQuickSplitViewAttached
    return QQuickSplitViewAttached._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickSplitView'

  #  A C++ QQuickSplitView Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickSplitView'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickSplitView::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksplitview.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickSplitView::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QQuickSplitView10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def orientation(self) -> Qt.Orientation:
    """
    Calls Qt's 'Qt::Orientation QQuickSplitView::orientation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksplitview.html#orientation

    Returns
    -------

    Qt.Orientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.Orientation(number)'
      gives.
    """
    #  Qt::Orientation QQuickSplitView::orientation() const
    return Qt.Orientation(self.uglySide.call(
        'ritual_ZNK15QQuickSplitView11orientationEv',
    ))

  def isResizing(self) -> bool:
    """
    Calls Qt's 'bool QQuickSplitView::isResizing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksplitview.html#isResizing
    """
    #  bool QQuickSplitView::isResizing() const
    return self.uglySide.call('ritual_ZNK15QQuickSplitView10isResizingEv')

  @overload(QQuickItem)
  @overload(NoneType)
  def isContent(self, item: Optional[QQuickItem]) -> bool:
    """
    Calls Qt's 'bool QQuickSplitView::isContent(QQuickItem *item) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksplitview.html#isContent

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickSplitView::isContent(QQuickItem *item) const
    ritual = 'ritual_ZNK15QQuickSplitView9isContentEP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QQuickSplitView9isContentEP10QQuickItem'
    return self.uglySide.call(ritual, self._addressOf(item))

  def accessibleRole(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QQuickSplitView::accessibleRole() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksplitview.html#accessibleRole

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QQuickSplitView::accessibleRole() const
    ritual = 'ritual_ZNK15QQuickSplitView14accessibleRoleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QQuickSplitView14accessibleRoleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.Orientation)
  def setOrientation(self, orientation: Qt.Orientation) -> None:
    """
    Calls Qt's 'void QQuickSplitView::setOrientation(Qt::Orientation
    orientation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksplitview.html#setOrientation

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  void QQuickSplitView::setOrientation(Qt::Orientation orientation)
    self.uglySide.call(
        'ritual_ZN15QQuickSplitView14setOrientationEN2Qt11OrientationE',
        orientation.value,
    )

  @overload(QQmlComponent)
  @overload(NoneType)
  def setHandle(self, handle: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void QQuickSplitView::setHandle(QQmlComponent *handle)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksplitview.html#setHandle

    Parameters
    ----------

    handle : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSplitView::setHandle(QQmlComponent *handle)
    self.uglySide.call(
        'ritual_ZN15QQuickSplitView9setHandleEP13QQmlComponent',
        self._addressOf(handle),
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
    'QQuickSplitView::QQuickSplitView(QQuickItem *parent)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksplitview.html#QQuickSplitView

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickSplitView::QQuickSplitView(QQuickItem *parent)
    self._noteCreation(QQuickSplitView, lambda: Rituals.call(
        'ritual_ZN15QQuickSplitViewC1EP10QQuickItem',
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

  def handle(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQuickSplitView::handle()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksplitview.html#handle

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQuickSplitView::handle()
    address = self.uglySide.call('ritual_ZN15QQuickSplitView6handleEv')
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  def saveState(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickSplitView::saveState()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksplitview.html#saveState

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickSplitView::saveState()
    address = self.uglySide.call('ritual_ZN15QQuickSplitView9saveStateEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QVariant)
  def restoreState(self, state: QVariant) -> bool:
    """
    Calls Qt's 'bool QQuickSplitView::restoreState(const QVariant &state)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksplitview.html#restoreState

    Parameters
    ----------

    state : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  bool QQuickSplitView::restoreState(const QVariant &state)
    return self.uglySide.call(
        'ritual_ZN15QQuickSplitView12restoreStateERK8QVariant',
        self._valueOf(state),
    )

  def orientationChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSplitView::orientationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksplitview.html#orientationChanged
    """
    #  void QQuickSplitView::orientationChanged()
    self.uglySide.call('ritual_ZN15QQuickSplitView18orientationChangedEv')

  def resizingChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSplitView::resizingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksplitview.html#resizingChanged
    """
    #  void QQuickSplitView::resizingChanged()
    self.uglySide.call('ritual_ZN15QQuickSplitView15resizingChangedEv')

  def handleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickSplitView::handleChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksplitview.html#handleChanged
    """
    #  void QQuickSplitView::handleChanged()
    self.uglySide.call('ritual_ZN15QQuickSplitView13handleChangedEv')

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickSplitView::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksplitview.html#componentComplete
    """
    #  void QQuickSplitView::componentComplete()
    ritual = 'ritual_ZN15QQuickSplitView17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickSplitView17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QHoverEvent)
  @overload(NoneType)
  def hoverMoveEvent(self, event: Optional[QHoverEvent]) -> None:
    """
    Calls Qt's 'void QQuickSplitView::hoverMoveEvent(QHoverEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksplitview.html#hoverMoveEvent

    Parameters
    ----------

    event : Optional[QHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSplitView::hoverMoveEvent(QHoverEvent *event)
    ritual = 'ritual_ZN15QQuickSplitView14hoverMoveEventEP11QHoverEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickSplitView14hoverMoveEventEP11QHoverEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QHoverEvent)
  @overload(NoneType)
  def hoverLeaveEvent(self, event: Optional[QHoverEvent]) -> None:
    """
    Calls Qt's 'void QQuickSplitView::hoverLeaveEvent(QHoverEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksplitview.html#hoverLeaveEvent

    Parameters
    ----------

    event : Optional[QHoverEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSplitView::hoverLeaveEvent(QHoverEvent *event)
    ritual = 'ritual_ZN15QQuickSplitView15hoverLeaveEventEP11QHoverEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickSplitView15hoverLeaveEventEP11QHoverEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QQuickItem, QEvent)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def childMouseEventFilter(
      self,
      item: Optional[QQuickItem],
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QQuickSplitView::childMouseEventFilter(QQuickItem *item,
    QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksplitview.html#childMouseEventFilter

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickSplitView::childMouseEventFilter(QQuickItem *item, QEvent
    #      *event)
    ritual = (
        'ritual_ZN15QQuickSplitView21childMouseEventFilterEP10QQuickItemP6Q'
        'Event')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN15QQuickSplitView21childMouseEventFilterEP10QQuickI'
          'temP6QEvent')
    return self.uglySide.call(
        ritual, self._addressOf(item), self._addressOf(event),
    )

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QQuickSplitView::geometryChange(const QRectF
    &newGeometry, const QRectF &oldGeometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquicksplitview.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickSplitView::geometryChange(const QRectF &newGeometry, const
    #      QRectF &oldGeometry)
    ritual = 'ritual_ZN15QQuickSplitView14geometryChangeERK6QRectFS2_'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickSplitView14geometryChangeERK6QRectFS2_'
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  @overload(int, QQuickItem)
  @overload(int, NoneType)
  def itemAdded(self, index: int, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickSplitView::itemAdded(int index, QQuickItem
    *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksplitview.html#itemAdded

    Parameters
    ----------

    index : int
      Passed on as it is.

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSplitView::itemAdded(int index, QQuickItem *item)
    ritual = 'ritual_ZN15QQuickSplitView9itemAddedEiP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickSplitView9itemAddedEiP10QQuickItem'
    self.uglySide.call(ritual, index, self._addressOf(item))

  @overload(int, QQuickItem)
  @overload(int, NoneType)
  def itemMoved(self, index: int, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickSplitView::itemMoved(int index, QQuickItem
    *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksplitview.html#itemMoved

    Parameters
    ----------

    index : int
      Passed on as it is.

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSplitView::itemMoved(int index, QQuickItem *item)
    ritual = 'ritual_ZN15QQuickSplitView9itemMovedEiP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickSplitView9itemMovedEiP10QQuickItem'
    self.uglySide.call(ritual, index, self._addressOf(item))

  @overload(int, QQuickItem)
  @overload(int, NoneType)
  def itemRemoved(self, index: int, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickSplitView::itemRemoved(int index, QQuickItem
    *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquicksplitview.html#itemRemoved

    Parameters
    ----------

    index : int
      Passed on as it is.

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickSplitView::itemRemoved(int index, QQuickItem *item)
    ritual = 'ritual_ZN15QQuickSplitView11itemRemovedEiP10QQuickItem'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickSplitView11itemRemovedEiP10QQuickItem'
    self.uglySide.call(ritual, index, self._addressOf(item))
