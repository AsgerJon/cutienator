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
from ..QtCore import Qt
from . import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPoint, QRect, QSize
  from ..QtGui import QAction, QIcon
  from . import QMenu
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAction = WAIT['QAction']
  QIcon = WAIT['QIcon']
  QMenu = WAIT['QMenu']
  QPoint = WAIT['QPoint']

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
  so far, 21 names in all: 'metaObject', 'tr', 'addMenu', 'addSeparator',
  'insertSeparator', 'insertMenu', 'clear', 'activeAction',
  'setActiveAction', 'setDefaultUp', 'isDefaultUp', 'sizeHint',
  'minimumSizeHint', 'heightForWidth', 'actionGeometry', 'actionAt',
  'setCornerWidget', 'cornerWidget', 'isNativeMenuBar', 'setNativeMenuBar',
  'setVisible'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QMenuBar::~QMenuBar()': the destructor: Python never removes a C++
    QMenuBar.

  What has no ritual
  ------------------

  26 of the 51 functions Qt declares: 15 protected; 3 takes or gives a type
  that cannot be passed yet; 3 private; 2 a signal; 2 forbidden; 1 a
  template.

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
    address = self.uglySide.call('ritual_ZNK8QMenuBar8sizeHintEv')
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
    address = self.uglySide.call('ritual_ZNK8QMenuBar15minimumSizeHintEv')
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
    return self.uglySide.call('ritual_ZNK8QMenuBar14heightForWidthEi', a0)

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
    self.uglySide.call('ritual_ZN8QMenuBar10setVisibleEb', visible)

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
