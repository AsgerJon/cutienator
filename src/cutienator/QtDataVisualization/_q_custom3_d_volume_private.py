"""
QCustom3DVolumePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/qcustom3dvolume_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QCustom3DVolumePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..QtCore import Qt
from . import QCustom3DItemPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QImage
  from . import QCustom3DVolume


class QCustom3DVolumePrivate(QCustom3DItemPrivate):
  """
  The cute side of Qt's QCustom3DVolumePrivate: a plain Python object
  standing in front of one C++ QCustom3DVolumePrivate.

  It is built on the cute 'QCustom3DItemPrivate', as Qt's
  QCustom3DVolumePrivate is built on Qt's QCustom3DItemPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QCustom3DVolumePrivate that has a ritual and that
  Python can call so far, 5 names in all: 'metaObject', 'resetDirtyBits',
  'renderSlice', 'qptr', 'multipliedAlphaValue'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QCustom3DVolumePrivate::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QCustom3DVolumePrivate::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QCustom3DVolumePrivate::~QCustom3DVolumePrivate()': the destructor:
    Python never removes a C++ QCustom3DVolumePrivate.

  What has no ritual
  ------------------

  5 of the 13 functions Qt declares: 3 leans on 'QCustom3DVolumePrivate; 2
  not a gap.

  What to expect
  --------------

  - The C++ QCustom3DVolumePrivate is created at the first use, not by
    'QCustom3DVolumePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCustom3DVolumePrivate.
  - Qt tells when it has removed the C++ QCustom3DVolumePrivate. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QCustom3DVolumePrivate that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
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
  __qt_class__ = 'QCustom3DVolumePrivate'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtDataVisualization'

  #  A C++ QCustom3DVolumePrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCustom3DVolumePrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QCustom3DVolumePrivate::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dvolumeprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QCustom3DVolumePrivate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QCustom3DVolumePrivate10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    - Qt's 'QCustom3DVolumePrivate::QCustom3DVolumePrivate(QCustom3DVolume
      *q)': leans on 'QCustom3DVolumePrivate::qt_metacall(QMetaObject::Call,
      int, void**)', which Qt's source does not mark for use from outside Qt
      and has no code for that could be taken.
    - Qt's 'QCustom3DVolumePrivate::QCustom3DVolumePrivate(QCustom3DVolume
      *q, const QVector3D &position, const QVector3D &scaling, const
      QQuaternion &rotation, int textureWidth, int textureHeight, int
      textureDepth, QList<uchar> *textureData, QImage::Format textureFormat,
      const QList<QRgb> &colorTable)': leans on
      'QCustom3DVolumePrivate::qt_metacall(QMetaObject::Call, int, void**)',
      which Qt's source does not mark for use from outside Qt and has no code
      for that could be taken.
    """
    raise NotImplementedError(
        "'QCustom3DVolumePrivate.__init__' has no cute function yet. Qt's "
        "'QCustom3DVolumePrivate::QCustom3DVolumePrivate(QCustom3DVolume "
        "*q)': leans on "
        "'QCustom3DVolumePrivate::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken. Qt's "
        "'QCustom3DVolumePrivate::QCustom3DVolumePrivate(QCustom3DVolume "
        "*q, const QVector3D &position, const QVector3D &scaling, const "
        "QQuaternion &rotation, int textureWidth, int textureHeight, int "
        "textureDepth, QList<uchar> *textureData, QImage::Format "
        "textureFormat, const QList<QRgb> &colorTable)': leans on "
        "'QCustom3DVolumePrivate::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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

  def resetDirtyBits(self) -> None:
    """
    Calls Qt's 'void QCustom3DVolumePrivate::resetDirtyBits()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dvolumeprivate.html#resetDirtyBits
    """
    #  void QCustom3DVolumePrivate::resetDirtyBits()
    self.uglySide.call('ritual_ZN22QCustom3DVolumePrivate14resetDirtyBitsEv')

  @overload(Qt.Axis, int)
  def renderSlice(self, axis: Qt.Axis, index: int) -> QImage:
    """
    Calls Qt's 'QImage QCustom3DVolumePrivate::renderSlice(Qt::Axis axis, int
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dvolumeprivate.html#renderSlice

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
    #  QImage QCustom3DVolumePrivate::renderSlice(Qt::Axis axis, int index)
    address = self.uglySide.call(
        'ritual_ZN22QCustom3DVolumePrivate11renderSliceEN2Qt4AxisEi',
        axis.value, index,
    )
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  def qptr(self) -> Optional[QCustom3DVolume]:
    """
    Calls Qt's 'QCustom3DVolume *QCustom3DVolumePrivate::qptr()'.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3dvolumeprivate.html#qptr

    Returns
    -------

    Optional[QCustom3DVolume]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCustom3DVolume *QCustom3DVolumePrivate::qptr()
    address = self.uglySide.call('ritual_ZN22QCustom3DVolumePrivate4qptrEv')
    from . import QCustom3DVolume
    return QCustom3DVolume._cuteAt(address)

  @overload(int)
  def multipliedAlphaValue(self, alpha: int) -> int:
    """
    Calls Qt's 'int QCustom3DVolumePrivate::multipliedAlphaValue(int alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dvolumeprivate.html#multipliedAlphaValue

    Parameters
    ----------

    alpha : int
      Passed on as it is.
    """
    #  int QCustom3DVolumePrivate::multipliedAlphaValue(int alpha)
    return self.uglySide.call(
        'ritual_ZN22QCustom3DVolumePrivate20multipliedAlphaValueEi', alpha,
    )
