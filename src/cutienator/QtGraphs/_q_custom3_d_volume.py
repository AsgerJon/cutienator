"""
QCustom3DVolume binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/qcustom3dvolume.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QList, QObject
from ..QtGui import QImage
from . import QCustom3DItem

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QColor, QVector3D
  from . import QCustom3DVolumePrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QCustom3DVolume(QCustom3DItem):
  """
  The cute side of Qt's QCustom3DVolume: a plain Python object standing in
  front of one C++ QCustom3DVolume.

  It is built on the cute 'QCustom3DItem', as Qt's QCustom3DVolume is built
  on Qt's QCustom3DItem, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QCustom3DVolume that has a ritual and that Python
  can call so far, 57 names in all: 'metaObject', 'tr', 'd_func',
  'setTextureWidth', 'textureWidth', 'setTextureHeight', 'textureHeight',
  'setTextureDepth', 'textureDepth', 'setTextureDimensions',
  'textureDataWidth', 'setSliceIndexX', 'sliceIndexX', 'setSliceIndexY',
  'sliceIndexY', 'setSliceIndexZ', 'sliceIndexZ', 'setSliceIndices',
  'setSubTextureData', 'setTextureFormat', 'textureFormat',
  'setAlphaMultiplier', 'alphaMultiplier', 'setPreserveOpacity',
  'preserveOpacity', 'setUseHighDefShader', 'useHighDefShader',
  'setDrawSlices', 'drawSlices', 'setDrawSliceFrames', 'drawSliceFrames',
  'setSliceFrameColor', 'sliceFrameColor', 'setSliceFrameWidths',
  'sliceFrameWidths', 'setSliceFrameGaps', 'sliceFrameGaps',
  'setSliceFrameThicknesses', 'sliceFrameThicknesses', 'renderSlice',
  'textureWidthChanged', 'textureHeightChanged', 'textureDepthChanged',
  'sliceIndexXChanged', 'sliceIndexYChanged', 'sliceIndexZChanged',
  'colorTableChanged', 'textureFormatChanged', 'alphaMultiplierChanged',
  'preserveOpacityChanged', 'useHighDefShaderChanged', 'drawSlicesChanged',
  'drawSliceFramesChanged', 'sliceFrameColorChanged',
  'sliceFrameWidthsChanged', 'sliceFrameGapsChanged',
  'sliceFrameThicknessesChanged'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QCustom3DVolume::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QCustom3DVolume::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QCustom3DVolumePrivate *QCustom3DVolume::d_func() const':
    takes in Python what 'QCustom3DVolumePrivate *QCustom3DVolume::d_func()'
    takes.
  - Qt's 'QCustom3DVolume::QCustom3DVolume(QVector3D position, QVector3D
    scaling, const QQuaternion &rotation, int textureWidth, int
    textureHeight, int textureDepth, QList<uchar> *textureData,
    QImage::Format textureFormat, const QList<QRgb> &colorTable, QObject
    *parent)': names 'QList<uchar>', which has no cute class yet.
  - Qt's 'QCustom3DVolume::~QCustom3DVolume()': the destructor: Python never
    removes a C++ QCustom3DVolume.
  - Qt's 'void QCustom3DVolume::setColorTable(const QList<QRgb> &colors)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QList<QRgb> QCustom3DVolume::colorTable() const': gives a type
    Python has no way to take yet.
  - Qt's 'void QCustom3DVolume::setTextureData(QList<uchar> *data)': names
    'QList<uchar>', which has no cute class yet.
  - Qt's 'QList<uchar> *QCustom3DVolume::createTextureData(const QList<QImage
    *> &images)': gives 'QList<uchar>', which has no cute class yet.
  - Qt's 'QList<uchar> *QCustom3DVolume::textureData() const': gives
    'QList<uchar>', which has no cute class yet.
  - Qt's 'void QCustom3DVolume::setSubTextureData(Qt::Axis axis, int index,
    const uchar *data)': names 'uchar', which has no cute class yet.
  - Qt's 'void QCustom3DVolume::textureDataChanged(QList<uchar> *data)':
    names 'QList<uchar>', which has no cute class yet.

  What has no ritual
  ------------------

  4 of the 74 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QCustom3DVolume is created at the first use, not by
    'QCustom3DVolume(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCustom3DVolume.
  - Qt tells when it has removed the C++ QCustom3DVolume. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QCustom3DVolume that has no cute function yet,
    'colorTable', 'createTextureData', 'setColorTable', 'setTextureData',
    'textureData', 'textureDataChanged', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QCustom3DVolume::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3dvolume.html#tr

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
    #  QString QCustom3DVolume::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN15QCustom3DVolume2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCustom3DVolume'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtGraphs'

  #  A C++ QCustom3DVolume Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCustom3DVolume'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QCustom3DVolume::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3dvolume.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QCustom3DVolume::metaObject() const
    address = self.uglySide.call('ritual_ZNK15QCustom3DVolume10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def textureWidth(self) -> int:
    """
    Calls Qt's 'int QCustom3DVolume::textureWidth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3dvolume.html#textureWidth
    """
    #  int QCustom3DVolume::textureWidth() const
    return self.uglySide.call('ritual_ZNK15QCustom3DVolume12textureWidthEv')

  def textureHeight(self) -> int:
    """
    Calls Qt's 'int QCustom3DVolume::textureHeight() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3dvolume.html#textureHeight
    """
    #  int QCustom3DVolume::textureHeight() const
    return self.uglySide.call('ritual_ZNK15QCustom3DVolume13textureHeightEv')

  def textureDepth(self) -> int:
    """
    Calls Qt's 'int QCustom3DVolume::textureDepth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3dvolume.html#textureDepth
    """
    #  int QCustom3DVolume::textureDepth() const
    return self.uglySide.call('ritual_ZNK15QCustom3DVolume12textureDepthEv')

  def textureDataWidth(self) -> int:
    """
    Calls Qt's 'int QCustom3DVolume::textureDataWidth() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dvolume.html#textureDataWidth
    """
    #  int QCustom3DVolume::textureDataWidth() const
    return self.uglySide.call(
        'ritual_ZNK15QCustom3DVolume16textureDataWidthEv',
    )

  def sliceIndexX(self) -> int:
    """
    Calls Qt's 'int QCustom3DVolume::sliceIndexX() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3dvolume.html#sliceIndexX
    """
    #  int QCustom3DVolume::sliceIndexX() const
    return self.uglySide.call('ritual_ZNK15QCustom3DVolume11sliceIndexXEv')

  def sliceIndexY(self) -> int:
    """
    Calls Qt's 'int QCustom3DVolume::sliceIndexY() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3dvolume.html#sliceIndexY
    """
    #  int QCustom3DVolume::sliceIndexY() const
    return self.uglySide.call('ritual_ZNK15QCustom3DVolume11sliceIndexYEv')

  def sliceIndexZ(self) -> int:
    """
    Calls Qt's 'int QCustom3DVolume::sliceIndexZ() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3dvolume.html#sliceIndexZ
    """
    #  int QCustom3DVolume::sliceIndexZ() const
    return self.uglySide.call('ritual_ZNK15QCustom3DVolume11sliceIndexZEv')

  def textureFormat(self) -> QImage.Format:
    """
    Calls Qt's 'QImage::Format QCustom3DVolume::textureFormat() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3dvolume.html#textureFormat

    Returns
    -------

    QImage.Format
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QImage.Format(number)'
      gives.
    """
    #  QImage::Format QCustom3DVolume::textureFormat() const
    return QImage.Format(self.uglySide.call(
        'ritual_ZNK15QCustom3DVolume13textureFormatEv',
    ))

  def alphaMultiplier(self) -> float:
    """
    Calls Qt's 'float QCustom3DVolume::alphaMultiplier() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dvolume.html#alphaMultiplier
    """
    #  float QCustom3DVolume::alphaMultiplier() const
    return self.uglySide.call(
        'ritual_ZNK15QCustom3DVolume15alphaMultiplierEv',
    )

  def preserveOpacity(self) -> bool:
    """
    Calls Qt's 'bool QCustom3DVolume::preserveOpacity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dvolume.html#preserveOpacity
    """
    #  bool QCustom3DVolume::preserveOpacity() const
    return self.uglySide.call(
        'ritual_ZNK15QCustom3DVolume15preserveOpacityEv',
    )

  def useHighDefShader(self) -> bool:
    """
    Calls Qt's 'bool QCustom3DVolume::useHighDefShader() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dvolume.html#useHighDefShader
    """
    #  bool QCustom3DVolume::useHighDefShader() const
    return self.uglySide.call(
        'ritual_ZNK15QCustom3DVolume16useHighDefShaderEv',
    )

  def drawSlices(self) -> bool:
    """
    Calls Qt's 'bool QCustom3DVolume::drawSlices() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3dvolume.html#drawSlices
    """
    #  bool QCustom3DVolume::drawSlices() const
    return self.uglySide.call('ritual_ZNK15QCustom3DVolume10drawSlicesEv')

  def drawSliceFrames(self) -> bool:
    """
    Calls Qt's 'bool QCustom3DVolume::drawSliceFrames() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dvolume.html#drawSliceFrames
    """
    #  bool QCustom3DVolume::drawSliceFrames() const
    return self.uglySide.call(
        'ritual_ZNK15QCustom3DVolume15drawSliceFramesEv',
    )

  def sliceFrameColor(self) -> QColor:
    """
    Calls Qt's 'QColor QCustom3DVolume::sliceFrameColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dvolume.html#sliceFrameColor

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  QColor QCustom3DVolume::sliceFrameColor() const
    address = self.uglySide.call(
        'ritual_ZNK15QCustom3DVolume15sliceFrameColorEv',
    )
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  def sliceFrameWidths(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QCustom3DVolume::sliceFrameWidths() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dvolume.html#sliceFrameWidths

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QCustom3DVolume::sliceFrameWidths() const
    address = self.uglySide.call(
        'ritual_ZNK15QCustom3DVolume16sliceFrameWidthsEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def sliceFrameGaps(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QCustom3DVolume::sliceFrameGaps() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dvolume.html#sliceFrameGaps

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QCustom3DVolume::sliceFrameGaps() const
    address = self.uglySide.call(
        'ritual_ZNK15QCustom3DVolume14sliceFrameGapsEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def sliceFrameThicknesses(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QCustom3DVolume::sliceFrameThicknesses() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dvolume.html#sliceFrameThicknesses

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QCustom3DVolume::sliceFrameThicknesses() const
    address = self.uglySide.call(
        'ritual_ZNK15QCustom3DVolume21sliceFrameThicknessesEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setTextureWidth(self, value: int) -> None:
    """
    Calls Qt's 'void QCustom3DVolume::setTextureWidth(int value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dvolume.html#setTextureWidth

    Parameters
    ----------

    value : int
      Passed on as it is.
    """
    #  void QCustom3DVolume::setTextureWidth(int value)
    self.uglySide.call(
        'ritual_ZN15QCustom3DVolume15setTextureWidthEi', value,
    )

  @overload(int)
  def setTextureHeight(self, value: int) -> None:
    """
    Calls Qt's 'void QCustom3DVolume::setTextureHeight(int value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dvolume.html#setTextureHeight

    Parameters
    ----------

    value : int
      Passed on as it is.
    """
    #  void QCustom3DVolume::setTextureHeight(int value)
    self.uglySide.call(
        'ritual_ZN15QCustom3DVolume16setTextureHeightEi', value,
    )

  @overload(int)
  def setTextureDepth(self, value: int) -> None:
    """
    Calls Qt's 'void QCustom3DVolume::setTextureDepth(int value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dvolume.html#setTextureDepth

    Parameters
    ----------

    value : int
      Passed on as it is.
    """
    #  void QCustom3DVolume::setTextureDepth(int value)
    self.uglySide.call(
        'ritual_ZN15QCustom3DVolume15setTextureDepthEi', value,
    )

  @overload(int, int, int)
  def setTextureDimensions(
      self,
      width: int,
      height: int,
      depth: int,
  ) -> None:
    """
    Calls Qt's 'void QCustom3DVolume::setTextureDimensions(int width, int
    height, int depth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dvolume.html#setTextureDimensions

    Parameters
    ----------

    width : int
      Passed on as it is.

    height : int
      Passed on as it is.

    depth : int
      Passed on as it is.
    """
    #  void QCustom3DVolume::setTextureDimensions(int width, int height, int
    #      depth)
    self.uglySide.call(
        'ritual_ZN15QCustom3DVolume20setTextureDimensionsEiii',
        width, height, depth,
    )

  @overload(int)
  def setSliceIndexX(self, value: int) -> None:
    """
    Calls Qt's 'void QCustom3DVolume::setSliceIndexX(int value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dvolume.html#setSliceIndexX

    Parameters
    ----------

    value : int
      Passed on as it is.
    """
    #  void QCustom3DVolume::setSliceIndexX(int value)
    self.uglySide.call('ritual_ZN15QCustom3DVolume14setSliceIndexXEi', value)

  @overload(int)
  def setSliceIndexY(self, value: int) -> None:
    """
    Calls Qt's 'void QCustom3DVolume::setSliceIndexY(int value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dvolume.html#setSliceIndexY

    Parameters
    ----------

    value : int
      Passed on as it is.
    """
    #  void QCustom3DVolume::setSliceIndexY(int value)
    self.uglySide.call('ritual_ZN15QCustom3DVolume14setSliceIndexYEi', value)

  @overload(int)
  def setSliceIndexZ(self, value: int) -> None:
    """
    Calls Qt's 'void QCustom3DVolume::setSliceIndexZ(int value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dvolume.html#setSliceIndexZ

    Parameters
    ----------

    value : int
      Passed on as it is.
    """
    #  void QCustom3DVolume::setSliceIndexZ(int value)
    self.uglySide.call('ritual_ZN15QCustom3DVolume14setSliceIndexZEi', value)

  @overload(int, int, int)
  def setSliceIndices(self, x: int, y: int, z: int) -> None:
    """
    Calls Qt's 'void QCustom3DVolume::setSliceIndices(int x, int y, int z)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dvolume.html#setSliceIndices

    Parameters
    ----------

    x : int
      Passed on as it is.

    y : int
      Passed on as it is.

    z : int
      Passed on as it is.
    """
    #  void QCustom3DVolume::setSliceIndices(int x, int y, int z)
    self.uglySide.call(
        'ritual_ZN15QCustom3DVolume15setSliceIndicesEiii', x, y, z,
    )

  @overload(Qt.Axis, int, QImage)
  def setSubTextureData(
      self,
      axis: Qt.Axis,
      index: int,
      image: QImage,
  ) -> None:
    """
    Calls Qt's 'void QCustom3DVolume::setSubTextureData(Qt::Axis axis, int
    index, const QImage &image)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dvolume.html#setSubTextureData

    Parameters
    ----------

    axis : Qt.Axis
      Passed on as its number.

    index : int
      Passed on as it is.

    image : QImage
      Passed on as a value: Qt reads the C++ QImage, which stays Python's
      own.
    """
    #  void QCustom3DVolume::setSubTextureData(Qt::Axis axis, int index,
    #      const QImage &image)
    self.uglySide.call(
        'ritual_ZN15QCustom3DVolume17setSubTextureDataEN2Qt4AxisEiRK6QImage',
        axis.value, index, self._valueOf(image),
    )

  @overload(QImage.Format)
  def setTextureFormat(self, format: QImage.Format) -> None:
    """
    Calls Qt's 'void QCustom3DVolume::setTextureFormat(QImage::Format
    format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dvolume.html#setTextureFormat

    Parameters
    ----------

    format : QImage.Format
      Passed on as its number.
    """
    #  void QCustom3DVolume::setTextureFormat(QImage::Format format)
    self.uglySide.call(
        'ritual_ZN15QCustom3DVolume16setTextureFormatEN6QImage6FormatE',
        format.value,
    )

  @overload(float)
  def setAlphaMultiplier(self, mult: float) -> None:
    """
    Calls Qt's 'void QCustom3DVolume::setAlphaMultiplier(float mult)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dvolume.html#setAlphaMultiplier

    Parameters
    ----------

    mult : float
      Passed on as it is.
    """
    #  void QCustom3DVolume::setAlphaMultiplier(float mult)
    self.uglySide.call(
        'ritual_ZN15QCustom3DVolume18setAlphaMultiplierEf', mult,
    )

  @overload(bool)
  def setPreserveOpacity(self, enable: bool) -> None:
    """
    Calls Qt's 'void QCustom3DVolume::setPreserveOpacity(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dvolume.html#setPreserveOpacity

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QCustom3DVolume::setPreserveOpacity(bool enable)
    self.uglySide.call(
        'ritual_ZN15QCustom3DVolume18setPreserveOpacityEb', enable,
    )

  @overload(bool)
  def setUseHighDefShader(self, enable: bool) -> None:
    """
    Calls Qt's 'void QCustom3DVolume::setUseHighDefShader(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dvolume.html#setUseHighDefShader

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QCustom3DVolume::setUseHighDefShader(bool enable)
    self.uglySide.call(
        'ritual_ZN15QCustom3DVolume19setUseHighDefShaderEb', enable,
    )

  @overload(bool)
  def setDrawSlices(self, enable: bool) -> None:
    """
    Calls Qt's 'void QCustom3DVolume::setDrawSlices(bool enable)'.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3dvolume.html#setDrawSlices

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QCustom3DVolume::setDrawSlices(bool enable)
    self.uglySide.call('ritual_ZN15QCustom3DVolume13setDrawSlicesEb', enable)

  @overload(bool)
  def setDrawSliceFrames(self, enable: bool) -> None:
    """
    Calls Qt's 'void QCustom3DVolume::setDrawSliceFrames(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dvolume.html#setDrawSliceFrames

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QCustom3DVolume::setDrawSliceFrames(bool enable)
    self.uglySide.call(
        'ritual_ZN15QCustom3DVolume18setDrawSliceFramesEb', enable,
    )

  @overload(QColor)
  def setSliceFrameColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QCustom3DVolume::setSliceFrameColor(QColor color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dvolume.html#setSliceFrameColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QCustom3DVolume::setSliceFrameColor(QColor color)
    self.uglySide.call(
        'ritual_ZN15QCustom3DVolume18setSliceFrameColorE6QColor',
        self._valueOf(color),
    )

  @overload(QVector3D)
  def setSliceFrameWidths(self, values: QVector3D) -> None:
    """
    Calls Qt's 'void QCustom3DVolume::setSliceFrameWidths(QVector3D values)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dvolume.html#setSliceFrameWidths

    Parameters
    ----------

    values : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QCustom3DVolume::setSliceFrameWidths(QVector3D values)
    self.uglySide.call(
        'ritual_ZN15QCustom3DVolume19setSliceFrameWidthsE9QVector3D',
        self._valueOf(values),
    )

  @overload(QVector3D)
  def setSliceFrameGaps(self, values: QVector3D) -> None:
    """
    Calls Qt's 'void QCustom3DVolume::setSliceFrameGaps(QVector3D values)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dvolume.html#setSliceFrameGaps

    Parameters
    ----------

    values : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QCustom3DVolume::setSliceFrameGaps(QVector3D values)
    self.uglySide.call(
        'ritual_ZN15QCustom3DVolume17setSliceFrameGapsE9QVector3D',
        self._valueOf(values),
    )

  @overload(QVector3D)
  def setSliceFrameThicknesses(self, values: QVector3D) -> None:
    """
    Calls Qt's 'void QCustom3DVolume::setSliceFrameThicknesses(QVector3D
    values)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dvolume.html#setSliceFrameThicknesses

    Parameters
    ----------

    values : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QCustom3DVolume::setSliceFrameThicknesses(QVector3D values)
    self.uglySide.call(
        'ritual_ZN15QCustom3DVolume24setSliceFrameThicknessesE9QVector3D',
        self._valueOf(values),
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
    Notes what was given, for Qt's 'QCustom3DVolume::QCustom3DVolume(QObject
    *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dvolume.html#QCustom3DVolume

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QCustom3DVolume::QCustom3DVolume(QObject *parent)
    self._noteCreation(QCustom3DVolume, lambda: Rituals.call(
        'ritual_ZN15QCustom3DVolumeC1EP7QObject',
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

  def d_func(self) -> Optional[QCustom3DVolumePrivate]:
    """
    Calls Qt's 'QCustom3DVolumePrivate *QCustom3DVolume::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3dvolume.html#d_func

    Returns
    -------

    Optional[QCustom3DVolumePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCustom3DVolumePrivate *QCustom3DVolume::d_func()
    address = self.uglySide.call('ritual_ZN15QCustom3DVolume6d_funcEv')
    from . import QCustom3DVolumePrivate
    return QCustom3DVolumePrivate._cuteAt(address)

  @overload(Qt.Axis, int)
  def renderSlice(self, axis: Qt.Axis, index: int) -> QImage:
    """
    Calls Qt's 'QImage QCustom3DVolume::renderSlice(Qt::Axis axis, int
    index)'.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3dvolume.html#renderSlice

    Parameters
    ----------

    axis : Qt.Axis
      Passed on as its number.

    index : int
      Passed on as it is.

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QCustom3DVolume::renderSlice(Qt::Axis axis, int index)
    address = self.uglySide.call(
        'ritual_ZN15QCustom3DVolume11renderSliceEN2Qt4AxisEi',
        axis.value, index,
    )
    return QImage._cuteOwning(address)

  @overload(int)
  def textureWidthChanged(self, value: int) -> None:
    """
    Calls Qt's 'void QCustom3DVolume::textureWidthChanged(int value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dvolume.html#textureWidthChanged

    Parameters
    ----------

    value : int
      Passed on as it is.
    """
    #  void QCustom3DVolume::textureWidthChanged(int value)
    self.uglySide.call(
        'ritual_ZN15QCustom3DVolume19textureWidthChangedEi', value,
    )

  @overload(int)
  def textureHeightChanged(self, value: int) -> None:
    """
    Calls Qt's 'void QCustom3DVolume::textureHeightChanged(int value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dvolume.html#textureHeightChanged

    Parameters
    ----------

    value : int
      Passed on as it is.
    """
    #  void QCustom3DVolume::textureHeightChanged(int value)
    self.uglySide.call(
        'ritual_ZN15QCustom3DVolume20textureHeightChangedEi', value,
    )

  @overload(int)
  def textureDepthChanged(self, value: int) -> None:
    """
    Calls Qt's 'void QCustom3DVolume::textureDepthChanged(int value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dvolume.html#textureDepthChanged

    Parameters
    ----------

    value : int
      Passed on as it is.
    """
    #  void QCustom3DVolume::textureDepthChanged(int value)
    self.uglySide.call(
        'ritual_ZN15QCustom3DVolume19textureDepthChangedEi', value,
    )

  @overload(int)
  def sliceIndexXChanged(self, value: int) -> None:
    """
    Calls Qt's 'void QCustom3DVolume::sliceIndexXChanged(int value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dvolume.html#sliceIndexXChanged

    Parameters
    ----------

    value : int
      Passed on as it is.
    """
    #  void QCustom3DVolume::sliceIndexXChanged(int value)
    self.uglySide.call(
        'ritual_ZN15QCustom3DVolume18sliceIndexXChangedEi', value,
    )

  @overload(int)
  def sliceIndexYChanged(self, value: int) -> None:
    """
    Calls Qt's 'void QCustom3DVolume::sliceIndexYChanged(int value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dvolume.html#sliceIndexYChanged

    Parameters
    ----------

    value : int
      Passed on as it is.
    """
    #  void QCustom3DVolume::sliceIndexYChanged(int value)
    self.uglySide.call(
        'ritual_ZN15QCustom3DVolume18sliceIndexYChangedEi', value,
    )

  @overload(int)
  def sliceIndexZChanged(self, value: int) -> None:
    """
    Calls Qt's 'void QCustom3DVolume::sliceIndexZChanged(int value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dvolume.html#sliceIndexZChanged

    Parameters
    ----------

    value : int
      Passed on as it is.
    """
    #  void QCustom3DVolume::sliceIndexZChanged(int value)
    self.uglySide.call(
        'ritual_ZN15QCustom3DVolume18sliceIndexZChangedEi', value,
    )

  def colorTableChanged(self) -> None:
    """
    Calls Qt's 'void QCustom3DVolume::colorTableChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dvolume.html#colorTableChanged
    """
    #  void QCustom3DVolume::colorTableChanged()
    self.uglySide.call('ritual_ZN15QCustom3DVolume17colorTableChangedEv')

  @overload(QImage.Format)
  def textureFormatChanged(self, format: QImage.Format) -> None:
    """
    Calls Qt's 'void QCustom3DVolume::textureFormatChanged(QImage::Format
    format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dvolume.html#textureFormatChanged

    Parameters
    ----------

    format : QImage.Format
      Passed on as its number.
    """
    #  void QCustom3DVolume::textureFormatChanged(QImage::Format format)
    self.uglySide.call(
        'ritual_ZN15QCustom3DVolume20textureFormatChangedEN6QImage6FormatE',
        format.value,
    )

  @overload(float)
  def alphaMultiplierChanged(self, mult: float) -> None:
    """
    Calls Qt's 'void QCustom3DVolume::alphaMultiplierChanged(float mult)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dvolume.html#alphaMultiplierChanged

    Parameters
    ----------

    mult : float
      Passed on as it is.
    """
    #  void QCustom3DVolume::alphaMultiplierChanged(float mult)
    self.uglySide.call(
        'ritual_ZN15QCustom3DVolume22alphaMultiplierChangedEf', mult,
    )

  @overload(bool)
  def preserveOpacityChanged(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QCustom3DVolume::preserveOpacityChanged(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dvolume.html#preserveOpacityChanged

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QCustom3DVolume::preserveOpacityChanged(bool enabled)
    self.uglySide.call(
        'ritual_ZN15QCustom3DVolume22preserveOpacityChangedEb', enabled,
    )

  @overload(bool)
  def useHighDefShaderChanged(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QCustom3DVolume::useHighDefShaderChanged(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dvolume.html#useHighDefShaderChanged

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QCustom3DVolume::useHighDefShaderChanged(bool enabled)
    self.uglySide.call(
        'ritual_ZN15QCustom3DVolume23useHighDefShaderChangedEb', enabled,
    )

  @overload(bool)
  def drawSlicesChanged(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QCustom3DVolume::drawSlicesChanged(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dvolume.html#drawSlicesChanged

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QCustom3DVolume::drawSlicesChanged(bool enabled)
    self.uglySide.call(
        'ritual_ZN15QCustom3DVolume17drawSlicesChangedEb', enabled,
    )

  @overload(bool)
  def drawSliceFramesChanged(self, enabled: bool) -> None:
    """
    Calls Qt's 'void QCustom3DVolume::drawSliceFramesChanged(bool enabled)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dvolume.html#drawSliceFramesChanged

    Parameters
    ----------

    enabled : bool
      Passed on as it is.
    """
    #  void QCustom3DVolume::drawSliceFramesChanged(bool enabled)
    self.uglySide.call(
        'ritual_ZN15QCustom3DVolume22drawSliceFramesChangedEb', enabled,
    )

  @overload(QColor)
  def sliceFrameColorChanged(self, color: QColor) -> None:
    """
    Calls Qt's 'void QCustom3DVolume::sliceFrameColorChanged(QColor color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dvolume.html#sliceFrameColorChanged

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QCustom3DVolume::sliceFrameColorChanged(QColor color)
    self.uglySide.call(
        'ritual_ZN15QCustom3DVolume22sliceFrameColorChangedE6QColor',
        self._valueOf(color),
    )

  @overload(QVector3D)
  def sliceFrameWidthsChanged(self, values: QVector3D) -> None:
    """
    Calls Qt's 'void QCustom3DVolume::sliceFrameWidthsChanged(QVector3D
    values)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dvolume.html#sliceFrameWidthsChanged

    Parameters
    ----------

    values : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QCustom3DVolume::sliceFrameWidthsChanged(QVector3D values)
    self.uglySide.call(
        'ritual_ZN15QCustom3DVolume23sliceFrameWidthsChangedE9QVector3D',
        self._valueOf(values),
    )

  @overload(QVector3D)
  def sliceFrameGapsChanged(self, values: QVector3D) -> None:
    """
    Calls Qt's 'void QCustom3DVolume::sliceFrameGapsChanged(QVector3D
    values)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dvolume.html#sliceFrameGapsChanged

    Parameters
    ----------

    values : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QCustom3DVolume::sliceFrameGapsChanged(QVector3D values)
    self.uglySide.call(
        'ritual_ZN15QCustom3DVolume21sliceFrameGapsChangedE9QVector3D',
        self._valueOf(values),
    )

  @overload(QVector3D)
  def sliceFrameThicknessesChanged(self, values: QVector3D) -> None:
    """
    Calls Qt's 'void QCustom3DVolume::sliceFrameThicknessesChanged(QVector3D
    values)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dvolume.html#sliceFrameThicknessesChanged

    Parameters
    ----------

    values : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QCustom3DVolume::sliceFrameThicknessesChanged(QVector3D values)
    self.uglySide.call(
        'ritual_ZN15QCustom3DVolume28sliceFrameThicknessesChangedE9QVector3'
        'D',
        self._valueOf(values),
    )

  @staticmethod
  def colorTable(*__, **_) -> Never:
    """
    Qt's 'QList<QRgb> QCustom3DVolume::colorTable() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QCustom3DVolume.colorTable' has no cute function yet. Qt's "
        "'QList<QRgb> QCustom3DVolume::colorTable() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def createTextureData(*__, **_) -> Never:
    """
    Qt's 'QList<uchar> *QCustom3DVolume::createTextureData(const QList<QImage
    *> &images)': gives 'QList<uchar>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QCustom3DVolume.createTextureData' has no cute function yet. Qt's "
        "'QList<uchar> *QCustom3DVolume::createTextureData(const "
        "QList<QImage *> &images)': gives 'QList<uchar>', which has no cute "
        "class yet.")

  @staticmethod
  def setColorTable(*__, **_) -> Never:
    """
    Qt's 'void QCustom3DVolume::setColorTable(const QList<QRgb> &colors)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QCustom3DVolume.setColorTable' has no cute function yet. Qt's "
        "'void QCustom3DVolume::setColorTable(const QList<QRgb> &colors)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def setTextureData(*__, **_) -> Never:
    """
    Qt's 'void QCustom3DVolume::setTextureData(QList<uchar> *data)': names
    'QList<uchar>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QCustom3DVolume.setTextureData' has no cute function yet. Qt's "
        "'void QCustom3DVolume::setTextureData(QList<uchar> *data)': names "
        "'QList<uchar>', which has no cute class yet.")

  @staticmethod
  def textureData(*__, **_) -> Never:
    """
    Qt's 'QList<uchar> *QCustom3DVolume::textureData() const': gives
    'QList<uchar>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QCustom3DVolume.textureData' has no cute function yet. Qt's "
        "'QList<uchar> *QCustom3DVolume::textureData() const': gives "
        "'QList<uchar>', which has no cute class yet.")

  @staticmethod
  def textureDataChanged(*__, **_) -> Never:
    """
    Qt's 'void QCustom3DVolume::textureDataChanged(QList<uchar> *data)':
    names 'QList<uchar>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QCustom3DVolume.textureDataChanged' has no cute function yet. "
        "Qt's 'void QCustom3DVolume::textureDataChanged(QList<uchar> "
        "*data)': names 'QList<uchar>', which has no cute class yet.")
