"""
Qt3DRender::QSceneLoader binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/qsceneloader.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QStringList
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSceneLoader(Qt3DCore.QComponent):
  """
  The cute side of Qt's Qt3DRender::QSceneLoader: a plain Python object
  standing in front of one C++ Qt3DRender::QSceneLoader.

  It is built on the cute 'Qt3DCore::QComponent', as Qt's
  Qt3DRender::QSceneLoader is built on Qt's Qt3DCore::QComponent, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QSceneLoader that has a ritual and that
  Python can call so far, 11 names in all: 'metaObject', 'tr', 'source',
  'status', 'entity', 'entityNames', 'component', 'setSource',
  'sourceChanged', 'statusChanged', 'd_func'. It can be made from Python, in
  1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *Qt3DRender::QSceneLoader::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int Qt3DRender::QSceneLoader::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'Qt3DRender::QSceneLoader::~QSceneLoader()': the destructor: Python
    never removes a C++ Qt3DRender::QSceneLoader.
  - Qt's 'Qt3DRender::QSceneLoader::QSceneLoader(QSceneLoaderPrivate &dd,
    Qt3DCore::QNode *parent)': takes a type Python has no way to hand over
    yet.
  - Qt's 'const QSceneLoaderPrivate *Qt3DRender::QSceneLoader::d_func()
    const': takes in Python what 'QSceneLoaderPrivate
    *Qt3DRender::QSceneLoader::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 19 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ Qt3DRender::QSceneLoader is created at the first use, not by
    'Qt3DRender::QSceneLoader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QSceneLoader.
  - Qt tells when it has removed the C++ Qt3DRender::QSceneLoader. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside Qt3DRender::QSceneLoader, each a class in
  #  here as in C++, and the names Qt has for the combinations of its flags
  #  enums.

  class ComponentType(CuteNum):
    """
    The enum 'Qt3DRender::QSceneLoader::ComponentType' of Qt, with the 6
    names Qt gives in it.
    """

    UnknownComponent = Kee[int](0)
    GeometryRendererComponent = Kee[int](1)
    TransformComponent = Kee[int](2)
    MaterialComponent = Kee[int](3)
    LightComponent = Kee[int](4)
    CameraLensComponent = Kee[int](5)

  class Status(CuteNum):
    """
    The enum 'Qt3DRender::QSceneLoader::Status' of Qt, with the 4 names Qt
    gives in it.
    """

    NULL = Kee[int](0)
    Loading = Kee[int](1)
    Ready = Kee[int](2)
    Error = Kee[int](3)

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
    Calls Qt's 'QString Qt3DRender::QSceneLoader::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qt3drender-qsceneloader.html#tr

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
    #  QString Qt3DRender::QSceneLoader::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN10Qt3DRender12QSceneLoader2trEPKcS2_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QSceneLoader'

  #  A C++ Qt3DRender::QSceneLoader Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QSceneLoader'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *Qt3DRender::QSceneLoader::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qsceneloader.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *Qt3DRender::QSceneLoader::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender12QSceneLoader10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def source(self) -> QUrl:
    """
    Calls Qt's 'QUrl Qt3DRender::QSceneLoader::source() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qsceneloader.html#source

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl Qt3DRender::QSceneLoader::source() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender12QSceneLoader6sourceEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def status(self) -> Status:
    """
    Calls Qt's 'Status Qt3DRender::QSceneLoader::status() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qsceneloader.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status Qt3DRender::QSceneLoader::status() const
    return QSceneLoader.Status(self.uglySide.call(
        'ritual_ZNK10Qt3DRender12QSceneLoader6statusEv',
    ))

  @overload(str)
  def entity(self, entityName: str) -> Optional[Qt3DCore.QEntity]:
    """
    Calls Qt's 'Qt3DCore::QEntity *Qt3DRender::QSceneLoader::entity(const
    QString &entityName) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qsceneloader.html#entity

    Parameters
    ----------

    entityName : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[Qt3DCore.QEntity]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QEntity *Qt3DRender::QSceneLoader::entity(const QString
    #      &entityName) const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender12QSceneLoader6entityERK7QString', entityName,
    )
    return Qt3DCore.QEntity._cuteAt(address)

  def entityNames(self) -> QStringList:
    """
    Calls Qt's 'QStringList Qt3DRender::QSceneLoader::entityNames() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qsceneloader.html#entityNames

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList Qt3DRender::QSceneLoader::entityNames() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender12QSceneLoader11entityNamesEv',
    )
    return QStringList._cuteOwning(address)

  @overload(str, ComponentType)
  def component(
      self,
      entityName: str,
      componentType: ComponentType,
  ) -> Optional[Qt3DCore.QComponent]:
    """
    Calls Qt's 'Qt3DCore::QComponent
    *Qt3DRender::QSceneLoader::component(const QString &entityName,
    ComponentType componentType) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qsceneloader.html#component

    Parameters
    ----------

    entityName : str
      Passed on as it is: a QString is made of it for the call.

    componentType : ComponentType
      Passed on as its number.

    Returns
    -------

    Optional[Qt3DCore.QComponent]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QComponent *Qt3DRender::QSceneLoader::component(const
    #      QString &entityName, ComponentType componentType) const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender12QSceneLoader9componentERK7QStringNS0_13Com'
        'ponentTypeE',
        entityName, componentType.value,
    )
    return Qt3DCore.QComponent._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setSource(self, arg: QUrl) -> None:
    """
    Calls Qt's 'void Qt3DRender::QSceneLoader::setSource(const QUrl &arg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qsceneloader.html#setSource

    Parameters
    ----------

    arg : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void Qt3DRender::QSceneLoader::setSource(const QUrl &arg)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender12QSceneLoader9setSourceERK4QUrl',
        self._valueOf(arg),
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
  @overload(Qt3DCore.QNode)
  @overload(NoneType)
  def __init__(self, parent: Optional[Qt3DCore.QNode] = None) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::QSceneLoader::QSceneLoader(Qt3DCore::QNode *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qsceneloader.html#QSceneLoader

    Parameters
    ----------

    parent : Optional[Qt3DCore.QNode]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  Qt3DRender::QSceneLoader::QSceneLoader(Qt3DCore::QNode *parent)
    self._noteCreation(QSceneLoader, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender12QSceneLoaderC1EPN8Qt3DCore5QNodeE',
        self._addressOf(parent),
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

  @overload(QUrl)
  def sourceChanged(self, source: QUrl) -> None:
    """
    Calls Qt's 'void Qt3DRender::QSceneLoader::sourceChanged(const QUrl
    &source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qsceneloader.html#sourceChanged

    Parameters
    ----------

    source : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void Qt3DRender::QSceneLoader::sourceChanged(const QUrl &source)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender12QSceneLoader13sourceChangedERK4QUrl',
        self._valueOf(source),
    )

  @overload(Status)
  def statusChanged(self, status: Status) -> None:
    """
    Calls Qt's 'void Qt3DRender::QSceneLoader::statusChanged(Status status)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qsceneloader.html#statusChanged

    Parameters
    ----------

    status : Status
      Passed on as its number.
    """
    #  void Qt3DRender::QSceneLoader::statusChanged(Status status)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender12QSceneLoader13statusChangedENS0_6StatusE',
        status.value,
    )

  def d_func(self) -> Optional[Qt3DRender.QSceneLoaderPrivate]:
    """
    Calls Qt's 'QSceneLoaderPrivate *Qt3DRender::QSceneLoader::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qsceneloader.html#d_func

    Returns
    -------

    Optional[Qt3DRender.QSceneLoaderPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSceneLoaderPrivate *Qt3DRender::QSceneLoader::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender12QSceneLoader6d_funcEv',
    )
    return Qt3DRender.QSceneLoaderPrivate._cuteAt(address)
