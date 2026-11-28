"""
QQuickMenu binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickmenu_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQuickMenu to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtGui import QAccessible
from ..QtQuick import QQuickItem
from . import QQuickPopup

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPointF, QTimerEvent, QVariant
  from ..QtGui import QFont, QKeyEvent
  from ..QtQml import QQmlComponent
  from . import QQuickAction, QQuickIcon, QQuickMenuPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QKeyEvent = WAIT['QKeyEvent']
  QPointF = WAIT['QPointF']
  QQmlComponent = WAIT['QQmlComponent']
  QQuickAction = WAIT['QQuickAction']
  QQuickIcon = WAIT['QQuickIcon']
  QTimerEvent = WAIT['QTimerEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickMenu(QQuickPopup):
  """
  The cute side of Qt's QQuickMenu: a plain Python object standing in front
  of one C++ QQuickMenu.

  It is built on the cute 'QQuickPopup', as Qt's QQuickMenu is built on Qt's
  QQuickPopup, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickMenu that has a ritual and that Python can
  call so far, 55 names in all: 'metaObject', 'tr', 'itemAt', 'addItem',
  'insertItem', 'moveItem', 'removeItem', 'contentModel', 'title',
  'setTitle', 'icon', 'setIcon', 'separatorsCollapsible',
  'setSeparatorsCollapsible', 'cascade', 'setCascade', 'resetCascade',
  'overlap', 'setOverlap', 'delegate', 'setDelegate', 'currentIndex',
  'setCurrentIndex', 'count', 'takeItem', 'menuAt', 'addMenu', 'insertMenu',
  'removeMenu', 'takeMenu', 'actionAt', 'addAction', 'insertAction',
  'removeAction', 'takeAction', 'isVisible', 'setVisible', 'popup',
  'dismiss', 'componentComplete', 'contentItemChange', 'itemChange',
  'keyPressEvent', 'titleChanged', 'countChanged', 'cascadeChanged',
  'overlapChanged', 'delegateChanged', 'currentIndexChanged', 'iconChanged',
  'separatorsCollapsibleChanged', 'timerEvent', 'defaultFont',
  'accessibleRole', 'd_func'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickMenu::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickMenu::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickMenu::~QQuickMenu()': the destructor: Python never removes a
    C++ QQuickMenu.
  - Qt's 'QQmlListProperty<QObject> QQuickMenu::contentData()': gives a type
    Python has no way to take yet.
  - Qt's 'const QQuickMenuPrivate *QQuickMenu::d_func() const': takes in
    Python what 'QQuickMenuPrivate *QQuickMenu::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 70 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickMenu is created at the first use, not by 'QQuickMenu(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickMenu.
  - Qt tells when it has removed the C++ QQuickMenu. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QQuickMenu that has no cute function yet,
    'contentData', holds a function that raises 'NotImplementedError', and
    its docstring says why.
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
    Calls Qt's 'QString QQuickMenu::tr(const char *s, const char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#tr

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
    #  QString QQuickMenu::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN10QQuickMenu2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickMenu'

  #  A C++ QQuickMenu Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickMenu'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickMenu::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickMenu::metaObject() const
    address = self.uglySide.call('ritual_ZNK10QQuickMenu10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(int)
  def itemAt(self, index: int) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickMenu::itemAt(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#itemAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickMenu::itemAt(int index) const
    address = self.uglySide.call('ritual_ZNK10QQuickMenu6itemAtEi', index)
    return QQuickItem._cuteAt(address)

  def contentModel(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQuickMenu::contentModel() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#contentModel

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQuickMenu::contentModel() const
    address = self.uglySide.call('ritual_ZNK10QQuickMenu12contentModelEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def title(self) -> str:
    """
    Calls Qt's 'QString QQuickMenu::title() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#title

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQuickMenu::title() const
    return self.uglySide.call('ritual_ZNK10QQuickMenu5titleEv')

  def icon(self) -> QQuickIcon:
    """
    Calls Qt's 'QQuickIcon QQuickMenu::icon() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#icon

    Returns
    -------

    QQuickIcon
      A new cute QQuickIcon around the copy Qt gave back. Python owns it.
    """
    #  QQuickIcon QQuickMenu::icon() const
    address = self.uglySide.call('ritual_ZNK10QQuickMenu4iconEv')
    from . import QQuickIcon
    return QQuickIcon._cuteOwning(address)

  def separatorsCollapsible(self) -> bool:
    """
    Calls Qt's 'bool QQuickMenu::separatorsCollapsible() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenu.html#separatorsCollapsible
    """
    #  bool QQuickMenu::separatorsCollapsible() const
    return self.uglySide.call(
        'ritual_ZNK10QQuickMenu21separatorsCollapsibleEv',
    )

  def cascade(self) -> bool:
    """
    Calls Qt's 'bool QQuickMenu::cascade() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#cascade
    """
    #  bool QQuickMenu::cascade() const
    return self.uglySide.call('ritual_ZNK10QQuickMenu7cascadeEv')

  def overlap(self) -> float:
    """
    Calls Qt's 'qreal QQuickMenu::overlap() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#overlap
    """
    #  qreal QQuickMenu::overlap() const
    return self.uglySide.call('ritual_ZNK10QQuickMenu7overlapEv')

  def delegate(self) -> Optional[QQmlComponent]:
    """
    Calls Qt's 'QQmlComponent *QQuickMenu::delegate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#delegate

    Returns
    -------

    Optional[QQmlComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlComponent *QQuickMenu::delegate() const
    address = self.uglySide.call('ritual_ZNK10QQuickMenu8delegateEv')
    from ..QtQml import QQmlComponent
    return QQmlComponent._cuteAt(address)

  def currentIndex(self) -> int:
    """
    Calls Qt's 'int QQuickMenu::currentIndex() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#currentIndex
    """
    #  int QQuickMenu::currentIndex() const
    return self.uglySide.call('ritual_ZNK10QQuickMenu12currentIndexEv')

  def count(self) -> int:
    """
    Calls Qt's 'int QQuickMenu::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#count
    """
    #  int QQuickMenu::count() const
    return self.uglySide.call('ritual_ZNK10QQuickMenu5countEv')

  @overload(int)
  def menuAt(self, index: int) -> Optional[QQuickMenu]:
    """
    Calls Qt's 'QQuickMenu *QQuickMenu::menuAt(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#menuAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QQuickMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickMenu *QQuickMenu::menuAt(int index) const
    address = self.uglySide.call('ritual_ZNK10QQuickMenu6menuAtEi', index)
    return QQuickMenu._cuteAt(address)

  @overload(int)
  def actionAt(self, index: int) -> Optional[QQuickAction]:
    """
    Calls Qt's 'QQuickAction *QQuickMenu::actionAt(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#actionAt

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QQuickAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAction *QQuickMenu::actionAt(int index) const
    address = self.uglySide.call('ritual_ZNK10QQuickMenu8actionAtEi', index)
    from . import QQuickAction
    return QQuickAction._cuteAt(address)

  def isVisible(self) -> bool:
    """
    Calls Qt's 'bool QQuickMenu::isVisible() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#isVisible
    """
    #  bool QQuickMenu::isVisible() const
    ritual = 'ritual_ZNK10QQuickMenu9isVisibleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QQuickMenu9isVisibleEv'
    return self.uglySide.call(ritual)

  def defaultFont(self) -> QFont:
    """
    Calls Qt's 'QFont QQuickMenu::defaultFont() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#defaultFont

    Returns
    -------

    QFont
      A new cute QFont around the copy Qt gave back. Python owns it.
    """
    #  QFont QQuickMenu::defaultFont() const
    ritual = 'ritual_ZNK10QQuickMenu11defaultFontEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QQuickMenu11defaultFontEv'
    address = self.uglySide.call(ritual)
    from ..QtGui import QFont
    return QFont._cuteOwning(address)

  def accessibleRole(self) -> QAccessible.Role:
    """
    Calls Qt's 'QAccessible::Role QQuickMenu::accessibleRole() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#accessibleRole

    Returns
    -------

    QAccessible.Role
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QAccessible.Role(number)'
      gives.
    """
    #  QAccessible::Role QQuickMenu::accessibleRole() const
    ritual = 'ritual_ZNK10QQuickMenu14accessibleRoleEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10QQuickMenu14accessibleRoleEv'
    return QAccessible.Role(self.uglySide.call(ritual))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setTitle(self, title: str) -> None:
    """
    Calls Qt's 'void QQuickMenu::setTitle(const QString &title)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#setTitle

    Parameters
    ----------

    title : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickMenu::setTitle(const QString &title)
    self.uglySide.call('ritual_ZN10QQuickMenu8setTitleERK7QString', title)

  @overload(QQuickIcon)
  def setIcon(self, icon: QQuickIcon) -> None:
    """
    Calls Qt's 'void QQuickMenu::setIcon(const QQuickIcon &icon)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#setIcon

    Parameters
    ----------

    icon : QQuickIcon
      Passed on as a value: Qt reads the C++ QQuickIcon, which stays Python's
      own.
    """
    #  void QQuickMenu::setIcon(const QQuickIcon &icon)
    self.uglySide.call(
        'ritual_ZN10QQuickMenu7setIconERK10QQuickIcon', self._valueOf(icon),
    )

  @overload(bool)
  def setSeparatorsCollapsible(self, collapsible: bool) -> None:
    """
    Calls Qt's 'void QQuickMenu::setSeparatorsCollapsible(bool collapsible)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenu.html#setSeparatorsCollapsible

    Parameters
    ----------

    collapsible : bool
      Passed on as it is.
    """
    #  void QQuickMenu::setSeparatorsCollapsible(bool collapsible)
    self.uglySide.call(
        'ritual_ZN10QQuickMenu24setSeparatorsCollapsibleEb', collapsible,
    )

  @overload(bool)
  def setCascade(self, cascade: bool) -> None:
    """
    Calls Qt's 'void QQuickMenu::setCascade(bool cascade)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#setCascade

    Parameters
    ----------

    cascade : bool
      Passed on as it is.
    """
    #  void QQuickMenu::setCascade(bool cascade)
    self.uglySide.call('ritual_ZN10QQuickMenu10setCascadeEb', cascade)

  @overload(float)
  def setOverlap(self, overlap: float) -> None:
    """
    Calls Qt's 'void QQuickMenu::setOverlap(qreal overlap)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#setOverlap

    Parameters
    ----------

    overlap : float
      Passed on as it is.
    """
    #  void QQuickMenu::setOverlap(qreal overlap)
    self.uglySide.call('ritual_ZN10QQuickMenu10setOverlapEd', overlap)

  @overload(QQmlComponent)
  @overload(NoneType)
  def setDelegate(self, delegate: Optional[QQmlComponent]) -> None:
    """
    Calls Qt's 'void QQuickMenu::setDelegate(QQmlComponent *delegate)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#setDelegate

    Parameters
    ----------

    delegate : Optional[QQmlComponent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMenu::setDelegate(QQmlComponent *delegate)
    self.uglySide.call(
        'ritual_ZN10QQuickMenu11setDelegateEP13QQmlComponent',
        self._addressOf(delegate),
    )

  @overload(int)
  def setCurrentIndex(self, index: int) -> None:
    """
    Calls Qt's 'void QQuickMenu::setCurrentIndex(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#setCurrentIndex

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QQuickMenu::setCurrentIndex(int index)
    self.uglySide.call('ritual_ZN10QQuickMenu15setCurrentIndexEi', index)

  @overload(bool)
  def setVisible(self, visible: bool) -> None:
    """
    Calls Qt's 'void QQuickMenu::setVisible(bool visible)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#setVisible

    Parameters
    ----------

    visible : bool
      Passed on as it is.
    """
    #  void QQuickMenu::setVisible(bool visible)
    ritual = 'ritual_ZN10QQuickMenu10setVisibleEb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickMenu10setVisibleEb'
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QQuickMenu::QQuickMenu(QObject *parent)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#QQuickMenu

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickMenu::QQuickMenu(QObject *parent)
    self._noteCreation(QQuickMenu, lambda: Rituals.call(
        'ritual_ZN10QQuickMenuC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  @overload(QQuickItem)
  @overload(NoneType)
  def addItem(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickMenu::addItem(QQuickItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#addItem

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMenu::addItem(QQuickItem *item)
    self.uglySide.call(
        'ritual_ZN10QQuickMenu7addItemEP10QQuickItem', self._addressOf(item),
    )

  @overload(int, QQuickItem)
  @overload(int, NoneType)
  def insertItem(self, index: int, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickMenu::insertItem(int index, QQuickItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#insertItem

    Parameters
    ----------

    index : int
      Passed on as it is.

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMenu::insertItem(int index, QQuickItem *item)
    self.uglySide.call(
        'ritual_ZN10QQuickMenu10insertItemEiP10QQuickItem',
        index, self._addressOf(item),
    )

  @overload(int, int)
  def moveItem(self, from_: int, to: int) -> None:
    """
    Calls Qt's 'void QQuickMenu::moveItem(int from, int to)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#moveItem

    Parameters
    ----------

    from_ : int
      Passed on as it is.

    to : int
      Passed on as it is.
    """
    #  void QQuickMenu::moveItem(int from, int to)
    self.uglySide.call('ritual_ZN10QQuickMenu8moveItemEii', from_, to)

  @overload(QQuickItem)
  @overload(NoneType)
  def removeItem(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QQuickMenu::removeItem(QQuickItem *item)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#removeItem

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMenu::removeItem(QQuickItem *item)
    self.uglySide.call(
        'ritual_ZN10QQuickMenu10removeItemEP10QQuickItem',
        self._addressOf(item),
    )

  def resetCascade(self) -> None:
    """
    Calls Qt's 'void QQuickMenu::resetCascade()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#resetCascade
    """
    #  void QQuickMenu::resetCascade()
    self.uglySide.call('ritual_ZN10QQuickMenu12resetCascadeEv')

  @overload(int)
  def takeItem(self, index: int) -> Optional[QQuickItem]:
    """
    Calls Qt's 'QQuickItem *QQuickMenu::takeItem(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#takeItem

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QQuickItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickItem *QQuickMenu::takeItem(int index)
    address = self.uglySide.call('ritual_ZN10QQuickMenu8takeItemEi', index)
    return QQuickItem._cuteAt(address)

  @overload(THIS)
  @overload(NoneType)
  def addMenu(self, menu: Optional[QQuickMenu]) -> None:
    """
    Calls Qt's 'void QQuickMenu::addMenu(QQuickMenu *menu)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#addMenu

    Parameters
    ----------

    menu : Optional[QQuickMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMenu::addMenu(QQuickMenu *menu)
    self.uglySide.call(
        'ritual_ZN10QQuickMenu7addMenuEPS_', self._addressOf(menu),
    )

  @overload(int, THIS)
  @overload(int, NoneType)
  def insertMenu(self, index: int, menu: Optional[QQuickMenu]) -> None:
    """
    Calls Qt's 'void QQuickMenu::insertMenu(int index, QQuickMenu *menu)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#insertMenu

    Parameters
    ----------

    index : int
      Passed on as it is.

    menu : Optional[QQuickMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMenu::insertMenu(int index, QQuickMenu *menu)
    self.uglySide.call(
        'ritual_ZN10QQuickMenu10insertMenuEiPS_',
        index, self._addressOf(menu),
    )

  @overload(THIS)
  @overload(NoneType)
  def removeMenu(self, menu: Optional[QQuickMenu]) -> None:
    """
    Calls Qt's 'void QQuickMenu::removeMenu(QQuickMenu *menu)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#removeMenu

    Parameters
    ----------

    menu : Optional[QQuickMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMenu::removeMenu(QQuickMenu *menu)
    self.uglySide.call(
        'ritual_ZN10QQuickMenu10removeMenuEPS_', self._addressOf(menu),
    )

  @overload(int)
  def takeMenu(self, index: int) -> Optional[QQuickMenu]:
    """
    Calls Qt's 'QQuickMenu *QQuickMenu::takeMenu(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#takeMenu

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QQuickMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickMenu *QQuickMenu::takeMenu(int index)
    address = self.uglySide.call('ritual_ZN10QQuickMenu8takeMenuEi', index)
    return QQuickMenu._cuteAt(address)

  @overload(QQuickAction)
  @overload(NoneType)
  def addAction(self, action: Optional[QQuickAction]) -> None:
    """
    Calls Qt's 'void QQuickMenu::addAction(QQuickAction *action)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#addAction

    Parameters
    ----------

    action : Optional[QQuickAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMenu::addAction(QQuickAction *action)
    self.uglySide.call(
        'ritual_ZN10QQuickMenu9addActionEP12QQuickAction',
        self._addressOf(action),
    )

  @overload(int, QQuickAction)
  @overload(int, NoneType)
  def insertAction(self, index: int, action: Optional[QQuickAction]) -> None:
    """
    Calls Qt's 'void QQuickMenu::insertAction(int index, QQuickAction
    *action)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#insertAction

    Parameters
    ----------

    index : int
      Passed on as it is.

    action : Optional[QQuickAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMenu::insertAction(int index, QQuickAction *action)
    self.uglySide.call(
        'ritual_ZN10QQuickMenu12insertActionEiP12QQuickAction',
        index, self._addressOf(action),
    )

  @overload(QQuickAction)
  @overload(NoneType)
  def removeAction(self, action: Optional[QQuickAction]) -> None:
    """
    Calls Qt's 'void QQuickMenu::removeAction(QQuickAction *action)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#removeAction

    Parameters
    ----------

    action : Optional[QQuickAction]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMenu::removeAction(QQuickAction *action)
    self.uglySide.call(
        'ritual_ZN10QQuickMenu12removeActionEP12QQuickAction',
        self._addressOf(action),
    )

  @overload(int)
  def takeAction(self, index: int) -> Optional[QQuickAction]:
    """
    Calls Qt's 'QQuickAction *QQuickMenu::takeAction(int index)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#takeAction

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QQuickAction]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickAction *QQuickMenu::takeAction(int index)
    address = self.uglySide.call(
        'ritual_ZN10QQuickMenu10takeActionEi', index,
    )
    from . import QQuickAction
    return QQuickAction._cuteAt(address)

  @overload(QQuickItem, float, float)
  @overload(NoneType, float, float)
  @overload(QQuickItem, float, float, QQuickItem)
  @overload(QQuickItem, float, float, NoneType)
  @overload(NoneType, float, float, QQuickItem)
  @overload(NoneType, float, float, NoneType)
  def popup(
      self,
      parent: Optional[QQuickItem],
      x: float,
      y: float,
      menuItem: Optional[QQuickItem] = None,
  ) -> None:
    """
    Calls Qt's 'void QQuickMenu::popup(QQuickItem *parent, qreal x, qreal y,
    QQuickItem *menuItem)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#popup

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    menuItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QQuickMenu::popup(QQuickItem *parent, qreal x, qreal y,
    #      QQuickItem *menuItem)
    self.uglySide.call(
        'ritual_ZN10QQuickMenu5popupEP10QQuickItemddS1_',
        self._addressOf(parent), x, y, self._addressOf(menuItem),
    )

  @overload(QQuickItem, QPointF)
  @overload(NoneType, QPointF)
  @overload(QQuickItem, QPointF, QQuickItem)
  @overload(QQuickItem, QPointF, NoneType)
  @overload(NoneType, QPointF, QQuickItem)
  @overload(NoneType, QPointF, NoneType)
  def popup(
      self,
      parent: Optional[QQuickItem],
      position: QPointF,
      menuItem: Optional[QQuickItem] = None,
  ) -> None:
    """
    Calls Qt's 'void QQuickMenu::popup(QQuickItem *parent, const QPointF
    &position, QQuickItem *menuItem)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#popup

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    menuItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QQuickMenu::popup(QQuickItem *parent, const QPointF &position,
    #      QQuickItem *menuItem)
    self.uglySide.call(
        'ritual_ZN10QQuickMenu5popupEP10QQuickItemRK7QPointFS1_',
        self._addressOf(parent), self._valueOf(position, 'QPointF'),
        self._addressOf(menuItem),
    )

  @overload(QQuickItem, QQuickItem)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QQuickItem)
  @overload(NoneType, NoneType)
  def popup(
      self,
      parent: Optional[QQuickItem],
      menuItem: Optional[QQuickItem],
  ) -> None:
    """
    Calls Qt's 'void QQuickMenu::popup(QQuickItem *parent, QQuickItem
    *menuItem)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#popup

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    menuItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMenu::popup(QQuickItem *parent, QQuickItem *menuItem)
    self.uglySide.call(
        'ritual_ZN10QQuickMenu5popupEP10QQuickItemS1_',
        self._addressOf(parent), self._addressOf(menuItem),
    )

  @overload()
  @overload(QQuickItem)
  @overload(NoneType)
  def popup(self, parent: Optional[QQuickItem] = None) -> None:
    """
    Calls Qt's 'void QQuickMenu::popup(QQuickItem *parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#popup

    Parameters
    ----------

    parent : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QQuickMenu::popup(QQuickItem *parent)
    self.uglySide.call(
        'ritual_ZN10QQuickMenu5popupEP10QQuickItem', self._addressOf(parent),
    )

  @overload(float, float)
  @overload(float, float, QQuickItem)
  @overload(float, float, NoneType)
  def popup(
      self,
      x: float,
      y: float,
      menuItem: Optional[QQuickItem] = None,
  ) -> None:
    """
    Calls Qt's 'void QQuickMenu::popup(qreal x, qreal y, QQuickItem
    *menuItem)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#popup

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    menuItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QQuickMenu::popup(qreal x, qreal y, QQuickItem *menuItem)
    self.uglySide.call(
        'ritual_ZN10QQuickMenu5popupEddP10QQuickItem',
        x, y, self._addressOf(menuItem),
    )

  @overload(QPointF)
  @overload(QPointF, QQuickItem)
  @overload(QPointF, NoneType)
  def popup(
      self,
      position: QPointF,
      menuItem: Optional[QQuickItem] = None,
  ) -> None:
    """
    Calls Qt's 'void QQuickMenu::popup(const QPointF &position, QQuickItem
    *menuItem)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#popup

    Parameters
    ----------

    position : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    menuItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  void QQuickMenu::popup(const QPointF &position, QQuickItem *menuItem)
    self.uglySide.call(
        'ritual_ZN10QQuickMenu5popupERK7QPointFP10QQuickItem',
        self._valueOf(position, 'QPointF'), self._addressOf(menuItem),
    )

  def dismiss(self) -> None:
    """
    Calls Qt's 'void QQuickMenu::dismiss()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#dismiss
    """
    #  void QQuickMenu::dismiss()
    self.uglySide.call('ritual_ZN10QQuickMenu7dismissEv')

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQuickMenu::componentComplete()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#componentComplete
    """
    #  void QQuickMenu::componentComplete()
    ritual = 'ritual_ZN10QQuickMenu17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickMenu17componentCompleteEv'
    self.uglySide.call(ritual)

  @overload(QQuickItem, QQuickItem)
  @overload(QQuickItem, NoneType)
  @overload(NoneType, QQuickItem)
  @overload(NoneType, NoneType)
  def contentItemChange(
      self,
      newItem: Optional[QQuickItem],
      oldItem: Optional[QQuickItem],
  ) -> None:
    """
    Calls Qt's 'void QQuickMenu::contentItemChange(QQuickItem *newItem,
    QQuickItem *oldItem)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#contentItemChange

    Parameters
    ----------

    newItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    oldItem : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMenu::contentItemChange(QQuickItem *newItem, QQuickItem
    #      *oldItem)
    ritual = 'ritual_ZN10QQuickMenu17contentItemChangeEP10QQuickItemS1_'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QQuickMenu17contentItemChangeEP10QQuickItemS1_')
    self.uglySide.call(
        ritual, self._addressOf(newItem), self._addressOf(oldItem),
    )

  @overload(QQuickItem.ItemChange, QQuickItem.ItemChangeData)
  def itemChange(
      self,
      change: QQuickItem.ItemChange,
      data: QQuickItem.ItemChangeData,
  ) -> None:
    """
    Calls Qt's 'void QQuickMenu::itemChange(QQuickItem::ItemChange change,
    const QQuickItem::ItemChangeData &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#itemChange

    Parameters
    ----------

    change : QQuickItem.ItemChange
      Passed on as its number.

    data : QQuickItem.ItemChangeData
      Passed on as a value: Qt reads the C++ QQuickItem::ItemChangeData,
      which stays Python's own.
    """
    #  void QQuickMenu::itemChange(QQuickItem::ItemChange change, const
    #      QQuickItem::ItemChangeData &data)
    ritual = (
        'ritual_ZN10QQuickMenu10itemChangeEN10QQuickItem10ItemChangeERKNS0_'
        '14ItemChangeDataE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10QQuickMenu10itemChangeEN10QQuickItem10ItemChangeE'
          'RKNS0_14ItemChangeDataE')
    self.uglySide.call(ritual, change.value, self._valueOf(data))

  @overload(QKeyEvent)
  @overload(NoneType)
  def keyPressEvent(self, event: Optional[QKeyEvent]) -> None:
    """
    Calls Qt's 'void QQuickMenu::keyPressEvent(QKeyEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#keyPressEvent

    Parameters
    ----------

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMenu::keyPressEvent(QKeyEvent *event)
    ritual = 'ritual_ZN10QQuickMenu13keyPressEventEP9QKeyEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickMenu13keyPressEventEP9QKeyEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(str)
  def titleChanged(self, title: str) -> None:
    """
    Calls Qt's 'void QQuickMenu::titleChanged(const QString &title)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#titleChanged

    Parameters
    ----------

    title : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQuickMenu::titleChanged(const QString &title)
    self.uglySide.call(
        'ritual_ZN10QQuickMenu12titleChangedERK7QString', title,
    )

  def countChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMenu::countChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#countChanged
    """
    #  void QQuickMenu::countChanged()
    self.uglySide.call('ritual_ZN10QQuickMenu12countChangedEv')

  @overload(bool)
  def cascadeChanged(self, cascade: bool) -> None:
    """
    Calls Qt's 'void QQuickMenu::cascadeChanged(bool cascade)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#cascadeChanged

    Parameters
    ----------

    cascade : bool
      Passed on as it is.
    """
    #  void QQuickMenu::cascadeChanged(bool cascade)
    self.uglySide.call('ritual_ZN10QQuickMenu14cascadeChangedEb', cascade)

  def overlapChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMenu::overlapChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#overlapChanged
    """
    #  void QQuickMenu::overlapChanged()
    self.uglySide.call('ritual_ZN10QQuickMenu14overlapChangedEv')

  def delegateChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMenu::delegateChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#delegateChanged
    """
    #  void QQuickMenu::delegateChanged()
    self.uglySide.call('ritual_ZN10QQuickMenu15delegateChangedEv')

  def currentIndexChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMenu::currentIndexChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenu.html#currentIndexChanged
    """
    #  void QQuickMenu::currentIndexChanged()
    self.uglySide.call('ritual_ZN10QQuickMenu19currentIndexChangedEv')

  @overload(QQuickIcon)
  def iconChanged(self, icon: QQuickIcon) -> None:
    """
    Calls Qt's 'void QQuickMenu::iconChanged(const QQuickIcon &icon)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#iconChanged

    Parameters
    ----------

    icon : QQuickIcon
      Passed on as a value: Qt reads the C++ QQuickIcon, which stays Python's
      own.
    """
    #  void QQuickMenu::iconChanged(const QQuickIcon &icon)
    self.uglySide.call(
        'ritual_ZN10QQuickMenu11iconChangedERK10QQuickIcon',
        self._valueOf(icon),
    )

  def separatorsCollapsibleChanged(self) -> None:
    """
    Calls Qt's 'void QQuickMenu::separatorsCollapsibleChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickmenu.html#separatorsCollapsibleChanged
    """
    #  void QQuickMenu::separatorsCollapsibleChanged()
    self.uglySide.call(
        'ritual_ZN10QQuickMenu28separatorsCollapsibleChangedEv',
    )

  @overload(QTimerEvent)
  @overload(NoneType)
  def timerEvent(self, event: Optional[QTimerEvent]) -> None:
    """
    Calls Qt's 'void QQuickMenu::timerEvent(QTimerEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#timerEvent

    Parameters
    ----------

    event : Optional[QTimerEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickMenu::timerEvent(QTimerEvent *event)
    ritual = 'ritual_ZN10QQuickMenu10timerEventEP11QTimerEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10QQuickMenu10timerEventEP11QTimerEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  def d_func(self) -> Optional[QQuickMenuPrivate]:
    """
    Calls Qt's 'QQuickMenuPrivate *QQuickMenu::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickmenu.html#d_func

    Returns
    -------

    Optional[QQuickMenuPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickMenuPrivate *QQuickMenu::d_func()
    address = self.uglySide.call('ritual_ZN10QQuickMenu6d_funcEv')
    from . import QQuickMenuPrivate
    return QQuickMenuPrivate._cuteAt(address)

  @staticmethod
  def contentData(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QObject> QQuickMenu::contentData()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickMenu.contentData' has no cute function yet. Qt's "
        "'QQmlListProperty<QObject> QQuickMenu::contentData()': gives a "
        "type Python has no way to take yet.")
