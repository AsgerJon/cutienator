"""
QQuick3DGeometryPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dgeometry_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuick3DGeometryPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QQuick3DGeometry, QQuick3DObjectPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArray
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QQuick3DGeometryPrivate(QQuick3DObjectPrivate):
  """
  The cute side of Qt's QQuick3DGeometryPrivate: a plain Python object
  standing in front of one C++ QQuick3DGeometryPrivate.

  It is built on the cute 'QQuick3DObjectPrivate', as Qt's
  QQuick3DGeometryPrivate is built on Qt's QQuick3DObjectPrivate, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DGeometryPrivate that has a ritual and that
  Python can call so far, 1 name in all: 'semanticFromName'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuick3DGeometry::Attribute::ComponentType
    QQuick3DGeometryPrivate::toComponentType(QSSGMesh::Mesh::ComponentType
    componentType)': names the enum 'QSSGRenderComponentType', whose class
    cannot be named here.

  What to expect
  --------------

  - The C++ QQuick3DGeometryPrivate is created at the first use, not by
    'QQuick3DGeometryPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DGeometryPrivate.
  - Each name of Qt's QQuick3DGeometryPrivate that has no cute function yet,
    'toComponentType', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The classes Qt writes inside QQuick3DGeometryPrivate, each a class in
  #  here as in C++.

  class Subset(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQuick3DGeometryPrivate::Subset: a plain Python
    object standing in front of one C++ QQuick3DGeometryPrivate::Subset.

    C++ hands a QQuick3DGeometryPrivate::Subset around as a copy, so every
    C++ QQuick3DGeometryPrivate::Subset behind a cute one is Python's own: it
    is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QQuick3DGeometryPrivate::Subset yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQuick3DGeometryPrivate::Subset::~Subset()': the destructor:
      Python removes its C++ QQuick3DGeometryPrivate::Subset by it, and has
      no other use for it.

    What to expect
    --------------

    - The C++ QQuick3DGeometryPrivate::Subset is created at the first use,
      not by 'QQuick3DGeometryPrivate::Subset(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQuick3DGeometryPrivate::Subset back gives a copy
      the ritual made for Python, in a new cute
      QQuick3DGeometryPrivate::Subset.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQuick3DGeometryPrivate::Subset'

    #  Qt's '~QQuick3DGeometryPrivate::Subset()'. Naming it makes this a
    #  value class: Python owns every C++ QQuick3DGeometryPrivate::Subset
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN23QQuick3DGeometryPrivate6SubsetD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QByteArray)
  def semanticFromName(
      name: QByteArray,
  ) -> QQuick3DGeometry.Attribute.Semantic:
    """
    Calls Qt's 'QQuick3DGeometry::Attribute::Semantic
    QQuick3DGeometryPrivate::semanticFromName(const QByteArray &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dgeometryprivate.html#semanticFromName

    Parameters
    ----------

    name : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    QQuick3DGeometry.Attribute.Semantic
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QQuick3DGeometry.Attribute.Semantic(number)' gives.
    """
    #  QQuick3DGeometry::Attribute::Semantic
    #      QQuick3DGeometryPrivate::semanticFromName(const QByteArray &name)
    return QQuick3DGeometry.Attribute.Semantic(Rituals.call(
        'ritual_ZN23QQuick3DGeometryPrivate16semanticFromNameERK10QByteArra'
        'y',
        CuteMixin._valueOf(name),
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DGeometryPrivate'

  #  A C++ QQuick3DGeometryPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DGeometryPrivate'

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
    'QQuick3DGeometryPrivate::QQuick3DGeometryPrivate()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dgeometryprivate.html
    """
    #  QQuick3DGeometryPrivate::QQuick3DGeometryPrivate()
    self._noteCreation(QQuick3DGeometryPrivate, lambda: Rituals.call(
        'ritual_ZN23QQuick3DGeometryPrivateC1Ev',
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

  @staticmethod
  def toComponentType(*__, **_) -> Never:
    """
    Qt's 'QQuick3DGeometry::Attribute::ComponentType
    QQuick3DGeometryPrivate::toComponentType(QSSGMesh::Mesh::ComponentType
    componentType)': names the enum 'QSSGRenderComponentType', whose class
    cannot be named here.
    """
    raise NotImplementedError(
        "'QQuick3DGeometryPrivate.toComponentType' has no cute function "
        "yet. Qt's 'QQuick3DGeometry::Attribute::ComponentType "
        "QQuick3DGeometryPrivate::toComponentType(QSSGMesh::Mesh::ComponentT"
        "ype componentType)': names the enum 'QSSGRenderComponentType', "
        "whose class cannot be named here.")
