"""
QPlaceSupplier binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/qplacesupplier.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QUrl
  from . import QPlaceIcon
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPlaceIcon = WAIT['QPlaceIcon']
  QUrl = WAIT['QUrl']


class QPlaceSupplier(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPlaceSupplier: a plain Python object standing in
  front of one C++ QPlaceSupplier.

  C++ hands a QPlaceSupplier around as a copy, so every C++ QPlaceSupplier
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPlaceSupplier that has a ritual and that Python can
  call so far, 12 names in all: '__eq__', '__ne__', 'name', 'setName',
  'supplierId', 'setSupplierId', 'url', 'setUrl', 'icon', 'setIcon',
  'isEmpty', 'isEqual'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPlaceSupplier::QPlaceSupplier(QPlaceSupplier &&other)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QPlaceSupplier::~QPlaceSupplier()': the destructor: Python removes
    its C++ QPlaceSupplier by it, and has no other use for it.
  - Qt's 'QPlaceSupplier &QPlaceSupplier::operator=(const QPlaceSupplier
    &other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QPlaceSupplier &QPlaceSupplier::operator=(QPlaceSupplier &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'void QPlaceSupplier::swap(QPlaceSupplier &other)': takes a type
    Python has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 22 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QPlaceSupplier is created at the first use, not by
    'QPlaceSupplier(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPlaceSupplier back gives a copy the ritual made for
    Python, in a new cute QPlaceSupplier.
  - Each name of Qt's QPlaceSupplier that has no cute function yet, 'swap',
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
  __qt_class__ = 'QPlaceSupplier'

  #  Qt's '~QPlaceSupplier()'. Naming it makes this a value class: Python
  #  owns every C++ QPlaceSupplier behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN14QPlaceSupplierD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def name(self) -> str:
    """
    Calls Qt's 'QString QPlaceSupplier::name() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacesupplier.html#name

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlaceSupplier::name() const
    return self.uglySide.call('ritual_ZNK14QPlaceSupplier4nameEv')

  def supplierId(self) -> str:
    """
    Calls Qt's 'QString QPlaceSupplier::supplierId() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacesupplier.html#supplierId

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QPlaceSupplier::supplierId() const
    return self.uglySide.call('ritual_ZNK14QPlaceSupplier10supplierIdEv')

  def url(self) -> QUrl:
    """
    Calls Qt's 'QUrl QPlaceSupplier::url() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacesupplier.html#url

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QPlaceSupplier::url() const
    address = self.uglySide.call('ritual_ZNK14QPlaceSupplier3urlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def icon(self) -> QPlaceIcon:
    """
    Calls Qt's 'QPlaceIcon QPlaceSupplier::icon() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacesupplier.html#icon

    Returns
    -------

    QPlaceIcon
      A new cute QPlaceIcon around the copy Qt gave back. Python owns it.
    """
    #  QPlaceIcon QPlaceSupplier::icon() const
    address = self.uglySide.call('ritual_ZNK14QPlaceSupplier4iconEv')
    from . import QPlaceIcon
    return QPlaceIcon._cuteOwning(address)

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QPlaceSupplier::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacesupplier.html#isEmpty
    """
    #  bool QPlaceSupplier::isEmpty() const
    return self.uglySide.call('ritual_ZNK14QPlaceSupplier7isEmptyEv')

  @overload(THIS)
  def isEqual(self, other: QPlaceSupplier) -> bool:
    """
    Calls Qt's 'bool QPlaceSupplier::isEqual(const QPlaceSupplier &other)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qplacesupplier.html#isEqual

    Parameters
    ----------

    other : QPlaceSupplier
      Passed on as a value: Qt reads the C++ QPlaceSupplier, which stays
      Python's own.
    """
    #  bool QPlaceSupplier::isEqual(const QPlaceSupplier &other) const
    return self.uglySide.call(
        'ritual_ZNK14QPlaceSupplier7isEqualERKS_', self._valueOf(other),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setName(self, data: str) -> None:
    """
    Calls Qt's 'void QPlaceSupplier::setName(const QString &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacesupplier.html#setName

    Parameters
    ----------

    data : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlaceSupplier::setName(const QString &data)
    self.uglySide.call('ritual_ZN14QPlaceSupplier7setNameERK7QString', data)

  @overload(str)
  def setSupplierId(self, identifier: str) -> None:
    """
    Calls Qt's 'void QPlaceSupplier::setSupplierId(const QString
    &identifier)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacesupplier.html#setSupplierId

    Parameters
    ----------

    identifier : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QPlaceSupplier::setSupplierId(const QString &identifier)
    self.uglySide.call(
        'ritual_ZN14QPlaceSupplier13setSupplierIdERK7QString', identifier,
    )

  @overload(QUrl)
  def setUrl(self, data: QUrl) -> None:
    """
    Calls Qt's 'void QPlaceSupplier::setUrl(const QUrl &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacesupplier.html#setUrl

    Parameters
    ----------

    data : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QPlaceSupplier::setUrl(const QUrl &data)
    self.uglySide.call(
        'ritual_ZN14QPlaceSupplier6setUrlERK4QUrl', self._valueOf(data),
    )

  @overload(QPlaceIcon)
  def setIcon(self, icon: QPlaceIcon) -> None:
    """
    Calls Qt's 'void QPlaceSupplier::setIcon(const QPlaceIcon &icon)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacesupplier.html#setIcon

    Parameters
    ----------

    icon : QPlaceIcon
      Passed on as a value: Qt reads the C++ QPlaceIcon, which stays Python's
      own.
    """
    #  void QPlaceSupplier::setIcon(const QPlaceIcon &icon)
    self.uglySide.call(
        'ritual_ZN14QPlaceSupplier7setIconERK10QPlaceIcon',
        self._valueOf(icon),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QPlaceSupplier) -> bool:
    """
    Calls Qt's 'bool operator==(const QPlaceSupplier &lhs, const
    QPlaceSupplier &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacesupplier.html#operator==

    Parameters
    ----------

    rhs : QPlaceSupplier
      Passed on as a value: Qt reads the C++ QPlaceSupplier, which stays
      Python's own.
    """
    #  bool operator==(const QPlaceSupplier &lhs, const QPlaceSupplier &rhs)
    return Rituals.call(
        'ritual_ZeqRK14QPlaceSupplierS1_',
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
  def __ne__(self, rhs: QPlaceSupplier) -> bool:
    """
    Calls Qt's 'bool operator!=(const QPlaceSupplier &lhs, const
    QPlaceSupplier &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qplacesupplier.html#operator!=

    Parameters
    ----------

    rhs : QPlaceSupplier
      Passed on as a value: Qt reads the C++ QPlaceSupplier, which stays
      Python's own.
    """
    #  bool operator!=(const QPlaceSupplier &lhs, const QPlaceSupplier &rhs)
    return Rituals.call(
        'ritual_ZneRK14QPlaceSupplierS1_',
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
    Notes what was given, for Qt's 'QPlaceSupplier::QPlaceSupplier()', which
    is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qplacesupplier.html#QPlaceSupplier
    """
    #  QPlaceSupplier::QPlaceSupplier()
    self._noteCreation(QPlaceSupplier, lambda: Rituals.call(
        'ritual_ZN14QPlaceSupplierC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QPlaceSupplier) -> None:
    """
    Notes what was given, for Qt's 'QPlaceSupplier::QPlaceSupplier(const
    QPlaceSupplier &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qplacesupplier.html#QPlaceSupplier

    Parameters
    ----------

    other : QPlaceSupplier
      Passed on as a value: Qt reads the C++ QPlaceSupplier, which stays
      Python's own.
    """
    #  QPlaceSupplier::QPlaceSupplier(const QPlaceSupplier &other)
    self._noteCreation(QPlaceSupplier, lambda: Rituals.call(
        'ritual_ZN14QPlaceSupplierC1ERKS_', self._valueOf(other),
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
    Qt's 'void QPlaceSupplier::swap(QPlaceSupplier &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPlaceSupplier.swap' has no cute function yet. Qt's 'void "
        "QPlaceSupplier::swap(QPlaceSupplier &other)': takes a type Python "
        "has no way to hand over yet.")
