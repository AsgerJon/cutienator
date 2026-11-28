"""
Qt3DRender::QRenderStatePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/qrenderstate_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DRender::QRenderStatePrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
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


class QRenderStatePrivate(Qt3DCore.QNodePrivate):
  """
  The cute side of Qt's Qt3DRender::QRenderStatePrivate: a plain Python
  object standing in front of one C++ Qt3DRender::QRenderStatePrivate.

  It is built on the cute 'Qt3DCore::QNodePrivate', as Qt's
  Qt3DRender::QRenderStatePrivate is built on Qt's Qt3DCore::QNodePrivate,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QRenderStatePrivate that has a ritual
  and that Python can call so far, 2 names in all: 'q_func', 'get'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::QRenderStatePrivate::~QRenderStatePrivate()': the
    destructor: Python never removes a C++ Qt3DRender::QRenderStatePrivate.
  - Qt's 'const QRenderState *Qt3DRender::QRenderStatePrivate::q_func()
    const': takes in Python what 'QRenderState
    *Qt3DRender::QRenderStatePrivate::q_func()' takes.
  - Qt's 'const QRenderStatePrivate
    *Qt3DRender::QRenderStatePrivate::get(const QRenderState *state)': takes
    in Python what 'QRenderStatePrivate
    *Qt3DRender::QRenderStatePrivate::get(QRenderState *state)' takes.

  What to expect
  --------------

  - The C++ Qt3DRender::QRenderStatePrivate is created at the first use, not
    by 'Qt3DRender::QRenderStatePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QRenderStatePrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['Qt3DRender.QRenderState'])
  @overload(NoneType)
  def get(
      state: Optional[Qt3DRender.QRenderState],
  ) -> Optional[QRenderStatePrivate]:
    """
    Calls Qt's 'QRenderStatePrivate
    *Qt3DRender::QRenderStatePrivate::get(QRenderState *state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrenderstateprivate.html#get

    Parameters
    ----------

    state : Optional[Qt3DRender.QRenderState]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QRenderStatePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRenderStatePrivate *Qt3DRender::QRenderStatePrivate::get(QRenderState
    #      *state)
    address = Rituals.call(
        'ritual_ZN10Qt3DRender19QRenderStatePrivate3getEPNS_12QRenderStateE',
        CuteMixin._addressOf(state),
    )
    return QRenderStatePrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QRenderStatePrivate'

  #  A C++ Qt3DRender::QRenderStatePrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QRenderStatePrivate'

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

  @overload(Qt3DRender.Render.StateMask)
  def __init__(self, type: Qt3DRender.Render.StateMask) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::QRenderStatePrivate::QRenderStatePrivate(Render::StateMask
    type)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrenderstateprivate.html

    Parameters
    ----------

    type : Qt3DRender.Render.StateMask
      Passed on as its number.
    """
    #  Qt3DRender::QRenderStatePrivate::QRenderStatePrivate(Render::StateMask
    #      type)
    self._noteCreation(QRenderStatePrivate, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender19QRenderStatePrivateC1ENS_6Render9StateMaskE',
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

  def q_func(self) -> Optional[Qt3DRender.QRenderState]:
    """
    Calls Qt's 'QRenderState *Qt3DRender::QRenderStatePrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrenderstateprivate.html#q_func

    Returns
    -------

    Optional[Qt3DRender.QRenderState]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRenderState *Qt3DRender::QRenderStatePrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender19QRenderStatePrivate6q_funcEv',
    )
    return Qt3DRender.QRenderState._cuteAt(address)
