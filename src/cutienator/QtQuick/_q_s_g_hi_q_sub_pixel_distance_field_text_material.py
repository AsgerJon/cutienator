"""
QSGHiQSubPixelDistanceFieldTextMaterial binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgdistancefieldglyphnode_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSGHiQSubPixelDistanceFieldTextMaterial to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from . import QSGDistanceFieldTextMaterial, QSGRendererInterface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QColor
  from . import QSGMaterialShader, QSGMaterialType
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']


class QSGHiQSubPixelDistanceFieldTextMaterial(QSGDistanceFieldTextMaterial):
  """
  The cute side of Qt's QSGHiQSubPixelDistanceFieldTextMaterial: a plain
  Python object standing in front of one C++
  QSGHiQSubPixelDistanceFieldTextMaterial.

  It is built on the cute 'QSGDistanceFieldTextMaterial', as Qt's
  QSGHiQSubPixelDistanceFieldTextMaterial is built on Qt's
  QSGDistanceFieldTextMaterial, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGHiQSubPixelDistanceFieldTextMaterial that has a
  ritual and that Python can call so far, 3 names in all: 'type',
  'createShader', 'setColor'. None can be made from Python: one comes out of
  a function of another class that gives one back.

  What to expect
  --------------

  - The C++ QSGHiQSubPixelDistanceFieldTextMaterial is created at the first
    use, not by 'QSGHiQSubPixelDistanceFieldTextMaterial(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGHiQSubPixelDistanceFieldTextMaterial.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGHiQSubPixelDistanceFieldTextMaterial'

  #  A C++ QSGHiQSubPixelDistanceFieldTextMaterial Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGHiQSubPixelDistanceFieldTextMaterial'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> Optional[QSGMaterialType]:
    """
    Calls Qt's 'QSGMaterialType
    *QSGHiQSubPixelDistanceFieldTextMaterial::type() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsghiqsubpixeldistancefieldtextmaterial.html#type

    Returns
    -------

    Optional[QSGMaterialType]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGMaterialType *QSGHiQSubPixelDistanceFieldTextMaterial::type() const
    ritual = 'ritual_ZNK39QSGHiQSubPixelDistanceFieldTextMaterial4typeEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK39QSGHiQSubPixelDistanceFieldTextMaterial4typeEv')
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
    *QSGHiQSubPixelDistanceFieldTextMaterial::createShader(
    QSGRendererInterface::RenderMode renderMode) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsghiqsubpixeldistancefieldtextmaterial.html

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
    #      *QSGHiQSubPixelDistanceFieldTextMaterial::createShader(
    #      QSGRendererInterface::RenderMode renderMode) const
    ritual = (
        'ritual_ZNK39QSGHiQSubPixelDistanceFieldTextMaterial12createShaderE'
        'N20QSGRendererInterface10RenderModeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK39QSGHiQSubPixelDistanceFieldTextMaterial12createS'
          'haderEN20QSGRendererInterface10RenderModeE')
    address = self.uglySide.call(ritual, renderMode.value)
    from . import QSGMaterialShader
    return QSGMaterialShader._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QSGHiQSubPixelDistanceFieldTextMaterial::setColor(const
    QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsghiqsubpixeldistancefieldtextmaterial.html

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSGHiQSubPixelDistanceFieldTextMaterial::setColor(const QColor
    #      &color)
    ritual = (
        'ritual_ZN39QSGHiQSubPixelDistanceFieldTextMaterial8setColorERK6QCo'
        'lor')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN39QSGHiQSubPixelDistanceFieldTextMaterial8setColorE'
          'RK6QColor')
    self.uglySide.call(ritual, self._valueOf(color))

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
