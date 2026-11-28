"""
QCustom3DItemPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDataVisualization/6.12.0/QtDataVisualization/private/qcustom3ditem_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QCustom3DItemPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from ..QtGui import QImage


class QCustom3DItemPrivate(QObject):
  """
  The cute side of Qt's QCustom3DItemPrivate: a plain Python object standing
  in front of one C++ QCustom3DItemPrivate.

  It is built on the cute 'QObject', as Qt's QCustom3DItemPrivate is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QCustom3DItemPrivate that has a ritual and that
  Python can call so far, 5 names in all: 'metaObject', 'textureImage',
  'clearTextureImage', 'resetDirtyBits', 'needUpdate'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QCustom3DItemPrivate::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QCustom3DItemPrivate::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QCustom3DItemPrivate::~QCustom3DItemPrivate()': the destructor:
    Python never removes a C++ QCustom3DItemPrivate.

  What has no ritual
  ------------------

  6 of the 14 functions Qt declares: 4 leans on 'QCustom3DItemPrivate; 2 not
  a gap.

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
  - Qt tells when it has removed the C++ QCustom3DItemPrivate. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QCustom3DItemPrivate that has no cute function yet,
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
  __qt_class__ = 'QCustom3DItemPrivate'
  #  The part of Qt it is of, as another part has a class of its name too.
  __qt_part__ = 'QtDataVisualization'

  #  A C++ QCustom3DItemPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCustom3DItemPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QCustom3DItemPrivate::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3ditemprivate.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QCustom3DItemPrivate::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QCustom3DItemPrivate10metaObjectEv',
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
    - Qt's 'QCustom3DItemPrivate::QCustom3DItemPrivate(QCustom3DItem *q)':
      leans on 'QCustom3DItemPrivate::qt_metacall(QMetaObject::Call, int,
      void**)', which Qt's source does not mark for use from outside Qt and
      has no code for that could be taken.
    - Qt's 'QCustom3DItemPrivate::QCustom3DItemPrivate(QCustom3DItem *q,
      const QString &meshFile, const QVector3D &position, const QVector3D
      &scaling, const QQuaternion &rotation)': leans on
      'QCustom3DItemPrivate::qt_metacall(QMetaObject::Call, int, void**)',
      which Qt's source does not mark for use from outside Qt and has no code
      for that could be taken.
    - Qt's 'QCustom3DItemPrivate::QCustom3DItemPrivate(QCustom3DItemPrivate
      *d)': leans on 'QCustom3DItemPrivate::qt_metacall(QMetaObject::Call,
      int, void**)', which Qt's source does not mark for use from outside Qt
      and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCustom3DItemPrivate.__init__' has no cute function yet. Qt's "
        "'QCustom3DItemPrivate::QCustom3DItemPrivate(QCustom3DItem *q)': "
        "leans on 'QCustom3DItemPrivate::qt_metacall(QMetaObject::Call, "
        "int, void**)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken. Qt's "
        "'QCustom3DItemPrivate::QCustom3DItemPrivate(QCustom3DItem *q, "
        "const QString &meshFile, const QVector3D &position, const "
        "QVector3D &scaling, const QQuaternion &rotation)': leans on "
        "'QCustom3DItemPrivate::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken. Qt's "
        "'QCustom3DItemPrivate::QCustom3DItemPrivate(QCustom3DItemPrivate "
        "*d)': leans on "
        "'QCustom3DItemPrivate::qt_metacall(QMetaObject::Call, int, "
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

  def needUpdate(self) -> None:
    """
    Calls Qt's 'void QCustom3DItemPrivate::needUpdate()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcustom3ditemprivate.html#needUpdate
    """
    #  void QCustom3DItemPrivate::needUpdate()
    self.uglySide.call('ritual_ZN20QCustom3DItemPrivate10needUpdateEv')
