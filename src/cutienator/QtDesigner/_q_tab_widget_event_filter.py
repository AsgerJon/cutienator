"""
QTabWidgetEventFilter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_tabwidget_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QTabWidgetEventFilter to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject
  from ..QtWidgets import QMenu, QTabBar, QTabWidget
  from . import QDesignerFormWindowInterface
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QMenu = WAIT['QMenu']
  QTabWidget = WAIT['QTabWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTabWidgetEventFilter(QObject):
  """
  The cute side of Qt's QTabWidgetEventFilter: a plain Python object standing
  in front of one C++ QTabWidgetEventFilter.

  It is built on the cute 'QObject', as Qt's QTabWidgetEventFilter is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTabWidgetEventFilter that has a ritual and that
  Python can call so far, 12 names in all: 'metaObject', 'tr', 'install',
  'eventFilterOf', 'addTabWidgetContextMenuActions', 'addContextMenuActions',
  'eventFilter', 'formWindow', 'removeCurrentPage', 'addPage',
  'addPageAfter', 'tabBar'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QTabWidgetEventFilter::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QTabWidgetEventFilter::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QTabWidgetEventFilter::~QTabWidgetEventFilter()': the destructor:
    Python never removes a C++ QTabWidgetEventFilter.
  - Qt's 'int QTabWidgetEventFilter::pageFromPosition(const QPoint &pos,
    QRect &rect) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 19 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QTabWidgetEventFilter is created at the first use, not by
    'QTabWidgetEventFilter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTabWidgetEventFilter.
  - Qt tells when it has removed the C++ QTabWidgetEventFilter. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QTabWidgetEventFilter that has no cute function yet,
    'pageFromPosition', holds a function that raises 'NotImplementedError',
    and its docstring says why.
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
    Calls Qt's 'QString QTabWidgetEventFilter::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidgeteventfilter.html#tr

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
    #  QString QTabWidgetEventFilter::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QTabWidgetEventFilter2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QTabWidget)
  @overload(NoneType)
  def install(tabWidget: Optional[QTabWidget]) -> None:
    """
    Calls Qt's 'void QTabWidgetEventFilter::install(QTabWidget *tabWidget)'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidgeteventfilter.html#install

    Parameters
    ----------

    tabWidget : Optional[QTabWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTabWidgetEventFilter::install(QTabWidget *tabWidget)
    Rituals.call(
        'ritual_ZN21QTabWidgetEventFilter7installEP10QTabWidget',
        CuteMixin._addressOf(tabWidget),
    )

  @staticmethod
  @overload(QTabWidget)
  @overload(NoneType)
  def eventFilterOf(
      tabWidget: Optional[QTabWidget],
  ) -> Optional[QTabWidgetEventFilter]:
    """
    Calls Qt's 'QTabWidgetEventFilter
    *QTabWidgetEventFilter::eventFilterOf(const QTabWidget *tabWidget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtabwidgeteventfilter.html#eventFilterOf

    Parameters
    ----------

    tabWidget : Optional[QTabWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QTabWidgetEventFilter]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTabWidgetEventFilter *QTabWidgetEventFilter::eventFilterOf(const
    #      QTabWidget *tabWidget)
    address = Rituals.call(
        'ritual_ZN21QTabWidgetEventFilter13eventFilterOfEPK10QTabWidget',
        CuteMixin._addressOf(tabWidget),
    )
    return QTabWidgetEventFilter._cuteAt(address)

  @staticmethod
  @overload(QTabWidget, QMenu)
  @overload(QTabWidget, NoneType)
  @overload(NoneType, QMenu)
  @overload(NoneType, NoneType)
  def addTabWidgetContextMenuActions(
      tabWidget: Optional[QTabWidget],
      popup: Optional[QMenu],
  ) -> Optional[QMenu]:
    """
    Calls Qt's 'QMenu
    *QTabWidgetEventFilter::addTabWidgetContextMenuActions(const QTabWidget
    *tabWidget, QMenu *popup)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtabwidgeteventfilter.html

    Parameters
    ----------

    tabWidget : Optional[QTabWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    popup : Optional[QMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMenu *QTabWidgetEventFilter::addTabWidgetContextMenuActions(const
    #      QTabWidget *tabWidget, QMenu *popup)
    address = Rituals.call(
        'ritual_ZN21QTabWidgetEventFilter30addTabWidgetContextMenuActionsEP'
        'K10QTabWidgetP5QMenu',
        CuteMixin._addressOf(tabWidget), CuteMixin._addressOf(popup),
    )
    from ..QtWidgets import QMenu
    return QMenu._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTabWidgetEventFilter'

  #  A C++ QTabWidgetEventFilter Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTabWidgetEventFilter'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QTabWidgetEventFilter::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtabwidgeteventfilter.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QTabWidgetEventFilter::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QTabWidgetEventFilter10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def formWindow(self) -> Optional[QDesignerFormWindowInterface]:
    """
    Calls Qt's 'QDesignerFormWindowInterface
    *QTabWidgetEventFilter::formWindow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtabwidgeteventfilter.html#formWindow

    Returns
    -------

    Optional[QDesignerFormWindowInterface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDesignerFormWindowInterface *QTabWidgetEventFilter::formWindow()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK21QTabWidgetEventFilter10formWindowEv',
    )
    from . import QDesignerFormWindowInterface
    return QDesignerFormWindowInterface._cuteAt(address)

  def tabBar(self) -> Optional[QTabBar]:
    """
    Calls Qt's 'QTabBar *QTabWidgetEventFilter::tabBar() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidgeteventfilter.html#tabBar

    Returns
    -------

    Optional[QTabBar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTabBar *QTabWidgetEventFilter::tabBar() const
    address = self.uglySide.call(
        'ritual_ZNK21QTabWidgetEventFilter6tabBarEv',
    )
    from ..QtWidgets import QTabBar
    return QTabBar._cuteAt(address)

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

  @overload(QTabWidget)
  @overload(NoneType)
  def __init__(self, parent: Optional[QTabWidget]) -> None:
    """
    Notes what was given, for Qt's
    'QTabWidgetEventFilter::QTabWidgetEventFilter(QTabWidget *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtabwidgeteventfilter.html#QTabWidgetEventFilter

    Parameters
    ----------

    parent : Optional[QTabWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QTabWidgetEventFilter::QTabWidgetEventFilter(QTabWidget *parent)
    self._noteCreation(QTabWidgetEventFilter, lambda: Rituals.call(
        'ritual_ZN21QTabWidgetEventFilterC1EP10QTabWidget',
        self._addressOf(parent),
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
  def addContextMenuActions(self, popup: Optional[QMenu]) -> Optional[QMenu]:
    """
    Calls Qt's 'QMenu *QTabWidgetEventFilter::addContextMenuActions(QMenu
    *popup)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtabwidgeteventfilter.html#addContextMenuActions

    Parameters
    ----------

    popup : Optional[QMenu]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMenu *QTabWidgetEventFilter::addContextMenuActions(QMenu *popup)
    address = self.uglySide.call(
        'ritual_ZN21QTabWidgetEventFilter21addContextMenuActionsEP5QMenu',
        self._addressOf(popup),
    )
    from ..QtWidgets import QMenu
    return QMenu._cuteAt(address)

  @overload(QObject, QEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QEvent)
  @overload(NoneType, NoneType)
  def eventFilter(self, o: Optional[QObject], e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QTabWidgetEventFilter::eventFilter(QObject *o, QEvent
    *e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtabwidgeteventfilter.html#eventFilter

    Parameters
    ----------

    o : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QTabWidgetEventFilter::eventFilter(QObject *o, QEvent *e)
    ritual = (
        'ritual_ZN21QTabWidgetEventFilter11eventFilterEP7QObjectP6QEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QTabWidgetEventFilter11eventFilterEP7QObjectP6QEv'
          'ent')
    return self.uglySide.call(
        ritual, self._addressOf(o, 'QObject'), self._addressOf(e),
    )

  def removeCurrentPage(self) -> None:
    """
    Calls Qt's 'void QTabWidgetEventFilter::removeCurrentPage()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtabwidgeteventfilter.html#removeCurrentPage
    """
    #  void QTabWidgetEventFilter::removeCurrentPage()
    self.uglySide.call(
        'ritual_ZN21QTabWidgetEventFilter17removeCurrentPageEv',
    )

  def addPage(self) -> None:
    """
    Calls Qt's 'void QTabWidgetEventFilter::addPage()'.

    Qt's own words: https://doc.qt.io/qt-6/qtabwidgeteventfilter.html#addPage
    """
    #  void QTabWidgetEventFilter::addPage()
    self.uglySide.call('ritual_ZN21QTabWidgetEventFilter7addPageEv')

  def addPageAfter(self) -> None:
    """
    Calls Qt's 'void QTabWidgetEventFilter::addPageAfter()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtabwidgeteventfilter.html#addPageAfter
    """
    #  void QTabWidgetEventFilter::addPageAfter()
    self.uglySide.call('ritual_ZN21QTabWidgetEventFilter12addPageAfterEv')

  @staticmethod
  def pageFromPosition(*__, **_) -> Never:
    """
    Qt's 'int QTabWidgetEventFilter::pageFromPosition(const QPoint &pos,
    QRect &rect) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QTabWidgetEventFilter.pageFromPosition' has no cute function yet. "
        "Qt's 'int QTabWidgetEventFilter::pageFromPosition(const QPoint "
        "&pos, QRect &rect) const': takes a type Python has no way to hand "
        "over yet.")
