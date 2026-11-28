"""
QSGDistanceFieldShiftedStyleTextMaterial binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qsgdistancefieldglyphnode_p_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSGDistanceFieldShiftedStyleTextMaterial to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QSGDistanceFieldStyledTextMaterial, QSGMaterial
from . import QSGRendererInterface

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QPointF
  from . import QSGMaterialShader, QSGMaterialType
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPointF = WAIT['QPointF']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSGDistanceFieldShiftedStyleTextMaterial(QSGDistanceFieldStyledTextMaterial):
  """
  The cute side of Qt's QSGDistanceFieldShiftedStyleTextMaterial: a plain
  Python object standing in front of one C++
  QSGDistanceFieldShiftedStyleTextMaterial.

  It is built on the cute 'QSGDistanceFieldStyledTextMaterial', as Qt's
  QSGDistanceFieldShiftedStyleTextMaterial is built on Qt's
  QSGDistanceFieldStyledTextMaterial, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSGDistanceFieldShiftedStyleTextMaterial that has a
  ritual and that Python can call so far, 5 names in all: 'type',
  'createShader', 'compare', 'setShift', 'shift'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSGDistanceFieldShiftedStyleTextMaterial::
    ~QSGDistanceFieldShiftedStyleTextMaterial()': the destructor: Python
    never removes a C++ QSGDistanceFieldShiftedStyleTextMaterial.

  What to expect
  --------------

  - The C++ QSGDistanceFieldShiftedStyleTextMaterial is created at the first
    use, not by 'QSGDistanceFieldShiftedStyleTextMaterial(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSGDistanceFieldShiftedStyleTextMaterial.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSGDistanceFieldShiftedStyleTextMaterial'

  #  A C++ QSGDistanceFieldShiftedStyleTextMaterial Python makes is of a C++
  #  class of ours, in which Python can take functions over. This ritual
  #  hands one over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSGDistanceFieldShiftedStyleTextMaterial'

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
    *QSGDistanceFieldShiftedStyleTextMaterial::type() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldshiftedstyletextmaterial.html#type

    Returns
    -------

    Optional[QSGMaterialType]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSGMaterialType *QSGDistanceFieldShiftedStyleTextMaterial::type()
    #      const
    ritual = 'ritual_ZNK40QSGDistanceFieldShiftedStyleTextMaterial4typeEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK40QSGDistanceFieldShiftedStyleTextMaterial4typeEv')
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
    *QSGDistanceFieldShiftedStyleTextMaterial::createShader(
    QSGRendererInterface::RenderMode renderMode) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldshiftedstyletextmaterial.html

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
    #      *QSGDistanceFieldShiftedStyleTextMaterial::createShader(
    #      QSGRendererInterface::RenderMode renderMode) const
    ritual = (
        'ritual_ZNK40QSGDistanceFieldShiftedStyleTextMaterial12createShader'
        'EN20QSGRendererInterface10RenderModeE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK40QSGDistanceFieldShiftedStyleTextMaterial12create'
          'ShaderEN20QSGRendererInterface10RenderModeE')
    address = self.uglySide.call(ritual, renderMode.value)
    from . import QSGMaterialShader
    return QSGMaterialShader._cuteAt(address)

  @overload(QSGMaterial)
  @overload(NoneType)
  def compare(self, other: Optional[QSGMaterial]) -> int:
    """
    Calls Qt's 'int QSGDistanceFieldShiftedStyleTextMaterial::compare(const
    QSGMaterial *other) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldshiftedstyletextmaterial.html

    Parameters
    ----------

    other : Optional[QSGMaterial]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  int QSGDistanceFieldShiftedStyleTextMaterial::compare(const
    #      QSGMaterial *other) const
    ritual = (
        'ritual_ZNK40QSGDistanceFieldShiftedStyleTextMaterial7compareEPK11Q'
        'SGMaterial')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK40QSGDistanceFieldShiftedStyleTextMaterial7compare'
          'EPK11QSGMaterial')
    return self.uglySide.call(ritual, self._addressOf(other))

  def shift(self) -> QPointF:
    """
    Calls Qt's 'const QPointF
    &QSGDistanceFieldShiftedStyleTextMaterial::shift() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldshiftedstyletextmaterial.html

    Returns
    -------

    QPointF
      A new cute QPointF around the copy Qt gave back. Python owns it.
    """
    #  const QPointF &QSGDistanceFieldShiftedStyleTextMaterial::shift() const
    address = self.uglySide.call(
        'ritual_ZNK40QSGDistanceFieldShiftedStyleTextMaterial5shiftEv',
    )
    from ..QtCore import QPointF
    return QPointF._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPointF)
  def setShift(self, shift: QPointF) -> None:
    """
    Calls Qt's 'void QSGDistanceFieldShiftedStyleTextMaterial::setShift(const
    QPointF &shift)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldshiftedstyletextmaterial.html

    Parameters
    ----------

    shift : QPointF
      Passed on as a value: Qt reads the C++ QPointF, which stays Python's
      own.
    """
    #  void QSGDistanceFieldShiftedStyleTextMaterial::setShift(const QPointF
    #      &shift)
    self.uglySide.call(
        'ritual_ZN40QSGDistanceFieldShiftedStyleTextMaterial8setShiftERK7QP'
        'ointF',
        self._valueOf(shift, 'QPointF'),
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
    'QSGDistanceFieldShiftedStyleTextMaterial::
    QSGDistanceFieldShiftedStyleTextMaterial()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qsgdistancefieldshiftedstyletextmaterial.html
    """
    #  QSGDistanceFieldShiftedStyleTextMaterial::
    #      QSGDistanceFieldShiftedStyleTextMaterial()
    self._noteCreation(
        QSGDistanceFieldShiftedStyleTextMaterial, lambda: Rituals.call(
            'ritual_ZN40QSGDistanceFieldShiftedStyleTextMaterialC1Ev',
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
