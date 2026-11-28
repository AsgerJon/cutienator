"""
QOpcUaEnumField binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuaenumfield.h, Qt 6.12.0. Changes made here are lost.
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


class QOpcUaEnumField(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaEnumField: a plain Python object standing in
  front of one C++ QOpcUaEnumField.

  C++ hands a QOpcUaEnumField around as a copy, so every C++ QOpcUaEnumField
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpcUaEnumField that has a ritual and that Python
  can call so far, 10 names in all: 'value', 'setValue', 'displayName',
  'setDisplayName', 'description', 'setDescription', 'name', 'setName',
  '__eq__', '__ne__'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QOpcUaEnumField::swap(QOpcUaEnumField &other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QOpcUaEnumField &QOpcUaEnumField::operator=(QOpcUaEnumField
    &&other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QOpcUaEnumField::QOpcUaEnumField(QOpcUaEnumField &&other)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QOpcUaEnumField &QOpcUaEnumField::operator=(const QOpcUaEnumField
    &rhs)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QVariant QOpcUaEnumField::operator QVariant() const': an operator
    Python has no name for.
  - Qt's 'QOpcUaEnumField::~QOpcUaEnumField()': the destructor: Python
    removes its C++ QOpcUaEnumField by it, and has no other use for it.

  What to expect
  --------------

  - The C++ QOpcUaEnumField is created at the first use, not by
    'QOpcUaEnumField(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaEnumField back gives a copy the ritual made for
    Python, in a new cute QOpcUaEnumField.
  - Each name of Qt's QOpcUaEnumField that has no cute function yet, 'swap',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOpcUaEnumField'

  #  Qt's '~QOpcUaEnumField()'. Naming it makes this a value class: Python
  #  owns every C++ QOpcUaEnumField behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QOpcUaEnumFieldD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def value(self) -> int:
    """
    Calls Qt's 'qint64 QOpcUaEnumField::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaenumfield.html#value
    """
    #  qint64 QOpcUaEnumField::value() const
    return self.uglySide.call('ritual_ZNK15QOpcUaEnumField5valueEv')

  def displayName(self) -> QOpcUaLocalizedText:
    """
    Calls Qt's 'QOpcUaLocalizedText QOpcUaEnumField::displayName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaenumfield.html#displayName

    Returns
    -------

    QOpcUaLocalizedText
      A new cute QOpcUaLocalizedText around the copy Qt gave back. Python
      owns it.
    """
    #  QOpcUaLocalizedText QOpcUaEnumField::displayName() const
    address = self.uglySide.call(
        'ritual_ZNK15QOpcUaEnumField11displayNameEv',
    )
    from . import QOpcUaLocalizedText
    return QOpcUaLocalizedText._cuteOwning(address)

  def description(self) -> QOpcUaLocalizedText:
    """
    Calls Qt's 'QOpcUaLocalizedText QOpcUaEnumField::description() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaenumfield.html#description

    Returns
    -------

    QOpcUaLocalizedText
      A new cute QOpcUaLocalizedText around the copy Qt gave back. Python
      owns it.
    """
    #  QOpcUaLocalizedText QOpcUaEnumField::description() const
    address = self.uglySide.call(
        'ritual_ZNK15QOpcUaEnumField11descriptionEv',
    )
    from . import QOpcUaLocalizedText
    return QOpcUaLocalizedText._cuteOwning(address)

  def name(self) -> str:
    """
    Calls Qt's 'QString QOpcUaEnumField::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaenumfield.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QOpcUaEnumField::name() const
    return self.uglySide.call('ritual_ZNK15QOpcUaEnumField4nameEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setValue(self, value: int) -> None:
    """
    Calls Qt's 'void QOpcUaEnumField::setValue(qint64 value)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaenumfield.html#setValue

    Parameters
    ----------

    value : int
      Passed on as it is.
    """
    #  void QOpcUaEnumField::setValue(qint64 value)
    self.uglySide.call('ritual_ZN15QOpcUaEnumField8setValueEx', value)

  @overload(QOpcUaLocalizedText)
  def setDisplayName(self, displayName: QOpcUaLocalizedText) -> None:
    """
    Calls Qt's 'void QOpcUaEnumField::setDisplayName(const
    QOpcUaLocalizedText &displayName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaenumfield.html#setDisplayName

    Parameters
    ----------

    displayName : QOpcUaLocalizedText
      Passed on as a value: Qt reads the C++ QOpcUaLocalizedText, which stays
      Python's own.
    """
    #  void QOpcUaEnumField::setDisplayName(const QOpcUaLocalizedText
    #      &displayName)
    self.uglySide.call(
        'ritual_ZN15QOpcUaEnumField14setDisplayNameERK19QOpcUaLocalizedText',
        self._valueOf(displayName),
    )

  @overload(QOpcUaLocalizedText)
  def setDescription(self, description: QOpcUaLocalizedText) -> None:
    """
    Calls Qt's 'void QOpcUaEnumField::setDescription(const
    QOpcUaLocalizedText &description)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaenumfield.html#setDescription

    Parameters
    ----------

    description : QOpcUaLocalizedText
      Passed on as a value: Qt reads the C++ QOpcUaLocalizedText, which stays
      Python's own.
    """
    #  void QOpcUaEnumField::setDescription(const QOpcUaLocalizedText
    #      &description)
    self.uglySide.call(
        'ritual_ZN15QOpcUaEnumField14setDescriptionERK19QOpcUaLocalizedText',
        self._valueOf(description),
    )

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void QOpcUaEnumField::setName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaenumfield.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QOpcUaEnumField::setName(const QString &name)
    self.uglySide.call('ritual_ZN15QOpcUaEnumField7setNameERK7QString', name)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QOpcUaEnumField) -> bool:
    """
    Calls Qt's 'bool operator==(const QOpcUaEnumField &lhs, const
    QOpcUaEnumField &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaenumfield.html#operator==

    Parameters
    ----------

    rhs : QOpcUaEnumField
      Passed on as a value: Qt reads the C++ QOpcUaEnumField, which stays
      Python's own.
    """
    #  bool operator==(const QOpcUaEnumField &lhs, const QOpcUaEnumField
    #      &rhs)
    return Rituals.call(
        'ritual_ZeqRK15QOpcUaEnumFieldS1_',
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
  def __ne__(self, rhs: QOpcUaEnumField) -> bool:
    """
    Calls Qt's 'bool operator!=(const QOpcUaEnumField &lhs, const
    QOpcUaEnumField &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaenumfield.html#operator!=

    Parameters
    ----------

    rhs : QOpcUaEnumField
      Passed on as a value: Qt reads the C++ QOpcUaEnumField, which stays
      Python's own.
    """
    #  bool operator!=(const QOpcUaEnumField &lhs, const QOpcUaEnumField
    #      &rhs)
    return Rituals.call(
        'ritual_ZneRK15QOpcUaEnumFieldS1_',
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QOpcUaEnumField::QOpcUaEnumField()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaenumfield.html#QOpcUaEnumField
    """
    #  QOpcUaEnumField::QOpcUaEnumField()
    self._noteCreation(QOpcUaEnumField, lambda: Rituals.call(
        'ritual_ZN15QOpcUaEnumFieldC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QOpcUaEnumField) -> None:
    """
    Notes what was given, for Qt's 'QOpcUaEnumField::QOpcUaEnumField(const
    QOpcUaEnumField &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaenumfield.html#QOpcUaEnumField

    Parameters
    ----------

    other : QOpcUaEnumField
      Passed on as a value: Qt reads the C++ QOpcUaEnumField, which stays
      Python's own.
    """
    #  QOpcUaEnumField::QOpcUaEnumField(const QOpcUaEnumField &other)
    self._noteCreation(QOpcUaEnumField, lambda: Rituals.call(
        'ritual_ZN15QOpcUaEnumFieldC1ERKS_', self._valueOf(other),
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
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QOpcUaEnumField::swap(QOpcUaEnumField &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOpcUaEnumField.swap' has no cute function yet. Qt's 'void "
        "QOpcUaEnumField::swap(QOpcUaEnumField &other)': takes a type "
        "Python has no way to hand over yet.")


#  Qt's 'QList<QOpcUaEnumField>': the list of QOpcUaEnumField, which
#  'QList[QOpcUaEnumField]' gives. It is made here, so that there is one as
#  soon as there can be a QOpcUaEnumField.
QList.createKind(
    QOpcUaEnumField, 'value',
    make='ritual_list_make_QOpcUaEnumField',
    add='ritual_list_add_QOpcUaEnumField',
    size='ritual_list_size_QOpcUaEnumField',
    at='ritual_list_at_QOpcUaEnumField',
    drop='ritual_list_drop_QOpcUaEnumField',
)
