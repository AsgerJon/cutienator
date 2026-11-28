"""
QVideoWidget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimediaWidgets/qvideowidget.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ..QtWidgets import QWidget

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject, QSize
  from ..QtGui import QHideEvent, QMoveEvent, QResizeEvent, QShowEvent
  from ..QtMultimedia import QVideoSink
  from . import QVideoWidgetPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QHideEvent = WAIT['QHideEvent']
  QMoveEvent = WAIT['QMoveEvent']
  QResizeEvent = WAIT['QResizeEvent']
  QShowEvent = WAIT['QShowEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QVideoWidget(QWidget):
  """
  The cute side of Qt's QVideoWidget: a plain Python object standing in front
  of one C++ QVideoWidget.

  It is built on the cute 'QWidget', as Qt's QVideoWidget is built on Qt's
  QWidget, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QVideoWidget that has a ritual and that Python can
  call so far, 15 names in all: 'metaObject', 'tr', 'videoSink',
  'aspectRatioMode', 'sizeHint', 'setFullScreen', 'setAspectRatioMode',
  'fullScreenChanged', 'aspectRatioModeChanged', 'event', 'showEvent',
  'hideEvent', 'resizeEvent', 'moveEvent', 'd_func'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QVideoWidget::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QVideoWidget::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QVideoWidget::~QVideoWidget()': the destructor: Python never
    removes a C++ QVideoWidget.
  - Qt's 'const QVideoWidgetPrivate *QVideoWidget::d_func() const': takes in
    Python what 'QVideoWidgetPrivate *QVideoWidget::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 22 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QVideoWidget is created at the first use, not by
    'QVideoWidget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QVideoWidget.
  - Qt tells when it has removed the C++ QVideoWidget. Every call on the cute
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
    Calls Qt's 'QString QVideoWidget::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qvideowidget.html#tr

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
    #  QString QVideoWidget::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QVideoWidget2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QVideoWidget'

  #  A C++ QVideoWidget Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QVideoWidget'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QVideoWidget::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideowidget.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QVideoWidget::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QVideoWidget10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def videoSink(self) -> Optional[QVideoSink]:
    """
    Calls Qt's 'QVideoSink *QVideoWidget::videoSink() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideowidget.html#videoSink

    Returns
    -------

    Optional[QVideoSink]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QVideoSink *QVideoWidget::videoSink() const
    address = self.uglySide.call('ritual_ZNK12QVideoWidget9videoSinkEv')
    from ..QtMultimedia import QVideoSink
    return QVideoSink._cuteAt(address)

  def aspectRatioMode(self) -> Qt.AspectRatioMode:
    """
    Calls Qt's 'Qt::AspectRatioMode QVideoWidget::aspectRatioMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideowidget.html#aspectRatioMode

    Returns
    -------

    Qt.AspectRatioMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.AspectRatioMode(number)' gives.
    """
    #  Qt::AspectRatioMode QVideoWidget::aspectRatioMode() const
    return Qt.AspectRatioMode(self.uglySide.call(
        'ritual_ZNK12QVideoWidget15aspectRatioModeEv',
    ))

  def sizeHint(self) -> QSize:
    """
    Calls Qt's 'QSize QVideoWidget::sizeHint() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideowidget.html#sizeHint

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QVideoWidget::sizeHint() const
    ritual = 'ritual_ZNK12QVideoWidget8sizeHintEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK12QVideoWidget8sizeHintEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setFullScreen(self, fullScreen: bool) -> None:
    """
    Calls Qt's 'void QVideoWidget::setFullScreen(bool fullScreen)'.

    Qt's own words: https://doc.qt.io/qt-6/qvideowidget.html#setFullScreen

    Parameters
    ----------

    fullScreen : bool
      Passed on as it is.
    """
    #  void QVideoWidget::setFullScreen(bool fullScreen)
    self.uglySide.call(
        'ritual_ZN12QVideoWidget13setFullScreenEb', fullScreen,
    )

  @overload(Qt.AspectRatioMode)
  def setAspectRatioMode(self, mode: Qt.AspectRatioMode) -> None:
    """
    Calls Qt's 'void QVideoWidget::setAspectRatioMode(Qt::AspectRatioMode
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideowidget.html#setAspectRatioMode

    Parameters
    ----------

    mode : Qt.AspectRatioMode
      Passed on as its number.
    """
    #  void QVideoWidget::setAspectRatioMode(Qt::AspectRatioMode mode)
    self.uglySide.call(
        'ritual_ZN12QVideoWidget18setAspectRatioModeEN2Qt15AspectRatioModeE',
        mode.value,
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
    Notes what was given, for Qt's 'QVideoWidget::QVideoWidget(QWidget
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvideowidget.html#QVideoWidget

    Parameters
    ----------

    parent : Optional[QWidget]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QVideoWidget::QVideoWidget(QWidget *parent)
    self._noteCreation(QVideoWidget, lambda: Rituals.call(
        'ritual_ZN12QVideoWidgetC1EP7QWidget', self._addressOf(parent),
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

  @overload(bool)
  def fullScreenChanged(self, fullScreen: bool) -> None:
    """
    Calls Qt's 'void QVideoWidget::fullScreenChanged(bool fullScreen)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideowidget.html#fullScreenChanged

    Parameters
    ----------

    fullScreen : bool
      Passed on as it is.
    """
    #  void QVideoWidget::fullScreenChanged(bool fullScreen)
    self.uglySide.call(
        'ritual_ZN12QVideoWidget17fullScreenChangedEb', fullScreen,
    )

  @overload(Qt.AspectRatioMode)
  def aspectRatioModeChanged(self, mode: Qt.AspectRatioMode) -> None:
    """
    Calls Qt's 'void QVideoWidget::aspectRatioModeChanged(Qt::AspectRatioMode
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideowidget.html#aspectRatioModeChanged

    Parameters
    ----------

    mode : Qt.AspectRatioMode
      Passed on as its number.
    """
    #  void QVideoWidget::aspectRatioModeChanged(Qt::AspectRatioMode mode)
    self.uglySide.call(
        'ritual_ZN12QVideoWidget22aspectRatioModeChangedEN2Qt15AspectRatioM'
        'odeE',
        mode.value,
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, event: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QVideoWidget::event(QEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qvideowidget.html#event

    Parameters
    ----------

    event : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QVideoWidget::event(QEvent *event)
    ritual = 'ritual_ZN12QVideoWidget5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QVideoWidget5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(event))

  @overload(QShowEvent)
  @overload(NoneType)
  def showEvent(self, event: Optional[QShowEvent]) -> None:
    """
    Calls Qt's 'void QVideoWidget::showEvent(QShowEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qvideowidget.html#showEvent

    Parameters
    ----------

    event : Optional[QShowEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QVideoWidget::showEvent(QShowEvent *event)
    ritual = 'ritual_ZN12QVideoWidget9showEventEP10QShowEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QVideoWidget9showEventEP10QShowEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QHideEvent)
  @overload(NoneType)
  def hideEvent(self, event: Optional[QHideEvent]) -> None:
    """
    Calls Qt's 'void QVideoWidget::hideEvent(QHideEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qvideowidget.html#hideEvent

    Parameters
    ----------

    event : Optional[QHideEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QVideoWidget::hideEvent(QHideEvent *event)
    ritual = 'ritual_ZN12QVideoWidget9hideEventEP10QHideEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QVideoWidget9hideEventEP10QHideEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QResizeEvent)
  @overload(NoneType)
  def resizeEvent(self, event: Optional[QResizeEvent]) -> None:
    """
    Calls Qt's 'void QVideoWidget::resizeEvent(QResizeEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qvideowidget.html#resizeEvent

    Parameters
    ----------

    event : Optional[QResizeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QVideoWidget::resizeEvent(QResizeEvent *event)
    ritual = 'ritual_ZN12QVideoWidget11resizeEventEP12QResizeEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QVideoWidget11resizeEventEP12QResizeEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  @overload(QMoveEvent)
  @overload(NoneType)
  def moveEvent(self, event: Optional[QMoveEvent]) -> None:
    """
    Calls Qt's 'void QVideoWidget::moveEvent(QMoveEvent *event)'.

    Qt's own words: https://doc.qt.io/qt-6/qvideowidget.html#moveEvent

    Parameters
    ----------

    event : Optional[QMoveEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QVideoWidget::moveEvent(QMoveEvent *event)
    ritual = 'ritual_ZN12QVideoWidget9moveEventEP10QMoveEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QVideoWidget9moveEventEP10QMoveEvent'
    self.uglySide.call(ritual, self._addressOf(event))

  def d_func(self) -> Optional[QVideoWidgetPrivate]:
    """
    Calls Qt's 'QVideoWidgetPrivate *QVideoWidget::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qvideowidget.html#d_func

    Returns
    -------

    Optional[QVideoWidgetPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QVideoWidgetPrivate *QVideoWidget::d_func()
    address = self.uglySide.call('ritual_ZN12QVideoWidget6d_funcEv')
    from . import QVideoWidgetPrivate
    return QVideoWidgetPrivate._cuteAt(address)
