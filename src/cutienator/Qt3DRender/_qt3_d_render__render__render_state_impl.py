"""
Qt3DRender::Render::RenderStateImpl binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/genericstate_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DRender::Render::RenderStateImpl to be private: it declares
#  the class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class RenderStateImpl(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DRender::Render::RenderStateImpl: a plain Python
  object standing in front of one C++ Qt3DRender::Render::RenderStateImpl.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::RenderStateImpl that has a
  ritual and that Python can call so far, 2 names in all: 'mask',
  'updateProperties'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::Render::RenderStateImpl::~RenderStateImpl()': the
    destructor: Python never removes a C++
    Qt3DRender::Render::RenderStateImpl.
  - Qt's 'bool Qt3DRender::Render::RenderStateImpl::equalTo(const
    RenderStateImpl &renderState) const': takes a type Python has no way to
    hand over yet.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::RenderStateImpl is created at the first use,
    not by 'Qt3DRender::Render::RenderStateImpl(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::RenderStateImpl.
  - Each name of Qt's Qt3DRender::Render::RenderStateImpl that has no cute
    function yet, 'equalTo', holds a function that raises
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
  __qt_class__ = 'Qt3DRender::Render::RenderStateImpl'

  #  A C++ Qt3DRender::Render::RenderStateImpl Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_Render_RenderStateImpl'

  #  The functions Qt calls itself that Qt3DRender::Render::RenderStateImpl
  #  is the first to declare and that cannot be handed to Python yet, each as
  #  Qt declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'equalTo': (
          'bool Qt3DRender::Render::RenderStateImpl::equalTo(const '
          'RenderStateImpl &) const',
      ),
  }

  #  The functions Qt calls itself that Qt3DRender::Render::RenderStateImpl
  #  is the first to declare. A class of a program built on it can write one
  #  anew, and Qt then calls that. For each name: the key C++ knows the
  #  function by, what it gives, and what it takes.
  __virtual_functions__ = {
      'mask': (
          ('_ZNK10Qt3DRender6Render15RenderStateImpl4maskEv',
           ('int', 'enum', 'Qt3DRender:Qt3DRender.Render.StateMask'),
           ()),
      ),
      'updateProperties': (
          ('_ZN10Qt3DRender6Render15RenderStateImpl16updatePropertiesEPKNS_'
           '12QRenderStateE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'Qt3DRender:Qt3DRender.QRenderState'),
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

  def mask(self) -> Qt3DRender.Render.StateMask:
    """
    Calls Qt's 'StateMask Qt3DRender::Render::RenderStateImpl::mask() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-renderstateimpl.html#mask

    Returns
    -------

    Qt3DRender.Render.StateMask
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DRender.Render.StateMask(number)' gives.
    """
    #  StateMask Qt3DRender::Render::RenderStateImpl::mask() const
    return Qt3DRender.Render.StateMask(self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render15RenderStateImpl4maskEv',
    ))

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

  @overload(WAIT['Qt3DRender.QRenderState'])
  @overload(NoneType)
  def updateProperties(self, a0: Optional[Qt3DRender.QRenderState]) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::RenderStateImpl::updateProperties(const QRenderState
    *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-renderstateimpl.html

    Parameters
    ----------

    a0 : Optional[Qt3DRender.QRenderState]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::RenderStateImpl::updateProperties(const
    #      QRenderState *a0)
    ritual = (
        'ritual_ZN10Qt3DRender6Render15RenderStateImpl16updatePropertiesEPK'
        'NS_12QRenderStateE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render15RenderStateImpl16updatePropert'
          'iesEPKNS_12QRenderStateE')
    self.uglySide.call(ritual, self._addressOf(a0))

  @staticmethod
  def equalTo(*__, **_) -> Never:
    """
    Qt's 'bool Qt3DRender::Render::RenderStateImpl::equalTo(const
    RenderStateImpl &renderState) const': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.RenderStateImpl.equalTo' has no cute function "
        "yet. Qt's 'bool Qt3DRender::Render::RenderStateImpl::equalTo(const "
        "RenderStateImpl &renderState) const': takes a type Python has no "
        "way to hand over yet.")
