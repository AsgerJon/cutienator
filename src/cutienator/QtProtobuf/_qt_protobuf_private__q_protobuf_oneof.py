"""
QtProtobufPrivate::QProtobufOneof binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtProtobuf/qprotobufoneof.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QMetaType, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaType = WAIT['QMetaType']
  QVariant = WAIT['QVariant']


class QProtobufOneof(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QtProtobufPrivate::QProtobufOneof: a plain Python
  object standing in front of one C++ QtProtobufPrivate::QProtobufOneof.

  C++ hands a QtProtobufPrivate::QProtobufOneof around as a copy, so every
  C++ QtProtobufPrivate::QProtobufOneof behind a cute one is Python's own: it
  is removed, by the ritual named in '__delete_ritual__', when the cute
  object goes.

  What exists
  -----------

  Every function of Qt's QtProtobufPrivate::QProtobufOneof that has a ritual
  and that Python can call so far, 8 names in all: 'fieldNumber',
  'holdsField', 'ensureMetaType', 'ensureRawValue', '__eq__', '__ne__',
  'setValue', 'rawValue'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QtProtobufPrivate::QProtobufOneof::~QProtobufOneof()': the
    destructor: Python removes its C++ QtProtobufPrivate::QProtobufOneof by
    it, and has no other use for it.
  - Qt's 'QProtobufOneof &QtProtobufPrivate::QProtobufOneof::operator=(const
    QProtobufOneof &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QtProtobufPrivate::QProtobufOneof::QProtobufOneof(QProtobufOneof
    &&other)': takes a type Python has no way to hand over yet.
  - Qt's 'QProtobufOneof
    &QtProtobufPrivate::QProtobufOneof::operator=(QProtobufOneof &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QtProtobufPrivate::QProtobufOneof::swap(QProtobufOneof
    &other)': takes a type Python has no way to hand over yet.
  - Qt's 'QVariant &QtProtobufPrivate::QProtobufOneof::rawValue()': gives a
    type Python has no way to take yet.

  What has no ritual
  ------------------

  9 of the 25 functions Qt declares: 7 a template; 2 the compiler refuses its
  ritual as it would be written here.

  What to expect
  --------------

  - The C++ QtProtobufPrivate::QProtobufOneof is created at the first use,
    not by 'QtProtobufPrivate::QProtobufOneof(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QtProtobufPrivate::QProtobufOneof back gives a copy
    the ritual made for Python, in a new cute
    QtProtobufPrivate::QProtobufOneof.
  - Each name of Qt's QtProtobufPrivate::QProtobufOneof that has no cute
    function yet, 'd_func', 'isEqual', 'message', 'swap', 'value', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(QMetaType, QMetaType)
  def ensureMetaType(lhs: QMetaType, rhs: QMetaType) -> None:
    """
    Calls Qt's 'void
    QtProtobufPrivate::QProtobufOneof::ensureMetaType(QMetaType lhs,
    QMetaType rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprotobufprivate-qprotobufoneof.html

    Parameters
    ----------

    lhs : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.

    rhs : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.
    """
    #  void QtProtobufPrivate::QProtobufOneof::ensureMetaType(QMetaType lhs,
    #      QMetaType rhs)
    Rituals.call(
        'ritual_ZN17QtProtobufPrivate14QProtobufOneof14ensureMetaTypeE9QMet'
        'aTypeS1_',
        CuteMixin._valueOf(lhs), CuteMixin._valueOf(rhs),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QtProtobufPrivate::QProtobufOneof'

  #  Qt's '~QtProtobufPrivate::QProtobufOneof()'. Naming it makes this a
  #  value class: Python owns every C++ QtProtobufPrivate::QProtobufOneof
  #  behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN17QtProtobufPrivate14QProtobufOneofD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def fieldNumber(self) -> int:
    """
    Calls Qt's 'int QtProtobufPrivate::QProtobufOneof::fieldNumber() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprotobufprivate-qprotobufoneof.html#fieldNumber
    """
    #  int QtProtobufPrivate::QProtobufOneof::fieldNumber() const
    return self.uglySide.call(
        'ritual_ZNK17QtProtobufPrivate14QProtobufOneof11fieldNumberEv',
    )

  @overload(int)
  def holdsField(self, fieldNumber: int) -> bool:
    """
    Calls Qt's 'bool QtProtobufPrivate::QProtobufOneof::holdsField(int
    fieldNumber) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprotobufprivate-qprotobufoneof.html#holdsField

    Parameters
    ----------

    fieldNumber : int
      Passed on as it is.
    """
    #  bool QtProtobufPrivate::QProtobufOneof::holdsField(int fieldNumber)
    #      const
    return self.uglySide.call(
        'ritual_ZNK17QtProtobufPrivate14QProtobufOneof10holdsFieldEi',
        fieldNumber,
    )

  def rawValue(self) -> QVariant:
    """
    Calls Qt's 'const QVariant &QtProtobufPrivate::QProtobufOneof::rawValue()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprotobufprivate-qprotobufoneof.html#rawValue

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  const QVariant &QtProtobufPrivate::QProtobufOneof::rawValue() const
    address = self.uglySide.call(
        'ritual_ZNK17QtProtobufPrivate14QProtobufOneof8rawValueEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant, int)
  def setValue(self, value: QVariant, fieldNumber: int) -> None:
    """
    Calls Qt's 'void QtProtobufPrivate::QProtobufOneof::setValue(const
    QVariant &value, int fieldNumber)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprotobufprivate-qprotobufoneof.html#setValue

    Parameters
    ----------

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    fieldNumber : int
      Passed on as it is.
    """
    #  void QtProtobufPrivate::QProtobufOneof::setValue(const QVariant
    #      &value, int fieldNumber)
    self.uglySide.call(
        'ritual_ZN17QtProtobufPrivate14QProtobufOneof8setValueERK8QVarianti',
        self._valueOf(value), fieldNumber,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QProtobufOneof) -> bool:
    """
    Calls Qt's 'bool operator==(const QProtobufOneof &lhs, const
    QProtobufOneof &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprotobufprivate-qprotobufoneof.html#operator==

    Parameters
    ----------

    rhs : QProtobufOneof
      Passed on as a value: Qt reads the C++
      QtProtobufPrivate::QProtobufOneof, which stays Python's own.
    """
    #  bool operator==(const QProtobufOneof &lhs, const QProtobufOneof &rhs)
    return Rituals.call(
        'ritual_ZN17QtProtobufPrivateeqERKNS_14QProtobufOneofES2_',
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
  def __ne__(self, rhs: QProtobufOneof) -> bool:
    """
    Calls Qt's 'bool operator!=(const QProtobufOneof &lhs, const
    QProtobufOneof &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprotobufprivate-qprotobufoneof.html#operator!=

    Parameters
    ----------

    rhs : QProtobufOneof
      Passed on as a value: Qt reads the C++
      QtProtobufPrivate::QProtobufOneof, which stays Python's own.
    """
    #  bool operator!=(const QProtobufOneof &lhs, const QProtobufOneof &rhs)
    return Rituals.call(
        'ritual_ZN17QtProtobufPrivateneERKNS_14QProtobufOneofES2_',
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
    'QtProtobufPrivate::QProtobufOneof::QProtobufOneof()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprotobufprivate-qprotobufoneof.html
    """
    #  QtProtobufPrivate::QProtobufOneof::QProtobufOneof()
    self._noteCreation(QProtobufOneof, lambda: Rituals.call(
        'ritual_ZN17QtProtobufPrivate14QProtobufOneofC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QProtobufOneof) -> None:
    """
    Notes what was given, for Qt's
    'QtProtobufPrivate::QProtobufOneof::QProtobufOneof(const QProtobufOneof
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprotobufprivate-qprotobufoneof.html

    Parameters
    ----------

    other : QProtobufOneof
      Passed on as a value: Qt reads the C++
      QtProtobufPrivate::QProtobufOneof, which stays Python's own.
    """
    #  QtProtobufPrivate::QProtobufOneof::QProtobufOneof(const QProtobufOneof
    #      &other)
    self._noteCreation(QProtobufOneof, lambda: Rituals.call(
        'ritual_ZN17QtProtobufPrivate14QProtobufOneofC1ERKS0_',
        self._valueOf(other),
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

  @overload(QMetaType)
  def ensureRawValue(self, metaType: QMetaType) -> None:
    """
    Calls Qt's 'void
    QtProtobufPrivate::QProtobufOneof::ensureRawValue(QMetaType metaType)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtprotobufprivate-qprotobufoneof.html

    Parameters
    ----------

    metaType : QMetaType
      Passed on as a value: Qt reads the C++ QMetaType, which stays Python's
      own.
    """
    #  void QtProtobufPrivate::QProtobufOneof::ensureRawValue(QMetaType
    #      metaType)
    self.uglySide.call(
        'ritual_ZN17QtProtobufPrivate14QProtobufOneof14ensureRawValueE9QMet'
        'aType',
        self._valueOf(metaType),
    )

  @staticmethod
  def d_func(*__, **_) -> Never:
    """
    - Qt's 'QProtobufOneofPrivate
      *QtProtobufPrivate::QProtobufOneof::d_func()': the compiler refuses its
      ritual as it would be written here: unknown type name
      'QProtobufOneofPrivate'; did you mean
      'QtProtobufPrivate::QProtobufOneofPrivate'?.
    - Qt's 'const QProtobufOneofPrivate
      *QtProtobufPrivate::QProtobufOneof::d_func() const': the compiler
      refuses its ritual as it would be written here: unknown type name
      'QProtobufOneofPrivate'; did you mean
      'QtProtobufPrivate::QProtobufOneofPrivate'?.
    """
    raise NotImplementedError(
        "'QtProtobufPrivate.QProtobufOneof.d_func' has no cute function "
        "yet. Qt's 'QProtobufOneofPrivate "
        "*QtProtobufPrivate::QProtobufOneof::d_func()': the compiler "
        "refuses its ritual as it would be written here: unknown type name "
        "'QProtobufOneofPrivate'; did you mean "
        "'QtProtobufPrivate::QProtobufOneofPrivate'?. Qt's 'const "
        "QProtobufOneofPrivate *QtProtobufPrivate::QProtobufOneof::d_func() "
        "const': the compiler refuses its ritual as it would be written "
        "here: unknown type name 'QProtobufOneofPrivate'; did you mean "
        "'QtProtobufPrivate::QProtobufOneofPrivate'?.")

  @staticmethod
  def isEqual(*__, **_) -> Never:
    """
    Qt's 'QtProtobufPrivate::QProtobufOneof::isEqual': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'QtProtobufPrivate.QProtobufOneof.isEqual' has no cute function "
        "yet. Qt's 'QtProtobufPrivate::QProtobufOneof::isEqual': a "
        "template: a pattern and no single function.")

  @staticmethod
  def message(*__, **_) -> Never:
    """
    Qt's 'QtProtobufPrivate::QProtobufOneof::message': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'QtProtobufPrivate.QProtobufOneof.message' has no cute function "
        "yet. Qt's 'QtProtobufPrivate::QProtobufOneof::message': a "
        "template: a pattern and no single function.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QtProtobufPrivate::QProtobufOneof::swap(QProtobufOneof
    &other)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QtProtobufPrivate.QProtobufOneof.swap' has no cute function yet. "
        "Qt's 'void QtProtobufPrivate::QProtobufOneof::swap(QProtobufOneof "
        "&other)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def value(*__, **_) -> Never:
    """
    Qt's 'QtProtobufPrivate::QProtobufOneof::value': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'QtProtobufPrivate.QProtobufOneof.value' has no cute function yet. "
        "Qt's 'QtProtobufPrivate::QProtobufOneof::value': a template: a "
        "pattern and no single function.")
