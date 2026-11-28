"""
Qt3DRender::QGeometryLoaderInterface binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/qgeometryloaderinterface_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Qt3DRender::QGeometryLoaderInterface to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QObject
from ..Qt3DCore import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QIODevice
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QIODevice = WAIT['QIODevice']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QGeometryLoaderInterface(QObject):
  """
  The cute side of Qt's Qt3DRender::QGeometryLoaderInterface: a plain Python
  object standing in front of one C++ Qt3DRender::QGeometryLoaderInterface.

  It is built on the cute 'QObject', as Qt's
  Qt3DRender::QGeometryLoaderInterface is built on Qt's QObject, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QGeometryLoaderInterface that has a
  ritual and that Python can call so far, 2 names in all: 'geometry', 'load'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What to expect
  --------------

  - The C++ Qt3DRender::QGeometryLoaderInterface is created at the first use,
    not by 'Qt3DRender::QGeometryLoaderInterface(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QGeometryLoaderInterface.
  - Qt tells when it has removed the C++
    Qt3DRender::QGeometryLoaderInterface. Every call on the cute object, and
    every use of it as an argument, then raises 'RuntimeError', and nothing
    reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QGeometryLoaderInterface'

  #  A C++ Qt3DRender::QGeometryLoaderInterface Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QGeometryLoaderInterface'

  #  The functions Qt calls itself that Qt3DRender::QGeometryLoaderInterface
  #  is the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'geometry': (
          ('_ZNK10Qt3DRender24QGeometryLoaderInterface8geometryEv',
           ('address', 'address', 'Qt3DCore:Qt3DCore.QGeometry'),
           ()),
      ),
      'load': (
          ('_ZN10Qt3DRender24QGeometryLoaderInterface4loadEP9QIODeviceRK7QS'
           'tring',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtCore:QIODevice'),
               ('address', 'text', ''),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def geometry(self) -> Optional[Qt3DCore.QGeometry]:
    """
    Calls Qt's 'Qt3DCore::QGeometry
    *Qt3DRender::QGeometryLoaderInterface::geometry() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgeometryloaderinterface.html#geometry

    Returns
    -------

    Optional[Qt3DCore.QGeometry]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QGeometry *Qt3DRender::QGeometryLoaderInterface::geometry()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender24QGeometryLoaderInterface8geometryEv',
    )
    return Qt3DCore.QGeometry._cuteAt(address)

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

  @overload(QIODevice)
  @overload(NoneType)
  @overload(QIODevice, str)
  @overload(NoneType, str)
  def load(self, ioDev: Optional[QIODevice], subMesh: str = '') -> bool:
    """
    Calls Qt's 'bool Qt3DRender::QGeometryLoaderInterface::load(QIODevice
    *ioDev, const QString &subMesh)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qgeometryloaderinterface.html#load

    Parameters
    ----------

    ioDev : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    subMesh : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  bool Qt3DRender::QGeometryLoaderInterface::load(QIODevice *ioDev,
    #      const QString &subMesh)
    return self.uglySide.call(
        'ritual_ZN10Qt3DRender24QGeometryLoaderInterface4loadEP9QIODeviceRK'
        '7QString',
        self._addressOf(ioDev), subMesh,
    )
