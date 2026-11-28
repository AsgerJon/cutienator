"""
QSurface3DSeries binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/qsurface3dseries.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QAbstract3DSeries

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QPoint
  from ..QtGui import QColor, QImage
  from . import QSurface3DSeriesPrivate, QSurfaceDataProxy
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QImage = WAIT['QImage']
  QPoint = WAIT['QPoint']
  QSurface3DSeriesPrivate = WAIT['QtDataVisualization:QSurface3DSeriesPrivate']
  QSurfaceDataProxy = WAIT['QtDataVisualization:QSurfaceDataProxy']

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
  can call so far, 28 names in all: 'metaObject', 'tr', 'setDataProxy',
  'dataProxy', 'setSelectedPoint', 'selectedPoint',
  'invalidSelectionPosition', 'setFlatShadingEnabled',
  'isFlatShadingEnabled', 'setDrawMode', 'drawMode',
  'isFlatShadingSupported', 'setTexture', 'texture', 'setTextureFile',
  'textureFile', 'setWireframeColor', 'wireframeColor', 'dataProxyChanged',
  'selectedPointChanged', 'flatShadingEnabledChanged',
  'flatShadingSupportedChanged', 'drawModeChanged', 'textureChanged',
  'textureFileChanged', 'wireframeColorChanged', 'dptr', 'dptrc'. It can be
  made from Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSurface3DSeries::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QSurface3DSeries::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QSurface3DSeries::~QSurface3DSeries()': the destructor: Python
    never removes a C++ QSurface3DSeries.

  What has no ritual
  ------------------

  4 of the 38 functions Qt declares: 2 not a gap; 2 forbidden.

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
  """

  #  The enums Qt writes inside QSurface3DSeries, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class DrawFlag(CuteFlags):
    """
    The flags enum 'QSurface3DSeries::DrawFlag' of Qt, with the 3 names Qt
    gives in it. Qt names the type of its combinations
    'QSurface3DSeries::DrawFlags'.
    """

    DrawWireframe = 0x1
    DrawSurface = 0x2
    DrawSurfaceAndWireframe = 0x3

  DrawFlags = DrawFlag

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
  __qt_part__ = 'QtDataVisualization'

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

  def isFlatShadingEnabled(self) -> bool:
    """
    Calls Qt's 'bool QSurface3DSeries::isFlatShadingEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseries.html#isFlatShadingEnabled
    """
    #  bool QSurface3DSeries::isFlatShadingEnabled() const
    return self.uglySide.call(
        'ritual_ZNK16QSurface3DSeries20isFlatShadingEnabledEv',
    )

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

  def dptrc(self) -> Optional[QSurface3DSeriesPrivate]:
    """
    Calls Qt's 'const QSurface3DSeriesPrivate *QSurface3DSeries::dptrc()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsurface3dseries.html#dptrc

    Returns
    -------

    Optional[QSurface3DSeriesPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QSurface3DSeriesPrivate *QSurface3DSeries::dptrc() const
    address = self.uglySide.call('ritual_ZNK16QSurface3DSeries5dptrcEv')
    from . import QSurface3DSeriesPrivate
    return QSurface3DSeriesPrivate._cuteAt(address)

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
    Calls Qt's 'void QSurface3DSeries::setSelectedPoint(const QPoint
    &position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseries.html#setSelectedPoint

    Parameters
    ----------

    position : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QSurface3DSeries::setSelectedPoint(const QPoint &position)
    self.uglySide.call(
        'ritual_ZN16QSurface3DSeries16setSelectedPointERK6QPoint',
        self._valueOf(position),
    )

  @overload(bool)
  def setFlatShadingEnabled(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QSurface3DSeries::setFlatShadingEnabled(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseries.html#setFlatShadingEnabled

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QSurface3DSeries::setFlatShadingEnabled(bool enabled)
    self.uglySide.call(
        'ritual_ZN16QSurface3DSeries21setFlatShadingEnabledEb', enabled,
    )

  @overload(DrawFlags)
  def setDrawMode(self, mode: DrawFlags) -> None:
    """
    Calls Qt's 'void QSurface3DSeries::setDrawMode(DrawFlags mode)'.

    Qt's own words: https://doc.qt.io/qt-6/qsurface3dseries.html#setDrawMode

    Parameters
    ----------

    mode : DrawFlags
      Passed on as its number.
    """
    #  void QSurface3DSeries::setDrawMode(DrawFlags mode)
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
    Calls Qt's 'void QSurface3DSeries::setWireframeColor(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseries.html#setWireframeColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSurface3DSeries::setWireframeColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN16QSurface3DSeries17setWireframeColorERK6QColor',
        self._valueOf(color),
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

  @overload(QSurface3DSeriesPrivate)
  @overload(QSurface3DSeriesPrivate, QObject)
  @overload(QSurface3DSeriesPrivate, NoneType)
  def __init__(
      self,
      d: Optional[QSurface3DSeriesPrivate],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QSurface3DSeries::QSurface3DSeries(QSurface3DSeriesPrivate *d, QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseries.html#QSurface3DSeries

    Parameters
    ----------

    d : Optional[QSurface3DSeriesPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QSurface3DSeries::QSurface3DSeries(QSurface3DSeriesPrivate *d, QObject
    #      *parent)
    self._noteCreation(QSurface3DSeries, lambda: Rituals.call(
        'ritual_ZN16QSurface3DSeriesC1EP23QSurface3DSeriesPrivateP7QObject',
        self._addressOf(d), self._addressOf(parent, 'QObject'),
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
    Calls Qt's 'void QSurface3DSeries::selectedPointChanged(const QPoint
    &position)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseries.html#selectedPointChanged

    Parameters
    ----------

    position : QPoint
      Passed on as a value: Qt reads the C++ QPoint, which stays Python's
      own.
    """
    #  void QSurface3DSeries::selectedPointChanged(const QPoint &position)
    self.uglySide.call(
        'ritual_ZN16QSurface3DSeries20selectedPointChangedERK6QPoint',
        self._valueOf(position),
    )

  @overload(bool)
  def flatShadingEnabledChanged(self, enable: bool) -> None:
    """
    Calls Qt's 'void QSurface3DSeries::flatShadingEnabledChanged(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseries.html#flatShadingEnabledChanged

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QSurface3DSeries::flatShadingEnabledChanged(bool enable)
    self.uglySide.call(
        'ritual_ZN16QSurface3DSeries25flatShadingEnabledChangedEb', enable,
    )

  @overload(bool)
  def flatShadingSupportedChanged(self, enable: bool) -> None:
    """
    Calls Qt's 'void QSurface3DSeries::flatShadingSupportedChanged(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseries.html#flatShadingSupportedChanged

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QSurface3DSeries::flatShadingSupportedChanged(bool enable)
    self.uglySide.call(
        'ritual_ZN16QSurface3DSeries27flatShadingSupportedChangedEb', enable,
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
    Calls Qt's 'void QSurface3DSeries::wireframeColorChanged(const QColor
    &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsurface3dseries.html#wireframeColorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSurface3DSeries::wireframeColorChanged(const QColor &color)
    self.uglySide.call(
        'ritual_ZN16QSurface3DSeries21wireframeColorChangedERK6QColor',
        self._valueOf(color),
    )

  def dptr(self) -> Optional[QSurface3DSeriesPrivate]:
    """
    Calls Qt's 'QSurface3DSeriesPrivate *QSurface3DSeries::dptr()'.

    Qt's own words: https://doc.qt.io/qt-6/qsurface3dseries.html#dptr

    Returns
    -------

    Optional[QSurface3DSeriesPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSurface3DSeriesPrivate *QSurface3DSeries::dptr()
    address = self.uglySide.call('ritual_ZN16QSurface3DSeries4dptrEv')
    from . import QSurface3DSeriesPrivate
    return QSurface3DSeriesPrivate._cuteAt(address)


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
