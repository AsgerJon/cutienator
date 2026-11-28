"""
QQuickRenderControl binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/qquickrendercontrol.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPoint, QThread
  from ..QtGui import QRhi, QRhiCommandBuffer, QWindow
  from . import QQuickRenderControlPrivate, QQuickWindow
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPoint = WAIT['QPoint']
  QQuickWindow = WAIT['QQuickWindow']
  QThread = WAIT['QThread']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickRenderControl(QObject):
  """
  The cute side of Qt's QQuickRenderControl: a plain Python object standing
  in front of one C++ QQuickRenderControl.

  It is built on the cute 'QObject', as Qt's QQuickRenderControl is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickRenderControl that has a ritual and that
  Python can call so far, 20 names in all: 'metaObject', 'tr',
  'prepareThread', 'setSamples', 'samples', 'initialize', 'invalidate',
  'beginFrame', 'endFrame', 'polishItems', 'sync', 'render',
  'renderWindowFor', 'renderWindow', 'window', 'rhi', 'commandBuffer',
  'renderRequested', 'sceneChanged', 'd_func'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickRenderControl::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuickRenderControl::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickRenderControl::~QQuickRenderControl()': the destructor:
    Python never removes a C++ QQuickRenderControl.
  - Qt's 'QQuickRenderControl::QQuickRenderControl(QQuickRenderControlPrivate
    &dd, QObject *parent)': takes a type Python has no way to hand over yet.
  - Qt's 'const QQuickRenderControlPrivate *QQuickRenderControl::d_func()
    const': takes in Python what 'QQuickRenderControlPrivate
    *QQuickRenderControl::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 28 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickRenderControl is created at the first use, not by
    'QQuickRenderControl(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickRenderControl.
  - Qt tells when it has removed the C++ QQuickRenderControl. Every call on
    the cute object, and every use of it as an argument, then raises
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
    Calls Qt's 'QString QQuickRenderControl::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrendercontrol.html#tr

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
    #  QString QQuickRenderControl::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QQuickRenderControl2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QQuickWindow)
  @overload(NoneType)
  @overload(QQuickWindow, QPoint)
  @overload(QQuickWindow, NoneType)
  @overload(NoneType, QPoint)
  @overload(NoneType, NoneType)
  def renderWindowFor(
      win: Optional[QQuickWindow],
      offset: Optional[QPoint] = None,
  ) -> Optional[QWindow]:
    """
    Calls Qt's 'QWindow *QQuickRenderControl::renderWindowFor(QQuickWindow
    *win, QPoint *offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrendercontrol.html#renderWindowFor

    Parameters
    ----------

    win : Optional[QQuickWindow]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    offset : Optional[QPoint]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.

    Returns
    -------

    Optional[QWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindow *QQuickRenderControl::renderWindowFor(QQuickWindow *win,
    #      QPoint *offset)
    address = Rituals.call(
        'ritual_ZN19QQuickRenderControl15renderWindowForEP12QQuickWindowP6Q'
        'Point',
        CuteMixin._addressOf(win), CuteMixin._addressOf(offset),
    )
    from ..QtGui import QWindow
    return QWindow._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickRenderControl'

  #  A C++ QQuickRenderControl Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickRenderControl'

  #  The functions Qt calls itself that QQuickRenderControl is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'renderWindow': (
          ('_ZN19QQuickRenderControl12renderWindowEP6QPoint',
           ('address', 'address', 'QtGui:QWindow'),
           (
               ('address', 'address', 'QtCore:QPoint'),
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
    Calls Qt's 'const QMetaObject *QQuickRenderControl::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrendercontrol.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickRenderControl::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickRenderControl10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def samples(self) -> int:
    """
    Calls Qt's 'int QQuickRenderControl::samples() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrendercontrol.html#samples
    """
    #  int QQuickRenderControl::samples() const
    return self.uglySide.call('ritual_ZNK19QQuickRenderControl7samplesEv')

  def window(self) -> Optional[QQuickWindow]:
    """
    Calls Qt's 'QQuickWindow *QQuickRenderControl::window() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrendercontrol.html#window

    Returns
    -------

    Optional[QQuickWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickWindow *QQuickRenderControl::window() const
    address = self.uglySide.call('ritual_ZNK19QQuickRenderControl6windowEv')
    from . import QQuickWindow
    return QQuickWindow._cuteAt(address)

  def rhi(self) -> Optional[QRhi]:
    """
    Calls Qt's 'QRhi *QQuickRenderControl::rhi() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrendercontrol.html#rhi

    Returns
    -------

    Optional[QRhi]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhi *QQuickRenderControl::rhi() const
    address = self.uglySide.call('ritual_ZNK19QQuickRenderControl3rhiEv')
    from ..QtGui import QRhi
    return QRhi._cuteAt(address)

  def commandBuffer(self) -> Optional[QRhiCommandBuffer]:
    """
    Calls Qt's 'QRhiCommandBuffer *QQuickRenderControl::commandBuffer()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrendercontrol.html#commandBuffer

    Returns
    -------

    Optional[QRhiCommandBuffer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRhiCommandBuffer *QQuickRenderControl::commandBuffer() const
    address = self.uglySide.call(
        'ritual_ZNK19QQuickRenderControl13commandBufferEv',
    )
    from ..QtGui import QRhiCommandBuffer
    return QRhiCommandBuffer._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setSamples(self, sampleCount: int) -> None:
    """
    Calls Qt's 'void QQuickRenderControl::setSamples(int sampleCount)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrendercontrol.html#setSamples

    Parameters
    ----------

    sampleCount : int
      Passed on as it is.
    """
    #  void QQuickRenderControl::setSamples(int sampleCount)
    self.uglySide.call(
        'ritual_ZN19QQuickRenderControl10setSamplesEi', sampleCount,
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQuickRenderControl::QQuickRenderControl(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrendercontrol.html#QQuickRenderControl

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQuickRenderControl::QQuickRenderControl(QObject *parent)
    self._noteCreation(QQuickRenderControl, lambda: Rituals.call(
        'ritual_ZN19QQuickRenderControlC1EP7QObject',
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

  @overload(QThread)
  @overload(NoneType)
  def prepareThread(self, targetThread: Optional[QThread]) -> None:
    """
    Calls Qt's 'void QQuickRenderControl::prepareThread(QThread
    *targetThread)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrendercontrol.html#prepareThread

    Parameters
    ----------

    targetThread : Optional[QThread]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickRenderControl::prepareThread(QThread *targetThread)
    self.uglySide.call(
        'ritual_ZN19QQuickRenderControl13prepareThreadEP7QThread',
        self._addressOf(targetThread),
    )

  def initialize(self) -> bool:
    """
    Calls Qt's 'bool QQuickRenderControl::initialize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrendercontrol.html#initialize
    """
    #  bool QQuickRenderControl::initialize()
    return self.uglySide.call('ritual_ZN19QQuickRenderControl10initializeEv')

  def invalidate(self) -> None:
    """
    Calls Qt's 'void QQuickRenderControl::invalidate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrendercontrol.html#invalidate
    """
    #  void QQuickRenderControl::invalidate()
    self.uglySide.call('ritual_ZN19QQuickRenderControl10invalidateEv')

  def beginFrame(self) -> None:
    """
    Calls Qt's 'void QQuickRenderControl::beginFrame()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrendercontrol.html#beginFrame
    """
    #  void QQuickRenderControl::beginFrame()
    self.uglySide.call('ritual_ZN19QQuickRenderControl10beginFrameEv')

  def endFrame(self) -> None:
    """
    Calls Qt's 'void QQuickRenderControl::endFrame()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrendercontrol.html#endFrame
    """
    #  void QQuickRenderControl::endFrame()
    self.uglySide.call('ritual_ZN19QQuickRenderControl8endFrameEv')

  def polishItems(self) -> None:
    """
    Calls Qt's 'void QQuickRenderControl::polishItems()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrendercontrol.html#polishItems
    """
    #  void QQuickRenderControl::polishItems()
    self.uglySide.call('ritual_ZN19QQuickRenderControl11polishItemsEv')

  def sync(self) -> bool:
    """
    Calls Qt's 'bool QQuickRenderControl::sync()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrendercontrol.html#sync
    """
    #  bool QQuickRenderControl::sync()
    return self.uglySide.call('ritual_ZN19QQuickRenderControl4syncEv')

  def render(self) -> None:
    """
    Calls Qt's 'void QQuickRenderControl::render()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrendercontrol.html#render
    """
    #  void QQuickRenderControl::render()
    self.uglySide.call('ritual_ZN19QQuickRenderControl6renderEv')

  @overload(QPoint)
  @overload(NoneType)
  def renderWindow(self, offset: Optional[QPoint]) -> Optional[QWindow]:
    """
    Calls Qt's 'QWindow *QQuickRenderControl::renderWindow(QPoint *offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrendercontrol.html#renderWindow

    Parameters
    ----------

    offset : Optional[QPoint]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QWindow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWindow *QQuickRenderControl::renderWindow(QPoint *offset)
    ritual = 'ritual_ZN19QQuickRenderControl12renderWindowEP6QPoint'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QQuickRenderControl12renderWindowEP6QPoint'
    address = self.uglySide.call(ritual, self._addressOf(offset))
    from ..QtGui import QWindow
    return QWindow._cuteAt(address)

  def renderRequested(self) -> None:
    """
    Calls Qt's 'void QQuickRenderControl::renderRequested()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrendercontrol.html#renderRequested
    """
    #  void QQuickRenderControl::renderRequested()
    self.uglySide.call('ritual_ZN19QQuickRenderControl15renderRequestedEv')

  def sceneChanged(self) -> None:
    """
    Calls Qt's 'void QQuickRenderControl::sceneChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickrendercontrol.html#sceneChanged
    """
    #  void QQuickRenderControl::sceneChanged()
    self.uglySide.call('ritual_ZN19QQuickRenderControl12sceneChangedEv')

  def d_func(self) -> Optional[QQuickRenderControlPrivate]:
    """
    Calls Qt's 'QQuickRenderControlPrivate *QQuickRenderControl::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickrendercontrol.html#d_func

    Returns
    -------

    Optional[QQuickRenderControlPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickRenderControlPrivate *QQuickRenderControl::d_func()
    address = self.uglySide.call('ritual_ZN19QQuickRenderControl6d_funcEv')
    from . import QQuickRenderControlPrivate
    return QQuickRenderControlPrivate._cuteAt(address)
