"""
QWebEngineHistoryModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtWebEngineCore/qwebenginehistory.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QAbstractListModel, QHash

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QMetaObject, QModelIndex, QVariant
  from . import QWebEngineHistoryModelPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']
  QWebEngineHistoryModelPrivate = WAIT['QWebEngineHistoryModelPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QWebEngineHistoryModel(QAbstractListModel):
  """
  The cute side of Qt's QWebEngineHistoryModel: a plain Python object
  standing in front of one C++ QWebEngineHistoryModel.

  It is built on the cute 'QAbstractListModel', as Qt's
  QWebEngineHistoryModel is built on Qt's QAbstractListModel, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QWebEngineHistoryModel that has a ritual and that
  Python can call so far, 7 names in all: 'metaObject', 'tr', 'rowCount',
  'data', 'roleNames', 'reset', 'd_func'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QWebEngineHistoryModel::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QWebEngineHistoryModel::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QWebEngineHistoryModel::~QWebEngineHistoryModel()': the destructor:
    Python never removes a C++ QWebEngineHistoryModel.
  - Qt's 'const QWebEngineHistoryModelPrivate
    *QWebEngineHistoryModel::d_func() const': takes in Python what
    'QWebEngineHistoryModelPrivate *QWebEngineHistoryModel::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 16 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QWebEngineHistoryModel is created at the first use, not by
    'QWebEngineHistoryModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QWebEngineHistoryModel.
  - Qt tells when it has removed the C++ QWebEngineHistoryModel. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QWebEngineHistoryModel, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class Roles(CuteNum):
    """
    The enum 'QWebEngineHistoryModel::Roles' of Qt, with the 4 names Qt gives
    in it.
    """

    UrlRole = Kee[int](256)
    TitleRole = Kee[int](257)
    OffsetRole = Kee[int](258)
    IconUrlRole = Kee[int](259)

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
    Calls Qt's 'QString QWebEngineHistoryModel::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginehistorymodel.html#tr

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
    #  QString QWebEngineHistoryModel::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN22QWebEngineHistoryModel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QWebEngineHistoryModel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QWebEngineHistoryModel::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginehistorymodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QWebEngineHistoryModel::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QWebEngineHistoryModel10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload()
  @overload(QModelIndex)
  def rowCount(self, parent: Optional[QModelIndex] = None) -> int:
    """
    Calls Qt's 'int QWebEngineHistoryModel::rowCount(const QModelIndex
    &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginehistorymodel.html#rowCount

    Parameters
    ----------

    parent : Optional[QModelIndex]
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own. May be left out, as in Qt: a new 'QModelIndex()' is then
      passed on.
    """
    #  int QWebEngineHistoryModel::rowCount(const QModelIndex &parent) const
    if parent is None:
      from ..QtCore import QModelIndex
      parent = QModelIndex()
    ritual = 'ritual_ZNK22QWebEngineHistoryModel8rowCountERK11QModelIndex'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK22QWebEngineHistoryModel8rowCountERK11QModelIndex')
    return self.uglySide.call(ritual, self._valueOf(parent))

  @overload(QModelIndex)
  @overload(QModelIndex, int)
  def data(self, index: QModelIndex, role: int = 0) -> QVariant:
    """
    Calls Qt's 'QVariant QWebEngineHistoryModel::data(const QModelIndex
    &index, int role) const'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginehistorymodel.html#data

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
    #  QVariant QWebEngineHistoryModel::data(const QModelIndex &index, int
    #      role) const
    ritual = 'ritual_ZNK22QWebEngineHistoryModel4dataERK11QModelIndexi'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK22QWebEngineHistoryModel4dataERK11QModelIndexi'
    address = self.uglySide.call(ritual, self._valueOf(index), role)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def roleNames(self) -> QHash[int, QByteArray]:
    """
    Calls Qt's 'QHash<int, QByteArray> QWebEngineHistoryModel::roleNames()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginehistorymodel.html#roleNames

    Returns
    -------

    QHash[int, QByteArray]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QHash<int, QByteArray> QWebEngineHistoryModel::roleNames() const
    address = self.uglySide.call(
        'ritual_ZNK22QWebEngineHistoryModel9roleNamesEv',
    )
    from ..QtCore import QByteArray
    return QHash[int, QByteArray]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QWebEngineHistoryModelPrivate)
  @overload(NoneType)
  def __init__(self, a0: Optional[QWebEngineHistoryModelPrivate]) -> None:
    """
    Notes what was given, for Qt's
    'QWebEngineHistoryModel::QWebEngineHistoryModel(
    QWebEngineHistoryModelPrivate *a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qwebenginehistorymodel.html#QWebEngineHistoryModel

    Parameters
    ----------

    a0 : Optional[QWebEngineHistoryModelPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QWebEngineHistoryModel::QWebEngineHistoryModel(
    #      QWebEngineHistoryModelPrivate *a0)
    self._noteCreation(QWebEngineHistoryModel, lambda: Rituals.call(
        'ritual_ZN22QWebEngineHistoryModelC1EP29QWebEngineHistoryModelPriva'
        'te',
        self._addressOf(a0),
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
    Calls Qt's 'void QWebEngineHistoryModel::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginehistorymodel.html#reset
    """
    #  void QWebEngineHistoryModel::reset()
    self.uglySide.call('ritual_ZN22QWebEngineHistoryModel5resetEv')

  def d_func(self) -> Optional[QWebEngineHistoryModelPrivate]:
    """
    Calls Qt's 'QWebEngineHistoryModelPrivate
    *QWebEngineHistoryModel::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qwebenginehistorymodel.html#d_func

    Returns
    -------

    Optional[QWebEngineHistoryModelPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QWebEngineHistoryModelPrivate *QWebEngineHistoryModel::d_func()
    address = self.uglySide.call(
        'ritual_ZN22QWebEngineHistoryModel6d_funcEv',
    )
    from . import QWebEngineHistoryModelPrivate
    return QWebEngineHistoryModelPrivate._cuteAt(address)
