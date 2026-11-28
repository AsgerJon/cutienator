"""
QCustom3DItemPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGraphs/6.12.0/QtGraphs/private/qcustom3ditem_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QCustom3DItemPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QImage, QQuaternion, QVector3D
  from . import QCustom3DItem
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuaternion = WAIT['QQuaternion']
  QVector3D = WAIT['QVector3D']


class QCustom3DItemPrivate(QObjectPrivate):
  """
  The cute side of Qt's QCustom3DItemPrivate: a plain Python object standing
  in front of one C++ QCustom3DItemPrivate.

  It is built on the cute 'QObjectPrivate', as Qt's QCustom3DItemPrivate is
  built on Qt's QObjectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QCustom3DItemPrivate that has a ritual and that
  Python can call so far, 4 names in all: 'q_func', 'textureImage',
  'clearTextureImage', 'resetDirtyBits'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QCustom3DItem *QCustom3DItemPrivate::q_func() const': takes
    in Python what 'QCustom3DItem *QCustom3DItemPrivate::q_func()' takes.
  - Qt's 'QCustom3DItemPrivate::~QCustom3DItemPrivate()': the destructor:
    Python never removes a C++ QCustom3DItemPrivate.

  What has no ritual
  ------------------

  1 of the 9 functions Qt declares: 1 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QCustom3DItemPrivate is created at the first use, not by
    'QCustom3DItemPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCustom3DItemPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCustom3DItemPrivate'
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
    'QCustom3DItemPrivate::QCustom3DItemPrivate()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3ditemprivate.html#QCustom3DItemPrivate
    """
    #  QCustom3DItemPrivate::QCustom3DItemPrivate()
    self._noteCreation(QCustom3DItemPrivate, lambda: Rituals.call(
        'ritual_ZN20QCustom3DItemPrivateC1Ev',
    ))

  @overload(str, QVector3D, QVector3D, QQuaternion)
  def __init__(
      self,
      meshFile: str,
      position: QVector3D,
      scaling: QVector3D,
      rotation: QQuaternion,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QCustom3DItemPrivate::QCustom3DItemPrivate(const QString &meshFile,
    QVector3D position, QVector3D scaling, const QQuaternion &rotation)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3ditemprivate.html#QCustom3DItemPrivate

    Parameters
    ----------

    meshFile : str
      Passed on as it is: a QString is made of it for the call.

    position : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    scaling : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.

    rotation : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.
    """
    #  QCustom3DItemPrivate::QCustom3DItemPrivate(const QString &meshFile,
    #      QVector3D position, QVector3D scaling, const QQuaternion
    #      &rotation)
    self._noteCreation(QCustom3DItemPrivate, lambda: Rituals.call(
        'ritual_ZN20QCustom3DItemPrivateC1ERK7QString9QVector3DS3_RK11QQuat'
        'ernion',
        meshFile, self._valueOf(position), self._valueOf(scaling),
        self._valueOf(rotation),
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

  def q_func(self) -> Optional[QCustom3DItem]:
    """
    Calls Qt's 'QCustom3DItem *QCustom3DItemPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qcustom3ditemprivate.html#q_func

    Returns
    -------

    Optional[QCustom3DItem]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCustom3DItem *QCustom3DItemPrivate::q_func()
    address = self.uglySide.call('ritual_ZN20QCustom3DItemPrivate6q_funcEv')
    from . import QCustom3DItem
    return QCustom3DItem._cuteAt(address)

  def textureImage(self) -> QImage:
    """
    Calls Qt's 'QImage QCustom3DItemPrivate::textureImage()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3ditemprivate.html#textureImage

    Returns
    -------

    QImage
      A new cute QImage around the copy Qt gave back. Python owns it.
    """
    #  QImage QCustom3DItemPrivate::textureImage()
    address = self.uglySide.call(
        'ritual_ZN20QCustom3DItemPrivate12textureImageEv',
    )
    from ..QtGui import QImage
    return QImage._cuteOwning(address)

  def clearTextureImage(self) -> None:
    """
    Calls Qt's 'void QCustom3DItemPrivate::clearTextureImage()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3ditemprivate.html#clearTextureImage
    """
    #  void QCustom3DItemPrivate::clearTextureImage()
    self.uglySide.call(
        'ritual_ZN20QCustom3DItemPrivate17clearTextureImageEv',
    )

  def resetDirtyBits(self) -> None:
    """
    Calls Qt's 'void QCustom3DItemPrivate::resetDirtyBits()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3ditemprivate.html#resetDirtyBits
    """
    #  void QCustom3DItemPrivate::resetDirtyBits()
    self.uglySide.call('ritual_ZN20QCustom3DItemPrivate14resetDirtyBitsEv')
