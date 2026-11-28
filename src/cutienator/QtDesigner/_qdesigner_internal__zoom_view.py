"""
qdesigner_internal::ZoomView binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/zoomwidget_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means qdesigner_internal::ZoomView to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtWidgets import QGraphicsView, QWidget
from . import qdesigner_internal

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPoint
  from ..QtGui import QContextMenuEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QContextMenuEvent = WAIT['QContextMenuEvent']
  QPoint = WAIT['QPoint']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class ZoomView(QGraphicsView):
  """
  The cute side of Qt's qdesigner_internal::ZoomView: a plain Python object
  standing in front of one C++ qdesigner_internal::ZoomView.

  It is built on the cute 'QGraphicsView', as Qt's
  qdesigner_internal::ZoomView is built on Qt's QGraphicsView, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::ZoomView that has a ritual and
  that Python can call so far, 14 names in all: 'metaObject', 'tr', 'zoom',
  'zoomFactor', 'isZoomContextMenuEnabled', 'setZoomContextMenuEnabled',
  'zoomMenu', 'scrollPosition', 'setScrollPosition', 'scrollToOrigin',
  'setZoom', 'showContextMenu', 'contextMenuEvent', 'applyZoom'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *qdesigner_internal::ZoomView::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int qdesigner_internal::ZoomView::qt_metacall(QMetaObject::Call a0,
    int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QGraphicsScene &qdesigner_internal::ZoomView::scene()': gives a
    type Python has no way to take yet.
  - Qt's 'const QGraphicsScene &qdesigner_internal::ZoomView::scene() const':
    gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  6 of the 25 functions Qt declares: 4 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ qdesigner_internal::ZoomView is created at the first use, not by
    'qdesigner_internal::ZoomView(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ qdesigner_internal::ZoomView.
  - Qt tells when it has removed the C++ qdesigner_internal::ZoomView. Every
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
    Calls Qt's 'QString qdesigner_internal::ZoomView::tr(const char *s, const
    char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-zoomview.html#tr

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
    #  QString qdesigner_internal::ZoomView::tr(const char *s, const char *c,
    #      int n)
    return Rituals.call(
        'ritual_ZN18qdesigner_internal8ZoomView2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::ZoomView'

  #  The functions Qt calls itself that qdesigner_internal::ZoomView is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'applyZoom': (
          ('_ZN18qdesigner_internal8ZoomView9applyZoomEv',
           ('nothing', 'nothing', ''),
           ()),
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
    Calls Qt's 'const QMetaObject *qdesigner_internal::ZoomView::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-zoomview.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *qdesigner_internal::ZoomView::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal8ZoomView10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def zoom(self) -> int:
    """
    Calls Qt's 'int qdesigner_internal::ZoomView::zoom() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-zoomview.html#zoom
    """
    #  int qdesigner_internal::ZoomView::zoom() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal8ZoomView4zoomEv',
    )

  def zoomFactor(self) -> float:
    """
    Calls Qt's 'qreal qdesigner_internal::ZoomView::zoomFactor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-zoomview.html#zoomFactor
    """
    #  qreal qdesigner_internal::ZoomView::zoomFactor() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal8ZoomView10zoomFactorEv',
    )

  def isZoomContextMenuEnabled(self) -> bool:
    """
    Calls Qt's 'bool qdesigner_internal::ZoomView::isZoomContextMenuEnabled()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-zoomview.html
    """
    #  bool qdesigner_internal::ZoomView::isZoomContextMenuEnabled() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal8ZoomView24isZoomContextMenuEnabledE'
        'v',
    )

  def scrollPosition(self) -> QPoint:
    """
    Calls Qt's 'QPoint qdesigner_internal::ZoomView::scrollPosition() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-zoomview.html#scrollPosition

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint qdesigner_internal::ZoomView::scrollPosition() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal8ZoomView14scrollPositionEv',
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setZoomContextMenuEnabled(self, e: bool) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ZoomView::setZoomContextMenuEnabled(bool e)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-zoomview.html

    Parameters
    ----------

    e : bool
      Passed on as it is.
    """
    #  void qdesigner_internal::ZoomView::setZoomContextMenuEnabled(bool e)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal8ZoomView25setZoomContextMenuEnabledE'
        'b',
        e,
    )

  @overload(QPoint)
  def setScrollPosition(self, pos: QPoint) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ZoomView::setScrollPosition(const
    QPoint &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-zoomview.html#setScrollPosition

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void qdesigner_internal::ZoomView::setScrollPosition(const QPoint
    #      &pos)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal8ZoomView17setScrollPositionERK6QPoin'
        't',
        self._valueOf(pos),
    )

  @overload(int)
  def setZoom(self, percent: int) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ZoomView::setZoom(int percent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-zoomview.html#setZoom

    Parameters
    ----------

    percent : int
      Passed on as it is.
    """
    #  void qdesigner_internal::ZoomView::setZoom(int percent)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal8ZoomView7setZoomEi', percent,
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
    Notes what was given, for Qt's
    'qdesigner_internal::ZoomView::ZoomView(QWidget *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-zoomview.html#ZoomView

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  qdesigner_internal::ZoomView::ZoomView(QWidget *parent)
    self._noteCreation(ZoomView, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal8ZoomViewC1EP7QWidget',
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

  def zoomMenu(self) -> Optional[qdesigner_internal.ZoomMenu]:
    """
    Calls Qt's 'ZoomMenu *qdesigner_internal::ZoomView::zoomMenu()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-zoomview.html#zoomMenu

    Returns
    -------

    Optional[qdesigner_internal.ZoomMenu]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  ZoomMenu *qdesigner_internal::ZoomView::zoomMenu()
    address = self.uglySide.call(
        'ritual_ZN18qdesigner_internal8ZoomView8zoomMenuEv',
    )
    return qdesigner_internal.ZoomMenu._cuteAt(address)

  def scrollToOrigin(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ZoomView::scrollToOrigin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-zoomview.html#scrollToOrigin
    """
    #  void qdesigner_internal::ZoomView::scrollToOrigin()
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal8ZoomView14scrollToOriginEv',
    )

  @overload(QPoint)
  def showContextMenu(self, globalPos: QPoint) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ZoomView::showContextMenu(const
    QPoint &globalPos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-zoomview.html#showContextMenu

    Parameters
    ----------

    globalPos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void qdesigner_internal::ZoomView::showContextMenu(const QPoint
    #      &globalPos)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal8ZoomView15showContextMenuERK6QPoint',
        self._valueOf(globalPos),
    )

  @overload(QContextMenuEvent)
  @overload(NoneType)
  def contextMenuEvent(self, event: Optional[QContextMenuEvent]) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::ZoomView::contextMenuEvent(QContextMenuEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-zoomview.html#contextMenuEvent

    Parameters
    ----------

    event : Optional[QContextMenuEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void qdesigner_internal::ZoomView::contextMenuEvent(QContextMenuEvent
    #      *event)
    ritual = (
        'ritual_ZN18qdesigner_internal8ZoomView16contextMenuEventEP17QConte'
        'xtMenuEvent')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18qdesigner_internal8ZoomView16contextMenuEventEP17'
          'QContextMenuEvent')
    self.uglySide.call(ritual, self._addressOf(event))

  def applyZoom(self) -> None:
    """
    Calls Qt's 'void qdesigner_internal::ZoomView::applyZoom()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-zoomview.html#applyZoom
    """
    #  void qdesigner_internal::ZoomView::applyZoom()
    ritual = 'ritual_ZN18qdesigner_internal8ZoomView9applyZoomEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18qdesigner_internal8ZoomView9applyZoomEv'
    self.uglySide.call(ritual)
