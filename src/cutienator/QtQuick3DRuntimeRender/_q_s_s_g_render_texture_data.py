"""
QSSGRenderTextureData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrendertexturedata_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGRenderTextureData to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QSSGRenderGraphObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QByteArray, QSize
  from ..QtQuick3DUtils import QSSGRenderTextureFormat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QSSGRenderTextureFormat = WAIT['QSSGRenderTextureFormat']
  QSize = WAIT['QSize']


class QSSGRenderTextureData(QSSGRenderGraphObject):
  """
  The cute side of Qt's QSSGRenderTextureData: a plain Python object standing
  in front of one C++ QSSGRenderTextureData.

  It is built on the cute 'QSSGRenderGraphObject', as Qt's
  QSSGRenderTextureData is built on Qt's QSSGRenderGraphObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QSSGRenderTextureData that has a ritual and that
  Python can call so far, 11 names in all: 'textureData', 'setTextureData',
  'size', 'setSize', 'depth', 'setDepth', 'format', 'setFormat',
  'hasTransparency', 'setHasTransparency', 'version'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGRenderTextureData::~QSSGRenderTextureData()': the destructor:
    Python never removes a C++ QSSGRenderTextureData.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QSSGRenderTextureData is created at the first use, not by
    'QSSGRenderTextureData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSSGRenderTextureData.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRenderTextureData'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def textureData(self) -> QByteArray:
    """
    Calls Qt's 'const QByteArray &QSSGRenderTextureData::textureData()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendertexturedata.html#textureData

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  const QByteArray &QSSGRenderTextureData::textureData() const
    address = self.uglySide.call(
        'ritual_ZNK21QSSGRenderTextureData11textureDataEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def size(self) -> QSize:
    """
    Calls Qt's 'QSize QSSGRenderTextureData::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrendertexturedata.html#size

    Returns
    -------

    QSize
      A new cute QSize around the copy Qt gave back. Python owns it.
    """
    #  QSize QSSGRenderTextureData::size() const
    address = self.uglySide.call('ritual_ZNK21QSSGRenderTextureData4sizeEv')
    from ..QtCore import QSize
    return QSize._cuteOwning(address)

  def depth(self) -> int:
    """
    Calls Qt's 'int QSSGRenderTextureData::depth() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrendertexturedata.html#depth
    """
    #  int QSSGRenderTextureData::depth() const
    return self.uglySide.call('ritual_ZNK21QSSGRenderTextureData5depthEv')

  def format(self) -> QSSGRenderTextureFormat:
    """
    Calls Qt's 'QSSGRenderTextureFormat QSSGRenderTextureData::format()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrendertexturedata.html#format

    Returns
    -------

    QSSGRenderTextureFormat
      A new cute QSSGRenderTextureFormat around the copy Qt gave back. Python
      owns it.
    """
    #  QSSGRenderTextureFormat QSSGRenderTextureData::format() const
    address = self.uglySide.call(
        'ritual_ZNK21QSSGRenderTextureData6formatEv',
    )
    from ..QtQuick3DUtils import QSSGRenderTextureFormat
    return QSSGRenderTextureFormat._cuteOwning(address)

  def hasTransparency(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderTextureData::hasTransparency() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendertexturedata.html#hasTransparency
    """
    #  bool QSSGRenderTextureData::hasTransparency() const
    return self.uglySide.call(
        'ritual_ZNK21QSSGRenderTextureData15hasTransparencyEv',
    )

  def version(self) -> int:
    """
    Calls Qt's 'quint32 QSSGRenderTextureData::version() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrendertexturedata.html#version
    """
    #  quint32 QSSGRenderTextureData::version() const
    return self.uglySide.call('ritual_ZNK21QSSGRenderTextureData7versionEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QByteArray)
  def setTextureData(self, data: QByteArray) -> None:
    """
    Calls Qt's 'void QSSGRenderTextureData::setTextureData(const QByteArray
    &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendertexturedata.html#setTextureData

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QSSGRenderTextureData::setTextureData(const QByteArray &data)
    self.uglySide.call(
        'ritual_ZN21QSSGRenderTextureData14setTextureDataERK10QByteArray',
        self._valueOf(data),
    )

  @overload(QSize)
  def setSize(self, size: QSize) -> None:
    """
    Calls Qt's 'void QSSGRenderTextureData::setSize(const QSize &size)'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrendertexturedata.html#setSize

    Parameters
    ----------

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QSSGRenderTextureData::setSize(const QSize &size)
    self.uglySide.call(
        'ritual_ZN21QSSGRenderTextureData7setSizeERK5QSize',
        self._valueOf(size),
    )

  @overload(int)
  def setDepth(self, depth: int) -> None:
    """
    Calls Qt's 'void QSSGRenderTextureData::setDepth(int depth)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendertexturedata.html#setDepth

    Parameters
    ----------

    depth : int
      Passed on as it is.
    """
    #  void QSSGRenderTextureData::setDepth(int depth)
    self.uglySide.call('ritual_ZN21QSSGRenderTextureData8setDepthEi', depth)

  @overload(QSSGRenderTextureFormat)
  def setFormat(self, format: QSSGRenderTextureFormat) -> None:
    """
    Calls Qt's 'void QSSGRenderTextureData::setFormat(QSSGRenderTextureFormat
    format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendertexturedata.html#setFormat

    Parameters
    ----------

    format : QSSGRenderTextureFormat
      Passed on as a value: Qt reads the C++ QSSGRenderTextureFormat, which
      stays Python's own.
    """
    #  void QSSGRenderTextureData::setFormat(QSSGRenderTextureFormat format)
    self.uglySide.call(
        'ritual_ZN21QSSGRenderTextureData9setFormatE23QSSGRenderTextureForm'
        'at',
        self._valueOf(format),
    )

  @overload(bool)
  def setHasTransparency(self, hasTransparency: bool) -> None:
    """
    Calls Qt's 'void QSSGRenderTextureData::setHasTransparency(bool
    hasTransparency)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendertexturedata.html#setHasTransparency

    Parameters
    ----------

    hasTransparency : bool
      Passed on as it is.
    """
    #  void QSSGRenderTextureData::setHasTransparency(bool hasTransparency)
    self.uglySide.call(
        'ritual_ZN21QSSGRenderTextureData18setHasTransparencyEb',
        hasTransparency,
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QSSGRenderTextureData::QSSGRenderTextureData()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendertexturedata.html#QSSGRenderTextureData
    """
    #  QSSGRenderTextureData::QSSGRenderTextureData()
    self._noteCreation(QSSGRenderTextureData, lambda: Rituals.call(
        'ritual_ZN21QSSGRenderTextureDataC1Ev',
    ))

  @overload(QSSGRenderGraphObject.Type)
  def __init__(self, inType: QSSGRenderGraphObject.Type) -> None:
    """
    Notes what was given, for Qt's
    'QSSGRenderTextureData::QSSGRenderTextureData(QSSGRenderGraphObject::Type
    inType)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrendertexturedata.html#QSSGRenderTextureData

    Parameters
    ----------

    inType : QSSGRenderGraphObject.Type
      Passed on as its number.
    """
    #  QSSGRenderTextureData::QSSGRenderTextureData(
    #      QSSGRenderGraphObject::Type inType)
    self._noteCreation(QSSGRenderTextureData, lambda: Rituals.call(
        'ritual_ZN21QSSGRenderTextureDataC1EN21QSSGRenderGraphObject4TypeE',
        inType.value,
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
