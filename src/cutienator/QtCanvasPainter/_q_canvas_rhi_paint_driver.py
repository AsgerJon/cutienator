"""
QCanvasRhiPaintDriver binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCanvasPainter/qcanvasrhipaintdriver.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QSize
  from ..QtGui import QColor, QMatrix4x4, QRhiCommandBuffer, QRhiRenderTarget
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QMatrix4x4 = WAIT['QMatrix4x4']
  QRhiCommandBuffer = WAIT['QRhiCommandBuffer']
  QRhiRenderTarget = WAIT['QRhiRenderTarget']
  QSize = WAIT['QSize']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCanvasRhiPaintDriver(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCanvasRhiPaintDriver: a plain Python object standing
  in front of one C++ QCanvasRhiPaintDriver.

  What exists
  -----------

  Every function of Qt's QCanvasRhiPaintDriver that has a ritual and that
  Python can call so far, 4 names in all: 'resetForNewFrame', 'beginPaint',
  'endPaint', 'renderPaint'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCanvasRhiPaintDriver::~QCanvasRhiPaintDriver()': the destructor:
    Python never removes a C++ QCanvasRhiPaintDriver.
  - Qt's 'void QCanvasRhiPaintDriver::beginPaint(QCanvasOffscreenCanvas
    &canvas, QRhiCommandBuffer *cb, BeginPaintFlags flags)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void QCanvasRhiPaintDriver::grabCanvasImpl(const
    QCanvasOffscreenCanvas &canvas, const QObject *context,
    QtPrivate::QSlotObjectBase *slotObj)': names
    'QtPrivate::QSlotObjectBase', which has no cute class yet.

  What has no ritual
  ------------------

  5 of the 14 functions Qt declares: 4 forbidden; 1 a template.

  What to expect
  --------------

  - The C++ QCanvasRhiPaintDriver is created at the first use, not by
    'QCanvasRhiPaintDriver(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCanvasRhiPaintDriver.
  - Each name of Qt's QCanvasRhiPaintDriver that has no cute function yet,
    'grabCanvas', 'grabCanvasImpl', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QCanvasRhiPaintDriver, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class BeginPaintFlag(CuteFlags, scoped=True):
    """
    The flags enum 'QCanvasRhiPaintDriver::BeginPaintFlag' of Qt, with the 1
    names Qt gives in it. Qt names the type of its combinations
    'QCanvasRhiPaintDriver::BeginPaintFlags'. C++ keeps these names inside
    the enum, so the class that holds the enum does not have them.
    """

    DepthTest = 0x1

  BeginPaintFlags = BeginPaintFlag

  class EndPaintFlag(CuteFlags, scoped=True):
    """
    The flags enum 'QCanvasRhiPaintDriver::EndPaintFlag' of Qt, with the 1
    names Qt gives in it. Qt names the type of its combinations
    'QCanvasRhiPaintDriver::EndPaintFlags'. C++ keeps these names inside the
    enum, so the class that holds the enum does not have them.
    """

    DoNotRecordRenderPass = 0x1

  EndPaintFlags = EndPaintFlag

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCanvasRhiPaintDriver'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QCanvasRhiPaintDriver::QCanvasRhiPaintDriver()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasrhipaintdriver.html#QCanvasRhiPaintDriver
    """
    #  QCanvasRhiPaintDriver::QCanvasRhiPaintDriver()
    self._noteCreation(QCanvasRhiPaintDriver, lambda: Rituals.call(
        'ritual_ZN21QCanvasRhiPaintDriverC1Ev',
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

  def resetForNewFrame(self) -> None:
    """
    Calls Qt's 'void QCanvasRhiPaintDriver::resetForNewFrame()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasrhipaintdriver.html#resetForNewFrame
    """
    #  void QCanvasRhiPaintDriver::resetForNewFrame()
    self.uglySide.call(
        'ritual_ZN21QCanvasRhiPaintDriver16resetForNewFrameEv',
    )

  @overload(QRhiCommandBuffer, QRhiRenderTarget)
  @overload(QRhiCommandBuffer, NoneType)
  @overload(NoneType, QRhiRenderTarget)
  @overload(NoneType, NoneType)
  @overload(QRhiCommandBuffer, QRhiRenderTarget, QColor)
  @overload(QRhiCommandBuffer, NoneType, QColor)
  @overload(NoneType, QRhiRenderTarget, QColor)
  @overload(NoneType, NoneType, QColor)
  @overload(QRhiCommandBuffer, QRhiRenderTarget, QColor, QSize)
  @overload(QRhiCommandBuffer, NoneType, QColor, QSize)
  @overload(NoneType, QRhiRenderTarget, QColor, QSize)
  @overload(NoneType, NoneType, QColor, QSize)
  @overload(QRhiCommandBuffer, QRhiRenderTarget, QColor, QSize, float)
  @overload(QRhiCommandBuffer, NoneType, QColor, QSize, float)
  @overload(NoneType, QRhiRenderTarget, QColor, QSize, float)
  @overload(NoneType, NoneType, QColor, QSize, float)
  @overload(
      QRhiCommandBuffer, QRhiRenderTarget, QColor, QSize, float,
      BeginPaintFlags,
  )
  @overload(
      QRhiCommandBuffer, NoneType, QColor, QSize, float, BeginPaintFlags,
  )
  @overload(
      NoneType, QRhiRenderTarget, QColor, QSize, float, BeginPaintFlags,
  )
  @overload(NoneType, NoneType, QColor, QSize, float, BeginPaintFlags)
  def beginPaint(
      self,
      cb: Optional[QRhiCommandBuffer],
      rt: Optional[QRhiRenderTarget],
      fillColor: Optional[QColor] = None,
      logicalSize: Optional[QSize] = None,
      dpr: float = 1.0,
      flags: BeginPaintFlags = BeginPaintFlags(),
  ) -> None:
    """
    Calls Qt's 'void QCanvasRhiPaintDriver::beginPaint(QRhiCommandBuffer *cb,
    QRhiRenderTarget *rt, QColor fillColor, QSize logicalSize, qreal dpr,
    BeginPaintFlags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasrhipaintdriver.html#beginPaint

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rt : Optional[QRhiRenderTarget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    fillColor : Optional[QColor]
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own. May be left out, as in Qt: a new 'QColor(Qt.GlobalColor.black)' is
      then passed on.

    logicalSize : Optional[QSize]
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
      May be left out, as in Qt: a new 'QSize()' is then passed on.

    dpr : float
      Passed on as it is. May be left out, as in Qt: it is then 1.0.

    flags : BeginPaintFlags
      Passed on as its number. May be left out, as in Qt: it is then
      BeginPaintFlags().
    """
    #  void QCanvasRhiPaintDriver::beginPaint(QRhiCommandBuffer *cb,
    #      QRhiRenderTarget *rt, QColor fillColor, QSize logicalSize, qreal
    #      dpr, BeginPaintFlags flags)
    if fillColor is None:
      from ..QtGui import QColor
      fillColor = QColor(Qt.GlobalColor.black)
    if logicalSize is None:
      from ..QtCore import QSize
      logicalSize = QSize()
    self.uglySide.call(
        'ritual_ZN21QCanvasRhiPaintDriver10beginPaintEP17QRhiCommandBufferP'
        '16QRhiRenderTarget6QColor5QSized6QFlagsINS_14BeginPaintFlagEE',
        self._addressOf(cb), self._addressOf(rt), self._valueOf(fillColor),
        self._valueOf(logicalSize), dpr, flags.value,
    )

  @overload(QRhiCommandBuffer, QRhiRenderTarget, QMatrix4x4)
  @overload(QRhiCommandBuffer, NoneType, QMatrix4x4)
  @overload(NoneType, QRhiRenderTarget, QMatrix4x4)
  @overload(NoneType, NoneType, QMatrix4x4)
  @overload(QRhiCommandBuffer, QRhiRenderTarget, QMatrix4x4, BeginPaintFlags)
  @overload(QRhiCommandBuffer, NoneType, QMatrix4x4, BeginPaintFlags)
  @overload(NoneType, QRhiRenderTarget, QMatrix4x4, BeginPaintFlags)
  @overload(NoneType, NoneType, QMatrix4x4, BeginPaintFlags)
  def beginPaint(
      self,
      cb: Optional[QRhiCommandBuffer],
      rt: Optional[QRhiRenderTarget],
      matrix: QMatrix4x4,
      flags: BeginPaintFlags = BeginPaintFlags(),
  ) -> None:
    """
    Calls Qt's 'void QCanvasRhiPaintDriver::beginPaint(QRhiCommandBuffer *cb,
    QRhiRenderTarget *rt, const QMatrix4x4 &matrix, BeginPaintFlags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasrhipaintdriver.html#beginPaint

    Parameters
    ----------

    cb : Optional[QRhiCommandBuffer]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    rt : Optional[QRhiRenderTarget]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    matrix : QMatrix4x4
      Passed on as a value: Qt reads the C++ QMatrix4x4, which stays Python's
      own.

    flags : BeginPaintFlags
      Passed on as its number. May be left out, as in Qt: it is then
      BeginPaintFlags().
    """
    #  void QCanvasRhiPaintDriver::beginPaint(QRhiCommandBuffer *cb,
    #      QRhiRenderTarget *rt, const QMatrix4x4 &matrix, BeginPaintFlags
    #      flags)
    self.uglySide.call(
        'ritual_ZN21QCanvasRhiPaintDriver10beginPaintEP17QRhiCommandBufferP'
        '16QRhiRenderTargetRK10QMatrix4x46QFlagsINS_14BeginPaintFlagEE',
        self._addressOf(cb), self._addressOf(rt), self._valueOf(matrix),
        flags.value,
    )

  @overload()
  @overload(EndPaintFlags)
  def endPaint(self, flags: EndPaintFlags = EndPaintFlags()) -> None:
    """
    Calls Qt's 'void QCanvasRhiPaintDriver::endPaint(EndPaintFlags flags)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasrhipaintdriver.html#endPaint

    Parameters
    ----------

    flags : EndPaintFlags
      Passed on as its number. May be left out, as in Qt: it is then
      EndPaintFlags().
    """
    #  void QCanvasRhiPaintDriver::endPaint(EndPaintFlags flags)
    self.uglySide.call(
        'ritual_ZN21QCanvasRhiPaintDriver8endPaintE6QFlagsINS_12EndPaintFla'
        'gEE',
        flags.value,
    )

  def renderPaint(self) -> None:
    """
    Calls Qt's 'void QCanvasRhiPaintDriver::renderPaint()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanvasrhipaintdriver.html#renderPaint
    """
    #  void QCanvasRhiPaintDriver::renderPaint()
    self.uglySide.call('ritual_ZN21QCanvasRhiPaintDriver11renderPaintEv')

  @staticmethod
  def grabCanvas(*__, **_) -> Never:
    """
    Qt's 'QCanvasRhiPaintDriver::grabCanvas': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QCanvasRhiPaintDriver.grabCanvas' has no cute function yet. Qt's "
        "'QCanvasRhiPaintDriver::grabCanvas': a template: a pattern and no "
        "single function.")

  @staticmethod
  def grabCanvasImpl(*__, **_) -> Never:
    """
    Qt's 'void QCanvasRhiPaintDriver::grabCanvasImpl(const
    QCanvasOffscreenCanvas &canvas, const QObject *context,
    QtPrivate::QSlotObjectBase *slotObj)': names
    'QtPrivate::QSlotObjectBase', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QCanvasRhiPaintDriver.grabCanvasImpl' has no cute function yet. "
        "Qt's 'void QCanvasRhiPaintDriver::grabCanvasImpl(const "
        "QCanvasOffscreenCanvas &canvas, const QObject *context, "
        "QtPrivate::QSlotObjectBase *slotObj)': names "
        "'QtPrivate::QSlotObjectBase', which has no cute class yet.")
