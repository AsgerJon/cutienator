"""
QMenuBar binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWidgets/qmenubar.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QObject
from . import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QPoint, QRect, QSize, QTimerEvent
  from ..QtGui import QAction, QActionEvent, QFocusEvent, QIcon, QKeyEvent
  from ..QtGui import QMouseEvent, QPaintEvent, QResizeEvent
  from . import QMenu, QStyleOptionMenuItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAction = WAIT['QAction']
  QActionEvent = WAIT['QActionEvent']
  QEvent = WAIT['QEvent']
  QFocusEvent = WAIT['QFocusEvent']
  QIcon = WAIT['QIcon']
  QKeyEvent = WAIT['QKeyEvent']
  QMenu = WAIT['QMenu']
  QMouseEvent = WAIT['QMouseEvent']
  QPaintEvent = WAIT['QPaintEvent']
  QPoint = WAIT['QPoint']
  QResizeEvent = WAIT['QResizeEvent']
  QStyleOptionMenuItem = WAIT['QStyleOptionMenuItem']
  QTimerEvent = WAIT['QTimerEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMenuBar(QWidget):
  """
  The cute side of Qt's QMenuBar: a plain Python object standing in front of
  one C++ QMenuBar.

  It is built on the cute 'QWidget', as Qt's QMenuBar is built on Qt's
  QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QMenuBar that has a ritual and that Python can call
  so far, 36 names in all: 'metaObject', 'tr', 'addMenu', 'addSeparator',
  'insertSeparator', 'insertMenu', 'clear', 'activeAction',
  'setActiveAction', 'setDefaultUp', 'isDefaultUp', 'sizeHint',
  'minimumSizeHint', 'heightForWidth', 'actionGeometry', 'actionAt',
  'setCornerWidget', 'cornerWidget', 'isNativeMenuBar', 'setNativeMenuBar',
  'setVisible', 'changeEvent', 'keyPressEvent', 'mouseReleaseEvent',
  'mousePressEvent', 'mouseMoveEvent', 'leaveEvent', 'paintEvent',
  'resizeEvent', 'actionEvent', 'focusOutEvent', 'focusInEvent',
  'timerEvent', 'eventFilter', 'event', 'initStyleOption'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMenuBar::~QMenuBar()': the destructor: Python never removes a C++
    QMenuBar.

  What has no ritual
  ------------------

  11 of the 51 functions Qt declares: 5 takes or gives a type that cannot be
  passed yet; 2 a signal; 2 forbidden; 1 a template; 1 declared and nowhere
  to be found.

  What to expect
  --------------

  - The C++ QMenuBar is created at the first use, not by 'QMenuBar(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMenuBar.
  - Qt tells when it has removed the C++ QMenuBar. Every call on the cute
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
    Calls Qt's 'QString QMenuBar::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenubar.html#tr

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
    #  QString QMenuBar::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN8QMenuBar2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMenuBar'

  #  A C++ QMenuBar Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QMenuBar'

  #  The functions Qt calls itself that QMenuBar is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'initStyleOption': (
          ('_ZNK8QMenuBar15initStyleOptionEP20QStyleOptionMenuItemPK7QActio'
           'n',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtWidgets:QStyleOptionMenuItem'),
               ('address', 'address', 'QtGui:QAction'),
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
    Calls Qt's 'const QMetaObject *QMenuBar::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmenubar.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QMenuBar::metaObject() const
    address = self.uglySide.call('ritual_ZNK8QMenuBar10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def activeAction(self) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QMenuBar::activeAction() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmenubar.html#activeAction

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QMenuBar::activeAction() const
    address = self.uglySide.call('ritual_ZNK8QMenuBar12activeActionEv')
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  def isDefaultUp(self) -> bool:
    """
    Calls Qt's 'bool QMenuBar::isDefaultUp() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmenubar.html#isDefaultUp
    """
    #  bool QMenuBar::isDefaultUp() const
    return self.uglySide.call('ritual_ZNK8QMenuBar11isDefaultUpEv')

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QMenuBar::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmenubar.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QMenuBar::sizeHint() const
    ritual = 'ritual_ZNK8QMenuBar8sizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK8QMenuBar8sizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def minimumSizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QMenuBar::minimumSizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmenubar.html#minimumSizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QMenuBar::minimumSizeHint() const
    ritual = 'ritual_ZNK8QMenuBar15minimumSizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK8QMenuBar15minimumSizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  @overload(int)
  def heightForWidth(self, a0: int) -> int:
    """
    Calls Qt's 'int QMenuBar::heightForWidth(int a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmenubar.html#heightForWidth

    Parameters
    ----------

    a0 : int
      Passed on as it is.
    """
    #  int QMenuBar::heightForWidth(int a0) const
    ritual = 'ritual_ZNK8QMenuBar14heightForWidthEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK8QMenuBar14heightForWidthEi'
    return self.uglySide.call(ritual, a0)

  @overload(QAction)
  @overload(NoneType)
  def actionGeometry(self, a0: Optional[QAction]) -> QRect:
    """
    Calls Qt's 'QRect QMenuBar::actionGeometry(QAction *a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmenubar.html#actionGeometry

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
    #  QRect QMenuBar::actionGeometry(QAction *a0) const
    address = self.uglySide.call(
        'ritual_ZNK8QMenuBar14actionGeometryEP7QAction', self._addressOf(a0),
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

  @overload(QPoint)
  def actionAt(self, a0: QPoint) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QMenuBar::actionAt(const QPoint &a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmenubar.html#actionAt

    Parameters
    ----------

    a0 : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QMenuBar::actionAt(const QPoint &a0) const
    address = self.uglySide.call(
        'ritual_ZNK8QMenuBar8actionAtERK6QPoint', self._valueOf(a0),
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  @overload()
  @overload(Qt.Corner)
  def cornerWidget(
      self,
      corner: Qt.Corner = Qt.Corner.TopRightCorner,
  ) -> Optional[QWidget]:
    """
    Calls Qt's 'QWidget *QMenuBar::cornerWidget(Qt::Corner corner) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmenubar.html#cornerWidget

    Parameters
    ----------

    corner : Qt.Corner
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.Corner.TopRightCorner.

    Returns
    -------

    Optional[QWidget]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWidget *QMenuBar::cornerWidget(Qt::Corner corner) const
    address = self.uglySide.call(
        'ritual_ZNK8QMenuBar12cornerWidgetEN2Qt6CornerE', corner.value,
    )
    return QWidget._cuteAt(address)

  def isNativeMenuBar(self) -> bool:
    """
    Calls Qt's 'bool QMenuBar::isNativeMenuBar() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmenubar.html#isNativeMenuBar
    """
    #  bool QMenuBar::isNativeMenuBar() const
    return self.uglySide.call('ritual_ZNK8QMenuBar15isNativeMenuBarEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAction)
  @overload(NoneType)
  def setActiveAction(self, action: Optional[QAction]) -> None:
    """
    Calls Qt's 'void QMenuBar::setActiveAction(QAction *action)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenubar.html#setActiveAction

    Parameters
    ----------

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMenuBar::setActiveAction(QAction *action)
    self.uglySide.call(
        'ritual_ZN8QMenuBar15setActiveActionEP7QAction',
        self._addressOf(action),
    )

  @overload(bool)
  def setDefaultUp(self, a0: bool) -> None:
    """
    Calls Qt's 'void QMenuBar::setDefaultUp(bool a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenubar.html#setDefaultUp

    Parameters
    ----------

    a0 : bool
      Passed on as it is.
    """
    #  void QMenuBar::setDefaultUp(bool a0)
    self.uglySide.call('ritual_ZN8QMenuBar12setDefaultUpEb', a0)

  @overload(QWidget)
  @overload(NoneType)
  @overload(QWidget, Qt.Corner)
  @overload(NoneType, Qt.Corner)
  def setCornerWidget(
      self,
      w: Optional[QWidget],
      corner: Qt.Corner = Qt.Corner.TopRightCorner,
  ) -> None:
    """
    Calls Qt's 'void QMenuBar::setCornerWidget(QWidget *w, Qt::Corner
    corner)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenubar.html#setCornerWidget

    Parameters
    ----------

    w : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    corner : Qt.Corner
      Passed on as its number. May be left out, as in Qt: it is then
      Qt.Corner.TopRightCorner.
    """
    #  void QMenuBar::setCornerWidget(QWidget *w, Qt::Corner corner)
    self.uglySide.call(
        'ritual_ZN8QMenuBar15setCornerWidgetEP7QWidgetN2Qt6CornerE',
        self._addressOf(w), corner.value,
    )

  @overload(bool)
  def setNativeMenuBar(self, nativeMenuBar: bool) -> None:
    """
    Calls Qt's 'void QMenuBar::setNativeMenuBar(bool nativeMenuBar)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenubar.html#setNativeMenuBar

    Parameters
    ----------

    nativeMenuBar : bool
      Passed on as it is.
    """
    #  void QMenuBar::setNativeMenuBar(bool nativeMenuBar)
    self.uglySide.call(
        'ritual_ZN8QMenuBar16setNativeMenuBarEb', nativeMenuBar,
    )

  @overload(bool)
  def setVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QMenuBar::setVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenubar.html#setVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QMenuBar::setVisible(bool visible)
    ritual = 'ritual_ZN8QMenuBar10setVisibleEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QMenuBar10setVisibleEb'
    self.uglySide.call(ritual, visible)

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
    Notes what was given, for Qt's 'QMenuBar::QMenuBar(QWidget *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmenubar.html#QMenuBar

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QMenuBar::QMenuBar(QWidget *parent)
    self._noteCreation(QMenuBar, lambda: Rituals.call(
        'ritual_ZN8QMenuBarC1EP7QWidget', self._addressOf(parent),
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

  @overload(QMenu)
  @overload(NoneType)
  def addMenu(self, menu: Optional[QMenu]) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QMenuBar::addMenu(QMenu *menu)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenubar.html#addMenu

    Parameters
    ----------

    menu : Optional[QMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QMenuBar::addMenu(QMenu *menu)
    address = self.uglySide.call(
        'ritual_ZN8QMenuBar7addMenuEP5QMenu', self._addressOf(menu),
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  @overload(str)
  def addMenu(self, title: str) -> Optional[QMenu]:
    """
    Calls Qt's 'QMenu *QMenuBar::addMenu(const QString &title)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenubar.html#addMenu

    Parameters
    ----------

    title : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMenu *QMenuBar::addMenu(const QString &title)
    address = self.uglySide.call(
        'ritual_ZN8QMenuBar7addMenuERK7QString', title,
    )
    from . import QMenu
    return QMenu._cuteAt(address)

  @overload(QIcon, str)
  def addMenu(self, icon: QIcon, title: str) -> Optional[QMenu]:
    """
    Calls Qt's 'QMenu *QMenuBar::addMenu(const QIcon &icon, const QString
    &title)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenubar.html#addMenu

    Parameters
    ----------

    icon : QIcon
      Passed on as a value: Qt reads the C++ QIcon, which stays Python's own.

    title : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMenu *QMenuBar::addMenu(const QIcon &icon, const QString &title)
    address = self.uglySide.call(
        'ritual_ZN8QMenuBar7addMenuERK5QIconRK7QString',
        self._valueOf(icon), title,
    )
    from . import QMenu
    return QMenu._cuteAt(address)

  def addSeparator(self) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QMenuBar::addSeparator()'.

    Qt's own words: https://doc.qt.io/qt-6/qmenubar.html#addSeparator

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QMenuBar::addSeparator()
    address = self.uglySide.call('ritual_ZN8QMenuBar12addSeparatorEv')
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  @overload(QAction)
  @overload(NoneType)
  def insertSeparator(self, before: Optional[QAction]) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QMenuBar::insertSeparator(QAction *before)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenubar.html#insertSeparator

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
    #  QAction *QMenuBar::insertSeparator(QAction *before)
    address = self.uglySide.call(
        'ritual_ZN8QMenuBar15insertSeparatorEP7QAction',
        self._addressOf(before),
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  @overload(QAction, QMenu)
  @overload(QAction, NoneType)
  @overload(NoneType, QMenu)
  @overload(NoneType, NoneType)
  def insertMenu(
      self,
      before: Optional[QAction],
      menu: Optional[QMenu],
  ) -> Optional[QAction]:
    """
    Calls Qt's 'QAction *QMenuBar::insertMenu(QAction *before, QMenu *menu)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenubar.html#insertMenu

    Parameters
    ----------

    before : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    menu : Optional[QMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAction *QMenuBar::insertMenu(QAction *before, QMenu *menu)
    address = self.uglySide.call(
        'ritual_ZN8QMenuBar10insertMenuEP7QActionP5QMenu',
        self._addressOf(before), self._addressOf(menu),
    )
    from ..QtGui import QAction
    return QAction._cuteAt(address)

  def clear(self) -> None:
    """
    Calls Qt's 'void QMenuBar::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qmenubar.html#clear
    """
    #  void QMenuBar::clear()
    self.uglySide.call('ritual_ZN8QMenuBar5clearEv')

  @overload(QEvent)
  @overload(NoneType)
  def changeEvent(self, a0: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QMenuBar::changeEvent(QEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenubar.html#changeEvent

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMenuBar::changeEvent(QEvent *a0)
    ritual = 'ritual_ZN8QMenuBar11changeEventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QMenuBar11changeEventEP6QEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, a0: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QMenuBar::keyPressEvent(QKeyEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenubar.html#keyPressEvent

    Parameters
    ----------

    a0 : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMenuBar::keyPressEvent(QKeyEvent *a0)
    ritual = 'ritual_ZN8QMenuBar13keyPressEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QMenuBar13keyPressEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseReleaseEvent(self, a0: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QMenuBar::mouseReleaseEvent(QMouseEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenubar.html#mouseReleaseEvent

    Parameters
    ----------

    a0 : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMenuBar::mouseReleaseEvent(QMouseEvent *a0)
    ritual = 'ritual_ZN8QMenuBar17mouseReleaseEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QMenuBar17mouseReleaseEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mousePressEvent(self, a0: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QMenuBar::mousePressEvent(QMouseEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenubar.html#mousePressEvent

    Parameters
    ----------

    a0 : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMenuBar::mousePressEvent(QMouseEvent *a0)
    ritual = 'ritual_ZN8QMenuBar15mousePressEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QMenuBar15mousePressEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QMouseEvent)
  @overload(NoneType)
  def mouseMoveEvent(self, a0: Optional[QMouseEvent]) -> None:
    """
    Calls Qt's 'void QMenuBar::mouseMoveEvent(QMouseEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenubar.html#mouseMoveEvent

    Parameters
    ----------

    a0 : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMenuBar::mouseMoveEvent(QMouseEvent *a0)
    ritual = 'ritual_ZN8QMenuBar14mouseMoveEventEP11QMouseEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QMenuBar14mouseMoveEventEP11QMouseEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QEvent)
  @overload(NoneType)
  def leaveEvent(self, a0: Optional[QEvent]) -> None:
    """
    Calls Qt's 'void QMenuBar::leaveEvent(QEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenubar.html#leaveEvent

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMenuBar::leaveEvent(QEvent *a0)
    ritual = 'ritual_ZN8QMenuBar10leaveEventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QMenuBar10leaveEventEP6QEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QPaintEvent)
  @overload(NoneType)
  def paintEvent(self, a0: Optional[QPaintEvent]) -> None:
    """
    Calls Qt's 'void QMenuBar::paintEvent(QPaintEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenubar.html#paintEvent

    Parameters
    ----------

    a0 : Optional[QPaintEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMenuBar::paintEvent(QPaintEvent *a0)
    ritual = 'ritual_ZN8QMenuBar10paintEventEP11QPaintEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QMenuBar10paintEventEP11QPaintEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QResizeEvent)
  @overload(NoneType)
  def resizeEvent(self, a0: Optional[QResizeEvent]) -> None:
    """
    Calls Qt's 'void QMenuBar::resizeEvent(QResizeEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenubar.html#resizeEvent

    Parameters
    ----------

    a0 : Optional[QResizeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMenuBar::resizeEvent(QResizeEvent *a0)
    ritual = 'ritual_ZN8QMenuBar11resizeEventEP12QResizeEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QMenuBar11resizeEventEP12QResizeEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QActionEvent)
  @overload(NoneType)
  def actionEvent(self, a0: Optional[QActionEvent]) -> None:
    """
    Calls Qt's 'void QMenuBar::actionEvent(QActionEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenubar.html#actionEvent

    Parameters
    ----------

    a0 : Optional[QActionEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMenuBar::actionEvent(QActionEvent *a0)
    ritual = 'ritual_ZN8QMenuBar11actionEventEP12QActionEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QMenuBar11actionEventEP12QActionEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusOutEvent(self, a0: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QMenuBar::focusOutEvent(QFocusEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenubar.html#focusOutEvent

    Parameters
    ----------

    a0 : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMenuBar::focusOutEvent(QFocusEvent *a0)
    ritual = 'ritual_ZN8QMenuBar13focusOutEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QMenuBar13focusOutEventEP11QFocusEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QFocusEvent)
  @overload(NoneType)
  def focusInEvent(self, a0: Optional[QFocusEvent]) -> None:
    """
    Calls Qt's 'void QMenuBar::focusInEvent(QFocusEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenubar.html#focusInEvent

    Parameters
    ----------

    a0 : Optional[QFocusEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMenuBar::focusInEvent(QFocusEvent *a0)
    ritual = 'ritual_ZN8QMenuBar12focusInEventEP11QFocusEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QMenuBar12focusInEventEP11QFocusEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, a0: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QMenuBar::timerEvent(QTimerEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenubar.html#timerEvent

    Parameters
    ----------

    a0 : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMenuBar::timerEvent(QTimerEvent *a0)
    ritual = 'ritual_ZN8QMenuBar10timerEventEP11QTimerEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QMenuBar10timerEventEP11QTimerEvent'
    self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def eventFilter(self, a0: Optional[QObject], a1: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QMenuBar::eventFilter(QObject *a0, QEvent *a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenubar.html#eventFilter

    Parameters
    ----------

    a0 : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    a1 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QMenuBar::eventFilter(QObject *a0, QEvent *a1)
    ritual = 'ritual_ZN8QMenuBar11eventFilterEP7QObjectP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QMenuBar11eventFilterEP7QObjectP6QEvent'
    return self.uglySide.call(
        ritual, self._addressOf(a0), self._addressOf(a1),
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, a0: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QMenuBar::event(QEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qmenubar.html#event

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QMenuBar::event(QEvent *a0)
    ritual = 'ritual_ZN8QMenuBar5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN8QMenuBar5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(a0))

  @overload(QStyleOptionMenuItem, QAction)
  @overload(QStyleOptionMenuItem, NoneType)
  @overload(NoneType, QAction)
  @overload(NoneType, NoneType)
  def initStyleOption(
      self,
      option: Optional[QStyleOptionMenuItem],
      action: Optional[QAction],
  ) -> None:
    """
    Calls Qt's 'void QMenuBar::initStyleOption(QStyleOptionMenuItem *option,
    const QAction *action) const'.

    Qt's own words: https://doc.qt.io/qt-6/qmenubar.html#initStyleOption

    Parameters
    ----------

    option : Optional[QStyleOptionMenuItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    action : Optional[QAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QMenuBar::initStyleOption(QStyleOptionMenuItem *option, const
    #      QAction *action) const
    ritual = (
        'ritual_ZNK8QMenuBar15initStyleOptionEP20QStyleOptionMenuItemPK7QAc'
        'tion')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK8QMenuBar15initStyleOptionEP20QStyleOptionMenuItem'
          'PK7QAction')
    self.uglySide.call(
        ritual, self._addressOf(option), self._addressOf(action),
    )
