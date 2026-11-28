"""
QQmlAbstractColumnModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLabsQmlModels/6.12.0/QtLabsQmlModels/private/qqmlabstractcolumnmodel_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQmlAbstractColumnModel to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import Qt, QHash

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QLatin1String, QMetaObject, QModelIndex
  from ..QtCore import QObject, QVariant
  from ..QtQml import QJSValue
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QJSValue = WAIT['QJSValue']
  QLatin1String = WAIT['QLatin1String']
  QModelIndex = WAIT['QModelIndex']
  QObject = WAIT['QObject']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlAbstractColumnModel(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlAbstractColumnModel: a plain Python object
  standing in front of one C++ QQmlAbstractColumnModel.

  What exists
  -----------

  Every function of Qt's QQmlAbstractColumnModel that has a ritual and that
  Python can call so far, 17 names in all: 'metaObject', 'tr', 'data',
  'setData', 'roleNames', 'flags', 'columnCountChanged', 'rowsChanged',
  'classBegin', 'componentComplete', 'firstRow', 'setInitialRows',
  'dataPrivate', 'setDataPrivate', 'fetchColumnMetadata', 'validateRowType',
  'jsTypeName'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlAbstractColumnModel::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQmlAbstractColumnModel::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QQmlAbstractColumnModel::qt_qmlMarker_anonymous()': one of
    Qt's own inner workings.
  - Qt's 'QQmlAbstractColumnModel::~QQmlAbstractColumnModel()': the
    destructor: Python never removes a C++ QQmlAbstractColumnModel.
  - Qt's 'QQmlListProperty<QQmlTableModelColumn>
    QQmlAbstractColumnModel::columns()': gives a type Python has no way to
    take yet.
  - Qt's 'void QQmlAbstractColumnModel::columns_append(
    QQmlListProperty<QQmlTableModelColumn> *property, QQmlTableModelColumn
    *value)': names 'QQmlListProperty<QQmlTableModelColumn>', which has no
    cute class yet.
  - Qt's 'qsizetype QQmlAbstractColumnModel::columns_count(
    QQmlListProperty<QQmlTableModelColumn> *property)': names
    'QQmlListProperty<QQmlTableModelColumn>', which has no cute class yet.
  - Qt's 'QQmlTableModelColumn *QQmlAbstractColumnModel::columns_at(
    QQmlListProperty<QQmlTableModelColumn> *property, qsizetype index)':
    names 'QQmlListProperty<QQmlTableModelColumn>', which has no cute class
    yet.
  - Qt's 'void QQmlAbstractColumnModel::columns_clear(
    QQmlListProperty<QQmlTableModelColumn> *property)': names
    'QQmlListProperty<QQmlTableModelColumn>', which has no cute class yet.
  - Qt's 'void QQmlAbstractColumnModel::columns_replace(
    QQmlListProperty<QQmlTableModelColumn> *property, qsizetype index,
    QQmlTableModelColumn *value)': names
    'QQmlListProperty<QQmlTableModelColumn>', which has no cute class yet.
  - Qt's 'void QQmlAbstractColumnModel::columns_removeLast(
    QQmlListProperty<QQmlTableModelColumn> *property)': names
    'QQmlListProperty<QQmlTableModelColumn>', which has no cute class yet.
  - Qt's 'ColumnRoleMetadata
    QQmlAbstractColumnModel::fetchColumnRoleData(const QString &roleNameKey,
    QQmlTableModelColumn *tableModelColumn, int columnIndex) const': gives a
    type Python has no way to take yet.
  - Qt's 'bool QQmlAbstractColumnModel::validateNewRow(QLatin1StringView
    functionName, const QVariant &row, NewRowOperationFlag operation) const':
    names the enum 'QQmlAbstractColumnModel::NewRowOperationFlag', whose
    class cannot be named here.
  - Qt's 'std::optional<QVariantList>
    QQmlAbstractColumnModel::validateRowsArgument(const QVariant &rows)
    const': gives a type Python has no way to take yet.

  What has no ritual
  ------------------

  6 of the 40 functions Qt declares: 4 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ QQmlAbstractColumnModel is created at the first use, not by
    'QQmlAbstractColumnModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlAbstractColumnModel.
  - Qt tells when it has removed the C++ QQmlAbstractColumnModel. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQmlAbstractColumnModel that has no cute function yet,
    'columns', 'columns_append', 'columns_at', 'columns_clear',
    'columns_count', 'columns_removeLast', 'columns_replace',
    'fetchColumnRoleData', 'validateNewRow', 'validateRowsArgument', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

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
    Calls Qt's 'QString QQmlAbstractColumnModel::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlabstractcolumnmodel.html#tr

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
    #  QString QQmlAbstractColumnModel::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QQmlAbstractColumnModel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QJSValue)
  def jsTypeName(v: QJSValue) -> QLatin1String:
    """
    Calls Qt's 'QLatin1StringView QQmlAbstractColumnModel::jsTypeName(const
    QJSValue &v)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractcolumnmodel.html#jsTypeName

    Parameters
    ----------

    v : QJSValue
      Passed on as a value: Qt reads the C++ QJSValue, which stays Python's
      own.

    Returns
    -------

    QLatin1String
      A new cute QLatin1String around the copy Qt gave back. Python owns it.
    """
    #  QLatin1StringView QQmlAbstractColumnModel::jsTypeName(const QJSValue
    #      &v)
    address = Rituals.call(
        'ritual_ZN23QQmlAbstractColumnModel10jsTypeNameERK8QJSValue',
        CuteMixin._valueOf(v),
    )
    from ..QtCore import QLatin1String
    return QLatin1String._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlAbstractColumnModel'

  #  A C++ QQmlAbstractColumnModel Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlAbstractColumnModel'

  #  The functions Qt calls itself that QQmlAbstractColumnModel is the first
  #  to declare and that cannot be handed to Python yet, each as Qt declares
  #  it. A class of a program that writes one of them anew is refused, since
  #  Qt would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'validateNewRow': (
          'bool QQmlAbstractColumnModel::validateNewRow(QLatin1StringView, '
          'const QVariant &, NewRowOperationFlag) const',
      ),
  }

  #  The functions Qt calls itself that QQmlAbstractColumnModel is the first
  #  to declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'firstRow': (
          ('_ZNK23QQmlAbstractColumnModel8firstRowEv',
           ('address', 'value', 'QtCore:QVariant'),
           ()),
      ),
      'setInitialRows': (
          ('_ZN23QQmlAbstractColumnModel14setInitialRowsEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'dataPrivate': (
          ('_ZNK23QQmlAbstractColumnModel11dataPrivateERK11QModelIndexRK7QS'
           'tring',
           ('address', 'value', 'QtCore:QVariant'),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
               ('address', 'text', ''),
           )),
      ),
      'setDataPrivate': (
          ('_ZN23QQmlAbstractColumnModel14setDataPrivateERK11QModelIndexRK7'
           'QString8QVariant',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtCore:QModelIndex'),
               ('address', 'text', ''),
               ('address', 'value', 'QtCore:QVariant'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlAbstractColumnModel::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractcolumnmodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlAbstractColumnModel::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QQmlAbstractColumnModel10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QModelIndex, str)
  def data(self, index: QModelIndex, role: str) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlAbstractColumnModel::data(const QModelIndex
    &index, const QString &role) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlabstractcolumnmodel.html#data

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    role : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlAbstractColumnModel::data(const QModelIndex &index, const
    #      QString &role) const
    address = self.uglySide.call(
        'ritual_ZNK23QQmlAbstractColumnModel4dataERK11QModelIndexRK7QString',
        self._valueOf(index), role,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QModelIndex)
  @overload(QModelIndex, int)
  def data(self, index: QModelIndex, role: int = 0) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlAbstractColumnModel::data(const QModelIndex
    &index, int role) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlabstractcolumnmodel.html#data

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    role : int
      Passed on as it is. May be left out, as in Qt: it is then 0.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlAbstractColumnModel::data(const QModelIndex &index, int
    #      role) const
    ritual = 'ritual_ZNK23QQmlAbstractColumnModel4dataERK11QModelIndexi'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK23QQmlAbstractColumnModel4dataERK11QModelIndexi')
    address = self.uglySide.call(ritual, self._valueOf(index), role)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def roleNames(self) -> QHash[int, QByteArray]:
    """
    Calls Qt's 'QHash<int, QByteArray> QQmlAbstractColumnModel::roleNames()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractcolumnmodel.html#roleNames

    Returns
    -------

    QHash[int, QByteArray]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QHash<int, QByteArray> QQmlAbstractColumnModel::roleNames() const
    address = self.uglySide.call(
        'ritual_ZNK23QQmlAbstractColumnModel9roleNamesEv',
    )
    from ..QtCore import QByteArray
    return QHash[int, QByteArray]._cuteOwning(address)

  @overload(QModelIndex)
  def flags(self, index: QModelIndex) -> Qt.ItemFlags:
    """
    Calls Qt's 'Qt::ItemFlags QQmlAbstractColumnModel::flags(const
    QModelIndex &index) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlabstractcolumnmodel.html#flags

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    Returns
    -------

    Qt.ItemFlags
      The value standing for the combination Qt gave back.
    """
    #  Qt::ItemFlags QQmlAbstractColumnModel::flags(const QModelIndex &index)
    #      const
    ritual = 'ritual_ZNK23QQmlAbstractColumnModel5flagsERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK23QQmlAbstractColumnModel5flagsERK11QModelIndex')
    return Qt.ItemFlags(self.uglySide.call(ritual, self._valueOf(index)))

  def firstRow(self) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlAbstractColumnModel::firstRow() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractcolumnmodel.html#firstRow

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlAbstractColumnModel::firstRow() const
    address = self.uglySide.call(
        'ritual_ZNK23QQmlAbstractColumnModel8firstRowEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QModelIndex, str)
  def dataPrivate(self, index: QModelIndex, roleName: str) -> QVariant:
    """
    Calls Qt's 'QVariant QQmlAbstractColumnModel::dataPrivate(const
    QModelIndex &index, const QString &roleName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractcolumnmodel.html#dataPrivate

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    roleName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QQmlAbstractColumnModel::dataPrivate(const QModelIndex
    #      &index, const QString &roleName) const
    address = self.uglySide.call(
        'ritual_ZNK23QQmlAbstractColumnModel11dataPrivateERK11QModelIndexRK'
        '7QString',
        self._valueOf(index), roleName,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  @overload(QLatin1String, QVariant)
  def validateRowType(
      self,
      functionName: QLatin1String,
      row: QVariant,
  ) -> bool:
    """
    Calls Qt's 'bool
    QQmlAbstractColumnModel::validateRowType(QLatin1StringView functionName,
    const QVariant &row) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractcolumnmodel.html#validateRowType

    Parameters
    ----------

    functionName : QLatin1String
      Passed on as a value: Qt reads the C++ QLatin1String, which stays
      Python's own.

    row : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  bool QQmlAbstractColumnModel::validateRowType(QLatin1StringView
    #      functionName, const QVariant &row) const
    return self.uglySide.call(
        'ritual_ZNK23QQmlAbstractColumnModel15validateRowTypeE13QLatin1Stri'
        'ngRK8QVariant',
        self._valueOf(functionName), self._valueOf(row),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QModelIndex, QVariant, str)
  def setData(self, index: QModelIndex, value: QVariant, role: str) -> bool:
    """
    Calls Qt's 'bool QQmlAbstractColumnModel::setData(const QModelIndex
    &index, const QVariant &value, const QString &role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractcolumnmodel.html#setData

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    role : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QQmlAbstractColumnModel::setData(const QModelIndex &index, const
    #      QVariant &value, const QString &role)
    return self.uglySide.call(
        'ritual_ZN23QQmlAbstractColumnModel7setDataERK11QModelIndexRK8QVari'
        'antRK7QString',
        self._valueOf(index), self._valueOf(value), role,
    )

  @overload(QModelIndex, QVariant)
  @overload(QModelIndex, QVariant, int)
  def setData(
      self,
      index: QModelIndex,
      value: QVariant,
      role: int = 0,
  ) -> bool:
    """
    Calls Qt's 'bool QQmlAbstractColumnModel::setData(const QModelIndex
    &index, const QVariant &value, int role)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractcolumnmodel.html#setData

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    role : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  bool QQmlAbstractColumnModel::setData(const QModelIndex &index, const
    #      QVariant &value, int role)
    ritual = (
        'ritual_ZN23QQmlAbstractColumnModel7setDataERK11QModelIndexRK8QVari'
        'anti')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN23QQmlAbstractColumnModel7setDataERK11QModelIndexRK'
          '8QVarianti')
    return self.uglySide.call(
        ritual, self._valueOf(index), self._valueOf(value), role,
    )

  def setInitialRows(self) -> None:
    """
    Calls Qt's 'void QQmlAbstractColumnModel::setInitialRows()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractcolumnmodel.html#setInitialRows
    """
    #  void QQmlAbstractColumnModel::setInitialRows()
    self.uglySide.call(
        'ritual_ZN23QQmlAbstractColumnModel14setInitialRowsEv',
    )

  @overload(QModelIndex, str, QVariant)
  def setDataPrivate(
      self,
      index: QModelIndex,
      roleName: str,
      value: QVariant,
  ) -> None:
    """
    Calls Qt's 'void QQmlAbstractColumnModel::setDataPrivate(const
    QModelIndex &index, const QString &roleName, QVariant value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractcolumnmodel.html#setDataPrivate

    Parameters
    ----------

    index : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.

    roleName : str
      Passed on as it is: a QString is made of it for the call.

    value : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QQmlAbstractColumnModel::setDataPrivate(const QModelIndex &index,
    #      const QString &roleName, QVariant value)
    self.uglySide.call(
        'ritual_ZN23QQmlAbstractColumnModel14setDataPrivateERK11QModelIndex'
        'RK7QString8QVariant',
        self._valueOf(index), roleName, self._valueOf(value),
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
    Notes what was given, for Qt's
    'QQmlAbstractColumnModel::QQmlAbstractColumnModel(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractcolumnmodel.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlAbstractColumnModel::QQmlAbstractColumnModel(QObject *parent)
    self._noteCreation(QQmlAbstractColumnModel, lambda: Rituals.call(
        'ritual_ZN23QQmlAbstractColumnModelC1EP7QObject',
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

  def columnCountChanged(self) -> None:
    """
    Calls Qt's 'void QQmlAbstractColumnModel::columnCountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractcolumnmodel.html#columnCountChanged
    """
    #  void QQmlAbstractColumnModel::columnCountChanged()
    self.uglySide.call(
        'ritual_ZN23QQmlAbstractColumnModel18columnCountChangedEv',
    )

  def rowsChanged(self) -> None:
    """
    Calls Qt's 'void QQmlAbstractColumnModel::rowsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractcolumnmodel.html#rowsChanged
    """
    #  void QQmlAbstractColumnModel::rowsChanged()
    self.uglySide.call('ritual_ZN23QQmlAbstractColumnModel11rowsChangedEv')

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QQmlAbstractColumnModel::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractcolumnmodel.html#classBegin
    """
    #  void QQmlAbstractColumnModel::classBegin()
    ritual = 'ritual_ZN23QQmlAbstractColumnModel10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QQmlAbstractColumnModel10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QQmlAbstractColumnModel::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractcolumnmodel.html#componentComplete
    """
    #  void QQmlAbstractColumnModel::componentComplete()
    ritual = 'ritual_ZN23QQmlAbstractColumnModel17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN23QQmlAbstractColumnModel17componentCompleteEv'
    self.uglySide.call(ritual)

  def fetchColumnMetadata(self) -> None:
    """
    Calls Qt's 'void QQmlAbstractColumnModel::fetchColumnMetadata()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlabstractcolumnmodel.html#fetchColumnMetadata
    """
    #  void QQmlAbstractColumnModel::fetchColumnMetadata()
    self.uglySide.call(
        'ritual_ZN23QQmlAbstractColumnModel19fetchColumnMetadataEv',
    )

  @staticmethod
  def columns(*__, **_) -> Never:
    """
    Qt's 'QQmlListProperty<QQmlTableModelColumn>
    QQmlAbstractColumnModel::columns()': gives a type Python has no way to
    take yet.
    """
    raise NotImplementedError(
        "'QQmlAbstractColumnModel.columns' has no cute function yet. Qt's "
        "'QQmlListProperty<QQmlTableModelColumn> "
        "QQmlAbstractColumnModel::columns()': gives a type Python has no "
        "way to take yet.")

  @staticmethod
  def columns_append(*__, **_) -> Never:
    """
    Qt's 'void QQmlAbstractColumnModel::columns_append(
    QQmlListProperty<QQmlTableModelColumn> *property, QQmlTableModelColumn
    *value)': names 'QQmlListProperty<QQmlTableModelColumn>', which has no
    cute class yet.
    """
    raise NotImplementedError(
        "'QQmlAbstractColumnModel.columns_append' has no cute function yet. "
        "Qt's 'void "
        "QQmlAbstractColumnModel::columns_append(QQmlListProperty<QQmlTableM"
        "odelColumn> *property, QQmlTableModelColumn *value)': names "
        "'QQmlListProperty<QQmlTableModelColumn>', which has no cute class "
        "yet.")

  @staticmethod
  def columns_at(*__, **_) -> Never:
    """
    Qt's 'QQmlTableModelColumn *QQmlAbstractColumnModel::columns_at(
    QQmlListProperty<QQmlTableModelColumn> *property, qsizetype index)':
    names 'QQmlListProperty<QQmlTableModelColumn>', which has no cute class
    yet.
    """
    raise NotImplementedError(
        "'QQmlAbstractColumnModel.columns_at' has no cute function yet. "
        "Qt's 'QQmlTableModelColumn "
        "*QQmlAbstractColumnModel::columns_at(QQmlListProperty<QQmlTableMode"
        "lColumn> *property, qsizetype index)': names "
        "'QQmlListProperty<QQmlTableModelColumn>', which has no cute class "
        "yet.")

  @staticmethod
  def columns_clear(*__, **_) -> Never:
    """
    Qt's 'void QQmlAbstractColumnModel::columns_clear(
    QQmlListProperty<QQmlTableModelColumn> *property)': names
    'QQmlListProperty<QQmlTableModelColumn>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlAbstractColumnModel.columns_clear' has no cute function yet. "
        "Qt's 'void "
        "QQmlAbstractColumnModel::columns_clear(QQmlListProperty<QQmlTableMo"
        "delColumn> *property)': names "
        "'QQmlListProperty<QQmlTableModelColumn>', which has no cute class "
        "yet.")

  @staticmethod
  def columns_count(*__, **_) -> Never:
    """
    Qt's 'qsizetype QQmlAbstractColumnModel::columns_count(
    QQmlListProperty<QQmlTableModelColumn> *property)': names
    'QQmlListProperty<QQmlTableModelColumn>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlAbstractColumnModel.columns_count' has no cute function yet. "
        "Qt's 'qsizetype "
        "QQmlAbstractColumnModel::columns_count(QQmlListProperty<QQmlTableMo"
        "delColumn> *property)': names "
        "'QQmlListProperty<QQmlTableModelColumn>', which has no cute class "
        "yet.")

  @staticmethod
  def columns_removeLast(*__, **_) -> Never:
    """
    Qt's 'void QQmlAbstractColumnModel::columns_removeLast(
    QQmlListProperty<QQmlTableModelColumn> *property)': names
    'QQmlListProperty<QQmlTableModelColumn>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlAbstractColumnModel.columns_removeLast' has no cute function "
        "yet. Qt's 'void "
        "QQmlAbstractColumnModel::columns_removeLast(QQmlListProperty<QQmlTa"
        "bleModelColumn> *property)': names "
        "'QQmlListProperty<QQmlTableModelColumn>', which has no cute class "
        "yet.")

  @staticmethod
  def columns_replace(*__, **_) -> Never:
    """
    Qt's 'void QQmlAbstractColumnModel::columns_replace(
    QQmlListProperty<QQmlTableModelColumn> *property, qsizetype index,
    QQmlTableModelColumn *value)': names
    'QQmlListProperty<QQmlTableModelColumn>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QQmlAbstractColumnModel.columns_replace' has no cute function "
        "yet. Qt's 'void "
        "QQmlAbstractColumnModel::columns_replace(QQmlListProperty<QQmlTable"
        "ModelColumn> *property, qsizetype index, QQmlTableModelColumn "
        "*value)': names 'QQmlListProperty<QQmlTableModelColumn>', which "
        "has no cute class yet.")

  @staticmethod
  def fetchColumnRoleData(*__, **_) -> Never:
    """
    Qt's 'ColumnRoleMetadata
    QQmlAbstractColumnModel::fetchColumnRoleData(const QString &roleNameKey,
    QQmlTableModelColumn *tableModelColumn, int columnIndex) const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlAbstractColumnModel.fetchColumnRoleData' has no cute function "
        "yet. Qt's 'ColumnRoleMetadata "
        "QQmlAbstractColumnModel::fetchColumnRoleData(const QString "
        "&roleNameKey, QQmlTableModelColumn *tableModelColumn, int "
        "columnIndex) const': gives a type Python has no way to take yet.")

  @staticmethod
  def validateNewRow(*__, **_) -> Never:
    """
    Qt's 'bool QQmlAbstractColumnModel::validateNewRow(QLatin1StringView
    functionName, const QVariant &row, NewRowOperationFlag operation) const':
    names the enum 'QQmlAbstractColumnModel::NewRowOperationFlag', whose
    class cannot be named here.
    """
    raise NotImplementedError(
        "'QQmlAbstractColumnModel.validateNewRow' has no cute function yet. "
        "Qt's 'bool "
        "QQmlAbstractColumnModel::validateNewRow(QLatin1StringView "
        "functionName, const QVariant &row, NewRowOperationFlag operation) "
        "const': names the enum "
        "'QQmlAbstractColumnModel::NewRowOperationFlag', whose class cannot "
        "be named here.")

  @staticmethod
  def validateRowsArgument(*__, **_) -> Never:
    """
    Qt's 'std::optional<QVariantList>
    QQmlAbstractColumnModel::validateRowsArgument(const QVariant &rows)
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlAbstractColumnModel.validateRowsArgument' has no cute "
        "function yet. Qt's 'std::optional<QVariantList> "
        "QQmlAbstractColumnModel::validateRowsArgument(const QVariant "
        "&rows) const': gives a type Python has no way to take yet.")
