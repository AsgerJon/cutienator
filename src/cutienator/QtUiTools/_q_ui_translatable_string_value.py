"""
QUiTranslatableStringValue binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtUiTools/6.12.0/QtUiTools/private/quiloader_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QUiTranslatableStringValue to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from ..QtCore import QByteArray
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']


class QUiTranslatableStringValue(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QUiTranslatableStringValue: a plain Python object
  standing in front of one C++ QUiTranslatableStringValue.

  C++ hands a QUiTranslatableStringValue around as a copy, so every C++
  QUiTranslatableStringValue behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QUiTranslatableStringValue that has a ritual and
  that Python can call so far, 5 names in all: 'value', 'setValue',
  'qualifier', 'setQualifier', 'translate'. None can be made from Python: one
  comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QUiTranslatableStringValue::~QUiTranslatableStringValue()': the
    destructor: Python removes its C++ QUiTranslatableStringValue by it, and
    has no other use for it.

  What to expect
  --------------

  - The C++ QUiTranslatableStringValue is created at the first use, not by
    'QUiTranslatableStringValue(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QUiTranslatableStringValue back gives a copy the
    ritual made for Python, in a new cute QUiTranslatableStringValue.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QUiTranslatableStringValue'

  #  Qt's '~QUiTranslatableStringValue()'. Naming it makes this a value
  #  class: Python owns every C++ QUiTranslatableStringValue behind a cute
  #  one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN26QUiTranslatableStringValueD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def value(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QUiTranslatableStringValue::value() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/quitranslatablestringvalue.html#value

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QUiTranslatableStringValue::value() const
    address = self.uglySide.call(
        'ritual_ZNK26QUiTranslatableStringValue5valueEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def qualifier(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QUiTranslatableStringValue::qualifier() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/quitranslatablestringvalue.html#qualifier

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QUiTranslatableStringValue::qualifier() const
    address = self.uglySide.call(
        'ritual_ZNK26QUiTranslatableStringValue9qualifierEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  @overload(QByteArray, bool)
  def translate(self, className: QByteArray, idBased: bool) -> str:
    """
    Calls Qt's 'QString QUiTranslatableStringValue::translate(const
    QByteArray &className, bool idBased) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/quitranslatablestringvalue.html#translate

    Parameters
    ----------

    className : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    idBased : bool
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QUiTranslatableStringValue::translate(const QByteArray
    #      &className, bool idBased) const
    return self.uglySide.call(
        'ritual_ZNK26QUiTranslatableStringValue9translateERK10QByteArrayb',
        self._valueOf(className), idBased,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QByteArray)
  def setValue(self, value: QByteArray) -> None:
    """
    Calls Qt's 'void QUiTranslatableStringValue::setValue(const QByteArray
    &value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/quitranslatablestringvalue.html#setValue

    Parameters
    ----------

    value : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QUiTranslatableStringValue::setValue(const QByteArray &value)
    self.uglySide.call(
        'ritual_ZN26QUiTranslatableStringValue8setValueERK10QByteArray',
        self._valueOf(value),
    )

  @overload(QByteArray)
  def setQualifier(self, qualifier: QByteArray) -> None:
    """
    Calls Qt's 'void QUiTranslatableStringValue::setQualifier(const
    QByteArray &qualifier)'.

    Qt's own words:
    https://doc.qt.io/qt-6/quitranslatablestringvalue.html#setQualifier

    Parameters
    ----------

    qualifier : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QUiTranslatableStringValue::setQualifier(const QByteArray
    #      &qualifier)
    self.uglySide.call(
        'ritual_ZN26QUiTranslatableStringValue12setQualifierERK10QByteArray',
        self._valueOf(qualifier),
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
