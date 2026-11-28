"""
QPlaceCategory binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/qplacecategory.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QLocation

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QPlaceIcon
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPlaceIcon = WAIT['QPlaceIcon']


class QPlaceCategory(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPlaceCategory: a plain Python object standing in
  front of one C++ QPlaceCategory.

  C++ hands a QPlaceCategory around as a copy, so every C++ QPlaceCategory
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPlaceCategory that has a ritual and that Python can
  call so far, 12 names in all: '__eq__', '__ne__', 'categoryId',
  'setCategoryId', 'name', 'setName', 'visibility', 'setVisibility', 'icon',
  'setIcon', 'isEmpty', 'isEqual'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPlaceCategory::QPlaceCategory(QPlaceCategory &&other)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QPlaceCategory::~QPlaceCategory()': the destructor: Python removes
    its C++ QPlaceCategory by it, and has no other use for it.
  - Qt's 'QPlaceCategory &QPlaceCategory::operator=(const QPlaceCategory
    &other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QPlaceCategory &QPlaceCategory::operator=(QPlaceCategory &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QPlaceCategory::swap(QPlaceCategory &other)': takes a type
    Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QPlaceCategory is created at the first use, not by
    'QPlaceCategory(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPlaceCategory back gives a copy the ritual made for
    Python, in a new cute QPlaceCategory.
  - Each name of Qt's QPlaceCategory that has no cute function yet, 'swap',
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
  __qt_class__ = 'QPlaceCategory'

  #  Qt's '~QPlaceCategory()'. Naming it makes this a value class: Python
  #  owns every C++ QPlaceCategory behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QPlaceCategoryD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def categoryId(self) -> str:
    """
    Calls Qt's 'QString QPlaceCategory::categoryId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacecategory.html#categoryId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlaceCategory::categoryId() const
    return self.uglySide.call('ritual_ZNK14QPlaceCategory10categoryIdEv')

  def name(self) -> str:
    """
    Calls Qt's 'QString QPlaceCategory::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacecategory.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlaceCategory::name() const
    return self.uglySide.call('ritual_ZNK14QPlaceCategory4nameEv')

  def visibility(self) -> QLocation.Visibility:
    """
    Calls Qt's 'QLocation::Visibility QPlaceCategory::visibility() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacecategory.html#visibility

    Returns
    -------

    QLocation.Visibility
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QLocation.Visibility(number)' gives.
    """
    #  QLocation::Visibility QPlaceCategory::visibility() const
    return QLocation.Visibility(self.uglySide.call(
        'ritual_ZNK14QPlaceCategory10visibilityEv',
    ))

  def icon(self) -> QPlaceIcon:
    """
    Calls Qt's 'QPlaceIcon QPlaceCategory::icon() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacecategory.html#icon

    Returns
    -------

    QPlaceIcon
      A new cute QPlaceIcon around the copy Qt gave back. Python owns it.
    """
    #  QPlaceIcon QPlaceCategory::icon() const
    address = self.uglySide.call('ritual_ZNK14QPlaceCategory4iconEv')
    from . import QPlaceIcon
    return QPlaceIcon._cuteOwning(address)

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QPlaceCategory::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacecategory.html#isEmpty
    """
    #  bool QPlaceCategory::isEmpty() const
    return self.uglySide.call('ritual_ZNK14QPlaceCategory7isEmptyEv')

  @overload(THIS)
  def isEqual(self, other: QPlaceCategory) -> bool:
    """
    Calls Qt's 'bool QPlaceCategory::isEqual(const QPlaceCategory &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacecategory.html#isEqual

    Parameters
    ----------

    other : QPlaceCategory
      Passed on as a value: Qt reads the C++ QPlaceCategory, which stays
      Python's own.
    """
    #  bool QPlaceCategory::isEqual(const QPlaceCategory &other) const
    return self.uglySide.call(
        'ritual_ZNK14QPlaceCategory7isEqualERKS_', self._valueOf(other),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setCategoryId(self, identifier: str) -> None:
    """
    Calls Qt's 'void QPlaceCategory::setCategoryId(const QString
    &identifier)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacecategory.html#setCategoryId

    Parameters
    ----------

    identifier : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlaceCategory::setCategoryId(const QString &identifier)
    self.uglySide.call(
        'ritual_ZN14QPlaceCategory13setCategoryIdERK7QString', identifier,
    )

  @overload(str)
  def setName(self, name: str) -> None:
    """
    Calls Qt's 'void QPlaceCategory::setName(const QString &name)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacecategory.html#setName

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlaceCategory::setName(const QString &name)
    self.uglySide.call('ritual_ZN14QPlaceCategory7setNameERK7QString', name)

  @overload(QLocation.Visibility)
  def setVisibility(self, visibility: QLocation.Visibility) -> None:
    """
    Calls Qt's 'void QPlaceCategory::setVisibility(QLocation::Visibility
    visibility)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacecategory.html#setVisibility

    Parameters
    ----------

    visibility : QLocation.Visibility
      Passed on as its number.
    """
    #  void QPlaceCategory::setVisibility(QLocation::Visibility visibility)
    self.uglySide.call(
        'ritual_ZN14QPlaceCategory13setVisibilityEN9QLocation10VisibilityE',
        visibility.value,
    )

  @overload(QPlaceIcon)
  def setIcon(self, icon: QPlaceIcon) -> None:
    """
    Calls Qt's 'void QPlaceCategory::setIcon(const QPlaceIcon &icon)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacecategory.html#setIcon

    Parameters
    ----------

    icon : QPlaceIcon
      Passed on as a value: Qt reads the C++ QPlaceIcon, which stays Python's
      own.
    """
    #  void QPlaceCategory::setIcon(const QPlaceIcon &icon)
    self.uglySide.call(
        'ritual_ZN14QPlaceCategory7setIconERK10QPlaceIcon',
        self._valueOf(icon),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QPlaceCategory) -> bool:
    """
    Calls Qt's 'bool operator==(const QPlaceCategory &lhs, const
    QPlaceCategory &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacecategory.html#operator==

    Parameters
    ----------

    rhs : QPlaceCategory
      Passed on as a value: Qt reads the C++ QPlaceCategory, which stays
      Python's own.
    """
    #  bool operator==(const QPlaceCategory &lhs, const QPlaceCategory &rhs)
    return Rituals.call(
        'ritual_ZeqRK14QPlaceCategoryS1_',
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
  def __ne__(self, rhs: QPlaceCategory) -> bool:
    """
    Calls Qt's 'bool operator!=(const QPlaceCategory &lhs, const
    QPlaceCategory &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacecategory.html#operator!=

    Parameters
    ----------

    rhs : QPlaceCategory
      Passed on as a value: Qt reads the C++ QPlaceCategory, which stays
      Python's own.
    """
    #  bool operator!=(const QPlaceCategory &lhs, const QPlaceCategory &rhs)
    return Rituals.call(
        'ritual_ZneRK14QPlaceCategoryS1_',
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
    Notes what was given, for Qt's 'QPlaceCategory::QPlaceCategory()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qplacecategory.html#QPlaceCategory
    """
    #  QPlaceCategory::QPlaceCategory()
    self._noteCreation(QPlaceCategory, lambda: Rituals.call(
        'ritual_ZN14QPlaceCategoryC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QPlaceCategory) -> None:
    """
    Notes what was given, for Qt's 'QPlaceCategory::QPlaceCategory(const
    QPlaceCategory &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qplacecategory.html#QPlaceCategory

    Parameters
    ----------

    other : QPlaceCategory
      Passed on as a value: Qt reads the C++ QPlaceCategory, which stays
      Python's own.
    """
    #  QPlaceCategory::QPlaceCategory(const QPlaceCategory &other)
    self._noteCreation(QPlaceCategory, lambda: Rituals.call(
        'ritual_ZN14QPlaceCategoryC1ERKS_', self._valueOf(other),
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
    Qt's 'void QPlaceCategory::swap(QPlaceCategory &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPlaceCategory.swap' has no cute function yet. Qt's 'void "
        "QPlaceCategory::swap(QPlaceCategory &other)': takes a type Python "
        "has no way to hand over yet.")


#  Qt's 'QList<QPlaceCategory>': the list of QPlaceCategory, which
#  'QList[QPlaceCategory]' gives. It is made here, so that there is one as
#  soon as there can be a QPlaceCategory.
QList.createKind(
    QPlaceCategory, 'value',
    make='ritual_list_make_QPlaceCategory',
    add='ritual_list_add_QPlaceCategory',
    size='ritual_list_size_QPlaceCategory',
    at='ritual_list_at_QPlaceCategory',
    drop='ritual_list_drop_QPlaceCategory',
)
