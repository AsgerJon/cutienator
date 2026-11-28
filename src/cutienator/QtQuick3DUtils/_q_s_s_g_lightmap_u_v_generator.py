"""
QSSGLightmapUVGenerator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DUtils/6.12.0/QtQuick3DUtils/private/qssglightmapuvgenerator_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QSSGLightmapUVGenerator to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QSSGLightmapUVGenerator(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSSGLightmapUVGenerator: a plain Python object
  standing in front of one C++ QSSGLightmapUVGenerator.

  C++ hands a QSSGLightmapUVGenerator around as a copy, so every C++
  QSSGLightmapUVGenerator behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  No function of Qt's QSSGLightmapUVGenerator yet. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSSGLightmapUVGeneratorResult QSSGLightmapUVGenerator::run(const
    QByteArray &positions, const QByteArray &normals, const QByteArray &uv0,
    const QByteArray &index, QSSGMesh::Mesh::ComponentType
    indexComponentType, float texelsPerUnit)': names the enum
    'QSSGRenderComponentType', whose class cannot be named here.
  - Qt's 'QSSGLightmapUVGenerator::~QSSGLightmapUVGenerator()': the
    destructor: Python removes its C++ QSSGLightmapUVGenerator by it, and has
    no other use for it.

  What has no ritual
  ------------------

  1 of the 3 functions Qt declares: 1 a template.

  What to expect
  --------------

  - The C++ QSSGLightmapUVGenerator is created at the first use, not by
    'QSSGLightmapUVGenerator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSSGLightmapUVGenerator back gives a copy the ritual
    made for Python, in a new cute QSSGLightmapUVGenerator.
  - Each name of Qt's QSSGLightmapUVGenerator that has no cute function yet,
    'remap', 'run', holds a function that raises 'NotImplementedError', and
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
  __qt_class__ = 'QSSGLightmapUVGenerator'

  #  Qt's '~QSSGLightmapUVGenerator()'. Naming it makes this a value class:
  #  Python owns every C++ QSSGLightmapUVGenerator behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23QSSGLightmapUVGeneratorD1Ev'

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
  def remap(*__, **_) -> Never:
    """
    Qt's 'QSSGLightmapUVGenerator::remap': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QSSGLightmapUVGenerator.remap' has no cute function yet. Qt's "
        "'QSSGLightmapUVGenerator::remap': a template: a pattern and no "
        "single function.")

  @staticmethod
  def run(*__, **_) -> Never:
    """
    Qt's 'QSSGLightmapUVGeneratorResult QSSGLightmapUVGenerator::run(const
    QByteArray &positions, const QByteArray &normals, const QByteArray &uv0,
    const QByteArray &index, QSSGMesh::Mesh::ComponentType
    indexComponentType, float texelsPerUnit)': names the enum
    'QSSGRenderComponentType', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QSSGLightmapUVGenerator.run' has no cute function yet. Qt's "
        "'QSSGLightmapUVGeneratorResult QSSGLightmapUVGenerator::run(const "
        "QByteArray &positions, const QByteArray &normals, const QByteArray "
        "&uv0, const QByteArray &index, QSSGMesh::Mesh::ComponentType "
        "indexComponentType, float texelsPerUnit)': names the enum "
        "'QSSGRenderComponentType', whose class cannot be named here.")
