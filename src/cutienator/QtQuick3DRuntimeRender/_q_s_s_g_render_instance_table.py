"""
QSSGRenderInstanceTable binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderinstancetable_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGRenderInstanceTable to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QSSGRenderGraphObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArray
  from ..QtGui import QMatrix4x4, QVector3D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QVector3D = WAIT['QVector3D']


class QSSGRenderInstanceTable(QSSGRenderGraphObject):
  """
  The cute side of Qt's QSSGRenderInstanceTable: a plain Python object
  standing in front of one C++ QSSGRenderInstanceTable.

  It is built on the cute 'QSSGRenderGraphObject', as Qt's
  QSSGRenderInstanceTable is built on Qt's QSSGRenderGraphObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QSSGRenderInstanceTable that has a ritual and that
  Python can call so far, 15 names in all: 'count', 'dataSize', 'setData',
  'setInstanceCountOverride', 'serial', 'stride', 'hasTransparency',
  'setHasTransparency', 'setDepthSorting', 'isDepthSortingEnabled',
  'getTransform', 'setShadowBoundsMinimum', 'setShadowBoundsMaximum',
  'getShadowBoundsMinimum', 'getShadowBoundsMaximum'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const void *QSSGRenderInstanceTable::constData() const': gives
    'void', which has no cute class yet.

  What to expect
  --------------

  - The C++ QSSGRenderInstanceTable is created at the first use, not by
    'QSSGRenderInstanceTable(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSSGRenderInstanceTable.
  - Each name of Qt's QSSGRenderInstanceTable that has no cute function yet,
    'constData', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSSGRenderInstanceTable'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def count(self) -> int:
    """
    Calls Qt's 'int QSSGRenderInstanceTable::count() const'.

    Qt's own words: https://doc.qt.io/qt-6/qssgrenderinstancetable.html#count
    """
    #  int QSSGRenderInstanceTable::count() const
    return self.uglySide.call('ritual_ZNK23QSSGRenderInstanceTable5countEv')

  def dataSize(self) -> int:
    """
    Calls Qt's 'qsizetype QSSGRenderInstanceTable::dataSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderinstancetable.html#dataSize
    """
    #  qsizetype QSSGRenderInstanceTable::dataSize() const
    return self.uglySide.call(
        'ritual_ZNK23QSSGRenderInstanceTable8dataSizeEv',
    )

  def serial(self) -> int:
    """
    Calls Qt's 'int QSSGRenderInstanceTable::serial() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderinstancetable.html#serial
    """
    #  int QSSGRenderInstanceTable::serial() const
    return self.uglySide.call('ritual_ZNK23QSSGRenderInstanceTable6serialEv')

  def stride(self) -> int:
    """
    Calls Qt's 'int QSSGRenderInstanceTable::stride() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderinstancetable.html#stride
    """
    #  int QSSGRenderInstanceTable::stride() const
    return self.uglySide.call('ritual_ZNK23QSSGRenderInstanceTable6strideEv')

  @overload(int)
  def getTransform(self, index: int) -> QMatrix4x4:
    """
    Calls Qt's 'QMatrix4x4 QSSGRenderInstanceTable::getTransform(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderinstancetable.html#getTransform

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QMatrix4x4
      A new cute QMatrix4x4 around the copy Qt gave back. Python owns it.
    """
    #  QMatrix4x4 QSSGRenderInstanceTable::getTransform(int index) const
    address = self.uglySide.call(
        'ritual_ZNK23QSSGRenderInstanceTable12getTransformEi', index,
    )
    from ..QtGui import QMatrix4x4
    return QMatrix4x4._cuteOwning(address)

  def getShadowBoundsMinimum(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QSSGRenderInstanceTable::getShadowBoundsMinimum()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderinstancetable.html

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QSSGRenderInstanceTable::getShadowBoundsMinimum() const
    address = self.uglySide.call(
        'ritual_ZNK23QSSGRenderInstanceTable22getShadowBoundsMinimumEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def getShadowBoundsMaximum(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QSSGRenderInstanceTable::getShadowBoundsMaximum()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderinstancetable.html

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QSSGRenderInstanceTable::getShadowBoundsMaximum() const
    address = self.uglySide.call(
        'ritual_ZNK23QSSGRenderInstanceTable22getShadowBoundsMaximumEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QByteArray, int, int)
  def setData(self, data: QByteArray, count: int, stride: int) -> None:
    """
    Calls Qt's 'void QSSGRenderInstanceTable::setData(const QByteArray &data,
    int count, int stride)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderinstancetable.html#setData

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    count : int
      Passed on as it is.

    stride : int
      Passed on as it is.
    """
    #  void QSSGRenderInstanceTable::setData(const QByteArray &data, int
    #      count, int stride)
    self.uglySide.call(
        'ritual_ZN23QSSGRenderInstanceTable7setDataERK10QByteArrayii',
        self._valueOf(data), count, stride,
    )

  @overload(int)
  def setInstanceCountOverride(self, count: int) -> None:
    """
    Calls Qt's 'void QSSGRenderInstanceTable::setInstanceCountOverride(int
    count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderinstancetable.html

    Parameters
    ----------

    count : int
      Passed on as it is.
    """
    #  void QSSGRenderInstanceTable::setInstanceCountOverride(int count)
    self.uglySide.call(
        'ritual_ZN23QSSGRenderInstanceTable24setInstanceCountOverrideEi',
        count,
    )

  @overload(bool)
  def setHasTransparency(self, t: bool) -> None:
    """
    Calls Qt's 'void QSSGRenderInstanceTable::setHasTransparency(bool t)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderinstancetable.html#setHasTransparency

    Parameters
    ----------

    t : bool
      Passed on as it is.
    """
    #  void QSSGRenderInstanceTable::setHasTransparency(bool t)
    self.uglySide.call(
        'ritual_ZN23QSSGRenderInstanceTable18setHasTransparencyEb', t,
    )

  @overload(bool)
  def setDepthSorting(self, enable: bool) -> None:
    """
    Calls Qt's 'void QSSGRenderInstanceTable::setDepthSorting(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderinstancetable.html#setDepthSorting

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QSSGRenderInstanceTable::setDepthSorting(bool enable)
    self.uglySide.call(
        'ritual_ZN23QSSGRenderInstanceTable15setDepthSortingEb', enable,
    )

  @overload(QVector3D)
  def setShadowBoundsMinimum(self, value: QVector3D) -> None:
    """
    Calls Qt's 'void QSSGRenderInstanceTable::setShadowBoundsMinimum(const
    QVector3D &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderinstancetable.html

    Parameters
    ----------

    value : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QSSGRenderInstanceTable::setShadowBoundsMinimum(const QVector3D
    #      &value)
    self.uglySide.call(
        'ritual_ZN23QSSGRenderInstanceTable22setShadowBoundsMinimumERK9QVec'
        'tor3D',
        self._valueOf(value),
    )

  @overload(QVector3D)
  def setShadowBoundsMaximum(self, value: QVector3D) -> None:
    """
    Calls Qt's 'void QSSGRenderInstanceTable::setShadowBoundsMaximum(const
    QVector3D &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderinstancetable.html

    Parameters
    ----------

    value : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QSSGRenderInstanceTable::setShadowBoundsMaximum(const QVector3D
    #      &value)
    self.uglySide.call(
        'ritual_ZN23QSSGRenderInstanceTable22setShadowBoundsMaximumERK9QVec'
        'tor3D',
        self._valueOf(value),
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
    'QSSGRenderInstanceTable::QSSGRenderInstanceTable()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderinstancetable.html
    """
    #  QSSGRenderInstanceTable::QSSGRenderInstanceTable()
    self._noteCreation(QSSGRenderInstanceTable, lambda: Rituals.call(
        'ritual_ZN23QSSGRenderInstanceTableC1Ev',
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

  def hasTransparency(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderInstanceTable::hasTransparency()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderinstancetable.html#hasTransparency
    """
    #  bool QSSGRenderInstanceTable::hasTransparency()
    return self.uglySide.call(
        'ritual_ZN23QSSGRenderInstanceTable15hasTransparencyEv',
    )

  def isDepthSortingEnabled(self) -> bool:
    """
    Calls Qt's 'bool QSSGRenderInstanceTable::isDepthSortingEnabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qssgrenderinstancetable.html#isDepthSortingEnabled
    """
    #  bool QSSGRenderInstanceTable::isDepthSortingEnabled()
    return self.uglySide.call(
        'ritual_ZN23QSSGRenderInstanceTable21isDepthSortingEnabledEv',
    )

  @staticmethod
  def constData(*__, **_) -> Never:
    """
    Qt's 'const void *QSSGRenderInstanceTable::constData() const': gives
    'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QSSGRenderInstanceTable.constData' has no cute function yet. Qt's "
        "'const void *QSSGRenderInstanceTable::constData() const': gives "
        "'void', which has no cute class yet.")
