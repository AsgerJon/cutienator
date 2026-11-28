"""
QDeclarativeGeoJsonData binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtLocation/6.12.0/QtLocation/private/qdeclarativegeojsondata_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QDeclarativeGeoJsonData to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QUrl, QVariant
  from ..QtQuick import QQuickItem
  from . import QDeclarativeGeoMap
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDeclarativeGeoMap = WAIT['QDeclarativeGeoMap']
  QQuickItem = WAIT['QQuickItem']
  QUrl = WAIT['QUrl']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDeclarativeGeoJsonData(QObject):
  """
  The cute side of Qt's QDeclarativeGeoJsonData: a plain Python object
  standing in front of one C++ QDeclarativeGeoJsonData.

  It is built on the cute 'QObject', as Qt's QDeclarativeGeoJsonData is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDeclarativeGeoJsonData that has a ritual and that
  Python can call so far, 18 names in all: 'metaObject', 'tr', 'model',
  'setModel', 'sourceUrl', 'clear', 'addItem', 'open', 'openUrl', 'save',
  'saveAs', 'setModelToMapContents', 'modelChanged', 'sourceUrlChanged',
  'toVariant', 'dumpGeoJSON', 'writeDebug', 'toString'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDeclarativeGeoJsonData::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QDeclarativeGeoJsonData::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QDeclarativeGeoJsonData::~QDeclarativeGeoJsonData()': the
    destructor: Python never removes a C++ QDeclarativeGeoJsonData.

  What has no ritual
  ------------------

  2 of the 24 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QDeclarativeGeoJsonData is created at the first use, not by
    'QDeclarativeGeoJsonData(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDeclarativeGeoJsonData.
  - Qt tells when it has removed the C++ QDeclarativeGeoJsonData. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QDeclarativeGeoJsonData::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativegeojsondata.html#tr

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
    #  QString QDeclarativeGeoJsonData::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QDeclarativeGeoJsonData2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(QDeclarativeGeoMap)
  @overload(NoneType)
  def toVariant(
      mapItemView: Optional[QDeclarativeGeoMap],
  ) -> QList[QVariant]:
    """
    Calls Qt's 'QVariantList
    QDeclarativeGeoJsonData::toVariant(QDeclarativeGeoMap *mapItemView)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeojsondata.html#toVariant

    Parameters
    ----------

    mapItemView : Optional[QDeclarativeGeoMap]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QList[QVariant]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QVariantList QDeclarativeGeoJsonData::toVariant(QDeclarativeGeoMap
    #      *mapItemView)
    address = Rituals.call(
        'ritual_ZN23QDeclarativeGeoJsonData9toVariantEP18QDeclarativeGeoMap',
        CuteMixin._addressOf(mapItemView),
    )
    from ..QtCore import QVariant
    return QList[QVariant]._cuteOwning(address)

  @staticmethod
  @overload(QList[QVariant], QUrl)
  def dumpGeoJSON(geoJson: QList[QVariant], url: QUrl) -> bool:
    """
    Calls Qt's 'bool QDeclarativeGeoJsonData::dumpGeoJSON(const QVariantList
    &geoJson, const QUrl &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeojsondata.html#dumpGeoJSON

    Parameters
    ----------

    geoJson : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  bool QDeclarativeGeoJsonData::dumpGeoJSON(const QVariantList &geoJson,
    #      const QUrl &url)
    return Rituals.call(
        'ritual_ZN23QDeclarativeGeoJsonData11dumpGeoJSONERK5QListI8QVariant'
        'ERK4QUrl',
        CuteMixin._valueOf(geoJson), CuteMixin._valueOf(url),
    )

  @staticmethod
  @overload(QList[QVariant], QUrl)
  def writeDebug(geoJson: QList[QVariant], url: QUrl) -> bool:
    """
    Calls Qt's 'bool QDeclarativeGeoJsonData::writeDebug(const QVariantList
    &geoJson, const QUrl &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeojsondata.html#writeDebug

    Parameters
    ----------

    geoJson : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  bool QDeclarativeGeoJsonData::writeDebug(const QVariantList &geoJson,
    #      const QUrl &url)
    return Rituals.call(
        'ritual_ZN23QDeclarativeGeoJsonData10writeDebugERK5QListI8QVariantE'
        'RK4QUrl',
        CuteMixin._valueOf(geoJson), CuteMixin._valueOf(url),
    )

  @staticmethod
  @overload(QList[QVariant])
  def toString(geoJson: QList[QVariant]) -> str:
    """
    Calls Qt's 'QString QDeclarativeGeoJsonData::toString(const QVariantList
    &geoJson)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeojsondata.html#toString

    Parameters
    ----------

    geoJson : QList[QVariant]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDeclarativeGeoJsonData::toString(const QVariantList &geoJson)
    return Rituals.call(
        'ritual_ZN23QDeclarativeGeoJsonData8toStringERK5QListI8QVariantE',
        CuteMixin._valueOf(geoJson),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDeclarativeGeoJsonData'

  #  A C++ QDeclarativeGeoJsonData Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDeclarativeGeoJsonData'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDeclarativeGeoJsonData::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeojsondata.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDeclarativeGeoJsonData::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QDeclarativeGeoJsonData10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def model(self) -> QVariant:
    """
    Calls Qt's 'QVariant QDeclarativeGeoJsonData::model() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativegeojsondata.html#model

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QDeclarativeGeoJsonData::model() const
    address = self.uglySide.call(
        'ritual_ZNK23QDeclarativeGeoJsonData5modelEv',
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def sourceUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QDeclarativeGeoJsonData::sourceUrl() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeojsondata.html#sourceUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QDeclarativeGeoJsonData::sourceUrl() const
    address = self.uglySide.call(
        'ritual_ZNK23QDeclarativeGeoJsonData9sourceUrlEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QVariant)
  def setModel(self, model: QVariant) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoJsonData::setModel(const QVariant
    &model)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeojsondata.html#setModel

    Parameters
    ----------

    model : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.
    """
    #  void QDeclarativeGeoJsonData::setModel(const QVariant &model)
    self.uglySide.call(
        'ritual_ZN23QDeclarativeGeoJsonData8setModelERK8QVariant',
        self._valueOf(model),
    )

  @overload(QDeclarativeGeoMap)
  @overload(NoneType)
  def setModelToMapContents(self, map: Optional[QDeclarativeGeoMap]) -> None:
    """
    Calls Qt's 'void
    QDeclarativeGeoJsonData::setModelToMapContents(QDeclarativeGeoMap *map)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeojsondata.html#setModelToMapContents

    Parameters
    ----------

    map : Optional[QDeclarativeGeoMap]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDeclarativeGeoJsonData::setModelToMapContents(QDeclarativeGeoMap
    #      *map)
    self.uglySide.call(
        'ritual_ZN23QDeclarativeGeoJsonData21setModelToMapContentsEP18QDecl'
        'arativeGeoMap',
        self._addressOf(map),
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
    'QDeclarativeGeoJsonData::QDeclarativeGeoJsonData(QObject *parent)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeojsondata.html

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDeclarativeGeoJsonData::QDeclarativeGeoJsonData(QObject *parent)
    self._noteCreation(QDeclarativeGeoJsonData, lambda: Rituals.call(
        'ritual_ZN23QDeclarativeGeoJsonDataC1EP7QObject',
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

  def clear(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoJsonData::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativegeojsondata.html#clear
    """
    #  void QDeclarativeGeoJsonData::clear()
    self.uglySide.call('ritual_ZN23QDeclarativeGeoJsonData5clearEv')

  @overload(QQuickItem)
  @overload(NoneType)
  def addItem(self, item: Optional[QQuickItem]) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoJsonData::addItem(QQuickItem *item)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeojsondata.html#addItem

    Parameters
    ----------

    item : Optional[QQuickItem]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QDeclarativeGeoJsonData::addItem(QQuickItem *item)
    self.uglySide.call(
        'ritual_ZN23QDeclarativeGeoJsonData7addItemEP10QQuickItem',
        self._addressOf(item),
    )

  def open(self) -> bool:
    """
    Calls Qt's 'bool QDeclarativeGeoJsonData::open()'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativegeojsondata.html#open
    """
    #  bool QDeclarativeGeoJsonData::open()
    return self.uglySide.call('ritual_ZN23QDeclarativeGeoJsonData4openEv')

  @overload(QUrl)
  def openUrl(self, url: QUrl) -> bool:
    """
    Calls Qt's 'bool QDeclarativeGeoJsonData::openUrl(const QUrl &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeojsondata.html#openUrl

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  bool QDeclarativeGeoJsonData::openUrl(const QUrl &url)
    return self.uglySide.call(
        'ritual_ZN23QDeclarativeGeoJsonData7openUrlERK4QUrl',
        self._valueOf(url),
    )

  def save(self) -> bool:
    """
    Calls Qt's 'bool QDeclarativeGeoJsonData::save()'.

    Qt's own words: https://doc.qt.io/qt-6/qdeclarativegeojsondata.html#save
    """
    #  bool QDeclarativeGeoJsonData::save()
    return self.uglySide.call('ritual_ZN23QDeclarativeGeoJsonData4saveEv')

  @overload(QUrl)
  def saveAs(self, url: QUrl) -> bool:
    """
    Calls Qt's 'bool QDeclarativeGeoJsonData::saveAs(const QUrl &url)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeojsondata.html#saveAs

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  bool QDeclarativeGeoJsonData::saveAs(const QUrl &url)
    return self.uglySide.call(
        'ritual_ZN23QDeclarativeGeoJsonData6saveAsERK4QUrl',
        self._valueOf(url),
    )

  def modelChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoJsonData::modelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeojsondata.html#modelChanged
    """
    #  void QDeclarativeGeoJsonData::modelChanged()
    self.uglySide.call('ritual_ZN23QDeclarativeGeoJsonData12modelChangedEv')

  def sourceUrlChanged(self) -> None:
    """
    Calls Qt's 'void QDeclarativeGeoJsonData::sourceUrlChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdeclarativegeojsondata.html#sourceUrlChanged
    """
    #  void QDeclarativeGeoJsonData::sourceUrlChanged()
    self.uglySide.call(
        'ritual_ZN23QDeclarativeGeoJsonData16sourceUrlChangedEv',
    )
