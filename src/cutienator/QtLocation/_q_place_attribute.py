"""
QPlaceAttribute binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/qplaceattribute.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import QMap

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QPlaceAttribute(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPlaceAttribute: a plain Python object standing in
  front of one C++ QPlaceAttribute.

  C++ hands a QPlaceAttribute around as a copy, so every C++ QPlaceAttribute
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPlaceAttribute that has a ritual and that Python
  can call so far, 8 names in all: '__eq__', '__ne__', 'label', 'setLabel',
  'text', 'setText', 'isEmpty', 'isEqual'. It can be made from Python, in 2
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPlaceAttribute::QPlaceAttribute(QPlaceAttribute &&other)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QPlaceAttribute::~QPlaceAttribute()': the destructor: Python
    removes its C++ QPlaceAttribute by it, and has no other use for it.
  - Qt's 'QPlaceAttribute &QPlaceAttribute::operator=(const QPlaceAttribute
    &other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QPlaceAttribute &QPlaceAttribute::operator=(QPlaceAttribute
    &&other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'void QPlaceAttribute::swap(QPlaceAttribute &other)': takes a type
    Python has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 18 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QPlaceAttribute is created at the first use, not by
    'QPlaceAttribute(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPlaceAttribute back gives a copy the ritual made for
    Python, in a new cute QPlaceAttribute.
  - Each name of Qt's QPlaceAttribute that has no cute function yet, 'swap',
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
  __qt_class__ = 'QPlaceAttribute'

  #  Qt's '~QPlaceAttribute()'. Naming it makes this a value class: Python
  #  owns every C++ QPlaceAttribute behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QPlaceAttributeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def label(self) -> str:
    """
    Calls Qt's 'QString QPlaceAttribute::label() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceattribute.html#label

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlaceAttribute::label() const
    return self.uglySide.call('ritual_ZNK15QPlaceAttribute5labelEv')

  def text(self) -> str:
    """
    Calls Qt's 'QString QPlaceAttribute::text() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceattribute.html#text

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlaceAttribute::text() const
    return self.uglySide.call('ritual_ZNK15QPlaceAttribute4textEv')

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QPlaceAttribute::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceattribute.html#isEmpty
    """
    #  bool QPlaceAttribute::isEmpty() const
    return self.uglySide.call('ritual_ZNK15QPlaceAttribute7isEmptyEv')

  @overload(THIS)
  def isEqual(self, other: QPlaceAttribute) -> bool:
    """
    Calls Qt's 'bool QPlaceAttribute::isEqual(const QPlaceAttribute &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceattribute.html#isEqual

    Parameters
    ----------

    other : QPlaceAttribute
      Passed on as a value: Qt reads the C++ QPlaceAttribute, which stays
      Python's own.
    """
    #  bool QPlaceAttribute::isEqual(const QPlaceAttribute &other) const
    return self.uglySide.call(
        'ritual_ZNK15QPlaceAttribute7isEqualERKS_', self._valueOf(other),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setLabel(self, label: str) -> None:
    """
    Calls Qt's 'void QPlaceAttribute::setLabel(const QString &label)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceattribute.html#setLabel

    Parameters
    ----------

    label : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlaceAttribute::setLabel(const QString &label)
    self.uglySide.call(
        'ritual_ZN15QPlaceAttribute8setLabelERK7QString', label,
    )

  @overload(str)
  def setText(self, text: str) -> None:
    """
    Calls Qt's 'void QPlaceAttribute::setText(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceattribute.html#setText

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlaceAttribute::setText(const QString &text)
    self.uglySide.call('ritual_ZN15QPlaceAttribute7setTextERK7QString', text)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QPlaceAttribute) -> bool:
    """
    Calls Qt's 'bool operator==(const QPlaceAttribute &lhs, const
    QPlaceAttribute &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceattribute.html#operator==

    Parameters
    ----------

    rhs : QPlaceAttribute
      Passed on as a value: Qt reads the C++ QPlaceAttribute, which stays
      Python's own.
    """
    #  bool operator==(const QPlaceAttribute &lhs, const QPlaceAttribute
    #      &rhs)
    return Rituals.call(
        'ritual_ZeqRK15QPlaceAttributeS1_',
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
  def __ne__(self, rhs: QPlaceAttribute) -> bool:
    """
    Calls Qt's 'bool operator!=(const QPlaceAttribute &lhs, const
    QPlaceAttribute &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceattribute.html#operator!=

    Parameters
    ----------

    rhs : QPlaceAttribute
      Passed on as a value: Qt reads the C++ QPlaceAttribute, which stays
      Python's own.
    """
    #  bool operator!=(const QPlaceAttribute &lhs, const QPlaceAttribute
    #      &rhs)
    return Rituals.call(
        'ritual_ZneRK15QPlaceAttributeS1_',
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
    Notes what was given, for Qt's 'QPlaceAttribute::QPlaceAttribute()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaceattribute.html#QPlaceAttribute
    """
    #  QPlaceAttribute::QPlaceAttribute()
    self._noteCreation(QPlaceAttribute, lambda: Rituals.call(
        'ritual_ZN15QPlaceAttributeC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QPlaceAttribute) -> None:
    """
    Notes what was given, for Qt's 'QPlaceAttribute::QPlaceAttribute(const
    QPlaceAttribute &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaceattribute.html#QPlaceAttribute

    Parameters
    ----------

    other : QPlaceAttribute
      Passed on as a value: Qt reads the C++ QPlaceAttribute, which stays
      Python's own.
    """
    #  QPlaceAttribute::QPlaceAttribute(const QPlaceAttribute &other)
    self._noteCreation(QPlaceAttribute, lambda: Rituals.call(
        'ritual_ZN15QPlaceAttributeC1ERKS_', self._valueOf(other),
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
    Qt's 'void QPlaceAttribute::swap(QPlaceAttribute &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPlaceAttribute.swap' has no cute function yet. Qt's 'void "
        "QPlaceAttribute::swap(QPlaceAttribute &other)': takes a type "
        "Python has no way to hand over yet.")


#  Qt's 'QMap<QString, QPlaceAttribute>': the QMap from text to
#  QPlaceAttribute, which 'QMap[str, QPlaceAttribute]' gives. It is completed
#  here, in the file of the class of its values.
QMap.createKind(
    str, QPlaceAttribute, 'value',
    make='ritual_map_make_QMap_QString_QPlaceAttribute',
    put='ritual_map_put_QMap_QString_QPlaceAttribute',
    size='ritual_map_size_QMap_QString_QPlaceAttribute',
    key='ritual_map_key_QMap_QString_QPlaceAttribute',
    value='ritual_map_value_QMap_QString_QPlaceAttribute',
    has='ritual_map_has_QMap_QString_QPlaceAttribute',
    get='ritual_map_get_QMap_QString_QPlaceAttribute',
    drop='ritual_map_drop_QMap_QString_QPlaceAttribute',
)
