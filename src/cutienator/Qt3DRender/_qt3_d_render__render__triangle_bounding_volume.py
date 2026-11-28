"""
Qt3DRender::Render::TriangleBoundingVolume binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/triangleboundingvolume_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Qt3DRender::Render::TriangleBoundingVolume to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtGui import QVector3D
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVector3D = WAIT['QVector3D']


class TriangleBoundingVolume(Qt3DRender.RayCasting.QBoundingVolume):
  """
  The cute side of Qt's Qt3DRender::Render::TriangleBoundingVolume: a plain
  Python object standing in front of one C++
  Qt3DRender::Render::TriangleBoundingVolume.

  It is built on the cute 'Qt3DRender::RayCasting::QBoundingVolume', as Qt's
  Qt3DRender::Render::TriangleBoundingVolume is built on Qt's
  Qt3DRender::RayCasting::QBoundingVolume, and has everything that class has.

  C++ hands a Qt3DRender::Render::TriangleBoundingVolume around as a copy, so
  every C++ Qt3DRender::Render::TriangleBoundingVolume behind a cute one is
  Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::TriangleBoundingVolume that has
  a ritual and that Python can call so far, 8 names in all: 'id', 'type',
  'a', 'b', 'c', 'setA', 'setB', 'setC'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'Qt3DRender::Render::TriangleBoundingVolume::~TriangleBoundingVolume()':
    the destructor: Python removes its C++
    Qt3DRender::Render::TriangleBoundingVolume by it, and has no other use
    for it.

  What has no ritual
  ------------------

  5 of the 14 functions Qt declares: 5 leans on 'Qt3DRender.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::TriangleBoundingVolume is created at the
    first use, not by 'Qt3DRender::Render::TriangleBoundingVolume(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DRender::Render::TriangleBoundingVolume back gives
    a copy the ritual made for Python, in a new cute
    Qt3DRender::Render::TriangleBoundingVolume.
  - Each name of Qt's Qt3DRender::Render::TriangleBoundingVolume that has no
    cute function yet, '__init__', 'transform', 'transformed', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::TriangleBoundingVolume'

  #  Qt's '~Qt3DRender::Render::TriangleBoundingVolume()'. Naming it makes
  #  this a value class: Python owns every C++
  #  Qt3DRender::Render::TriangleBoundingVolume behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN10Qt3DRender6Render22TriangleBoundingVolumeD1Ev')

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def id(self) -> Qt3DCore.QNodeId:
    """
    Calls Qt's 'Qt3DCore::QNodeId
    Qt3DRender::Render::TriangleBoundingVolume::id() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-triangleboundingvolume.html#id

    Returns
    -------

    Qt3DCore.QNodeId
      A new cute Qt3DCore::QNodeId around the copy Qt gave back. Python owns
      it.
    """
    #  Qt3DCore::QNodeId Qt3DRender::Render::TriangleBoundingVolume::id()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render22TriangleBoundingVolume2idEv',
    )
    return Qt3DCore.QNodeId._cuteOwning(address)

  def type(self) -> Qt3DRender.RayCasting.QBoundingVolume.Type:
    """
    Calls Qt's 'Type Qt3DRender::Render::TriangleBoundingVolume::type()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-triangleboundingvolume.html#type

    Returns
    -------

    Qt3DRender.RayCasting.QBoundingVolume.Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DRender.RayCasting.QBoundingVolume.Type(number)' gives.
    """
    #  Type Qt3DRender::Render::TriangleBoundingVolume::type() const
    return Qt3DRender.RayCasting.QBoundingVolume.Type(self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render22TriangleBoundingVolume4typeEv',
    ))

  def a(self) -> QVector3D:
    """
    Calls Qt's 'Vector3D Qt3DRender::Render::TriangleBoundingVolume::a()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-triangleboundingvolume.html#a

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  Vector3D Qt3DRender::Render::TriangleBoundingVolume::a() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render22TriangleBoundingVolume1aEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def b(self) -> QVector3D:
    """
    Calls Qt's 'Vector3D Qt3DRender::Render::TriangleBoundingVolume::b()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-triangleboundingvolume.html#b

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  Vector3D Qt3DRender::Render::TriangleBoundingVolume::b() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render22TriangleBoundingVolume1bEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def c(self) -> QVector3D:
    """
    Calls Qt's 'Vector3D Qt3DRender::Render::TriangleBoundingVolume::c()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-triangleboundingvolume.html#c

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  Vector3D Qt3DRender::Render::TriangleBoundingVolume::c() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render22TriangleBoundingVolume1cEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVector3D)
  def setA(self, a: QVector3D) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::TriangleBoundingVolume::setA(const
    Vector3D &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-triangleboundingvolume.html#setA

    Parameters
    ----------

    a : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Qt3DRender::Render::TriangleBoundingVolume::setA(const Vector3D
    #      &a)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render22TriangleBoundingVolume4setAERK9QVect'
        'or3D',
        self._valueOf(a),
    )

  @overload(QVector3D)
  def setB(self, b: QVector3D) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::TriangleBoundingVolume::setB(const
    Vector3D &b)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-triangleboundingvolume.html#setB

    Parameters
    ----------

    b : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Qt3DRender::Render::TriangleBoundingVolume::setB(const Vector3D
    #      &b)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render22TriangleBoundingVolume4setBERK9QVect'
        'or3D',
        self._valueOf(b),
    )

  @overload(QVector3D)
  def setC(self, c: QVector3D) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::TriangleBoundingVolume::setC(const
    Vector3D &c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-triangleboundingvolume.html#setC

    Parameters
    ----------

    c : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void Qt3DRender::Render::TriangleBoundingVolume::setC(const Vector3D
    #      &c)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render22TriangleBoundingVolume4setCERK9QVect'
        'or3D',
        self._valueOf(c),
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
    - Qt's
      'Qt3DRender::Render::TriangleBoundingVolume::TriangleBoundingVolume()':
      leans on 'Qt3DRender::Render::intersectsSegmentTriangle(Qt3DRender::
      RayCasting::QRay3D const&, QVector3D const&, QVector3D const&,
      QVector3D const&, QVector3D&, float&)', which Qt's source does not mark
      for use from outside Qt and has no code for that could be taken.
    - Qt's
      'Qt3DRender::Render::TriangleBoundingVolume::TriangleBoundingVolume(
      Qt3DCore::QNodeId id, const Vector3D &a, const Vector3D &b, const
      Vector3D &c)': leans on
      'Qt3DRender::Render::intersectsSegmentTriangle(Qt3DRender::
      RayCasting::QRay3D const&, QVector3D const&, QVector3D const&,
      QVector3D const&, QVector3D&, float&)', which Qt's source does not mark
      for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.TriangleBoundingVolume.__init__' has no cute "
        "function yet. Qt's "
        "'Qt3DRender::Render::TriangleBoundingVolume::TriangleBoundingVolume"
        "()': leans on "
        "'Qt3DRender::Render::intersectsSegmentTriangle(Qt3DRender::RayCasti"
        "ng::QRay3D const&, QVector3D const&, QVector3D const&, QVector3D "
        "const&, QVector3D&, float&)', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken. Qt's "
        "'Qt3DRender::Render::TriangleBoundingVolume::TriangleBoundingVolume"
        "(Qt3DCore::QNodeId id, const Vector3D &a, const Vector3D &b, const "
        "Vector3D &c)': leans on "
        "'Qt3DRender::Render::intersectsSegmentTriangle(Qt3DRender::RayCasti"
        "ng::QRay3D const&, QVector3D const&, QVector3D const&, QVector3D "
        "const&, QVector3D&, float&)', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

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

  @staticmethod
  def transform(*__, **_) -> Never:
    """
    Qt's 'TriangleBoundingVolume
    &Qt3DRender::Render::TriangleBoundingVolume::transform(const Matrix4x4
    &mat)': leans on
    'Qt3DRender::Render::intersectsSegmentTriangle(Qt3DRender::RayCasting::
    QRay3D const&, QVector3D const&, QVector3D const&, QVector3D const&,
    QVector3D&, float&)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.TriangleBoundingVolume.transform' has no cute "
        "function yet. Qt's 'TriangleBoundingVolume "
        "&Qt3DRender::Render::TriangleBoundingVolume::transform(const "
        "Matrix4x4 &mat)': leans on "
        "'Qt3DRender::Render::intersectsSegmentTriangle(Qt3DRender::RayCasti"
        "ng::QRay3D const&, QVector3D const&, QVector3D const&, QVector3D "
        "const&, QVector3D&, float&)', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def transformed(*__, **_) -> Never:
    """
    Qt's 'TriangleBoundingVolume
    Qt3DRender::Render::TriangleBoundingVolume::transformed(const Matrix4x4
    &mat) const': leans on
    'Qt3DRender::Render::intersectsSegmentTriangle(Qt3DRender::RayCasting::
    QRay3D const&, QVector3D const&, QVector3D const&, QVector3D const&,
    QVector3D&, float&)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.TriangleBoundingVolume.transformed' has no cute "
        "function yet. Qt's 'TriangleBoundingVolume "
        "Qt3DRender::Render::TriangleBoundingVolume::transformed(const "
        "Matrix4x4 &mat) const': leans on "
        "'Qt3DRender::Render::intersectsSegmentTriangle(Qt3DRender::RayCasti"
        "ng::QRay3D const&, QVector3D const&, QVector3D const&, QVector3D "
        "const&, QVector3D&, float&)', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")
