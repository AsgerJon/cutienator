"""
QQuickContext2D binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickcontext2d_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QQuickContext2D to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QMap, QStringList
from ..QtQml import QV4
from . import QQuickCanvasContext

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPointF, QRect, QRectF, QSize, QThread
  from ..QtCore import QVariant
  from ..QtGui import QImage, QPainterPath, QSurface
  from . import QQuickCanvasItem, QQuickContext2DCommandBuffer
  from . import QQuickContext2DTexture
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QImage = WAIT['QImage']
  QPointF = WAIT['QPointF']
  QQuickCanvasItem = WAIT['QQuickCanvasItem']
  QRect = WAIT['QRect']
  QRectF = WAIT['QRectF']
  QSize = WAIT['QSize']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickContext2D(QQuickCanvasContext):
  """
  The cute side of Qt's QQuickContext2D: a plain Python object standing in
  front of one C++ QQuickContext2D.

  It is built on the cute 'QQuickCanvasContext', as Qt's QQuickContext2D is
  built on Qt's QQuickCanvasContext, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickContext2D that has a ritual and that Python
  can call so far, 46 names in all: 'metaObject', 'contextNames', 'init',
  'prepare', 'flush', 'thread', 'texture', 'toImage', 'v4value', 'v4Engine',
  'setV4Engine', 'canvas', 'buffer', 'bufferValid', 'popState', 'pushState',
  'reset', 'fill', 'clip', 'stroke', 'fillRect', 'strokeRect', 'clearRect',
  'drawText', 'scale', 'rotate', 'shear', 'translate', 'transform',
  'setTransform', 'beginPath', 'closePath', 'moveTo', 'lineTo',
  'quadraticCurveTo', 'bezierCurveTo', 'arcTo', 'rect', 'roundedRect',
  'ellipse', 'text', 'arc', 'addArcTo', 'createTextGlyphs', 'surface',
  'setGrabbedImage'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickContext2D::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuickContext2D::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickContext2D::~QQuickContext2D()': the destructor: Python never
    removes a C++ QQuickContext2D.

  What has no ritual
  ------------------

  9 of the 58 functions Qt declares: 2 not a gap; 2 forbidden; 2 leans on
  'QQuickContext2D; 1 cannot be called and cannot be called through the
  meta-object and cannot be copied; 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 leans on
  'QQuickCanvasItem.

  What to expect
  --------------

  - The C++ QQuickContext2D is created at the first use, not by
    'QQuickContext2D(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickContext2D.
  - Qt tells when it has removed the C++ QQuickContext2D. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickContext2D that has no cute function yet,
    '__init__', 'createPixmap', 'isPointInPath', 'sync', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuickContext2D, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class PaintCommand(CuteNum):
    """
    The enum 'QQuickContext2D::PaintCommand' of Qt, with the 31 names Qt
    gives in it.
    """

    Invalid = Kee[int](0)
    UpdateMatrix = Kee[int](1)
    ClearRect = Kee[int](2)
    FillRect = Kee[int](3)
    StrokeRect = Kee[int](4)
    Fill = Kee[int](5)
    Stroke = Kee[int](6)
    Clip = Kee[int](7)
    UpdateBrush = Kee[int](8)
    GlobalAlpha = Kee[int](9)
    GlobalCompositeOperation = Kee[int](10)
    StrokeStyle = Kee[int](11)
    FillStyle = Kee[int](12)
    LineWidth = Kee[int](13)
    LineCap = Kee[int](14)
    LineJoin = Kee[int](15)
    LineDash = Kee[int](16)
    LineDashOffset = Kee[int](17)
    MiterLimit = Kee[int](18)
    ShadowOffsetX = Kee[int](19)
    ShadowOffsetY = Kee[int](20)
    ShadowBlur = Kee[int](21)
    ShadowColor = Kee[int](22)
    Font = Kee[int](23)
    TextBaseline = Kee[int](24)
    TextAlign = Kee[int](25)
    FillText = Kee[int](26)
    StrokeText = Kee[int](27)
    DrawImage = Kee[int](28)
    DrawPixmap = Kee[int](29)
    GetImageData = Kee[int](30)

  class TextAlignType(CuteNum):
    """
    The enum 'QQuickContext2D::TextAlignType' of Qt, with the 5 names Qt
    gives in it.
    """

    Start = Kee[int](0)
    End = Kee[int](1)
    Left = Kee[int](2)
    Right = Kee[int](3)
    Center = Kee[int](4)

  class TextBaseLineType(CuteNum):
    """
    The enum 'QQuickContext2D::TextBaseLineType' of Qt, with the 5 names Qt
    gives in it.
    """

    Alphabetic = Kee[int](0)
    Top = Kee[int](1)
    Middle = Kee[int](2)
    Bottom = Kee[int](3)
    Hanging = Kee[int](4)

  #  The classes Qt writes inside QQuickContext2D, each a class in here as in
  #  C++.

  class State(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuickContext2D::State: a plain Python object
    standing in front of one C++ QQuickContext2D::State.

    C++ hands a QQuickContext2D::State around as a copy, so every C++
    QQuickContext2D::State behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QQuickContext2D::State yet. It can be made from
    Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuickContext2D::State::~State()': the destructor: Python removes
      its C++ QQuickContext2D::State by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QQuickContext2D::State is created at the first use, not by
      'QQuickContext2D::State(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuickContext2D::State back gives a copy the ritual
      made for Python, in a new cute QQuickContext2D::State.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuickContext2D::State'

    #  Qt's '~QQuickContext2D::State()'. Naming it makes this a value class:
    #  Python owns every C++ QQuickContext2D::State behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN15QQuickContext2D5StateD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's 'QQuickContext2D::State::State()', which
      is called at the first use.

      Qt's own words: https://doc.qt.io/qt-6/qquickcontext2d-state.html#State
      """
      #  QQuickContext2D::State::State()
      self._noteCreation(QQuickContext2D.State, lambda: Rituals.call(
          'ritual_ZN15QQuickContext2D5StateC1Ev',
      ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickContext2D'

  #  A C++ QQuickContext2D Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickContext2D'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickContext2D::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontext2d.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickContext2D::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QQuickContext2D10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def contextNames(self) -> QStringList:
    """
    Calls Qt's 'QStringList QQuickContext2D::contextNames() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontext2d.html#contextNames

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQuickContext2D::contextNames() const
    address = self.uglySide.call(
        'ritual_ZNK15QQuickContext2D12contextNamesEv',
    )
    return QStringList._cuteOwning(address)

  def thread(self) -> Optional[QThread]:
    """
    Calls Qt's 'QThread *QQuickContext2D::thread() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontext2d.html#thread

    Returns
    -------

    Optional[QThread]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QThread *QQuickContext2D::thread() const
    address = self.uglySide.call('ritual_ZNK15QQuickContext2D6threadEv')
    from ..QtCore import QThread
    return QThread._cuteAt(address)

  def texture(self) -> Optional[QQuickContext2DTexture]:
    """
    Calls Qt's 'QQuickContext2DTexture *QQuickContext2D::texture() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontext2d.html#texture

    Returns
    -------

    Optional[QQuickContext2DTexture]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickContext2DTexture *QQuickContext2D::texture() const
    address = self.uglySide.call('ritual_ZNK15QQuickContext2D7textureEv')
    from . import QQuickContext2DTexture
    return QQuickContext2DTexture._cuteAt(address)

  def v4value(self) -> int:
    """
    Calls Qt's 'QV4::ReturnedValue QQuickContext2D::v4value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontext2d.html#v4value
    """
    #  QV4::ReturnedValue QQuickContext2D::v4value() const
    ritual = 'ritual_ZNK15QQuickContext2D7v4valueEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QQuickContext2D7v4valueEv'
    return self.uglySide.call(ritual)

  def v4Engine(self) -> Optional[QV4.ExecutionEngine]:
    """
    Calls Qt's 'QV4::ExecutionEngine *QQuickContext2D::v4Engine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontext2d.html#v4Engine

    Returns
    -------

    Optional[QV4.ExecutionEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QV4::ExecutionEngine *QQuickContext2D::v4Engine() const
    ritual = 'ritual_ZNK15QQuickContext2D8v4EngineEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK15QQuickContext2D8v4EngineEv'
    address = self.uglySide.call(ritual)
    return QV4.ExecutionEngine._cuteAt(address)

  def canvas(self) -> Optional[QQuickCanvasItem]:
    """
    Calls Qt's 'QQuickCanvasItem *QQuickContext2D::canvas() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontext2d.html#canvas

    Returns
    -------

    Optional[QQuickCanvasItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickCanvasItem *QQuickContext2D::canvas() const
    address = self.uglySide.call('ritual_ZNK15QQuickContext2D6canvasEv')
    from . import QQuickCanvasItem
    return QQuickCanvasItem._cuteAt(address)

  def buffer(self) -> Optional[QQuickContext2DCommandBuffer]:
    """
    Calls Qt's 'QQuickContext2DCommandBuffer *QQuickContext2D::buffer()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontext2d.html#buffer

    Returns
    -------

    Optional[QQuickContext2DCommandBuffer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuickContext2DCommandBuffer *QQuickContext2D::buffer() const
    address = self.uglySide.call('ritual_ZNK15QQuickContext2D6bufferEv')
    from . import QQuickContext2DCommandBuffer
    return QQuickContext2DCommandBuffer._cuteAt(address)

  def bufferValid(self) -> bool:
    """
    Calls Qt's 'bool QQuickContext2D::bufferValid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontext2d.html#bufferValid
    """
    #  bool QQuickContext2D::bufferValid() const
    return self.uglySide.call('ritual_ZNK15QQuickContext2D11bufferValidEv')

  def surface(self) -> Optional[QSurface]:
    """
    Calls Qt's 'QSurface *QQuickContext2D::surface() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontext2d.html#surface

    Returns
    -------

    Optional[QSurface]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSurface *QQuickContext2D::surface() const
    address = self.uglySide.call('ritual_ZNK15QQuickContext2D7surfaceEv')
    from ..QtGui import QSurface
    return QSurface._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['QV4.ExecutionEngine'])
  @overload(NoneType)
  def setV4Engine(self, eng: Optional[QV4.ExecutionEngine]) -> None:
    """
    Calls Qt's 'void QQuickContext2D::setV4Engine(QV4::ExecutionEngine
    *eng)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontext2d.html#setV4Engine

    Parameters
    ----------

    eng : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickContext2D::setV4Engine(QV4::ExecutionEngine *eng)
    self.uglySide.call(
        'ritual_ZN15QQuickContext2D11setV4EngineEPN3QV415ExecutionEngineE',
        self._addressOf(eng),
    )

  @overload(float, float, float, float, float, float)
  def setTransform(
      self,
      a: float,
      b: float,
      c: float,
      d: float,
      e: float,
      f: float,
  ) -> None:
    """
    Calls Qt's 'void QQuickContext2D::setTransform(qreal a, qreal b, qreal c,
    qreal d, qreal e, qreal f)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontext2d.html#setTransform

    Parameters
    ----------

    a : float
      Passed on as it is.

    b : float
      Passed on as it is.

    c : float
      Passed on as it is.

    d : float
      Passed on as it is.

    e : float
      Passed on as it is.

    f : float
      Passed on as it is.
    """
    #  void QQuickContext2D::setTransform(qreal a, qreal b, qreal c, qreal d,
    #      qreal e, qreal f)
    self.uglySide.call(
        'ritual_ZN15QQuickContext2D12setTransformEdddddd', a, b, c, d, e, f,
    )

  @overload(QImage)
  def setGrabbedImage(self, grab: QImage) -> None:
    """
    Calls Qt's 'void QQuickContext2D::setGrabbedImage(const QImage &grab)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2d.html#setGrabbedImage

    Parameters
    ----------

    grab : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  void QQuickContext2D::setGrabbedImage(const QImage &grab)
    self.uglySide.call(
        'ritual_ZN15QQuickContext2D15setGrabbedImageERK6QImage',
        self._valueOf(grab),
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQuickContext2D::QQuickContext2D(QObject *parent)': leans on
    'QQuickContext2D::qt_metacall(QMetaObject::Call, int, void**)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQuickContext2D.__init__' has no cute function yet. Qt's "
        "'QQuickContext2D::QQuickContext2D(QObject *parent)': leans on "
        "'QQuickContext2D::qt_metacall(QMetaObject::Call, int, void**)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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

  @overload(QQuickCanvasItem, QMap[str, QVariant])
  @overload(NoneType, QMap[str, QVariant])
  def init(
      self,
      canvasItem: Optional[QQuickCanvasItem],
      args: QMap[str, QVariant],
  ) -> None:
    """
    Calls Qt's 'void QQuickContext2D::init(QQuickCanvasItem *canvasItem,
    const QVariantMap &args)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontext2d.html#init

    Parameters
    ----------

    canvasItem : Optional[QQuickCanvasItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    args : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void QQuickContext2D::init(QQuickCanvasItem *canvasItem, const
    #      QVariantMap &args)
    self.uglySide.call(
        'ritual_ZN15QQuickContext2D4initEP16QQuickCanvasItemRK4QMapI7QStrin'
        'g8QVariantE',
        self._addressOf(canvasItem), self._valueOf(args),
    )

  @overload(QSize, QSize, QRect, QRect, bool, bool)
  def prepare(
      self,
      canvasSize: QSize,
      tileSize: QSize,
      canvasWindow: QRect,
      dirtyRect: QRect,
      smooth: bool,
      antialiasing: bool,
  ) -> None:
    """
    Calls Qt's 'void QQuickContext2D::prepare(const QSize &canvasSize, const
    QSize &tileSize, const QRect &canvasWindow, const QRect &dirtyRect, bool
    smooth, bool antialiasing)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontext2d.html#prepare

    Parameters
    ----------

    canvasSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    tileSize : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.

    canvasWindow : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    dirtyRect : QRect
      Passed on as a value: Qt reads the C++ QRect, which stays Python's own.

    smooth : bool
      Passed on as it is.

    antialiasing : bool
      Passed on as it is.
    """
    #  void QQuickContext2D::prepare(const QSize &canvasSize, const QSize
    #      &tileSize, const QRect &canvasWindow, const QRect &dirtyRect, bool
    #      smooth, bool antialiasing)
    self.uglySide.call(
        'ritual_ZN15QQuickContext2D7prepareERK5QSizeS2_RK5QRectS5_bb',
        self._valueOf(canvasSize), self._valueOf(tileSize),
        self._valueOf(canvasWindow), self._valueOf(dirtyRect), smooth,
        antialiasing,
    )

  def flush(self) -> None:
    """
    Calls Qt's 'void QQuickContext2D::flush()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontext2d.html#flush
    """
    #  void QQuickContext2D::flush()
    self.uglySide.call('ritual_ZN15QQuickContext2D5flushEv')

  @overload(QRectF)
  def toImage(self, bounds: QRectF) -> QImage:
    """
    Calls Qt's 'QImage QQuickContext2D::toImage(const QRectF &bounds)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontext2d.html#toImage

    Parameters
    ----------

    bounds : QRectF
      Passed on as a value: Qt reads the C++ QRectF, which stays Python's
      own.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QQuickContext2D::toImage(const QRectF &bounds)
    ritual = 'ritual_ZN15QQuickContext2D7toImageERK6QRectF'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN15QQuickContext2D7toImageERK6QRectF'
    address = self.uglySide.call(ritual, self._valueOf(bounds))
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  def popState(self) -> None:
    """
    Calls Qt's 'void QQuickContext2D::popState()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontext2d.html#popState
    """
    #  void QQuickContext2D::popState()
    self.uglySide.call('ritual_ZN15QQuickContext2D8popStateEv')

  def pushState(self) -> None:
    """
    Calls Qt's 'void QQuickContext2D::pushState()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontext2d.html#pushState
    """
    #  void QQuickContext2D::pushState()
    self.uglySide.call('ritual_ZN15QQuickContext2D9pushStateEv')

  def reset(self) -> None:
    """
    Calls Qt's 'void QQuickContext2D::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontext2d.html#reset
    """
    #  void QQuickContext2D::reset()
    self.uglySide.call('ritual_ZN15QQuickContext2D5resetEv')

  def fill(self) -> None:
    """
    Calls Qt's 'void QQuickContext2D::fill()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontext2d.html#fill
    """
    #  void QQuickContext2D::fill()
    self.uglySide.call('ritual_ZN15QQuickContext2D4fillEv')

  def clip(self) -> None:
    """
    Calls Qt's 'void QQuickContext2D::clip()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontext2d.html#clip
    """
    #  void QQuickContext2D::clip()
    self.uglySide.call('ritual_ZN15QQuickContext2D4clipEv')

  def stroke(self) -> None:
    """
    Calls Qt's 'void QQuickContext2D::stroke()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontext2d.html#stroke
    """
    #  void QQuickContext2D::stroke()
    self.uglySide.call('ritual_ZN15QQuickContext2D6strokeEv')

  @overload(float, float, float, float)
  def fillRect(self, x: float, y: float, w: float, h: float) -> None:
    """
    Calls Qt's 'void QQuickContext2D::fillRect(qreal x, qreal y, qreal w,
    qreal h)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontext2d.html#fillRect

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    w : float
      Passed on as it is.

    h : float
      Passed on as it is.
    """
    #  void QQuickContext2D::fillRect(qreal x, qreal y, qreal w, qreal h)
    self.uglySide.call(
        'ritual_ZN15QQuickContext2D8fillRectEdddd', x, y, w, h,
    )

  @overload(float, float, float, float)
  def strokeRect(self, x: float, y: float, w: float, h: float) -> None:
    """
    Calls Qt's 'void QQuickContext2D::strokeRect(qreal x, qreal y, qreal w,
    qreal h)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontext2d.html#strokeRect

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    w : float
      Passed on as it is.

    h : float
      Passed on as it is.
    """
    #  void QQuickContext2D::strokeRect(qreal x, qreal y, qreal w, qreal h)
    self.uglySide.call(
        'ritual_ZN15QQuickContext2D10strokeRectEdddd', x, y, w, h,
    )

  @overload(float, float, float, float)
  def clearRect(self, x: float, y: float, w: float, h: float) -> None:
    """
    Calls Qt's 'void QQuickContext2D::clearRect(qreal x, qreal y, qreal w,
    qreal h)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontext2d.html#clearRect

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    w : float
      Passed on as it is.

    h : float
      Passed on as it is.
    """
    #  void QQuickContext2D::clearRect(qreal x, qreal y, qreal w, qreal h)
    self.uglySide.call(
        'ritual_ZN15QQuickContext2D9clearRectEdddd', x, y, w, h,
    )

  @overload(str, float, float, bool)
  def drawText(self, text: str, x: float, y: float, fill: bool) -> None:
    """
    Calls Qt's 'void QQuickContext2D::drawText(const QString &text, qreal x,
    qreal y, bool fill)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontext2d.html#drawText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    fill : bool
      Passed on as it is.
    """
    #  void QQuickContext2D::drawText(const QString &text, qreal x, qreal y,
    #      bool fill)
    self.uglySide.call(
        'ritual_ZN15QQuickContext2D8drawTextERK7QStringddb',
        text, x, y, fill,
    )

  @overload(float, float)
  def scale(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QQuickContext2D::scale(qreal x, qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontext2d.html#scale

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QQuickContext2D::scale(qreal x, qreal y)
    self.uglySide.call('ritual_ZN15QQuickContext2D5scaleEdd', x, y)

  @overload(float)
  def rotate(self, angle: float) -> None:
    """
    Calls Qt's 'void QQuickContext2D::rotate(qreal angle)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontext2d.html#rotate

    Parameters
    ----------

    angle : float
      Passed on as it is.
    """
    #  void QQuickContext2D::rotate(qreal angle)
    self.uglySide.call('ritual_ZN15QQuickContext2D6rotateEd', angle)

  @overload(float, float)
  def shear(self, h: float, v: float) -> None:
    """
    Calls Qt's 'void QQuickContext2D::shear(qreal h, qreal v)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontext2d.html#shear

    Parameters
    ----------

    h : float
      Passed on as it is.

    v : float
      Passed on as it is.
    """
    #  void QQuickContext2D::shear(qreal h, qreal v)
    self.uglySide.call('ritual_ZN15QQuickContext2D5shearEdd', h, v)

  @overload(float, float)
  def translate(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QQuickContext2D::translate(qreal x, qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontext2d.html#translate

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QQuickContext2D::translate(qreal x, qreal y)
    self.uglySide.call('ritual_ZN15QQuickContext2D9translateEdd', x, y)

  @overload(float, float, float, float, float, float)
  def transform(
      self,
      a: float,
      b: float,
      c: float,
      d: float,
      e: float,
      f: float,
  ) -> None:
    """
    Calls Qt's 'void QQuickContext2D::transform(qreal a, qreal b, qreal c,
    qreal d, qreal e, qreal f)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontext2d.html#transform

    Parameters
    ----------

    a : float
      Passed on as it is.

    b : float
      Passed on as it is.

    c : float
      Passed on as it is.

    d : float
      Passed on as it is.

    e : float
      Passed on as it is.

    f : float
      Passed on as it is.
    """
    #  void QQuickContext2D::transform(qreal a, qreal b, qreal c, qreal d,
    #      qreal e, qreal f)
    self.uglySide.call(
        'ritual_ZN15QQuickContext2D9transformEdddddd', a, b, c, d, e, f,
    )

  def beginPath(self) -> None:
    """
    Calls Qt's 'void QQuickContext2D::beginPath()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontext2d.html#beginPath
    """
    #  void QQuickContext2D::beginPath()
    self.uglySide.call('ritual_ZN15QQuickContext2D9beginPathEv')

  def closePath(self) -> None:
    """
    Calls Qt's 'void QQuickContext2D::closePath()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontext2d.html#closePath
    """
    #  void QQuickContext2D::closePath()
    self.uglySide.call('ritual_ZN15QQuickContext2D9closePathEv')

  @overload(float, float)
  def moveTo(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QQuickContext2D::moveTo(qreal x, qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontext2d.html#moveTo

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QQuickContext2D::moveTo(qreal x, qreal y)
    self.uglySide.call('ritual_ZN15QQuickContext2D6moveToEdd', x, y)

  @overload(float, float)
  def lineTo(self, x: float, y: float) -> None:
    """
    Calls Qt's 'void QQuickContext2D::lineTo(qreal x, qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontext2d.html#lineTo

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QQuickContext2D::lineTo(qreal x, qreal y)
    self.uglySide.call('ritual_ZN15QQuickContext2D6lineToEdd', x, y)

  @overload(float, float, float, float)
  def quadraticCurveTo(
      self,
      cpx: float,
      cpy: float,
      x: float,
      y: float,
  ) -> None:
    """
    Calls Qt's 'void QQuickContext2D::quadraticCurveTo(qreal cpx, qreal cpy,
    qreal x, qreal y)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2d.html#quadraticCurveTo

    Parameters
    ----------

    cpx : float
      Passed on as it is.

    cpy : float
      Passed on as it is.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QQuickContext2D::quadraticCurveTo(qreal cpx, qreal cpy, qreal x,
    #      qreal y)
    self.uglySide.call(
        'ritual_ZN15QQuickContext2D16quadraticCurveToEdddd', cpx, cpy, x, y,
    )

  @overload(float, float, float, float, float, float)
  def bezierCurveTo(
      self,
      cp1x: float,
      cp1y: float,
      cp2x: float,
      cp2y: float,
      x: float,
      y: float,
  ) -> None:
    """
    Calls Qt's 'void QQuickContext2D::bezierCurveTo(qreal cp1x, qreal cp1y,
    qreal cp2x, qreal cp2y, qreal x, qreal y)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontext2d.html#bezierCurveTo

    Parameters
    ----------

    cp1x : float
      Passed on as it is.

    cp1y : float
      Passed on as it is.

    cp2x : float
      Passed on as it is.

    cp2y : float
      Passed on as it is.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QQuickContext2D::bezierCurveTo(qreal cp1x, qreal cp1y, qreal
    #      cp2x, qreal cp2y, qreal x, qreal y)
    self.uglySide.call(
        'ritual_ZN15QQuickContext2D13bezierCurveToEdddddd',
        cp1x, cp1y, cp2x, cp2y, x, y,
    )

  @overload(float, float, float, float, float)
  def arcTo(
      self,
      x1: float,
      y1: float,
      x2: float,
      y2: float,
      radius: float,
  ) -> None:
    """
    Calls Qt's 'void QQuickContext2D::arcTo(qreal x1, qreal y1, qreal x2,
    qreal y2, qreal radius)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontext2d.html#arcTo

    Parameters
    ----------

    x1 : float
      Passed on as it is.

    y1 : float
      Passed on as it is.

    x2 : float
      Passed on as it is.

    y2 : float
      Passed on as it is.

    radius : float
      Passed on as it is.
    """
    #  void QQuickContext2D::arcTo(qreal x1, qreal y1, qreal x2, qreal y2,
    #      qreal radius)
    self.uglySide.call(
        'ritual_ZN15QQuickContext2D5arcToEddddd', x1, y1, x2, y2, radius,
    )

  @overload(float, float, float, float)
  def rect(self, x: float, y: float, w: float, h: float) -> None:
    """
    Calls Qt's 'void QQuickContext2D::rect(qreal x, qreal y, qreal w, qreal
    h)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontext2d.html#rect

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    w : float
      Passed on as it is.

    h : float
      Passed on as it is.
    """
    #  void QQuickContext2D::rect(qreal x, qreal y, qreal w, qreal h)
    self.uglySide.call('ritual_ZN15QQuickContext2D4rectEdddd', x, y, w, h)

  @overload(float, float, float, float, float, float)
  def roundedRect(
      self,
      x: float,
      y: float,
      w: float,
      h: float,
      xr: float,
      yr: float,
  ) -> None:
    """
    Calls Qt's 'void QQuickContext2D::roundedRect(qreal x, qreal y, qreal w,
    qreal h, qreal xr, qreal yr)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontext2d.html#roundedRect

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    w : float
      Passed on as it is.

    h : float
      Passed on as it is.

    xr : float
      Passed on as it is.

    yr : float
      Passed on as it is.
    """
    #  void QQuickContext2D::roundedRect(qreal x, qreal y, qreal w, qreal h,
    #      qreal xr, qreal yr)
    self.uglySide.call(
        'ritual_ZN15QQuickContext2D11roundedRectEdddddd', x, y, w, h, xr, yr,
    )

  @overload(float, float, float, float)
  def ellipse(self, x: float, y: float, w: float, h: float) -> None:
    """
    Calls Qt's 'void QQuickContext2D::ellipse(qreal x, qreal y, qreal w,
    qreal h)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontext2d.html#ellipse

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    w : float
      Passed on as it is.

    h : float
      Passed on as it is.
    """
    #  void QQuickContext2D::ellipse(qreal x, qreal y, qreal w, qreal h)
    self.uglySide.call('ritual_ZN15QQuickContext2D7ellipseEdddd', x, y, w, h)

  @overload(str, float, float)
  def text(self, str: str, x: float, y: float) -> None:
    """
    Calls Qt's 'void QQuickContext2D::text(const QString &str, qreal x, qreal
    y)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontext2d.html#text

    Parameters
    ----------

    str : str
      Passed on as it is: a QString is made of it for the call.

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.
    """
    #  void QQuickContext2D::text(const QString &str, qreal x, qreal y)
    self.uglySide.call(
        'ritual_ZN15QQuickContext2D4textERK7QStringdd', str, x, y,
    )

  @overload(float, float, float, float, float, bool)
  def arc(
      self,
      x: float,
      y: float,
      radius: float,
      startAngle: float,
      endAngle: float,
      anticlockwise: bool,
  ) -> None:
    """
    Calls Qt's 'void QQuickContext2D::arc(qreal x, qreal y, qreal radius,
    qreal startAngle, qreal endAngle, bool anticlockwise)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontext2d.html#arc

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    radius : float
      Passed on as it is.

    startAngle : float
      Passed on as it is.

    endAngle : float
      Passed on as it is.

    anticlockwise : bool
      Passed on as it is.
    """
    #  void QQuickContext2D::arc(qreal x, qreal y, qreal radius, qreal
    #      startAngle, qreal endAngle, bool anticlockwise)
    self.uglySide.call(
        'ritual_ZN15QQuickContext2D3arcEdddddb',
        x, y, radius, startAngle, endAngle, anticlockwise,
    )

  @overload(QPointF, QPointF, float)
  def addArcTo(self, p1: QPointF, p2: QPointF, radius: float) -> None:
    """
    Calls Qt's 'void QQuickContext2D::addArcTo(const QPointF &p1, const
    QPointF &p2, qreal radius)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickcontext2d.html#addArcTo

    Parameters
    ----------

    p1 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    p2 : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.

    radius : float
      Passed on as it is.
    """
    #  void QQuickContext2D::addArcTo(const QPointF &p1, const QPointF &p2,
    #      qreal radius)
    self.uglySide.call(
        'ritual_ZN15QQuickContext2D8addArcToERK7QPointFS2_d',
        self._valueOf(p1, 'QPointF'), self._valueOf(p2, 'QPointF'), radius,
    )

  @overload(float, float, str)
  def createTextGlyphs(self, x: float, y: float, text: str) -> QPainterPath:
    """
    Calls Qt's 'QPainterPath QQuickContext2D::createTextGlyphs(qreal x, qreal
    y, const QString &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickcontext2d.html#createTextGlyphs

    Parameters
    ----------

    x : float
      Passed on as it is.

    y : float
      Passed on as it is.

    text : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QPainterPath
      A new cute QPainterPath around the copy Qt gave back. Python owns it.
    """
    #  QPainterPath QQuickContext2D::createTextGlyphs(qreal x, qreal y, const
    #      QString &text)
    address = self.uglySide.call(
        'ritual_ZN15QQuickContext2D16createTextGlyphsEddRK7QString',
        x, y, text,
    )
    from ..QtGui import QPainterPath
    return QPainterPath._cuteOwning(address)

  @staticmethod
  def createPixmap(*__, **_) -> Never:
    """
    Qt's 'QQmlRefPointer<QQuickCanvasPixmap>
    QQuickContext2D::createPixmap(const QUrl &url, QSizeF sourceSize)': leans
    on 'QQuickCanvasItem::loadedPixmap(QUrl const&, QSizeF)', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuickContext2D.createPixmap' has no cute function yet. Qt's "
        "'QQmlRefPointer<QQuickCanvasPixmap> "
        "QQuickContext2D::createPixmap(const QUrl &url, QSizeF "
        "sourceSize)': leans on 'QQuickCanvasItem::loadedPixmap(QUrl "
        "const&, QSizeF)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def isPointInPath(*__, **_) -> Never:
    """
    Qt's 'bool QQuickContext2D::isPointInPath(qreal x, qreal y) const': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'withinRange'.
    """
    raise NotImplementedError(
        "'QQuickContext2D.isPointInPath' has no cute function yet. Qt's "
        "'bool QQuickContext2D::isPointInPath(qreal x, qreal y) const': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'withinRange'.")

  @staticmethod
  def sync(*__, **_) -> Never:
    """
    Qt's 'void QQuickContext2D::sync()': cannot be called and cannot be
    called through the meta-object and cannot be copied: no header file has
    its code, Qt's source does not mark it or its class for use from outside
    Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QQuickContext2D.sync' has no cute function yet. Qt's 'void "
        "QQuickContext2D::sync()': cannot be called and cannot be called "
        "through the meta-object and cannot be copied: no header file has "
        "its code, Qt's source does not mark it or its class for use from "
        "outside Qt or writes it 'inline' or nowhere, and it is no signal, "
        "slot or invokable function giving back nothing, of a class built "
        "on QObject, and Qt's source has no code for it that could be told "
        "from the rest.")
