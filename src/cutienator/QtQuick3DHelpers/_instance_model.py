"""
InstanceModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DHelpers/6.12.0/QtQuick3DHelpers/private/instancerepeater_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means InstanceModel to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QAbstractListModel, QHash, QObject
from ..QtQuick3D import QQuick3DInstancing

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QMetaObject, QModelIndex, QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class InstanceModel(QAbstractListModel):
  """
  The cute side of Qt's InstanceModel: a plain Python object standing in
  front of one C++ InstanceModel.

  It is built on the cute 'QAbstractListModel', as Qt's InstanceModel is
  built on Qt's QAbstractListModel, and has everything that class has.

  What exists
  -----------

  Every function of Qt's InstanceModel that has a ritual and that Python can
  call so far, 11 names in all: 'metaObject', 'tr', 'data', 'rowCount',
  'instancing', 'setInstancing', 'instanceData', 'roleNames', 'reset',
  'instancingChanged', 'ensureTable'. It can be made from Python, in 1 way;
  see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *InstanceModel::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int InstanceModel::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  2 of the 16 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ InstanceModel is created at the first use, not by
    'InstanceModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ InstanceModel.
  - Qt tells when it has removed the C++ InstanceModel. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside InstanceModel, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Roles(CuteNum):
    """
    The enum 'InstanceModel::Roles' of Qt, with the 5 names Qt gives in it.
    """

    PositionRole = Kee[int](0)
    RotationRole = Kee[int](1)
    ScaleRole = Kee[int](2)
    ColorRole = Kee[int](3)
    CustomDataRole = Kee[int](4)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(str)
  @overload(NoneType)
  @overload(str, str)
  @overload(str, NoneType)
  @overload(NoneType, str)
  @overload(NoneType, NoneType)
  @overload(str, str, int)
  @overload(str, NoneType, int)
  @overload(NoneType, str, int)
  @overload(NoneType, NoneType, int)
  def tr(s: Optional[str], c: Optional[str] = None, n: int = -1) -> str:
    """
    Calls Qt's 'QString InstanceModel::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/instancemodel.html#tr

    Parameters
    ----------

    s : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text.

    c : Optional[str]
      Passed on as the bytes of the text. None is passed on as no text. May
      be left out, as in Qt: it is then None.

    n : int
      Passed on as it is. May be left out, as in Qt: it is then -1.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString InstanceModel::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13InstanceModel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'InstanceModel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *InstanceModel::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/instancemodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *InstanceModel::metaObject() const
    address = self.uglySide.call('ritual_ZNK13InstanceModel10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QModelIndex, int)
  def data(self, index: QModelIndex, role: int) -> QVariant:
    """
    Calls Qt's 'QVariant InstanceModel::data(const QModelIndex &index, int
    role) const'.

    Qt's own words: https://doc.qt.io/qt-6/instancemodel.html#data

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    role : int
      Passed on as it is.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant InstanceModel::data(const QModelIndex &index, int role) const
    ritual = 'ritual_ZNK13InstanceModel4dataERK11QModelIndexi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13InstanceModel4dataERK11QModelIndexi'
    address = self.uglySide.call(ritual, self._valueOf(index), role)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QModelIndex)
  def rowCount(self, parent: QModelIndex) -> int:
    """
    Calls Qt's 'int InstanceModel::rowCount(const QModelIndex &parent)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/instancemodel.html#rowCount

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  int InstanceModel::rowCount(const QModelIndex &parent) const
    ritual = 'ritual_ZNK13InstanceModel8rowCountERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK13InstanceModel8rowCountERK11QModelIndex'
    return self.uglySide.call(ritual, self._valueOf(parent))

  def instancing(self) -> Optional[QQuick3DInstancing]:
    """
    Calls Qt's 'QQuick3DInstancing *InstanceModel::instancing() const'.

    Qt's own words: https://doc.qt.io/qt-6/instancemodel.html#instancing

    Returns
    -------

    Optional[QQuick3DInstancing]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DInstancing *InstanceModel::instancing() const
    address = self.uglySide.call('ritual_ZNK13InstanceModel10instancingEv')
    return QQuick3DInstancing._cuteAt(address)

  @overload(int)
  def instanceData(
      self,
      index: int,
  ) -> Optional[QQuick3DInstancing.InstanceTableEntry]:
    """
    Calls Qt's 'const QQuick3DInstancing::InstanceTableEntry
    *InstanceModel::instanceData(int index) const'.

    Qt's own words: https://doc.qt.io/qt-6/instancemodel.html#instanceData

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    Optional[QQuick3DInstancing.InstanceTableEntry]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QQuick3DInstancing::InstanceTableEntry
    #      *InstanceModel::instanceData(int index) const
    address = self.uglySide.call(
        'ritual_ZNK13InstanceModel12instanceDataEi', index,
    )
    return QQuick3DInstancing.InstanceTableEntry._cuteAt(address)

  def roleNames(self) -> QHash[int, QByteArray]:
    """
    Calls Qt's 'QHash<int, QByteArray> InstanceModel::roleNames() const'.

    Qt's own words: https://doc.qt.io/qt-6/instancemodel.html#roleNames

    Returns
    -------

    QHash[int, QByteArray]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QHash<int, QByteArray> InstanceModel::roleNames() const
    address = self.uglySide.call('ritual_ZNK13InstanceModel9roleNamesEv')
    from ..QtCore import QByteArray
    return QHash[int, QByteArray]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQuick3DInstancing)
  @overload(NoneType)
  def setInstancing(self, instancing: Optional[QQuick3DInstancing]) -> None:
    """
    Calls Qt's 'void InstanceModel::setInstancing(QQuick3DInstancing
    *instancing)'.

    Qt's own words: https://doc.qt.io/qt-6/instancemodel.html#setInstancing

    Parameters
    ----------

    instancing : Optional[QQuick3DInstancing]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void InstanceModel::setInstancing(QQuick3DInstancing *instancing)
    self.uglySide.call(
        'ritual_ZN13InstanceModel13setInstancingEP18QQuick3DInstancing',
        self._addressOf(instancing),
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

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'InstanceModel::InstanceModel(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/instancemodel.html#InstanceModel

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  InstanceModel::InstanceModel(QObject *parent)
    self._noteCreation(InstanceModel, lambda: Rituals.call(
        'ritual_ZN13InstanceModelC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def reset(self) -> None:
    """
    Calls Qt's 'void InstanceModel::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/instancemodel.html#reset
    """
    #  void InstanceModel::reset()
    self.uglySide.call('ritual_ZN13InstanceModel5resetEv')

  def instancingChanged(self) -> None:
    """
    Calls Qt's 'void InstanceModel::instancingChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/instancemodel.html#instancingChanged
    """
    #  void InstanceModel::instancingChanged()
    self.uglySide.call('ritual_ZN13InstanceModel17instancingChangedEv')

  def ensureTable(self) -> None:
    """
    Calls Qt's 'void InstanceModel::ensureTable() const'.

    Qt's own words: https://doc.qt.io/qt-6/instancemodel.html#ensureTable
    """
    #  void InstanceModel::ensureTable() const
    self.uglySide.call('ritual_ZNK13InstanceModel11ensureTableEv')
