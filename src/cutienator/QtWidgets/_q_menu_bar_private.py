"""
QMenuBarPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/6.12.0/QtWidgets/private/qmenubar_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QMenuBarPrivate to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtGui import QAction
from . import QWidgetPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QPoint, QRect
  from ..QtGui import QPlatformMenu
  from . import QMenuBar
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPlatformMenu = WAIT['QPlatformMenu']
  QPoint = WAIT['QPoint']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMenuBarPrivate(QWidgetPrivate):
  """
  The cute side of Qt's QMenuBarPrivate: a plain Python object standing in
  front of one C++ QMenuBarPrivate.

  It is built on the cute 'QWidgetPrivate', as Qt's QMenuBarPrivate is built
  on Qt's QWidgetPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QMenuBarPrivate that has a ritual and that Python
  can call so far, 21 names in all: 'q_func', 'getNextAction',
  'calcActionRects', 'actionRect', 'mouseRelaseEventFromQMenu', 'actionAt',
  'setCurrentAction', 'popupAction', 'focusFirstAction', 'setKeyboardMode',
  'activateAction', '_q_actionTriggered', '_q_actionHovered',
  '_q_internalShortcutActivated', '_q_updateLayout', 'isVisible',
  'handleReparent', 'getPlatformMenu', 'findInsertionPlatformMenu',
  'copyActionToPlatformMenu', 'indexOf'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QMenuBar *QMenuBarPrivate::q_func() const': takes in Python
    what 'QMenuBar *QMenuBarPrivate::q_func()' takes.
  - Qt's 'QMenuBarPrivate::~QMenuBarPrivate()': the destructor: Python never
    removes a C++ QMenuBarPrivate.

  What has no ritual
  ------------------

  3 of the 27 functions Qt declares: 3 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QMenuBarPrivate is created at the first use, not by
    'QMenuBarPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMenuBarPrivate.
  - Each name of Qt's QMenuBarPrivate that has no cute function yet,
    'menuRect', 'updateGeometries', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMenuBarPrivate'

  #  A C++ QMenuBarPrivate Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QMenuBarPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int, int)
  def getNextAction(self, start: int, increment: int) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QMenuBarPrivate::getNextAction(const qsizetype
    start, const qsizetype increment) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmenubarprivate.html#getNextAction

    Parameters
    ----------

    start : int
      Passed on as it is.

    increment : int
      Passed on as it is.

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QMenuBarPrivate::getNextAction(const qsizetype start, const
    #      qsizetype increment) const
    address = self.uglySide.call(
        'ritual_ZNK15QMenuBarPrivate13getNextActionExx', start, increment,
    )
    return QAction._cuteAt(address)

  @overload(QAction)
  @overload(NoneType)
  def actionRect(self, a0: Optional[QAction]) -> QRect:
    """
    Calls Qt's 'QRect QMenuBarPrivate::actionRect(QAction *a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmenubarprivate.html#actionRect

    Parameters
    ----------

    a0 : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QMenuBarPrivate::actionRect(QAction *a0) const
    address = self.uglySide.call(
        'ritual_ZNK15QMenuBarPrivate10actionRectEP7QAction',
        self._addressOf(a0),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QPoint)
  def actionAt(self, p: QPoint) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QMenuBarPrivate::actionAt(QPoint p) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmenubarprivate.html#actionAt

    Parameters
    ----------

    p : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QMenuBarPrivate::actionAt(QPoint p) const
    address = self.uglySide.call(
        'ritual_ZNK15QMenuBarPrivate8actionAtE6QPoint', self._valueOf(p),
    )
    return QAction._cuteAt(address)

  @overload(QAction)
  @overload(NoneType)
  def indexOf(self, act: Optional[QAction]) -> int:
    """
    Calls Qt's 'int QMenuBarPrivate::indexOf(QAction *act) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmenubarprivate.html#indexOf

    Parameters
    ----------

    act : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QMenuBarPrivate::indexOf(QAction *act) const
    return self.uglySide.call(
        'ritual_ZNK15QMenuBarPrivate7indexOfEP7QAction',
        self._addressOf(act),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAction)
  @overload(NoneType)
  @overload(QAction, bool)
  @overload(NoneType, bool)
  @overload(QAction, bool, bool)
  @overload(NoneType, bool, bool)
  def setCurrentAction(
      self,
      a0: Optional[QAction],
      a1: bool = False,
      a2: bool = False,
  ) -> None:
    """
    Calls Qt's 'void QMenuBarPrivate::setCurrentAction(QAction *a0, bool a1,
    bool a2)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmenubarprivate.html#setCurrentAction

    Parameters
    ----------

    a0 : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : bool
      Passed on as it is. May be left out, as in Qt: it is then False.

    a2 : bool
      Passed on as it is. May be left out, as in Qt: it is then False.
    """
    #  void QMenuBarPrivate::setCurrentAction(QAction *a0, bool a1, bool a2)
    self.uglySide.call(
        'ritual_ZN15QMenuBarPrivate16setCurrentActionEP7QActionbb',
        self._addressOf(a0), a1, a2,
    )

  @overload(bool)
  def setKeyboardMode(self, a0: bool) -> None:
    """
    Calls Qt's 'void QMenuBarPrivate::setKeyboardMode(bool a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmenubarprivate.html#setKeyboardMode

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QMenuBarPrivate::setKeyboardMode(bool a0)
    self.uglySide.call('ritual_ZN15QMenuBarPrivate15setKeyboardModeEb', a0)

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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QMenuBarPrivate::QMenuBarPrivate()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qmenubarprivate.html#QMenuBarPrivate
    """
    #  QMenuBarPrivate::QMenuBarPrivate()
    self._noteCreation(QMenuBarPrivate, lambda: Rituals.call(
        'ritual_ZN15QMenuBarPrivateC1Ev',
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

  def q_func(self) -> Optional[QMenuBar]:
    """
    Calls Qt's 'QMenuBar *QMenuBarPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qmenubarprivate.html#q_func

    Returns
    -------

    Optional[QMenuBar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMenuBar *QMenuBarPrivate::q_func()
    address = self.uglySide.call('ritual_ZN15QMenuBarPrivate6q_funcEv')
    from . import QMenuBar
    return QMenuBar._cuteAt(address)

  @overload(int, int)
  def calcActionRects(self, max_width: int, start: int) -> None:
    """
    Calls Qt's 'void QMenuBarPrivate::calcActionRects(int max_width, int
    start) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmenubarprivate.html#calcActionRects

    Parameters
    ----------

    max_width : int
      Passed on as it is.

    start : int
      Passed on as it is.
    """
    #  void QMenuBarPrivate::calcActionRects(int max_width, int start) const
    self.uglySide.call(
        'ritual_ZNK15QMenuBarPrivate15calcActionRectsEii', max_width, start,
    )

  def mouseRelaseEventFromQMenu(self) -> None:
    """
    Calls Qt's 'void QMenuBarPrivate::mouseRelaseEventFromQMenu()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmenubarprivate.html#mouseRelaseEventFromQMenu
    """
    #  void QMenuBarPrivate::mouseRelaseEventFromQMenu()
    self.uglySide.call(
        'ritual_ZN15QMenuBarPrivate25mouseRelaseEventFromQMenuEv',
    )

  @overload(QAction, bool)
  @overload(NoneType, bool)
  def popupAction(self, a0: Optional[QAction], a1: bool) -> None:
    """
    Calls Qt's 'void QMenuBarPrivate::popupAction(QAction *a0, bool a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenubarprivate.html#popupAction

    Parameters
    ----------

    a0 : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : bool
      Passed on as it is.
    """
    #  void QMenuBarPrivate::popupAction(QAction *a0, bool a1)
    self.uglySide.call(
        'ritual_ZN15QMenuBarPrivate11popupActionEP7QActionb',
        self._addressOf(a0), a1,
    )

  def focusFirstAction(self) -> None:
    """
    Calls Qt's 'void QMenuBarPrivate::focusFirstAction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmenubarprivate.html#focusFirstAction
    """
    #  void QMenuBarPrivate::focusFirstAction()
    self.uglySide.call('ritual_ZN15QMenuBarPrivate16focusFirstActionEv')

  @overload(QAction, QAction.ActionEvent)
  @overload(NoneType, QAction.ActionEvent)
  def activateAction(
      self,
      a0: Optional[QAction],
      a1: QAction.ActionEvent,
  ) -> None:
    """
    Calls Qt's 'void QMenuBarPrivate::activateAction(QAction *a0,
    QAction::ActionEvent a1)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmenubarprivate.html#activateAction

    Parameters
    ----------

    a0 : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : QAction.ActionEvent
      Passed on as its number.
    """
    #  void QMenuBarPrivate::activateAction(QAction *a0, QAction::ActionEvent
    #      a1)
    self.uglySide.call(
        'ritual_ZN15QMenuBarPrivate14activateActionEP7QActionNS0_11ActionEv'
        'entE',
        self._addressOf(a0), a1.value,
    )

  def _q_actionTriggered(self) -> None:
    """
    Calls Qt's 'void QMenuBarPrivate::_q_actionTriggered()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmenubarprivate.html#_q_actionTriggered
    """
    #  void QMenuBarPrivate::_q_actionTriggered()
    self.uglySide.call('ritual_ZN15QMenuBarPrivate18_q_actionTriggeredEv')

  def _q_actionHovered(self) -> None:
    """
    Calls Qt's 'void QMenuBarPrivate::_q_actionHovered()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmenubarprivate.html#_q_actionHovered
    """
    #  void QMenuBarPrivate::_q_actionHovered()
    self.uglySide.call('ritual_ZN15QMenuBarPrivate16_q_actionHoveredEv')

  @overload(int)
  def _q_internalShortcutActivated(self, a0: int) -> None:
    """
    Calls Qt's 'void QMenuBarPrivate::_q_internalShortcutActivated(int a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmenubarprivate.html#_q_internalShortcutActivated

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  void QMenuBarPrivate::_q_internalShortcutActivated(int a0)
    self.uglySide.call(
        'ritual_ZN15QMenuBarPrivate28_q_internalShortcutActivatedEi', a0,
    )

  def _q_updateLayout(self) -> None:
    """
    Calls Qt's 'void QMenuBarPrivate::_q_updateLayout()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmenubarprivate.html#_q_updateLayout
    """
    #  void QMenuBarPrivate::_q_updateLayout()
    self.uglySide.call('ritual_ZN15QMenuBarPrivate15_q_updateLayoutEv')

  @overload(QAction)
  @overload(NoneType)
  def isVisible(self, action: Optional[QAction]) -> bool:
    """
    Calls Qt's 'bool QMenuBarPrivate::isVisible(QAction *action)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenubarprivate.html#isVisible

    Parameters
    ----------

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QMenuBarPrivate::isVisible(QAction *action)
    return self.uglySide.call(
        'ritual_ZN15QMenuBarPrivate9isVisibleEP7QAction',
        self._addressOf(action),
    )

  def handleReparent(self) -> None:
    """
    Calls Qt's 'void QMenuBarPrivate::handleReparent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmenubarprivate.html#handleReparent
    """
    #  void QMenuBarPrivate::handleReparent()
    self.uglySide.call('ritual_ZN15QMenuBarPrivate14handleReparentEv')

  @overload(QAction)
  @overload(NoneType)
  def getPlatformMenu(
      self,
      action: Optional[QAction],
  ) -> Optional[QPlatformMenu]:
    """
    Calls Qt's 'QPlatformMenu *QMenuBarPrivate::getPlatformMenu(const QAction
    *action)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmenubarprivate.html#getPlatformMenu

    Parameters
    ----------

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QPlatformMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformMenu *QMenuBarPrivate::getPlatformMenu(const QAction *action)
    address = self.uglySide.call(
        'ritual_ZN15QMenuBarPrivate15getPlatformMenuEPK7QAction',
        self._addressOf(action),
    )
    from ..QtGui import QPlatformMenu
    return QPlatformMenu._cuteAt(address)

  @overload(QAction)
  @overload(NoneType)
  def findInsertionPlatformMenu(
      self,
      action: Optional[QAction],
  ) -> Optional[QPlatformMenu]:
    """
    Calls Qt's 'QPlatformMenu
    *QMenuBarPrivate::findInsertionPlatformMenu(const QAction *action)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmenubarprivate.html#findInsertionPlatformMenu

    Parameters
    ----------

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QPlatformMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformMenu *QMenuBarPrivate::findInsertionPlatformMenu(const
    #      QAction *action)
    address = self.uglySide.call(
        'ritual_ZN15QMenuBarPrivate25findInsertionPlatformMenuEPK7QAction',
        self._addressOf(action),
    )
    from ..QtGui import QPlatformMenu
    return QPlatformMenu._cuteAt(address)

  @overload(QAction, QPlatformMenu)
  @overload(QAction, NoneType)
  @overload(NoneType, QPlatformMenu)
  @overload(NoneType, NoneType)
  def copyActionToPlatformMenu(
      self,
      e: Optional[QAction],
      menu: Optional[QPlatformMenu],
  ) -> None:
    """
    Calls Qt's 'void QMenuBarPrivate::copyActionToPlatformMenu(const QAction
    *e, QPlatformMenu *menu)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmenubarprivate.html#copyActionToPlatformMenu

    Parameters
    ----------

    e : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    menu : Optional[QPlatformMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMenuBarPrivate::copyActionToPlatformMenu(const QAction *e,
    #      QPlatformMenu *menu)
    self.uglySide.call(
        'ritual_ZN15QMenuBarPrivate24copyActionToPlatformMenuEPK7QActionP13'
        'QPlatformMenu',
        self._addressOf(e), self._addressOf(menu),
    )

  @staticmethod
  def menuRect(*__, **_) -> Never:
    """
    Qt's 'QRect QMenuBarPrivate::menuRect(bool a0) const': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: member access into incomplete type 'QMenuBarExtension'.
    """
    raise NotImplementedError(
        "'QMenuBarPrivate.menuRect' has no cute function yet. Qt's 'QRect "
        "QMenuBarPrivate::menuRect(bool a0) const': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type "
        "'QMenuBarExtension'.")

  @staticmethod
  def updateGeometries(*__, **_) -> Never:
    """
    Qt's 'void QMenuBarPrivate::updateGeometries()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    member access into incomplete type 'QMenuBarExtension'.
    """
    raise NotImplementedError(
        "'QMenuBarPrivate.updateGeometries' has no cute function yet. Qt's "
        "'void QMenuBarPrivate::updateGeometries()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type "
        "'QMenuBarExtension'.")
