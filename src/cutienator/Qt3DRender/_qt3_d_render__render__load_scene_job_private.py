"""
Qt3DRender::Render::LoadSceneJobPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/loadscenejob_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DRender::Render::LoadSceneJobPrivate to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class LoadSceneJobPrivate(Qt3DCore.QAspectJobPrivate):
  """
  The cute side of Qt's Qt3DRender::Render::LoadSceneJobPrivate: a plain
  Python object standing in front of one C++
  Qt3DRender::Render::LoadSceneJobPrivate.

  It is built on the cute 'Qt3DCore::QAspectJobPrivate', as Qt's
  Qt3DRender::Render::LoadSceneJobPrivate is built on Qt's
  Qt3DCore::QAspectJobPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::LoadSceneJobPrivate that has a
  ritual and that Python can call so far, 2 names in all: 'postFrame',
  'q_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::Render::LoadSceneJobPrivate::~LoadSceneJobPrivate()':
    the destructor: Python never removes a C++
    Qt3DRender::Render::LoadSceneJobPrivate.
  - Qt's 'const LoadSceneJob
    *Qt3DRender::Render::LoadSceneJobPrivate::q_func() const': takes in
    Python what 'LoadSceneJob
    *Qt3DRender::Render::LoadSceneJobPrivate::q_func()' takes.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::LoadSceneJobPrivate is created at the first
    use, not by 'Qt3DRender::Render::LoadSceneJobPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::LoadSceneJobPrivate.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::LoadSceneJobPrivate'

  #  A C++ Qt3DRender::Render::LoadSceneJobPrivate Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_Render_LoadSceneJobPrivate'

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

  @overload(WAIT['Qt3DRender.Render.LoadSceneJob'])
  @overload(NoneType)
  def __init__(self, q: Optional[Qt3DRender.Render.LoadSceneJob]) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::Render::LoadSceneJobPrivate::LoadSceneJobPrivate(
    LoadSceneJob *q)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-loadscenejobprivate.html

    Parameters
    ----------

    q : Optional[Qt3DRender.Render.LoadSceneJob]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  Qt3DRender::Render::LoadSceneJobPrivate::LoadSceneJobPrivate(
    #      LoadSceneJob *q)
    self._noteCreation(LoadSceneJobPrivate, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render19LoadSceneJobPrivateC1EPNS0_12LoadSce'
        'neJobE',
        self._addressOf(q),
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

  @overload(WAIT['Qt3DCore.QAspectManager'])
  @overload(NoneType)
  def postFrame(self, manager: Optional[Qt3DCore.QAspectManager]) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::LoadSceneJobPrivate::postFrame(Qt3DCore::
    QAspectManager *manager)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-loadscenejobprivate.html

    Parameters
    ----------

    manager : Optional[Qt3DCore.QAspectManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::LoadSceneJobPrivate::postFrame(Qt3DCore::
    #      QAspectManager *manager)
    ritual = (
        'ritual_ZN10Qt3DRender6Render19LoadSceneJobPrivate9postFrameEPN8Qt3'
        'DCore14QAspectManagerE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render19LoadSceneJobPrivate9postFrameE'
          'PN8Qt3DCore14QAspectManagerE')
    self.uglySide.call(ritual, self._addressOf(manager))

  def q_func(self) -> Optional[Qt3DRender.Render.LoadSceneJob]:
    """
    Calls Qt's 'LoadSceneJob
    *Qt3DRender::Render::LoadSceneJobPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-loadscenejobprivate.html#q_func

    Returns
    -------

    Optional[Qt3DRender.Render.LoadSceneJob]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  LoadSceneJob *Qt3DRender::Render::LoadSceneJobPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render19LoadSceneJobPrivate6q_funcEv',
    )
    return Qt3DRender.Render.LoadSceneJob._cuteAt(address)
