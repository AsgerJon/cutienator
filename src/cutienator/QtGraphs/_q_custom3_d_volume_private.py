"""
QCustom3DVolumePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/6.12.0/QtGraphs/private/qcustom3dvolume_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QCustom3DVolumePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QCustom3DItemPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

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
  Python can call so far, 3 names in all: 'q_func', 'resetDirtyBits',
  'multipliedAlphaValue'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QCustom3DVolume *QCustom3DVolumePrivate::q_func() const':
    takes in Python what 'QCustom3DVolume *QCustom3DVolumePrivate::q_func()'
    takes.
  - Qt's 'QCustom3DVolumePrivate::QCustom3DVolumePrivate(QVector3D position,
    QVector3D scaling, const QQuaternion &rotation, int textureWidth, int
    textureHeight, int textureDepth, QList<uchar> *textureData,
    QImage::Format textureFormat, const QList<QRgb> &colorTable)': names
    'QList<uchar>', which has no cute class yet.
  - Qt's 'QCustom3DVolumePrivate::~QCustom3DVolumePrivate()': the destructor:
    Python never removes a C++ QCustom3DVolumePrivate.

  What has no ritual
  ------------------

  1 of the 8 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

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
  - Each name of Qt's QCustom3DVolumePrivate that has no cute function yet,
    'renderSlice', holds a function that raises 'NotImplementedError', and
    its docstring says why.
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
  __qt_part__ = 'QtGraphs'

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
    'QCustom3DVolumePrivate::QCustom3DVolumePrivate()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dvolumeprivate.html#QCustom3DVolumePrivate
    """
    #  QCustom3DVolumePrivate::QCustom3DVolumePrivate()
    self._noteCreation(QCustom3DVolumePrivate, lambda: Rituals.call(
        'ritual_ZN22QCustom3DVolumePrivateC1Ev',
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

  def q_func(self) -> Optional[QCustom3DVolume]:
    """
    Calls Qt's 'QCustom3DVolume *QCustom3DVolumePrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3dvolumeprivate.html#q_func

    Returns
    -------

    Optional[QCustom3DVolume]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCustom3DVolume *QCustom3DVolumePrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN22QCustom3DVolumePrivate6q_funcEv',
    )
    from . import QCustom3DVolume
    return QCustom3DVolume._cuteAt(address)

  def resetDirtyBits(self) -> None:
    """
    Calls Qt's 'void QCustom3DVolumePrivate::resetDirtyBits()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3dvolumeprivate.html#resetDirtyBits
    """
    #  void QCustom3DVolumePrivate::resetDirtyBits()
    self.uglySide.call('ritual_ZN22QCustom3DVolumePrivate14resetDirtyBitsEv')

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

  @staticmethod
  def renderSlice(*__, **_) -> Never:
    """
    Qt's 'QImage QCustom3DVolumePrivate::renderSlice(Qt::Axis axis, int
    index)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'QGraphs3DCustomVolumeRenderSlice'.
    """
    raise NotImplementedError(
        "'QCustom3DVolumePrivate.renderSlice' has no cute function yet. "
        "Qt's 'QImage QCustom3DVolumePrivate::renderSlice(Qt::Axis axis, "
        "int index)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'QGraphs3DCustomVolumeRenderSlice'.")
