"""
Qt3DExtras::QForwardRendererPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DExtras/6.12.0/Qt3DExtras/private/qforwardrenderer_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DExtras::QForwardRendererPrivate to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..Qt3DRender import Qt3DRender
from . import Qt3DExtras

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class QForwardRendererPrivate(Qt3DRender.QTechniqueFilterPrivate):
  """
  The cute side of Qt's Qt3DExtras::QForwardRendererPrivate: a plain Python
  object standing in front of one C++ Qt3DExtras::QForwardRendererPrivate.

  It is built on the cute 'Qt3DRender::QTechniqueFilterPrivate', as Qt's
  Qt3DExtras::QForwardRendererPrivate is built on Qt's
  Qt3DRender::QTechniqueFilterPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DExtras::QForwardRendererPrivate that has a
  ritual and that Python can call so far, 2 names in all: 'init', 'q_func'.
  It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QForwardRenderer
    *Qt3DExtras::QForwardRendererPrivate::q_func() const': takes in Python
    what 'QForwardRenderer *Qt3DExtras::QForwardRendererPrivate::q_func()'
    takes.

  What to expect
  --------------

  - The C++ Qt3DExtras::QForwardRendererPrivate is created at the first use,
    not by 'Qt3DExtras::QForwardRendererPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DExtras::QForwardRendererPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DExtras::QForwardRendererPrivate'

  #  A C++ Qt3DExtras::QForwardRendererPrivate Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DExtras_QForwardRendererPrivate'

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
    'Qt3DExtras::QForwardRendererPrivate::QForwardRendererPrivate()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qforwardrendererprivate.html
    """
    #  Qt3DExtras::QForwardRendererPrivate::QForwardRendererPrivate()
    self._noteCreation(QForwardRendererPrivate, lambda: Rituals.call(
        'ritual_ZN10Qt3DExtras23QForwardRendererPrivateC1Ev',
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
    Calls Qt's 'void Qt3DExtras::QForwardRendererPrivate::init()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qforwardrendererprivate.html#init
    """
    #  void Qt3DExtras::QForwardRendererPrivate::init()
    self.uglySide.call(
        'ritual_ZN10Qt3DExtras23QForwardRendererPrivate4initEv',
    )

  def q_func(self) -> Optional[Qt3DExtras.QForwardRenderer]:
    """
    Calls Qt's 'QForwardRenderer
    *Qt3DExtras::QForwardRendererPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dextras-qforwardrendererprivate.html#q_func

    Returns
    -------

    Optional[Qt3DExtras.QForwardRenderer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QForwardRenderer *Qt3DExtras::QForwardRendererPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DExtras23QForwardRendererPrivate6q_funcEv',
    )
    return Qt3DExtras.QForwardRenderer._cuteAt(address)
