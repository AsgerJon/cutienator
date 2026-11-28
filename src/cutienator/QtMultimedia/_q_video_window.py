"""
QVideoWindow binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qvideowindow_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QVideoWindow to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt
from ..QtGui import QWindow

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QEvent, QMetaObject
  from ..QtGui import QResizeEvent, QScreen
  from . import QVideoFrame, QVideoSink
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QResizeEvent = WAIT['QResizeEvent']
  QScreen = WAIT['QScreen']
  QVideoFrame = WAIT['QVideoFrame']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QVideoWindow(QWindow):
  """
  The cute side of Qt's QVideoWindow: a plain Python object standing in front
  of one C++ QVideoWindow.

  It is built on the cute 'QWindow', as Qt's QVideoWindow is built on Qt's
  QWindow, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QVideoWindow that has a ritual and that Python can
  call so far, 9 names in all: 'metaObject', 'tr', 'videoSink',
  'aspectRatioMode', 'setAspectRatioMode', 'aspectRatioModeChanged', 'event',
  'resizeEvent', 'setVideoFrame'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QVideoWindow::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QVideoWindow::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QVideoWindow::~QVideoWindow()': the destructor: Python never
    removes a C++ QVideoWindow.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QVideoWindow is created at the first use, not by
    'QVideoWindow(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QVideoWindow.
  - Qt tells when it has removed the C++ QVideoWindow. Every call on the cute
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
    Calls Qt's 'QString QVideoWindow::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qvideowindow.html#tr

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
    #  QString QVideoWindow::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QVideoWindow2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QVideoWindow'

  #  A C++ QVideoWindow Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QVideoWindow'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QVideoWindow::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideowindow.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QVideoWindow::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QVideoWindow10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def videoSink(self) -> Optional[QVideoSink]:
    """
    Calls Qt's 'QVideoSink *QVideoWindow::videoSink() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideowindow.html#videoSink

    Returns
    -------

    Optional[QVideoSink]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QVideoSink *QVideoWindow::videoSink() const
    address = self.uglySide.call('ritual_ZNK12QVideoWindow9videoSinkEv')
    from . import QVideoSink
    return QVideoSink._cuteAt(address)

  def aspectRatioMode(self) -> Qt.AspectRatioMode:
    """
    Calls Qt's 'Qt::AspectRatioMode QVideoWindow::aspectRatioMode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qvideowindow.html#aspectRatioMode

    Returns
    -------

    Qt.AspectRatioMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt.AspectRatioMode(number)' gives.
    """
    #  Qt::AspectRatioMode QVideoWindow::aspectRatioMode() const
    return Qt.AspectRatioMode(self.uglySide.call(
        'ritual_ZNK12QVideoWindow15aspectRatioModeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt.AspectRatioMode)
  def setAspectRatioMode(self, mode: Qt.AspectRatioMode) -> None:
    """
    Calls Qt's 'void QVideoWindow::setAspectRatioMode(Qt::AspectRatioMode
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideowindow.html#setAspectRatioMode

    Parameters
    ----------

    mode : Qt.AspectRatioMode
      Passed on as its number.
    """
    #  void QVideoWindow::setAspectRatioMode(Qt::AspectRatioMode mode)
    self.uglySide.call(
        'ritual_ZN12QVideoWindow18setAspectRatioModeEN2Qt15AspectRatioModeE',
        mode.value,
    )

  @overload(QVideoFrame)
  def setVideoFrame(self, frame: QVideoFrame) -> None:
    """
    Calls Qt's 'void QVideoWindow::setVideoFrame(const QVideoFrame &frame)'.

    Qt's own words: https://doc.qt.io/qt-6/qvideowindow.html#setVideoFrame

    Parameters
    ----------

    frame : QVideoFrame
      Passed on as a value: Qt reads the C++ QVideoFrame, which stays
      Python's own.
    """
    #  void QVideoWindow::setVideoFrame(const QVideoFrame &frame)
    self.uglySide.call(
        'ritual_ZN12QVideoWindow13setVideoFrameERK11QVideoFrame',
        self._valueOf(frame),
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
  @overload(QScreen)
  @overload(NoneType)
  def __init__(self, screen: Optional[QScreen] = None) -> None:
    """
    Notes what was given, for Qt's 'QVideoWindow::QVideoWindow(QScreen
    *screen)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvideowindow.html#QVideoWindow

    Parameters
    ----------

    screen : Optional[QScreen]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QVideoWindow::QVideoWindow(QScreen *screen)
    self._noteCreation(QVideoWindow, lambda: Rituals.call(
        'ritual_ZN12QVideoWindowC1EP7QScreen', self._addressOf(screen),
    ))

  @overload(QWindow)
  def __init__(self, parent: Optional[QWindow]) -> None:
    """
    Notes what was given, for Qt's 'QVideoWindow::QVideoWindow(QWindow
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qvideowindow.html#QVideoWindow

    Parameters
    ----------

    parent : Optional[QWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QVideoWindow::QVideoWindow(QWindow *parent)
    self._noteCreation(QVideoWindow, lambda: Rituals.call(
        'ritual_ZN12QVideoWindowC1EP7QWindow', self._addressOf(parent),
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

  @overload(Qt.AspectRatioMode)
  def aspectRatioModeChanged(self, mode: Qt.AspectRatioMode) -> None:
    """
    Calls Qt's 'void QVideoWindow::aspectRatioModeChanged(Qt::AspectRatioMode
    mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qvideowindow.html#aspectRatioModeChanged

    Parameters
    ----------

    mode : Qt.AspectRatioMode
      Passed on as its number.
    """
    #  void QVideoWindow::aspectRatioModeChanged(Qt::AspectRatioMode mode)
    self.uglySide.call(
        'ritual_ZN12QVideoWindow22aspectRatioModeChangedEN2Qt15AspectRatioM'
        'odeE',
        mode.value,
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QVideoWindow::event(QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qvideowindow.html#event

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QVideoWindow::event(QEvent *e)
    ritual = 'ritual_ZN12QVideoWindow5eventEP6QEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QVideoWindow5eventEP6QEvent'
    return self.uglySide.call(ritual, self._addressOf(e))

  @overload(QResizeEvent)
  @overload(NoneType)
  def resizeEvent(self, a0: Optional[QResizeEvent]) -> None:
    """
    Calls Qt's 'void QVideoWindow::resizeEvent(QResizeEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qvideowindow.html#resizeEvent

    Parameters
    ----------

    a0 : Optional[QResizeEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QVideoWindow::resizeEvent(QResizeEvent *a0)
    ritual = 'ritual_ZN12QVideoWindow11resizeEventEP12QResizeEvent'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QVideoWindow11resizeEventEP12QResizeEvent'
    self.uglySide.call(ritual, self._addressOf(a0))
