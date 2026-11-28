"""
qdesigner_internal::PropertySheetKeySequenceValue binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_utils_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::PropertySheetKeySequenceValue to be private:
#  it declares the class in a header it calls private. cutienator does not
#  care. Qt hands objects of the class out all the same, and a class we are
#  handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..occult import Rituals
from ..QtGui import QKeySequence
from . import qdesigner_internal

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional


class PropertySheetKeySequenceValue(qdesigner_internal.PropertySheetTranslatableData):
  """
  The cute side of Qt's qdesigner_internal::PropertySheetKeySequenceValue: a
  plain Python object standing in front of one C++
  qdesigner_internal::PropertySheetKeySequenceValue.

  It is built on the cute
  'qdesigner_internal::PropertySheetTranslatableData', as Qt's
  qdesigner_internal::PropertySheetKeySequenceValue is built on Qt's
  qdesigner_internal::PropertySheetTranslatableData, and has everything that
  class has.

  C++ hands a qdesigner_internal::PropertySheetKeySequenceValue around as a
  copy, so every C++ qdesigner_internal::PropertySheetKeySequenceValue behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::PropertySheetKeySequenceValue
  that has a ritual and that Python can call so far, 6 names in all: 'value',
  'setValue', 'standardKey', 'isStandardKey', '__eq__', '__ne__'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'qdesigner_internal::PropertySheetKeySequenceValue::
    PropertySheetKeySequenceValue(const QKeySequence::StandardKey
    &standardKey, bool translatable, const QString &disambiguation, const
    QString &comment)': takes a type Python has no way to hand over yet.
  - Qt's 'void
    qdesigner_internal::PropertySheetKeySequenceValue::setStandardKey(const
    QKeySequence::StandardKey &standardKey)': takes a type Python has no way
    to hand over yet.
  - Qt's 'qdesigner_internal::PropertySheetKeySequenceValue::
    ~PropertySheetKeySequenceValue()': the destructor: Python removes its C++
    qdesigner_internal::PropertySheetKeySequenceValue by it, and has no other
    use for it.

  What to expect
  --------------

  - The C++ qdesigner_internal::PropertySheetKeySequenceValue is created at
    the first use, not by
    'qdesigner_internal::PropertySheetKeySequenceValue(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a qdesigner_internal::PropertySheetKeySequenceValue
    back gives a copy the ritual made for Python, in a new cute
    qdesigner_internal::PropertySheetKeySequenceValue.
  - Each name of Qt's qdesigner_internal::PropertySheetKeySequenceValue that
    has no cute function yet, 'setStandardKey', holds a function that raises
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
  __qt_class__ = 'qdesigner_internal::PropertySheetKeySequenceValue'

  #  Qt's '~qdesigner_internal::PropertySheetKeySequenceValue()'. Naming it
  #  makes this a value class: Python owns every C++
  #  qdesigner_internal::PropertySheetKeySequenceValue behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN18qdesigner_internal29PropertySheetKeySequenceValueD1Ev')

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def value(self) -> QKeySequence:
    """
    Calls Qt's 'QKeySequence
    qdesigner_internal::PropertySheetKeySequenceValue::value() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheetkeysequencevalue.html

    Returns
    -------

    QKeySequence
      A new cute QKeySequence around the copy Qt gave back. Python owns it.
    """
    #  QKeySequence
    #      qdesigner_internal::PropertySheetKeySequenceValue::value() const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal29PropertySheetKeySequenceValue5valu'
        'eEv',
    )
    return QKeySequence._cuteOwning(address)

  def standardKey(self) -> QKeySequence.StandardKey:
    """
    Calls Qt's 'QKeySequence::StandardKey
    qdesigner_internal::PropertySheetKeySequenceValue::standardKey() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheetkeysequencevalue.html

    Returns
    -------

    QKeySequence.StandardKey
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QKeySequence.StandardKey(number)' gives.
    """
    #  QKeySequence::StandardKey
    #      qdesigner_internal::PropertySheetKeySequenceValue::standardKey()
    #      const
    return QKeySequence.StandardKey(self.uglySide.call(
        'ritual_ZNK18qdesigner_internal29PropertySheetKeySequenceValue11sta'
        'ndardKeyEv',
    ))

  def isStandardKey(self) -> bool:
    """
    Calls Qt's 'bool
    qdesigner_internal::PropertySheetKeySequenceValue::isStandardKey()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheetkeysequencevalue.html
    """
    #  bool
    #      qdesigner_internal::PropertySheetKeySequenceValue::isStandardKey()
    #      const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal29PropertySheetKeySequenceValue13isS'
        'tandardKeyEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QKeySequence)
  def setValue(self, value: QKeySequence) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::PropertySheetKeySequenceValue::setValue(const
    QKeySequence &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheetkeysequencevalue.html

    Parameters
    ----------

    value : QKeySequence
      Passed on as a value: Qt reads the C++ QKeySequence, which stays
      Python's own.
    """
    #  void qdesigner_internal::PropertySheetKeySequenceValue::setValue(const
    #      QKeySequence &value)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal29PropertySheetKeySequenceValue8setVa'
        'lueERK12QKeySequence',
        self._valueOf(value),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: PropertySheetKeySequenceValue) -> bool:
    """
    Calls Qt's 'bool operator==(const PropertySheetKeySequenceValue &lhs,
    const PropertySheetKeySequenceValue &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheetkeysequencevalue.html

    Parameters
    ----------

    rhs : PropertySheetKeySequenceValue
      Passed on as a value: Qt reads the C++
      qdesigner_internal::PropertySheetKeySequenceValue, which stays Python's
      own.
    """
    #  bool operator==(const PropertySheetKeySequenceValue &lhs, const
    #      PropertySheetKeySequenceValue &rhs)
    return Rituals.call(
        'ritual_ZN18qdesigner_internaleqERKNS_29PropertySheetKeySequenceVal'
        'ueES2_',
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
  def __ne__(self, rhs: PropertySheetKeySequenceValue) -> bool:
    """
    Calls Qt's 'bool operator!=(const PropertySheetKeySequenceValue &lhs,
    const PropertySheetKeySequenceValue &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheetkeysequencevalue.html

    Parameters
    ----------

    rhs : PropertySheetKeySequenceValue
      Passed on as a value: Qt reads the C++
      qdesigner_internal::PropertySheetKeySequenceValue, which stays Python's
      own.
    """
    #  bool operator!=(const PropertySheetKeySequenceValue &lhs, const
    #      PropertySheetKeySequenceValue &rhs)
    return Rituals.call(
        'ritual_ZN18qdesigner_internalneERKNS_29PropertySheetKeySequenceVal'
        'ueES2_',
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
  @overload(QKeySequence)
  @overload(QKeySequence, bool)
  @overload(QKeySequence, bool, str)
  @overload(QKeySequence, bool, str, str)
  def __init__(
      self,
      value: Optional[QKeySequence] = None,
      translatable: bool = True,
      disambiguation: str = '',
      comment: str = '',
  ) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::PropertySheetKeySequenceValue::
    PropertySheetKeySequenceValue(const QKeySequence &value, bool
    translatable, const QString &disambiguation, const QString &comment)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheetkeysequencevalue.html

    Parameters
    ----------

    value : Optional[QKeySequence]
      Passed on as a value: Qt reads the C++ QKeySequence, which stays
      Python's own. May be left out, as in Qt: a new 'QKeySequence()' is then
      passed on.

    translatable : bool
      Passed on as it is. May be left out, as in Qt: it is then True.

    disambiguation : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    comment : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  qdesigner_internal::PropertySheetKeySequenceValue::
    #      PropertySheetKeySequenceValue(const QKeySequence &value, bool
    #      translatable, const QString &disambiguation, const QString
    #      &comment)
    if value is None:
      value = QKeySequence()
    self._noteCreation(PropertySheetKeySequenceValue, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal29PropertySheetKeySequenceValueC1ERK1'
        '2QKeySequencebRK7QStringS6_',
        self._valueOf(value), translatable, disambiguation, comment,
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
  def setStandardKey(*__, **_) -> Never:
    """
    Qt's 'void
    qdesigner_internal::PropertySheetKeySequenceValue::setStandardKey(const
    QKeySequence::StandardKey &standardKey)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'qdesigner_internal.PropertySheetKeySequenceValue.setStandardKey' "
        "has no cute function yet. Qt's 'void "
        "qdesigner_internal::PropertySheetKeySequenceValue::setStandardKey(c"
        "onst QKeySequence::StandardKey &standardKey)': takes a type Python "
        "has no way to hand over yet.")
