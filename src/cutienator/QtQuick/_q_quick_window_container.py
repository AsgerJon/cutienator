"""
QQuickWindowContainer binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickwindowcontainer_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuickWindowContainer to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QQuickImplicitSizeItem, QQuickItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QRectF
  from ..QtGui import QFocusEvent, QWindow
  from . import QQuickWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QFocusEvent = WAIT['QFocusEvent']
  QQuickWindow = WAIT['QQuickWindow']
  QRectF = WAIT['QRectF']
  QWindow = WAIT['QWindow']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickWindowContainer(QQuickImplicitSizeItem):
  """
  The cute side of Qt's QQuickWindowContainer: a plain Python object standing
  in front of one C++ QQuickWindowContainer.

  It is built on the cute 'QQuickImplicitSizeItem', as Qt's
  QQuickWindowContainer is built on Qt's QQuickImplicitSizeItem, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickWindowContainer that has a ritual and that
  Python can call so far, 19 names in all: 'metaObject', 'tr',
  'containedWindow', 'setContainedWindow', 'containedWindowChanged',
  'classBegin', 'componentComplete', 'geometryChange', 'itemChange',
  'updatePolish', 'eventFilter', 'focusInEvent', 'clipRect',
  'releaseResources', 'initializeContainedWindow', 'windowUpdated',
  'syncWindowToItem', 'parentWindowChanged', 'windowDestroyed'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickWindowContainer::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickWindowContainer::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickWindowContainer::~QQuickWindowContainer()': the destructor:
    Python never removes a C++ QQuickWindowContainer.
  - Qt's 'QQuickWindowContainerPrivate *QQuickWindowContainer::d_func()':
    gives 'QQuickWindowContainerPrivate', which has no cute class yet.
  - Qt's 'const QQuickWindowContainerPrivate *QQuickWindowContainer::d_func()
    const': gives 'QQuickWindowContainerPrivate', which has no cute class
    yet.

  What has no ritual
  ------------------

  2 of the 27 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickWindowContainer is created at the first use, not by
    'QQuickWindowContainer(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickWindowContainer.
  - Qt tells when it has removed the C++ QQuickWindowContainer. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QQuickWindowContainer, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class ContainerMode(CuteNum):
    """
    The enum 'QQuickWindowContainer::ContainerMode' of Qt, with the 2 names
    Qt gives in it.
    """

    WindowControlsItem = Kee[int](0)
    ItemControlsWindow = Kee[int](1)

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
    Calls Qt's 'QString QQuickWindowContainer::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickwindowcontainer.html#tr

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
    #  QString QQuickWindowContainer::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QQuickWindowContainer2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickWindowContainer'

  #  A C++ QQuickWindowContainer Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickWindowContainer'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickWindowContainer::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowcontainer.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickWindowContainer::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickWindowContainer10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def containedWindow(self) -> Optional[QWindow]:
    """
    Calls Qt's 'QWindow *QQuickWindowContainer::containedWindow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowcontainer.html#containedWindow

    Returns
    -------

    Optional[QWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindow *QQuickWindowContainer::containedWindow() const
    address = self.uglySide.call(
        'ritual_ZNK21QQuickWindowContainer15containedWindowEv',
    )
    from ..QtGui import QWindow
    return QWindow._cuteAt(address)

  def clipRect(self) -> QRectF:
    """
    Calls Qt's 'QRectF QQuickWindowContainer::clipRect() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowcontainer.html#clipRect

    Returns
    -------

    QRectF
      A new cute QRectF around the copy Qt gave back. Python owns it.
    """
    #  QRectF QQuickWindowContainer::clipRect() const
    ritual = 'ritual_ZNK21QQuickWindowContainer8clipRectEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QQuickWindowContainer8clipRectEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QRectF
    return QRectF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QWindow)
  @overload(NoneType)
  def setContainedWindow(self, window: Optional[QWindow]) -> None:
    """
    Calls Qt's 'void QQuickWindowContainer::setContainedWindow(QWindow
    *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowcontainer.html#setContainedWindow

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWindowContainer::setContainedWindow(QWindow *window)
    self.uglySide.call(
        'ritual_ZN21QQuickWindowContainer18setContainedWindowEP7QWindow',
        self._addressOf(window),
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
  @overload(QQuickItem, ContainerMode)
  @overload(NoneType, ContainerMode)
  def __init__(
      self,
      parent: Optional[QQuickItem] = None,
      containerMode: ContainerMode = ContainerMode.ItemControlsWindow,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQuickWindowContainer::QQuickWindowContainer(QQuickItem *parent,
    ContainerMode containerMode)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowcontainer.html#QQuickWindowContainer

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    containerMode : ContainerMode
      Passed on as its number. May be left out, as in Qt: it is then
      ContainerMode.ItemControlsWindow.
    """
    #  QQuickWindowContainer::QQuickWindowContainer(QQuickItem *parent,
    #      ContainerMode containerMode)
    self._noteCreation(QQuickWindowContainer, lambda: Rituals.call(
        'ritual_ZN21QQuickWindowContainerC1EP10QQuickItemNS_13ContainerMode'
        'E',
        self._addressOf(parent), containerMode.value,
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

  @overload(QWindow)
  @overload(NoneType)
  def containedWindowChanged(self, window: Optional[QWindow]) -> None:
    """
    Calls Qt's 'void QQuickWindowContainer::containedWindowChanged(QWindow
    *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowcontainer.html#containedWindowChanged

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWindowContainer::containedWindowChanged(QWindow *window)
    self.uglySide.call(
        'ritual_ZN21QQuickWindowContainer22containedWindowChangedEP7QWindow',
        self._addressOf(window),
    )

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQuickWindowContainer::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowcontainer.html#classBegin
    """
    #  void QQuickWindowContainer::classBegin()
    ritual = 'ritual_ZN21QQuickWindowContainer10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QQuickWindowContainer10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickWindowContainer::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowcontainer.html#componentComplete
    """
    #  void QQuickWindowContainer::componentComplete()
    ritual = 'ritual_ZN21QQuickWindowContainer17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QQuickWindowContainer17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QRectF, QRectF)
  def geometryChange(self, newGeometry: QRectF, oldGeometry: QRectF) -> None:
    """
    Calls Qt's 'void QQuickWindowContainer::geometryChange(const QRectF
    &newGeometry, const QRectF &oldGeometry)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowcontainer.html#geometryChange

    Parameters
    ----------

    newGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    oldGeometry : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.
    """
    #  void QQuickWindowContainer::geometryChange(const QRectF &newGeometry,
    #      const QRectF &oldGeometry)
    ritual = 'ritual_ZN21QQuickWindowContainer14geometryChangeERK6QRectFS2_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QQuickWindowContainer14geometryChangeERK6QRectFS2'
          '_')
    self.uglySide.call(
        ritual, self._valueOf(newGeometry), self._valueOf(oldGeometry),
    )

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      a0: QQuickItem.ItemChange,
      a1: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickWindowContainer::itemChange(QQuickItem::ItemChange
    a0, const QQuickItem::ItemChangeData &a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowcontainer.html#itemChange

    Parameters
    ----------

    a0 : QQuickItem.ItemChange
      Passed on as its number.

    a1 : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickWindowContainer::itemChange(QQuickItem::ItemChange a0,
    #      const QQuickItem::ItemChangeData &a1)
    ritual = (
        'ritual_ZN21QQuickWindowContainer10itemChangeEN10QQuickItem10ItemCh'
        'angeERKNS0_14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QQuickWindowContainer10itemChangeEN10QQuickItem10'
          'ItemChangeERKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, a0.value, self._valueOf(a1))

  def updatePolish(self) -> None:
    """
    Calls Qt's 'void QQuickWindowContainer::updatePolish()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowcontainer.html#updatePolish
    """
    #  void QQuickWindowContainer::updatePolish()
    ritual = 'ritual_ZN21QQuickWindowContainer12updatePolishEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QQuickWindowContainer12updatePolishEv'
    self.uglySide.call(ritual)

  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def eventFilter(
      self,
      object: Optional[QObject],
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool QQuickWindowContainer::eventFilter(QObject *object,
    QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowcontainer.html#eventFilter

    Parameters
    ----------

    object : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickWindowContainer::eventFilter(QObject *object, QEvent
    #      *event)
    ritual = (
        'ritual_ZN21QQuickWindowContainer11eventFilterEP7QObjectP6QEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QQuickWindowContainer11eventFilterEP7QObjectP6QEv'
          'ent')
    return self.uglySide.call(
        ritual, self._addressOf(object, 'QObject'), self._addressOf(event),
    )

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusInEvent(self, a0: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QQuickWindowContainer::focusInEvent(QFocusEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowcontainer.html#focusInEvent

    Parameters
    ----------

    a0 : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWindowContainer::focusInEvent(QFocusEvent *a0)
    ritual = 'ritual_ZN21QQuickWindowContainer12focusInEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QQuickWindowContainer12focusInEventEP11QFocusEven'
          't')
    self.uglySide.call(ritual, self._addressOf(a0))

  def releaseResources(self) -> None:
    """
    Calls Qt's 'void QQuickWindowContainer::releaseResources()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowcontainer.html#releaseResources
    """
    #  void QQuickWindowContainer::releaseResources()
    ritual = 'ritual_ZN21QQuickWindowContainer16releaseResourcesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN21QQuickWindowContainer16releaseResourcesEv'
    self.uglySide.call(ritual)

  def initializeContainedWindow(self) -> None:
    """
    Calls Qt's 'void QQuickWindowContainer::initializeContainedWindow()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowcontainer.html
    """
    #  void QQuickWindowContainer::initializeContainedWindow()
    self.uglySide.call(
        'ritual_ZN21QQuickWindowContainer25initializeContainedWindowEv',
    )

  def windowUpdated(self) -> None:
    """
    Calls Qt's 'void QQuickWindowContainer::windowUpdated()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowcontainer.html#windowUpdated
    """
    #  void QQuickWindowContainer::windowUpdated()
    self.uglySide.call('ritual_ZN21QQuickWindowContainer13windowUpdatedEv')

  def syncWindowToItem(self) -> None:
    """
    Calls Qt's 'void QQuickWindowContainer::syncWindowToItem()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowcontainer.html#syncWindowToItem
    """
    #  void QQuickWindowContainer::syncWindowToItem()
    self.uglySide.call(
        'ritual_ZN21QQuickWindowContainer16syncWindowToItemEv',
    )

  @overload(QQuickWindow)
  @overload(NoneType)
  def parentWindowChanged(self, window: Optional[QQuickWindow]) -> None:
    """
    Calls Qt's 'void QQuickWindowContainer::parentWindowChanged(QQuickWindow
    *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowcontainer.html#parentWindowChanged

    Parameters
    ----------

    window : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickWindowContainer::parentWindowChanged(QQuickWindow *window)
    self.uglySide.call(
        'ritual_ZN21QQuickWindowContainer19parentWindowChangedEP12QQuickWin'
        'dow',
        self._addressOf(window),
    )

  def windowDestroyed(self) -> None:
    """
    Calls Qt's 'void QQuickWindowContainer::windowDestroyed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickwindowcontainer.html#windowDestroyed
    """
    #  void QQuickWindowContainer::windowDestroyed()
    self.uglySide.call('ritual_ZN21QQuickWindowContainer15windowDestroyedEv')
