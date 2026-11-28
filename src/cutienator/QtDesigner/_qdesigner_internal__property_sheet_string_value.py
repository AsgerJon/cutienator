"""
qdesigner_internal::PropertySheetStringValue binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtDesigner/6.12.0/QtDesigner/private/qdesigner_utils_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means qdesigner_internal::PropertySheetStringValue to be private: it
#  declares the class in a header it calls private. cutienator does not care.
#  Qt hands objects of the class out all the same, and a class we are handed
#  is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..occult import Rituals
from . import qdesigner_internal


class PropertySheetStringValue(qdesigner_internal.PropertySheetTranslatableData):
  """
  The cute side of Qt's qdesigner_internal::PropertySheetStringValue: a plain
  Python object standing in front of one C++
  qdesigner_internal::PropertySheetStringValue.

  It is built on the cute
  'qdesigner_internal::PropertySheetTranslatableData', as Qt's
  qdesigner_internal::PropertySheetStringValue is built on Qt's
  qdesigner_internal::PropertySheetTranslatableData, and has everything that
  class has.

  C++ hands a qdesigner_internal::PropertySheetStringValue around as a copy,
  so every C++ qdesigner_internal::PropertySheetStringValue behind a cute one
  is Python's own: it is removed, by the ritual named in '__delete_ritual__',
  when the cute object goes.

  What exists
  -----------

  Every function of Qt's qdesigner_internal::PropertySheetStringValue that
  has a ritual and that Python can call so far, 4 names in all: 'value',
  'setValue', '__eq__', '__ne__'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's
    'qdesigner_internal::PropertySheetStringValue::~PropertySheetStringValue(
    )': the destructor: Python removes its C++
    qdesigner_internal::PropertySheetStringValue by it, and has no other use
    for it.

  What to expect
  --------------

  - The C++ qdesigner_internal::PropertySheetStringValue is created at the
    first use, not by 'qdesigner_internal::PropertySheetStringValue(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a qdesigner_internal::PropertySheetStringValue back
    gives a copy the ritual made for Python, in a new cute
    qdesigner_internal::PropertySheetStringValue.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'qdesigner_internal::PropertySheetStringValue'

  #  Qt's '~qdesigner_internal::PropertySheetStringValue()'. Naming it makes
  #  this a value class: Python owns every C++
  #  qdesigner_internal::PropertySheetStringValue behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = (
      'ritual_ZN18qdesigner_internal24PropertySheetStringValueD1Ev')

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def value(self) -> str:
    """
    Calls Qt's 'QString qdesigner_internal::PropertySheetStringValue::value()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheetstringvalue.html

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString qdesigner_internal::PropertySheetStringValue::value() const
    return self.uglySide.call(
        'ritual_ZNK18qdesigner_internal24PropertySheetStringValue5valueEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setValue(self, value: str) -> None:
    """
    Calls Qt's 'void
    qdesigner_internal::PropertySheetStringValue::setValue(const QString
    &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheetstringvalue.html

    Parameters
    ----------

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void qdesigner_internal::PropertySheetStringValue::setValue(const
    #      QString &value)
    self.uglySide.call(
        'ritual_ZN18qdesigner_internal24PropertySheetStringValue8setValueER'
        'K7QString',
        value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: PropertySheetStringValue) -> bool:
    """
    Calls Qt's 'bool operator==(const PropertySheetStringValue &lhs, const
    PropertySheetStringValue &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheetstringvalue.html

    Parameters
    ----------

    rhs : PropertySheetStringValue
      Passed on as a value: Qt reads the C++
      qdesigner_internal::PropertySheetStringValue, which stays Python's own.
    """
    #  bool operator==(const PropertySheetStringValue &lhs, const
    #      PropertySheetStringValue &rhs)
    return Rituals.call(
        'ritual_ZN18qdesigner_internaleqERKNS_24PropertySheetStringValueES2'
        '_',
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
  def __ne__(self, rhs: PropertySheetStringValue) -> bool:
    """
    Calls Qt's 'bool operator!=(const PropertySheetStringValue &lhs, const
    PropertySheetStringValue &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheetstringvalue.html

    Parameters
    ----------

    rhs : PropertySheetStringValue
      Passed on as a value: Qt reads the C++
      qdesigner_internal::PropertySheetStringValue, which stays Python's own.
    """
    #  bool operator!=(const PropertySheetStringValue &lhs, const
    #      PropertySheetStringValue &rhs)
    return Rituals.call(
        'ritual_ZN18qdesigner_internalneERKNS_24PropertySheetStringValueES2'
        '_',
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
  @overload(str)
  @overload(str, bool)
  @overload(str, bool, str)
  @overload(str, bool, str, str)
  def __init__(
      self,
      value: str = '',
      translatable: bool = True,
      disambiguation: str = '',
      comment: str = '',
  ) -> None:
    """
    Notes what was given, for Qt's
    'qdesigner_internal::PropertySheetStringValue::PropertySheetStringValue(
    const QString &value, bool translatable, const QString &disambiguation,
    const QString &comment)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdesigner_internal-propertysheetstringvalue.html

    Parameters
    ----------

    value : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    translatable : bool
      Passed on as it is. May be left out, as in Qt: it is then True.

    disambiguation : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    comment : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  qdesigner_internal::PropertySheetStringValue::
    #      PropertySheetStringValue(const QString &value, bool translatable,
    #      const QString &disambiguation, const QString &comment)
    self._noteCreation(PropertySheetStringValue, lambda: Rituals.call(
        'ritual_ZN18qdesigner_internal24PropertySheetStringValueC1ERK7QStri'
        'ngbS3_S3_',
        value, translatable, disambiguation, comment,
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
