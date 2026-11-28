"""
QPlaceIcon binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/qplaceicon.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QMap

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QSize, QUrl, QVariant
  from . import QPlaceManager
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QPlaceManager = WAIT['QPlaceManager']
  QSize = WAIT['QSize']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlaceIcon(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPlaceIcon: a plain Python object standing in front
  of one C++ QPlaceIcon.

  C++ hands a QPlaceIcon around as a copy, so every C++ QPlaceIcon behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPlaceIcon that has a ritual and that Python can
  call so far, 9 names in all: '__eq__', '__ne__', 'url', 'manager',
  'setManager', 'parameters', 'setParameters', 'isEmpty', 'isEqual'. It can
  be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPlaceIcon::QPlaceIcon(QPlaceIcon &&other)': takes a type Python
    has no way to hand over yet.
  - Qt's 'QPlaceIcon::~QPlaceIcon()': the destructor: Python removes its C++
    QPlaceIcon by it, and has no other use for it.
  - Qt's 'QPlaceIcon &QPlaceIcon::operator=(const QPlaceIcon &other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QPlaceIcon &QPlaceIcon::operator=(QPlaceIcon &&other)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'void QPlaceIcon::swap(QPlaceIcon &other)': takes a type Python has
    no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 19 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QPlaceIcon is created at the first use, not by 'QPlaceIcon(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPlaceIcon back gives a copy the ritual made for
    Python, in a new cute QPlaceIcon.
  - Each name of Qt's QPlaceIcon that has no cute function yet, 'swap', holds
    a function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlaceIcon'

  #  Qt's '~QPlaceIcon()'. Naming it makes this a value class: Python owns
  #  every C++ QPlaceIcon behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN10QPlaceIconD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  @overload(QSize)
  def url(self, size: Optional[QSize] = None) -> QUrl:
    """
    Calls Qt's 'QUrl QPlaceIcon::url(const QSize &size) const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceicon.html#url

    Parameters
    ----------

    size : Optional[QSize]
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
      May be left out, as in Qt: a new 'QSize()' is then passed on.

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QPlaceIcon::url(const QSize &size) const
    if size is None:
      from ..QtCore import QSize
      size = QSize()
    address = self.uglySide.call(
        'ritual_ZNK10QPlaceIcon3urlERK5QSize', self._valueOf(size),
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def manager(self) -> Optional[QPlaceManager]:
    """
    Calls Qt's 'QPlaceManager *QPlaceIcon::manager() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceicon.html#manager

    Returns
    -------

    Optional[QPlaceManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlaceManager *QPlaceIcon::manager() const
    address = self.uglySide.call('ritual_ZNK10QPlaceIcon7managerEv')
    from . import QPlaceManager
    return QPlaceManager._cuteAt(address)

  def parameters(self) -> QMap[str, QVariant]:
    """
    Calls Qt's 'QVariantMap QPlaceIcon::parameters() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceicon.html#parameters

    Returns
    -------

    QMap[str, QVariant]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QVariantMap QPlaceIcon::parameters() const
    address = self.uglySide.call('ritual_ZNK10QPlaceIcon10parametersEv')
    from ..QtCore import QVariant
    return QMap[str, QVariant]._cuteOwning(address)

  def isEmpty(self) -> bool:
    """
    Calls Qt's 'bool QPlaceIcon::isEmpty() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceicon.html#isEmpty
    """
    #  bool QPlaceIcon::isEmpty() const
    return self.uglySide.call('ritual_ZNK10QPlaceIcon7isEmptyEv')

  @overload(THIS)
  def isEqual(self, other: QPlaceIcon) -> bool:
    """
    Calls Qt's 'bool QPlaceIcon::isEqual(const QPlaceIcon &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceicon.html#isEqual

    Parameters
    ----------

    other : QPlaceIcon
      Passed on as a value: Qt reads the C++ QPlaceIcon, which stays Python's
      own.
    """
    #  bool QPlaceIcon::isEqual(const QPlaceIcon &other) const
    return self.uglySide.call(
        'ritual_ZNK10QPlaceIcon7isEqualERKS_', self._valueOf(other),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QPlaceManager)
  @overload(NoneType)
  def setManager(self, manager: Optional[QPlaceManager]) -> None:
    """
    Calls Qt's 'void QPlaceIcon::setManager(QPlaceManager *manager)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceicon.html#setManager

    Parameters
    ----------

    manager : Optional[QPlaceManager]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlaceIcon::setManager(QPlaceManager *manager)
    self.uglySide.call(
        'ritual_ZN10QPlaceIcon10setManagerEP13QPlaceManager',
        self._addressOf(manager),
    )

  @overload(QMap[str, QVariant])
  def setParameters(self, parameters: QMap[str, QVariant]) -> None:
    """
    Calls Qt's 'void QPlaceIcon::setParameters(const QVariantMap
    &parameters)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceicon.html#setParameters

    Parameters
    ----------

    parameters : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void QPlaceIcon::setParameters(const QVariantMap &parameters)
    self.uglySide.call(
        'ritual_ZN10QPlaceIcon13setParametersERK4QMapI7QString8QVariantE',
        self._valueOf(parameters),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QPlaceIcon) -> bool:
    """
    Calls Qt's 'bool operator==(const QPlaceIcon &lhs, const QPlaceIcon
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceicon.html#operator==

    Parameters
    ----------

    rhs : QPlaceIcon
      Passed on as a value: Qt reads the C++ QPlaceIcon, which stays Python's
      own.
    """
    #  bool operator==(const QPlaceIcon &lhs, const QPlaceIcon &rhs)
    return Rituals.call(
        'ritual_ZeqRK10QPlaceIconS1_',
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
  def __ne__(self, rhs: QPlaceIcon) -> bool:
    """
    Calls Qt's 'bool operator!=(const QPlaceIcon &lhs, const QPlaceIcon
    &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaceicon.html#operator!=

    Parameters
    ----------

    rhs : QPlaceIcon
      Passed on as a value: Qt reads the C++ QPlaceIcon, which stays Python's
      own.
    """
    #  bool operator!=(const QPlaceIcon &lhs, const QPlaceIcon &rhs)
    return Rituals.call(
        'ritual_ZneRK10QPlaceIconS1_',
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
    Notes what was given, for Qt's 'QPlaceIcon::QPlaceIcon()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qplaceicon.html#QPlaceIcon
    """
    #  QPlaceIcon::QPlaceIcon()
    self._noteCreation(QPlaceIcon, lambda: Rituals.call(
        'ritual_ZN10QPlaceIconC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QPlaceIcon) -> None:
    """
    Notes what was given, for Qt's 'QPlaceIcon::QPlaceIcon(const QPlaceIcon
    &other)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qplaceicon.html#QPlaceIcon

    Parameters
    ----------

    other : QPlaceIcon
      Passed on as a value: Qt reads the C++ QPlaceIcon, which stays Python's
      own.
    """
    #  QPlaceIcon::QPlaceIcon(const QPlaceIcon &other)
    self._noteCreation(QPlaceIcon, lambda: Rituals.call(
        'ritual_ZN10QPlaceIconC1ERKS_', self._valueOf(other),
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
    Qt's 'void QPlaceIcon::swap(QPlaceIcon &other)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPlaceIcon.swap' has no cute function yet. Qt's 'void "
        "QPlaceIcon::swap(QPlaceIcon &other)': takes a type Python has no "
        "way to hand over yet.")
