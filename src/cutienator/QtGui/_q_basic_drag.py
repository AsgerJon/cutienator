"""
QBasicDrag binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGui/6.12.0/QtGui/private/qsimpledrag_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QBasicDrag to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import Qt, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QPoint
  from . import QDrag, QScreen, QShapedPixmapWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDrag = WAIT['QDrag']
  QEvent = WAIT['QEvent']
  QPoint = WAIT['QPoint']
  QScreen = WAIT['QScreen']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QBasicDrag(QObject):
  """
  The cute side of Qt's QBasicDrag: a plain Python object standing in front
  of one C++ QBasicDrag.

  What exists
  -----------

  Every function of Qt's QBasicDrag that has a ritual and that Python can
  call so far, 23 names in all: 'drag', 'cancelDrag', 'eventFilter',
  'startDrag', 'cancel', 'move', 'drop', 'endDrag', 'moveShapedPixmapWindow',
  'shapedPixmapWindow', 'recreateShapedPixmapWindow', 'updateCursor',
  'canDrop', 'setCanDrop', 'useCompositing', 'setUseCompositing',
  'setScreen', 'executedDropAction', 'setExecutedDropAction',
  'enableEventFilter', 'disableEventFilter', 'restoreCursor',
  'exitDndEventLoop'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QBasicDrag::~QBasicDrag()': the destructor: Python never removes a
    C++ QBasicDrag.

  What has no ritual
  ------------------

  1 of the 26 functions Qt declares: 1 the class is abstract, so C++ cannot
  make one.

  What to expect
  --------------

  - The C++ QBasicDrag is created at the first use, not by 'QBasicDrag(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QBasicDrag.
  - Qt tells when it has removed the C++ QBasicDrag. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QBasicDrag'

  #  Qt's QBasicDrag is built on more than one class. The part of a C++
  #  QBasicDrag that belongs to a class after the first begins somewhere
  #  inside the object, and the ritual named for that class gives where; see
  #  'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QObject': 'ritual_cast_QBasicDrag_QObject',
  }

  #  A C++ QBasicDrag Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QBasicDrag'

  #  The functions Qt calls itself that QBasicDrag is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'drag': (
          ('_ZN10QBasicDrag4dragEP5QDrag',
           ('int', 'enum', 'QtCore:Qt.DropAction'),
           (
               ('address', 'address', 'QtGui:QDrag'),
           )),
      ),
      'cancelDrag': (
          ('_ZN10QBasicDrag10cancelDragEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'startDrag': (
          ('_ZN10QBasicDrag9startDragEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'cancel': (
          ('_ZN10QBasicDrag6cancelEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'move': (
          ('_ZN10QBasicDrag4moveERK6QPoint6QFlagsIN2Qt11MouseButtonEES3_INS'
           '4_16KeyboardModifierEE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QPoint'),
               ('int', 'flags', 'QtCore:Qt.MouseButton'),
               ('int', 'flags', 'QtCore:Qt.KeyboardModifier'),
           )),
      ),
      'drop': (
          ('_ZN10QBasicDrag4dropERK6QPoint6QFlagsIN2Qt11MouseButtonEES3_INS'
           '4_16KeyboardModifierEE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QPoint'),
               ('int', 'flags', 'QtCore:Qt.MouseButton'),
               ('int', 'flags', 'QtCore:Qt.KeyboardModifier'),
           )),
      ),
      'endDrag': (
          ('_ZN10QBasicDrag7endDragEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def shapedPixmapWindow(self) -> Optional[QShapedPixmapWindow]:
    """
    Calls Qt's 'QShapedPixmapWindow *QBasicDrag::shapedPixmapWindow() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbasicdrag.html#shapedPixmapWindow

    Returns
    -------

    Optional[QShapedPixmapWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QShapedPixmapWindow *QBasicDrag::shapedPixmapWindow() const
    address = self.uglySide.call(
        'ritual_ZNK10QBasicDrag18shapedPixmapWindowEv',
    )
    from . import QShapedPixmapWindow
    return QShapedPixmapWindow._cuteAt(address)

  def canDrop(self) -> bool:
    """
    Calls Qt's 'bool QBasicDrag::canDrop() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbasicdrag.html#canDrop
    """
    #  bool QBasicDrag::canDrop() const
    return self.uglySide.call('ritual_ZNK10QBasicDrag7canDropEv')

  def useCompositing(self) -> bool:
    """
    Calls Qt's 'bool QBasicDrag::useCompositing() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbasicdrag.html#useCompositing
    """
    #  bool QBasicDrag::useCompositing() const
    return self.uglySide.call('ritual_ZNK10QBasicDrag14useCompositingEv')

  def executedDropAction(self) -> Qt.DropAction:
    """
    Calls Qt's 'Qt::DropAction QBasicDrag::executedDropAction() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbasicdrag.html#executedDropAction

    Returns
    -------

    Qt.DropAction
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.DropAction(number)'
      gives.
    """
    #  Qt::DropAction QBasicDrag::executedDropAction() const
    return Qt.DropAction(self.uglySide.call(
        'ritual_ZNK10QBasicDrag18executedDropActionEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setCanDrop(self, c: bool) -> None:
    """
    Calls Qt's 'void QBasicDrag::setCanDrop(bool c)'.

    Qt's own words: https://doc.qt.io/qt-6/qbasicdrag.html#setCanDrop

    Parameters
    ----------

    c : bool
      Passed on as it is.
    """
    #  void QBasicDrag::setCanDrop(bool c)
    self.uglySide.call('ritual_ZN10QBasicDrag10setCanDropEb', c)

  @overload(bool)
  def setUseCompositing(self, on: bool) -> None:
    """
    Calls Qt's 'void QBasicDrag::setUseCompositing(bool on)'.

    Qt's own words: https://doc.qt.io/qt-6/qbasicdrag.html#setUseCompositing

    Parameters
    ----------

    on : bool
      Passed on as it is.
    """
    #  void QBasicDrag::setUseCompositing(bool on)
    self.uglySide.call('ritual_ZN10QBasicDrag17setUseCompositingEb', on)

  @overload(QScreen)
  @overload(NoneType)
  def setScreen(self, screen: Optional[QScreen]) -> None:
    """
    Calls Qt's 'void QBasicDrag::setScreen(QScreen *screen)'.

    Qt's own words: https://doc.qt.io/qt-6/qbasicdrag.html#setScreen

    Parameters
    ----------

    screen : Optional[QScreen]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QBasicDrag::setScreen(QScreen *screen)
    self.uglySide.call(
        'ritual_ZN10QBasicDrag9setScreenEP7QScreen', self._addressOf(screen),
    )

  @overload(Qt.DropAction)
  def setExecutedDropAction(self, da: Qt.DropAction) -> None:
    """
    Calls Qt's 'void QBasicDrag::setExecutedDropAction(Qt::DropAction da)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbasicdrag.html#setExecutedDropAction

    Parameters
    ----------

    da : Qt.DropAction
      Passed on as its number.
    """
    #  void QBasicDrag::setExecutedDropAction(Qt::DropAction da)
    self.uglySide.call(
        'ritual_ZN10QBasicDrag21setExecutedDropActionEN2Qt10DropActionE',
        da.value,
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

  @overload(QDrag)
  @overload(NoneType)
  def drag(self, drag: Optional[QDrag]) -> Qt.DropAction:
    """
    Calls Qt's 'Qt::DropAction QBasicDrag::drag(QDrag *drag)'.

    Qt's own words: https://doc.qt.io/qt-6/qbasicdrag.html#drag

    Parameters
    ----------

    drag : Optional[QDrag]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Qt.DropAction
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.DropAction(number)'
      gives.
    """
    #  Qt::DropAction QBasicDrag::drag(QDrag *drag)
    ritual = 'ritual_ZN10QBasicDrag4dragEP5QDrag'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QBasicDrag4dragEP5QDrag'
    return Qt.DropAction(self.uglySide.call(ritual, self._addressOf(drag)))

  @overload()
  def drag(self) -> Optional[QDrag]:
    """
    Calls Qt's 'QDrag *QBasicDrag::drag() const'.

    Qt's own words: https://doc.qt.io/qt-6/qbasicdrag.html#drag

    Returns
    -------

    Optional[QDrag]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDrag *QBasicDrag::drag() const
    address = self.uglySide.call('ritual_ZNK10QBasicDrag4dragEv')
    from . import QDrag
    return QDrag._cuteAt(address)

  def cancelDrag(self) -> None:
    """
    Calls Qt's 'void QBasicDrag::cancelDrag()'.

    Qt's own words: https://doc.qt.io/qt-6/qbasicdrag.html#cancelDrag
    """
    #  void QBasicDrag::cancelDrag()
    ritual = 'ritual_ZN10QBasicDrag10cancelDragEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QBasicDrag10cancelDragEv'
    self.uglySide.call(ritual)

  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def eventFilter(self, o: Optional[QObject], e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QBasicDrag::eventFilter(QObject *o, QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qbasicdrag.html#eventFilter

    Parameters
    ----------

    o : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QBasicDrag::eventFilter(QObject *o, QEvent *e)
    ritual = 'ritual_ZN10QBasicDrag11eventFilterEP7QObjectP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QBasicDrag11eventFilterEP7QObjectP6QEvent'
    return self.uglySide.call(
        ritual, self._addressOf(o, 'QObject'), self._addressOf(e),
    )

  def startDrag(self) -> None:
    """
    Calls Qt's 'void QBasicDrag::startDrag()'.

    Qt's own words: https://doc.qt.io/qt-6/qbasicdrag.html#startDrag
    """
    #  void QBasicDrag::startDrag()
    ritual = 'ritual_ZN10QBasicDrag9startDragEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QBasicDrag9startDragEv'
    self.uglySide.call(ritual)

  def cancel(self) -> None:
    """
    Calls Qt's 'void QBasicDrag::cancel()'.

    Qt's own words: https://doc.qt.io/qt-6/qbasicdrag.html#cancel
    """
    #  void QBasicDrag::cancel()
    ritual = 'ritual_ZN10QBasicDrag6cancelEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QBasicDrag6cancelEv'
    self.uglySide.call(ritual)

  @overload(QPoint, Qt.MouseButtons, Qt.KeyboardModifiers)
  def move(
      self,
      globalPos: QPoint,
      b: Qt.MouseButtons,
      mods: Qt.KeyboardModifiers,
  ) -> None:
    """
    Calls Qt's 'void QBasicDrag::move(const QPoint &globalPos,
    Qt::MouseButtons b, Qt::KeyboardModifiers mods)'.

    Qt's own words: https://doc.qt.io/qt-6/qbasicdrag.html#move

    Parameters
    ----------

    globalPos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    b : Qt.MouseButtons
      Passed on as its number.

    mods : Qt.KeyboardModifiers
      Passed on as its number.
    """
    #  void QBasicDrag::move(const QPoint &globalPos, Qt::MouseButtons b,
    #      Qt::KeyboardModifiers mods)
    self.uglySide.call(
        'ritual_ZN10QBasicDrag4moveERK6QPoint6QFlagsIN2Qt11MouseButtonEES3_'
        'INS4_16KeyboardModifierEE',
        self._valueOf(globalPos), b.value, mods.value,
    )

  @overload(QPoint, Qt.MouseButtons, Qt.KeyboardModifiers)
  def drop(
      self,
      globalPos: QPoint,
      b: Qt.MouseButtons,
      mods: Qt.KeyboardModifiers,
  ) -> None:
    """
    Calls Qt's 'void QBasicDrag::drop(const QPoint &globalPos,
    Qt::MouseButtons b, Qt::KeyboardModifiers mods)'.

    Qt's own words: https://doc.qt.io/qt-6/qbasicdrag.html#drop

    Parameters
    ----------

    globalPos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    b : Qt.MouseButtons
      Passed on as its number.

    mods : Qt.KeyboardModifiers
      Passed on as its number.
    """
    #  void QBasicDrag::drop(const QPoint &globalPos, Qt::MouseButtons b,
    #      Qt::KeyboardModifiers mods)
    self.uglySide.call(
        'ritual_ZN10QBasicDrag4dropERK6QPoint6QFlagsIN2Qt11MouseButtonEES3_'
        'INS4_16KeyboardModifierEE',
        self._valueOf(globalPos), b.value, mods.value,
    )

  def endDrag(self) -> None:
    """
    Calls Qt's 'void QBasicDrag::endDrag()'.

    Qt's own words: https://doc.qt.io/qt-6/qbasicdrag.html#endDrag
    """
    #  void QBasicDrag::endDrag()
    ritual = 'ritual_ZN10QBasicDrag7endDragEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QBasicDrag7endDragEv'
    self.uglySide.call(ritual)

  @overload(QPoint)
  def moveShapedPixmapWindow(
      self,
      deviceIndependentPosition: QPoint,
  ) -> None:
    """
    Calls Qt's 'void QBasicDrag::moveShapedPixmapWindow(const QPoint
    &deviceIndependentPosition)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbasicdrag.html#moveShapedPixmapWindow

    Parameters
    ----------

    deviceIndependentPosition : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QBasicDrag::moveShapedPixmapWindow(const QPoint
    #      &deviceIndependentPosition)
    self.uglySide.call(
        'ritual_ZN10QBasicDrag22moveShapedPixmapWindowERK6QPoint',
        self._valueOf(deviceIndependentPosition),
    )

  @overload(QScreen, QPoint)
  @overload(NoneType, QPoint)
  def recreateShapedPixmapWindow(
      self,
      screen: Optional[QScreen],
      pos: QPoint,
  ) -> None:
    """
    Calls Qt's 'void QBasicDrag::recreateShapedPixmapWindow(QScreen *screen,
    const QPoint &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qbasicdrag.html#recreateShapedPixmapWindow

    Parameters
    ----------

    screen : Optional[QScreen]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QBasicDrag::recreateShapedPixmapWindow(QScreen *screen, const
    #      QPoint &pos)
    self.uglySide.call(
        'ritual_ZN10QBasicDrag26recreateShapedPixmapWindowEP7QScreenRK6QPoi'
        'nt',
        self._addressOf(screen), self._valueOf(pos),
    )

  @overload(Qt.DropAction)
  def updateCursor(self, action: Qt.DropAction) -> None:
    """
    Calls Qt's 'void QBasicDrag::updateCursor(Qt::DropAction action)'.

    Qt's own words: https://doc.qt.io/qt-6/qbasicdrag.html#updateCursor

    Parameters
    ----------

    action : Qt.DropAction
      Passed on as its number.
    """
    #  void QBasicDrag::updateCursor(Qt::DropAction action)
    self.uglySide.call(
        'ritual_ZN10QBasicDrag12updateCursorEN2Qt10DropActionE',
        action.value,
    )

  def enableEventFilter(self) -> None:
    """
    Calls Qt's 'void QBasicDrag::enableEventFilter()'.

    Qt's own words: https://doc.qt.io/qt-6/qbasicdrag.html#enableEventFilter
    """
    #  void QBasicDrag::enableEventFilter()
    self.uglySide.call('ritual_ZN10QBasicDrag17enableEventFilterEv')

  def disableEventFilter(self) -> None:
    """
    Calls Qt's 'void QBasicDrag::disableEventFilter()'.

    Qt's own words: https://doc.qt.io/qt-6/qbasicdrag.html#disableEventFilter
    """
    #  void QBasicDrag::disableEventFilter()
    self.uglySide.call('ritual_ZN10QBasicDrag18disableEventFilterEv')

  def restoreCursor(self) -> None:
    """
    Calls Qt's 'void QBasicDrag::restoreCursor()'.

    Qt's own words: https://doc.qt.io/qt-6/qbasicdrag.html#restoreCursor
    """
    #  void QBasicDrag::restoreCursor()
    self.uglySide.call('ritual_ZN10QBasicDrag13restoreCursorEv')

  def exitDndEventLoop(self) -> None:
    """
    Calls Qt's 'void QBasicDrag::exitDndEventLoop()'.

    Qt's own words: https://doc.qt.io/qt-6/qbasicdrag.html#exitDndEventLoop
    """
    #  void QBasicDrag::exitDndEventLoop()
    self.uglySide.call('ritual_ZN10QBasicDrag16exitDndEventLoopEv')
