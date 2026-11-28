"""
Qt3DRender::Render::SubtreeEnabler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/subtreeenabler_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means Qt3DRender::Render::SubtreeEnabler to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class SubtreeEnabler(Qt3DRender.Render.FrameGraphNode):
  """
  The cute side of Qt's Qt3DRender::Render::SubtreeEnabler: a plain Python
  object standing in front of one C++ Qt3DRender::Render::SubtreeEnabler.

  It is built on the cute 'Qt3DRender::Render::FrameGraphNode', as Qt's
  Qt3DRender::Render::SubtreeEnabler is built on Qt's
  Qt3DRender::Render::FrameGraphNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::SubtreeEnabler that has a ritual
  and that Python can call so far, 2 names in all: 'enablement',
  'syncFromFrontEnd'. It can be made from Python, in 1 way; see '__init__'.

  What has no ritual
  ------------------

  1 of the 4 functions Qt declares: 1 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::SubtreeEnabler is created at the first use,
    not by 'Qt3DRender::Render::SubtreeEnabler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::SubtreeEnabler.
  - Each name of Qt's Qt3DRender::Render::SubtreeEnabler that has no cute
    function yet, 'sendDisableToFrontend', holds a function that raises
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
  __qt_class__ = 'Qt3DRender::Render::SubtreeEnabler'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def enablement(self) -> Qt3DRender.QSubtreeEnabler.Enablement:
    """
    Calls Qt's 'QSubtreeEnabler::Enablement
    Qt3DRender::Render::SubtreeEnabler::enablement() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-subtreeenabler.html#enablement

    Returns
    -------

    Qt3DRender.QSubtreeEnabler.Enablement
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DRender.QSubtreeEnabler.Enablement(number)' gives.
    """
    #  QSubtreeEnabler::Enablement
    #      Qt3DRender::Render::SubtreeEnabler::enablement() const
    return Qt3DRender.QSubtreeEnabler.Enablement(self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render14SubtreeEnabler10enablementEv',
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::Render::SubtreeEnabler::SubtreeEnabler()', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-subtreeenabler.html
    """
    #  Qt3DRender::Render::SubtreeEnabler::SubtreeEnabler()
    self._noteCreation(SubtreeEnabler, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render14SubtreeEnablerC1Ev',
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

  @overload(WAIT['Qt3DCore.QNode'], bool)
  @overload(NoneType, bool)
  def syncFromFrontEnd(
      self,
      frontEnd: Optional[Qt3DCore.QNode],
      firstTime: bool,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::SubtreeEnabler::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-subtreeenabler.html

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DRender::Render::SubtreeEnabler::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN10Qt3DRender6Render14SubtreeEnabler16syncFromFrontEndEPKN'
        '8Qt3DCore5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render14SubtreeEnabler16syncFromFrontE'
          'ndEPKN8Qt3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)

  @staticmethod
  def sendDisableToFrontend(*__, **_) -> Never:
    """
    Qt's 'void Qt3DRender::Render::SubtreeEnabler::sendDisableToFrontend()':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.SubtreeEnabler.sendDisableToFrontend' has no "
        "cute function yet. Qt's 'void "
        "Qt3DRender::Render::SubtreeEnabler::sendDisableToFrontend()': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")
