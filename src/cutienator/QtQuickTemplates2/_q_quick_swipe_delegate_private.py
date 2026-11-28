"""
QQuickSwipeDelegatePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickswipedelegate_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickSwipeDelegatePrivate to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QQuickItemDelegatePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPointF
  from ..QtGui import QMouseEvent, QPalette
  from ..QtQuick import QQuickItem
  from . import QQuickSwipeDelegate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMouseEvent = WAIT['QMouseEvent']
  QPointF = WAIT['QPointF']
  QQuickItem = WAIT['QQuickItem']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickSwipeDelegatePrivate(QQuickItemDelegatePrivate):
  """
  The cute side of Qt's QQuickSwipeDelegatePrivate: a plain Python object
  standing in front of one C++ QQuickSwipeDelegatePrivate.

  It is built on the cute 'QQuickItemDelegatePrivate', as Qt's
  QQuickSwipeDelegatePrivate is built on Qt's QQuickItemDelegatePrivate, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickSwipeDelegatePrivate that has a ritual and
  that Python can call so far, 6 names in all: 'q_func', 'forwardMouseEvent',
  'getPressedItem', 'resizeContent', 'resizeBackground', 'defaultPalette'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QQuickSwipeDelegate *QQuickSwipeDelegatePrivate::q_func()
    const': takes in Python what 'QQuickSwipeDelegate
    *QQuickSwipeDelegatePrivate::q_func()' takes.

  What has no ritual
  ------------------

  5 of the 12 functions Qt declares: 4 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 leans on
  'QQuickSwipeDelegatePrivate.

  What to expect
  --------------

  - The C++ QQuickSwipeDelegatePrivate is created at the first use, not by
    'QQuickSwipeDelegatePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickSwipeDelegatePrivate.
  - Each name of Qt's QQuickSwipeDelegatePrivate that has no cute function
    yet, '__init__', 'attachedObjectsSetPressed', 'handleMouseMoveEvent',
    'handleMousePressEvent', 'handleMouseReleaseEvent', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickSwipeDelegatePrivate'

  #  A C++ QQuickSwipeDelegatePrivate Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickSwipeDelegatePrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuickItem, QMouseEvent)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QMouseEvent)
  @overload(NoneType, NoneType)
  def getPressedItem(
      self,
      childItem: Optional[QQuickItem],
      event: Optional[QMouseEvent],
  ) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem
    *QQuickSwipeDelegatePrivate::getPressedItem(QQuickItem *childItem,
    QMouseEvent *event) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswipedelegateprivate.html#getPressedItem

    Parameters
    ----------

    childItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickSwipeDelegatePrivate::getPressedItem(QQuickItem
    #      *childItem, QMouseEvent *event) const
    address = self.uglySide.call(
        'ritual_ZNK26QQuickSwipeDelegatePrivate14getPressedItemEP10QQuickIt'
        'emP11QMouseEvent',
        self._addressOf(childItem), self._addressOf(event),
    )
    from ..QtQuick import QQuickItem
    return QQuickItem._cuteAt(address)

  def defaultPalette(self) -> QPalette:
    """
    Calls Qt's 'QPalette QQuickSwipeDelegatePrivate::defaultPalette() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswipedelegateprivate.html#defaultPalette

    Returns
    -------

    QPalette
      A new cute QPalette around the copy Qt gave back. Python owns it.
    """
    #  QPalette QQuickSwipeDelegatePrivate::defaultPalette() const
    ritual = 'ritual_ZNK26QQuickSwipeDelegatePrivate14defaultPaletteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK26QQuickSwipeDelegatePrivate14defaultPaletteEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QPalette
    return QPalette._cuteOwning(address)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQuickSwipeDelegatePrivate::QQuickSwipeDelegatePrivate(
    QQuickSwipeDelegate *control)': leans on
    'QQuickSwipeDelegatePrivate::resizeContent()', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuickSwipeDelegatePrivate.__init__' has no cute function yet. "
        "Qt's "
        "'QQuickSwipeDelegatePrivate::QQuickSwipeDelegatePrivate(QQuickSwipe"
        "Delegate *control)': leans on "
        "'QQuickSwipeDelegatePrivate::resizeContent()', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

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

  def q_func(self) -> Optional[QQuickSwipeDelegate]:
    """
    Calls Qt's 'QQuickSwipeDelegate *QQuickSwipeDelegatePrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswipedelegateprivate.html#q_func

    Returns
    -------

    Optional[QQuickSwipeDelegate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickSwipeDelegate *QQuickSwipeDelegatePrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN26QQuickSwipeDelegatePrivate6q_funcEv',
    )
    from . import QQuickSwipeDelegate
    return QQuickSwipeDelegate._cuteAt(address)

  @overload(QMouseEvent, QQuickItem, QPointF)
  @overload(QMouseEvent, NoneType, QPointF)
  @overload(NoneType, QQuickItem, QPointF)
  @overload(NoneType, NoneType, QPointF)
  def forwardMouseEvent(
      self,
      event: Optional[QMouseEvent],
      destination: Optional[QQuickItem],
      localPos: QPointF,
  ) -> None:
    """
    Calls Qt's 'void
    QQuickSwipeDelegatePrivate::forwardMouseEvent(QMouseEvent *event,
    QQuickItem *destination, QPointF localPos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswipedelegateprivate.html#forwardMouseEvent

    Parameters
    ----------

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    destination : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    localPos : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QQuickSwipeDelegatePrivate::forwardMouseEvent(QMouseEvent *event,
    #      QQuickItem *destination, QPointF localPos)
    self.uglySide.call(
        'ritual_ZN26QQuickSwipeDelegatePrivate17forwardMouseEventEP11QMouse'
        'EventP10QQuickItem7QPointF',
        self._addressOf(event), self._addressOf(destination),
        self._valueOf(localPos, 'QPointF'),
    )

  def resizeContent(self) -> None:
    """
    Calls Qt's 'void QQuickSwipeDelegatePrivate::resizeContent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswipedelegateprivate.html#resizeContent
    """
    #  void QQuickSwipeDelegatePrivate::resizeContent()
    self.uglySide.call(
        'ritual_ZN26QQuickSwipeDelegatePrivate13resizeContentEv',
    )

  def resizeBackground(self) -> None:
    """
    Calls Qt's 'void QQuickSwipeDelegatePrivate::resizeBackground()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickswipedelegateprivate.html#resizeBackground
    """
    #  void QQuickSwipeDelegatePrivate::resizeBackground()
    ritual = 'ritual_ZN26QQuickSwipeDelegatePrivate16resizeBackgroundEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN26QQuickSwipeDelegatePrivate16resizeBackgroundEv')
    self.uglySide.call(ritual)

  @staticmethod
  def attachedObjectsSetPressed(*__, **_) -> Never:
    """
    Qt's 'bool
    QQuickSwipeDelegatePrivate::attachedObjectsSetPressed(QQuickItem *item,
    QPointF scenePos, bool pressed, bool cancel)': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'attached'.
    """
    raise NotImplementedError(
        "'QQuickSwipeDelegatePrivate.attachedObjectsSetPressed' has no cute "
        "function yet. Qt's 'bool "
        "QQuickSwipeDelegatePrivate::attachedObjectsSetPressed(QQuickItem "
        "*item, QPointF scenePos, bool pressed, bool cancel)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'attached'.")

  @staticmethod
  def handleMouseMoveEvent(*__, **_) -> Never:
    """
    Qt's 'bool QQuickSwipeDelegatePrivate::handleMouseMoveEvent(QQuickItem
    *item, QMouseEvent *event)': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: incomplete type
    'QQuickSwipePrivate' named in nested name specifier.
    """
    raise NotImplementedError(
        "'QQuickSwipeDelegatePrivate.handleMouseMoveEvent' has no cute "
        "function yet. Qt's 'bool "
        "QQuickSwipeDelegatePrivate::handleMouseMoveEvent(QQuickItem *item, "
        "QMouseEvent *event)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: "
        "incomplete type 'QQuickSwipePrivate' named in nested name "
        "specifier.")

  @staticmethod
  def handleMousePressEvent(*__, **_) -> Never:
    """
    Qt's 'bool QQuickSwipeDelegatePrivate::handleMousePressEvent(QQuickItem
    *item, QMouseEvent *event)': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: member access
    into incomplete type 'QQuickSwipePrivate'.
    """
    raise NotImplementedError(
        "'QQuickSwipeDelegatePrivate.handleMousePressEvent' has no cute "
        "function yet. Qt's 'bool "
        "QQuickSwipeDelegatePrivate::handleMousePressEvent(QQuickItem "
        "*item, QMouseEvent *event)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: "
        "member access into incomplete type 'QQuickSwipePrivate'.")

  @staticmethod
  def handleMouseReleaseEvent(*__, **_) -> Never:
    """
    Qt's 'bool QQuickSwipeDelegatePrivate::handleMouseReleaseEvent(QQuickItem
    *item, QMouseEvent *event)': Qt's library has no name for it, and its
    code in Qt's source does not compile apart from its file: incomplete type
    'QQuickSwipePrivate' named in nested name specifier.
    """
    raise NotImplementedError(
        "'QQuickSwipeDelegatePrivate.handleMouseReleaseEvent' has no cute "
        "function yet. Qt's 'bool "
        "QQuickSwipeDelegatePrivate::handleMouseReleaseEvent(QQuickItem "
        "*item, QMouseEvent *event)': Qt's library has no name for it, and "
        "its code in Qt's source does not compile apart from its file: "
        "incomplete type 'QQuickSwipePrivate' named in nested name "
        "specifier.")
