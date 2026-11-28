"""
QStackedWidgetEventFilter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_stackedbox_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QStackedWidgetEventFilter to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from . import QStackedWidgetPreviewEventFilter

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from ..QtWidgets import QMenu, QStackedWidget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMenu = WAIT['QMenu']
  QStackedWidget = WAIT['QStackedWidget']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QStackedWidgetEventFilter(QStackedWidgetPreviewEventFilter):
  """
  The cute side of Qt's QStackedWidgetEventFilter: a plain Python object
  standing in front of one C++ QStackedWidgetEventFilter.

  It is built on the cute 'QStackedWidgetPreviewEventFilter', as Qt's
  QStackedWidgetEventFilter is built on Qt's
  QStackedWidgetPreviewEventFilter, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QStackedWidgetEventFilter that has a ritual and that
  Python can call so far, 11 names in all: 'metaObject', 'tr', 'install',
  'eventFilterOf', 'addStackedWidgetContextMenuActions',
  'addContextMenuActions', 'removeCurrentPage', 'addPage', 'addPageAfter',
  'changeOrder', 'gotoPage'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QStackedWidgetEventFilter::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QStackedWidgetEventFilter::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QStackedWidgetEventFilter is created at the first use, not by
    'QStackedWidgetEventFilter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QStackedWidgetEventFilter.
  - Qt tells when it has removed the C++ QStackedWidgetEventFilter. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QStackedWidgetEventFilter::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qstackedwidgeteventfilter.html#tr

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
    #  QString QStackedWidgetEventFilter::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN25QStackedWidgetEventFilter2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QStackedWidget)
  @overload(NoneType)
  def install(stackedWidget: Optional[QStackedWidget]) -> None:
    """
    Calls Qt's 'void QStackedWidgetEventFilter::install(QStackedWidget
    *stackedWidget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstackedwidgeteventfilter.html#install

    Parameters
    ----------

    stackedWidget : Optional[QStackedWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QStackedWidgetEventFilter::install(QStackedWidget *stackedWidget)
    Rituals.call(
        'ritual_ZN25QStackedWidgetEventFilter7installEP14QStackedWidget',
        CuteMixin._addressOf(stackedWidget),
    )

  @staticmethod
  @overload(QStackedWidget)
  @overload(NoneType)
  def eventFilterOf(
      stackedWidget: Optional[QStackedWidget],
  ) -> Optional[QStackedWidgetEventFilter]:
    """
    Calls Qt's 'QStackedWidgetEventFilter
    *QStackedWidgetEventFilter::eventFilterOf(const QStackedWidget
    *stackedWidget)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstackedwidgeteventfilter.html#eventFilterOf

    Parameters
    ----------

    stackedWidget : Optional[QStackedWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QStackedWidgetEventFilter]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QStackedWidgetEventFilter
    #      *QStackedWidgetEventFilter::eventFilterOf(const QStackedWidget
    #      *stackedWidget)
    address = Rituals.call(
        'ritual_ZN25QStackedWidgetEventFilter13eventFilterOfEPK14QStackedWi'
        'dget',
        CuteMixin._addressOf(stackedWidget),
    )
    return QStackedWidgetEventFilter._cuteAt(address)

  @staticmethod
  @overload(QStackedWidget, QMenu)
  @overload(QStackedWidget, NoneType)
  @overload(NoneType, QMenu)
  @overload(NoneType, NoneType)
  def addStackedWidgetContextMenuActions(
      stackedWidget: Optional[QStackedWidget],
      popup: Optional[QMenu],
  ) -> Optional[QMenu]:
    """
    Calls Qt's 'QMenu
    *QStackedWidgetEventFilter::addStackedWidgetContextMenuActions(const
    QStackedWidget *stackedWidget, QMenu *popup)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstackedwidgeteventfilter.html

    Parameters
    ----------

    stackedWidget : Optional[QStackedWidget]
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
    #  QMenu *QStackedWidgetEventFilter::addStackedWidgetContextMenuActions(
    #      const QStackedWidget *stackedWidget, QMenu *popup)
    address = Rituals.call(
        'ritual_ZN25QStackedWidgetEventFilter34addStackedWidgetContextMenuA'
        'ctionsEPK14QStackedWidgetP5QMenu',
        CuteMixin._addressOf(stackedWidget), CuteMixin._addressOf(popup),
    )
    from ..QtWidgets import QMenu
    return QMenu._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QStackedWidgetEventFilter'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QStackedWidgetEventFilter::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstackedwidgeteventfilter.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QStackedWidgetEventFilter::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK25QStackedWidgetEventFilter10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  @overload(QStackedWidget)
  @overload(NoneType)
  def __init__(self, parent: Optional[QStackedWidget]) -> None:
    """
    Notes what was given, for Qt's
    'QStackedWidgetEventFilter::QStackedWidgetEventFilter(QStackedWidget
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qstackedwidgeteventfilter.html

    Parameters
    ----------

    parent : Optional[QStackedWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QStackedWidgetEventFilter::QStackedWidgetEventFilter(QStackedWidget
    #      *parent)
    self._noteCreation(QStackedWidgetEventFilter, lambda: Rituals.call(
        'ritual_ZN25QStackedWidgetEventFilterC1EP14QStackedWidget',
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
    Calls Qt's 'QMenu *QStackedWidgetEventFilter::addContextMenuActions(QMenu
    *popup)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstackedwidgeteventfilter.html

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
    #  QMenu *QStackedWidgetEventFilter::addContextMenuActions(QMenu *popup)
    address = self.uglySide.call(
        'ritual_ZN25QStackedWidgetEventFilter21addContextMenuActionsEP5QMen'
        'u',
        self._addressOf(popup),
    )
    from ..QtWidgets import QMenu
    return QMenu._cuteAt(address)

  def removeCurrentPage(self) -> None:
    """
    Calls Qt's 'void QStackedWidgetEventFilter::removeCurrentPage()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstackedwidgeteventfilter.html#removeCurrentPage
    """
    #  void QStackedWidgetEventFilter::removeCurrentPage()
    self.uglySide.call(
        'ritual_ZN25QStackedWidgetEventFilter17removeCurrentPageEv',
    )

  def addPage(self) -> None:
    """
    Calls Qt's 'void QStackedWidgetEventFilter::addPage()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstackedwidgeteventfilter.html#addPage
    """
    #  void QStackedWidgetEventFilter::addPage()
    self.uglySide.call('ritual_ZN25QStackedWidgetEventFilter7addPageEv')

  def addPageAfter(self) -> None:
    """
    Calls Qt's 'void QStackedWidgetEventFilter::addPageAfter()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstackedwidgeteventfilter.html#addPageAfter
    """
    #  void QStackedWidgetEventFilter::addPageAfter()
    self.uglySide.call(
        'ritual_ZN25QStackedWidgetEventFilter12addPageAfterEv',
    )

  def changeOrder(self) -> None:
    """
    Calls Qt's 'void QStackedWidgetEventFilter::changeOrder()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstackedwidgeteventfilter.html#changeOrder
    """
    #  void QStackedWidgetEventFilter::changeOrder()
    self.uglySide.call('ritual_ZN25QStackedWidgetEventFilter11changeOrderEv')

  @overload(int)
  def gotoPage(self, page: int) -> None:
    """
    Calls Qt's 'void QStackedWidgetEventFilter::gotoPage(int page)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qstackedwidgeteventfilter.html#gotoPage

    Parameters
    ----------

    page : int
      Passed on as it is.
    """
    #  void QStackedWidgetEventFilter::gotoPage(int page)
    ritual = 'ritual_ZN25QStackedWidgetEventFilter8gotoPageEi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN25QStackedWidgetEventFilter8gotoPageEi'
    self.uglySide.call(ritual, page)
