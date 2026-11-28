"""
QQuick3DPhysicsMeshManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DPhysics/6.12.0/QtQuick3DPhysics/private/qphysicsmeshutils_p_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DPhysicsMeshManager to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import CuteMixin, MetaCute

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QQuick3DPhysicsMeshManager(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuick3DPhysicsMeshManager: a plain Python object
  standing in front of one C++ QQuick3DPhysicsMeshManager.

  C++ hands a QQuick3DPhysicsMeshManager around as a copy, so every C++
  QQuick3DPhysicsMeshManager behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  No function of Qt's QQuick3DPhysicsMeshManager yet. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQuick3DPhysicsMeshManager::~QQuick3DPhysicsMeshManager()': the
    destructor: Python removes its C++ QQuick3DPhysicsMeshManager by it, and
    has no other use for it.

  What has no ritual
  ------------------

  3 of the 4 functions Qt declares: 2 leans on 'QQuick3DPhysicsMeshManager; 1
  leans on 'lcQuick3dPhysics()', which Qt's source does not mark for use from
  outside Qt and has no code for that could be taken.

  What to expect
  --------------

  - The C++ QQuick3DPhysicsMeshManager is created at the first use, not by
    'QQuick3DPhysicsMeshManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQuick3DPhysicsMeshManager back gives a copy the
    ritual made for Python, in a new cute QQuick3DPhysicsMeshManager.
  - Each name of Qt's QQuick3DPhysicsMeshManager that has no cute function
    yet, 'getMesh', 'releaseMesh', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DPhysicsMeshManager'

  #  Qt's '~QQuick3DPhysicsMeshManager()'. Naming it makes this a value
  #  class: Python owns every C++ QQuick3DPhysicsMeshManager behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN26QQuick3DPhysicsMeshManagerD1Ev'

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
  def getMesh(*__, **_) -> Never:
    """
    - Qt's 'QQuick3DPhysicsMesh *QQuick3DPhysicsMeshManager::getMesh(const
      QUrl &source, QObject *contextObject)': leans on
      'QQuick3DPhysicsMeshManager::sourceMeshHash', which Qt's source does
      not mark for use from outside Qt and has no code for that could be
      taken.
    - Qt's 'QQuick3DPhysicsMesh
      *QQuick3DPhysicsMeshManager::getMesh(QQuick3DGeometry *source)': leans
      on 'QQuick3DPhysicsMeshManager::geometryMeshHash', which Qt's source
      does not mark for use from outside Qt and has no code for that could be
      taken.
    """
    raise NotImplementedError(
        "'QQuick3DPhysicsMeshManager.getMesh' has no cute function yet. "
        "Qt's 'QQuick3DPhysicsMesh "
        "*QQuick3DPhysicsMeshManager::getMesh(const QUrl &source, QObject "
        "*contextObject)': leans on "
        "'QQuick3DPhysicsMeshManager::sourceMeshHash', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken. Qt's 'QQuick3DPhysicsMesh "
        "*QQuick3DPhysicsMeshManager::getMesh(QQuick3DGeometry *source)': "
        "leans on 'QQuick3DPhysicsMeshManager::geometryMeshHash', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def releaseMesh(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DPhysicsMeshManager::releaseMesh(QQuick3DPhysicsMesh
    *mesh)': leans on 'lcQuick3dPhysics()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DPhysicsMeshManager.releaseMesh' has no cute function yet. "
        "Qt's 'void "
        "QQuick3DPhysicsMeshManager::releaseMesh(QQuick3DPhysicsMesh "
        "*mesh)': leans on 'lcQuick3dPhysics()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")
