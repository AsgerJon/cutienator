"""
Qt3DRender::MeshLoaderFunctor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/qmesh_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means Qt3DRender::MeshLoaderFunctor to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class MeshLoaderFunctor(Qt3DCore.QGeometryFactory):
  """
  The cute side of Qt's Qt3DRender::MeshLoaderFunctor: a plain Python object
  standing in front of one C++ Qt3DRender::MeshLoaderFunctor.

  It is built on the cute 'Qt3DCore::QGeometryFactory', as Qt's
  Qt3DRender::MeshLoaderFunctor is built on Qt's Qt3DCore::QGeometryFactory,
  and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::MeshLoaderFunctor that has a ritual and
  that Python can call so far, 12 names in all: 'setNodeManagers',
  'nodeManagers', 'setDownloaderService', 'downloaderService',
  'setSourceData', 'sourceData', 'sourcePath', 'mesh', 'meshName', 'status',
  '__call__', 'id'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'bool Qt3DRender::MeshLoaderFunctor::equals(const
    Qt3DCore::QGeometryFactory &other) const': takes a type Python has no way
    to hand over yet.

  What to expect
  --------------

  - The C++ Qt3DRender::MeshLoaderFunctor is created at the first use, not by
    'Qt3DRender::MeshLoaderFunctor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::MeshLoaderFunctor.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::MeshLoaderFunctor'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def nodeManagers(self) -> Optional[Qt3DRender.Render.NodeManagers]:
    """
    Calls Qt's 'Render::NodeManagers
    *Qt3DRender::MeshLoaderFunctor::nodeManagers() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-meshloaderfunctor.html#nodeManagers

    Returns
    -------

    Optional[Qt3DRender.Render.NodeManagers]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Render::NodeManagers *Qt3DRender::MeshLoaderFunctor::nodeManagers()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender17MeshLoaderFunctor12nodeManagersEv',
    )
    return Qt3DRender.Render.NodeManagers._cuteAt(address)

  def downloaderService(self) -> Optional[Qt3DCore.QDownloadHelperService]:
    """
    Calls Qt's 'Qt3DCore::QDownloadHelperService
    *Qt3DRender::MeshLoaderFunctor::downloaderService() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-meshloaderfunctor.html

    Returns
    -------

    Optional[Qt3DCore.QDownloadHelperService]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QDownloadHelperService
    #      *Qt3DRender::MeshLoaderFunctor::downloaderService() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender17MeshLoaderFunctor17downloaderServiceEv',
    )
    return Qt3DCore.QDownloadHelperService._cuteAt(address)

  def sourceData(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray Qt3DRender::MeshLoaderFunctor::sourceData()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-meshloaderfunctor.html#sourceData

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray Qt3DRender::MeshLoaderFunctor::sourceData() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender17MeshLoaderFunctor10sourceDataEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def sourcePath(self) -> QUrl:
    """
    Calls Qt's 'QUrl Qt3DRender::MeshLoaderFunctor::sourcePath() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-meshloaderfunctor.html#sourcePath

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl Qt3DRender::MeshLoaderFunctor::sourcePath() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender17MeshLoaderFunctor10sourcePathEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def mesh(self) -> Qt3DCore.QNodeId:
    """
    Calls Qt's 'Qt3DCore::QNodeId Qt3DRender::MeshLoaderFunctor::mesh()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-meshloaderfunctor.html#mesh

    Returns
    -------

    Qt3DCore.QNodeId
      A new cute Qt3DCore::QNodeId around the copy Qt gave back. Python owns
      it.
    """
    #  Qt3DCore::QNodeId Qt3DRender::MeshLoaderFunctor::mesh() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender17MeshLoaderFunctor4meshEv',
    )
    return Qt3DCore.QNodeId._cuteOwning(address)

  def meshName(self) -> str:
    """
    Calls Qt's 'QString Qt3DRender::MeshLoaderFunctor::meshName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-meshloaderfunctor.html#meshName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString Qt3DRender::MeshLoaderFunctor::meshName() const
    return self.uglySide.call(
        'ritual_ZNK10Qt3DRender17MeshLoaderFunctor8meshNameEv',
    )

  def status(self) -> Qt3DRender.QMesh.Status:
    """
    Calls Qt's 'QMesh::Status Qt3DRender::MeshLoaderFunctor::status() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-meshloaderfunctor.html#status

    Returns
    -------

    Qt3DRender.QMesh.Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'Qt3DRender.QMesh.Status(number)' gives.
    """
    #  QMesh::Status Qt3DRender::MeshLoaderFunctor::status() const
    return Qt3DRender.QMesh.Status(self.uglySide.call(
        'ritual_ZNK10Qt3DRender17MeshLoaderFunctor6statusEv',
    ))

  def id(self) -> int:
    """
    Calls Qt's 'qintptr Qt3DRender::MeshLoaderFunctor::id() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-meshloaderfunctor.html#id
    """
    #  qintptr Qt3DRender::MeshLoaderFunctor::id() const
    ritual = 'ritual_ZNK10Qt3DRender17MeshLoaderFunctor2idEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK10Qt3DRender17MeshLoaderFunctor2idEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DRender.Render.NodeManagers'])
  @overload(NoneType)
  def setNodeManagers(
      self,
      managers: Optional[Qt3DRender.Render.NodeManagers],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::MeshLoaderFunctor::setNodeManagers(Render::NodeManagers
    *managers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-meshloaderfunctor.html#setNodeManagers

    Parameters
    ----------

    managers : Optional[Qt3DRender.Render.NodeManagers]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::MeshLoaderFunctor::setNodeManagers(Render::
    #      NodeManagers *managers)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender17MeshLoaderFunctor15setNodeManagersEPNS_6Ren'
        'der12NodeManagersE',
        self._addressOf(managers),
    )

  @overload(WAIT['Qt3DCore.QDownloadHelperService'])
  @overload(NoneType)
  def setDownloaderService(
      self,
      service: Optional[Qt3DCore.QDownloadHelperService],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::MeshLoaderFunctor::setDownloaderService(Qt3DCore::
    QDownloadHelperService *service)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-meshloaderfunctor.html

    Parameters
    ----------

    service : Optional[Qt3DCore.QDownloadHelperService]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::MeshLoaderFunctor::setDownloaderService(Qt3DCore::
    #      QDownloadHelperService *service)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender17MeshLoaderFunctor20setDownloaderServiceEPN8'
        'Qt3DCore22QDownloadHelperServiceE',
        self._addressOf(service),
    )

  @overload(QByteArray)
  def setSourceData(self, data: QByteArray) -> None:
    """
    Calls Qt's 'void Qt3DRender::MeshLoaderFunctor::setSourceData(const
    QByteArray &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-meshloaderfunctor.html#setSourceData

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void Qt3DRender::MeshLoaderFunctor::setSourceData(const QByteArray
    #      &data)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender17MeshLoaderFunctor13setSourceDataERK10QByteA'
        'rray',
        self._valueOf(data),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def __call__(self) -> Optional[Qt3DCore.QGeometry]:
    """
    Calls Qt's 'Qt3DCore::QGeometry
    *Qt3DRender::MeshLoaderFunctor::operator()()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-meshloaderfunctor.html#operator()

    Returns
    -------

    Optional[Qt3DCore.QGeometry]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Qt3DCore::QGeometry *Qt3DRender::MeshLoaderFunctor::operator()()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender17MeshLoaderFunctorclEv',
    )
    return Qt3DCore.QGeometry._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DRender.QMesh'])
  @overload(NoneType)
  @overload(WAIT['Qt3DRender.QMesh'], QByteArray)
  @overload(NoneType, QByteArray)
  def __init__(
      self,
      mesh: Optional[Qt3DRender.QMesh],
      sourceData: Optional[QByteArray] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::MeshLoaderFunctor::MeshLoaderFunctor(QMesh *mesh, const
    QByteArray &sourceData)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-meshloaderfunctor.html

    Parameters
    ----------

    mesh : Optional[Qt3DRender.QMesh]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    sourceData : Optional[QByteArray]
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own. May be left out, as in Qt: a new 'QByteArray()' is then passed on.
    """
    #  Qt3DRender::MeshLoaderFunctor::MeshLoaderFunctor(QMesh *mesh, const
    #      QByteArray &sourceData)
    if sourceData is None:
      from ..QtCore import QByteArray
      sourceData = QByteArray()
    self._noteCreation(MeshLoaderFunctor, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender17MeshLoaderFunctorC1EPNS_5QMeshERK10QByteArr'
        'ay',
        self._addressOf(mesh), self._valueOf(sourceData),
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
