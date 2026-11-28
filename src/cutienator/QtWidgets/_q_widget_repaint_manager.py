"""
QWidgetRepaintManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qwidgetrepaintmanager_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QWidgetRepaintManager to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPoint, QRect
  from ..QtGui import QBackingStore, QPlatformTextureList, QRegion
  from . import QWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QBackingStore = WAIT['QBackingStore']
  QPlatformTextureList = WAIT['QPlatformTextureList']
  QPoint = WAIT['QPoint']
  QRect = WAIT['QRect']
  QRegion = WAIT['QRegion']
  QWidget = WAIT['QWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWidgetRepaintManager(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QWidgetRepaintManager: a plain Python object standing
  in front of one C++ QWidgetRepaintManager.

  What exists
  -----------

  Every function of Qt's QWidgetRepaintManager that has a ritual and that
  Python can call so far, 23 names in all: 'backingStore', 'setBackingStore',
  'removeDirtyWidget', 'sync', 'markNeedsFlush', 'addStaticWidget',
  'moveStaticWidgets', 'removeStaticWidget', 'staticContents', 'dirtyRegion',
  'dirtyWidgetList', 'isDirty', 'bltRect', 'updateLists', 'addDirtyWidget',
  'resetWidget', 'addDirtyRenderToTextureWidget', 'sendUpdateRequest',
  'syncAllowed', 'paintAndFlush', 'flush', 'hasStaticContents',
  'updateStaticContentsSize'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QWidgetRepaintManager::~QWidgetRepaintManager()': the destructor:
    Python never removes a C++ QWidgetRepaintManager.

  What has no ritual
  ------------------

  8 of the 36 functions Qt declares: 4 forbidden; 3 not a gap; 1 a template.

  What to expect
  --------------

  - The C++ QWidgetRepaintManager is created at the first use, not by
    'QWidgetRepaintManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWidgetRepaintManager.
  - Each name of Qt's QWidgetRepaintManager that has no cute function yet,
    'markDirty', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QWidgetRepaintManager, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class BufferState(CuteNum):
    """
    The enum 'QWidgetRepaintManager::BufferState' of Qt, with the 2 names Qt
    gives in it.
    """

    BufferValid = Kee[int](0)
    BufferInvalid = Kee[int](1)

  class UpdateTime(CuteNum):
    """
    The enum 'QWidgetRepaintManager::UpdateTime' of Qt, with the 2 names Qt
    gives in it.
    """

    UpdateNow = Kee[int](0)
    UpdateLater = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWidgetRepaintManager'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def backingStore(self) -> Optional[QBackingStore]:
    """
    Calls Qt's 'QBackingStore *QWidgetRepaintManager::backingStore() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetrepaintmanager.html#backingStore

    Returns
    -------

    Optional[QBackingStore]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBackingStore *QWidgetRepaintManager::backingStore() const
    address = self.uglySide.call(
        'ritual_ZNK21QWidgetRepaintManager12backingStoreEv',
    )
    from ..QtGui import QBackingStore
    return QBackingStore._cuteAt(address)

  @overload()
  @overload(QWidget)
  @overload(NoneType)
  @overload(QWidget, QRect)
  @overload(NoneType, QRect)
  def staticContents(
      self,
      widget: Optional[QWidget] = None,
      withinClipRect: Optional[QRect] = None,
  ) -> QRegion:
    """
    Calls Qt's 'QRegion QWidgetRepaintManager::staticContents(QWidget
    *widget, const QRect &withinClipRect) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetrepaintmanager.html#staticContents

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    withinClipRect : Optional[QRect]
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.
      May be left out, as in Qt: a new 'QRect()' is then passed on.

    Returns
    -------

    QRegion
      A new cute QRegion around the copy Qt gave back. Python owns it.
    """
    #  QRegion QWidgetRepaintManager::staticContents(QWidget *widget, const
    #      QRect &withinClipRect) const
    if withinClipRect is None:
      from ..QtCore import QRect
      withinClipRect = QRect()
    address = self.uglySide.call(
        'ritual_ZNK21QWidgetRepaintManager14staticContentsEP7QWidgetRK5QRec'
        't',
        self._addressOf(widget), self._valueOf(withinClipRect),
    )
    from ..QtGui import QRegion
    return QRegion._cuteOwning(address)

  def dirtyRegion(self) -> QRegion:
    """
    Calls Qt's 'QRegion QWidgetRepaintManager::dirtyRegion() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetrepaintmanager.html#dirtyRegion

    Returns
    -------

    QRegion
      A new cute QRegion around the copy Qt gave back. Python owns it.
    """
    #  QRegion QWidgetRepaintManager::dirtyRegion() const
    address = self.uglySide.call(
        'ritual_ZNK21QWidgetRepaintManager11dirtyRegionEv',
    )
    from ..QtGui import QRegion
    return QRegion._cuteOwning(address)

  def dirtyWidgetList(self) -> QList[QWidget]:
    """
    Calls Qt's 'QList<QWidget *> QWidgetRepaintManager::dirtyWidgetList()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetrepaintmanager.html#dirtyWidgetList

    Returns
    -------

    QList[QWidget]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QWidget *> QWidgetRepaintManager::dirtyWidgetList() const
    address = self.uglySide.call(
        'ritual_ZNK21QWidgetRepaintManager15dirtyWidgetListEv',
    )
    from . import QWidget
    return QList[QWidget]._cuteOwning(address)

  def isDirty(self) -> bool:
    """
    Calls Qt's 'bool QWidgetRepaintManager::isDirty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetrepaintmanager.html#isDirty
    """
    #  bool QWidgetRepaintManager::isDirty() const
    return self.uglySide.call('ritual_ZNK21QWidgetRepaintManager7isDirtyEv')

  def hasStaticContents(self) -> bool:
    """
    Calls Qt's 'bool QWidgetRepaintManager::hasStaticContents() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetrepaintmanager.html#hasStaticContents
    """
    #  bool QWidgetRepaintManager::hasStaticContents() const
    return self.uglySide.call(
        'ritual_ZNK21QWidgetRepaintManager17hasStaticContentsEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QBackingStore)
  @overload(NoneType)
  def setBackingStore(self, backingStore: Optional[QBackingStore]) -> None:
    """
    Calls Qt's 'void QWidgetRepaintManager::setBackingStore(QBackingStore
    *backingStore)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetrepaintmanager.html#setBackingStore

    Parameters
    ----------

    backingStore : Optional[QBackingStore]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidgetRepaintManager::setBackingStore(QBackingStore
    #      *backingStore)
    self.uglySide.call(
        'ritual_ZN21QWidgetRepaintManager15setBackingStoreEP13QBackingStore',
        self._addressOf(backingStore),
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

  @overload(QWidget)
  @overload(NoneType)
  def __init__(self, t: Optional[QWidget]) -> None:
    """
    Notes what was given, for Qt's
    'QWidgetRepaintManager::QWidgetRepaintManager(QWidget *t)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetrepaintmanager.html#QWidgetRepaintManager

    Parameters
    ----------

    t : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QWidgetRepaintManager::QWidgetRepaintManager(QWidget *t)
    self._noteCreation(QWidgetRepaintManager, lambda: Rituals.call(
        'ritual_ZN21QWidgetRepaintManagerC1EP7QWidget', self._addressOf(t),
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

  @overload(QWidget)
  @overload(NoneType)
  def removeDirtyWidget(self, w: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QWidgetRepaintManager::removeDirtyWidget(QWidget *w)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetrepaintmanager.html#removeDirtyWidget

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidgetRepaintManager::removeDirtyWidget(QWidget *w)
    self.uglySide.call(
        'ritual_ZN21QWidgetRepaintManager17removeDirtyWidgetEP7QWidget',
        self._addressOf(w),
    )

  @overload(QWidget, QRegion)
  @overload(NoneType, QRegion)
  def sync(
      self,
      exposedWidget: Optional[QWidget],
      exposedRegion: QRegion,
  ) -> None:
    """
    Calls Qt's 'void QWidgetRepaintManager::sync(QWidget *exposedWidget,
    const QRegion &exposedRegion)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetrepaintmanager.html#sync

    Parameters
    ----------

    exposedWidget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    exposedRegion : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.
    """
    #  void QWidgetRepaintManager::sync(QWidget *exposedWidget, const QRegion
    #      &exposedRegion)
    self.uglySide.call(
        'ritual_ZN21QWidgetRepaintManager4syncEP7QWidgetRK7QRegion',
        self._addressOf(exposedWidget), self._valueOf(exposedRegion),
    )

  @overload()
  def sync(self) -> None:
    """
    Calls Qt's 'void QWidgetRepaintManager::sync()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetrepaintmanager.html#sync
    """
    #  void QWidgetRepaintManager::sync()
    self.uglySide.call('ritual_ZN21QWidgetRepaintManager4syncEv')

  @overload(QWidget, QRegion, QPoint)
  @overload(NoneType, QRegion, QPoint)
  def markNeedsFlush(
      self,
      widget: Optional[QWidget],
      region: QRegion,
      topLevelOffset: QPoint,
  ) -> None:
    """
    Calls Qt's 'void QWidgetRepaintManager::markNeedsFlush(QWidget *widget,
    const QRegion &region, const QPoint &topLevelOffset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetrepaintmanager.html#markNeedsFlush

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    region : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.

    topLevelOffset : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QWidgetRepaintManager::markNeedsFlush(QWidget *widget, const
    #      QRegion &region, const QPoint &topLevelOffset)
    self.uglySide.call(
        'ritual_ZN21QWidgetRepaintManager14markNeedsFlushEP7QWidgetRK7QRegi'
        'onRK6QPoint',
        self._addressOf(widget), self._valueOf(region),
        self._valueOf(topLevelOffset),
    )

  @overload(QWidget)
  @overload(NoneType)
  @overload(QWidget, QRegion)
  @overload(NoneType, QRegion)
  def markNeedsFlush(
      self,
      widget: Optional[QWidget],
      region: Optional[QRegion] = None,
  ) -> None:
    """
    Calls Qt's 'void QWidgetRepaintManager::markNeedsFlush(QWidget *widget,
    const QRegion &region)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetrepaintmanager.html#markNeedsFlush

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    region : Optional[QRegion]
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own. May be left out, as in Qt: a new 'QRegion()' is then passed on.
    """
    #  void QWidgetRepaintManager::markNeedsFlush(QWidget *widget, const
    #      QRegion &region)
    if region is None:
      from ..QtGui import QRegion
      region = QRegion()
    self.uglySide.call(
        'ritual_ZN21QWidgetRepaintManager14markNeedsFlushEP7QWidgetRK7QRegi'
        'on',
        self._addressOf(widget), self._valueOf(region),
    )

  @overload(QWidget)
  @overload(NoneType)
  def addStaticWidget(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QWidgetRepaintManager::addStaticWidget(QWidget
    *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetrepaintmanager.html#addStaticWidget

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidgetRepaintManager::addStaticWidget(QWidget *widget)
    self.uglySide.call(
        'ritual_ZN21QWidgetRepaintManager15addStaticWidgetEP7QWidget',
        self._addressOf(widget),
    )

  @overload(QWidget)
  @overload(NoneType)
  def moveStaticWidgets(self, reparented: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QWidgetRepaintManager::moveStaticWidgets(QWidget
    *reparented)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetrepaintmanager.html#moveStaticWidgets

    Parameters
    ----------

    reparented : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidgetRepaintManager::moveStaticWidgets(QWidget *reparented)
    self.uglySide.call(
        'ritual_ZN21QWidgetRepaintManager17moveStaticWidgetsEP7QWidget',
        self._addressOf(reparented),
    )

  @overload(QWidget)
  @overload(NoneType)
  def removeStaticWidget(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QWidgetRepaintManager::removeStaticWidget(QWidget
    *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetrepaintmanager.html#removeStaticWidget

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidgetRepaintManager::removeStaticWidget(QWidget *widget)
    self.uglySide.call(
        'ritual_ZN21QWidgetRepaintManager18removeStaticWidgetEP7QWidget',
        self._addressOf(widget),
    )

  @overload(QRect, int, int, QWidget)
  @overload(QRect, int, int, NoneType)
  def bltRect(
      self,
      rect: QRect,
      dx: int,
      dy: int,
      widget: Optional[QWidget],
  ) -> bool:
    """
    Calls Qt's 'bool QWidgetRepaintManager::bltRect(const QRect &rect, int
    dx, int dy, QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetrepaintmanager.html#bltRect

    Parameters
    ----------

    rect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    dx : int
      Passed on as it is.

    dy : int
      Passed on as it is.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QWidgetRepaintManager::bltRect(const QRect &rect, int dx, int dy,
    #      QWidget *widget)
    return self.uglySide.call(
        'ritual_ZN21QWidgetRepaintManager7bltRectERK5QRectiiP7QWidget',
        self._valueOf(rect), dx, dy, self._addressOf(widget),
    )

  @overload(QWidget)
  @overload(NoneType)
  def updateLists(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QWidgetRepaintManager::updateLists(QWidget *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetrepaintmanager.html#updateLists

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidgetRepaintManager::updateLists(QWidget *widget)
    self.uglySide.call(
        'ritual_ZN21QWidgetRepaintManager11updateListsEP7QWidget',
        self._addressOf(widget),
    )

  @overload(QWidget, QRegion)
  @overload(NoneType, QRegion)
  def addDirtyWidget(self, widget: Optional[QWidget], rgn: QRegion) -> None:
    """
    Calls Qt's 'void QWidgetRepaintManager::addDirtyWidget(QWidget *widget,
    const QRegion &rgn)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetrepaintmanager.html#addDirtyWidget

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rgn : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.
    """
    #  void QWidgetRepaintManager::addDirtyWidget(QWidget *widget, const
    #      QRegion &rgn)
    self.uglySide.call(
        'ritual_ZN21QWidgetRepaintManager14addDirtyWidgetEP7QWidgetRK7QRegi'
        'on',
        self._addressOf(widget), self._valueOf(rgn),
    )

  @overload(QWidget)
  @overload(NoneType)
  def resetWidget(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void QWidgetRepaintManager::resetWidget(QWidget *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetrepaintmanager.html#resetWidget

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidgetRepaintManager::resetWidget(QWidget *widget)
    self.uglySide.call(
        'ritual_ZN21QWidgetRepaintManager11resetWidgetEP7QWidget',
        self._addressOf(widget),
    )

  @overload(QWidget)
  @overload(NoneType)
  def addDirtyRenderToTextureWidget(self, widget: Optional[QWidget]) -> None:
    """
    Calls Qt's 'void
    QWidgetRepaintManager::addDirtyRenderToTextureWidget(QWidget *widget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetrepaintmanager.html

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidgetRepaintManager::addDirtyRenderToTextureWidget(QWidget
    #      *widget)
    self.uglySide.call(
        'ritual_ZN21QWidgetRepaintManager29addDirtyRenderToTextureWidgetEP7'
        'QWidget',
        self._addressOf(widget),
    )

  @overload(QWidget, UpdateTime)
  @overload(NoneType, UpdateTime)
  def sendUpdateRequest(
      self,
      widget: Optional[QWidget],
      updateTime: UpdateTime,
  ) -> None:
    """
    Calls Qt's 'void QWidgetRepaintManager::sendUpdateRequest(QWidget
    *widget, UpdateTime updateTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetrepaintmanager.html#sendUpdateRequest

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    updateTime : UpdateTime
      Passed on as its number.
    """
    #  void QWidgetRepaintManager::sendUpdateRequest(QWidget *widget,
    #      UpdateTime updateTime)
    self.uglySide.call(
        'ritual_ZN21QWidgetRepaintManager17sendUpdateRequestEP7QWidgetNS_10'
        'UpdateTimeE',
        self._addressOf(widget), updateTime.value,
    )

  def syncAllowed(self) -> bool:
    """
    Calls Qt's 'bool QWidgetRepaintManager::syncAllowed()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetrepaintmanager.html#syncAllowed
    """
    #  bool QWidgetRepaintManager::syncAllowed()
    return self.uglySide.call(
        'ritual_ZN21QWidgetRepaintManager11syncAllowedEv',
    )

  def paintAndFlush(self) -> None:
    """
    Calls Qt's 'void QWidgetRepaintManager::paintAndFlush()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetrepaintmanager.html#paintAndFlush
    """
    #  void QWidgetRepaintManager::paintAndFlush()
    self.uglySide.call('ritual_ZN21QWidgetRepaintManager13paintAndFlushEv')

  @overload()
  def flush(self) -> None:
    """
    Calls Qt's 'void QWidgetRepaintManager::flush()'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetrepaintmanager.html#flush
    """
    #  void QWidgetRepaintManager::flush()
    self.uglySide.call('ritual_ZN21QWidgetRepaintManager5flushEv')

  @overload(QWidget, QRegion, QPlatformTextureList)
  @overload(QWidget, QRegion, NoneType)
  @overload(NoneType, QRegion, QPlatformTextureList)
  @overload(NoneType, QRegion, NoneType)
  def flush(
      self,
      widget: Optional[QWidget],
      region: QRegion,
      widgetTextures: Optional[QPlatformTextureList],
  ) -> None:
    """
    Calls Qt's 'void QWidgetRepaintManager::flush(QWidget *widget, const
    QRegion &region, QPlatformTextureList *widgetTextures)'.

    Qt's own words: https://doc.qt.io/qt-6/qwidgetrepaintmanager.html#flush

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    region : QRegion
      Passed on as a value: Qt reads the C++ QRegion, which stays Python's
      own.

    widgetTextures : Optional[QPlatformTextureList]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QWidgetRepaintManager::flush(QWidget *widget, const QRegion
    #      &region, QPlatformTextureList *widgetTextures)
    self.uglySide.call(
        'ritual_ZN21QWidgetRepaintManager5flushEP7QWidgetRK7QRegionP20QPlat'
        'formTextureList',
        self._addressOf(widget), self._valueOf(region),
        self._addressOf(widgetTextures),
    )

  def updateStaticContentsSize(self) -> None:
    """
    Calls Qt's 'void QWidgetRepaintManager::updateStaticContentsSize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwidgetrepaintmanager.html
    """
    #  void QWidgetRepaintManager::updateStaticContentsSize()
    self.uglySide.call(
        'ritual_ZN21QWidgetRepaintManager24updateStaticContentsSizeEv',
    )

  @staticmethod
  def markDirty(*__, **_) -> Never:
    """
    Qt's 'QWidgetRepaintManager::markDirty': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QWidgetRepaintManager.markDirty' has no cute function yet. Qt's "
        "'QWidgetRepaintManager::markDirty': a template: a pattern and no "
        "single function.")
