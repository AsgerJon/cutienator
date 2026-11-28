"""
Qt3DExtras::QSphereGeometryPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/6.12.0/Qt3DExtras/private/qspheregeometry_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DExtras::QSphereGeometryPrivate to be private: it declares the
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
  from typing import Optional

  from ..QtCore import QByteArray


class QSphereGeometryPrivate(Qt3DCore.QGeometryPrivate):
  """
  The cute side of Qt's Qt3DExtras::QSphereGeometryPrivate: a plain Python
  object standing in front of one C++ Qt3DExtras::QSphereGeometryPrivate.

  It is built on the cute 'Qt3DCore::QGeometryPrivate', as Qt's
  Qt3DExtras::QSphereGeometryPrivate is built on Qt's
  Qt3DCore::QGeometryPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::QSphereGeometryPrivate that has a ritual
  and that Python can call so far, 4 names in all: 'init', 'q_func',
  'generateVertexData', 'generateIndexData'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QSphereGeometry *Qt3DExtras::QSphereGeometryPrivate::q_func()
    const': takes in Python what 'QSphereGeometry
    *Qt3DExtras::QSphereGeometryPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ Qt3DExtras::QSphereGeometryPrivate is created at the first use,
    not by 'Qt3DExtras::QSphereGeometryPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DExtras::QSphereGeometryPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DExtras::QSphereGeometryPrivate'

  #  A C++ Qt3DExtras::QSphereGeometryPrivate Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DExtras_QSphereGeometryPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def generateVertexData(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray
    Qt3DExtras::QSphereGeometryPrivate::generateVertexData() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspheregeometryprivate.html

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray Qt3DExtras::QSphereGeometryPrivate::generateVertexData()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras22QSphereGeometryPrivate18generateVertexData'
        'Ev',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def generateIndexData(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray
    Qt3DExtras::QSphereGeometryPrivate::generateIndexData() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspheregeometryprivate.html

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray Qt3DExtras::QSphereGeometryPrivate::generateIndexData()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DExtras22QSphereGeometryPrivate17generateIndexDataE'
        'v',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

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
    'Qt3DExtras::QSphereGeometryPrivate::QSphereGeometryPrivate()', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspheregeometryprivate.html
    """
    #  Qt3DExtras::QSphereGeometryPrivate::QSphereGeometryPrivate()
    self._noteCreation(QSphereGeometryPrivate, lambda: Rituals.call(
        'ritual_ZN10Qt3DExtras22QSphereGeometryPrivateC1Ev',
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

  def init(self) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QSphereGeometryPrivate::init()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspheregeometryprivate.html#init
    """
    #  void Qt3DExtras::QSphereGeometryPrivate::init()
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras22QSphereGeometryPrivate4initEv',
    )

  def q_func(self) -> Optional[Qt3DExtras.QSphereGeometry]:
    """
    Calls Qt's 'QSphereGeometry
    *Qt3DExtras::QSphereGeometryPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qspheregeometryprivate.html#q_func

    Returns
    -------

    Optional[Qt3DExtras.QSphereGeometry]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSphereGeometry *Qt3DExtras::QSphereGeometryPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DExtras22QSphereGeometryPrivate6q_funcEv',
    )
    return Qt3DExtras.QSphereGeometry._cuteAt(address)
