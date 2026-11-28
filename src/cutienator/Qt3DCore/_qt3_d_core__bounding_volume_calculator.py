"""
Qt3DCore::BoundingVolumeCalculator binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DCore/6.12.0/Qt3DCore/private/qgeometryview_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DCore::BoundingVolumeCalculator to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtGui import QVector3D


class BoundingVolumeCalculator(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DCore::BoundingVolumeCalculator: a plain Python
  object standing in front of one C++ Qt3DCore::BoundingVolumeCalculator.

  C++ hands a Qt3DCore::BoundingVolumeCalculator around as a copy, so every
  C++ Qt3DCore::BoundingVolumeCalculator behind a cute one is Python's own:
  it is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's Qt3DCore::BoundingVolumeCalculator that has a ritual
  and that Python can call so far, 5 names in all: 'min', 'max', 'center',
  'radius', 'isValid'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DCore::BoundingVolumeCalculator::~BoundingVolumeCalculator()':
    the destructor: Python removes its C++ Qt3DCore::BoundingVolumeCalculator
    by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 8 functions Qt declares: 1 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ Qt3DCore::BoundingVolumeCalculator is created at the first use,
    not by 'Qt3DCore::BoundingVolumeCalculator(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a Qt3DCore::BoundingVolumeCalculator back gives a copy
    the ritual made for Python, in a new cute
    Qt3DCore::BoundingVolumeCalculator.
  - Each name of Qt's Qt3DCore::BoundingVolumeCalculator that has no cute
    function yet, 'apply', holds a function that raises
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
  __qt_class__ = 'Qt3DCore::BoundingVolumeCalculator'

  #  Qt's '~Qt3DCore::BoundingVolumeCalculator()'. Naming it makes this a
  #  value class: Python owns every C++ Qt3DCore::BoundingVolumeCalculator
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN8Qt3DCore24BoundingVolumeCalculatorD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def min(self) -> QVector3D:
    """
    Calls Qt's 'const QVector3D Qt3DCore::BoundingVolumeCalculator::min()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-boundingvolumecalculator.html#min

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  const QVector3D Qt3DCore::BoundingVolumeCalculator::min() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore24BoundingVolumeCalculator3minEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def max(self) -> QVector3D:
    """
    Calls Qt's 'const QVector3D Qt3DCore::BoundingVolumeCalculator::max()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-boundingvolumecalculator.html#max

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  const QVector3D Qt3DCore::BoundingVolumeCalculator::max() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore24BoundingVolumeCalculator3maxEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def center(self) -> QVector3D:
    """
    Calls Qt's 'const QVector3D Qt3DCore::BoundingVolumeCalculator::center()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-boundingvolumecalculator.html#center

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  const QVector3D Qt3DCore::BoundingVolumeCalculator::center() const
    address = self.uglySide.call(
        'ritual_ZNK8Qt3DCore24BoundingVolumeCalculator6centerEv',
    )
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def radius(self) -> float:
    """
    Calls Qt's 'float Qt3DCore::BoundingVolumeCalculator::radius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-boundingvolumecalculator.html#radius
    """
    #  float Qt3DCore::BoundingVolumeCalculator::radius() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore24BoundingVolumeCalculator6radiusEv',
    )

  def isValid(self) -> bool:
    """
    Calls Qt's 'bool Qt3DCore::BoundingVolumeCalculator::isValid() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-boundingvolumecalculator.html#isValid
    """
    #  bool Qt3DCore::BoundingVolumeCalculator::isValid() const
    return self.uglySide.call(
        'ritual_ZNK8Qt3DCore24BoundingVolumeCalculator7isValidEv',
    )

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
    'Qt3DCore::BoundingVolumeCalculator::BoundingVolumeCalculator()', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3dcore-boundingvolumecalculator.html
    """
    #  Qt3DCore::BoundingVolumeCalculator::BoundingVolumeCalculator()
    self._noteCreation(BoundingVolumeCalculator, lambda: Rituals.call(
        'ritual_ZN8Qt3DCore24BoundingVolumeCalculatorC1Ev',
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

  @staticmethod
  def apply(*__, **_) -> Never:
    """
    Qt's 'bool Qt3DCore::BoundingVolumeCalculator::apply(QAttribute
    *positionAttribute, QAttribute *indexAttribute, int drawVertexCount, bool
    primitiveRestartEnabled, int primitiveRestartIndex)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'FindMaxDistantPoint'; did you mean
    'maxDistantPointY'?.
    """
    raise NotImplementedError(
        "'Qt3DCore.BoundingVolumeCalculator.apply' has no cute function "
        "yet. Qt's 'bool "
        "Qt3DCore::BoundingVolumeCalculator::apply(QAttribute "
        "*positionAttribute, QAttribute *indexAttribute, int "
        "drawVertexCount, bool primitiveRestartEnabled, int "
        "primitiveRestartIndex)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'FindMaxDistantPoint'; did you mean "
        "'maxDistantPointY'?.")
