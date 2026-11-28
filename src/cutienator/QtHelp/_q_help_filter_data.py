"""
QHelpFilterData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtHelp/qhelpfilterdata.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QVersionNumber
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVersionNumber = WAIT['QVersionNumber']


class QHelpFilterData(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QHelpFilterData: a plain Python object standing in
  front of one C++ QHelpFilterData.

  C++ hands a QHelpFilterData around as a copy, so every C++ QHelpFilterData
  behind a cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QHelpFilterData that has a ritual and that Python
  can call so far, 5 names in all: '__eq__', 'setComponents', 'setVersions',
  'components', 'versions'. It can be made from Python, in 2 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QHelpFilterData::QHelpFilterData(QHelpFilterData &&other)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QHelpFilterData::~QHelpFilterData()': the destructor: Python
    removes its C++ QHelpFilterData by it, and has no other use for it.
  - Qt's 'QHelpFilterData &QHelpFilterData::operator=(const QHelpFilterData
    &other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QHelpFilterData &QHelpFilterData::operator=(QHelpFilterData
    &&other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'void QHelpFilterData::swap(QHelpFilterData &other)': takes a type
    Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QHelpFilterData is created at the first use, not by
    'QHelpFilterData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QHelpFilterData back gives a copy the ritual made for
    Python, in a new cute QHelpFilterData.
  - Each name of Qt's QHelpFilterData that has no cute function yet, 'swap',
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
  __qt_class__ = 'QHelpFilterData'

  #  Qt's '~QHelpFilterData()'. Naming it makes this a value class: Python
  #  owns every C++ QHelpFilterData behind a cute one, and removes it by this
  #  ritual.
  __delete_ritual__ = 'ritual_ZN15QHelpFilterDataD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def components(self) -> QStringList:
    """
    Calls Qt's 'QStringList QHelpFilterData::components() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpfilterdata.html#components

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QHelpFilterData::components() const
    address = self.uglySide.call('ritual_ZNK15QHelpFilterData10componentsEv')
    return QStringList._cuteOwning(address)

  def versions(self) -> QList[QVersionNumber]:
    """
    Calls Qt's 'QList<QVersionNumber> QHelpFilterData::versions() const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpfilterdata.html#versions

    Returns
    -------

    QList[QVersionNumber]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QVersionNumber> QHelpFilterData::versions() const
    address = self.uglySide.call('ritual_ZNK15QHelpFilterData8versionsEv')
    from ..QtCore import QVersionNumber
    return QList[QVersionNumber]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QStringList)
  def setComponents(self, components: QStringList) -> None:
    """
    Calls Qt's 'void QHelpFilterData::setComponents(const QStringList
    &components)'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpfilterdata.html#setComponents

    Parameters
    ----------

    components : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QHelpFilterData::setComponents(const QStringList &components)
    self.uglySide.call(
        'ritual_ZN15QHelpFilterData13setComponentsERK5QListI7QStringE',
        self._valueOf(components),
    )

  @overload(QList[QVersionNumber])
  def setVersions(self, versions: QList[QVersionNumber]) -> None:
    """
    Calls Qt's 'void QHelpFilterData::setVersions(const QList<QVersionNumber>
    &versions)'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpfilterdata.html#setVersions

    Parameters
    ----------

    versions : QList[QVersionNumber]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QHelpFilterData::setVersions(const QList<QVersionNumber>
    #      &versions)
    self.uglySide.call(
        'ritual_ZN15QHelpFilterData11setVersionsERK5QListI14QVersionNumberE',
        self._valueOf(versions),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: QHelpFilterData) -> bool:
    """
    Calls Qt's 'bool QHelpFilterData::operator==(const QHelpFilterData
    &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qhelpfilterdata.html#operator==

    Parameters
    ----------

    other : QHelpFilterData
      Passed on as a value: Qt reads the C++ QHelpFilterData, which stays
      Python's own.
    """
    #  bool QHelpFilterData::operator==(const QHelpFilterData &other) const
    return self.uglySide.call(
        'ritual_ZNK15QHelpFilterDataeqERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
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
    Notes what was given, for Qt's 'QHelpFilterData::QHelpFilterData()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpfilterdata.html#QHelpFilterData
    """
    #  QHelpFilterData::QHelpFilterData()
    self._noteCreation(QHelpFilterData, lambda: Rituals.call(
        'ritual_ZN15QHelpFilterDataC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QHelpFilterData) -> None:
    """
    Notes what was given, for Qt's 'QHelpFilterData::QHelpFilterData(const
    QHelpFilterData &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhelpfilterdata.html#QHelpFilterData

    Parameters
    ----------

    other : QHelpFilterData
      Passed on as a value: Qt reads the C++ QHelpFilterData, which stays
      Python's own.
    """
    #  QHelpFilterData::QHelpFilterData(const QHelpFilterData &other)
    self._noteCreation(QHelpFilterData, lambda: Rituals.call(
        'ritual_ZN15QHelpFilterDataC1ERKS_', self._valueOf(other),
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
    Qt's 'void QHelpFilterData::swap(QHelpFilterData &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QHelpFilterData.swap' has no cute function yet. Qt's 'void "
        "QHelpFilterData::swap(QHelpFilterData &other)': takes a type "
        "Python has no way to hand over yet.")
