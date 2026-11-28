"""
Qt3DRender::QBlendEquationArgumentsPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/qblendequationarguments_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means Qt3DRender::QBlendEquationArgumentsPrivate to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional


class QBlendEquationArgumentsPrivate(Qt3DRender.QRenderStatePrivate):
  """
  The cute side of Qt's Qt3DRender::QBlendEquationArgumentsPrivate: a plain
  Python object standing in front of one C++
  Qt3DRender::QBlendEquationArgumentsPrivate.

  It is built on the cute 'Qt3DRender::QRenderStatePrivate', as Qt's
  Qt3DRender::QBlendEquationArgumentsPrivate is built on Qt's
  Qt3DRender::QRenderStatePrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QBlendEquationArgumentsPrivate that has
  a ritual and that Python can call so far, 1 name in all: 'q_func'. It can
  be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QBlendEquationArguments
    *Qt3DRender::QBlendEquationArgumentsPrivate::q_func() const': takes in
    Python what 'QBlendEquationArguments
    *Qt3DRender::QBlendEquationArgumentsPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ Qt3DRender::QBlendEquationArgumentsPrivate is created at the
    first use, not by 'Qt3DRender::QBlendEquationArgumentsPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QBlendEquationArgumentsPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QBlendEquationArgumentsPrivate'

  #  A C++ Qt3DRender::QBlendEquationArgumentsPrivate Python makes is of a
  #  C++ class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QBlendEquationArgumentsPrivate'

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
  @overload(Qt3DRender.Render.StateMask)
  def __init__(
      self,
      type: Qt3DRender.Render.StateMask = (
          Qt3DRender.Render.StateMask.BlendEquationArgumentsMask),
  ) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::QBlendEquationArgumentsPrivate::
    QBlendEquationArgumentsPrivate(Render::StateMask type)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblendequationargumentsprivate.html

    Parameters
    ----------

    type : Qt3DRender.Render.StateMask
      Passed on as its number. May be left out, as in Qt: it is then
      Qt3DRender.Render.StateMask.BlendEquationArgumentsMask.
    """
    #  Qt3DRender::QBlendEquationArgumentsPrivate::
    #      QBlendEquationArgumentsPrivate(Render::StateMask type)
    self._noteCreation(QBlendEquationArgumentsPrivate, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender30QBlendEquationArgumentsPrivateC1ENS_6Render'
        '9StateMaskE',
        type.value,
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

  def q_func(self) -> Optional[Qt3DRender.QBlendEquationArguments]:
    """
    Calls Qt's 'QBlendEquationArguments
    *Qt3DRender::QBlendEquationArgumentsPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qblendequationargumentsprivate.html

    Returns
    -------

    Optional[Qt3DRender.QBlendEquationArguments]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QBlendEquationArguments
    #      *Qt3DRender::QBlendEquationArgumentsPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender30QBlendEquationArgumentsPrivate6q_funcEv',
    )
    return Qt3DRender.QBlendEquationArguments._cuteAt(address)
