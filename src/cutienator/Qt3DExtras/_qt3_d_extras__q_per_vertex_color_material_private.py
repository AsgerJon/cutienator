"""
Qt3DExtras::QPerVertexColorMaterialPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/6.12.0/Qt3DExtras/private/qpervertexcolormaterial_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Qt3DExtras::QPerVertexColorMaterialPrivate to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..Qt3DRender import Qt3DRender
from . import Qt3DExtras

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class QPerVertexColorMaterialPrivate(Qt3DRender.QMaterialPrivate):
  """
  The cute side of Qt's Qt3DExtras::QPerVertexColorMaterialPrivate: a plain
  Python object standing in front of one C++
  Qt3DExtras::QPerVertexColorMaterialPrivate.

  It is built on the cute 'Qt3DRender::QMaterialPrivate', as Qt's
  Qt3DExtras::QPerVertexColorMaterialPrivate is built on Qt's
  Qt3DRender::QMaterialPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::QPerVertexColorMaterialPrivate that has
  a ritual and that Python can call so far, 2 names in all: 'init', 'q_func'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QPerVertexColorMaterial
    *Qt3DExtras::QPerVertexColorMaterialPrivate::q_func() const': takes in
    Python what 'QPerVertexColorMaterial
    *Qt3DExtras::QPerVertexColorMaterialPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ Qt3DExtras::QPerVertexColorMaterialPrivate is created at the
    first use, not by 'Qt3DExtras::QPerVertexColorMaterialPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DExtras::QPerVertexColorMaterialPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DExtras::QPerVertexColorMaterialPrivate'

  #  A C++ Qt3DExtras::QPerVertexColorMaterialPrivate Python makes is of a
  #  C++ class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DExtras_QPerVertexColorMaterialPrivate'

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
    'Qt3DExtras::QPerVertexColorMaterialPrivate::
    QPerVertexColorMaterialPrivate()', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qpervertexcolormaterialprivate.html
    """
    #  Qt3DExtras::QPerVertexColorMaterialPrivate::
    #      QPerVertexColorMaterialPrivate()
    self._noteCreation(QPerVertexColorMaterialPrivate, lambda: Rituals.call(
        'ritual_ZN10Qt3DExtras30QPerVertexColorMaterialPrivateC1Ev',
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
    Calls Qt's 'void Qt3DExtras::QPerVertexColorMaterialPrivate::init()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qpervertexcolormaterialprivate.html
    """
    #  void Qt3DExtras::QPerVertexColorMaterialPrivate::init()
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras30QPerVertexColorMaterialPrivate4initEv',
    )

  def q_func(self) -> Optional[Qt3DExtras.QPerVertexColorMaterial]:
    """
    Calls Qt's 'QPerVertexColorMaterial
    *Qt3DExtras::QPerVertexColorMaterialPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qpervertexcolormaterialprivate.html

    Returns
    -------

    Optional[Qt3DExtras.QPerVertexColorMaterial]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPerVertexColorMaterial
    #      *Qt3DExtras::QPerVertexColorMaterialPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DExtras30QPerVertexColorMaterialPrivate6q_funcEv',
    )
    return Qt3DExtras.QPerVertexColorMaterial._cuteAt(address)
