"""
Qt3DRender::Render::LoadSceneJob binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/loadscenejob_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DRender::Render::LoadSceneJob to be private: it declares the
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


class LoadSceneJob(Qt3DCore.QAspectJob):
  """
  The cute side of Qt's Qt3DRender::Render::LoadSceneJob: a plain Python
  object standing in front of one C++ Qt3DRender::Render::LoadSceneJob.

  It is built on the cute 'Qt3DCore::QAspectJob', as Qt's
  Qt3DRender::Render::LoadSceneJob is built on Qt's Qt3DCore::QAspectJob, and
  has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::Render::LoadSceneJob that has a ritual
  and that Python can call so far, 7 names in all: 'setData',
  'setNodeManagers', 'nodeManagers', 'source', 'sceneComponentId', 'run',
  'd_func'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void Qt3DRender::Render::LoadSceneJob::setSceneImporters(const
    QList<QSceneImporter *> sceneImporters)': takes a type Python has no way
    to hand over yet.
  - Qt's 'QList<QSceneImporter *>
    Qt3DRender::Render::LoadSceneJob::sceneImporters() const': gives a type
    Python has no way to take yet.
  - Qt's 'Qt3DCore::QEntity
    *Qt3DRender::Render::LoadSceneJob::tryLoadScene(QSceneLoader::Status
    &finalStatus, const QStringList &extensions, const std::function<void
    (QSceneImporter *)> &importerSetupFunc)': takes a type Python has no way
    to hand over yet.
  - Qt's 'const LoadSceneJobPrivate
    *Qt3DRender::Render::LoadSceneJob::d_func() const': takes in Python what
    'LoadSceneJobPrivate *Qt3DRender::Render::LoadSceneJob::d_func()' takes.

  What to expect
  --------------

  - The C++ Qt3DRender::Render::LoadSceneJob is created at the first use, not
    by 'Qt3DRender::Render::LoadSceneJob(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::Render::LoadSceneJob.
  - Each name of Qt's Qt3DRender::Render::LoadSceneJob that has no cute
    function yet, 'sceneImporters', 'setSceneImporters', 'tryLoadScene',
    holds a function that raises 'NotImplementedError', and its docstring
    says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::Render::LoadSceneJob'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def nodeManagers(self) -> Optional[Qt3DRender.Render.NodeManagers]:
    """
    Calls Qt's 'NodeManagers
    *Qt3DRender::Render::LoadSceneJob::nodeManagers() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-loadscenejob.html#nodeManagers

    Returns
    -------

    Optional[Qt3DRender.Render.NodeManagers]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  NodeManagers *Qt3DRender::Render::LoadSceneJob::nodeManagers() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12LoadSceneJob12nodeManagersEv',
    )
    return Qt3DRender.Render.NodeManagers._cuteAt(address)

  def source(self) -> QUrl:
    """
    Calls Qt's 'QUrl Qt3DRender::Render::LoadSceneJob::source() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-loadscenejob.html#source

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl Qt3DRender::Render::LoadSceneJob::source() const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12LoadSceneJob6sourceEv',
    )
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def sceneComponentId(self) -> Qt3DCore.QNodeId:
    """
    Calls Qt's 'Qt3DCore::QNodeId
    Qt3DRender::Render::LoadSceneJob::sceneComponentId() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-loadscenejob.html

    Returns
    -------

    Qt3DCore.QNodeId
      A new cute Qt3DCore::QNodeId around the copy Qt gave back. Python owns
      it.
    """
    #  Qt3DCore::QNodeId Qt3DRender::Render::LoadSceneJob::sceneComponentId()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK10Qt3DRender6Render12LoadSceneJob16sceneComponentIdEv',
    )
    return Qt3DCore.QNodeId._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QByteArray)
  def setData(self, data: QByteArray) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::LoadSceneJob::setData(const
    QByteArray &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-loadscenejob.html#setData

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void Qt3DRender::Render::LoadSceneJob::setData(const QByteArray &data)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render12LoadSceneJob7setDataERK10QByteArray',
        self._valueOf(data),
    )

  @overload(WAIT['Qt3DRender.Render.NodeManagers'])
  @overload(NoneType)
  def setNodeManagers(
      self,
      managers: Optional[Qt3DRender.Render.NodeManagers],
  ) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::Render::LoadSceneJob::setNodeManagers(NodeManagers
    *managers)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-loadscenejob.html

    Parameters
    ----------

    managers : Optional[Qt3DRender.Render.NodeManagers]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void Qt3DRender::Render::LoadSceneJob::setNodeManagers(NodeManagers
    #      *managers)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render12LoadSceneJob15setNodeManagersEPNS0_1'
        '2NodeManagersE',
        self._addressOf(managers),
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

  @overload(QUrl, WAIT['Qt3DCore.QNodeId'])
  def __init__(self, source: QUrl, sceneComponent: Qt3DCore.QNodeId) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::Render::LoadSceneJob::LoadSceneJob(const QUrl &source,
    Qt3DCore::QNodeId sceneComponent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-loadscenejob.html#LoadSceneJob

    Parameters
    ----------

    source : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    sceneComponent : Qt3DCore.QNodeId
      Passed on as a value: Qt reads the C++ Qt3DCore::QNodeId, which stays
      Python's own.
    """
    #  Qt3DRender::Render::LoadSceneJob::LoadSceneJob(const QUrl &source,
    #      Qt3DCore::QNodeId sceneComponent)
    self._noteCreation(LoadSceneJob, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender6Render12LoadSceneJobC1ERK4QUrlN8Qt3DCore7QNo'
        'deIdE',
        self._valueOf(source), self._valueOf(sceneComponent),
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

  def run(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::Render::LoadSceneJob::run()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-loadscenejob.html#run
    """
    #  void Qt3DRender::Render::LoadSceneJob::run()
    ritual = 'ritual_ZN10Qt3DRender6Render12LoadSceneJob3runEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10Qt3DRender6Render12LoadSceneJob3runEv'
    self.uglySide.call(ritual)

  def d_func(self) -> Optional[Qt3DRender.Render.LoadSceneJobPrivate]:
    """
    Calls Qt's 'LoadSceneJobPrivate
    *Qt3DRender::Render::LoadSceneJob::d_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-render-loadscenejob.html#d_func

    Returns
    -------

    Optional[Qt3DRender.Render.LoadSceneJobPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  LoadSceneJobPrivate *Qt3DRender::Render::LoadSceneJob::d_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender6Render12LoadSceneJob6d_funcEv',
    )
    return Qt3DRender.Render.LoadSceneJobPrivate._cuteAt(address)

  @staticmethod
  def sceneImporters(*__, **_) -> Never:
    """
    Qt's 'QList<QSceneImporter *>
    Qt3DRender::Render::LoadSceneJob::sceneImporters() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.LoadSceneJob.sceneImporters' has no cute "
        "function yet. Qt's 'QList<QSceneImporter *> "
        "Qt3DRender::Render::LoadSceneJob::sceneImporters() const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def setSceneImporters(*__, **_) -> Never:
    """
    Qt's 'void Qt3DRender::Render::LoadSceneJob::setSceneImporters(const
    QList<QSceneImporter *> sceneImporters)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.LoadSceneJob.setSceneImporters' has no cute "
        "function yet. Qt's 'void "
        "Qt3DRender::Render::LoadSceneJob::setSceneImporters(const "
        "QList<QSceneImporter *> sceneImporters)': takes a type Python has "
        "no way to hand over yet.")

  @staticmethod
  def tryLoadScene(*__, **_) -> Never:
    """
    Qt's 'Qt3DCore::QEntity
    *Qt3DRender::Render::LoadSceneJob::tryLoadScene(QSceneLoader::Status
    &finalStatus, const QStringList &extensions, const std::function<void
    (QSceneImporter *)> &importerSetupFunc)': takes a type Python has no way
    to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.Render.LoadSceneJob.tryLoadScene' has no cute function "
        "yet. Qt's 'Qt3DCore::QEntity "
        "*Qt3DRender::Render::LoadSceneJob::tryLoadScene(QSceneLoader::Statu"
        "s &finalStatus, const QStringList &extensions, const "
        "std::function<void (QSceneImporter *)> &importerSetupFunc)': takes "
        "a type Python has no way to hand over yet.")
