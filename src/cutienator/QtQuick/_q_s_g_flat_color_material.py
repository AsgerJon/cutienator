"""
QSGFlatColorMaterial binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/qsgflatcolormaterial.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QSGMaterial, QSGRendererInterface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QColor
  from . import QSGMaterialShader, QSGMaterialType
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGFlatColorMaterial(QSGMaterial):
  """
  The cute side of Qt's QSGFlatColorMaterial: a plain Python object standing
  in front of one C++ QSGFlatColorMaterial.

  It is built on the cute 'QSGMaterial', as Qt's QSGFlatColorMaterial is
  built on Qt's QSGMaterial, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGFlatColorMaterial that has a ritual and that
  Python can call so far, 5 names in all: 'type', 'createShader', 'setColor',
  'color', 'compare'. It can be made from Python, in 1 way; see '__init__'.

  What to expect
  --------------

  - The C++ QSGFlatColorMaterial is created at the first use, not by
    'QSGFlatColorMaterial(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGFlatColorMaterial.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGFlatColorMaterial'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> Optional[QSGMaterialType]:
    """
    Calls Qt's 'QSGMaterialType *QSGFlatColorMaterial::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgflatcolormaterial.html#type

    Returns
    -------

    Optional[QSGMaterialType]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGMaterialType *QSGFlatColorMaterial::type() const
    ritual = 'ritual_ZNK20QSGFlatColorMaterial4typeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QSGFlatColorMaterial4typeEv'
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
    *QSGFlatColorMaterial::createShader(QSGRendererInterface::RenderMode
    renderMode) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgflatcolormaterial.html#createShader

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
    #      *QSGFlatColorMaterial::createShader(QSGRendererInterface::
    #      RenderMode renderMode) const
    ritual = (
        'ritual_ZNK20QSGFlatColorMaterial12createShaderEN20QSGRendererInter'
        'face10RenderModeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK20QSGFlatColorMaterial12createShaderEN20QSGRendere'
          'rInterface10RenderModeE')
    address = self.uglySide.call(ritual, renderMode.value)
    from . import QSGMaterialShader
    return QSGMaterialShader._cuteAt(address)

  def color(self) -> QColor:
    """
    Calls Qt's 'const QColor &QSGFlatColorMaterial::color() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgflatcolormaterial.html#color

    Returns
    -------

    QColor
      A new cute QColor around the copy Qt gave back. Python owns it.
    """
    #  const QColor &QSGFlatColorMaterial::color() const
    address = self.uglySide.call('ritual_ZNK20QSGFlatColorMaterial5colorEv')
    from ..QtGui import QColor
    return QColor._cuteOwning(address)

  @overload(QSGMaterial)
  @overload(NoneType)
  def compare(self, other: Optional[QSGMaterial]) -> int:
    """
    Calls Qt's 'int QSGFlatColorMaterial::compare(const QSGMaterial *other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qsgflatcolormaterial.html#compare

    Parameters
    ----------

    other : Optional[QSGMaterial]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QSGFlatColorMaterial::compare(const QSGMaterial *other) const
    ritual = 'ritual_ZNK20QSGFlatColorMaterial7compareEPK11QSGMaterial'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QSGFlatColorMaterial7compareEPK11QSGMaterial'
    return self.uglySide.call(ritual, self._addressOf(other))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QColor)
  def setColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QSGFlatColorMaterial::setColor(const QColor &color)'.

    Qt's own words: https://doc.qt.io/qt-6/qsgflatcolormaterial.html#setColor

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSGFlatColorMaterial::setColor(const QColor &color)
    self.uglySide.call(
        'ritual_ZN20QSGFlatColorMaterial8setColorERK6QColor',
        self._valueOf(color),
    )

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
    'QSGFlatColorMaterial::QSGFlatColorMaterial()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgflatcolormaterial.html#QSGFlatColorMaterial
    """
    #  QSGFlatColorMaterial::QSGFlatColorMaterial()
    self._noteCreation(QSGFlatColorMaterial, lambda: Rituals.call(
        'ritual_ZN20QSGFlatColorMaterialC1Ev',
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
