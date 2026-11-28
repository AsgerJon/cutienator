"""
QQuick3DXrAnchorManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxranchormanager_visionos_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DXrAnchorManager to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QtQuick3DXr

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QUuid
  from . import QQuick3DXrSpatialAnchor
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQuick3DXrSpatialAnchor = WAIT['QQuick3DXrSpatialAnchor']
  QUuid = WAIT['QUuid']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DXrAnchorManager(QObject):
  """
  The cute side of Qt's QQuick3DXrAnchorManager: a plain Python object
  standing in front of one C++ QQuick3DXrAnchorManager.

  It is built on the cute 'QObject', as Qt's QQuick3DXrAnchorManager is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DXrAnchorManager that has a ritual and that
  Python can call so far, 13 names in all: 'metaObject', 'tr', 'instance',
  'getCurrentSpaceId', 'requestSceneCapture', 'queryAllAnchors', 'teardown',
  'anchors', 'anchorCount', 'anchorAdded', 'anchorRemoved', 'anchorUpdated',
  'sceneCaptureCompleted'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DXrAnchorManager::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuick3DXrAnchorManager::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'bool
    QQuick3DXrAnchorManager::getBoundingBox3D(QtQuick3DXr::XrSpaceId space,
    QVector3D &offset, QVector3D &extent)': takes a type Python has no way to
    hand over yet.
  - Qt's 'bool
    QQuick3DXrAnchorManager::getBoundingBox2D(QtQuick3DXr::XrSpaceId space,
    QVector2D &offset, QVector2D &extent)': takes a type Python has no way to
    hand over yet.
  - Qt's 'bool
    QQuick3DXrAnchorManager::setupSpatialAnchor(QtQuick3DXr::XrSpaceId space,
    QQuick3DXrSpatialAnchor &anchor)': takes a type Python has no way to hand
    over yet.
  - Qt's 'QQuick3DXrAnchorManager::~QQuick3DXrAnchorManager()': the
    destructor: Python never removes a C++ QQuick3DXrAnchorManager.

  What has no ritual
  ------------------

  10 of the 29 functions Qt declares: 8 cannot be called and cannot be called
  through the meta-object and cannot be copied; 2 not a gap.

  What to expect
  --------------

  - The C++ QQuick3DXrAnchorManager is created at the first use, not by
    'QQuick3DXrAnchorManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DXrAnchorManager.
  - Qt tells when it has removed the C++ QQuick3DXrAnchorManager. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DXrAnchorManager that has no cute function yet,
    '__init__', 'addAnchor', 'getBoundingBox2D', 'getBoundingBox3D',
    'initAnchorManager', 'planeUpdateHandler', 'populateAnchorsList',
    'prepareAnchorManager', 'removeAnchor', 'setupSpatialAnchor',
    'updateAnchor', holds a function that raises 'NotImplementedError', and
    its docstring says why.
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
    Calls Qt's 'QString QQuick3DXrAnchorManager::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxranchormanager.html#tr

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
    #  QString QQuick3DXrAnchorManager::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN23QQuick3DXrAnchorManager2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def instance() -> Optional[QQuick3DXrAnchorManager]:
    """
    Calls Qt's 'QQuick3DXrAnchorManager
    *QQuick3DXrAnchorManager::instance()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxranchormanager.html#instance

    Returns
    -------

    Optional[QQuick3DXrAnchorManager]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQuick3DXrAnchorManager *QQuick3DXrAnchorManager::instance()
    address = Rituals.call('ritual_ZN23QQuick3DXrAnchorManager8instanceEv')
    return QQuick3DXrAnchorManager._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DXrAnchorManager'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DXrAnchorManager::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxranchormanager.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DXrAnchorManager::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK23QQuick3DXrAnchorManager10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def getCurrentSpaceId(self) -> QtQuick3DXr.XrSpaceId:
    """
    Calls Qt's 'QtQuick3DXr::XrSpaceId
    QQuick3DXrAnchorManager::getCurrentSpaceId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxranchormanager.html#getCurrentSpaceId

    Returns
    -------

    QtQuick3DXr.XrSpaceId
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QtQuick3DXr.XrSpaceId(number)' gives.
    """
    #  QtQuick3DXr::XrSpaceId QQuick3DXrAnchorManager::getCurrentSpaceId()
    #      const
    return QtQuick3DXr.XrSpaceId(self.uglySide.call(
        'ritual_ZNK23QQuick3DXrAnchorManager17getCurrentSpaceIdEv',
    ))

  def anchors(self) -> QList[QQuick3DXrSpatialAnchor]:
    """
    Calls Qt's 'QList<QQuick3DXrSpatialAnchor *>
    QQuick3DXrAnchorManager::anchors() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxranchormanager.html#anchors

    Returns
    -------

    QList[QQuick3DXrSpatialAnchor]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQuick3DXrSpatialAnchor *> QQuick3DXrAnchorManager::anchors()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK23QQuick3DXrAnchorManager7anchorsEv',
    )
    from . import QQuick3DXrSpatialAnchor
    return QList[QQuick3DXrSpatialAnchor]._cuteOwning(address)

  def anchorCount(self) -> int:
    """
    Calls Qt's 'qsizetype QQuick3DXrAnchorManager::anchorCount() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxranchormanager.html#anchorCount
    """
    #  qsizetype QQuick3DXrAnchorManager::anchorCount() const
    return self.uglySide.call(
        'ritual_ZNK23QQuick3DXrAnchorManager11anchorCountEv',
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
    Qt's 'QQuick3DXrAnchorManager::QQuick3DXrAnchorManager(QObject *parent)':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QQuick3DXrAnchorManager.__init__' has no cute function yet. Qt's "
        "'QQuick3DXrAnchorManager::QQuick3DXrAnchorManager(QObject "
        "*parent)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

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
    Calls Qt's 'void QQuick3DXrAnchorManager::requestSceneCapture()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxranchormanager.html#requestSceneCapture
    """
    #  void QQuick3DXrAnchorManager::requestSceneCapture()
    self.uglySide.call(
        'ritual_ZN23QQuick3DXrAnchorManager19requestSceneCaptureEv',
    )

  def queryAllAnchors(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DXrAnchorManager::queryAllAnchors()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxranchormanager.html#queryAllAnchors
    """
    #  bool QQuick3DXrAnchorManager::queryAllAnchors()
    return self.uglySide.call(
        'ritual_ZN23QQuick3DXrAnchorManager15queryAllAnchorsEv',
    )

  def teardown(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrAnchorManager::teardown()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxranchormanager.html#teardown
    """
    #  void QQuick3DXrAnchorManager::teardown()
    self.uglySide.call('ritual_ZN23QQuick3DXrAnchorManager8teardownEv')

  @overload(QQuick3DXrSpatialAnchor)
  @overload(NoneType)
  def anchorAdded(self, anchor: Optional[QQuick3DXrSpatialAnchor]) -> None:
    """
    Calls Qt's 'void
    QQuick3DXrAnchorManager::anchorAdded(QQuick3DXrSpatialAnchor *anchor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxranchormanager.html#anchorAdded

    Parameters
    ----------

    anchor : Optional[QQuick3DXrSpatialAnchor]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DXrAnchorManager::anchorAdded(QQuick3DXrSpatialAnchor
    #      *anchor)
    self.uglySide.call(
        'ritual_ZN23QQuick3DXrAnchorManager11anchorAddedEP23QQuick3DXrSpati'
        'alAnchor',
        self._addressOf(anchor),
    )

  @overload(QUuid)
  def anchorRemoved(self, uuid: QUuid) -> None:
    """
    Calls Qt's 'void QQuick3DXrAnchorManager::anchorRemoved(QUuid uuid)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxranchormanager.html#anchorRemoved

    Parameters
    ----------

    uuid : QUuid
      Passed on as a value: Qt reads the C++ QUuid, which stays Python's own.
    """
    #  void QQuick3DXrAnchorManager::anchorRemoved(QUuid uuid)
    self.uglySide.call(
        'ritual_ZN23QQuick3DXrAnchorManager13anchorRemovedE5QUuid',
        self._valueOf(uuid),
    )

  @overload(QQuick3DXrSpatialAnchor)
  @overload(NoneType)
  def anchorUpdated(self, anchor: Optional[QQuick3DXrSpatialAnchor]) -> None:
    """
    Calls Qt's 'void
    QQuick3DXrAnchorManager::anchorUpdated(QQuick3DXrSpatialAnchor *anchor)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxranchormanager.html#anchorUpdated

    Parameters
    ----------

    anchor : Optional[QQuick3DXrSpatialAnchor]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuick3DXrAnchorManager::anchorUpdated(QQuick3DXrSpatialAnchor
    #      *anchor)
    self.uglySide.call(
        'ritual_ZN23QQuick3DXrAnchorManager13anchorUpdatedEP23QQuick3DXrSpa'
        'tialAnchor',
        self._addressOf(anchor),
    )

  def sceneCaptureCompleted(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrAnchorManager::sceneCaptureCompleted()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxranchormanager.html#sceneCaptureCompleted
    """
    #  void QQuick3DXrAnchorManager::sceneCaptureCompleted()
    self.uglySide.call(
        'ritual_ZN23QQuick3DXrAnchorManager21sceneCaptureCompletedEv',
    )

  @staticmethod
  def addAnchor(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrAnchorManager::addAnchor(QQuick3DXrSpatialAnchor
    *anchor)': cannot be called and cannot be called through the meta-object
    and cannot be copied: no header file has its code, Qt's source does not
    mark it or its class for use from outside Qt or writes it 'inline' or
    nowhere, and it is no signal, slot or invokable function giving back
    nothing, of a class built on QObject, and Qt's source has no code for it
    that could be told from the rest.
    """
    raise NotImplementedError(
        "'QQuick3DXrAnchorManager.addAnchor' has no cute function yet. Qt's "
        "'void QQuick3DXrAnchorManager::addAnchor(QQuick3DXrSpatialAnchor "
        "*anchor)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def getBoundingBox2D(*__, **_) -> Never:
    """
    Qt's 'bool
    QQuick3DXrAnchorManager::getBoundingBox2D(QtQuick3DXr::XrSpaceId space,
    QVector2D &offset, QVector2D &extent)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQuick3DXrAnchorManager.getBoundingBox2D' has no cute function "
        "yet. Qt's 'bool "
        "QQuick3DXrAnchorManager::getBoundingBox2D(QtQuick3DXr::XrSpaceId "
        "space, QVector2D &offset, QVector2D &extent)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def getBoundingBox3D(*__, **_) -> Never:
    """
    Qt's 'bool
    QQuick3DXrAnchorManager::getBoundingBox3D(QtQuick3DXr::XrSpaceId space,
    QVector3D &offset, QVector3D &extent)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQuick3DXrAnchorManager.getBoundingBox3D' has no cute function "
        "yet. Qt's 'bool "
        "QQuick3DXrAnchorManager::getBoundingBox3D(QtQuick3DXr::XrSpaceId "
        "space, QVector3D &offset, QVector3D &extent)': takes a type Python "
        "has no way to hand over yet.")

  @staticmethod
  def initAnchorManager(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrAnchorManager::initAnchorManager()': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QQuick3DXrAnchorManager.initAnchorManager' has no cute function "
        "yet. Qt's 'void QQuick3DXrAnchorManager::initAnchorManager()': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def planeUpdateHandler(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrAnchorManager::planeUpdateHandler(void *a0,
    ar_plane_anchors_t a1, ar_plane_anchors_t a2, ar_plane_anchors_t a3)':
    cannot be called and cannot be called through the meta-object and cannot
    be copied: no header file has its code, Qt's source does not mark it or
    its class for use from outside Qt or writes it 'inline' or nowhere, and
    it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QQuick3DXrAnchorManager.planeUpdateHandler' has no cute function "
        "yet. Qt's 'void QQuick3DXrAnchorManager::planeUpdateHandler(void "
        "*a0, ar_plane_anchors_t a1, ar_plane_anchors_t a2, "
        "ar_plane_anchors_t a3)': cannot be called and cannot be called "
        "through the meta-object and cannot be copied: no header file has "
        "its code, Qt's source does not mark it or its class for use from "
        "outside Qt or writes it 'inline' or nowhere, and it is no signal, "
        "slot or invokable function giving back nothing, of a class built "
        "on QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def populateAnchorsList(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrAnchorManager::populateAnchorsList()': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QQuick3DXrAnchorManager.populateAnchorsList' has no cute function "
        "yet. Qt's 'void QQuick3DXrAnchorManager::populateAnchorsList()': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def prepareAnchorManager(*__, **_) -> Never:
    """
    Qt's 'void
    QQuick3DXrAnchorManager::prepareAnchorManager(ar_data_providers_t
    dataProviders)': cannot be called and cannot be called through the
    meta-object and cannot be copied: no header file has its code, Qt's
    source does not mark it or its class for use from outside Qt or writes it
    'inline' or nowhere, and it is no signal, slot or invokable function
    giving back nothing, of a class built on QObject, and Qt's source has no
    code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QQuick3DXrAnchorManager.prepareAnchorManager' has no cute "
        "function yet. Qt's 'void "
        "QQuick3DXrAnchorManager::prepareAnchorManager(ar_data_providers_t "
        "dataProviders)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def removeAnchor(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrAnchorManager::removeAnchor(QUuid uuid)': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QQuick3DXrAnchorManager.removeAnchor' has no cute function yet. "
        "Qt's 'void QQuick3DXrAnchorManager::removeAnchor(QUuid uuid)': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def setupSpatialAnchor(*__, **_) -> Never:
    """
    Qt's 'bool
    QQuick3DXrAnchorManager::setupSpatialAnchor(QtQuick3DXr::XrSpaceId space,
    QQuick3DXrSpatialAnchor &anchor)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QQuick3DXrAnchorManager.setupSpatialAnchor' has no cute function "
        "yet. Qt's 'bool "
        "QQuick3DXrAnchorManager::setupSpatialAnchor(QtQuick3DXr::XrSpaceId "
        "space, QQuick3DXrSpatialAnchor &anchor)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def updateAnchor(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrAnchorManager::updateAnchor(QQuick3DXrSpatialAnchor
    *anchor)': cannot be called and cannot be called through the meta-object
    and cannot be copied: no header file has its code, Qt's source does not
    mark it or its class for use from outside Qt or writes it 'inline' or
    nowhere, and it is no signal, slot or invokable function giving back
    nothing, of a class built on QObject, and Qt's source has no code for it
    that could be told from the rest.
    """
    raise NotImplementedError(
        "'QQuick3DXrAnchorManager.updateAnchor' has no cute function yet. "
        "Qt's 'void "
        "QQuick3DXrAnchorManager::updateAnchor(QQuick3DXrSpatialAnchor "
        "*anchor)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")
