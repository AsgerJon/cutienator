"""
QDeclarativePlaceContentModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qdeclarativeplacecontentmodel_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QDeclarativePlaceContentModel to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QAbstractListModel, QHash, QMap, QObject
from ..QtQml import QQmlParserStatus
from . import QPlaceContent

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QMetaObject, QModelIndex, QVariant
  from . import QDeclarativePlace
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDeclarativePlace = WAIT['QDeclarativePlace']
  QModelIndex = WAIT['QModelIndex']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDeclarativePlaceContentModel(QAbstractListModel, QQmlParserStatus):
  """
  The cute side of Qt's QDeclarativePlaceContentModel: a plain Python object
  standing in front of one C++ QDeclarativePlaceContentModel.

  It is built on the cute 'QAbstractListModel', as Qt's
  QDeclarativePlaceContentModel is built on Qt's QAbstractListModel, and has
  everything that class has. It is built on the cute 'QQmlParserStatus' as
  well, as Qt's QDeclarativePlaceContentModel is built on Qt's
  QQmlParserStatus too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDeclarativePlaceContentModel that has a ritual and
  that Python can call so far, 20 names in all: 'metaObject', 'tr', 'place',
  'setPlace', 'batchSize', 'setBatchSize', 'totalCount', 'clearData',
  'initializeCollection', 'rowCount', 'data', 'roleNames', 'canFetchMore',
  'fetchMore', 'classBegin', 'componentComplete', 'placeChanged',
  'batchSizeChanged', 'totalCountChanged', 'fetchFinished'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDeclarativePlaceContentModel::qt_metacast(const char *a0)':
    one of Qt's own inner workings.
  - Qt's 'int QDeclarativePlaceContentModel::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QDeclarativePlaceContentModel::~QDeclarativePlaceContentModel()':
    the destructor: Python never removes a C++ QDeclarativePlaceContentModel.

  What has no ritual
  ------------------

  2 of the 26 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QDeclarativePlaceContentModel is created at the first use, not by
    'QDeclarativePlaceContentModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDeclarativePlaceContentModel.
  - Qt tells when it has removed the C++ QDeclarativePlaceContentModel. Every
    call on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QDeclarativePlaceContentModel, each a class
  #  in here as in C++, and the names Qt has for the combinations of its
  #  flags enums.

  class Roles(CuteNum):
    """
    The enum 'QDeclarativePlaceContentModel::Roles' of Qt, with the 15 names
    Qt gives in it.
    """

    ContentSupplierRole = Kee[int](256)
    ContentUserRole = Kee[int](257)
    ContentAttributionRole = Kee[int](258)
    EditorialTitleRole = Kee[int](259)
    EditorialTextRole = Kee[int](260)
    EditorialLanguageRole = Kee[int](261)
    ImageIdRole = Kee[int](262)
    ImageUrlRole = Kee[int](263)
    ImageMimeTypeRole = Kee[int](264)
    ReviewIdRole = Kee[int](265)
    ReviewDateTimeRole = Kee[int](266)
    ReviewTitleRole = Kee[int](267)
    ReviewTextRole = Kee[int](268)
    ReviewLanguageRole = Kee[int](269)
    ReviewRatingRole = Kee[int](270)

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
    Calls Qt's 'QString QDeclarativePlaceContentModel::tr(const char *s,
    const char *c, int n)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplacecontentmodel.html#tr

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
    #  QString QDeclarativePlaceContentModel::tr(const char *s, const char
    #      *c, int n)
    return Rituals.call(
        'ritual_ZN29QDeclarativePlaceContentModel2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDeclarativePlaceContentModel'

  #  Qt's QDeclarativePlaceContentModel is built on more than one class. The
  #  part of a C++ QDeclarativePlaceContentModel that belongs to a class
  #  after the first begins somewhere inside the object, and the ritual named
  #  for that class gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlParserStatus':
          'ritual_cast_QDeclarativePlaceContentModel_QQmlParserStatus',
  }

  #  A C++ QDeclarativePlaceContentModel Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDeclarativePlaceContentModel'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject
    *QDeclarativePlaceContentModel::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplacecontentmodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDeclarativePlaceContentModel::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK29QDeclarativePlaceContentModel10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def place(self) -> Optional[QDeclarativePlace]:
    """
    Calls Qt's 'QDeclarativePlace *QDeclarativePlaceContentModel::place()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplacecontentmodel.html#place

    Returns
    -------

    Optional[QDeclarativePlace]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDeclarativePlace *QDeclarativePlaceContentModel::place() const
    address = self.uglySide.call(
        'ritual_ZNK29QDeclarativePlaceContentModel5placeEv',
    )
    from . import QDeclarativePlace
    return QDeclarativePlace._cuteAt(address)

  def batchSize(self) -> int:
    """
    Calls Qt's 'int QDeclarativePlaceContentModel::batchSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplacecontentmodel.html#batchSize
    """
    #  int QDeclarativePlaceContentModel::batchSize() const
    return self.uglySide.call(
        'ritual_ZNK29QDeclarativePlaceContentModel9batchSizeEv',
    )

  def totalCount(self) -> int:
    """
    Calls Qt's 'int QDeclarativePlaceContentModel::totalCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplacecontentmodel.html#totalCount
    """
    #  int QDeclarativePlaceContentModel::totalCount() const
    return self.uglySide.call(
        'ritual_ZNK29QDeclarativePlaceContentModel10totalCountEv',
    )

  @overload(QModelIndex)
  def rowCount(self, parent: QModelIndex) -> int:
    """
    Calls Qt's 'int QDeclarativePlaceContentModel::rowCount(const QModelIndex
    &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplacecontentmodel.html#rowCount

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  int QDeclarativePlaceContentModel::rowCount(const QModelIndex &parent)
    #      const
    ritual = (
        'ritual_ZNK29QDeclarativePlaceContentModel8rowCountERK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK29QDeclarativePlaceContentModel8rowCountERK11QMode'
          'lIndex')
    return self.uglySide.call(ritual, self._valueOf(parent))

  @overload(QModelIndex, int)
  def data(self, index: QModelIndex, role: int) -> QVariant:
    """
    Calls Qt's 'QVariant QDeclarativePlaceContentModel::data(const
    QModelIndex &index, int role) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplacecontentmodel.html#data

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
    #  QVariant QDeclarativePlaceContentModel::data(const QModelIndex &index,
    #      int role) const
    ritual = (
        'ritual_ZNK29QDeclarativePlaceContentModel4dataERK11QModelIndexi')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK29QDeclarativePlaceContentModel4dataERK11QModelInd'
          'exi')
    address = self.uglySide.call(ritual, self._valueOf(index), role)
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def roleNames(self) -> QHash[int, QByteArray]:
    """
    Calls Qt's 'QHash<int, QByteArray>
    QDeclarativePlaceContentModel::roleNames() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplacecontentmodel.html#roleNames

    Returns
    -------

    QHash[int, QByteArray]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QHash<int, QByteArray> QDeclarativePlaceContentModel::roleNames()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK29QDeclarativePlaceContentModel9roleNamesEv',
    )
    from ..QtCore import QByteArray
    return QHash[int, QByteArray]._cuteOwning(address)

  @overload(QModelIndex)
  def canFetchMore(self, parent: QModelIndex) -> bool:
    """
    Calls Qt's 'bool QDeclarativePlaceContentModel::canFetchMore(const
    QModelIndex &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplacecontentmodel.html#canFetchMore

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  bool QDeclarativePlaceContentModel::canFetchMore(const QModelIndex
    #      &parent) const
    ritual = (
        'ritual_ZNK29QDeclarativePlaceContentModel12canFetchMoreERK11QModel'
        'Index')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZNK29QDeclarativePlaceContentModel12canFetchMoreERK11'
          'QModelIndex')
    return self.uglySide.call(ritual, self._valueOf(parent))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QDeclarativePlace)
  @overload(NoneType)
  def setPlace(self, place: Optional[QDeclarativePlace]) -> None:
    """
    Calls Qt's 'void
    QDeclarativePlaceContentModel::setPlace(QDeclarativePlace *place)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplacecontentmodel.html#setPlace

    Parameters
    ----------

    place : Optional[QDeclarativePlace]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDeclarativePlaceContentModel::setPlace(QDeclarativePlace *place)
    self.uglySide.call(
        'ritual_ZN29QDeclarativePlaceContentModel8setPlaceEP17QDeclarativeP'
        'lace',
        self._addressOf(place),
    )

  @overload(int)
  def setBatchSize(self, batchSize: int) -> None:
    """
    Calls Qt's 'void QDeclarativePlaceContentModel::setBatchSize(int
    batchSize)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplacecontentmodel.html#setBatchSize

    Parameters
    ----------

    batchSize : int
      Passed on as it is.
    """
    #  void QDeclarativePlaceContentModel::setBatchSize(int batchSize)
    self.uglySide.call(
        'ritual_ZN29QDeclarativePlaceContentModel12setBatchSizeEi',
        batchSize,
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

  @overload(QPlaceContent.Type)
  @overload(QPlaceContent.Type, QObject)
  @overload(QPlaceContent.Type, NoneType)
  def __init__(
      self,
      type: QPlaceContent.Type,
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QDeclarativePlaceContentModel::QDeclarativePlaceContentModel(
    QPlaceContent::Type type, QObject *parent)', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplacecontentmodel.html

    Parameters
    ----------

    type : QPlaceContent.Type
      Passed on as its number.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDeclarativePlaceContentModel::QDeclarativePlaceContentModel(
    #      QPlaceContent::Type type, QObject *parent)
    self._noteCreation(QDeclarativePlaceContentModel, lambda: Rituals.call(
        'ritual_ZN29QDeclarativePlaceContentModelC1EN13QPlaceContent4TypeEP'
        '7QObject',
        type.value, self._addressOf(parent, 'QObject'),
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

  def clearData(self) -> None:
    """
    Calls Qt's 'void QDeclarativePlaceContentModel::clearData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplacecontentmodel.html#clearData
    """
    #  void QDeclarativePlaceContentModel::clearData()
    self.uglySide.call(
        'ritual_ZN29QDeclarativePlaceContentModel9clearDataEv',
    )

  @overload(int, QMap[int, QPlaceContent])
  def initializeCollection(
      self,
      totalCount: int,
      collection: QMap[int, QPlaceContent],
  ) -> None:
    """
    Calls Qt's 'void QDeclarativePlaceContentModel::initializeCollection(int
    totalCount, const QPlaceContent::Collection &collection)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplacecontentmodel.html

    Parameters
    ----------

    totalCount : int
      Passed on as it is.

    collection : QMap[int, QPlaceContent]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  void QDeclarativePlaceContentModel::initializeCollection(int
    #      totalCount, const QPlaceContent::Collection &collection)
    self.uglySide.call(
        'ritual_ZN29QDeclarativePlaceContentModel20initializeCollectionEiRK'
        '4QMapIi13QPlaceContentE',
        totalCount, self._valueOf(collection),
    )

  @overload(QModelIndex)
  def fetchMore(self, parent: QModelIndex) -> None:
    """
    Calls Qt's 'void QDeclarativePlaceContentModel::fetchMore(const
    QModelIndex &parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplacecontentmodel.html#fetchMore

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  void QDeclarativePlaceContentModel::fetchMore(const QModelIndex
    #      &parent)
    ritual = (
        'ritual_ZN29QDeclarativePlaceContentModel9fetchMoreERK11QModelIndex')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN29QDeclarativePlaceContentModel9fetchMoreERK11QMode'
          'lIndex')
    self.uglySide.call(ritual, self._valueOf(parent))

  def classBegin(self) -> None:
    """
    Calls Qt's 'void QDeclarativePlaceContentModel::classBegin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplacecontentmodel.html#classBegin
    """
    #  void QDeclarativePlaceContentModel::classBegin()
    ritual = 'ritual_ZN29QDeclarativePlaceContentModel10classBeginEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN29QDeclarativePlaceContentModel10classBeginEv'
    self.uglySide.call(ritual)

  def componentComplete(self) -> None:
    """
    Calls Qt's 'void QDeclarativePlaceContentModel::componentComplete()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplacecontentmodel.html
    """
    #  void QDeclarativePlaceContentModel::componentComplete()
    ritual = 'ritual_ZN29QDeclarativePlaceContentModel17componentCompleteEv'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN29QDeclarativePlaceContentModel17componentCompleteE'
          'v')
    self.uglySide.call(ritual)

  def placeChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativePlaceContentModel::placeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplacecontentmodel.html#placeChanged
    """
    #  void QDeclarativePlaceContentModel::placeChanged()
    self.uglySide.call(
        'ritual_ZN29QDeclarativePlaceContentModel12placeChangedEv',
    )

  def batchSizeChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativePlaceContentModel::batchSizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplacecontentmodel.html
    """
    #  void QDeclarativePlaceContentModel::batchSizeChanged()
    self.uglySide.call(
        'ritual_ZN29QDeclarativePlaceContentModel16batchSizeChangedEv',
    )

  def totalCountChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativePlaceContentModel::totalCountChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplacecontentmodel.html
    """
    #  void QDeclarativePlaceContentModel::totalCountChanged()
    self.uglySide.call(
        'ritual_ZN29QDeclarativePlaceContentModel17totalCountChangedEv',
    )

  def fetchFinished(self) -> None:
    """
    Calls Qt's 'void QDeclarativePlaceContentModel::fetchFinished()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativeplacecontentmodel.html#fetchFinished
    """
    #  void QDeclarativePlaceContentModel::fetchFinished()
    self.uglySide.call(
        'ritual_ZN29QDeclarativePlaceContentModel13fetchFinishedEv',
    )
