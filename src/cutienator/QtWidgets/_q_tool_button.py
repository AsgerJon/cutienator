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

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from . import QAbstractButton, QToolButtonToolButtonPopupMode, QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QSize
  from ..QtGui import QAction
  from . import QMenu
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAction = WAIT['QAction']
  QMenu = WAIT['QMenu']

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
  call so far, 17 names in all: 'metaObject', 'tr', 'sizeHint',
  'minimumSizeHint', 'toolButtonStyle', 'arrowType', 'setArrowType',
  'setMenu', 'menu', 'setPopupMode', 'popupMode', 'defaultAction',
  'setAutoRaise', 'autoRaise', 'showMenu', 'setToolButtonStyle',
  'setDefaultAction'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QToolButton::~QToolButton()': the destructor: Python never removes
    a C++ QToolButton.

  What has no ritual
  ------------------

  22 of the 41 functions Qt declares: 13 protected; 3 private; 2 takes or
  gives a type that cannot be passed yet; 2 forbidden; 1 a template; 1 a
  signal.

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

  #  The enums Qt writes inside QToolButton, and the names Qt has for the
  #  combinations of its flags enums.
  ToolButtonPopupMode = QToolButtonToolButtonPopupMode

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
    address = self.uglySide.call('ritual_ZNK11QToolButton8sizeHintEv')
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
    address = self.uglySide.call(
        'ritual_ZNK11QToolButton15minimumSizeHintEv',
    )
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
