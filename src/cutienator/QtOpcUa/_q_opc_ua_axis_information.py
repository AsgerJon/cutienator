"""
QOpcUaAxisInformation binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuaaxisinformation.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from . import QOpcUa

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QOpcUaEUInformation, QOpcUaLocalizedText, QOpcUaRange
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpcUaEUInformation = WAIT['QOpcUaEUInformation']
  QOpcUaLocalizedText = WAIT['QOpcUaLocalizedText']
  QOpcUaRange = WAIT['QOpcUaRange']


class QOpcUaAxisInformation(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaAxisInformation: a plain Python object standing
  in front of one C++ QOpcUaAxisInformation.

  C++ hands a QOpcUaAxisInformation around as a copy, so every C++
  QOpcUaAxisInformation behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpcUaAxisInformation that has a ritual and that
  Python can call so far, 9 names in all: '__eq__', 'engineeringUnits',
  'setEngineeringUnits', 'eURange', 'setEURange', 'title', 'setTitle',
  'axisScaleType', 'setAxisScaleType'. It can be made from Python, in 2 ways;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaAxisInformation::QOpcUaAxisInformation(const
    QOpcUaEUInformation &engineeringUnits, const QOpcUaRange &eURange, const
    QOpcUaLocalizedText &title, const QOpcUa::AxisScale &axisScaleType, const
    QList<double> &axisSteps)': takes a type Python has no way to hand over
    yet.
  - Qt's 'QOpcUaAxisInformation &QOpcUaAxisInformation::operator=(const
    QOpcUaAxisInformation &a0)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QVariant QOpcUaAxisInformation::operator QVariant() const': an
    operator Python has no name for.
  - Qt's 'QOpcUaAxisInformation::~QOpcUaAxisInformation()': the destructor:
    Python removes its C++ QOpcUaAxisInformation by it, and has no other use
    for it.
  - Qt's 'QList<double> QOpcUaAxisInformation::axisSteps() const': gives a
    type Python has no way to take yet.
  - Qt's 'void QOpcUaAxisInformation::setAxisSteps(const QList<double>
    &axisSteps)': takes a type Python has no way to hand over yet.
  - Qt's 'QList<double> &QOpcUaAxisInformation::axisStepsRef()': gives a type
    Python has no way to take yet.

  What to expect
  --------------

  - The C++ QOpcUaAxisInformation is created at the first use, not by
    'QOpcUaAxisInformation(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaAxisInformation back gives a copy the ritual
    made for Python, in a new cute QOpcUaAxisInformation.
  - Each name of Qt's QOpcUaAxisInformation that has no cute function yet,
    'axisSteps', 'axisStepsRef', 'setAxisSteps', holds a function that raises
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
  __qt_class__ = 'QOpcUaAxisInformation'

  #  Qt's '~QOpcUaAxisInformation()'. Naming it makes this a value class:
  #  Python owns every C++ QOpcUaAxisInformation behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN21QOpcUaAxisInformationD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def engineeringUnits(self) -> QOpcUaEUInformation:
    """
    Calls Qt's 'QOpcUaEUInformation QOpcUaAxisInformation::engineeringUnits()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaaxisinformation.html#engineeringUnits

    Returns
    -------

    QOpcUaEUInformation
      A new cute QOpcUaEUInformation around the copy Qt gave back. Python
      owns it.
    """
    #  QOpcUaEUInformation QOpcUaAxisInformation::engineeringUnits() const
    address = self.uglySide.call(
        'ritual_ZNK21QOpcUaAxisInformation16engineeringUnitsEv',
    )
    from . import QOpcUaEUInformation
    return QOpcUaEUInformation._cuteOwning(address)

  def eURange(self) -> QOpcUaRange:
    """
    Calls Qt's 'QOpcUaRange QOpcUaAxisInformation::eURange() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaaxisinformation.html#eURange

    Returns
    -------

    QOpcUaRange
      A new cute QOpcUaRange around the copy Qt gave back. Python owns it.
    """
    #  QOpcUaRange QOpcUaAxisInformation::eURange() const
    address = self.uglySide.call(
        'ritual_ZNK21QOpcUaAxisInformation7eURangeEv',
    )
    from . import QOpcUaRange
    return QOpcUaRange._cuteOwning(address)

  def title(self) -> QOpcUaLocalizedText:
    """
    Calls Qt's 'QOpcUaLocalizedText QOpcUaAxisInformation::title() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaaxisinformation.html#title

    Returns
    -------

    QOpcUaLocalizedText
      A new cute QOpcUaLocalizedText around the copy Qt gave back. Python
      owns it.
    """
    #  QOpcUaLocalizedText QOpcUaAxisInformation::title() const
    address = self.uglySide.call('ritual_ZNK21QOpcUaAxisInformation5titleEv')
    from . import QOpcUaLocalizedText
    return QOpcUaLocalizedText._cuteOwning(address)

  def axisScaleType(self) -> QOpcUa.AxisScale:
    """
    Calls Qt's 'QOpcUa::AxisScale QOpcUaAxisInformation::axisScaleType()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaaxisinformation.html#axisScaleType

    Returns
    -------

    QOpcUa.AxisScale
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'QOpcUa.AxisScale(number)'
      gives.
    """
    #  QOpcUa::AxisScale QOpcUaAxisInformation::axisScaleType() const
    return QOpcUa.AxisScale(self.uglySide.call(
        'ritual_ZNK21QOpcUaAxisInformation13axisScaleTypeEv',
    ))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QOpcUaEUInformation)
  def setEngineeringUnits(
      self,
      engineeringUnits: QOpcUaEUInformation,
  ) -> None:
    """
    Calls Qt's 'void QOpcUaAxisInformation::setEngineeringUnits(const
    QOpcUaEUInformation &engineeringUnits)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaaxisinformation.html#setEngineeringUnits

    Parameters
    ----------

    engineeringUnits : QOpcUaEUInformation
      Passed on as a value: Qt reads the C++ QOpcUaEUInformation, which stays
      Python's own.
    """
    #  void QOpcUaAxisInformation::setEngineeringUnits(const
    #      QOpcUaEUInformation &engineeringUnits)
    self.uglySide.call(
        'ritual_ZN21QOpcUaAxisInformation19setEngineeringUnitsERK19QOpcUaEU'
        'Information',
        self._valueOf(engineeringUnits),
    )

  @overload(QOpcUaRange)
  def setEURange(self, eURange: QOpcUaRange) -> None:
    """
    Calls Qt's 'void QOpcUaAxisInformation::setEURange(const QOpcUaRange
    &eURange)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaaxisinformation.html#setEURange

    Parameters
    ----------

    eURange : QOpcUaRange
      Passed on as a value: Qt reads the C++ QOpcUaRange, which stays
      Python's own.
    """
    #  void QOpcUaAxisInformation::setEURange(const QOpcUaRange &eURange)
    self.uglySide.call(
        'ritual_ZN21QOpcUaAxisInformation10setEURangeERK11QOpcUaRange',
        self._valueOf(eURange),
    )

  @overload(QOpcUaLocalizedText)
  def setTitle(self, title: QOpcUaLocalizedText) -> None:
    """
    Calls Qt's 'void QOpcUaAxisInformation::setTitle(const
    QOpcUaLocalizedText &title)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaaxisinformation.html#setTitle

    Parameters
    ----------

    title : QOpcUaLocalizedText
      Passed on as a value: Qt reads the C++ QOpcUaLocalizedText, which stays
      Python's own.
    """
    #  void QOpcUaAxisInformation::setTitle(const QOpcUaLocalizedText &title)
    self.uglySide.call(
        'ritual_ZN21QOpcUaAxisInformation8setTitleERK19QOpcUaLocalizedText',
        self._valueOf(title),
    )

  @overload(QOpcUa.AxisScale)
  def setAxisScaleType(self, axisScaleType: QOpcUa.AxisScale) -> None:
    """
    Calls Qt's 'void
    QOpcUaAxisInformation::setAxisScaleType(QOpcUa::AxisScale
    axisScaleType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaaxisinformation.html#setAxisScaleType

    Parameters
    ----------

    axisScaleType : QOpcUa.AxisScale
      Passed on as its number.
    """
    #  void QOpcUaAxisInformation::setAxisScaleType(QOpcUa::AxisScale
    #      axisScaleType)
    self.uglySide.call(
        'ritual_ZN21QOpcUaAxisInformation16setAxisScaleTypeEN6QOpcUa9AxisSc'
        'aleE',
        axisScaleType.value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QOpcUaAxisInformation) -> bool:
    """
    Calls Qt's 'bool QOpcUaAxisInformation::operator==(const
    QOpcUaAxisInformation &rhs) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaaxisinformation.html#operator==

    Parameters
    ----------

    rhs : QOpcUaAxisInformation
      Passed on as a value: Qt reads the C++ QOpcUaAxisInformation, which
      stays Python's own.
    """
    #  bool QOpcUaAxisInformation::operator==(const QOpcUaAxisInformation
    #      &rhs) const
    return self.uglySide.call(
        'ritual_ZNK21QOpcUaAxisInformationeqERKS_', self._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaAxisInformation::QOpcUaAxisInformation()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaaxisinformation.html#QOpcUaAxisInformation
    """
    #  QOpcUaAxisInformation::QOpcUaAxisInformation()
    self._noteCreation(QOpcUaAxisInformation, lambda: Rituals.call(
        'ritual_ZN21QOpcUaAxisInformationC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: QOpcUaAxisInformation) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaAxisInformation::QOpcUaAxisInformation(const QOpcUaAxisInformation
    &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaaxisinformation.html#QOpcUaAxisInformation

    Parameters
    ----------

    a0 : QOpcUaAxisInformation
      Passed on as a value: Qt reads the C++ QOpcUaAxisInformation, which
      stays Python's own.
    """
    #  QOpcUaAxisInformation::QOpcUaAxisInformation(const
    #      QOpcUaAxisInformation &a0)
    self._noteCreation(QOpcUaAxisInformation, lambda: Rituals.call(
        'ritual_ZN21QOpcUaAxisInformationC1ERKS_', self._valueOf(a0),
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
  def axisSteps(*__, **_) -> Never:
    """
    Qt's 'QList<double> QOpcUaAxisInformation::axisSteps() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QOpcUaAxisInformation.axisSteps' has no cute function yet. Qt's "
        "'QList<double> QOpcUaAxisInformation::axisSteps() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def axisStepsRef(*__, **_) -> Never:
    """
    Qt's 'QList<double> &QOpcUaAxisInformation::axisStepsRef()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QOpcUaAxisInformation.axisStepsRef' has no cute function yet. "
        "Qt's 'QList<double> &QOpcUaAxisInformation::axisStepsRef()': gives "
        "a type Python has no way to take yet.")

  @staticmethod
  def setAxisSteps(*__, **_) -> Never:
    """
    Qt's 'void QOpcUaAxisInformation::setAxisSteps(const QList<double>
    &axisSteps)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOpcUaAxisInformation.setAxisSteps' has no cute function yet. "
        "Qt's 'void QOpcUaAxisInformation::setAxisSteps(const QList<double> "
        "&axisSteps)': takes a type Python has no way to hand over yet.")
