"""
qdesigner_internal::PropertySheetStringListValue binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_utils_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::PropertySheetStringListValue to be private:
#  it declares the class in a header it calls private. cutienator does not
#  care. Qt hands objects of the class out all the same, and a class we are
#  handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..occult import Rituals
from ..QtCore import QStringList
from . import qdesigner_internal


class PropertySheetStringListValue(qdesigner_internal.PropertySheetTranslatableData):
  """
  The cute side of Qt's qdesigner_internal::PropertySheetStringListValue: a
  plain Python object standing in front of one C++
  qdesigner_internal::PropertySheetStringListValue.

  It is built on the cute
  'qdesigner_internal::PropertySheetTranslatableData', as Qt's
  qdesigner_internal::PropertySheetStringListValue is built on Qt's
  qdesigner_internal::PropertySheetTranslatableData, and has everything that
  class has.

  C++ hands a qdesigner_internal::PropertySheetStringListValue around as a
  copy, so every C++ qdesigner_internal::PropertySheetStringListValue behind
  a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::PropertySheetStringListValue
  that has a ritual and that Python can call so far, 4 names in all: 'value',
  'setValue', '__eq__', '__ne__'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'qdesigner_internal::PropertySheetStringListValue::
    ~PropertySheetStringListValue()': the destructor: Python removes its C++
    qdesigner_internal::PropertySheetStringListValue by it, and has no other
    use for it.

  What to expect
  --------------

  - The C++ qdesigner_internal::PropertySheetStringListValue is created at
    the first use, not by
    'qdesigner_internal::PropertySheetStringListValue(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a qdesigner_internal::PropertySheetStringListValue back
    gives a copy the ritual made for Python, in a new cute
    qdesigner_internal::PropertySheetStringListValue.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::PropertySheetStringListValue'

  #  Qt's '~qdesigner_internal::PropertySheetStringListValue()'. Naming it
  #  makes this a value class: Python owns every C++
  #  qdesigner_internal::PropertySheetStringListValue behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN18qdesigner_internal28PropertySheetStringListValueD1Ev')

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def value(self) -> QStringList:
    """
    Calls Qt's 'QStringList
    qdesigner_internal::PropertySheetStringListValue::value() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheetstringlistvalue.html

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList qdesigner_internal::PropertySheetStringListValue::value()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18qdesigner_internal28PropertySheetStringListValue5value'
        'Ev',
    )
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QStringList)
  def setValue(self, value: QStringList) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::PropertySheetStringListValue::setValue(const
    QStringList &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheetstringlistvalue.html

    Parameters
    ----------

    value : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void qdesigner_internal::PropertySheetStringListValue::setValue(const
    #      QStringList &value)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal28PropertySheetStringListValue8setVal'
        'ueERK5QListI7QStringE',
        self._valueOf(value),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: PropertySheetStringListValue) -> bool:
    """
    Calls Qt's 'bool operator==(const PropertySheetStringListValue &lhs,
    const PropertySheetStringListValue &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheetstringlistvalue.html

    Parameters
    ----------

    rhs : PropertySheetStringListValue
      Passed on as a value: Qt reads the C++
      qdesigner_internal::PropertySheetStringListValue, which stays Python's
      own.
    """
    #  bool operator==(const PropertySheetStringListValue &lhs, const
    #      PropertySheetStringListValue &rhs)
    return Rituals.call(
        'ritual_ZN18qdesigner_internaleqERKNS_28PropertySheetStringListValu'
        'eES2_',
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
  def __ne__(self, rhs: PropertySheetStringListValue) -> bool:
    """
    Calls Qt's 'bool operator!=(const PropertySheetStringListValue &lhs,
    const PropertySheetStringListValue &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheetstringlistvalue.html

    Parameters
    ----------

    rhs : PropertySheetStringListValue
      Passed on as a value: Qt reads the C++
      qdesigner_internal::PropertySheetStringListValue, which stays Python's
      own.
    """
    #  bool operator!=(const PropertySheetStringListValue &lhs, const
    #      PropertySheetStringListValue &rhs)
    return Rituals.call(
        'ritual_ZN18qdesigner_internalneERKNS_28PropertySheetStringListValu'
        'eES2_',
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

  @overload(QStringList)
  @overload(QStringList, bool)
  @overload(QStringList, bool, str)
  @overload(QStringList, bool, str, str)
  def __init__(
      self,
      value: QStringList,
      translatable: bool = True,
      disambiguation: str = '',
      comment: str = '',
  ) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::PropertySheetStringListValue::
    PropertySheetStringListValue(const QStringList &value, bool translatable,
    const QString &disambiguation, const QString &comment)', which is called
    at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheetstringlistvalue.html

    Parameters
    ----------

    value : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    translatable : bool
      Passed on as it is. May be left out, as in Qt: it is then True.

    disambiguation : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    comment : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  qdesigner_internal::PropertySheetStringListValue::
    #      PropertySheetStringListValue(const QStringList &value, bool
    #      translatable, const QString &disambiguation, const QString
    #      &comment)
    self._noteCreation(PropertySheetStringListValue, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal28PropertySheetStringListValueC1ERK5Q'
        'ListI7QStringEbRKS2_S7_',
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
