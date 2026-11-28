"""
QOpcUaArgument binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuaargument.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QOpcUaLocalizedText
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpcUaLocalizedText = WAIT['QOpcUaLocalizedText']


class QOpcUaArgument(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaArgument: a plain Python object standing in
  front of one C++ QOpcUaArgument.

  C++ hands a QOpcUaArgument around as a copy, so every C++ QOpcUaArgument
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpcUaArgument that has a ritual and that Python can
  call so far, 9 names in all: '__eq__', 'name', 'setName', 'dataTypeId',
  'setDataTypeId', 'valueRank', 'setValueRank', 'description',
  'setDescription'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOpcUaArgument::QOpcUaArgument(const QString &name, const QString
    &dataTypeId, qint32 valueRank, const QList<quint32> &arrayDimensions,
    const QOpcUaLocalizedText &description)': takes a type Python has no way
    to hand over yet.
  - Qt's 'QOpcUaArgument &QOpcUaArgument::operator=(const QOpcUaArgument
    &a0)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QVariant QOpcUaArgument::operator QVariant() const': an operator
    Python has no name for.
  - Qt's 'QOpcUaArgument::~QOpcUaArgument()': the destructor: Python removes
    its C++ QOpcUaArgument by it, and has no other use for it.
  - Qt's 'QList<quint32> QOpcUaArgument::arrayDimensions() const': gives a
    type Python has no way to take yet.
  - Qt's 'QList<quint32> &QOpcUaArgument::arrayDimensionsRef()': gives a type
    Python has no way to take yet.
  - Qt's 'void QOpcUaArgument::setArrayDimensions(const QList<quint32>
    &arrayDimensions)': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QOpcUaArgument is created at the first use, not by
    'QOpcUaArgument(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaArgument back gives a copy the ritual made for
    Python, in a new cute QOpcUaArgument.
  - Each name of Qt's QOpcUaArgument that has no cute function yet,
    'arrayDimensions', 'arrayDimensionsRef', 'setArrayDimensions', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaArgument'

  #  Qt's '~QOpcUaArgument()'. Naming it makes this a value class: Python
  #  owns every C++ QOpcUaArgument behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QOpcUaArgumentD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> str:
    """
    Calls Qt's 'QString QOpcUaArgument::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaargument.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaArgument::name() const
    return self.uglySide.call('ritual_ZNK14QOpcUaArgument4nameEv')

  def dataTypeId(self) -> str:
    """
    Calls Qt's 'QString QOpcUaArgument::dataTypeId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaargument.html#dataTypeId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaArgument::dataTypeId() const
    return self.uglySide.call('ritual_ZNK14QOpcUaArgument10dataTypeIdEv')

  def valueRank(self) -> int:
    """
    Calls Qt's 'qint32 QOpcUaArgument::valueRank() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaargument.html#valueRank
    """
    #  qint32 QOpcUaArgument::valueRank() const
    return self.uglySide.call('ritual_ZNK14QOpcUaArgument9valueRankEv')

  def description(self) -> QOpcUaLocalizedText:
    """
    Calls Qt's 'QOpcUaLocalizedText QOpcUaArgument::description() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaargument.html#description

    Returns
    -------

    QOpcUaLocalizedText
      A new cute QOpcUaLocalizedText around the copy Qt gave back. Python
      owns it.
    """
    #  QOpcUaLocalizedText QOpcUaArgument::description() const
    address = self.uglySide.call('ritual_ZNK14QOpcUaArgument11descriptionEv')
    from . import QOpcUaLocalizedText
    return QOpcUaLocalizedText._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void QOpcUaArgument::setName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaargument.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaArgument::setName(const QString &name)
    self.uglySide.call('ritual_ZN14QOpcUaArgument7setNameERK7QString', name)

  @overload(str)
  def setDataTypeId(self, dataTypeId: str) -> None:
    """
    Calls Qt's 'void QOpcUaArgument::setDataTypeId(const QString
    &dataTypeId)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaargument.html#setDataTypeId

    Parameters
    ----------

    dataTypeId : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaArgument::setDataTypeId(const QString &dataTypeId)
    self.uglySide.call(
        'ritual_ZN14QOpcUaArgument13setDataTypeIdERK7QString', dataTypeId,
    )

  @overload(int)
  def setValueRank(self, valueRank: int) -> None:
    """
    Calls Qt's 'void QOpcUaArgument::setValueRank(qint32 valueRank)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaargument.html#setValueRank

    Parameters
    ----------

    valueRank : int
      Passed on as it is.
    """
    #  void QOpcUaArgument::setValueRank(qint32 valueRank)
    self.uglySide.call(
        'ritual_ZN14QOpcUaArgument12setValueRankEi', valueRank,
    )

  @overload(QOpcUaLocalizedText)
  def setDescription(self, description: QOpcUaLocalizedText) -> None:
    """
    Calls Qt's 'void QOpcUaArgument::setDescription(const QOpcUaLocalizedText
    &description)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaargument.html#setDescription

    Parameters
    ----------

    description : QOpcUaLocalizedText
      Passed on as a value: Qt reads the C++ QOpcUaLocalizedText, which stays
      Python's own.
    """
    #  void QOpcUaArgument::setDescription(const QOpcUaLocalizedText
    #      &description)
    self.uglySide.call(
        'ritual_ZN14QOpcUaArgument14setDescriptionERK19QOpcUaLocalizedText',
        self._valueOf(description),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: QOpcUaArgument) -> bool:
    """
    Calls Qt's 'bool QOpcUaArgument::operator==(const QOpcUaArgument &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaargument.html#operator==

    Parameters
    ----------

    other : QOpcUaArgument
      Passed on as a value: Qt reads the C++ QOpcUaArgument, which stays
      Python's own.
    """
    #  bool QOpcUaArgument::operator==(const QOpcUaArgument &other) const
    return self.uglySide.call(
        'ritual_ZNK14QOpcUaArgumenteqERKS_', self._valueOf(other),
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
    Notes what was given, for Qt's 'QOpcUaArgument::QOpcUaArgument()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaargument.html#QOpcUaArgument
    """
    #  QOpcUaArgument::QOpcUaArgument()
    self._noteCreation(QOpcUaArgument, lambda: Rituals.call(
        'ritual_ZN14QOpcUaArgumentC1Ev',
    ))

  @overload(THIS)
  def __init__(self, rhs: QOpcUaArgument) -> None:
    """
    Notes what was given, for Qt's 'QOpcUaArgument::QOpcUaArgument(const
    QOpcUaArgument &rhs)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaargument.html#QOpcUaArgument

    Parameters
    ----------

    rhs : QOpcUaArgument
      Passed on as a value: Qt reads the C++ QOpcUaArgument, which stays
      Python's own.
    """
    #  QOpcUaArgument::QOpcUaArgument(const QOpcUaArgument &rhs)
    self._noteCreation(QOpcUaArgument, lambda: Rituals.call(
        'ritual_ZN14QOpcUaArgumentC1ERKS_', self._valueOf(rhs),
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
    Qt's 'QList<quint32> QOpcUaArgument::arrayDimensions() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QOpcUaArgument.arrayDimensions' has no cute function yet. Qt's "
        "'QList<quint32> QOpcUaArgument::arrayDimensions() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def arrayDimensionsRef(*__, **_) -> Never:
    """
    Qt's 'QList<quint32> &QOpcUaArgument::arrayDimensionsRef()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QOpcUaArgument.arrayDimensionsRef' has no cute function yet. Qt's "
        "'QList<quint32> &QOpcUaArgument::arrayDimensionsRef()': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def setArrayDimensions(*__, **_) -> Never:
    """
    Qt's 'void QOpcUaArgument::setArrayDimensions(const QList<quint32>
    &arrayDimensions)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOpcUaArgument.setArrayDimensions' has no cute function yet. Qt's "
        "'void QOpcUaArgument::setArrayDimensions(const QList<quint32> "
        "&arrayDimensions)': takes a type Python has no way to hand over "
        "yet.")
