"""
Qt3DRender::Render::ParameterPack binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/parameterpack_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DRender::Render::ParameterPack to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class ParameterPack(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DRender::Render::ParameterPack: a plain Python
  object standing in front of one C++ Qt3DRender::Render::ParameterPack.

  C++ hands a Qt3DRender::Render::ParameterPack around as a copy, so every
  C++ Qt3DRender::Render::ParameterPack behind a cute one is Python's own: it
  is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::ParameterPack that has a ritual
  and that Python can call so far, 3 names in all: 'clear',
  'appendParameter', 'removeParameter'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::Render::ParameterPack::~ParameterPack()': the
    destructor: Python removes its C++ Qt3DRender::Render::ParameterPack by
    it, and has no other use for it.
  - Qt's 'QList<Qt3DCore::QNodeId>
    Qt3DRender::Render::ParameterPack::parameters() const': gives a type
    Python has no way to take yet.
  - Qt's 'void Qt3DRender::Render::ParameterPack::setParameters(const
    Qt3DCore::QNodeIdVector &parameterIds)': takes a type Python has no way
    to hand over yet.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::ParameterPack is created at the first use,
    not by 'Qt3DRender::Render::ParameterPack(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DRender::Render::ParameterPack back gives a copy
    the ritual made for Python, in a new cute
    Qt3DRender::Render::ParameterPack.
  - Each name of Qt's Qt3DRender::Render::ParameterPack that has no cute
    function yet, 'parameters', 'setParameters', holds a function that raises
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
  __qt_class__ = 'Qt3DRender::Render::ParameterPack'

  #  Qt's '~Qt3DRender::Render::ParameterPack()'. Naming it makes this a
  #  value class: Python owns every C++ Qt3DRender::Render::ParameterPack
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10Qt3DRender6Render13ParameterPackD1Ev'

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
    'Qt3DRender::Render::ParameterPack::ParameterPack()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-parameterpack.html#ParameterPack
    """
    #  Qt3DRender::Render::ParameterPack::ParameterPack()
    self._noteCreation(ParameterPack, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render13ParameterPackC1Ev',
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

  def clear(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::ParameterPack::clear()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-parameterpack.html#clear
    """
    #  void Qt3DRender::Render::ParameterPack::clear()
    self.uglySide.call('ritual_ZN10Qt3DRender6Render13ParameterPack5clearEv')

  @overload(WAIT['Qt3DCore.QNodeId'])
  def appendParameter(self, parameterId: Qt3DCore.QNodeId) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::ParameterPack::appendParameter(Qt3DCore::QNodeId
    parameterId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-parameterpack.html

    Parameters
    ----------

    parameterId : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DRender::Render::ParameterPack::appendParameter(Qt3DCore::
    #      QNodeId parameterId)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render13ParameterPack15appendParameterEN8Qt3'
        'DCore7QNodeIdE',
        self._valueOf(parameterId),
    )

  @overload(WAIT['Qt3DCore.QNodeId'])
  def removeParameter(self, parameterId: Qt3DCore.QNodeId) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::ParameterPack::removeParameter(Qt3DCore::QNodeId
    parameterId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-parameterpack.html

    Parameters
    ----------

    parameterId : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DRender::Render::ParameterPack::removeParameter(Qt3DCore::
    #      QNodeId parameterId)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render13ParameterPack15removeParameterEN8Qt3'
        'DCore7QNodeIdE',
        self._valueOf(parameterId),
    )

  @staticmethod
  def parameters(*__, **_) -> Never:
    """
    Qt's 'QList<Qt3DCore::QNodeId>
    Qt3DRender::Render::ParameterPack::parameters() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.ParameterPack.parameters' has no cute function "
        "yet. Qt's 'QList<Qt3DCore::QNodeId> "
        "Qt3DRender::Render::ParameterPack::parameters() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def setParameters(*__, **_) -> Never:
    """
    Qt's 'void Qt3DRender::Render::ParameterPack::setParameters(const
    Qt3DCore::QNodeIdVector &parameterIds)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.ParameterPack.setParameters' has no cute "
        "function yet. Qt's 'void "
        "Qt3DRender::Render::ParameterPack::setParameters(const "
        "Qt3DCore::QNodeIdVector &parameterIds)': takes a type Python has "
        "no way to hand over yet.")
