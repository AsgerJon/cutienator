"""
Qt3DExtras::QExtrudedTextGeometryPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/6.12.0/Qt3DExtras/private/qextrudedtextgeometry_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DExtras::QExtrudedTextGeometryPrivate to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import WAIT
from ..Qt3DCore import Qt3DCore
from . import Qt3DExtras

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional


class QExtrudedTextGeometryPrivate(Qt3DCore.QGeometryPrivate):
  """
  The cute side of Qt's Qt3DExtras::QExtrudedTextGeometryPrivate: a plain
  Python object standing in front of one C++
  Qt3DExtras::QExtrudedTextGeometryPrivate.

  It is built on the cute 'Qt3DCore::QGeometryPrivate', as Qt's
  Qt3DExtras::QExtrudedTextGeometryPrivate is built on Qt's
  Qt3DCore::QGeometryPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::QExtrudedTextGeometryPrivate that has a
  ritual and that Python can call so far, 3 names in all: 'init', 'update',
  'q_func'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QExtrudedTextGeometry
    *Qt3DExtras::QExtrudedTextGeometryPrivate::q_func() const': takes in
    Python what 'QExtrudedTextGeometry
    *Qt3DExtras::QExtrudedTextGeometryPrivate::q_func()' takes.

  What has no ritual
  ------------------

  1 of the 5 functions Qt declares: 1 leans on 'Qt3DExtras.

  What to expect
  --------------

  - The C++ Qt3DExtras::QExtrudedTextGeometryPrivate is created at the first
    use, not by 'Qt3DExtras::QExtrudedTextGeometryPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DExtras::QExtrudedTextGeometryPrivate.
  - Each name of Qt's Qt3DExtras::QExtrudedTextGeometryPrivate that has no
    cute function yet, '__init__', holds a function that raises
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
  __qt_class__ = 'Qt3DExtras::QExtrudedTextGeometryPrivate'

  #  A C++ Qt3DExtras::QExtrudedTextGeometryPrivate Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DExtras_QExtrudedTextGeometryPrivate'

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's
    'Qt3DExtras::QExtrudedTextGeometryPrivate::QExtrudedTextGeometryPrivate(
    )': leans on 'Qt3DExtras::QExtrudedTextGeometryPrivate::update()', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'Qt3DExtras.QExtrudedTextGeometryPrivate.__init__' has no cute "
        "function yet. Qt's "
        "'Qt3DExtras::QExtrudedTextGeometryPrivate::QExtrudedTextGeometryPri"
        "vate()': leans on "
        "'Qt3DExtras::QExtrudedTextGeometryPrivate::update()', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

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
    Calls Qt's 'void Qt3DExtras::QExtrudedTextGeometryPrivate::init()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qextrudedtextgeometryprivate.html#init
    """
    #  void Qt3DExtras::QExtrudedTextGeometryPrivate::init()
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras28QExtrudedTextGeometryPrivate4initEv',
    )

  def update(self) -> None:
    """
    Calls Qt's 'void Qt3DExtras::QExtrudedTextGeometryPrivate::update()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qextrudedtextgeometryprivate.html
    """
    #  void Qt3DExtras::QExtrudedTextGeometryPrivate::update()
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras28QExtrudedTextGeometryPrivate6updateEv',
    )

  def q_func(self) -> Optional[Qt3DExtras.QExtrudedTextGeometry]:
    """
    Calls Qt's 'QExtrudedTextGeometry
    *Qt3DExtras::QExtrudedTextGeometryPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qextrudedtextgeometryprivate.html

    Returns
    -------

    Optional[Qt3DExtras.QExtrudedTextGeometry]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QExtrudedTextGeometry
    #      *Qt3DExtras::QExtrudedTextGeometryPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DExtras28QExtrudedTextGeometryPrivate6q_funcEv',
    )
    return Qt3DExtras.QExtrudedTextGeometry._cuteAt(address)
