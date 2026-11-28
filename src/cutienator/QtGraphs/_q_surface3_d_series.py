"""
QSurface3DSeries binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/qsurface3dseries.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QAbstract3DSeries

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QPoint
  from ..QtGui import QColor, QImage
  from . import QSurface3DSeriesPrivate, QSurfaceDataProxy, QValue3DAxis
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QImage = WAIT['QImage']
  QPoint = WAIT['QPoint']
  QSurfaceDataProxy = WAIT['QtGraphs:QSurfaceDataProxy']
  QValue3DAxis = WAIT['QtGraphs:QValue3DAxis']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSurface3DSeries(QAbstract3DSeries):
  """
  The cute side of Qt's QSurface3DSeries: a plain Python object standing in
  front of one C++ QSurface3DSeries.

  It is built on the cute 'QAbstract3DSeries', as Qt's QSurface3DSeries is
  built on Qt's QAbstract3DSeries, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSurface3DSeries that has a ritual and that Python
  can call so far, 42 names in all: 'metaObject', 'tr', 'd_func',
  'setDataProxy', 'dataProxy', 'setSelectedPoint', 'selectedPoint',
  'invalidSelectionPosition', 'shading', 'setDrawMode', 'drawMode',
  'isFlatShadingSupported', 'setTexture', 'texture', 'setTextureFile',
  'textureFile', 'setWireframeColor', 'wireframeColor', 'setRowsSanitized',
  'rowsSanitized', 'clearRow', 'clearArray', 'setAxisX', 'setAxisY',
  'setAxisZ', 'axisX', 'axisY', 'axisZ', 'resetAxisX', 'resetAxisY',
  'resetAxisZ', 'dataProxyChanged', 'selectedPointChanged',
  'flatShadingSupportedChanged', 'drawModeChanged', 'textureChanged',
  'textureFileChanged', 'wireframeColorChanged', 'rowsSanitizedChanged',
  'axisXChanged', 'axisYChanged', 'axisZChanged'. It can be made from Python,
  in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSurface3DSeries::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QSurface3DSeries::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'const QSurface3DSeriesPrivate *QSurface3DSeries::d_func() const':
    takes in Python what 'QSurface3DSeriesPrivate
    *QSurface3DSeries::d_func()' takes.
  - Qt's 'void QSurface3DSeries::qt_qmlMarker_uncreatable()': one of Qt's own
    inner workings.
  - Qt's 'QSurface3DSeries::~QSurface3DSeries()': the destructor: Python
    never removes a C++ QSurface3DSeries.
  - Qt's 'void QSurface3DSeries::setShading(const QSurface3DSeries::Shading
    shading)': takes a type Python has no way to hand over yet.
  - Qt's 'void QSurface3DSeries::setDataArray(const QSurfaceDataArray
    &newDataArray)': takes a type Python has no way to hand over yet.
  - Qt's 'const QSurfaceDataArray &QSurface3DSeries::dataArray() const':
    gives a type Python has no way to take yet.
  - Qt's 'void QSurface3DSeries::dataArrayChanged(const QSurfaceDataArray
    &array)': takes a type Python has no way to hand over yet.
  - Qt's 'void QSurface3DSeries::shadingChanged(const Shading shading)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QSurface3DSeries::QSurface3DSeries(QSurface3DSeriesPrivate &d,
    QObject *parent)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  5 of the 60 functions Qt declares: 3 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QSurface3DSeries is created at the first use, not by
    'QSurface3DSeries(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSurface3DSeries.
  - Qt tells when it has removed the C++ QSurface3DSeries. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QSurface3DSeries that has no cute function yet,
    'dataArray', 'dataArrayChanged', 'setDataArray', 'setShading',
    'shadingChanged', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QSurface3DSeries, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class DrawFlag(CuteFlags):
    """
    The flags enum 'QSurface3DSeries::DrawFlag' of Qt, with the 4 names Qt
    gives in it. Qt names the type of its combinations
    'QSurface3DSeries::DrawFlags'.
    """

    DrawWireframe = 0x1
    DrawSurface = 0x2
    DrawSurfaceAndWireframe = 0x3
    DrawFilledSurface = 0x4

  DrawFlags = DrawFlag

  class Shading(CuteNum, scoped=True):
    """
    The enum 'QSurface3DSeries::Shading' of Qt, with the 2 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Smooth = Kee[int](0)
    Flat = Kee[int](1)

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
    Calls Qt's 'QString QSurface3DSeries::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qsurface3dseries.html#tr

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
    #  QString QSurface3DSeries::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QSurface3DSeries2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def invalidSelectionPosition() -> QPoint:
    """
    Calls Qt's 'QPoint QSurface3DSeries::invalidSelectionPosition()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseries.html#invalidSelectionPosition

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QSurface3DSeries::invalidSelectionPosition()
    address = Rituals.call(
        'ritual_ZN16QSurface3DSeries24invalidSelectionPositionEv',
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSurface3DSeries'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtGraphs'

  #  A C++ QSurface3DSeries Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSurface3DSeries'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSurface3DSeries::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsurface3dseries.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSurface3DSeries::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QSurface3DSeries10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def dataProxy(self) -> Optional[QSurfaceDataProxy]:
    """
    Calls Qt's 'QSurfaceDataProxy *QSurface3DSeries::dataProxy() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsurface3dseries.html#dataProxy

    Returns
    -------

    Optional[QSurfaceDataProxy]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSurfaceDataProxy *QSurface3DSeries::dataProxy() const
    address = self.uglySide.call('ritual_ZNK16QSurface3DSeries9dataProxyEv')
    from . import QSurfaceDataProxy
    return QSurfaceDataProxy._cuteAt(address)

  def selectedPoint(self) -> QPoint:
    """
    Calls Qt's 'QPoint QSurface3DSeries::selectedPoint() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseries.html#selectedPoint

    Returns
    -------

    QPoint
      A new cute QPoint around the copy Qt gave back. Python owns it.
    """
    #  QPoint QSurface3DSeries::selectedPoint() const
    address = self.uglySide.call(
        'ritual_ZNK16QSurface3DSeries13selectedPointEv',
    )
    from ..QtCore import QPoint
    return QPoint._cuteOwning(address)

  def shading(self) -> Shading:
    """
    Calls Qt's 'QSurface3DSeries::Shading QSurface3DSeries::shading() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsurface3dseries.html#shading

    Returns
    -------

    Shading
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Shading(number)' gives.
    """
    #  QSurface3DSeries::Shading QSurface3DSeries::shading() const
    return QSurface3DSeries.Shading(self.uglySide.call(
        'ritual_ZNK16QSurface3DSeries7shadingEv',
    ))

  def drawMode(self) -> DrawFlags:
    """
    Calls Qt's 'QSurface3DSeries::DrawFlags QSurface3DSeries::drawMode()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsurface3dseries.html#drawMode

    Returns
    -------

    DrawFlags
      The value standing for the combination Qt gave back.
    """
    #  QSurface3DSeries::DrawFlags QSurface3DSeries::drawMode() const
    return QSurface3DSeries.DrawFlags(self.uglySide.call(
        'ritual_ZNK16QSurface3DSeries8drawModeEv',
    ))

  def isFlatShadingSupported(self) -> bool:
    """
    Calls Qt's 'bool QSurface3DSeries::isFlatShadingSupported() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseries.html#isFlatShadingSupported
    """
    #  bool QSurface3DSeries::isFlatShadingSupported() const
    return self.uglySide.call(
        'ritual_ZNK16QSurface3DSeries22isFlatShadingSupportedEv',
    )

  def texture(self) -> QImage:
    """
    Calls Qt's 'QImage QSurface3DSeries::texture() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsurface3dseries.html#texture

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QSurface3DSeries::texture() const
    address = self.uglySide.call('ritual_ZNK16QSurface3DSeries7textureEv')
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  def textureFile(self) -> str:
    """
    Calls Qt's 'QString QSurface3DSeries::textureFile() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsurface3dseries.html#textureFile

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QSurface3DSeries::textureFile() const
    return self.uglySide.call('ritual_ZNK16QSurface3DSeries11textureFileEv')

  def wireframeColor(self) -> QColor:
    """
    Calls Qt's 'QColor QSurface3DSeries::wireframeColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseries.html#wireframeColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QSurface3DSeries::wireframeColor() const
    address = self.uglySide.call(
        'ritual_ZNK16QSurface3DSeries14wireframeColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def rowsSanitized(self) -> bool:
    """
    Calls Qt's 'bool QSurface3DSeries::rowsSanitized() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseries.html#rowsSanitized
    """
    #  bool QSurface3DSeries::rowsSanitized() const
    return self.uglySide.call(
        'ritual_ZNK16QSurface3DSeries13rowsSanitizedEv',
    )

  def axisX(self) -> Optional[QValue3DAxis]:
    """
    Calls Qt's 'QValue3DAxis *QSurface3DSeries::axisX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsurface3dseries.html#axisX

    Returns
    -------

    Optional[QValue3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QValue3DAxis *QSurface3DSeries::axisX() const
    address = self.uglySide.call('ritual_ZNK16QSurface3DSeries5axisXEv')
    from . import QValue3DAxis
    return QValue3DAxis._cuteAt(address)

  def axisY(self) -> Optional[QValue3DAxis]:
    """
    Calls Qt's 'QValue3DAxis *QSurface3DSeries::axisY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsurface3dseries.html#axisY

    Returns
    -------

    Optional[QValue3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QValue3DAxis *QSurface3DSeries::axisY() const
    address = self.uglySide.call('ritual_ZNK16QSurface3DSeries5axisYEv')
    from . import QValue3DAxis
    return QValue3DAxis._cuteAt(address)

  def axisZ(self) -> Optional[QValue3DAxis]:
    """
    Calls Qt's 'QValue3DAxis *QSurface3DSeries::axisZ() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsurface3dseries.html#axisZ

    Returns
    -------

    Optional[QValue3DAxis]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QValue3DAxis *QSurface3DSeries::axisZ() const
    address = self.uglySide.call('ritual_ZNK16QSurface3DSeries5axisZEv')
    from . import QValue3DAxis
    return QValue3DAxis._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSurfaceDataProxy)
  @overload(NoneType)
  def setDataProxy(self, proxy: Optional[QSurfaceDataProxy]) -> None:
    """
    Calls Qt's 'void QSurface3DSeries::setDataProxy(QSurfaceDataProxy
    *proxy)'.

    Qt's own words: https://doc.qt.io/qt-6/qsurface3dseries.html#setDataProxy

    Parameters
    ----------

    proxy : Optional[QSurfaceDataProxy]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSurface3DSeries::setDataProxy(QSurfaceDataProxy *proxy)
    self.uglySide.call(
        'ritual_ZN16QSurface3DSeries12setDataProxyEP17QSurfaceDataProxy',
        self._addressOf(proxy),
    )

  @overload(QPoint)
  def setSelectedPoint(self, position: QPoint) -> None:
    """
    Calls Qt's 'void QSurface3DSeries::setSelectedPoint(QPoint position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseries.html#setSelectedPoint

    Parameters
    ----------

    position : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QSurface3DSeries::setSelectedPoint(QPoint position)
    self.uglySide.call(
        'ritual_ZN16QSurface3DSeries16setSelectedPointE6QPoint',
        self._valueOf(position),
    )

  @overload(DrawFlags)
  def setDrawMode(self, mode: DrawFlags) -> None:
    """
    Calls Qt's 'void
    QSurface3DSeries::setDrawMode(QSurface3DSeries::DrawFlags mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qsurface3dseries.html#setDrawMode

    Parameters
    ----------

    mode : DrawFlags
      Passed on as its number.
    """
    #  void QSurface3DSeries::setDrawMode(QSurface3DSeries::DrawFlags mode)
    self.uglySide.call(
        'ritual_ZN16QSurface3DSeries11setDrawModeE6QFlagsINS_8DrawFlagEE',
        mode.value,
    )

  @overload(QImage)
  def setTexture(self, texture: QImage) -> None:
    """
    Calls Qt's 'void QSurface3DSeries::setTexture(const QImage &texture)'.

    Qt's own words: https://doc.qt.io/qt-6/qsurface3dseries.html#setTexture

    Parameters
    ----------

    texture : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  void QSurface3DSeries::setTexture(const QImage &texture)
    self.uglySide.call(
        'ritual_ZN16QSurface3DSeries10setTextureERK6QImage',
        self._valueOf(texture),
    )

  @overload(str)
  def setTextureFile(self, filename: str) -> None:
    """
    Calls Qt's 'void QSurface3DSeries::setTextureFile(const QString
    &filename)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseries.html#setTextureFile

    Parameters
    ----------

    filename : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSurface3DSeries::setTextureFile(const QString &filename)
    self.uglySide.call(
        'ritual_ZN16QSurface3DSeries14setTextureFileERK7QString', filename,
    )

  @overload(QColor)
  def setWireframeColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QSurface3DSeries::setWireframeColor(QColor color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseries.html#setWireframeColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSurface3DSeries::setWireframeColor(QColor color)
    self.uglySide.call(
        'ritual_ZN16QSurface3DSeries17setWireframeColorE6QColor',
        self._valueOf(color),
    )

  @overload(bool)
  def setRowsSanitized(self, sanitized: bool) -> None:
    """
    Calls Qt's 'void QSurface3DSeries::setRowsSanitized(bool sanitized)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseries.html#setRowsSanitized

    Parameters
    ----------

    sanitized : bool
      Passed on as it is.
    """
    #  void QSurface3DSeries::setRowsSanitized(bool sanitized)
    self.uglySide.call(
        'ritual_ZN16QSurface3DSeries16setRowsSanitizedEb', sanitized,
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def setAxisX(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void QSurface3DSeries::setAxisX(QValue3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/qsurface3dseries.html#setAxisX

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSurface3DSeries::setAxisX(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN16QSurface3DSeries8setAxisXEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def setAxisY(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void QSurface3DSeries::setAxisY(QValue3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/qsurface3dseries.html#setAxisY

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSurface3DSeries::setAxisY(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN16QSurface3DSeries8setAxisYEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def setAxisZ(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void QSurface3DSeries::setAxisZ(QValue3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/qsurface3dseries.html#setAxisZ

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSurface3DSeries::setAxisZ(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN16QSurface3DSeries8setAxisZEP12QValue3DAxis',
        self._addressOf(axis),
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

  @overload(QSurfaceDataProxy)
  @overload(QSurfaceDataProxy, QObject)
  @overload(QSurfaceDataProxy, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      dataProxy: Optional[QSurfaceDataProxy],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QSurface3DSeries::QSurface3DSeries(QSurfaceDataProxy *dataProxy, QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseries.html#QSurface3DSeries

    Parameters
    ----------

    dataProxy : Optional[QSurfaceDataProxy]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSurface3DSeries::QSurface3DSeries(QSurfaceDataProxy *dataProxy,
    #      QObject *parent)
    self._noteCreation(QSurface3DSeries, lambda: Rituals.call(
        'ritual_ZN16QSurface3DSeriesC1EP17QSurfaceDataProxyP7QObject',
        self._addressOf(dataProxy), self._addressOf(parent, 'QObject'),
    ))

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QSurface3DSeries::QSurface3DSeries(QObject *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseries.html#QSurface3DSeries

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSurface3DSeries::QSurface3DSeries(QObject *parent)
    self._noteCreation(QSurface3DSeries, lambda: Rituals.call(
        'ritual_ZN16QSurface3DSeriesC1EP7QObject',
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

  def d_func(self) -> Optional[QSurface3DSeriesPrivate]:
    """
    Calls Qt's 'QSurface3DSeriesPrivate *QSurface3DSeries::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qsurface3dseries.html#d_func

    Returns
    -------

    Optional[QSurface3DSeriesPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSurface3DSeriesPrivate *QSurface3DSeries::d_func()
    address = self.uglySide.call('ritual_ZN16QSurface3DSeries6d_funcEv')
    from . import QSurface3DSeriesPrivate
    return QSurface3DSeriesPrivate._cuteAt(address)

  @overload(int)
  def clearRow(self, rowIndex: int) -> None:
    """
    Calls Qt's 'void QSurface3DSeries::clearRow(qsizetype rowIndex)'.

    Qt's own words: https://doc.qt.io/qt-6/qsurface3dseries.html#clearRow

    Parameters
    ----------

    rowIndex : int
      Passed on as it is.
    """
    #  void QSurface3DSeries::clearRow(qsizetype rowIndex)
    self.uglySide.call('ritual_ZN16QSurface3DSeries8clearRowEx', rowIndex)

  def clearArray(self) -> None:
    """
    Calls Qt's 'void QSurface3DSeries::clearArray()'.

    Qt's own words: https://doc.qt.io/qt-6/qsurface3dseries.html#clearArray
    """
    #  void QSurface3DSeries::clearArray()
    self.uglySide.call('ritual_ZN16QSurface3DSeries10clearArrayEv')

  def resetAxisX(self) -> None:
    """
    Calls Qt's 'void QSurface3DSeries::resetAxisX()'.

    Qt's own words: https://doc.qt.io/qt-6/qsurface3dseries.html#resetAxisX
    """
    #  void QSurface3DSeries::resetAxisX()
    self.uglySide.call('ritual_ZN16QSurface3DSeries10resetAxisXEv')

  def resetAxisY(self) -> None:
    """
    Calls Qt's 'void QSurface3DSeries::resetAxisY()'.

    Qt's own words: https://doc.qt.io/qt-6/qsurface3dseries.html#resetAxisY
    """
    #  void QSurface3DSeries::resetAxisY()
    self.uglySide.call('ritual_ZN16QSurface3DSeries10resetAxisYEv')

  def resetAxisZ(self) -> None:
    """
    Calls Qt's 'void QSurface3DSeries::resetAxisZ()'.

    Qt's own words: https://doc.qt.io/qt-6/qsurface3dseries.html#resetAxisZ
    """
    #  void QSurface3DSeries::resetAxisZ()
    self.uglySide.call('ritual_ZN16QSurface3DSeries10resetAxisZEv')

  @overload(QSurfaceDataProxy)
  @overload(NoneType)
  def dataProxyChanged(self, proxy: Optional[QSurfaceDataProxy]) -> None:
    """
    Calls Qt's 'void QSurface3DSeries::dataProxyChanged(QSurfaceDataProxy
    *proxy)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseries.html#dataProxyChanged

    Parameters
    ----------

    proxy : Optional[QSurfaceDataProxy]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSurface3DSeries::dataProxyChanged(QSurfaceDataProxy *proxy)
    self.uglySide.call(
        'ritual_ZN16QSurface3DSeries16dataProxyChangedEP17QSurfaceDataProxy',
        self._addressOf(proxy),
    )

  @overload(QPoint)
  def selectedPointChanged(self, position: QPoint) -> None:
    """
    Calls Qt's 'void QSurface3DSeries::selectedPointChanged(QPoint
    position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseries.html#selectedPointChanged

    Parameters
    ----------

    position : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QSurface3DSeries::selectedPointChanged(QPoint position)
    self.uglySide.call(
        'ritual_ZN16QSurface3DSeries20selectedPointChangedE6QPoint',
        self._valueOf(position),
    )

  @overload(bool)
  def flatShadingSupportedChanged(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QSurface3DSeries::flatShadingSupportedChanged(bool
    enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseries.html#flatShadingSupportedChanged

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QSurface3DSeries::flatShadingSupportedChanged(bool enabled)
    self.uglySide.call(
        'ritual_ZN16QSurface3DSeries27flatShadingSupportedChangedEb',
        enabled,
    )

  @overload(DrawFlags)
  def drawModeChanged(self, mode: DrawFlags) -> None:
    """
    Calls Qt's 'void
    QSurface3DSeries::drawModeChanged(QSurface3DSeries::DrawFlags mode)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseries.html#drawModeChanged

    Parameters
    ----------

    mode : DrawFlags
      Passed on as its number.
    """
    #  void QSurface3DSeries::drawModeChanged(QSurface3DSeries::DrawFlags
    #      mode)
    self.uglySide.call(
        'ritual_ZN16QSurface3DSeries15drawModeChangedE6QFlagsINS_8DrawFlagE'
        'E',
        mode.value,
    )

  @overload(QImage)
  def textureChanged(self, image: QImage) -> None:
    """
    Calls Qt's 'void QSurface3DSeries::textureChanged(const QImage &image)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseries.html#textureChanged

    Parameters
    ----------

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  void QSurface3DSeries::textureChanged(const QImage &image)
    self.uglySide.call(
        'ritual_ZN16QSurface3DSeries14textureChangedERK6QImage',
        self._valueOf(image),
    )

  @overload(str)
  def textureFileChanged(self, filename: str) -> None:
    """
    Calls Qt's 'void QSurface3DSeries::textureFileChanged(const QString
    &filename)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseries.html#textureFileChanged

    Parameters
    ----------

    filename : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QSurface3DSeries::textureFileChanged(const QString &filename)
    self.uglySide.call(
        'ritual_ZN16QSurface3DSeries18textureFileChangedERK7QString',
        filename,
    )

  @overload(QColor)
  def wireframeColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void QSurface3DSeries::wireframeColorChanged(QColor color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseries.html#wireframeColorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSurface3DSeries::wireframeColorChanged(QColor color)
    self.uglySide.call(
        'ritual_ZN16QSurface3DSeries21wireframeColorChangedE6QColor',
        self._valueOf(color),
    )

  @overload(bool)
  def rowsSanitizedChanged(self, newRowsSanitized: bool) -> None:
    """
    Calls Qt's 'void QSurface3DSeries::rowsSanitizedChanged(bool
    newRowsSanitized)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseries.html#rowsSanitizedChanged

    Parameters
    ----------

    newRowsSanitized : bool
      Passed on as it is.
    """
    #  void QSurface3DSeries::rowsSanitizedChanged(bool newRowsSanitized)
    self.uglySide.call(
        'ritual_ZN16QSurface3DSeries20rowsSanitizedChangedEb',
        newRowsSanitized,
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def axisXChanged(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void QSurface3DSeries::axisXChanged(QValue3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/qsurface3dseries.html#axisXChanged

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSurface3DSeries::axisXChanged(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN16QSurface3DSeries12axisXChangedEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def axisYChanged(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void QSurface3DSeries::axisYChanged(QValue3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/qsurface3dseries.html#axisYChanged

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSurface3DSeries::axisYChanged(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN16QSurface3DSeries12axisYChangedEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @overload(QValue3DAxis)
  @overload(NoneType)
  def axisZChanged(self, axis: Optional[QValue3DAxis]) -> None:
    """
    Calls Qt's 'void QSurface3DSeries::axisZChanged(QValue3DAxis *axis)'.

    Qt's own words: https://doc.qt.io/qt-6/qsurface3dseries.html#axisZChanged

    Parameters
    ----------

    axis : Optional[QValue3DAxis]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QSurface3DSeries::axisZChanged(QValue3DAxis *axis)
    self.uglySide.call(
        'ritual_ZN16QSurface3DSeries12axisZChangedEP12QValue3DAxis',
        self._addressOf(axis),
    )

  @staticmethod
  def dataArray(*__, **_) -> Never:
    """
    Qt's 'const QSurfaceDataArray &QSurface3DSeries::dataArray() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSurface3DSeries.dataArray' has no cute function yet. Qt's 'const "
        "QSurfaceDataArray &QSurface3DSeries::dataArray() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def dataArrayChanged(*__, **_) -> Never:
    """
    Qt's 'void QSurface3DSeries::dataArrayChanged(const QSurfaceDataArray
    &array)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSurface3DSeries.dataArrayChanged' has no cute function yet. Qt's "
        "'void QSurface3DSeries::dataArrayChanged(const QSurfaceDataArray "
        "&array)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def setDataArray(*__, **_) -> Never:
    """
    Qt's 'void QSurface3DSeries::setDataArray(const QSurfaceDataArray
    &newDataArray)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSurface3DSeries.setDataArray' has no cute function yet. Qt's "
        "'void QSurface3DSeries::setDataArray(const QSurfaceDataArray "
        "&newDataArray)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def setShading(*__, **_) -> Never:
    """
    Qt's 'void QSurface3DSeries::setShading(const QSurface3DSeries::Shading
    shading)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSurface3DSeries.setShading' has no cute function yet. Qt's 'void "
        "QSurface3DSeries::setShading(const QSurface3DSeries::Shading "
        "shading)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def shadingChanged(*__, **_) -> Never:
    """
    Qt's 'void QSurface3DSeries::shadingChanged(const Shading shading)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QSurface3DSeries.shadingChanged' has no cute function yet. Qt's "
        "'void QSurface3DSeries::shadingChanged(const Shading shading)': "
        "takes a type Python has no way to hand over yet.")


#  Qt's 'QList<QSurface3DSeries *>': the list of QSurface3DSeries, which
#  'QList[QSurface3DSeries]' gives. It is made here, so that there is one as
#  soon as there can be a QSurface3DSeries.
QList.createKind(
    QSurface3DSeries, 'address',
    make='ritual_list_make_QSurface3DSeries_ptr',
    add='ritual_list_add_QSurface3DSeries_ptr',
    size='ritual_list_size_QSurface3DSeries_ptr',
    at='ritual_list_at_QSurface3DSeries_ptr',
    drop='ritual_list_drop_QSurface3DSeries_ptr',
)
