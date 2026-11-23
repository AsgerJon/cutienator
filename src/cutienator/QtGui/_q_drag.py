"""
QDrag binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtGui/qdrag.h,
#  Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QMimeData, QPoint
  from . import QPixmap
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMimeData = WAIT['QMimeData']
  QPixmap = WAIT['QPixmap']
  QPoint = WAIT['QPoint']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDrag(QObject):
  """
  The cute side of Qt's QDrag: a plain Python object standing in front of one
  C++ QDrag.

  It is built on the cute 'QObject', as Qt's QDrag is built on Qt's QObject,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDrag that has a ritual and that Python can call so
  far, 16 names in all: 'metaObject', 'tr', 'setMimeData', 'mimeData',
  'setPixmap', 'pixmap', 'setHotSpot', 'hotSpot', 'source', 'target', 'exec',
  'setDragCursor', 'dragCursor', 'supportedActions', 'defaultAction',
  'cancel'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDrag::~QDrag()': the destructor: Python never removes a C++ QDrag.

  What has no ritual
  ------------------

  10 of the 29 functions Qt declares: 4 takes or gives a type that cannot be
  passed yet; 2 a signal; 2 forbidden; 1 a template; 1 declared and nowhere
  to be found.

  What to expect
  --------------

  - The C++ QDrag is created at the first use, not by 'QDrag(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDrag.
  - Qt tells when it has removed the C++ QDrag. Every call on the cute
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
    Calls Qt's 'QString QDrag::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qdrag.html#tr

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
    #  QString QDrag::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN5QDrag2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def cancel() -> None:
    """
    Calls Qt's 'void QDrag::cancel()'.

    Qt's own words: https://doc.qt.io/qt-6/qdrag.html#cancel
    """
    #  void QDrag::cancel()
    Rituals.call('ritual_ZN5QDrag6cancelEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDrag'

  #  A C++ QDrag Python makes is of a C++ class of ours, in which Python can
  #  take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDrag'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDrag::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdrag.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDrag::metaObject() const
    address = self.uglySide.call('ritual_ZNK5QDrag10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def mimeData(self) -> Optional[QMimeData]:
    """
    Calls Qt's 'QMimeData *QDrag::mimeData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdrag.html#mimeData

    Returns
    -------

    Optional[QMimeData]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMimeData *QDrag::mimeData() const
    address = self.uglySide.call('ritual_ZNK5QDrag8mimeDataEv')
    from ..QtCore import QMimeData
    return QMimeData._cuteAt(address)

  def pixmap(self) -> QPixmap:
    """
    Calls Qt's 'QPixmap QDrag::pixmap() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdrag.html#pixmap

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QDrag::pixmap() const
    address = self.uglySide.call('ritual_ZNK5QDrag6pixmapEv')
    from . import QPixmap
    return QPixmap._cuteOwning(address)

  def hotSpot(self) -> QPoint:
    """
    Calls Qt's 'QPoint QDrag::hotSpot() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdrag.html#hotSpot

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QDrag::hotSpot() const
    address = self.uglySide.call('ritual_ZNK5QDrag7hotSpotEv')
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def source(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QDrag::source() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdrag.html#source

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QDrag::source() const
    address = self.uglySide.call('ritual_ZNK5QDrag6sourceEv')
    return QObject._cuteAt(address)

  def target(self) -> Optional[QObject]:
    """
    Calls Qt's 'QObject *QDrag::target() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdrag.html#target

    Returns
    -------

    Optional[QObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QObject *QDrag::target() const
    address = self.uglySide.call('ritual_ZNK5QDrag6targetEv')
    return QObject._cuteAt(address)

  @overload(Qt.DropAction)
  def dragCursor(self, action: Qt.DropAction) -> QPixmap:
    """
    Calls Qt's 'QPixmap QDrag::dragCursor(Qt::DropAction action) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdrag.html#dragCursor

    Parameters
    ----------

    action : Qt.DropAction
      Passed on as its number.

    Returns
    -------

    QPixmap
      A new cute QPixmap around the copy Qt gave back. Python owns it.
    """
    #  QPixmap QDrag::dragCursor(Qt::DropAction action) const
    address = self.uglySide.call(
        'ritual_ZNK5QDrag10dragCursorEN2Qt10DropActionE', action.value,
    )
    from . import QPixmap
    return QPixmap._cuteOwning(address)

  def supportedActions(self) -> Qt.DropActions:
    """
    Calls Qt's 'Qt::DropActions QDrag::supportedActions() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdrag.html#supportedActions

    Returns
    -------

    Qt.DropActions
      The value standing for the combination Qt gave back.
    """
    #  Qt::DropActions QDrag::supportedActions() const
    return Qt.DropActions(self.uglySide.call(
        'ritual_ZNK5QDrag16supportedActionsEv',
    ))

  def defaultAction(self) -> Qt.DropAction:
    """
    Calls Qt's 'Qt::DropAction QDrag::defaultAction() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdrag.html#defaultAction

    Returns
    -------

    Qt.DropAction
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.DropAction(number)'
      gives.
    """
    #  Qt::DropAction QDrag::defaultAction() const
    return Qt.DropAction(self.uglySide.call(
        'ritual_ZNK5QDrag13defaultActionEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QMimeData)
  @overload(NoneType)
  def setMimeData(self, data: Optional[QMimeData]) -> None:
    """
    Calls Qt's 'void QDrag::setMimeData(QMimeData *data)'.

    Qt's own words: https://doc.qt.io/qt-6/qdrag.html#setMimeData

    Parameters
    ----------

    data : Optional[QMimeData]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDrag::setMimeData(QMimeData *data)
    self.uglySide.call(
        'ritual_ZN5QDrag11setMimeDataEP9QMimeData', self._addressOf(data),
    )

  @overload(QPixmap)
  def setPixmap(self, a0: QPixmap) -> None:
    """
    Calls Qt's 'void QDrag::setPixmap(const QPixmap &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qdrag.html#setPixmap

    Parameters
    ----------

    a0 : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.
    """
    #  void QDrag::setPixmap(const QPixmap &a0)
    self.uglySide.call(
        'ritual_ZN5QDrag9setPixmapERK7QPixmap', self._valueOf(a0),
    )

  @overload(QPoint)
  def setHotSpot(self, hotspot: QPoint) -> None:
    """
    Calls Qt's 'void QDrag::setHotSpot(const QPoint &hotspot)'.

    Qt's own words: https://doc.qt.io/qt-6/qdrag.html#setHotSpot

    Parameters
    ----------

    hotspot : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QDrag::setHotSpot(const QPoint &hotspot)
    self.uglySide.call(
        'ritual_ZN5QDrag10setHotSpotERK6QPoint', self._valueOf(hotspot),
    )

  @overload(QPixmap, Qt.DropAction)
  def setDragCursor(self, cursor: QPixmap, action: Qt.DropAction) -> None:
    """
    Calls Qt's 'void QDrag::setDragCursor(const QPixmap &cursor,
    Qt::DropAction action)'.

    Qt's own words: https://doc.qt.io/qt-6/qdrag.html#setDragCursor

    Parameters
    ----------

    cursor : QPixmap
      Passed on as a value: Qt reads the C++ QPixmap, which stays Python's
      own.

    action : Qt.DropAction
      Passed on as its number.
    """
    #  void QDrag::setDragCursor(const QPixmap &cursor, Qt::DropAction
    #      action)
    self.uglySide.call(
        'ritual_ZN5QDrag13setDragCursorERK7QPixmapN2Qt10DropActionE',
        self._valueOf(cursor), action.value,
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

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, dragSource: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's 'QDrag::QDrag(QObject *dragSource)', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdrag.html#QDrag

    Parameters
    ----------

    dragSource : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QDrag::QDrag(QObject *dragSource)
    self._noteCreation(QDrag, lambda: Rituals.call(
        'ritual_ZN5QDragC1EP7QObject', self._addressOf(dragSource),
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

  @overload()
  @overload(Qt.DropActions)
  def exec(
      self,
      supportedActions: Qt.DropActions = Qt.DropActions.MoveAction,
  ) -> Qt.DropAction:
    """
    Calls Qt's 'Qt::DropAction QDrag::exec(Qt::DropActions
    supportedActions)'.

    Qt's own words: https://doc.qt.io/qt-6/qdrag.html#exec

    Parameters
    ----------

    supportedActions : Qt.DropActions
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.DropActions.MoveAction.

    Returns
    -------

    Qt.DropAction
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.DropAction(number)'
      gives.
    """
    #  Qt::DropAction QDrag::exec(Qt::DropActions supportedActions)
    return Qt.DropAction(self.uglySide.call(
        'ritual_ZN5QDrag4execE6QFlagsIN2Qt10DropActionEE',
        supportedActions.value,
    ))

  @overload(Qt.DropActions, Qt.DropAction)
  def exec(
      self,
      supportedActions: Qt.DropActions,
      defaultAction: Qt.DropAction,
  ) -> Qt.DropAction:
    """
    Calls Qt's 'Qt::DropAction QDrag::exec(Qt::DropActions supportedActions,
    Qt::DropAction defaultAction)'.

    Qt's own words: https://doc.qt.io/qt-6/qdrag.html#exec

    Parameters
    ----------

    supportedActions : Qt.DropActions
      Passed on as its number.

    defaultAction : Qt.DropAction
      Passed on as its number.

    Returns
    -------

    Qt.DropAction
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.DropAction(number)'
      gives.
    """
    #  Qt::DropAction QDrag::exec(Qt::DropActions supportedActions,
    #      Qt::DropAction defaultAction)
    return Qt.DropAction(self.uglySide.call(
        'ritual_ZN5QDrag4execE6QFlagsIN2Qt10DropActionEES2_',
        supportedActions.value, defaultAction.value,
    ))
