"""
QSGSmoothColorMaterial binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgdefaultinternalrectanglenode_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QSGSmoothColorMaterial to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from . import QSGMaterial, QSGRendererInterface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QSGMaterialShader, QSGMaterialType

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGSmoothColorMaterial(QSGMaterial):
  """
  The cute side of Qt's QSGSmoothColorMaterial: a plain Python object
  standing in front of one C++ QSGSmoothColorMaterial.

  It is built on the cute 'QSGMaterial', as Qt's QSGSmoothColorMaterial is
  built on Qt's QSGMaterial, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGSmoothColorMaterial that has a ritual and that
  Python can call so far, 3 names in all: 'compare', 'type', 'createShader'.
  It can be made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ QSGSmoothColorMaterial is created at the first use, not by
    'QSGSmoothColorMaterial(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGSmoothColorMaterial.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGSmoothColorMaterial'

  #  A C++ QSGSmoothColorMaterial Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGSmoothColorMaterial'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSGMaterial)
  @overload(NoneType)
  def compare(self, other: Optional[QSGMaterial]) -> int:
    """
    Calls Qt's 'int QSGSmoothColorMaterial::compare(const QSGMaterial *other)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsmoothcolormaterial.html#compare

    Parameters
    ----------

    other : Optional[QSGMaterial]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QSGSmoothColorMaterial::compare(const QSGMaterial *other) const
    ritual = 'ritual_ZNK22QSGSmoothColorMaterial7compareEPK11QSGMaterial'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK22QSGSmoothColorMaterial7compareEPK11QSGMaterial')
    return self.uglySide.call(ritual, self._addressOf(other))

  def type(self) -> Optional[QSGMaterialType]:
    """
    Calls Qt's 'QSGMaterialType *QSGSmoothColorMaterial::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgsmoothcolormaterial.html#type

    Returns
    -------

    Optional[QSGMaterialType]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGMaterialType *QSGSmoothColorMaterial::type() const
    ritual = 'ritual_ZNK22QSGSmoothColorMaterial4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QSGSmoothColorMaterial4typeEv'
    address = self.uglySide.call(ritual)
    from . import QSGMaterialType
    return QSGMaterialType._cuteAt(address)

  @overload(QSGRendererInterface.RenderMode)
  def createShader(
      self,
      renderMode: QSGRendererInterface.RenderMode,
  ) -> Optional[QSGMaterialShader]:
    """
    Calls Qt's 'QSGMaterialShader
    *QSGSmoothColorMaterial::createShader(QSGRendererInterface::RenderMode
    renderMode) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsmoothcolormaterial.html#createShader

    Parameters
    ----------

    renderMode : QSGRendererInterface.RenderMode
      Passed on as its number.

    Returns
    -------

    Optional[QSGMaterialShader]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGMaterialShader
    #      *QSGSmoothColorMaterial::createShader(QSGRendererInterface::
    #      RenderMode renderMode) const
    ritual = (
        'ritual_ZNK22QSGSmoothColorMaterial12createShaderEN20QSGRendererInt'
        'erface10RenderModeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK22QSGSmoothColorMaterial12createShaderEN20QSGRende'
          'rerInterface10RenderModeE')
    address = self.uglySide.call(ritual, renderMode.value)
    from . import QSGMaterialShader
    return QSGMaterialShader._cuteAt(address)

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
    'QSGSmoothColorMaterial::QSGSmoothColorMaterial()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgsmoothcolormaterial.html#QSGSmoothColorMaterial
    """
    #  QSGSmoothColorMaterial::QSGSmoothColorMaterial()
    self._noteCreation(QSGSmoothColorMaterial, lambda: Rituals.call(
        'ritual_ZN22QSGSmoothColorMaterialC1Ev',
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
