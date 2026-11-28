"""
Qt3DExtras::QCylinderGeometryPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/6.12.0/Qt3DExtras/private/qcylindergeometry_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DExtras::QCylinderGeometryPrivate to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DExtras

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional


class QCylinderGeometryPrivate(Qt3DCore.QGeometryPrivate):
  """
  The cute side of Qt's Qt3DExtras::QCylinderGeometryPrivate: a plain Python
  object standing in front of one C++ Qt3DExtras::QCylinderGeometryPrivate.

  It is built on the cute 'Qt3DCore::QGeometryPrivate', as Qt's
  Qt3DExtras::QCylinderGeometryPrivate is built on Qt's
  Qt3DCore::QGeometryPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::QCylinderGeometryPrivate that has a
  ritual and that Python can call so far, 1 name in all: 'q_func'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QCylinderGeometry
    *Qt3DExtras::QCylinderGeometryPrivate::q_func() const': takes in Python
    what 'QCylinderGeometry *Qt3DExtras::QCylinderGeometryPrivate::q_func()'
    takes.

  What has no ritual
  ------------------

  3 of the 6 functions Qt declares: 2 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 leans on
  'Qt3DExtras.

  What to expect
  --------------

  - The C++ Qt3DExtras::QCylinderGeometryPrivate is created at the first use,
    not by 'Qt3DExtras::QCylinderGeometryPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DExtras::QCylinderGeometryPrivate.
  - Each name of Qt's Qt3DExtras::QCylinderGeometryPrivate that has no cute
    function yet, 'generateIndexData', 'generateVertexData', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DExtras::QCylinderGeometryPrivate'

  #  A C++ Qt3DExtras::QCylinderGeometryPrivate Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DExtras_QCylinderGeometryPrivate'

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
    'Qt3DExtras::QCylinderGeometryPrivate::QCylinderGeometryPrivate()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcylindergeometryprivate.html
    """
    #  Qt3DExtras::QCylinderGeometryPrivate::QCylinderGeometryPrivate()
    self._noteCreation(QCylinderGeometryPrivate, lambda: Rituals.call(
        'ritual_ZN10Qt3DExtras24QCylinderGeometryPrivateC1Ev',
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

  def q_func(self) -> Optional[Qt3DExtras.QCylinderGeometry]:
    """
    Calls Qt's 'QCylinderGeometry
    *Qt3DExtras::QCylinderGeometryPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qcylindergeometryprivate.html#q_func

    Returns
    -------

    Optional[Qt3DExtras.QCylinderGeometry]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QCylinderGeometry *Qt3DExtras::QCylinderGeometryPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DExtras24QCylinderGeometryPrivate6q_funcEv',
    )
    return Qt3DExtras.QCylinderGeometry._cuteAt(address)

  @staticmethod
  def generateIndexData(*__, **_) -> Never:
    """
    Qt's 'QByteArray
    Qt3DExtras::QCylinderGeometryPrivate::generateIndexData() const': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'faceCount'.
    """
    raise NotImplementedError(
        "'Qt3DExtras.QCylinderGeometryPrivate.generateIndexData' has no "
        "cute function yet. Qt's 'QByteArray "
        "Qt3DExtras::QCylinderGeometryPrivate::generateIndexData() const': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'faceCount'.")

  @staticmethod
  def generateVertexData(*__, **_) -> Never:
    """
    Qt's 'QByteArray
    Qt3DExtras::QCylinderGeometryPrivate::generateVertexData() const': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'vertexCount'.
    """
    raise NotImplementedError(
        "'Qt3DExtras.QCylinderGeometryPrivate.generateVertexData' has no "
        "cute function yet. Qt's 'QByteArray "
        "Qt3DExtras::QCylinderGeometryPrivate::generateVertexData() const': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'vertexCount'.")
