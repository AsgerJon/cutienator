"""
QQuick3DXrSpatialAnchorListModel binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrspatialanchorlistmodel_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DXrSpatialAnchorListModel to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteFlags, CuteNum, WAIT
from ..QtCore import QAbstractListModel, QHash, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject, QModelIndex, QUuid, QVariant
  from . import QQuick3DXrSpatialAnchor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QModelIndex = WAIT['QModelIndex']
  QQuick3DXrSpatialAnchor = WAIT['QQuick3DXrSpatialAnchor']
  QUuid = WAIT['QUuid']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DXrSpatialAnchorListModel(QAbstractListModel):
  """
  The cute side of Qt's QQuick3DXrSpatialAnchorListModel: a plain Python
  object standing in front of one C++ QQuick3DXrSpatialAnchorListModel.

  It is built on the cute 'QAbstractListModel', as Qt's
  QQuick3DXrSpatialAnchorListModel is built on Qt's QAbstractListModel, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DXrSpatialAnchorListModel that has a ritual
  and that Python can call so far, 18 names in all: 'metaObject', 'rowCount',
  'data', 'roleNames', 'requestSceneCapture', 'queryAnchors', 'filterMode',
  'identifierFilter', 'classificationFilter', 'classificationStringFilter',
  'filterModeChanged', 'identifierFilterChanged',
  'classificationFilterChanged', 'classificationStringFilterChanged',
  'handleAnchorAdded', 'handleAnchorRemoved', 'handleAnchorUpdated',
  'matchesAnchorFilter'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DXrSpatialAnchorListModel::qt_metacast(const char
    *a0)': one of Qt's own inner workings.
  - Qt's 'int QQuick3DXrSpatialAnchorListModel::qt_metacall(QMetaObject::Call
    a0, int a1, void **a2)': one of Qt's own inner workings.

  What has no ritual
  ------------------

  9 of the 29 functions Qt declares: 5 leans on
  'QQuick3DXrSpatialAnchorListModel; 2 not a gap; 2 Qt's library has no name
  for it, and its code in Qt's source does not compile apart from its file.

  What to expect
  --------------

  - The C++ QQuick3DXrSpatialAnchorListModel is created at the first use, not
    by 'QQuick3DXrSpatialAnchorListModel(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DXrSpatialAnchorListModel.
  - Qt tells when it has removed the C++ QQuick3DXrSpatialAnchorListModel.
    Every call on the cute object, and every use of it as an argument, then
    raises 'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DXrSpatialAnchorListModel that has no cute
    function yet, '__init__', 'anchorsFiltered', 'setClassificationFilter',
    'setClassificationStringFilter', 'setFilterMode', 'setIdentifierFilter',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  #  The enums Qt writes inside QQuick3DXrSpatialAnchorListModel, each a
  #  class in here as in C++, and the names Qt has for the combinations of
  #  its flags enums.

  class ClassificationFlag(CuteFlags, number='unsigned int'):
    """
    The flags enum 'QQuick3DXrSpatialAnchorListModel::ClassificationFlag' of
    Qt, with the 8 names Qt gives in it. Qt names the type of its
    combinations 'QQuick3DXrSpatialAnchorListModel::ClassificationFlags'.
    """

    Wall = 0x1
    Ceiling = 0x2
    Floor = 0x4
    Table = 0x8
    Seat = 0x10
    Window = 0x20
    Door = 0x40
    Other = 0x80

  ClassificationFlags = ClassificationFlag

  class FilterMode(CuteNum, scoped=True):
    """
    The enum 'QQuick3DXrSpatialAnchorListModel::FilterMode' of Qt, with the 3
    names Qt gives in it. C++ keeps these names inside the enum, so the class
    that holds the enum does not have them.
    """

    All = Kee[int](0)
    Classification = Kee[int](1)
    Identifier = Kee[int](2)

  class SpatialAnchorRoles(CuteNum):
    """
    The enum 'QQuick3DXrSpatialAnchorListModel::SpatialAnchorRoles' of Qt,
    with the 1 names Qt gives in it.
    """

    Anchor = Kee[int](277)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DXrSpatialAnchorListModel'

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
    *QQuick3DXrSpatialAnchorListModel::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrspatialanchorlistmodel.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DXrSpatialAnchorListModel::metaObject()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK32QQuick3DXrSpatialAnchorListModel10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  @overload(QModelIndex)
  def rowCount(self, parent: QModelIndex) -> int:
    """
    Calls Qt's 'int QQuick3DXrSpatialAnchorListModel::rowCount(const
    QModelIndex &parent) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrspatialanchorlistmodel.html#rowCount

    Parameters
    ----------

    parent : QModelIndex
      Passed on as a value: Qt reads the C++ QModelIndex, which stays
      Python's own.
    """
    #  int QQuick3DXrSpatialAnchorListModel::rowCount(const QModelIndex
    #      &parent) const
    return self.uglySide.call(
        'ritual_ZNK32QQuick3DXrSpatialAnchorListModel8rowCountERK11QModelIn'
        'dex',
        self._valueOf(parent),
    )

  @overload(QModelIndex, int)
  def data(self, index: QModelIndex, role: int) -> QVariant:
    """
    Calls Qt's 'QVariant QQuick3DXrSpatialAnchorListModel::data(const
    QModelIndex &index, int role) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrspatialanchorlistmodel.html#data

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
    #  QVariant QQuick3DXrSpatialAnchorListModel::data(const QModelIndex
    #      &index, int role) const
    address = self.uglySide.call(
        'ritual_ZNK32QQuick3DXrSpatialAnchorListModel4dataERK11QModelIndexi',
        self._valueOf(index), role,
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  def roleNames(self) -> QHash[int, QByteArray]:
    """
    Calls Qt's 'QHash<int, QByteArray>
    QQuick3DXrSpatialAnchorListModel::roleNames() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrspatialanchorlistmodel.html#roleNames

    Returns
    -------

    QHash[int, QByteArray]
      A new cute map around the copy Qt gave back. Python owns it.
    """
    #  QHash<int, QByteArray> QQuick3DXrSpatialAnchorListModel::roleNames()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK32QQuick3DXrSpatialAnchorListModel9roleNamesEv',
    )
    from ..QtCore import QByteArray
    return QHash[int, QByteArray]._cuteOwning(address)

  def filterMode(self) -> FilterMode:
    """
    Calls Qt's 'FilterMode QQuick3DXrSpatialAnchorListModel::filterMode()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrspatialanchorlistmodel.html#filterMode

    Returns
    -------

    FilterMode
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'FilterMode(number)'
      gives.
    """
    #  FilterMode QQuick3DXrSpatialAnchorListModel::filterMode() const
    return QQuick3DXrSpatialAnchorListModel.FilterMode(self.uglySide.call(
        'ritual_ZNK32QQuick3DXrSpatialAnchorListModel10filterModeEv',
    ))

  def identifierFilter(self) -> QStringList:
    """
    Calls Qt's 'QStringList
    QQuick3DXrSpatialAnchorListModel::identifierFilter() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrspatialanchorlistmodel.html

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QQuick3DXrSpatialAnchorListModel::identifierFilter() const
    address = self.uglySide.call(
        'ritual_ZNK32QQuick3DXrSpatialAnchorListModel16identifierFilterEv',
    )
    return QStringList._cuteOwning(address)

  def classificationFilter(self) -> ClassificationFlags:
    """
    Calls Qt's 'ClassificationFlags
    QQuick3DXrSpatialAnchorListModel::classificationFilter() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrspatialanchorlistmodel.html

    Returns
    -------

    ClassificationFlags
      The value standing for the combination Qt gave back.
    """
    #  ClassificationFlags
    #      QQuick3DXrSpatialAnchorListModel::classificationFilter() const
    return QQuick3DXrSpatialAnchorListModel.ClassificationFlags(
        self.uglySide.call(
            'ritual_ZNK32QQuick3DXrSpatialAnchorListModel20classificationFi'
            'lterEv',
        ))

  def classificationStringFilter(self) -> QStringList:
    """
    Calls Qt's 'QStringList
    QQuick3DXrSpatialAnchorListModel::classificationStringFilter() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrspatialanchorlistmodel.html

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList
    #      QQuick3DXrSpatialAnchorListModel::classificationStringFilter()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK32QQuick3DXrSpatialAnchorListModel26classificationString'
        'FilterEv',
    )
    return QStringList._cuteOwning(address)

  @overload(QQuick3DXrSpatialAnchor)
  @overload(NoneType)
  def matchesAnchorFilter(
      self,
      anchor: Optional[QQuick3DXrSpatialAnchor],
  ) -> bool:
    """
    Calls Qt's 'bool QQuick3DXrSpatialAnchorListModel::matchesAnchorFilter(
    QQuick3DXrSpatialAnchor *anchor) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrspatialanchorlistmodel.html

    Parameters
    ----------

    anchor : Optional[QQuick3DXrSpatialAnchor]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuick3DXrSpatialAnchorListModel::matchesAnchorFilter(
    #      QQuick3DXrSpatialAnchor *anchor) const
    return self.uglySide.call(
        'ritual_ZNK32QQuick3DXrSpatialAnchorListModel19matchesAnchorFilterE'
        'P23QQuick3DXrSpatialAnchor',
        self._addressOf(anchor),
    )

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQuick3DXrSpatialAnchorListModel::QQuick3DXrSpatialAnchorListModel(
    QObject *parent)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: incomplete type
    'QQuick3DXrAnchorManager' named in nested name specifier.
    """
    raise NotImplementedError(
        "'QQuick3DXrSpatialAnchorListModel.__init__' has no cute function "
        "yet. Qt's "
        "'QQuick3DXrSpatialAnchorListModel::QQuick3DXrSpatialAnchorListModel"
        "(QObject *parent)': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: incomplete "
        "type 'QQuick3DXrAnchorManager' named in nested name specifier.")

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

  def requestSceneCapture(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DXrSpatialAnchorListModel::requestSceneCapture()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrspatialanchorlistmodel.html
    """
    #  void QQuick3DXrSpatialAnchorListModel::requestSceneCapture()
    self.uglySide.call(
        'ritual_ZN32QQuick3DXrSpatialAnchorListModel19requestSceneCaptureEv',
    )

  def queryAnchors(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrSpatialAnchorListModel::queryAnchors()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrspatialanchorlistmodel.html#queryAnchors
    """
    #  void QQuick3DXrSpatialAnchorListModel::queryAnchors()
    self.uglySide.call(
        'ritual_ZN32QQuick3DXrSpatialAnchorListModel12queryAnchorsEv',
    )

  def filterModeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrSpatialAnchorListModel::filterModeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrspatialanchorlistmodel.html
    """
    #  void QQuick3DXrSpatialAnchorListModel::filterModeChanged()
    self.uglySide.call(
        'ritual_ZN32QQuick3DXrSpatialAnchorListModel17filterModeChangedEv',
    )

  def identifierFilterChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DXrSpatialAnchorListModel::identifierFilterChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrspatialanchorlistmodel.html
    """
    #  void QQuick3DXrSpatialAnchorListModel::identifierFilterChanged()
    self.uglySide.call(
        'ritual_ZN32QQuick3DXrSpatialAnchorListModel23identifierFilterChang'
        'edEv',
    )

  def classificationFilterChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DXrSpatialAnchorListModel::classificationFilterChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrspatialanchorlistmodel.html
    """
    #  void QQuick3DXrSpatialAnchorListModel::classificationFilterChanged()
    self.uglySide.call(
        'ritual_ZN32QQuick3DXrSpatialAnchorListModel27classificationFilterC'
        'hangedEv',
    )

  def classificationStringFilterChanged(self) -> None:
    """
    Calls Qt's 'void
    QQuick3DXrSpatialAnchorListModel::classificationStringFilterChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrspatialanchorlistmodel.html
    """
    #  void QQuick3DXrSpatialAnchorListModel::
    #      classificationStringFilterChanged()
    self.uglySide.call(
        'ritual_ZN32QQuick3DXrSpatialAnchorListModel33classificationStringF'
        'ilterChangedEv',
    )

  @overload(QQuick3DXrSpatialAnchor)
  @overload(NoneType)
  def handleAnchorAdded(
      self,
      anchor: Optional[QQuick3DXrSpatialAnchor],
  ) -> None:
    """
    Calls Qt's 'void QQuick3DXrSpatialAnchorListModel::handleAnchorAdded(
    QQuick3DXrSpatialAnchor *anchor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrspatialanchorlistmodel.html

    Parameters
    ----------

    anchor : Optional[QQuick3DXrSpatialAnchor]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DXrSpatialAnchorListModel::handleAnchorAdded(
    #      QQuick3DXrSpatialAnchor *anchor)
    self.uglySide.call(
        'ritual_ZN32QQuick3DXrSpatialAnchorListModel17handleAnchorAddedEP23'
        'QQuick3DXrSpatialAnchor',
        self._addressOf(anchor),
    )

  @overload(QUuid)
  def handleAnchorRemoved(self, uuid: QUuid) -> None:
    """
    Calls Qt's 'void
    QQuick3DXrSpatialAnchorListModel::handleAnchorRemoved(QUuid uuid)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrspatialanchorlistmodel.html

    Parameters
    ----------

    uuid : QUuid
      Passed on as a value: Qt reads the C++ QUuid, which stays Python's own.
    """
    #  void QQuick3DXrSpatialAnchorListModel::handleAnchorRemoved(QUuid uuid)
    self.uglySide.call(
        'ritual_ZN32QQuick3DXrSpatialAnchorListModel19handleAnchorRemovedE5'
        'QUuid',
        self._valueOf(uuid),
    )

  @overload(QQuick3DXrSpatialAnchor)
  @overload(NoneType)
  def handleAnchorUpdated(
      self,
      anchor: Optional[QQuick3DXrSpatialAnchor],
  ) -> None:
    """
    Calls Qt's 'void QQuick3DXrSpatialAnchorListModel::handleAnchorUpdated(
    QQuick3DXrSpatialAnchor *anchor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrspatialanchorlistmodel.html

    Parameters
    ----------

    anchor : Optional[QQuick3DXrSpatialAnchor]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DXrSpatialAnchorListModel::handleAnchorUpdated(
    #      QQuick3DXrSpatialAnchor *anchor)
    self.uglySide.call(
        'ritual_ZN32QQuick3DXrSpatialAnchorListModel19handleAnchorUpdatedEP'
        '23QQuick3DXrSpatialAnchor',
        self._addressOf(anchor),
    )

  @staticmethod
  def anchorsFiltered(*__, **_) -> Never:
    """
    Qt's 'QList<QQuick3DXrSpatialAnchor *>
    QQuick3DXrSpatialAnchorListModel::anchorsFiltered() const': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: member access into incomplete type
    'QQuick3DXrAnchorManager'.
    """
    raise NotImplementedError(
        "'QQuick3DXrSpatialAnchorListModel.anchorsFiltered' has no cute "
        "function yet. Qt's 'QList<QQuick3DXrSpatialAnchor *> "
        "QQuick3DXrSpatialAnchorListModel::anchorsFiltered() const': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'QQuick3DXrAnchorManager'.")

  @staticmethod
  def setClassificationFilter(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrSpatialAnchorListModel::setClassificationFilter(
    ClassificationFlags newClassFilter)': leans on
    'QQuick3DXrSpatialAnchorListModel::classificationFilterChanged()', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DXrSpatialAnchorListModel.setClassificationFilter' has no "
        "cute function yet. Qt's 'void "
        "QQuick3DXrSpatialAnchorListModel::setClassificationFilter(Classific"
        "ationFlags newClassFilter)': leans on "
        "'QQuick3DXrSpatialAnchorListModel::classificationFilterChanged()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def setClassificationStringFilter(*__, **_) -> Never:
    """
    Qt's 'void
    QQuick3DXrSpatialAnchorListModel::setClassificationStringFilter(const
    QStringList &newClassStringFilter)': leans on
    'QQuick3DXrSpatialAnchorListModel::classificationStringFilterChanged()',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DXrSpatialAnchorListModel.setClassificationStringFilter' "
        "has no cute function yet. Qt's 'void "
        "QQuick3DXrSpatialAnchorListModel::setClassificationStringFilter(con"
        "st QStringList &newClassStringFilter)': leans on "
        "'QQuick3DXrSpatialAnchorListModel::classificationStringFilterChange"
        "d()', which Qt's source does not mark for use from outside Qt and "
        "has no code for that could be taken.")

  @staticmethod
  def setFilterMode(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrSpatialAnchorListModel::setFilterMode(FilterMode
    newFilterMode)': leans on
    'QQuick3DXrSpatialAnchorListModel::filterModeChanged()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DXrSpatialAnchorListModel.setFilterMode' has no cute "
        "function yet. Qt's 'void "
        "QQuick3DXrSpatialAnchorListModel::setFilterMode(FilterMode "
        "newFilterMode)': leans on "
        "'QQuick3DXrSpatialAnchorListModel::filterModeChanged()', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def setIdentifierFilter(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrSpatialAnchorListModel::setIdentifierFilter(const
    QStringList &filter)': leans on
    'QQuick3DXrSpatialAnchorListModel::identifierFilterChanged()', which Qt's
    source does not mark for use from outside Qt and has no code for that
    could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DXrSpatialAnchorListModel.setIdentifierFilter' has no cute "
        "function yet. Qt's 'void "
        "QQuick3DXrSpatialAnchorListModel::setIdentifierFilter(const "
        "QStringList &filter)': leans on "
        "'QQuick3DXrSpatialAnchorListModel::identifierFilterChanged()', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")
