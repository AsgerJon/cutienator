"""
Qt3DRender::Quick::QScene2DPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DQuickScene2D/6.12.0/Qt3DQuickScene2D/private/qscene2d_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::Quick::QScene2DPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from ..cute import WAIT
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional


class QScene2DPrivate(Qt3DCore.QNodePrivate):
  """
  The cute side of Qt's Qt3DRender::Quick::QScene2DPrivate: a plain Python
  object standing in front of one C++ Qt3DRender::Quick::QScene2DPrivate.

  It is built on the cute 'Qt3DCore::QNodePrivate', as Qt's
  Qt3DRender::Quick::QScene2DPrivate is built on Qt's Qt3DCore::QNodePrivate,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Quick::QScene2DPrivate that has a ritual
  and that Python can call so far, 1 name in all: 'q_func'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QScene2D *Qt3DRender::Quick::QScene2DPrivate::q_func()
    const': takes in Python what 'QScene2D
    *Qt3DRender::Quick::QScene2DPrivate::q_func()' takes.
  - Qt's 'Qt3DRender::Quick::QScene2DPrivate::~QScene2DPrivate()': the
    destructor: Python never removes a C++
    Qt3DRender::Quick::QScene2DPrivate.

  What has no ritual
  ------------------

  1 of the 4 functions Qt declares: 1 leans on 'Qt3DRender.

  What to expect
  --------------

  - The C++ Qt3DRender::Quick::QScene2DPrivate is created at the first use,
    not by 'Qt3DRender::Quick::QScene2DPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Quick::QScene2DPrivate.
  - Each name of Qt's Qt3DRender::Quick::QScene2DPrivate that has no cute
    function yet, '__init__', holds a function that raises
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
  __qt_class__ = 'Qt3DRender::Quick::QScene2DPrivate'

  #  A C++ Qt3DRender::Quick::QScene2DPrivate Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_Quick_QScene2DPrivate'

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
    Qt's 'Qt3DRender::Quick::QScene2DPrivate::QScene2DPrivate()': leans on
    'Qt3DRender::Quick::Scene2DManager::staticMetaObject', which Qt's source
    does not mark for use from outside Qt and has no code for that could be
    taken.
    """
    raise NotImplementedError(
        "'Qt3DRender.Quick.QScene2DPrivate.__init__' has no cute function "
        "yet. Qt's 'Qt3DRender::Quick::QScene2DPrivate::QScene2DPrivate()': "
        "leans on 'Qt3DRender::Quick::Scene2DManager::staticMetaObject', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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

  def q_func(self) -> Optional[Qt3DRender.Quick.QScene2D]:
    """
    Calls Qt's 'QScene2D *Qt3DRender::Quick::QScene2DPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-quick-qscene2dprivate.html#q_func

    Returns
    -------

    Optional[Qt3DRender.Quick.QScene2D]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScene2D *Qt3DRender::Quick::QScene2DPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender5Quick15QScene2DPrivate6q_funcEv',
    )
    return Qt3DRender.Quick.QScene2D._cuteAt(address)
