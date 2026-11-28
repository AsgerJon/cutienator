"""
Qt3DRender::Render::Parameter binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/parameter_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DRender::Render::Parameter to be private: it declares the
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
  from typing import Optional

  from ..QtCore import QVariant

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Parameter(Qt3DRender.Render.BackendNode):
  """
  The cute side of Qt's Qt3DRender::Render::Parameter: a plain Python object
  standing in front of one C++ Qt3DRender::Render::Parameter.

  It is built on the cute 'Qt3DRender::Render::BackendNode', as Qt's
  Qt3DRender::Render::Parameter is built on Qt's
  Qt3DRender::Render::BackendNode, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::Parameter that has a ritual and
  that Python can call so far, 6 names in all: 'cleanup', 'syncFromFrontEnd',
  'name', 'nameId', 'uniformValue', 'backendValue'. It can be made from
  Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::Parameter is created at the first use, not by
    'Qt3DRender::Render::Parameter(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::Parameter.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::Parameter'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> str:
    """
    Calls Qt's 'QString Qt3DRender::Render::Parameter::name() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-parameter.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DRender::Render::Parameter::name() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render9Parameter4nameEv',
    )

  def nameId(self) -> int:
    """
    Calls Qt's 'int Qt3DRender::Render::Parameter::nameId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-parameter.html#nameId
    """
    #  int Qt3DRender::Render::Parameter::nameId() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render9Parameter6nameIdEv',
    )

  def uniformValue(self) -> Qt3DRender.Render.UniformValue:
    """
    Calls Qt's 'const UniformValue
    &Qt3DRender::Render::Parameter::uniformValue() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-parameter.html#uniformValue

    Returns
    -------

    Qt3DRender.Render.UniformValue
      A new cute Qt3DRender::Render::UniformValue around the copy Qt gave
      back. Python owns it.
    """
    #  const UniformValue &Qt3DRender::Render::Parameter::uniformValue()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render9Parameter12uniformValueEv',
    )
    return Qt3DRender.Render.UniformValue._cuteOwning(address)

  def backendValue(self) -> QVariant:
    """
    Calls Qt's 'QVariant Qt3DRender::Render::Parameter::backendValue()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-parameter.html#backendValue

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant Qt3DRender::Render::Parameter::backendValue() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render9Parameter12backendValueEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

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
    'Qt3DRender::Render::Parameter::Parameter()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-parameter.html#Parameter
    """
    #  Qt3DRender::Render::Parameter::Parameter()
    self._noteCreation(Parameter, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render9ParameterC1Ev',
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

  def cleanup(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::Parameter::cleanup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-parameter.html#cleanup
    """
    #  void Qt3DRender::Render::Parameter::cleanup()
    self.uglySide.call('ritual_ZN10Qt3DRender6Render9Parameter7cleanupEv')

  @overload(WAIT['Qt3DCore.QNode'], bool)
  @overload(NoneType, bool)
  def syncFromFrontEnd(
      self,
      frontEnd: Optional[Qt3DCore.QNode],
      firstTime: bool,
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::Parameter::syncFromFrontEnd(const
    Qt3DCore::QNode *frontEnd, bool firstTime)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-parameter.html#syncFromFrontEnd

    Parameters
    ----------

    frontEnd : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    firstTime : bool
      Passed on as it is.
    """
    #  void Qt3DRender::Render::Parameter::syncFromFrontEnd(const
    #      Qt3DCore::QNode *frontEnd, bool firstTime)
    ritual = (
        'ritual_ZN10Qt3DRender6Render9Parameter16syncFromFrontEndEPKN8Qt3DC'
        'ore5QNodeEb')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender6Render9Parameter16syncFromFrontEndEPKN'
          '8Qt3DCore5QNodeEb')
    self.uglySide.call(ritual, self._addressOf(frontEnd), firstTime)
