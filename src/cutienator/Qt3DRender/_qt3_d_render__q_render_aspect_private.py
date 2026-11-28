"""
Qt3DRender::QRenderAspectPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  Qt3DRender/6.12.0/Qt3DRender/private/qrenderaspect_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means Qt3DRender::QRenderAspectPrivate to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..Qt3DCore import Qt3DCore
from . import Qt3DRender

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QObject
  from ..QtGui import QKeyEvent, QMouseEvent
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QKeyEvent = WAIT['QKeyEvent']
  QMouseEvent = WAIT['QMouseEvent']
  QObject = WAIT['QObject']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QRenderAspectPrivate(Qt3DCore.QAbstractAspectPrivate):
  """
  The cute side of Qt's Qt3DRender::QRenderAspectPrivate: a plain Python
  object standing in front of one C++ Qt3DRender::QRenderAspectPrivate.

  It is built on the cute 'Qt3DCore::QAbstractAspectPrivate', as Qt's
  Qt3DRender::QRenderAspectPrivate is built on Qt's
  Qt3DCore::QAbstractAspectPrivate, and has everything that class has.

  What exists
  -----------

  Every function of Qt's Qt3DRender::QRenderAspectPrivate that has a ritual
  and that Python can call so far, 16 names in all: 'q_func', 'findPrivate',
  'get', 'jobsDone', 'frameDone', 'createNodeManagers', 'onEngineStartup',
  'onEngineAboutToShutdown', 'registerBackendTypes',
  'unregisterBackendTypes', 'loadSceneImporters', 'loadRenderPlugin',
  'loadRendererPlugin', 'processMouseEvent', 'processKeyEvent',
  'configurePlugin'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'Qt3DRender::QRenderAspectPrivate::~QRenderAspectPrivate()': the
    destructor: Python never removes a C++ Qt3DRender::QRenderAspectPrivate.
  - Qt's 'const QRenderAspect *Qt3DRender::QRenderAspectPrivate::q_func()
    const': takes in Python what 'QRenderAspect
    *Qt3DRender::QRenderAspectPrivate::q_func()' takes.
  - Qt's 'void Qt3DRender::QRenderAspectPrivate::registerBackendType(const
    QMetaObject &a0, const Qt3DCore::QBackendNodeMapperPtr &functor)': takes
    a type Python has no way to hand over yet.
  - Qt's 'std::vector<Qt3DCore::QAspectJobPtr>
    Qt3DRender::QRenderAspectPrivate::createGeometryRendererJobs() const':
    gives a type Python has no way to take yet.
  - Qt's 'std::vector<Qt3DCore::QAspectJobPtr>
    Qt3DRender::QRenderAspectPrivate::createPreRendererJobs() const': gives a
    type Python has no way to take yet.

  What has no ritual
  ------------------

  1 of the 23 functions Qt declares: 1 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ Qt3DRender::QRenderAspectPrivate is created at the first use, not
    by 'Qt3DRender::QRenderAspectPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ Qt3DRender::QRenderAspectPrivate.
  - Each name of Qt's Qt3DRender::QRenderAspectPrivate that has no cute
    function yet, 'createGeometryRendererJobs', 'createPreRendererJobs',
    'createRenderBufferJobs', 'registerBackendType', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  @overload(WAIT['Qt3DCore.QAspectEngine'])
  @overload(NoneType)
  def findPrivate(
      engine: Optional[Qt3DCore.QAspectEngine],
  ) -> Optional[QRenderAspectPrivate]:
    """
    Calls Qt's 'QRenderAspectPrivate
    *Qt3DRender::QRenderAspectPrivate::findPrivate(Qt3DCore::QAspectEngine
    *engine)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrenderaspectprivate.html#findPrivate

    Parameters
    ----------

    engine : Optional[Qt3DCore.QAspectEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QRenderAspectPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRenderAspectPrivate
    #      *Qt3DRender::QRenderAspectPrivate::findPrivate(Qt3DCore::
    #      QAspectEngine *engine)
    address = Rituals.call(
        'ritual_ZN10Qt3DRender20QRenderAspectPrivate11findPrivateEPN8Qt3DCo'
        're13QAspectEngineE',
        CuteMixin._addressOf(engine),
    )
    return QRenderAspectPrivate._cuteAt(address)

  @staticmethod
  @overload(WAIT['Qt3DRender.QRenderAspect'])
  @overload(NoneType)
  def get(
      q: Optional[Qt3DRender.QRenderAspect],
  ) -> Optional[QRenderAspectPrivate]:
    """
    Calls Qt's 'QRenderAspectPrivate
    *Qt3DRender::QRenderAspectPrivate::get(QRenderAspect *q)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrenderaspectprivate.html#get

    Parameters
    ----------

    q : Optional[Qt3DRender.QRenderAspect]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QRenderAspectPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRenderAspectPrivate
    #      *Qt3DRender::QRenderAspectPrivate::get(QRenderAspect *q)
    address = Rituals.call(
        'ritual_ZN10Qt3DRender20QRenderAspectPrivate3getEPNS_13QRenderAspec'
        'tE',
        CuteMixin._addressOf(q),
    )
    return QRenderAspectPrivate._cuteAt(address)

  @staticmethod
  @overload(str)
  def configurePlugin(plugin: str) -> None:
    """
    Calls Qt's 'void Qt3DRender::QRenderAspectPrivate::configurePlugin(const
    QString &plugin)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrenderaspectprivate.html

    Parameters
    ----------

    plugin : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DRender::QRenderAspectPrivate::configurePlugin(const QString
    #      &plugin)
    Rituals.call(
        'ritual_ZN10Qt3DRender20QRenderAspectPrivate15configurePluginERK7QS'
        'tring',
        plugin,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'Qt3DRender::QRenderAspectPrivate'

  #  A C++ Qt3DRender::QRenderAspectPrivate Python makes is of a C++ class of
  #  ours, in which Python can take functions over. This ritual hands one
  #  over; see 'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_Qt3DRender_QRenderAspectPrivate'

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(Qt3DRender.QRenderAspect.SubmissionType)
  def __init__(
      self,
      submissionType: Qt3DRender.QRenderAspect.SubmissionType,
  ) -> None:
    """
    Notes what was given, for Qt's
    'Qt3DRender::QRenderAspectPrivate::QRenderAspectPrivate(QRenderAspect::
    SubmissionType submissionType)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrenderaspectprivate.html

    Parameters
    ----------

    submissionType : Qt3DRender.QRenderAspect.SubmissionType
      Passed on as its number.
    """
    #  Qt3DRender::QRenderAspectPrivate::QRenderAspectPrivate(
    #      QRenderAspect::SubmissionType submissionType)
    self._noteCreation(QRenderAspectPrivate, lambda: Rituals.call(
        'ritual_ZN10Qt3DRender20QRenderAspectPrivateC1ENS_13QRenderAspect14'
        'SubmissionTypeE',
        submissionType.value,
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

  def q_func(self) -> Optional[Qt3DRender.QRenderAspect]:
    """
    Calls Qt's 'QRenderAspect *Qt3DRender::QRenderAspectPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrenderaspectprivate.html#q_func

    Returns
    -------

    Optional[Qt3DRender.QRenderAspect]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QRenderAspect *Qt3DRender::QRenderAspectPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender20QRenderAspectPrivate6q_funcEv',
    )
    return Qt3DRender.QRenderAspect._cuteAt(address)

  def jobsDone(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::QRenderAspectPrivate::jobsDone()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrenderaspectprivate.html#jobsDone
    """
    #  void Qt3DRender::QRenderAspectPrivate::jobsDone()
    ritual = 'ritual_ZN10Qt3DRender20QRenderAspectPrivate8jobsDoneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10Qt3DRender20QRenderAspectPrivate8jobsDoneEv'
    self.uglySide.call(ritual)

  def frameDone(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::QRenderAspectPrivate::frameDone()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrenderaspectprivate.html#frameDone
    """
    #  void Qt3DRender::QRenderAspectPrivate::frameDone()
    ritual = 'ritual_ZN10Qt3DRender20QRenderAspectPrivate9frameDoneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN10Qt3DRender20QRenderAspectPrivate9frameDoneEv'
    self.uglySide.call(ritual)

  def createNodeManagers(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::QRenderAspectPrivate::createNodeManagers()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrenderaspectprivate.html
    """
    #  void Qt3DRender::QRenderAspectPrivate::createNodeManagers()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender20QRenderAspectPrivate18createNodeManagersEv',
    )

  def onEngineStartup(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::QRenderAspectPrivate::onEngineStartup()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrenderaspectprivate.html
    """
    #  void Qt3DRender::QRenderAspectPrivate::onEngineStartup()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender20QRenderAspectPrivate15onEngineStartupEv',
    )

  def onEngineAboutToShutdown(self) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QRenderAspectPrivate::onEngineAboutToShutdown()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrenderaspectprivate.html
    """
    #  void Qt3DRender::QRenderAspectPrivate::onEngineAboutToShutdown()
    ritual = (
        'ritual_ZN10Qt3DRender20QRenderAspectPrivate23onEngineAboutToShutdo'
        'wnEv')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN10Qt3DRender20QRenderAspectPrivate23onEngineAboutTo'
          'ShutdownEv')
    self.uglySide.call(ritual)

  def registerBackendTypes(self) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QRenderAspectPrivate::registerBackendTypes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrenderaspectprivate.html
    """
    #  void Qt3DRender::QRenderAspectPrivate::registerBackendTypes()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender20QRenderAspectPrivate20registerBackendTypesE'
        'v',
    )

  def unregisterBackendTypes(self) -> None:
    """
    Calls Qt's 'void
    Qt3DRender::QRenderAspectPrivate::unregisterBackendTypes()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrenderaspectprivate.html
    """
    #  void Qt3DRender::QRenderAspectPrivate::unregisterBackendTypes()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender20QRenderAspectPrivate22unregisterBackendType'
        'sEv',
    )

  def loadSceneImporters(self) -> None:
    """
    Calls Qt's 'void Qt3DRender::QRenderAspectPrivate::loadSceneImporters()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrenderaspectprivate.html
    """
    #  void Qt3DRender::QRenderAspectPrivate::loadSceneImporters()
    self.uglySide.call(
        'ritual_ZN10Qt3DRender20QRenderAspectPrivate18loadSceneImportersEv',
    )

  @overload(str)
  def loadRenderPlugin(self, pluginName: str) -> None:
    """
    Calls Qt's 'void Qt3DRender::QRenderAspectPrivate::loadRenderPlugin(const
    QString &pluginName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrenderaspectprivate.html

    Parameters
    ----------

    pluginName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void Qt3DRender::QRenderAspectPrivate::loadRenderPlugin(const QString
    #      &pluginName)
    self.uglySide.call(
        'ritual_ZN10Qt3DRender20QRenderAspectPrivate16loadRenderPluginERK7Q'
        'String',
        pluginName,
    )

  def loadRendererPlugin(
      self,
  ) -> Optional[Qt3DRender.Render.AbstractRenderer]:
    """
    Calls Qt's 'Render::AbstractRenderer
    *Qt3DRender::QRenderAspectPrivate::loadRendererPlugin()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrenderaspectprivate.html

    Returns
    -------

    Optional[Qt3DRender.Render.AbstractRenderer]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  Render::AbstractRenderer
    #      *Qt3DRender::QRenderAspectPrivate::loadRendererPlugin()
    address = self.uglySide.call(
        'ritual_ZN10Qt3DRender20QRenderAspectPrivate18loadRendererPluginEv',
    )
    return Qt3DRender.Render.AbstractRenderer._cuteAt(address)

  @overload(QObject, QMouseEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QMouseEvent)
  @overload(NoneType, NoneType)
  def processMouseEvent(
      self,
      obj: Optional[QObject],
      event: Optional[QMouseEvent],
  ) -> bool:
    """
    Calls Qt's 'bool
    Qt3DRender::QRenderAspectPrivate::processMouseEvent(QObject *obj,
    QMouseEvent *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrenderaspectprivate.html

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QMouseEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool Qt3DRender::QRenderAspectPrivate::processMouseEvent(QObject *obj,
    #      QMouseEvent *event)
    return self.uglySide.call(
        'ritual_ZN10Qt3DRender20QRenderAspectPrivate17processMouseEventEP7Q'
        'ObjectP11QMouseEvent',
        self._addressOf(obj, 'QObject'), self._addressOf(event),
    )

  @overload(QObject, QKeyEvent)
  @overload(QObject, NoneType)
  @overload(NoneType, QKeyEvent)
  @overload(NoneType, NoneType)
  def processKeyEvent(
      self,
      obj: Optional[QObject],
      event: Optional[QKeyEvent],
  ) -> bool:
    """
    Calls Qt's 'bool
    Qt3DRender::QRenderAspectPrivate::processKeyEvent(QObject *obj, QKeyEvent
    *event)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qt3drender-qrenderaspectprivate.html

    Parameters
    ----------

    obj : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    event : Optional[QKeyEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool Qt3DRender::QRenderAspectPrivate::processKeyEvent(QObject *obj,
    #      QKeyEvent *event)
    return self.uglySide.call(
        'ritual_ZN10Qt3DRender20QRenderAspectPrivate15processKeyEventEP7QOb'
        'jectP9QKeyEvent',
        self._addressOf(obj, 'QObject'), self._addressOf(event),
    )

  @staticmethod
  def createGeometryRendererJobs(*__, **_) -> Never:
    """
    Qt's 'std::vector<Qt3DCore::QAspectJobPtr>
    Qt3DRender::QRenderAspectPrivate::createGeometryRendererJobs() const':
    gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.QRenderAspectPrivate.createGeometryRendererJobs' has "
        "no cute function yet. Qt's 'std::vector<Qt3DCore::QAspectJobPtr> "
        "Qt3DRender::QRenderAspectPrivate::createGeometryRendererJobs() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def createPreRendererJobs(*__, **_) -> Never:
    """
    Qt's 'std::vector<Qt3DCore::QAspectJobPtr>
    Qt3DRender::QRenderAspectPrivate::createPreRendererJobs() const': gives a
    type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.QRenderAspectPrivate.createPreRendererJobs' has no "
        "cute function yet. Qt's 'std::vector<Qt3DCore::QAspectJobPtr> "
        "Qt3DRender::QRenderAspectPrivate::createPreRendererJobs() const': "
        "gives a type Python has no way to take yet.")

  @staticmethod
  def createRenderBufferJobs(*__, **_) -> Never:
    """
    Qt's 'std::vector<Qt3DCore::QAspectJobPtr>
    Qt3DRender::QRenderAspectPrivate::createRenderBufferJobs() const': cannot
    be called and cannot be called through the meta-object and cannot be
    copied: no header file has its code, Qt's source does not mark it or its
    class for use from outside Qt or writes it 'inline' or nowhere, and it is
    no signal, slot or invokable function giving back nothing, of a class
    built on QObject, and Qt's source has no code for it that could be told
    from the rest.
    """
    raise NotImplementedError(
        "'Qt3DRender.QRenderAspectPrivate.createRenderBufferJobs' has no "
        "cute function yet. Qt's 'std::vector<Qt3DCore::QAspectJobPtr> "
        "Qt3DRender::QRenderAspectPrivate::createRenderBufferJobs() const': "
        "cannot be called and cannot be called through the meta-object and "
        "cannot be copied: no header file has its code, Qt's source does "
        "not mark it or its class for use from outside Qt or writes it "
        "'inline' or nowhere, and it is no signal, slot or invokable "
        "function giving back nothing, of a class built on QObject, and "
        "Qt's source has no code for it that could be told from the rest.")

  @staticmethod
  def registerBackendType(*__, **_) -> Never:
    """
    Qt's 'void Qt3DRender::QRenderAspectPrivate::registerBackendType(const
    QMetaObject &a0, const Qt3DCore::QBackendNodeMapperPtr &functor)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'Qt3DRender.QRenderAspectPrivate.registerBackendType' has no cute "
        "function yet. Qt's 'void "
        "Qt3DRender::QRenderAspectPrivate::registerBackendType(const "
        "QMetaObject &a0, const Qt3DCore::QBackendNodeMapperPtr &functor)': "
        "takes a type Python has no way to hand over yet.")
