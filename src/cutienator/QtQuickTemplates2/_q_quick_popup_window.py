"""
QQuickPopupWindow binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickpopupwindow_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuickPopupWindow to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtGui import QWindow
from ..QtQuick import QQuickWindowQmlImpl

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject, QPoint, QRect
  from ..QtGui import QHideEvent, QMoveEvent, QResizeEvent
  from . import QQuickPopup
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QHideEvent = WAIT['QHideEvent']
  QMoveEvent = WAIT['QMoveEvent']
  QPoint = WAIT['QPoint']
  QQuickPopup = WAIT['QQuickPopup']
  QResizeEvent = WAIT['QResizeEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickPopupWindow(QQuickWindowQmlImpl):
  """
  The cute side of Qt's QQuickPopupWindow: a plain Python object standing in
  front of one C++ QQuickPopupWindow.

  It is built on the cute 'QQuickWindowQmlImpl', as Qt's QQuickPopupWindow is
  built on Qt's QQuickWindowQmlImpl, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickPopupWindow that has a ritual and that Python
  can call so far, 14 names in all: 'metaObject', 'tr', 'popup', 'hideEvent',
  'moveEvent', 'resizeEvent', 'event', 'windowChanged',
  'parentWindowXChanged', 'parentWindowYChanged',
  'handlePopupPositionChangeFromWindowSystem', 'implicitWidthChanged',
  'implicitHeightChanged', 'parentControlGeometry'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickPopupWindow::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickPopupWindow::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQuickPopupWindow::qt_qmlMarker_anonymous()': one of Qt's own
    inner workings.
  - Qt's 'std::optional<QPoint> QQuickPopupWindow::global2Local(const QPoint
    &pos) const': gives a type Python has no way to take yet.
  - Qt's 'QQuickPopupWindowPrivate *QQuickPopupWindow::d_func()': gives
    'QQuickPopupWindowPrivate', which has no cute class yet.
  - Qt's 'const QQuickPopupWindowPrivate *QQuickPopupWindow::d_func() const':
    gives 'QQuickPopupWindowPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 25 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QQuickPopupWindow is created at the first use, not by
    'QQuickPopupWindow(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickPopupWindow.
  - Qt tells when it has removed the C++ QQuickPopupWindow. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickPopupWindow that has no cute function yet,
    'global2Local', holds a function that raises 'NotImplementedError', and
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
    Calls Qt's 'QString QQuickPopupWindow::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopupwindow.html#tr

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
    #  QString QQuickPopupWindow::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN17QQuickPopupWindow2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickPopupWindow'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickPopupWindow::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopupwindow.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickPopupWindow::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickPopupWindow10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def popup(self) -> Optional[QQuickPopup]:
    """
    Calls Qt's 'QQuickPopup *QQuickPopupWindow::popup() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopupwindow.html#popup

    Returns
    -------

    Optional[QQuickPopup]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickPopup *QQuickPopupWindow::popup() const
    address = self.uglySide.call('ritual_ZNK17QQuickPopupWindow5popupEv')
    from . import QQuickPopup
    return QQuickPopup._cuteAt(address)

  def parentControlGeometry(self) -> QRect:
    """
    Calls Qt's 'QRect QQuickPopupWindow::parentControlGeometry() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupwindow.html#parentControlGeometry

    Returns
    -------

    QRect
      A new cute QRect around the copy Qt gave back. Python owns it.
    """
    #  QRect QQuickPopupWindow::parentControlGeometry() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuickPopupWindow21parentControlGeometryEv',
    )
    from ..QtCore import QRect
    return QRect._cuteOwning(address)

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

  @overload(QQuickPopup)
  @overload(NoneType)
  @overload(QQuickPopup, QWindow)
  @overload(QQuickPopup, NoneType)
  @overload(NoneType, QWindow)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      popup: Optional[QQuickPopup],
      parent: Optional[QWindow] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQuickPopupWindow::QQuickPopupWindow(QQuickPopup *popup, QWindow
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupwindow.html#QQuickPopupWindow

    Parameters
    ----------

    popup : Optional[QQuickPopup]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickPopupWindow::QQuickPopupWindow(QQuickPopup *popup, QWindow
    #      *parent)
    self._noteCreation(QQuickPopupWindow, lambda: Rituals.call(
        'ritual_ZN17QQuickPopupWindowC1EP11QQuickPopupP7QWindow',
        self._addressOf(popup), self._addressOf(parent),
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

  @overload(QHideEvent)
  @overload(NoneType)
  def hideEvent(self, e: Optional[QHideEvent]) -> None:
    """
    Calls Qt's 'void QQuickPopupWindow::hideEvent(QHideEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopupwindow.html#hideEvent

    Parameters
    ----------

    e : Optional[QHideEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPopupWindow::hideEvent(QHideEvent *e)
    ritual = 'ritual_ZN17QQuickPopupWindow9hideEventEP10QHideEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickPopupWindow9hideEventEP10QHideEvent'
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QMoveEvent)
  @overload(NoneType)
  def moveEvent(self, e: Optional[QMoveEvent]) -> None:
    """
    Calls Qt's 'void QQuickPopupWindow::moveEvent(QMoveEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopupwindow.html#moveEvent

    Parameters
    ----------

    e : Optional[QMoveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPopupWindow::moveEvent(QMoveEvent *e)
    ritual = 'ritual_ZN17QQuickPopupWindow9moveEventEP10QMoveEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickPopupWindow9moveEventEP10QMoveEvent'
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QResizeEvent)
  @overload(NoneType)
  def resizeEvent(self, e: Optional[QResizeEvent]) -> None:
    """
    Calls Qt's 'void QQuickPopupWindow::resizeEvent(QResizeEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopupwindow.html#resizeEvent

    Parameters
    ----------

    e : Optional[QResizeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPopupWindow::resizeEvent(QResizeEvent *e)
    ritual = 'ritual_ZN17QQuickPopupWindow11resizeEventEP12QResizeEvent'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QQuickPopupWindow11resizeEventEP12QResizeEvent')
    self.uglySide.call(ritual, self._addressOf(e))

  @overload(QEvent)
  @overload(NoneType)
  def event(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QQuickPopupWindow::event(QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickpopupwindow.html#event

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuickPopupWindow::event(QEvent *e)
    ritual = 'ritual_ZN17QQuickPopupWindow5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QQuickPopupWindow5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(e))

  @overload(QWindow)
  @overload(NoneType)
  def windowChanged(self, window: Optional[QWindow]) -> None:
    """
    Calls Qt's 'void QQuickPopupWindow::windowChanged(QWindow *window)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupwindow.html#windowChanged

    Parameters
    ----------

    window : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickPopupWindow::windowChanged(QWindow *window)
    self.uglySide.call(
        'ritual_ZN17QQuickPopupWindow13windowChangedEP7QWindow',
        self._addressOf(window),
    )

  @overload(int)
  def parentWindowXChanged(self, newX: int) -> None:
    """
    Calls Qt's 'void QQuickPopupWindow::parentWindowXChanged(int newX)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupwindow.html#parentWindowXChanged

    Parameters
    ----------

    newX : int
      Passed on as it is.
    """
    #  void QQuickPopupWindow::parentWindowXChanged(int newX)
    self.uglySide.call(
        'ritual_ZN17QQuickPopupWindow20parentWindowXChangedEi', newX,
    )

  @overload(int)
  def parentWindowYChanged(self, newY: int) -> None:
    """
    Calls Qt's 'void QQuickPopupWindow::parentWindowYChanged(int newY)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupwindow.html#parentWindowYChanged

    Parameters
    ----------

    newY : int
      Passed on as it is.
    """
    #  void QQuickPopupWindow::parentWindowYChanged(int newY)
    self.uglySide.call(
        'ritual_ZN17QQuickPopupWindow20parentWindowYChangedEi', newY,
    )

  @overload(QPoint)
  def handlePopupPositionChangeFromWindowSystem(self, pos: QPoint) -> None:
    """
    Calls Qt's 'void
    QQuickPopupWindow::handlePopupPositionChangeFromWindowSystem(const QPoint
    &pos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupwindow.html

    Parameters
    ----------

    pos : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void
    #      QQuickPopupWindow::handlePopupPositionChangeFromWindowSystem(const
    #      QPoint &pos)
    self.uglySide.call(
        'ritual_ZN17QQuickPopupWindow41handlePopupPositionChangeFromWindowS'
        'ystemERK6QPoint',
        self._valueOf(pos),
    )

  def implicitWidthChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopupWindow::implicitWidthChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupwindow.html#implicitWidthChanged
    """
    #  void QQuickPopupWindow::implicitWidthChanged()
    self.uglySide.call(
        'ritual_ZN17QQuickPopupWindow20implicitWidthChangedEv',
    )

  def implicitHeightChanged(self) -> None:
    """
    Calls Qt's 'void QQuickPopupWindow::implicitHeightChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickpopupwindow.html#implicitHeightChanged
    """
    #  void QQuickPopupWindow::implicitHeightChanged()
    self.uglySide.call(
        'ritual_ZN17QQuickPopupWindow21implicitHeightChangedEv',
    )

  @staticmethod
  def global2Local(*__, **_) -> Never:
    """
    Qt's 'std::optional<QPoint> QQuickPopupWindow::global2Local(const QPoint
    &pos) const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQuickPopupWindow.global2Local' has no cute function yet. Qt's "
        "'std::optional<QPoint> QQuickPopupWindow::global2Local(const "
        "QPoint &pos) const': gives a type Python has no way to take yet.")
