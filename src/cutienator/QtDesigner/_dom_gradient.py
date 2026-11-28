"""
DomGradient binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means DomGradient to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import DomGradientStop
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  DomGradientStop = WAIT['DomGradientStop']


class DomGradient(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's DomGradient: a plain Python object standing in front
  of one C++ DomGradient.

  What exists
  -----------

  Every function of Qt's DomGradient that has a ritual and that Python can
  call so far, 54 names in all: 'hasAttributeStartX', 'attributeStartX',
  'setAttributeStartX', 'clearAttributeStartX', 'hasAttributeStartY',
  'attributeStartY', 'setAttributeStartY', 'clearAttributeStartY',
  'hasAttributeEndX', 'attributeEndX', 'setAttributeEndX',
  'clearAttributeEndX', 'hasAttributeEndY', 'attributeEndY',
  'setAttributeEndY', 'clearAttributeEndY', 'hasAttributeCentralX',
  'attributeCentralX', 'setAttributeCentralX', 'clearAttributeCentralX',
  'hasAttributeCentralY', 'attributeCentralY', 'setAttributeCentralY',
  'clearAttributeCentralY', 'hasAttributeFocalX', 'attributeFocalX',
  'setAttributeFocalX', 'clearAttributeFocalX', 'hasAttributeFocalY',
  'attributeFocalY', 'setAttributeFocalY', 'clearAttributeFocalY',
  'hasAttributeRadius', 'attributeRadius', 'setAttributeRadius',
  'clearAttributeRadius', 'hasAttributeAngle', 'attributeAngle',
  'setAttributeAngle', 'clearAttributeAngle', 'hasAttributeType',
  'attributeType', 'setAttributeType', 'clearAttributeType',
  'hasAttributeSpread', 'attributeSpread', 'setAttributeSpread',
  'clearAttributeSpread', 'hasAttributeCoordinateMode',
  'attributeCoordinateMode', 'setAttributeCoordinateMode',
  'clearAttributeCoordinateMode', 'elementGradientStop',
  'setElementGradientStop'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'DomGradient::~DomGradient()': the destructor: Python never removes
    a C++ DomGradient.
  - Qt's 'void DomGradient::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
  - Qt's 'void DomGradient::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 62 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ DomGradient is created at the first use, not by
    'DomGradient(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ DomGradient.
  - Each name of Qt's DomGradient that has no cute function yet, 'read',
    'write', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'DomGradient'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasAttributeStartX(self) -> bool:
    """
    Calls Qt's 'bool DomGradient::hasAttributeStartX() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domgradient.html#hasAttributeStartX
    """
    #  bool DomGradient::hasAttributeStartX() const
    return self.uglySide.call(
        'ritual_ZNK11DomGradient18hasAttributeStartXEv',
    )

  def attributeStartX(self) -> float:
    """
    Calls Qt's 'double DomGradient::attributeStartX() const'.

    Qt's own words: https://doc.qt.io/qt-6/domgradient.html#attributeStartX
    """
    #  double DomGradient::attributeStartX() const
    return self.uglySide.call('ritual_ZNK11DomGradient15attributeStartXEv')

  def hasAttributeStartY(self) -> bool:
    """
    Calls Qt's 'bool DomGradient::hasAttributeStartY() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domgradient.html#hasAttributeStartY
    """
    #  bool DomGradient::hasAttributeStartY() const
    return self.uglySide.call(
        'ritual_ZNK11DomGradient18hasAttributeStartYEv',
    )

  def attributeStartY(self) -> float:
    """
    Calls Qt's 'double DomGradient::attributeStartY() const'.

    Qt's own words: https://doc.qt.io/qt-6/domgradient.html#attributeStartY
    """
    #  double DomGradient::attributeStartY() const
    return self.uglySide.call('ritual_ZNK11DomGradient15attributeStartYEv')

  def hasAttributeEndX(self) -> bool:
    """
    Calls Qt's 'bool DomGradient::hasAttributeEndX() const'.

    Qt's own words: https://doc.qt.io/qt-6/domgradient.html#hasAttributeEndX
    """
    #  bool DomGradient::hasAttributeEndX() const
    return self.uglySide.call('ritual_ZNK11DomGradient16hasAttributeEndXEv')

  def attributeEndX(self) -> float:
    """
    Calls Qt's 'double DomGradient::attributeEndX() const'.

    Qt's own words: https://doc.qt.io/qt-6/domgradient.html#attributeEndX
    """
    #  double DomGradient::attributeEndX() const
    return self.uglySide.call('ritual_ZNK11DomGradient13attributeEndXEv')

  def hasAttributeEndY(self) -> bool:
    """
    Calls Qt's 'bool DomGradient::hasAttributeEndY() const'.

    Qt's own words: https://doc.qt.io/qt-6/domgradient.html#hasAttributeEndY
    """
    #  bool DomGradient::hasAttributeEndY() const
    return self.uglySide.call('ritual_ZNK11DomGradient16hasAttributeEndYEv')

  def attributeEndY(self) -> float:
    """
    Calls Qt's 'double DomGradient::attributeEndY() const'.

    Qt's own words: https://doc.qt.io/qt-6/domgradient.html#attributeEndY
    """
    #  double DomGradient::attributeEndY() const
    return self.uglySide.call('ritual_ZNK11DomGradient13attributeEndYEv')

  def hasAttributeCentralX(self) -> bool:
    """
    Calls Qt's 'bool DomGradient::hasAttributeCentralX() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domgradient.html#hasAttributeCentralX
    """
    #  bool DomGradient::hasAttributeCentralX() const
    return self.uglySide.call(
        'ritual_ZNK11DomGradient20hasAttributeCentralXEv',
    )

  def attributeCentralX(self) -> float:
    """
    Calls Qt's 'double DomGradient::attributeCentralX() const'.

    Qt's own words: https://doc.qt.io/qt-6/domgradient.html#attributeCentralX
    """
    #  double DomGradient::attributeCentralX() const
    return self.uglySide.call('ritual_ZNK11DomGradient17attributeCentralXEv')

  def hasAttributeCentralY(self) -> bool:
    """
    Calls Qt's 'bool DomGradient::hasAttributeCentralY() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domgradient.html#hasAttributeCentralY
    """
    #  bool DomGradient::hasAttributeCentralY() const
    return self.uglySide.call(
        'ritual_ZNK11DomGradient20hasAttributeCentralYEv',
    )

  def attributeCentralY(self) -> float:
    """
    Calls Qt's 'double DomGradient::attributeCentralY() const'.

    Qt's own words: https://doc.qt.io/qt-6/domgradient.html#attributeCentralY
    """
    #  double DomGradient::attributeCentralY() const
    return self.uglySide.call('ritual_ZNK11DomGradient17attributeCentralYEv')

  def hasAttributeFocalX(self) -> bool:
    """
    Calls Qt's 'bool DomGradient::hasAttributeFocalX() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domgradient.html#hasAttributeFocalX
    """
    #  bool DomGradient::hasAttributeFocalX() const
    return self.uglySide.call(
        'ritual_ZNK11DomGradient18hasAttributeFocalXEv',
    )

  def attributeFocalX(self) -> float:
    """
    Calls Qt's 'double DomGradient::attributeFocalX() const'.

    Qt's own words: https://doc.qt.io/qt-6/domgradient.html#attributeFocalX
    """
    #  double DomGradient::attributeFocalX() const
    return self.uglySide.call('ritual_ZNK11DomGradient15attributeFocalXEv')

  def hasAttributeFocalY(self) -> bool:
    """
    Calls Qt's 'bool DomGradient::hasAttributeFocalY() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domgradient.html#hasAttributeFocalY
    """
    #  bool DomGradient::hasAttributeFocalY() const
    return self.uglySide.call(
        'ritual_ZNK11DomGradient18hasAttributeFocalYEv',
    )

  def attributeFocalY(self) -> float:
    """
    Calls Qt's 'double DomGradient::attributeFocalY() const'.

    Qt's own words: https://doc.qt.io/qt-6/domgradient.html#attributeFocalY
    """
    #  double DomGradient::attributeFocalY() const
    return self.uglySide.call('ritual_ZNK11DomGradient15attributeFocalYEv')

  def hasAttributeRadius(self) -> bool:
    """
    Calls Qt's 'bool DomGradient::hasAttributeRadius() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domgradient.html#hasAttributeRadius
    """
    #  bool DomGradient::hasAttributeRadius() const
    return self.uglySide.call(
        'ritual_ZNK11DomGradient18hasAttributeRadiusEv',
    )

  def attributeRadius(self) -> float:
    """
    Calls Qt's 'double DomGradient::attributeRadius() const'.

    Qt's own words: https://doc.qt.io/qt-6/domgradient.html#attributeRadius
    """
    #  double DomGradient::attributeRadius() const
    return self.uglySide.call('ritual_ZNK11DomGradient15attributeRadiusEv')

  def hasAttributeAngle(self) -> bool:
    """
    Calls Qt's 'bool DomGradient::hasAttributeAngle() const'.

    Qt's own words: https://doc.qt.io/qt-6/domgradient.html#hasAttributeAngle
    """
    #  bool DomGradient::hasAttributeAngle() const
    return self.uglySide.call('ritual_ZNK11DomGradient17hasAttributeAngleEv')

  def attributeAngle(self) -> float:
    """
    Calls Qt's 'double DomGradient::attributeAngle() const'.

    Qt's own words: https://doc.qt.io/qt-6/domgradient.html#attributeAngle
    """
    #  double DomGradient::attributeAngle() const
    return self.uglySide.call('ritual_ZNK11DomGradient14attributeAngleEv')

  def hasAttributeType(self) -> bool:
    """
    Calls Qt's 'bool DomGradient::hasAttributeType() const'.

    Qt's own words: https://doc.qt.io/qt-6/domgradient.html#hasAttributeType
    """
    #  bool DomGradient::hasAttributeType() const
    return self.uglySide.call('ritual_ZNK11DomGradient16hasAttributeTypeEv')

  def attributeType(self) -> str:
    """
    Calls Qt's 'QString DomGradient::attributeType() const'.

    Qt's own words: https://doc.qt.io/qt-6/domgradient.html#attributeType

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomGradient::attributeType() const
    return self.uglySide.call('ritual_ZNK11DomGradient13attributeTypeEv')

  def hasAttributeSpread(self) -> bool:
    """
    Calls Qt's 'bool DomGradient::hasAttributeSpread() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domgradient.html#hasAttributeSpread
    """
    #  bool DomGradient::hasAttributeSpread() const
    return self.uglySide.call(
        'ritual_ZNK11DomGradient18hasAttributeSpreadEv',
    )

  def attributeSpread(self) -> str:
    """
    Calls Qt's 'QString DomGradient::attributeSpread() const'.

    Qt's own words: https://doc.qt.io/qt-6/domgradient.html#attributeSpread

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomGradient::attributeSpread() const
    return self.uglySide.call('ritual_ZNK11DomGradient15attributeSpreadEv')

  def hasAttributeCoordinateMode(self) -> bool:
    """
    Calls Qt's 'bool DomGradient::hasAttributeCoordinateMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domgradient.html#hasAttributeCoordinateMode
    """
    #  bool DomGradient::hasAttributeCoordinateMode() const
    return self.uglySide.call(
        'ritual_ZNK11DomGradient26hasAttributeCoordinateModeEv',
    )

  def attributeCoordinateMode(self) -> str:
    """
    Calls Qt's 'QString DomGradient::attributeCoordinateMode() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domgradient.html#attributeCoordinateMode

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString DomGradient::attributeCoordinateMode() const
    return self.uglySide.call(
        'ritual_ZNK11DomGradient23attributeCoordinateModeEv',
    )

  def elementGradientStop(self) -> QList[DomGradientStop]:
    """
    Calls Qt's 'QList<DomGradientStop *> DomGradient::elementGradientStop()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/domgradient.html#elementGradientStop

    Returns
    -------

    QList[DomGradientStop]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<DomGradientStop *> DomGradient::elementGradientStop() const
    address = self.uglySide.call(
        'ritual_ZNK11DomGradient19elementGradientStopEv',
    )
    from . import DomGradientStop
    return QList[DomGradientStop]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setAttributeStartX(self, a: float) -> None:
    """
    Calls Qt's 'void DomGradient::setAttributeStartX(double a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domgradient.html#setAttributeStartX

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void DomGradient::setAttributeStartX(double a)
    self.uglySide.call('ritual_ZN11DomGradient18setAttributeStartXEd', a)

  @overload(float)
  def setAttributeStartY(self, a: float) -> None:
    """
    Calls Qt's 'void DomGradient::setAttributeStartY(double a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domgradient.html#setAttributeStartY

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void DomGradient::setAttributeStartY(double a)
    self.uglySide.call('ritual_ZN11DomGradient18setAttributeStartYEd', a)

  @overload(float)
  def setAttributeEndX(self, a: float) -> None:
    """
    Calls Qt's 'void DomGradient::setAttributeEndX(double a)'.

    Qt's own words: https://doc.qt.io/qt-6/domgradient.html#setAttributeEndX

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void DomGradient::setAttributeEndX(double a)
    self.uglySide.call('ritual_ZN11DomGradient16setAttributeEndXEd', a)

  @overload(float)
  def setAttributeEndY(self, a: float) -> None:
    """
    Calls Qt's 'void DomGradient::setAttributeEndY(double a)'.

    Qt's own words: https://doc.qt.io/qt-6/domgradient.html#setAttributeEndY

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void DomGradient::setAttributeEndY(double a)
    self.uglySide.call('ritual_ZN11DomGradient16setAttributeEndYEd', a)

  @overload(float)
  def setAttributeCentralX(self, a: float) -> None:
    """
    Calls Qt's 'void DomGradient::setAttributeCentralX(double a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domgradient.html#setAttributeCentralX

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void DomGradient::setAttributeCentralX(double a)
    self.uglySide.call('ritual_ZN11DomGradient20setAttributeCentralXEd', a)

  @overload(float)
  def setAttributeCentralY(self, a: float) -> None:
    """
    Calls Qt's 'void DomGradient::setAttributeCentralY(double a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domgradient.html#setAttributeCentralY

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void DomGradient::setAttributeCentralY(double a)
    self.uglySide.call('ritual_ZN11DomGradient20setAttributeCentralYEd', a)

  @overload(float)
  def setAttributeFocalX(self, a: float) -> None:
    """
    Calls Qt's 'void DomGradient::setAttributeFocalX(double a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domgradient.html#setAttributeFocalX

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void DomGradient::setAttributeFocalX(double a)
    self.uglySide.call('ritual_ZN11DomGradient18setAttributeFocalXEd', a)

  @overload(float)
  def setAttributeFocalY(self, a: float) -> None:
    """
    Calls Qt's 'void DomGradient::setAttributeFocalY(double a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domgradient.html#setAttributeFocalY

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void DomGradient::setAttributeFocalY(double a)
    self.uglySide.call('ritual_ZN11DomGradient18setAttributeFocalYEd', a)

  @overload(float)
  def setAttributeRadius(self, a: float) -> None:
    """
    Calls Qt's 'void DomGradient::setAttributeRadius(double a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domgradient.html#setAttributeRadius

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void DomGradient::setAttributeRadius(double a)
    self.uglySide.call('ritual_ZN11DomGradient18setAttributeRadiusEd', a)

  @overload(float)
  def setAttributeAngle(self, a: float) -> None:
    """
    Calls Qt's 'void DomGradient::setAttributeAngle(double a)'.

    Qt's own words: https://doc.qt.io/qt-6/domgradient.html#setAttributeAngle

    Parameters
    ----------

    a : float
      Passed on as it is.
    """
    #  void DomGradient::setAttributeAngle(double a)
    self.uglySide.call('ritual_ZN11DomGradient17setAttributeAngleEd', a)

  @overload(str)
  def setAttributeType(self, a: str) -> None:
    """
    Calls Qt's 'void DomGradient::setAttributeType(const QString &a)'.

    Qt's own words: https://doc.qt.io/qt-6/domgradient.html#setAttributeType

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomGradient::setAttributeType(const QString &a)
    self.uglySide.call(
        'ritual_ZN11DomGradient16setAttributeTypeERK7QString', a,
    )

  @overload(str)
  def setAttributeSpread(self, a: str) -> None:
    """
    Calls Qt's 'void DomGradient::setAttributeSpread(const QString &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domgradient.html#setAttributeSpread

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomGradient::setAttributeSpread(const QString &a)
    self.uglySide.call(
        'ritual_ZN11DomGradient18setAttributeSpreadERK7QString', a,
    )

  @overload(str)
  def setAttributeCoordinateMode(self, a: str) -> None:
    """
    Calls Qt's 'void DomGradient::setAttributeCoordinateMode(const QString
    &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domgradient.html#setAttributeCoordinateMode

    Parameters
    ----------

    a : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void DomGradient::setAttributeCoordinateMode(const QString &a)
    self.uglySide.call(
        'ritual_ZN11DomGradient26setAttributeCoordinateModeERK7QString', a,
    )

  @overload(QList[DomGradientStop])
  def setElementGradientStop(self, a: QList[DomGradientStop]) -> None:
    """
    Calls Qt's 'void DomGradient::setElementGradientStop(const
    QList<DomGradientStop *> &a)'.

    Qt's own words:
    https://doc.qt.io/qt-6/domgradient.html#setElementGradientStop

    Parameters
    ----------

    a : QList[DomGradientStop]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void DomGradient::setElementGradientStop(const QList<DomGradientStop
    #      *> &a)
    self.uglySide.call(
        'ritual_ZN11DomGradient22setElementGradientStopERK5QListIP15DomGrad'
        'ientStopE',
        self._valueOf(a),
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
    Notes what was given, for Qt's 'DomGradient::DomGradient()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/domgradient.html#DomGradient
    """
    #  DomGradient::DomGradient()
    self._noteCreation(DomGradient, lambda: Rituals.call(
        'ritual_ZN11DomGradientC1Ev',
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

  def clearAttributeStartX(self) -> None:
    """
    Calls Qt's 'void DomGradient::clearAttributeStartX()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domgradient.html#clearAttributeStartX
    """
    #  void DomGradient::clearAttributeStartX()
    self.uglySide.call('ritual_ZN11DomGradient20clearAttributeStartXEv')

  def clearAttributeStartY(self) -> None:
    """
    Calls Qt's 'void DomGradient::clearAttributeStartY()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domgradient.html#clearAttributeStartY
    """
    #  void DomGradient::clearAttributeStartY()
    self.uglySide.call('ritual_ZN11DomGradient20clearAttributeStartYEv')

  def clearAttributeEndX(self) -> None:
    """
    Calls Qt's 'void DomGradient::clearAttributeEndX()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domgradient.html#clearAttributeEndX
    """
    #  void DomGradient::clearAttributeEndX()
    self.uglySide.call('ritual_ZN11DomGradient18clearAttributeEndXEv')

  def clearAttributeEndY(self) -> None:
    """
    Calls Qt's 'void DomGradient::clearAttributeEndY()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domgradient.html#clearAttributeEndY
    """
    #  void DomGradient::clearAttributeEndY()
    self.uglySide.call('ritual_ZN11DomGradient18clearAttributeEndYEv')

  def clearAttributeCentralX(self) -> None:
    """
    Calls Qt's 'void DomGradient::clearAttributeCentralX()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domgradient.html#clearAttributeCentralX
    """
    #  void DomGradient::clearAttributeCentralX()
    self.uglySide.call('ritual_ZN11DomGradient22clearAttributeCentralXEv')

  def clearAttributeCentralY(self) -> None:
    """
    Calls Qt's 'void DomGradient::clearAttributeCentralY()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domgradient.html#clearAttributeCentralY
    """
    #  void DomGradient::clearAttributeCentralY()
    self.uglySide.call('ritual_ZN11DomGradient22clearAttributeCentralYEv')

  def clearAttributeFocalX(self) -> None:
    """
    Calls Qt's 'void DomGradient::clearAttributeFocalX()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domgradient.html#clearAttributeFocalX
    """
    #  void DomGradient::clearAttributeFocalX()
    self.uglySide.call('ritual_ZN11DomGradient20clearAttributeFocalXEv')

  def clearAttributeFocalY(self) -> None:
    """
    Calls Qt's 'void DomGradient::clearAttributeFocalY()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domgradient.html#clearAttributeFocalY
    """
    #  void DomGradient::clearAttributeFocalY()
    self.uglySide.call('ritual_ZN11DomGradient20clearAttributeFocalYEv')

  def clearAttributeRadius(self) -> None:
    """
    Calls Qt's 'void DomGradient::clearAttributeRadius()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domgradient.html#clearAttributeRadius
    """
    #  void DomGradient::clearAttributeRadius()
    self.uglySide.call('ritual_ZN11DomGradient20clearAttributeRadiusEv')

  def clearAttributeAngle(self) -> None:
    """
    Calls Qt's 'void DomGradient::clearAttributeAngle()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domgradient.html#clearAttributeAngle
    """
    #  void DomGradient::clearAttributeAngle()
    self.uglySide.call('ritual_ZN11DomGradient19clearAttributeAngleEv')

  def clearAttributeType(self) -> None:
    """
    Calls Qt's 'void DomGradient::clearAttributeType()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domgradient.html#clearAttributeType
    """
    #  void DomGradient::clearAttributeType()
    self.uglySide.call('ritual_ZN11DomGradient18clearAttributeTypeEv')

  def clearAttributeSpread(self) -> None:
    """
    Calls Qt's 'void DomGradient::clearAttributeSpread()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domgradient.html#clearAttributeSpread
    """
    #  void DomGradient::clearAttributeSpread()
    self.uglySide.call('ritual_ZN11DomGradient20clearAttributeSpreadEv')

  def clearAttributeCoordinateMode(self) -> None:
    """
    Calls Qt's 'void DomGradient::clearAttributeCoordinateMode()'.

    Qt's own words:
    https://doc.qt.io/qt-6/domgradient.html#clearAttributeCoordinateMode
    """
    #  void DomGradient::clearAttributeCoordinateMode()
    self.uglySide.call(
        'ritual_ZN11DomGradient28clearAttributeCoordinateModeEv',
    )

  @staticmethod
  def read(*__, **_) -> Never:
    """
    Qt's 'void DomGradient::read(QXmlStreamReader &reader)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomGradient.read' has no cute function yet. Qt's 'void "
        "DomGradient::read(QXmlStreamReader &reader)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    Qt's 'void DomGradient::write(QXmlStreamWriter &writer, const QString
    &tagName) const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'DomGradient.write' has no cute function yet. Qt's 'void "
        "DomGradient::write(QXmlStreamWriter &writer, const QString "
        "&tagName) const': takes a type Python has no way to hand over yet.")
