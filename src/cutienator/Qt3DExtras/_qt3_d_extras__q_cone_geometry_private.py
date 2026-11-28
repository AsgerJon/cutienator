"""
Qt3DExtras::QConeGeometryPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/6.12.0/Qt3DExtras/private/qconegeometry_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DExtras::QConeGeometryPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
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


class QConeGeometryPrivate(Qt3DCore.QGeometryPrivate):
  """
  The cute side of Qt's Qt3DExtras::QConeGeometryPrivate: a plain Python
  object standing in front of one C++ Qt3DExtras::QConeGeometryPrivate.

  It is built on the cute 'Qt3DCore::QGeometryPrivate', as Qt's
  Qt3DExtras::QConeGeometryPrivate is built on Qt's
  Qt3DCore::QGeometryPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::QConeGeometryPrivate that has a ritual
  and that Python can call so far, 1 name in all: 'q_func'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QConeGeometry *Qt3DExtras::QConeGeometryPrivate::q_func()
    const': takes in Python what 'QConeGeometry
    *Qt3DExtras::QConeGeometryPrivate::q_func()' takes.

  What has no ritual
  ------------------

  3 of the 6 functions Qt declares: 2 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 leans on
  'Qt3DExtras.

  What to expect
  --------------

  - The C++ Qt3DExtras::QConeGeometryPrivate is created at the first use, not
    by 'Qt3DExtras::QConeGeometryPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DExtras::QConeGeometryPrivate.
  - Each name of Qt's Qt3DExtras::QConeGeometryPrivate that has no cute
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
  __qt_class__ = 'Qt3DExtras::QConeGeometryPrivate'

  #  A C++ Qt3DExtras::QConeGeometryPrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DExtras_QConeGeometryPrivate'

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
    'Qt3DExtras::QConeGeometryPrivate::QConeGeometryPrivate()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometryprivate.html
    """
    #  Qt3DExtras::QConeGeometryPrivate::QConeGeometryPrivate()
    self._noteCreation(QConeGeometryPrivate, lambda: Rituals.call(
        'ritual_ZN10Qt3DExtras20QConeGeometryPrivateC1Ev',
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

  def q_func(self) -> Optional[Qt3DExtras.QConeGeometry]:
    """
    Calls Qt's 'QConeGeometry *Qt3DExtras::QConeGeometryPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qconegeometryprivate.html#q_func

    Returns
    -------

    Optional[Qt3DExtras.QConeGeometry]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QConeGeometry *Qt3DExtras::QConeGeometryPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DExtras20QConeGeometryPrivate6q_funcEv',
    )
    return Qt3DExtras.QConeGeometry._cuteAt(address)

  @staticmethod
  def generateIndexData(*__, **_) -> Never:
    """
    Qt's 'QByteArray Qt3DExtras::QConeGeometryPrivate::generateIndexData()
    const': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'faceCount'.
    """
    raise NotImplementedError(
        "'Qt3DExtras.QConeGeometryPrivate.generateIndexData' has no cute "
        "function yet. Qt's 'QByteArray "
        "Qt3DExtras::QConeGeometryPrivate::generateIndexData() const': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'faceCount'.")

  @staticmethod
  def generateVertexData(*__, **_) -> Never:
    """
    Qt's 'QByteArray Qt3DExtras::QConeGeometryPrivate::generateVertexData()
    const': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'vertexCount'.
    """
    raise NotImplementedError(
        "'Qt3DExtras.QConeGeometryPrivate.generateVertexData' has no cute "
        "function yet. Qt's 'QByteArray "
        "Qt3DExtras::QConeGeometryPrivate::generateVertexData() const': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'vertexCount'.")
