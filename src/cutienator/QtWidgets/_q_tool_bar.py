"""
QToolBar binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qtoolbar.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList
from . import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QPoint, QRect, QSize
  from ..QtGui import QAction, QActionEvent, QPaintEvent
  from . import QStyleOptionToolBar
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAction = WAIT['QAction']
  QActionEvent = WAIT['QActionEvent']
  QEvent = WAIT['QEvent']
  QPaintEvent = WAIT['QPaintEvent']
  QPoint = WAIT['QPoint']
  QSize = WAIT['QSize']
  QStyleOptionToolBar = WAIT['QStyleOptionToolBar']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QToolBar(QWidget):
  """
  The cute side of Qt's QToolBar: a plain Python object standing in front of
  one C++ QToolBar.

  It is built on the cute 'QWidget', as Qt's QToolBar is built on Qt's
  QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QToolBar that has a ritual and that Python can call
  so far, 30 names in all: 'metaObject', 'tr', 'setMovable', 'isMovable',
  'setAllowedAreas', 'allowedAreas', 'isAreaAllowed', 'setOrientation',
  'orientation', 'clear', 'addSeparator', 'insertSeparator', 'addWidget',
  'insertWidget', 'actionGeometry', 'actionAt', 'toggleViewAction',
  'iconSize', 'toolButtonStyle', 'widgetForAction', 'isFloatable',
  'setFloatable', 'isFloating', 'setIconSize', 'setToolButtonStyle',
  'actionEvent', 'changeEvent', 'paintEvent', 'event', 'initStyleOption'. It
  can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QToolBar::~QToolBar()': the destructor: Python never removes a C++
    QToolBar.
  - Qt's 'QToolBarPrivate *QToolBar::d_func()': gives 'QToolBarPrivate',
    which has no cute class yet.
  - Qt's 'const QToolBarPrivate *QToolBar::d_func() const': gives
    'QToolBarPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  14 of the 50 functions Qt declares: 8 a signal; 2 takes or gives a type
  that cannot be passed yet; 2 forbidden; 1 a template; 1 declared and
  nowhere to be found.

  What to expect
  --------------

  - The C++ QToolBar is created at the first use, not by 'QToolBar(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QToolBar.
  - Qt tells when it has removed the C++ QToolBar. Every call on the cute
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
    Calls Qt's 'QString QToolBar::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbar.html#tr

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
    #  QString QToolBar::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN8QToolBar2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QToolBar'

  #  A C++ QToolBar Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QToolBar'

  #  The functions Qt calls itself that QToolBar is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'initStyleOption': (
          ('_ZNK8QToolBar15initStyleOptionEP19QStyleOptionToolBar',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QStyleOptionToolBar'),
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
    Calls Qt's 'const QMetaObject *QToolBar::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbar.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QToolBar::metaObject() const
    address = self.uglySide.call('ritual_ZNK8QToolBar10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isMovable(self) -> bool:
    """
    Calls Qt's 'bool QToolBar::isMovable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbar.html#isMovable
    """
    #  bool QToolBar::isMovable() const
    return self.uglySide.call('ritual_ZNK8QToolBar9isMovableEv')

  def allowedAreas(self) -> Qt.ToolBarAreas:
    """
    Calls Qt's 'Qt::ToolBarAreas QToolBar::allowedAreas() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbar.html#allowedAreas

    Returns
    -------

    Qt.ToolBarAreas
      The value standing for the combination Qt gave back.
    """
    #  Qt::ToolBarAreas QToolBar::allowedAreas() const
    return Qt.ToolBarAreas(self.uglySide.call(
        'ritual_ZNK8QToolBar12allowedAreasEv',
    ))

  @overload(Qt.ToolBarArea)
  def isAreaAllowed(self, area: Qt.ToolBarArea) -> bool:
    """
    Calls Qt's 'bool QToolBar::isAreaAllowed(Qt::ToolBarArea area) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbar.html#isAreaAllowed

    Parameters
    ----------

    area : Qt.ToolBarArea
      Passed on as its number.
    """
    #  bool QToolBar::isAreaAllowed(Qt::ToolBarArea area) const
    return self.uglySide.call(
        'ritual_ZNK8QToolBar13isAreaAllowedEN2Qt11ToolBarAreaE', area.value,
    )

  def orientation(self) -> Qt.Orientation:
    """
    Calls Qt's 'Qt::Orientation QToolBar::orientation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbar.html#orientation

    Returns
    -------

    Qt.Orientation
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Qt.Orientation(number)'
      gives.
    """
    #  Qt::Orientation QToolBar::orientation() const
    return Qt.Orientation(self.uglySide.call(
        'ritual_ZNK8QToolBar11orientationEv',
    ))

  @overload(QAction)
  @overload(NoneType)
  def actionGeometry(self, action: Optional[QAction]) -> QRect:
    """
    Calls Qt's 'QRect QToolBar::actionGeometry(QAction *action) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbar.html#actionGeometry

    Parameters
    ----------

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QToolBar::actionGeometry(QAction *action) const
    address = self.uglySide.call(
        'ritual_ZNK8QToolBar14actionGeometryEP7QAction',
        self._addressOf(action),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QPoint)
  def actionAt(self, p: QPoint) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QToolBar::actionAt(const QPoint &p) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbar.html#actionAt

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
    #  QAction *QToolBar::actionAt(const QPoint &p) const
    address = self.uglySide.call(
        'ritual_ZNK8QToolBar8actionAtERK6QPoint', self._valueOf(p),
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  @overload(int, int)
  def actionAt(self, x: int, y: int) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QToolBar::actionAt(int x, int y) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbar.html#actionAt

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QToolBar::actionAt(int x, int y) const
    address = self.uglySide.call('ritual_ZNK8QToolBar8actionAtEii', x, y)
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  def toggleViewAction(self) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QToolBar::toggleViewAction() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbar.html#toggleViewAction

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QToolBar::toggleViewAction() const
    address = self.uglySide.call('ritual_ZNK8QToolBar16toggleViewActionEv')
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  def iconSize(self) -> QSize:
    """
    Calls Qt's 'QSize QToolBar::iconSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbar.html#iconSize

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QToolBar::iconSize() const
    address = self.uglySide.call('ritual_ZNK8QToolBar8iconSizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def toolButtonStyle(self) -> Qt.ToolButtonStyle:
    """
    Calls Qt's 'Qt::ToolButtonStyle QToolBar::toolButtonStyle() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbar.html#toolButtonStyle

    Returns
    -------

    Qt.ToolButtonStyle
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.ToolButtonStyle(number)' gives.
    """
    #  Qt::ToolButtonStyle QToolBar::toolButtonStyle() const
    return Qt.ToolButtonStyle(self.uglySide.call(
        'ritual_ZNK8QToolBar15toolButtonStyleEv',
    ))

  @overload(QAction)
  @overload(NoneType)
  def widgetForAction(self, action: Optional[QAction]) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QToolBar::widgetForAction(QAction *action) const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbar.html#widgetForAction

    Parameters
    ----------

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QToolBar::widgetForAction(QAction *action) const
    address = self.uglySide.call(
        'ritual_ZNK8QToolBar15widgetForActionEP7QAction',
        self._addressOf(action),
    )
    return QWidget._cuteAt(address)

  def isFloatable(self) -> bool:
    """
    Calls Qt's 'bool QToolBar::isFloatable() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbar.html#isFloatable
    """
    #  bool QToolBar::isFloatable() const
    return self.uglySide.call('ritual_ZNK8QToolBar11isFloatableEv')

  def isFloating(self) -> bool:
    """
    Calls Qt's 'bool QToolBar::isFloating() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbar.html#isFloating
    """
    #  bool QToolBar::isFloating() const
    return self.uglySide.call('ritual_ZNK8QToolBar10isFloatingEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setMovable(self, movable: bool) -> None:
    """
    Calls Qt's 'void QToolBar::setMovable(bool movable)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbar.html#setMovable

    Parameters
    ----------

    movable : bool
      Passed on as it is.
    """
    #  void QToolBar::setMovable(bool movable)
    self.uglySide.call('ritual_ZN8QToolBar10setMovableEb', movable)

  @overload(Qt.ToolBarAreas)
  def setAllowedAreas(self, areas: Qt.ToolBarAreas) -> None:
    """
    Calls Qt's 'void QToolBar::setAllowedAreas(Qt::ToolBarAreas areas)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbar.html#setAllowedAreas

    Parameters
    ----------

    areas : Qt.ToolBarAreas
      Passed on as its number.
    """
    #  void QToolBar::setAllowedAreas(Qt::ToolBarAreas areas)
    self.uglySide.call(
        'ritual_ZN8QToolBar15setAllowedAreasE6QFlagsIN2Qt11ToolBarAreaEE',
        areas.value,
    )

  @overload(Qt.Orientation)
  def setOrientation(self, orientation: Qt.Orientation) -> None:
    """
    Calls Qt's 'void QToolBar::setOrientation(Qt::Orientation orientation)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbar.html#setOrientation

    Parameters
    ----------

    orientation : Qt.Orientation
      Passed on as its number.
    """
    #  void QToolBar::setOrientation(Qt::Orientation orientation)
    self.uglySide.call(
        'ritual_ZN8QToolBar14setOrientationEN2Qt11OrientationE',
        orientation.value,
    )

  @overload(bool)
  def setFloatable(self, floatable: bool) -> None:
    """
    Calls Qt's 'void QToolBar::setFloatable(bool floatable)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbar.html#setFloatable

    Parameters
    ----------

    floatable : bool
      Passed on as it is.
    """
    #  void QToolBar::setFloatable(bool floatable)
    self.uglySide.call('ritual_ZN8QToolBar12setFloatableEb', floatable)

  @overload(QSize)
  def setIconSize(self, iconSize: QSize) -> None:
    """
    Calls Qt's 'void QToolBar::setIconSize(const QSize &iconSize)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbar.html#setIconSize

    Parameters
    ----------

    iconSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QToolBar::setIconSize(const QSize &iconSize)
    self.uglySide.call(
        'ritual_ZN8QToolBar11setIconSizeERK5QSize', self._valueOf(iconSize),
    )

  @overload(Qt.ToolButtonStyle)
  def setToolButtonStyle(self, toolButtonStyle: Qt.ToolButtonStyle) -> None:
    """
    Calls Qt's 'void QToolBar::setToolButtonStyle(Qt::ToolButtonStyle
    toolButtonStyle)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbar.html#setToolButtonStyle

    Parameters
    ----------

    toolButtonStyle : Qt.ToolButtonStyle
      Passed on as its number.
    """
    #  void QToolBar::setToolButtonStyle(Qt::ToolButtonStyle toolButtonStyle)
    self.uglySide.call(
        'ritual_ZN8QToolBar18setToolButtonStyleEN2Qt15ToolButtonStyleE',
        toolButtonStyle.value,
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

  @overload(str)
  @overload(str, QWidget)
  @overload(str, NoneType)
  def __init__(self, title: str, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's 'QToolBar::QToolBar(const QString &title,
    QWidget *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbar.html#QToolBar

    Parameters
    ----------

    title : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QToolBar::QToolBar(const QString &title, QWidget *parent)
    self._noteCreation(QToolBar, lambda: Rituals.call(
        'ritual_ZN8QToolBarC1ERK7QStringP7QWidget',
        title, self._addressOf(parent),
    ))

  @overload()
  @overload(QWidget)
  @overload(NoneType)
  def __init__(self, parent: Optional[QWidget] = None) -> None:
    """
    Notes what was given, for Qt's 'QToolBar::QToolBar(QWidget *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbar.html#QToolBar

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QToolBar::QToolBar(QWidget *parent)
    self._noteCreation(QToolBar, lambda: Rituals.call(
        'ritual_ZN8QToolBarC1EP7QWidget', self._addressOf(parent),
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

  def clear(self) -> None:
    """
    Calls Qt's 'void QToolBar::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbar.html#clear
    """
    #  void QToolBar::clear()
    self.uglySide.call('ritual_ZN8QToolBar5clearEv')

  def addSeparator(self) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QToolBar::addSeparator()'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbar.html#addSeparator

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QToolBar::addSeparator()
    address = self.uglySide.call('ritual_ZN8QToolBar12addSeparatorEv')
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  @overload(QAction)
  @overload(NoneType)
  def insertSeparator(self, before: Optional[QAction]) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QToolBar::insertSeparator(QAction *before)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbar.html#insertSeparator

    Parameters
    ----------

    before : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QToolBar::insertSeparator(QAction *before)
    address = self.uglySide.call(
        'ritual_ZN8QToolBar15insertSeparatorEP7QAction',
        self._addressOf(before),
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  @overload(QWidget)
  @overload(NoneType)
  def addWidget(self, widget: Optional[QWidget]) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QToolBar::addWidget(QWidget *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbar.html#addWidget

    Parameters
    ----------

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QToolBar::addWidget(QWidget *widget)
    address = self.uglySide.call(
        'ritual_ZN8QToolBar9addWidgetEP7QWidget', self._addressOf(widget),
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  @overload(QAction, QWidget)
  @overload(QAction, NoneType)
  @overload(NoneType, QWidget)
  @overload(NoneType, NoneType)
  def insertWidget(
      self,
      before: Optional[QAction],
      widget: Optional[QWidget],
  ) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QToolBar::insertWidget(QAction *before, QWidget
    *widget)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbar.html#insertWidget

    Parameters
    ----------

    before : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    widget : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QToolBar::insertWidget(QAction *before, QWidget *widget)
    address = self.uglySide.call(
        'ritual_ZN8QToolBar12insertWidgetEP7QActionP7QWidget',
        self._addressOf(before), self._addressOf(widget),
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  @overload(QActionEvent)
  @overload(NoneType)
  def actionEvent(self, event: Optional[QActionEvent]) -> None:
    """
    Calls Qt's 'void QToolBar::actionEvent(QActionEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbar.html#actionEvent

    Parameters
    ----------

    event : Optional[QActionEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QToolBar::actionEvent(QActionEvent *event)
    ritual = 'ritual_ZN8QToolBar11actionEventEP12QActionEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QToolBar11actionEventEP12QActionEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QEvent)
  @overload(NoneType)
  def changeEvent(self, event: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QToolBar::changeEvent(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbar.html#changeEvent

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QToolBar::changeEvent(QEvent *event)
    ritual = 'ritual_ZN8QToolBar11changeEventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QToolBar11changeEventEP6QEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QPaintEvent)
  @overload(NoneType)
  def paintEvent(self, event: Optional[QPaintEvent]) -> None:
    """
    Calls Qt's 'void QToolBar::paintEvent(QPaintEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbar.html#paintEvent

    Parameters
    ----------

    event : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QToolBar::paintEvent(QPaintEvent *event)
    ritual = 'ritual_ZN8QToolBar10paintEventEP11QPaintEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QToolBar10paintEventEP11QPaintEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QToolBar::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbar.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QToolBar::event(QEvent *event)
    ritual = 'ritual_ZN8QToolBar5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QToolBar5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  @overload(QStyleOptionToolBar)
  @overload(NoneType)
  def initStyleOption(self, option: Optional[QStyleOptionToolBar]) -> None:
    """
    Calls Qt's 'void QToolBar::initStyleOption(QStyleOptionToolBar *option)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtoolbar.html#initStyleOption

    Parameters
    ----------

    option : Optional[QStyleOptionToolBar]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QToolBar::initStyleOption(QStyleOptionToolBar *option) const
    ritual = 'ritual_ZNK8QToolBar15initStyleOptionEP19QStyleOptionToolBar'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK8QToolBar15initStyleOptionEP19QStyleOptionToolBar')
    self.uglySide.call(ritual, self._addressOf(option))


#  Qt's 'QList<QToolBar *>': the list of QToolBar, which 'QList[QToolBar]'
#  gives. It is made here, so that there is one as soon as there can be a
#  QToolBar.
QList.createKind(
    QToolBar, 'address',
    make='ritual_list_make_QToolBar_ptr',
    add='ritual_list_add_QToolBar_ptr',
    size='ritual_list_size_QToolBar_ptr',
    at='ritual_list_at_QToolBar_ptr',
    drop='ritual_list_drop_QToolBar_ptr',
)
