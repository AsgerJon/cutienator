"""
QOpcUaEnumDefinition binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtOpcUa/qopcuaenumdefinition.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QOpcUaEnumField
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QOpcUaEnumField = WAIT['QOpcUaEnumField']


class QOpcUaEnumDefinition(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QOpcUaEnumDefinition: a plain Python object standing
  in front of one C++ QOpcUaEnumDefinition.

  C++ hands a QOpcUaEnumDefinition around as a copy, so every C++
  QOpcUaEnumDefinition behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOpcUaEnumDefinition that has a ritual and that
  Python can call so far, 4 names in all: 'fields', 'setFields', '__eq__',
  '__ne__'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void QOpcUaEnumDefinition::swap(QOpcUaEnumDefinition &other)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QOpcUaEnumDefinition
    &QOpcUaEnumDefinition::operator=(QOpcUaEnumDefinition &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QOpcUaEnumDefinition::QOpcUaEnumDefinition(QOpcUaEnumDefinition
    &&other)': takes a type Python has no way to hand over yet.
  - Qt's 'QOpcUaEnumDefinition &QOpcUaEnumDefinition::operator=(const
    QOpcUaEnumDefinition &rhs)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QVariant QOpcUaEnumDefinition::operator QVariant() const': an
    operator Python has no name for.
  - Qt's 'QOpcUaEnumDefinition::~QOpcUaEnumDefinition()': the destructor:
    Python removes its C++ QOpcUaEnumDefinition by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ QOpcUaEnumDefinition is created at the first use, not by
    'QOpcUaEnumDefinition(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOpcUaEnumDefinition back gives a copy the ritual
    made for Python, in a new cute QOpcUaEnumDefinition.
  - Each name of Qt's QOpcUaEnumDefinition that has no cute function yet,
    'swap', holds a function that raises 'NotImplementedError', and its
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
  __qt_class__ = 'QOpcUaEnumDefinition'

  #  Qt's '~QOpcUaEnumDefinition()'. Naming it makes this a value class:
  #  Python owns every C++ QOpcUaEnumDefinition behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN20QOpcUaEnumDefinitionD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def fields(self) -> QList[QOpcUaEnumField]:
    """
    Calls Qt's 'QList<QOpcUaEnumField> QOpcUaEnumDefinition::fields() const'.

    Qt's own words: https://doc.qt.io/qt-6/qopcuaenumdefinition.html#fields

    Returns
    -------

    QList[QOpcUaEnumField]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QOpcUaEnumField> QOpcUaEnumDefinition::fields() const
    address = self.uglySide.call('ritual_ZNK20QOpcUaEnumDefinition6fieldsEv')
    from . import QOpcUaEnumField
    return QList[QOpcUaEnumField]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QList[QOpcUaEnumField])
  def setFields(self, fields: QList[QOpcUaEnumField]) -> None:
    """
    Calls Qt's 'void QOpcUaEnumDefinition::setFields(const
    QList<QOpcUaEnumField> &fields)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaenumdefinition.html#setFields

    Parameters
    ----------

    fields : QList[QOpcUaEnumField]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QOpcUaEnumDefinition::setFields(const QList<QOpcUaEnumField>
    #      &fields)
    self.uglySide.call(
        'ritual_ZN20QOpcUaEnumDefinition9setFieldsERK5QListI15QOpcUaEnumFie'
        'ldE',
        self._valueOf(fields),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QOpcUaEnumDefinition) -> bool:
    """
    Calls Qt's 'bool operator==(const QOpcUaEnumDefinition &lhs, const
    QOpcUaEnumDefinition &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaenumdefinition.html#operator==

    Parameters
    ----------

    rhs : QOpcUaEnumDefinition
      Passed on as a value: Qt reads the C++ QOpcUaEnumDefinition, which
      stays Python's own.
    """
    #  bool operator==(const QOpcUaEnumDefinition &lhs, const
    #      QOpcUaEnumDefinition &rhs)
    return Rituals.call(
        'ritual_ZeqRK20QOpcUaEnumDefinitionS1_',
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
  def __ne__(self, rhs: QOpcUaEnumDefinition) -> bool:
    """
    Calls Qt's 'bool operator!=(const QOpcUaEnumDefinition &lhs, const
    QOpcUaEnumDefinition &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaenumdefinition.html#operator!=

    Parameters
    ----------

    rhs : QOpcUaEnumDefinition
      Passed on as a value: Qt reads the C++ QOpcUaEnumDefinition, which
      stays Python's own.
    """
    #  bool operator!=(const QOpcUaEnumDefinition &lhs, const
    #      QOpcUaEnumDefinition &rhs)
    return Rituals.call(
        'ritual_ZneRK20QOpcUaEnumDefinitionS1_',
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
    Notes what was given, for Qt's
    'QOpcUaEnumDefinition::QOpcUaEnumDefinition()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaenumdefinition.html#QOpcUaEnumDefinition
    """
    #  QOpcUaEnumDefinition::QOpcUaEnumDefinition()
    self._noteCreation(QOpcUaEnumDefinition, lambda: Rituals.call(
        'ritual_ZN20QOpcUaEnumDefinitionC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QOpcUaEnumDefinition) -> None:
    """
    Notes what was given, for Qt's
    'QOpcUaEnumDefinition::QOpcUaEnumDefinition(const QOpcUaEnumDefinition
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qopcuaenumdefinition.html#QOpcUaEnumDefinition

    Parameters
    ----------

    other : QOpcUaEnumDefinition
      Passed on as a value: Qt reads the C++ QOpcUaEnumDefinition, which
      stays Python's own.
    """
    #  QOpcUaEnumDefinition::QOpcUaEnumDefinition(const QOpcUaEnumDefinition
    #      &other)
    self._noteCreation(QOpcUaEnumDefinition, lambda: Rituals.call(
        'ritual_ZN20QOpcUaEnumDefinitionC1ERKS_', self._valueOf(other),
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
    Qt's 'void QOpcUaEnumDefinition::swap(QOpcUaEnumDefinition &other)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QOpcUaEnumDefinition.swap' has no cute function yet. Qt's 'void "
        "QOpcUaEnumDefinition::swap(QOpcUaEnumDefinition &other)': takes a "
        "type Python has no way to hand over yet.")
