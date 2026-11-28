"""
Qt3DRender::Render::SceneManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/scenemanager_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DRender::Render::SceneManager to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QUrl
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class SceneManager(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's Qt3DRender::Render::SceneManager: a plain Python
  object standing in front of one C++ Qt3DRender::Render::SceneManager.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::SceneManager that has a ritual
  and that Python can call so far, 4 names in all: 'setDownloadService',
  'addSceneData', 'startSceneDownload', 'clearSceneDownload'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::Render::SceneManager::~SceneManager()': the destructor:
    Python never removes a C++ Qt3DRender::Render::SceneManager.
  - Qt's 'std::vector<LoadSceneJobPtr>
    Qt3DRender::Render::SceneManager::takePendingSceneLoaderJobs()': gives a
    type Python has no way to take yet.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::SceneManager is created at the first use, not
    by 'Qt3DRender::Render::SceneManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::SceneManager.
  - Each name of Qt's Qt3DRender::Render::SceneManager that has no cute
    function yet, 'takePendingSceneLoaderJobs', holds a function that raises
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
  __qt_class__ = 'Qt3DRender::Render::SceneManager'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(WAIT['Qt3DCore.QDownloadHelperService'])
  @overload(NoneType)
  def setDownloadService(
      self,
      service: Optional[Qt3DCore.QDownloadHelperService],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::SceneManager::setDownloadService(Qt3DCore::
    QDownloadHelperService *service)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-scenemanager.html

    Parameters
    ----------

    service : Optional[Qt3DCore.QDownloadHelperService]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::SceneManager::setDownloadService(Qt3DCore::
    #      QDownloadHelperService *service)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render12SceneManager18setDownloadServiceEPN8'
        'Qt3DCore22QDownloadHelperServiceE',
        self._addressOf(service),
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
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::Render::SceneManager::SceneManager()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-scenemanager.html#SceneManager
    """
    #  Qt3DRender::Render::SceneManager::SceneManager()
    self._noteCreation(SceneManager, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render12SceneManagerC1Ev',
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

  @overload(QUrl, WAIT['Qt3DCore.QNodeId'])
  @overload(QUrl, WAIT['Qt3DCore.QNodeId'], QByteArray)
  def addSceneData(
      self,
      source: QUrl,
      sceneUuid: Qt3DCore.QNodeId,
      data: Optional[QByteArray] = None,
  ) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::SceneManager::addSceneData(const
    QUrl &source, Qt3DCore::QNodeId sceneUuid, const QByteArray &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-scenemanager.html#addSceneData

    Parameters
    ----------

    source : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    sceneUuid : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.

    data : Optional[QByteArray]
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own. May be left out, as in Qt: a new 'QByteArray()' is then passed on.
    """
    #  void Qt3DRender::Render::SceneManager::addSceneData(const QUrl
    #      &source, Qt3DCore::QNodeId sceneUuid, const QByteArray &data)
    if data is None:
      from ..QtCore import QByteArray
      data = QByteArray()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render12SceneManager12addSceneDataERK4QUrlN8'
        'Qt3DCore7QNodeIdERK10QByteArray',
        self._valueOf(source), self._valueOf(sceneUuid), self._valueOf(data),
    )

  @overload(QUrl, WAIT['Qt3DCore.QNodeId'])
  def startSceneDownload(
      self,
      source: QUrl,
      sceneUuid: Qt3DCore.QNodeId,
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::SceneManager::startSceneDownload(const QUrl &source,
    Qt3DCore::QNodeId sceneUuid)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-scenemanager.html

    Parameters
    ----------

    source : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    sceneUuid : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  void Qt3DRender::Render::SceneManager::startSceneDownload(const QUrl
    #      &source, Qt3DCore::QNodeId sceneUuid)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render12SceneManager18startSceneDownloadERK4'
        'QUrlN8Qt3DCore7QNodeIdE',
        self._valueOf(source), self._valueOf(sceneUuid),
    )

  @overload(WAIT['Qt3DRender.Render.SceneDownloader'])
  @overload(NoneType)
  def clearSceneDownload(
      self,
      downloader: Optional[Qt3DRender.Render.SceneDownloader],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::SceneManager::clearSceneDownload(SceneDownloader
    *downloader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-scenemanager.html

    Parameters
    ----------

    downloader : Optional[Qt3DRender.Render.SceneDownloader]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::SceneManager::clearSceneDownload(
    #      SceneDownloader *downloader)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render12SceneManager18clearSceneDownloadEPNS'
        '0_15SceneDownloaderE',
        self._addressOf(downloader),
    )

  @staticmethod
  def takePendingSceneLoaderJobs(*__, **_) -> Never:
    """
    Qt's 'std::vector<LoadSceneJobPtr>
    Qt3DRender::Render::SceneManager::takePendingSceneLoaderJobs()': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.SceneManager.takePendingSceneLoaderJobs' has no "
        "cute function yet. Qt's 'std::vector<LoadSceneJobPtr> "
        "Qt3DRender::Render::SceneManager::takePendingSceneLoaderJobs()': "
        "gives a type Python has no way to take yet.")
