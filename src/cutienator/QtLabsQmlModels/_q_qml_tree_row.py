"""
QQmlTreeRow binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsQmlModels/6.12.0/QtLabsQmlModels/private/qqmltreerow_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQmlTreeRow to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QMap

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QVariant
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlTreeRow(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlTreeRow: a plain Python object standing in front
  of one C++ QQmlTreeRow.

  C++ hands a QQmlTreeRow around as a copy, so every C++ QQmlTreeRow behind a
  cute one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QQmlTreeRow that has a ritual and that Python can
  call so far, 12 names in all: 'parent', 'setParent', 'getRow', 'addChild',
  'rowCount', 'subTreeSize', 'data', 'removeChildAt', 'setData', 'setField',
  'toVariant', 'unpackVariantMap'. It can be made from Python, in 3 ways; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const std::vector<std::unique_ptr<QQmlTreeRow>>
    &QQmlTreeRow::children() const': gives a type Python has no way to take
    yet.
  - Qt's 'void
    QQmlTreeRow::removeChild(std::vector<std::unique_ptr<QQmlTreeRow>>::
    const_iterator &child)': takes a type Python has no way to hand over yet.
  - Qt's 'std::unique_ptr<QQmlTreeRow> QQmlTreeRow::takeChild(int i)': gives
    a type Python has no way to take yet.
  - Qt's 'QQmlTreeRow::~QQmlTreeRow()': the destructor: Python removes its
    C++ QQmlTreeRow by it, and has no other use for it.

  What has no ritual
  ------------------

  1 of the 22 functions Qt declares: 1 the compiler refuses its ritual as it
  would be written here.

  What to expect
  --------------

  - The C++ QQmlTreeRow is created at the first use, not by
    'QQmlTreeRow(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlTreeRow back gives a copy the ritual made for
    Python, in a new cute QQmlTreeRow.
  - Each name of Qt's QQmlTreeRow that has no cute function yet, 'children',
    'insertChild', 'removeChild', 'takeChild', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlTreeRow'

  #  Qt's '~QQmlTreeRow()'. Naming it makes this a value class: Python owns
  #  every C++ QQmlTreeRow behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN11QQmlTreeRowD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def parent(self) -> Optional[QQmlTreeRow]:
    """
    Calls Qt's 'QQmlTreeRow *QQmlTreeRow::parent() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltreerow.html#parent

    Returns
    -------

    Optional[QQmlTreeRow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlTreeRow *QQmlTreeRow::parent() const
    address = self.uglySide.call('ritual_ZNK11QQmlTreeRow6parentEv')
    return QQmlTreeRow._cuteAt(address)

  @overload(int)
  def getRow(self, i: int) -> Optional[QQmlTreeRow]:
    """
    Calls Qt's 'const QQmlTreeRow *QQmlTreeRow::getRow(int i) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltreerow.html#getRow

    Parameters
    ----------

    i : int
      Passed on as it is.

    Returns
    -------

    Optional[QQmlTreeRow]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QQmlTreeRow *QQmlTreeRow::getRow(int i) const
    address = self.uglySide.call('ritual_ZNK11QQmlTreeRow6getRowEi', i)
    return QQmlTreeRow._cuteAt(address)

  def rowCount(self) -> int:
    """
    Calls Qt's 'size_t QQmlTreeRow::rowCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltreerow.html#rowCount
    """
    #  size_t QQmlTreeRow::rowCount() const
    return self.uglySide.call('ritual_ZNK11QQmlTreeRow8rowCountEv')

  def subTreeSize(self) -> int:
    """
    Calls Qt's 'int QQmlTreeRow::subTreeSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltreerow.html#subTreeSize
    """
    #  int QQmlTreeRow::subTreeSize() const
    return self.uglySide.call('ritual_ZNK11QQmlTreeRow11subTreeSizeEv')

  @overload()
  def data(self) -> QMap[str, QVariant]:
    """
    Calls Qt's 'QVariantMap QQmlTreeRow::data() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltreerow.html#data

    Returns
    -------

    QMap[str, QVariant]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QVariantMap QQmlTreeRow::data() const
    address = self.uglySide.call('ritual_ZNK11QQmlTreeRow4dataEv')
    from ..QtCore import QVariant
    return QMap[str, QVariant]._cuteOwning(address)

  @overload(str)
  def data(self, key: str) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlTreeRow::data(const QString &key) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltreerow.html#data

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlTreeRow::data(const QString &key) const
    address = self.uglySide.call(
        'ritual_ZNK11QQmlTreeRow4dataERK7QString', key,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def toVariant(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlTreeRow::toVariant() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltreerow.html#toVariant

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlTreeRow::toVariant() const
    address = self.uglySide.call('ritual_ZNK11QQmlTreeRow9toVariantEv')
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  @overload(NoneType)
  def setParent(self, parent: Optional[QQmlTreeRow]) -> None:
    """
    Calls Qt's 'void QQmlTreeRow::setParent(QQmlTreeRow *parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltreerow.html#setParent

    Parameters
    ----------

    parent : Optional[QQmlTreeRow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlTreeRow::setParent(QQmlTreeRow *parent)
    self.uglySide.call(
        'ritual_ZN11QQmlTreeRow9setParentEPS_', self._addressOf(parent),
    )

  @overload(QVariant)
  def setData(self, data: QVariant) -> None:
    """
    Calls Qt's 'void QQmlTreeRow::setData(const QVariant &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltreerow.html#setData

    Parameters
    ----------

    data : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQmlTreeRow::setData(const QVariant &data)
    self.uglySide.call(
        'ritual_ZN11QQmlTreeRow7setDataERK8QVariant', self._valueOf(data),
    )

  @overload(QMap[str, QVariant])
  def setData(self, data: QMap[str, QVariant]) -> None:
    """
    Calls Qt's 'void QQmlTreeRow::setData(const QVariantMap &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltreerow.html#setData

    Parameters
    ----------

    data : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void QQmlTreeRow::setData(const QVariantMap &data)
    self.uglySide.call(
        'ritual_ZN11QQmlTreeRow7setDataERK4QMapI7QString8QVariantE',
        self._valueOf(data),
    )

  @overload(str, QVariant)
  def setField(self, key: str, value: QVariant) -> None:
    """
    Calls Qt's 'void QQmlTreeRow::setField(const QString &key, const QVariant
    &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltreerow.html#setField

    Parameters
    ----------

    key : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQmlTreeRow::setField(const QString &key, const QVariant &value)
    self.uglySide.call(
        'ritual_ZN11QQmlTreeRow8setFieldERK7QStringRK8QVariant',
        key, self._valueOf(value),
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
  @overload(THIS)
  @overload(NoneType)
  def __init__(self, parentItem: Optional[QQmlTreeRow] = None) -> None:
    """
    Notes what was given, for Qt's 'QQmlTreeRow::QQmlTreeRow(QQmlTreeRow
    *parentItem)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmltreerow.html#QQmlTreeRow

    Parameters
    ----------

    parentItem : Optional[QQmlTreeRow]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlTreeRow::QQmlTreeRow(QQmlTreeRow *parentItem)
    self._noteCreation(QQmlTreeRow, lambda: Rituals.call(
        'ritual_ZN11QQmlTreeRowC1EPS_', self._addressOf(parentItem),
    ))

  @overload(QVariant)
  @overload(QVariant, THIS)
  @overload(QVariant, NoneType)
  def __init__(
      self,
      data: QVariant,
      parentItem: Optional[QQmlTreeRow] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QQmlTreeRow::QQmlTreeRow(const QVariant
    &data, QQmlTreeRow *parentItem)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmltreerow.html#QQmlTreeRow

    Parameters
    ----------

    data : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    parentItem : Optional[QQmlTreeRow]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlTreeRow::QQmlTreeRow(const QVariant &data, QQmlTreeRow
    #      *parentItem)
    self._noteCreation(QQmlTreeRow, lambda: Rituals.call(
        'ritual_ZN11QQmlTreeRowC1ERK8QVariantPS_',
        self._valueOf(data), self._addressOf(parentItem),
    ))

  @overload(QMap[str, QVariant])
  @overload(QMap[str, QVariant], THIS)
  @overload(QMap[str, QVariant], NoneType)
  def __init__(
      self,
      data: QMap[str, QVariant],
      parentItem: Optional[QQmlTreeRow] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QQmlTreeRow::QQmlTreeRow(const
    QVariantMap &data, QQmlTreeRow *parentItem)', which is called at the
    first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmltreerow.html#QQmlTreeRow

    Parameters
    ----------

    data : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    parentItem : Optional[QQmlTreeRow]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlTreeRow::QQmlTreeRow(const QVariantMap &data, QQmlTreeRow
    #      *parentItem)
    self._noteCreation(QQmlTreeRow, lambda: Rituals.call(
        'ritual_ZN11QQmlTreeRowC1ERK4QMapI7QString8QVariantEPS_',
        self._valueOf(data), self._addressOf(parentItem),
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

  @overload(THIS)
  @overload(NoneType)
  def addChild(self, child: Optional[QQmlTreeRow]) -> None:
    """
    Calls Qt's 'void QQmlTreeRow::addChild(QQmlTreeRow *child)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltreerow.html#addChild

    Parameters
    ----------

    child : Optional[QQmlTreeRow]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlTreeRow::addChild(QQmlTreeRow *child)
    self.uglySide.call(
        'ritual_ZN11QQmlTreeRow8addChildEPS_', self._addressOf(child),
    )

  @overload(int)
  def removeChildAt(self, i: int) -> None:
    """
    Calls Qt's 'void QQmlTreeRow::removeChildAt(int i)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltreerow.html#removeChildAt

    Parameters
    ----------

    i : int
      Passed on as it is.
    """
    #  void QQmlTreeRow::removeChildAt(int i)
    self.uglySide.call('ritual_ZN11QQmlTreeRow13removeChildAtEi', i)

  @overload(QMap[str, QVariant])
  def unpackVariantMap(self, dataMap: QMap[str, QVariant]) -> None:
    """
    Calls Qt's 'void QQmlTreeRow::unpackVariantMap(const QVariantMap
    &dataMap)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmltreerow.html#unpackVariantMap

    Parameters
    ----------

    dataMap : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void QQmlTreeRow::unpackVariantMap(const QVariantMap &dataMap)
    self.uglySide.call(
        'ritual_ZN11QQmlTreeRow16unpackVariantMapERK4QMapI7QString8QVariant'
        'E',
        self._valueOf(dataMap),
    )

  @staticmethod
  def children(*__, **_) -> Never:
    """
    Qt's 'const std::vector<std::unique_ptr<QQmlTreeRow>>
    &QQmlTreeRow::children() const': gives a type Python has no way to take
    yet.
    """
    raise NotImplementedError(
        "'QQmlTreeRow.children' has no cute function yet. Qt's 'const "
        "std::vector<std::unique_ptr<QQmlTreeRow>> &QQmlTreeRow::children() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def insertChild(*__, **_) -> Never:
    """
    Qt's 'void QQmlTreeRow::insertChild(int index,
    std::unique_ptr<QQmlTreeRow> child)': the compiler refuses its ritual as
    it would be written here: call to deleted constructor of
    'std::unique_ptr<QQmlTreeRow>'.
    """
    raise NotImplementedError(
        "'QQmlTreeRow.insertChild' has no cute function yet. Qt's 'void "
        "QQmlTreeRow::insertChild(int index, std::unique_ptr<QQmlTreeRow> "
        "child)': the compiler refuses its ritual as it would be written "
        "here: call to deleted constructor of "
        "'std::unique_ptr<QQmlTreeRow>'.")

  @staticmethod
  def removeChild(*__, **_) -> Never:
    """
    Qt's 'void
    QQmlTreeRow::removeChild(std::vector<std::unique_ptr<QQmlTreeRow>>::
    const_iterator &child)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlTreeRow.removeChild' has no cute function yet. Qt's 'void "
        "QQmlTreeRow::removeChild(std::vector<std::unique_ptr<QQmlTreeRow>>:"
        ":const_iterator &child)': takes a type Python has no way to hand "
        "over yet.")

  @staticmethod
  def takeChild(*__, **_) -> Never:
    """
    Qt's 'std::unique_ptr<QQmlTreeRow> QQmlTreeRow::takeChild(int i)': gives
    a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlTreeRow.takeChild' has no cute function yet. Qt's "
        "'std::unique_ptr<QQmlTreeRow> QQmlTreeRow::takeChild(int i)': "
        "gives a type Python has no way to take yet.")
