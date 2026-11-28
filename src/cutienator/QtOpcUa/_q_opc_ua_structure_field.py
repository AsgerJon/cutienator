"""
QOpcUaStructureField binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuastructurefield.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QOpcUaLocalizedText
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpcUaLocalizedText = WAIT['QOpcUaLocalizedText']


class QOpcUaStructureField(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaStructureField: a plain Python object standing
  in front of one C++ QOpcUaStructureField.

  C++ hands a QOpcUaStructureField around as a copy, so every C++
  QOpcUaStructureField behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpcUaStructureField that has a ritual and that
  Python can call so far, 14 names in all: 'name', 'setName', 'description',
  'setDescription', 'dataType', 'setDataType', 'valueRank', 'setValueRank',
  'maxStringLength', 'setMaxStringLength', 'isOptional', 'setIsOptional',
  '__eq__', '__ne__'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QOpcUaStructureField::swap(QOpcUaStructureField &other)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QOpcUaStructureField
    &QOpcUaStructureField::operator=(QOpcUaStructureField &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QOpcUaStructureField::QOpcUaStructureField(QOpcUaStructureField
    &&other)': takes a type Python has no way to hand over yet.
  - Qt's 'QOpcUaStructureField &QOpcUaStructureField::operator=(const
    QOpcUaStructureField &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QVariant QOpcUaStructureField::operator QVariant() const': an
    operator Python has no name for.
  - Qt's 'QOpcUaStructureField::~QOpcUaStructureField()': the destructor:
    Python removes its C++ QOpcUaStructureField by it, and has no other use
    for it.
  - Qt's 'QList<quint32> QOpcUaStructureField::arrayDimensions() const':
    gives a type Python has no way to take yet.
  - Qt's 'void QOpcUaStructureField::setArrayDimensions(const QList<quint32>
    &arrayDimensions)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QOpcUaStructureField is created at the first use, not by
    'QOpcUaStructureField(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaStructureField back gives a copy the ritual
    made for Python, in a new cute QOpcUaStructureField.
  - Each name of Qt's QOpcUaStructureField that has no cute function yet,
    'arrayDimensions', 'setArrayDimensions', 'swap', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaStructureField'

  #  Qt's '~QOpcUaStructureField()'. Naming it makes this a value class:
  #  Python owns every C++ QOpcUaStructureField behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QOpcUaStructureFieldD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> str:
    """
    Calls Qt's 'QString QOpcUaStructureField::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuastructurefield.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaStructureField::name() const
    return self.uglySide.call('ritual_ZNK20QOpcUaStructureField4nameEv')

  def description(self) -> QOpcUaLocalizedText:
    """
    Calls Qt's 'QOpcUaLocalizedText QOpcUaStructureField::description()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuastructurefield.html#description

    Returns
    -------

    QOpcUaLocalizedText
      A new cute QOpcUaLocalizedText around the copy Qt gave back. Python
      owns it.
    """
    #  QOpcUaLocalizedText QOpcUaStructureField::description() const
    address = self.uglySide.call(
        'ritual_ZNK20QOpcUaStructureField11descriptionEv',
    )
    from . import QOpcUaLocalizedText
    return QOpcUaLocalizedText._cuteOwning(address)

  def dataType(self) -> str:
    """
    Calls Qt's 'QString QOpcUaStructureField::dataType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuastructurefield.html#dataType

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaStructureField::dataType() const
    return self.uglySide.call('ritual_ZNK20QOpcUaStructureField8dataTypeEv')

  def valueRank(self) -> int:
    """
    Calls Qt's 'qint32 QOpcUaStructureField::valueRank() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuastructurefield.html#valueRank
    """
    #  qint32 QOpcUaStructureField::valueRank() const
    return self.uglySide.call('ritual_ZNK20QOpcUaStructureField9valueRankEv')

  def maxStringLength(self) -> int:
    """
    Calls Qt's 'quint32 QOpcUaStructureField::maxStringLength() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuastructurefield.html#maxStringLength
    """
    #  quint32 QOpcUaStructureField::maxStringLength() const
    return self.uglySide.call(
        'ritual_ZNK20QOpcUaStructureField15maxStringLengthEv',
    )

  def isOptional(self) -> bool:
    """
    Calls Qt's 'bool QOpcUaStructureField::isOptional() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuastructurefield.html#isOptional
    """
    #  bool QOpcUaStructureField::isOptional() const
    return self.uglySide.call(
        'ritual_ZNK20QOpcUaStructureField10isOptionalEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void QOpcUaStructureField::setName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuastructurefield.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaStructureField::setName(const QString &name)
    self.uglySide.call(
        'ritual_ZN20QOpcUaStructureField7setNameERK7QString', name,
    )

  @overload(QOpcUaLocalizedText)
  def setDescription(self, description: QOpcUaLocalizedText) -> None:
    """
    Calls Qt's 'void QOpcUaStructureField::setDescription(const
    QOpcUaLocalizedText &description)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuastructurefield.html#setDescription

    Parameters
    ----------

    description : QOpcUaLocalizedText
      Passed on as a value: Qt reads the C++ QOpcUaLocalizedText, which stays
      Python's own.
    """
    #  void QOpcUaStructureField::setDescription(const QOpcUaLocalizedText
    #      &description)
    self.uglySide.call(
        'ritual_ZN20QOpcUaStructureField14setDescriptionERK19QOpcUaLocalize'
        'dText',
        self._valueOf(description),
    )

  @overload(str)
  def setDataType(self, dataTypeId: str) -> None:
    """
    Calls Qt's 'void QOpcUaStructureField::setDataType(const QString
    &dataTypeId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuastructurefield.html#setDataType

    Parameters
    ----------

    dataTypeId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaStructureField::setDataType(const QString &dataTypeId)
    self.uglySide.call(
        'ritual_ZN20QOpcUaStructureField11setDataTypeERK7QString',
        dataTypeId,
    )

  @overload(int)
  def setValueRank(self, valueRank: int) -> None:
    """
    Calls Qt's 'void QOpcUaStructureField::setValueRank(qint32 valueRank)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuastructurefield.html#setValueRank

    Parameters
    ----------

    valueRank : int
      Passed on as it is.
    """
    #  void QOpcUaStructureField::setValueRank(qint32 valueRank)
    self.uglySide.call(
        'ritual_ZN20QOpcUaStructureField12setValueRankEi', valueRank,
    )

  @overload(int)
  def setMaxStringLength(self, maxStringLength: int) -> None:
    """
    Calls Qt's 'void QOpcUaStructureField::setMaxStringLength(quint32
    maxStringLength)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuastructurefield.html#setMaxStringLength

    Parameters
    ----------

    maxStringLength : int
      Passed on as it is.
    """
    #  void QOpcUaStructureField::setMaxStringLength(quint32 maxStringLength)
    self.uglySide.call(
        'ritual_ZN20QOpcUaStructureField18setMaxStringLengthEj',
        maxStringLength,
    )

  @overload(bool)
  def setIsOptional(self, isOptional: bool) -> None:
    """
    Calls Qt's 'void QOpcUaStructureField::setIsOptional(bool isOptional)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuastructurefield.html#setIsOptional

    Parameters
    ----------

    isOptional : bool
      Passed on as it is.
    """
    #  void QOpcUaStructureField::setIsOptional(bool isOptional)
    self.uglySide.call(
        'ritual_ZN20QOpcUaStructureField13setIsOptionalEb', isOptional,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QOpcUaStructureField) -> bool:
    """
    Calls Qt's 'bool operator==(const QOpcUaStructureField &lhs, const
    QOpcUaStructureField &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuastructurefield.html#operator==

    Parameters
    ----------

    rhs : QOpcUaStructureField
      Passed on as a value: Qt reads the C++ QOpcUaStructureField, which
      stays Python's own.
    """
    #  bool operator==(const QOpcUaStructureField &lhs, const
    #      QOpcUaStructureField &rhs)
    return Rituals.call(
        'ritual_ZeqRK20QOpcUaStructureFieldS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: QOpcUaStructureField) -> bool:
    """
    Calls Qt's 'bool operator!=(const QOpcUaStructureField &lhs, const
    QOpcUaStructureField &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuastructurefield.html#operator!=

    Parameters
    ----------

    rhs : QOpcUaStructureField
      Passed on as a value: Qt reads the C++ QOpcUaStructureField, which
      stays Python's own.
    """
    #  bool operator!=(const QOpcUaStructureField &lhs, const
    #      QOpcUaStructureField &rhs)
    return Rituals.call(
        'ritual_ZneRK20QOpcUaStructureFieldS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
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
  @overload(int)
  def __init__(self, valueRank: int = -1) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaStructureField::QOpcUaStructureField(qint32 valueRank)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuastructurefield.html#QOpcUaStructureField

    Parameters
    ----------

    valueRank : int
      Passed on as it is. May be left out, as in Qt: it is then -1.
    """
    #  QOpcUaStructureField::QOpcUaStructureField(qint32 valueRank)
    self._noteCreation(QOpcUaStructureField, lambda: Rituals.call(
        'ritual_ZN20QOpcUaStructureFieldC1Ei', valueRank,
    ))

  @overload(THIS)
  def __init__(self, other: QOpcUaStructureField) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaStructureField::QOpcUaStructureField(const QOpcUaStructureField
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuastructurefield.html#QOpcUaStructureField

    Parameters
    ----------

    other : QOpcUaStructureField
      Passed on as a value: Qt reads the C++ QOpcUaStructureField, which
      stays Python's own.
    """
    #  QOpcUaStructureField::QOpcUaStructureField(const QOpcUaStructureField
    #      &other)
    self._noteCreation(QOpcUaStructureField, lambda: Rituals.call(
        'ritual_ZN20QOpcUaStructureFieldC1ERKS_', self._valueOf(other),
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
  def arrayDimensions(*__, **_) -> Never:
    """
    Qt's 'QList<quint32> QOpcUaStructureField::arrayDimensions() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QOpcUaStructureField.arrayDimensions' has no cute function yet. "
        "Qt's 'QList<quint32> QOpcUaStructureField::arrayDimensions() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def setArrayDimensions(*__, **_) -> Never:
    """
    Qt's 'void QOpcUaStructureField::setArrayDimensions(const QList<quint32>
    &arrayDimensions)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOpcUaStructureField.setArrayDimensions' has no cute function "
        "yet. Qt's 'void QOpcUaStructureField::setArrayDimensions(const "
        "QList<quint32> &arrayDimensions)': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QOpcUaStructureField::swap(QOpcUaStructureField &other)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOpcUaStructureField.swap' has no cute function yet. Qt's 'void "
        "QOpcUaStructureField::swap(QOpcUaStructureField &other)': takes a "
        "type Python has no way to hand over yet.")


#  Qt's 'QList<QOpcUaStructureField>': the list of QOpcUaStructureField,
#  which 'QList[QOpcUaStructureField]' gives. It is made here, so that there
#  is one as soon as there can be a QOpcUaStructureField.
QList.createKind(
    QOpcUaStructureField, 'value',
    make='ritual_list_make_QOpcUaStructureField',
    add='ritual_list_add_QOpcUaStructureField',
    size='ritual_list_size_QOpcUaStructureField',
    at='ritual_list_at_QOpcUaStructureField',
    drop='ritual_list_drop_QOpcUaStructureField',
)
