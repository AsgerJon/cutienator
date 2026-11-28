"""
QSGDistanceFieldStyledTextMaterial binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgdistancefieldglyphnode_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSGDistanceFieldStyledTextMaterial to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QSGDistanceFieldTextMaterial, QSGMaterial, QSGRendererInterface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtGui import QColor, QVector4D
  from . import QSGMaterialShader, QSGMaterialType
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QColor = WAIT['QColor']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGDistanceFieldStyledTextMaterial(QSGDistanceFieldTextMaterial):
  """
  The cute side of Qt's QSGDistanceFieldStyledTextMaterial: a plain Python
  object standing in front of one C++ QSGDistanceFieldStyledTextMaterial.

  It is built on the cute 'QSGDistanceFieldTextMaterial', as Qt's
  QSGDistanceFieldStyledTextMaterial is built on Qt's
  QSGDistanceFieldTextMaterial, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGDistanceFieldStyledTextMaterial that has a ritual
  and that Python can call so far, 5 names in all: 'type', 'createShader',
  'compare', 'setStyleColor', 'styleColor'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'QSGDistanceFieldStyledTextMaterial::~QSGDistanceFieldStyledTextMaterial(
    )': the destructor: Python never removes a C++
    QSGDistanceFieldStyledTextMaterial.

  What to expect
  --------------

  - The C++ QSGDistanceFieldStyledTextMaterial is created at the first use,
    not by 'QSGDistanceFieldStyledTextMaterial(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGDistanceFieldStyledTextMaterial.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGDistanceFieldStyledTextMaterial'

  #  A C++ QSGDistanceFieldStyledTextMaterial Python makes is of a C++ class
  #  of ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGDistanceFieldStyledTextMaterial'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def type(self) -> Optional[QSGMaterialType]:
    """
    Calls Qt's 'QSGMaterialType *QSGDistanceFieldStyledTextMaterial::type()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldstyledtextmaterial.html#type

    Returns
    -------

    Optional[QSGMaterialType]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGMaterialType *QSGDistanceFieldStyledTextMaterial::type() const
    address = self.uglySide.call(
        'ritual_ZNK34QSGDistanceFieldStyledTextMaterial4typeEv',
    )
    from . import QSGMaterialType
    return QSGMaterialType._cuteAt(address)

  @overload(QSGRendererInterface.RenderMode)
  def createShader(
      self,
      renderMode: QSGRendererInterface.RenderMode,
  ) -> Optional[QSGMaterialShader]:
    """
    Calls Qt's 'QSGMaterialShader
    *QSGDistanceFieldStyledTextMaterial::createShader(QSGRendererInterface::
    RenderMode renderMode) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldstyledtextmaterial.html

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
    #  QSGMaterialShader *QSGDistanceFieldStyledTextMaterial::createShader(
    #      QSGRendererInterface::RenderMode renderMode) const
    address = self.uglySide.call(
        'ritual_ZNK34QSGDistanceFieldStyledTextMaterial12createShaderEN20QS'
        'GRendererInterface10RenderModeE',
        renderMode.value,
    )
    from . import QSGMaterialShader
    return QSGMaterialShader._cuteAt(address)

  @overload(QSGMaterial)
  @overload(NoneType)
  def compare(self, other: Optional[QSGMaterial]) -> int:
    """
    Calls Qt's 'int QSGDistanceFieldStyledTextMaterial::compare(const
    QSGMaterial *other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldstyledtextmaterial.html#compare

    Parameters
    ----------

    other : Optional[QSGMaterial]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QSGDistanceFieldStyledTextMaterial::compare(const QSGMaterial
    #      *other) const
    ritual = (
        'ritual_ZNK34QSGDistanceFieldStyledTextMaterial7compareEPK11QSGMate'
        'rial')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK34QSGDistanceFieldStyledTextMaterial7compareEPK11Q'
          'SGMaterial')
    return self.uglySide.call(ritual, self._addressOf(other))

  def styleColor(self) -> QVector4D:
    """
    Calls Qt's 'const QVector4D
    &QSGDistanceFieldStyledTextMaterial::styleColor() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldstyledtextmaterial.html#styleColor

    Returns
    -------

    QVector4D
      A new cute QVector4D around the copy Qt gave back. Python owns it.
    """
    #  const QVector4D &QSGDistanceFieldStyledTextMaterial::styleColor()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK34QSGDistanceFieldStyledTextMaterial10styleColorEv',
    )
    from ..QtGui import QVector4D
    return QVector4D._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QColor)
  def setStyleColor(self, color: QColor) -> None:
    """
    Calls Qt's 'void QSGDistanceFieldStyledTextMaterial::setStyleColor(const
    QColor &color)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldstyledtextmaterial.html

    Parameters
    ----------

    color : QColor
      Passed on as a value: Qt reads the C++ QColor, which stays Python's
      own.
    """
    #  void QSGDistanceFieldStyledTextMaterial::setStyleColor(const QColor
    #      &color)
    self.uglySide.call(
        'ritual_ZN34QSGDistanceFieldStyledTextMaterial13setStyleColorERK6QC'
        'olor',
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
    'QSGDistanceFieldStyledTextMaterial::QSGDistanceFieldStyledTextMaterial(
    )', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldstyledtextmaterial.html
    """
    #  QSGDistanceFieldStyledTextMaterial::
    #      QSGDistanceFieldStyledTextMaterial()
    self._noteCreation(
        QSGDistanceFieldStyledTextMaterial, lambda: Rituals.call(
            'ritual_ZN34QSGDistanceFieldStyledTextMaterialC1Ev',
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
