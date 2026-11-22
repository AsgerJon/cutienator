"""
QToolButton binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qtoolbutton.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QAbstractButton, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QPoint, QSize, QTimerEvent
  from ..QtGui import QAction, QActionEvent, QEnterEvent, QMouseEvent
  from ..QtGui import QPaintEvent
  from . import QMenu, QStyleOptionToolButton
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAction = WAIT['QAction']
  QActionEvent = WAIT['QActionEvent']
  QEnterEvent = WAIT['QEnterEvent']
  QEvent = WAIT['QEvent']
  QMenu = WAIT['QMenu']
  QMouseEvent = WAIT['QMouseEvent']
  QPaintEvent = WAIT['QPaintEvent']
  QPoint = WAIT['QPoint']
  QStyleOptionToolButton = WAIT['QStyleOptionToolButton']
  QTimerEvent = WAIT['QTimerEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QToolButton(QAbstractButton):
  """
  The cute side of Qt's QToolButton: a plain Python object standing in front
  of one C++ QToolButton.

  It is built on the cute 'QAbstractButton', as Qt's QToolButton is built on
  Qt's QAbstractButton, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QToolButton that has a ritual and that Python can
  call so far, 30 names in all: 'metaObject', 'tr', 'sizeHint',
  'minimumSizeHint', 'toolButtonStyle', 'arrowType', 'setArrowType',
  'setMenu', 'menu', 'setPopupMode', 'popupMode', 'defaultAction',
  'setAutoRaise', 'autoRaise', 'showMenu', 'setToolButtonStyle',
  'setDefaultAction', 'event', 'mousePressEvent', 'mouseReleaseEvent',
  'paintEvent', 'actionEvent', 'enterEvent', 'leaveEvent', 'timerEvent',
  'changeEvent', 'hitButton', 'checkStateSet', 'nextCheckState',
  'initStyleOption'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QToolButton::~QToolButton()': the destructor: Python never removes
    a C++ QToolButton.

  What has no ritual
  ------------------

  9 of the 41 functions Qt declares: 3 private; 2 takes or gives a type that
  cannot be passed yet; 2 forbidden; 1 a template; 1 a signal.

  What to expect
  --------------

  - The C++ QToolButton is created at the first use, not by
    'QToolButton(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QToolButton.
  - Qt tells when it has removed the C++ QToolButton. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  """

  #  The enums Qt writes inside QToolButton, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class ToolButtonPopupMode(CuteNum):
    """
    The enum 'QToolButton::ToolButtonPopupMode' of Qt, with the 3 names Qt
    gives in it.
    """

    DelayedPopup = Kee[int](0)
    MenuButtonPopup = Kee[int](1)
    InstantPopup = Kee[int](2)

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
    Calls Qt's 'QString QToolButton::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbutton.html#tr

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
    #  QString QToolButton::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN11QToolButton2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QToolButton'

  #  A C++ QToolButton Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QToolButton'

  #  The functions Qt calls itself that QToolButton is the first to declare.
  #  A class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'initStyleOption': (
          ('_ZNK11QToolButton15initStyleOptionEP22QStyleOptionToolButton',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QStyleOptionToolButton'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QToolButton::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbutton.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QToolButton::metaObject() const
    address = self.uglySide.call('ritual_ZNK11QToolButton10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QToolButton::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbutton.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QToolButton::sizeHint() const
    ritual = 'ritual_ZNK11QToolButton8sizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QToolButton8sizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def minimumSizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QToolButton::minimumSizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbutton.html#minimumSizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QToolButton::minimumSizeHint() const
    ritual = 'ritual_ZNK11QToolButton15minimumSizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK11QToolButton15minimumSizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def toolButtonStyle(self) -> Qt.ToolButtonStyle:
    """
    Calls Qt's 'Qt::ToolButtonStyle QToolButton::toolButtonStyle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbutton.html#toolButtonStyle

    Returns
    -------

    Qt.ToolButtonStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.ToolButtonStyle(number)' gives.
    """
    #  Qt::ToolButtonStyle QToolButton::toolButtonStyle() const
    return Qt.ToolButtonStyle(self.uglySide.call(
        'ritual_ZNK11QToolButton15toolButtonStyleEv',
    ))

  def arrowType(self) -> Qt.ArrowType:
    """
    Calls Qt's 'Qt::ArrowType QToolButton::arrowType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbutton.html#arrowType

    Returns
    -------

    Qt.ArrowType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.ArrowType(number)'
      gives.
    """
    #  Qt::ArrowType QToolButton::arrowType() const
    return Qt.ArrowType(self.uglySide.call(
        'ritual_ZNK11QToolButton9arrowTypeEv',
    ))

  def menu(self) -> Optional[QMenu]:
    """
    Calls Qt's 'QMenu *QToolButton::menu() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbutton.html#menu

    Returns
    -------

    Optional[QMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMenu *QToolButton::menu() const
    address = self.uglySide.call('ritual_ZNK11QToolButton4menuEv')
    from . import QMenu
    return QMenu._cuteAt(address)

  def popupMode(self) -> ToolButtonPopupMode:
    """
    Calls Qt's 'ToolButtonPopupMode QToolButton::popupMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbutton.html#popupMode

    Returns
    -------

    ToolButtonPopupMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'ToolButtonPopupMode(number)' gives.
    """
    #  ToolButtonPopupMode QToolButton::popupMode() const
    return QToolButton.ToolButtonPopupMode(self.uglySide.call(
        'ritual_ZNK11QToolButton9popupModeEv',
    ))

  def defaultAction(self) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QToolButton::defaultAction() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbutton.html#defaultAction

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QToolButton::defaultAction() const
    address = self.uglySide.call('ritual_ZNK11QToolButton13defaultActionEv')
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  def autoRaise(self) -> bool:
    """
    Calls Qt's 'bool QToolButton::autoRaise() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbutton.html#autoRaise
    """
    #  bool QToolButton::autoRaise() const
    return self.uglySide.call('ritual_ZNK11QToolButton9autoRaiseEv')

  @overload(QPoint)
  def hitButton(self, pos: QPoint) -> bool:
    """
    Calls Qt's 'bool QToolButton::hitButton(const QPoint &pos) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbutton.html#hitButton

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  bool QToolButton::hitButton(const QPoint &pos) const
    return self.uglySide.call(
        'ritual_own_ZNK11QToolButton9hitButtonERK6QPoint',
        self._valueOf(pos),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.ArrowType)
  def setArrowType(self, type: Qt.ArrowType) -> None:
    """
    Calls Qt's 'void QToolButton::setArrowType(Qt::ArrowType type)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbutton.html#setArrowType

    Parameters
    ----------

    type : Qt.ArrowType
      Passed on as its number.
    """
    #  void QToolButton::setArrowType(Qt::ArrowType type)
    self.uglySide.call(
        'ritual_ZN11QToolButton12setArrowTypeEN2Qt9ArrowTypeE', type.value,
    )

  @overload(QMenu)
  @overload(NoneType)
  def setMenu(self, menu: Optional[QMenu]) -> None:
    """
    Calls Qt's 'void QToolButton::setMenu(QMenu *menu)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbutton.html#setMenu

    Parameters
    ----------

    menu : Optional[QMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QToolButton::setMenu(QMenu *menu)
    self.uglySide.call(
        'ritual_ZN11QToolButton7setMenuEP5QMenu', self._addressOf(menu),
    )

  @overload(ToolButtonPopupMode)
  def setPopupMode(self, mode: ToolButtonPopupMode) -> None:
    """
    Calls Qt's 'void QToolButton::setPopupMode(ToolButtonPopupMode mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbutton.html#setPopupMode

    Parameters
    ----------

    mode : ToolButtonPopupMode
      Passed on as its number.
    """
    #  void QToolButton::setPopupMode(ToolButtonPopupMode mode)
    self.uglySide.call(
        'ritual_ZN11QToolButton12setPopupModeENS_19ToolButtonPopupModeE',
        mode.value,
    )

  @overload(bool)
  def setAutoRaise(self, enable: bool) -> None:
    """
    Calls Qt's 'void QToolButton::setAutoRaise(bool enable)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbutton.html#setAutoRaise

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QToolButton::setAutoRaise(bool enable)
    self.uglySide.call('ritual_ZN11QToolButton12setAutoRaiseEb', enable)

  @overload(Qt.ToolButtonStyle)
  def setToolButtonStyle(self, style: Qt.ToolButtonStyle) -> None:
    """
    Calls Qt's 'void QToolButton::setToolButtonStyle(Qt::ToolButtonStyle
    style)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtoolbutton.html#setToolButtonStyle

    Parameters
    ----------

    style : Qt.ToolButtonStyle
      Passed on as its number.
    """
    #  void QToolButton::setToolButtonStyle(Qt::ToolButtonStyle style)
    self.uglySide.call(
        'ritual_ZN11QToolButton18setToolButtonStyleEN2Qt15ToolButtonStyleE',
        style.value,
    )

  @overload(QAction)
  @overload(NoneType)
  def setDefaultAction(self, a0: Optional[QAction]) -> None:
    """
    Calls Qt's 'void QToolButton::setDefaultAction(QAction *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbutton.html#setDefaultAction

    Parameters
    ----------

    a0 : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QToolButton::setDefaultAction(QAction *a0)
    self.uglySide.call(
        'ritual_ZN11QToolButton16setDefaultActionEP7QAction',
        self._addressOf(a0),
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
  @overload(QWidget)
  @overload(NoneType)
  def __init__(self, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's 'QToolButton::QToolButton(QWidget
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbutton.html#QToolButton

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QToolButton::QToolButton(QWidget *parent)
    self._noteCreation(QToolButton, lambda: Rituals.call(
        'ritual_ZN11QToolButtonC1EP7QWidget', self._addressOf(parent),
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

  def showMenu(self) -> None:
    """
    Calls Qt's 'void QToolButton::showMenu()'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbutton.html#showMenu
    """
    #  void QToolButton::showMenu()
    self.uglySide.call('ritual_ZN11QToolButton8showMenuEv')

  @overload(QEvent)
  @overload(NoneType)
  def event(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QToolButton::event(QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbutton.html#event

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QToolButton::event(QEvent *e)
    return self.uglySide.call(
        'ritual_own_ZN11QToolButton5eventEP6QEvent', self._addressOf(e),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, a0: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QToolButton::mousePressEvent(QMouseEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbutton.html#mousePressEvent

    Parameters
    ----------

    a0 : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QToolButton::mousePressEvent(QMouseEvent *a0)
    self.uglySide.call(
        'ritual_own_ZN11QToolButton15mousePressEventEP11QMouseEvent',
        self._addressOf(a0),
    )

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(self, a0: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QToolButton::mouseReleaseEvent(QMouseEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbutton.html#mouseReleaseEvent

    Parameters
    ----------

    a0 : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QToolButton::mouseReleaseEvent(QMouseEvent *a0)
    self.uglySide.call(
        'ritual_own_ZN11QToolButton17mouseReleaseEventEP11QMouseEvent',
        self._addressOf(a0),
    )

  @overload(QPaintEvent)
  @overload(NoneType)
  def paintEvent(self, a0: Optional[QPaintEvent]) -> None:
    """
    Calls Qt's 'void QToolButton::paintEvent(QPaintEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbutton.html#paintEvent

    Parameters
    ----------

    a0 : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QToolButton::paintEvent(QPaintEvent *a0)
    self.uglySide.call(
        'ritual_own_ZN11QToolButton10paintEventEP11QPaintEvent',
        self._addressOf(a0),
    )

  @overload(QActionEvent)
  @overload(NoneType)
  def actionEvent(self, a0: Optional[QActionEvent]) -> None:
    """
    Calls Qt's 'void QToolButton::actionEvent(QActionEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbutton.html#actionEvent

    Parameters
    ----------

    a0 : Optional[QActionEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QToolButton::actionEvent(QActionEvent *a0)
    self.uglySide.call(
        'ritual_own_ZN11QToolButton11actionEventEP12QActionEvent',
        self._addressOf(a0),
    )

  @overload(QEnterEvent)
  @overload(NoneType)
  def enterEvent(self, a0: Optional[QEnterEvent]) -> None:
    """
    Calls Qt's 'void QToolButton::enterEvent(QEnterEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbutton.html#enterEvent

    Parameters
    ----------

    a0 : Optional[QEnterEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QToolButton::enterEvent(QEnterEvent *a0)
    self.uglySide.call(
        'ritual_own_ZN11QToolButton10enterEventEP11QEnterEvent',
        self._addressOf(a0),
    )

  @overload(QEvent)
  @overload(NoneType)
  def leaveEvent(self, a0: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QToolButton::leaveEvent(QEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbutton.html#leaveEvent

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QToolButton::leaveEvent(QEvent *a0)
    self.uglySide.call(
        'ritual_own_ZN11QToolButton10leaveEventEP6QEvent',
        self._addressOf(a0),
    )

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, a0: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QToolButton::timerEvent(QTimerEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbutton.html#timerEvent

    Parameters
    ----------

    a0 : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QToolButton::timerEvent(QTimerEvent *a0)
    self.uglySide.call(
        'ritual_own_ZN11QToolButton10timerEventEP11QTimerEvent',
        self._addressOf(a0),
    )

  @overload(QEvent)
  @overload(NoneType)
  def changeEvent(self, a0: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QToolButton::changeEvent(QEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbutton.html#changeEvent

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QToolButton::changeEvent(QEvent *a0)
    self.uglySide.call(
        'ritual_own_ZN11QToolButton11changeEventEP6QEvent',
        self._addressOf(a0),
    )

  def checkStateSet(self) -> None:
    """
    Calls Qt's 'void QToolButton::checkStateSet()'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbutton.html#checkStateSet
    """
    #  void QToolButton::checkStateSet()
    self.uglySide.call('ritual_own_ZN11QToolButton13checkStateSetEv')

  def nextCheckState(self) -> None:
    """
    Calls Qt's 'void QToolButton::nextCheckState()'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbutton.html#nextCheckState
    """
    #  void QToolButton::nextCheckState()
    self.uglySide.call('ritual_own_ZN11QToolButton14nextCheckStateEv')

  @overload(QStyleOptionToolButton)
  @overload(NoneType)
  def initStyleOption(
      self,
      option: Optional[QStyleOptionToolButton],
  ) -> None:
    """
    Calls Qt's 'void QToolButton::initStyleOption(QStyleOptionToolButton
    *option) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbutton.html#initStyleOption

    Parameters
    ----------

    option : Optional[QStyleOptionToolButton]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QToolButton::initStyleOption(QStyleOptionToolButton *option)
    #      const
    self.uglySide.call(
        'ritual_own_ZNK11QToolButton15initStyleOptionEP22QStyleOptionToolBu'
        'tton',
        self._addressOf(option),
    )
