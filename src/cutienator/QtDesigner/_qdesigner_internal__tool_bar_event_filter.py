"""
qdesigner_internal::ToolBarEventFilter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_toolbar_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::ToolBarEventFilter to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QPoint, QRect
  from ..QtGui import QAction, QContextMenuEvent, QDragLeaveEvent
  from ..QtGui import QDragMoveEvent, QDropEvent, QMouseEvent
  from ..QtWidgets import QToolBar
  from . import QDesignerFormWindowInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QContextMenuEvent = WAIT['QContextMenuEvent']
  QDesignerFormWindowInterface = WAIT['QDesignerFormWindowInterface']
  QDragLeaveEvent = WAIT['QDragLeaveEvent']
  QDragMoveEvent = WAIT['QDragMoveEvent']
  QDropEvent = WAIT['QDropEvent']
  QEvent = WAIT['QEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QPoint = WAIT['QPoint']
  QToolBar = WAIT['QToolBar']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ToolBarEventFilter(QObject):
  """
  The cute side of Qt's qdesigner_internal::ToolBarEventFilter: a plain
  Python object standing in front of one C++
  qdesigner_internal::ToolBarEventFilter.

  It is built on the cute 'QObject', as Qt's
  qdesigner_internal::ToolBarEventFilter is built on Qt's QObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::ToolBarEventFilter that has a
  ritual and that Python can call so far, 25 names in all: 'metaObject',
  'tr', 'install', 'actionAt', 'withinHandleArea', 'handleArea', 'freeArea',
  'createAction', 'eventFilter', 'contextMenuActions', 'eventFilterOf',
  'slotRemoveSelectedAction', 'slotRemoveToolBar', 'slotInsertSeparator',
  'handleContextMenuEvent', 'handleDragEnterMoveEvent',
  'handleDragLeaveEvent', 'handleDropEvent', 'handleMousePressEvent',
  'handleMouseReleaseEvent', 'handleMouseMoveEvent', 'formWindow',
  'adjustDragIndicator', 'hideDragIndicator', 'startDrag'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *qdesigner_internal::ToolBarEventFilter::qt_metacast(const
    char *a0)': one of Qt's own inner workings.
  - Qt's 'int
    qdesigner_internal::ToolBarEventFilter::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 31 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ qdesigner_internal::ToolBarEventFilter is created at the first
    use, not by 'qdesigner_internal::ToolBarEventFilter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::ToolBarEventFilter.
  - Qt tells when it has removed the C++
    qdesigner_internal::ToolBarEventFilter. Every call on the cute object,
    and every use of it as an argument, then raises 'RuntimeError', and
    nothing reaches C++.
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
    Calls Qt's 'QString qdesigner_internal::ToolBarEventFilter::tr(const char
    *s, const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-toolbareventfilter.html#tr

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
    #  QString qdesigner_internal::ToolBarEventFilter::tr(const char *s,
    #      const char *c, int n)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal18ToolBarEventFilter2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QToolBar)
  @overload(NoneType)
  def install(tb: Optional[QToolBar]) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ToolBarEventFilter::install(QToolBar
    *tb)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-toolbareventfilter.html#install

    Parameters
    ----------

    tb : Optional[QToolBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ToolBarEventFilter::install(QToolBar *tb)
    Rituals.call(
        'ritual_ZN18qdesigner_internal18ToolBarEventFilter7installEP8QToolB'
        'ar',
        CuteMixin._addressOf(tb),
    )

  @staticmethod
  @overload(QToolBar, QPoint)
  @overload(NoneType, QPoint)
  def actionAt(tb: Optional[QToolBar], pos: QPoint) -> Optional[QAction]:
    """
    Calls Qt's 'QAction
    *qdesigner_internal::ToolBarEventFilter::actionAt(const QToolBar *tb,
    const QPoint &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-toolbareventfilter.html

    Parameters
    ----------

    tb : Optional[QToolBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *qdesigner_internal::ToolBarEventFilter::actionAt(const
    #      QToolBar *tb, const QPoint &pos)
    address = Rituals.call(
        'ritual_ZN18qdesigner_internal18ToolBarEventFilter8actionAtEPK8QToo'
        'lBarRK6QPoint',
        CuteMixin._addressOf(tb), CuteMixin._valueOf(pos),
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  @staticmethod
  @overload(QToolBar, QPoint)
  @overload(NoneType, QPoint)
  def withinHandleArea(tb: Optional[QToolBar], pos: QPoint) -> bool:
    """
    Calls Qt's 'bool
    qdesigner_internal::ToolBarEventFilter::withinHandleArea(const QToolBar
    *tb, const QPoint &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-toolbareventfilter.html

    Parameters
    ----------

    tb : Optional[QToolBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  bool qdesigner_internal::ToolBarEventFilter::withinHandleArea(const
    #      QToolBar *tb, const QPoint &pos)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal18ToolBarEventFilter16withinHandleAre'
        'aEPK8QToolBarRK6QPoint',
        CuteMixin._addressOf(tb), CuteMixin._valueOf(pos),
    )

  @overload(QPoint)
  def withinHandleArea(self, pos: QPoint) -> bool:
    """
    Calls Qt's 'bool
    qdesigner_internal::ToolBarEventFilter::withinHandleArea(const QPoint
    &pos) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-toolbareventfilter.html

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  bool qdesigner_internal::ToolBarEventFilter::withinHandleArea(const
    #      QPoint &pos) const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal18ToolBarEventFilter16withinHandleAr'
        'eaERK6QPoint',
        self._valueOf(pos),
    )

  @staticmethod
  @overload(QToolBar)
  @overload(NoneType)
  def handleArea(tb: Optional[QToolBar]) -> QRect:
    """
    Calls Qt's 'QRect
    qdesigner_internal::ToolBarEventFilter::handleArea(const QToolBar *tb)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-toolbareventfilter.html

    Parameters
    ----------

    tb : Optional[QToolBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect qdesigner_internal::ToolBarEventFilter::handleArea(const
    #      QToolBar *tb)
    address = Rituals.call(
        'ritual_ZN18qdesigner_internal18ToolBarEventFilter10handleAreaEPK8Q'
        'ToolBar',
        CuteMixin._addressOf(tb),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @staticmethod
  @overload(QToolBar)
  @overload(NoneType)
  def freeArea(tb: Optional[QToolBar]) -> QRect:
    """
    Calls Qt's 'QRect qdesigner_internal::ToolBarEventFilter::freeArea(const
    QToolBar *tb)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-toolbareventfilter.html

    Parameters
    ----------

    tb : Optional[QToolBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect qdesigner_internal::ToolBarEventFilter::freeArea(const QToolBar
    #      *tb)
    address = Rituals.call(
        'ritual_ZN18qdesigner_internal18ToolBarEventFilter8freeAreaEPK8QToo'
        'lBar',
        CuteMixin._addressOf(tb),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @staticmethod
  @overload(QDesignerFormWindowInterface, str, bool)
  @overload(NoneType, str, bool)
  def createAction(
      fw: Optional[QDesignerFormWindowInterface],
      objectName: str,
      separator: bool,
  ) -> Optional[QAction]:
    """
    Calls Qt's 'QAction
    *qdesigner_internal::ToolBarEventFilter::createAction(
    QDesignerFormWindowInterface *fw, const QString &objectName, bool
    separator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-toolbareventfilter.html

    Parameters
    ----------

    fw : Optional[QDesignerFormWindowInterface]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    objectName : str
      Passed on as it is: a QString is made of it for the call.

    separator : bool
      Passed on as it is.

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *qdesigner_internal::ToolBarEventFilter::createAction(
    #      QDesignerFormWindowInterface *fw, const QString &objectName, bool
    #      separator)
    address = Rituals.call(
        'ritual_ZN18qdesigner_internal18ToolBarEventFilter12createActionEP2'
        '8QDesignerFormWindowInterfaceRK7QStringb',
        CuteMixin._addressOf(fw), objectName, separator,
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  @staticmethod
  @overload(QToolBar)
  @overload(NoneType)
  def eventFilterOf(tb: Optional[QToolBar]) -> Optional[ToolBarEventFilter]:
    """
    Calls Qt's 'ToolBarEventFilter
    *qdesigner_internal::ToolBarEventFilter::eventFilterOf(const QToolBar
    *tb)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-toolbareventfilter.html

    Parameters
    ----------

    tb : Optional[QToolBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[ToolBarEventFilter]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ToolBarEventFilter
    #      *qdesigner_internal::ToolBarEventFilter::eventFilterOf(const
    #      QToolBar *tb)
    address = Rituals.call(
        'ritual_ZN18qdesigner_internal18ToolBarEventFilter13eventFilterOfEP'
        'K8QToolBar',
        CuteMixin._addressOf(tb),
    )
    return ToolBarEventFilter._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::ToolBarEventFilter'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *qdesigner_internal::ToolBarEventFilter::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-toolbareventfilter.html

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject
    #      *qdesigner_internal::ToolBarEventFilter::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal18ToolBarEventFilter10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def formWindow(self) -> Optional[QDesignerFormWindowInterface]:
    """
    Calls Qt's 'QDesignerFormWindowInterface
    *qdesigner_internal::ToolBarEventFilter::formWindow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-toolbareventfilter.html

    Returns
    -------

    Optional[QDesignerFormWindowInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerFormWindowInterface
    #      *qdesigner_internal::ToolBarEventFilter::formWindow() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal18ToolBarEventFilter10formWindowEv',
    )
    from . import QDesignerFormWindowInterface
    return QDesignerFormWindowInterface._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QToolBar)
  @overload(NoneType)
  def __init__(self, tb: Optional[QToolBar]) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::ToolBarEventFilter::ToolBarEventFilter(QToolBar
    *tb)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-toolbareventfilter.html

    Parameters
    ----------

    tb : Optional[QToolBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  qdesigner_internal::ToolBarEventFilter::ToolBarEventFilter(QToolBar
    #      *tb)
    self._noteCreation(ToolBarEventFilter, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal18ToolBarEventFilterC1EP8QToolBar',
        self._addressOf(tb),
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

  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def eventFilter(
      self,
      watched: Optional[QObject],
      event: Optional[QEvent],
  ) -> bool:
    """
    Calls Qt's 'bool
    qdesigner_internal::ToolBarEventFilter::eventFilter(QObject *watched,
    QEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-toolbareventfilter.html

    Parameters
    ----------

    watched : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool qdesigner_internal::ToolBarEventFilter::eventFilter(QObject
    #      *watched, QEvent *event)
    ritual = (
        'ritual_ZN18qdesigner_internal18ToolBarEventFilter11eventFilterEP7Q'
        'ObjectP6QEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal18ToolBarEventFilter11eventFilt'
          'erEP7QObjectP6QEvent')
    return self.uglySide.call(
        ritual, self._addressOf(watched, 'QObject'), self._addressOf(event),
    )

  @overload()
  @overload(QPoint)
  def contextMenuActions(
      self,
      globalPos: Optional[QPoint] = None,
  ) -> QList[QAction]:
    """
    Calls Qt's 'QList<QAction *>
    qdesigner_internal::ToolBarEventFilter::contextMenuActions(const QPoint
    &globalPos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-toolbareventfilter.html

    Parameters
    ----------

    globalPos : Optional[QPoint]
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own. May be left out, as in Qt: a new 'QPoint(-1, -1)' is then passed
      on.

    Returns
    -------

    QList[QAction]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QAction *>
    #      qdesigner_internal::ToolBarEventFilter::contextMenuActions(const
    #      QPoint &globalPos)
    if globalPos is None:
      from ..QtCore import QPoint
      globalPos = QPoint(-1, -1)
    address = self.uglySide.call(
        'ritual_ZN18qdesigner_internal18ToolBarEventFilter18contextMenuActi'
        'onsERK6QPoint',
        self._valueOf(globalPos),
    )
    from ..QtGui import QAction
    return QList[QAction]._cuteOwning(address)

  def slotRemoveSelectedAction(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ToolBarEventFilter::slotRemoveSelectedAction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-toolbareventfilter.html
    """
    #  void
    #      qdesigner_internal::ToolBarEventFilter::slotRemoveSelectedAction()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal18ToolBarEventFilter24slotRemoveSelec'
        'tedActionEv',
    )

  def slotRemoveToolBar(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ToolBarEventFilter::slotRemoveToolBar()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-toolbareventfilter.html
    """
    #  void qdesigner_internal::ToolBarEventFilter::slotRemoveToolBar()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal18ToolBarEventFilter17slotRemoveToolB'
        'arEv',
    )

  def slotInsertSeparator(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ToolBarEventFilter::slotInsertSeparator()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-toolbareventfilter.html
    """
    #  void qdesigner_internal::ToolBarEventFilter::slotInsertSeparator()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal18ToolBarEventFilter19slotInsertSepar'
        'atorEv',
    )

  @overload(QContextMenuEvent)
  @overload(NoneType)
  def handleContextMenuEvent(
      self,
      event: Optional[QContextMenuEvent],
  ) -> bool:
    """
    Calls Qt's 'bool
    qdesigner_internal::ToolBarEventFilter::handleContextMenuEvent(
    QContextMenuEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-toolbareventfilter.html

    Parameters
    ----------

    event : Optional[QContextMenuEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool qdesigner_internal::ToolBarEventFilter::handleContextMenuEvent(
    #      QContextMenuEvent *event)
    return self.uglySide.call(
        'ritual_ZN18qdesigner_internal18ToolBarEventFilter22handleContextMe'
        'nuEventEP17QContextMenuEvent',
        self._addressOf(event),
    )

  @overload(QDragMoveEvent)
  @overload(NoneType)
  def handleDragEnterMoveEvent(
      self,
      event: Optional[QDragMoveEvent],
  ) -> bool:
    """
    Calls Qt's 'bool
    qdesigner_internal::ToolBarEventFilter::handleDragEnterMoveEvent(
    QDragMoveEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-toolbareventfilter.html

    Parameters
    ----------

    event : Optional[QDragMoveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool qdesigner_internal::ToolBarEventFilter::handleDragEnterMoveEvent(
    #      QDragMoveEvent *event)
    return self.uglySide.call(
        'ritual_ZN18qdesigner_internal18ToolBarEventFilter24handleDragEnter'
        'MoveEventEP14QDragMoveEvent',
        self._addressOf(event),
    )

  @overload(QDragLeaveEvent)
  @overload(NoneType)
  def handleDragLeaveEvent(self, a0: Optional[QDragLeaveEvent]) -> bool:
    """
    Calls Qt's 'bool
    qdesigner_internal::ToolBarEventFilter::handleDragLeaveEvent(
    QDragLeaveEvent *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-toolbareventfilter.html

    Parameters
    ----------

    a0 : Optional[QDragLeaveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool qdesigner_internal::ToolBarEventFilter::handleDragLeaveEvent(
    #      QDragLeaveEvent *a0)
    return self.uglySide.call(
        'ritual_ZN18qdesigner_internal18ToolBarEventFilter20handleDragLeave'
        'EventEP15QDragLeaveEvent',
        self._addressOf(a0),
    )

  @overload(QDropEvent)
  @overload(NoneType)
  def handleDropEvent(self, event: Optional[QDropEvent]) -> bool:
    """
    Calls Qt's 'bool
    qdesigner_internal::ToolBarEventFilter::handleDropEvent(QDropEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-toolbareventfilter.html

    Parameters
    ----------

    event : Optional[QDropEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool
    #      qdesigner_internal::ToolBarEventFilter::handleDropEvent(QDropEvent
    #      *event)
    return self.uglySide.call(
        'ritual_ZN18qdesigner_internal18ToolBarEventFilter15handleDropEvent'
        'EP10QDropEvent',
        self._addressOf(event),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def handleMousePressEvent(self, event: Optional[QMouseEvent]) -> bool:
    """
    Calls Qt's 'bool
    qdesigner_internal::ToolBarEventFilter::handleMousePressEvent(QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-toolbareventfilter.html

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool qdesigner_internal::ToolBarEventFilter::handleMousePressEvent(
    #      QMouseEvent *event)
    return self.uglySide.call(
        'ritual_ZN18qdesigner_internal18ToolBarEventFilter21handleMousePres'
        'sEventEP11QMouseEvent',
        self._addressOf(event),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def handleMouseReleaseEvent(self, event: Optional[QMouseEvent]) -> bool:
    """
    Calls Qt's 'bool
    qdesigner_internal::ToolBarEventFilter::handleMouseReleaseEvent(
    QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-toolbareventfilter.html

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool qdesigner_internal::ToolBarEventFilter::handleMouseReleaseEvent(
    #      QMouseEvent *event)
    return self.uglySide.call(
        'ritual_ZN18qdesigner_internal18ToolBarEventFilter23handleMouseRele'
        'aseEventEP11QMouseEvent',
        self._addressOf(event),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def handleMouseMoveEvent(self, event: Optional[QMouseEvent]) -> bool:
    """
    Calls Qt's 'bool
    qdesigner_internal::ToolBarEventFilter::handleMouseMoveEvent(QMouseEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-toolbareventfilter.html

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool qdesigner_internal::ToolBarEventFilter::handleMouseMoveEvent(
    #      QMouseEvent *event)
    return self.uglySide.call(
        'ritual_ZN18qdesigner_internal18ToolBarEventFilter20handleMouseMove'
        'EventEP11QMouseEvent',
        self._addressOf(event),
    )

  @overload(QPoint)
  def adjustDragIndicator(self, pos: QPoint) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ToolBarEventFilter::adjustDragIndicator(const QPoint
    &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-toolbareventfilter.html

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void qdesigner_internal::ToolBarEventFilter::adjustDragIndicator(const
    #      QPoint &pos)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal18ToolBarEventFilter19adjustDragIndic'
        'atorERK6QPoint',
        self._valueOf(pos),
    )

  def hideDragIndicator(self) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ToolBarEventFilter::hideDragIndicator()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-toolbareventfilter.html
    """
    #  void qdesigner_internal::ToolBarEventFilter::hideDragIndicator()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal18ToolBarEventFilter17hideDragIndicat'
        'orEv',
    )

  @overload(QPoint, Qt.KeyboardModifiers)
  def startDrag(self, pos: QPoint, modifiers: Qt.KeyboardModifiers) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::ToolBarEventFilter::startDrag(const
    QPoint &pos, Qt::KeyboardModifiers modifiers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-toolbareventfilter.html

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    modifiers : Qt.KeyboardModifiers
      Passed on as its number.
    """
    #  bool qdesigner_internal::ToolBarEventFilter::startDrag(const QPoint
    #      &pos, Qt::KeyboardModifiers modifiers)
    return self.uglySide.call(
        'ritual_ZN18qdesigner_internal18ToolBarEventFilter9startDragERK6QPo'
        'int6QFlagsIN2Qt16KeyboardModifierEE',
        self._valueOf(pos), modifiers.value,
    )
