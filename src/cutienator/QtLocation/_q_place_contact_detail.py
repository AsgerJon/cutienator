"""
QPlaceContactDetail binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/qplacecontactdetail.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals
from ..QtCore import QList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QPlaceContactDetail(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPlaceContactDetail: a plain Python object standing
  in front of one C++ QPlaceContactDetail.

  C++ hands a QPlaceContactDetail around as a copy, so every C++
  QPlaceContactDetail behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPlaceContactDetail that has a ritual and that
  Python can call so far, 8 names in all: '__eq__', '__ne__', 'label',
  'setLabel', 'value', 'setValue', 'clear', 'isEqual'. It can be made from
  Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPlaceContactDetail::QPlaceContactDetail(QPlaceContactDetail
    &&other)': takes a type Python has no way to hand over yet.
  - Qt's 'QPlaceContactDetail::~QPlaceContactDetail()': the destructor:
    Python removes its C++ QPlaceContactDetail by it, and has no other use
    for it.
  - Qt's 'QPlaceContactDetail &QPlaceContactDetail::operator=(const
    QPlaceContactDetail &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QPlaceContactDetail
    &QPlaceContactDetail::operator=(QPlaceContactDetail &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QPlaceContactDetail::swap(QPlaceContactDetail &other)': takes
    a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 18 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QPlaceContactDetail is created at the first use, not by
    'QPlaceContactDetail(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPlaceContactDetail back gives a copy the ritual made
    for Python, in a new cute QPlaceContactDetail.
  - Each name of Qt's QPlaceContactDetail that has no cute function yet,
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
  __qt_class__ = 'QPlaceContactDetail'

  #  Qt's '~QPlaceContactDetail()'. Naming it makes this a value class:
  #  Python owns every C++ QPlaceContactDetail behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QPlaceContactDetailD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def label(self) -> str:
    """
    Calls Qt's 'QString QPlaceContactDetail::label() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacecontactdetail.html#label

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlaceContactDetail::label() const
    return self.uglySide.call('ritual_ZNK19QPlaceContactDetail5labelEv')

  def value(self) -> str:
    """
    Calls Qt's 'QString QPlaceContactDetail::value() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacecontactdetail.html#value

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlaceContactDetail::value() const
    return self.uglySide.call('ritual_ZNK19QPlaceContactDetail5valueEv')

  @overload(THIS)
  def isEqual(self, other: QPlaceContactDetail) -> bool:
    """
    Calls Qt's 'bool QPlaceContactDetail::isEqual(const QPlaceContactDetail
    &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacecontactdetail.html#isEqual

    Parameters
    ----------

    other : QPlaceContactDetail
      Passed on as a value: Qt reads the C++ QPlaceContactDetail, which stays
      Python's own.
    """
    #  bool QPlaceContactDetail::isEqual(const QPlaceContactDetail &other)
    #      const
    return self.uglySide.call(
        'ritual_ZNK19QPlaceContactDetail7isEqualERKS_', self._valueOf(other),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setLabel(self, label: str) -> None:
    """
    Calls Qt's 'void QPlaceContactDetail::setLabel(const QString &label)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacecontactdetail.html#setLabel

    Parameters
    ----------

    label : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlaceContactDetail::setLabel(const QString &label)
    self.uglySide.call(
        'ritual_ZN19QPlaceContactDetail8setLabelERK7QString', label,
    )

  @overload(str)
  def setValue(self, value: str) -> None:
    """
    Calls Qt's 'void QPlaceContactDetail::setValue(const QString &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacecontactdetail.html#setValue

    Parameters
    ----------

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlaceContactDetail::setValue(const QString &value)
    self.uglySide.call(
        'ritual_ZN19QPlaceContactDetail8setValueERK7QString', value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QPlaceContactDetail) -> bool:
    """
    Calls Qt's 'bool operator==(const QPlaceContactDetail &lhs, const
    QPlaceContactDetail &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacecontactdetail.html#operator==

    Parameters
    ----------

    rhs : QPlaceContactDetail
      Passed on as a value: Qt reads the C++ QPlaceContactDetail, which stays
      Python's own.
    """
    #  bool operator==(const QPlaceContactDetail &lhs, const
    #      QPlaceContactDetail &rhs)
    return Rituals.call(
        'ritual_ZeqRK19QPlaceContactDetailS1_',
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
  def __ne__(self, rhs: QPlaceContactDetail) -> bool:
    """
    Calls Qt's 'bool operator!=(const QPlaceContactDetail &lhs, const
    QPlaceContactDetail &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacecontactdetail.html#operator!=

    Parameters
    ----------

    rhs : QPlaceContactDetail
      Passed on as a value: Qt reads the C++ QPlaceContactDetail, which stays
      Python's own.
    """
    #  bool operator!=(const QPlaceContactDetail &lhs, const
    #      QPlaceContactDetail &rhs)
    return Rituals.call(
        'ritual_ZneRK19QPlaceContactDetailS1_',
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
    'QPlaceContactDetail::QPlaceContactDetail()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacecontactdetail.html#QPlaceContactDetail
    """
    #  QPlaceContactDetail::QPlaceContactDetail()
    self._noteCreation(QPlaceContactDetail, lambda: Rituals.call(
        'ritual_ZN19QPlaceContactDetailC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QPlaceContactDetail) -> None:
    """
    Notes what was given, for Qt's
    'QPlaceContactDetail::QPlaceContactDetail(const QPlaceContactDetail
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplacecontactdetail.html#QPlaceContactDetail

    Parameters
    ----------

    other : QPlaceContactDetail
      Passed on as a value: Qt reads the C++ QPlaceContactDetail, which stays
      Python's own.
    """
    #  QPlaceContactDetail::QPlaceContactDetail(const QPlaceContactDetail
    #      &other)
    self._noteCreation(QPlaceContactDetail, lambda: Rituals.call(
        'ritual_ZN19QPlaceContactDetailC1ERKS_', self._valueOf(other),
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

  def clear(self) -> None:
    """
    Calls Qt's 'void QPlaceContactDetail::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qplacecontactdetail.html#clear
    """
    #  void QPlaceContactDetail::clear()
    self.uglySide.call('ritual_ZN19QPlaceContactDetail5clearEv')

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QPlaceContactDetail::swap(QPlaceContactDetail &other)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPlaceContactDetail.swap' has no cute function yet. Qt's 'void "
        "QPlaceContactDetail::swap(QPlaceContactDetail &other)': takes a "
        "type Python has no way to hand over yet.")


#  Qt's 'QList<QPlaceContactDetail>': the list of QPlaceContactDetail, which
#  'QList[QPlaceContactDetail]' gives. It is made here, so that there is one
#  as soon as there can be a QPlaceContactDetail.
QList.createKind(
    QPlaceContactDetail, 'value',
    make='ritual_list_make_QPlaceContactDetail',
    add='ritual_list_add_QPlaceContactDetail',
    size='ritual_list_size_QPlaceContactDetail',
    at='ritual_list_at_QPlaceContactDetail',
    drop='ritual_list_drop_QPlaceContactDetail',
)
