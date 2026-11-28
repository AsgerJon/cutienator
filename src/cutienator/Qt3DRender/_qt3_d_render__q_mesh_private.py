"""
Qt3DRender::QMeshPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/qmesh_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means Qt3DRender::QMeshPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMeshPrivate(Qt3DRender.QGeometryRendererPrivate):
  """
  The cute side of Qt's Qt3DRender::QMeshPrivate: a plain Python object
  standing in front of one C++ Qt3DRender::QMeshPrivate.

  It is built on the cute 'Qt3DRender::QGeometryRendererPrivate', as Qt's
  Qt3DRender::QMeshPrivate is built on Qt's
  Qt3DRender::QGeometryRendererPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QMeshPrivate that has a ritual and that
  Python can call so far, 5 names in all: 'q_func', 'get', 'setScene',
  'updateFunctor', 'setStatus'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QMesh *Qt3DRender::QMeshPrivate::q_func() const': takes in
    Python what 'QMesh *Qt3DRender::QMeshPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ Qt3DRender::QMeshPrivate is created at the first use, not by
    'Qt3DRender::QMeshPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QMeshPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['Qt3DRender.QMesh'])
  @overload(NoneType)
  def get(q: Optional[Qt3DRender.QMesh]) -> Optional[QMeshPrivate]:
    """
    Calls Qt's 'QMeshPrivate *Qt3DRender::QMeshPrivate::get(QMesh *q)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qmeshprivate.html#get

    Parameters
    ----------

    q : Optional[Qt3DRender.QMesh]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QMeshPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMeshPrivate *Qt3DRender::QMeshPrivate::get(QMesh *q)
    address = Rituals.call(
        'ritual_ZN10Qt3DRender12QMeshPrivate3getEPNS_5QMeshE',
        CuteMixin._addressOf(q),
    )
    return QMeshPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QMeshPrivate'

  #  A C++ Qt3DRender::QMeshPrivate Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QMeshPrivate'

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

  @overload(WAIT['Qt3DCore.QScene'])
  @overload(NoneType)
  def setScene(self, scene: Optional[Qt3DCore.QScene]) -> None:
    """
    Calls Qt's 'void Qt3DRender::QMeshPrivate::setScene(Qt3DCore::QScene
    *scene)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qmeshprivate.html#setScene

    Parameters
    ----------

    scene : Optional[Qt3DCore.QScene]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::QMeshPrivate::setScene(Qt3DCore::QScene *scene)
    ritual = (
        'ritual_ZN10Qt3DRender12QMeshPrivate8setSceneEPN8Qt3DCore6QSceneE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender12QMeshPrivate8setSceneEPN8Qt3DCore6QSc'
          'eneE')
    self.uglySide.call(ritual, self._addressOf(scene))

  @overload(Qt3DRender.QMesh.Status)
  def setStatus(self, status: Qt3DRender.QMesh.Status) -> None:
    """
    Calls Qt's 'void Qt3DRender::QMeshPrivate::setStatus(QMesh::Status
    status)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qmeshprivate.html#setStatus

    Parameters
    ----------

    status : Qt3DRender.QMesh.Status
      Passed on as its number.
    """
    #  void Qt3DRender::QMeshPrivate::setStatus(QMesh::Status status)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender12QMeshPrivate9setStatusENS_5QMesh6StatusE',
        status.value,
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
    'Qt3DRender::QMeshPrivate::QMeshPrivate()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qmeshprivate.html#QMeshPrivate
    """
    #  Qt3DRender::QMeshPrivate::QMeshPrivate()
    self._noteCreation(QMeshPrivate, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender12QMeshPrivateC1Ev',
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

  def q_func(self) -> Optional[Qt3DRender.QMesh]:
    """
    Calls Qt's 'QMesh *Qt3DRender::QMeshPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qmeshprivate.html#q_func

    Returns
    -------

    Optional[Qt3DRender.QMesh]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QMesh *Qt3DRender::QMeshPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender12QMeshPrivate6q_funcEv',
    )
    return Qt3DRender.QMesh._cuteAt(address)

  def updateFunctor(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::QMeshPrivate::updateFunctor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qmeshprivate.html#updateFunctor
    """
    #  void Qt3DRender::QMeshPrivate::updateFunctor()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender12QMeshPrivate13updateFunctorEv',
    )
