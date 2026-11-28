"""
QQuick3DXrManager binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DXr/6.12.0/QtQuick3DXr/private/qquick3dxrmanager_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QQuick3DXrManager to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DXrManager(QObject):
  """
  The cute side of Qt's QQuick3DXrManager: a plain Python object standing in
  front of one C++ QQuick3DXrManager.

  It is built on the cute 'QObject', as Qt's QQuick3DXrManager is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuick3DXrManager that has a ritual and that Python
  can call so far, 12 names in all: 'metaObject',
  'isMultiViewRenderingSupported', 'isMultiviewRenderingDisabled', 'update',
  'initialized', 'sessionEnded', 'xrOriginChanged', 'frameReady',
  'referenceSpaceChanged', 'multiViewRenderingEnabledChanged', 'event',
  'preSetupQuickScene'. None can be made from Python: one comes out of a
  function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DXrManager::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QQuick3DXrManager::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DXrManagerPrivate *QQuick3DXrManager::d_func()': gives
    'QQuick3DXrManagerPrivate', which has no cute class yet.
  - Qt's 'const QQuick3DXrManagerPrivate *QQuick3DXrManager::d_func() const':
    gives 'QQuick3DXrManagerPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  28 of the 44 functions Qt declares: 24 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 2 not a gap;
  2 leans on 'QQuick3DXrManager.

  What to expect
  --------------

  - The C++ QQuick3DXrManager is created at the first use, not by
    'QQuick3DXrManager(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DXrManager.
  - Qt tells when it has removed the C++ QQuick3DXrManager. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DXrManager that has no cute function yet,
    '__init__', 'errorString', 'getDefaultClipDistances',
    'getFixedFoveationLevel', 'getInputManager', 'getReferenceSpace',
    'initialize', 'isDepthSubmissionEnabled', 'isMultiViewRenderingEnabled',
    'isPassthroughEnabled', 'isReady', 'isValid', 'renderFrame',
    'setDepthSubmissionEnabled', 'setFixedFoveationLevel',
    'setMultiViewRenderingEnabled', 'setPassthroughEnabled',
    'setReferenceSpace', 'setSamples', 'setXROrigin', 'setupGraphics',
    'setupQuickScene', 'supportsPassthrough', 'teardown', holds a function
    that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def isMultiviewRenderingDisabled() -> bool:
    """
    Calls Qt's 'bool QQuick3DXrManager::isMultiviewRenderingDisabled()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrmanager.html
    """
    #  bool QQuick3DXrManager::isMultiviewRenderingDisabled()
    return Rituals.call(
        'ritual_ZN17QQuick3DXrManager28isMultiviewRenderingDisabledEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DXrManager'

  #  A C++ QQuick3DXrManager Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DXrManager'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DXrManager::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxrmanager.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DXrManager::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QQuick3DXrManager10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def isMultiViewRenderingSupported(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DXrManager::isMultiViewRenderingSupported()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrmanager.html
    """
    #  bool QQuick3DXrManager::isMultiViewRenderingSupported() const
    return self.uglySide.call(
        'ritual_ZNK17QQuick3DXrManager29isMultiViewRenderingSupportedEv',
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
    Qt's 'QQuick3DXrManager::QQuick3DXrManager(QObject *parent)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: allocation of incomplete type
    'QQuick3DXrManagerPrivate'.
    """
    raise NotImplementedError(
        "'QQuick3DXrManager.__init__' has no cute function yet. Qt's "
        "'QQuick3DXrManager::QQuick3DXrManager(QObject *parent)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: allocation of incomplete type "
        "'QQuick3DXrManagerPrivate'.")

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

  def update(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrManager::update()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxrmanager.html#update
    """
    #  void QQuick3DXrManager::update()
    self.uglySide.call('ritual_ZN17QQuick3DXrManager6updateEv')

  def initialized(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrManager::initialized()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxrmanager.html#initialized
    """
    #  void QQuick3DXrManager::initialized()
    self.uglySide.call('ritual_ZN17QQuick3DXrManager11initializedEv')

  def sessionEnded(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrManager::sessionEnded()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrmanager.html#sessionEnded
    """
    #  void QQuick3DXrManager::sessionEnded()
    self.uglySide.call('ritual_ZN17QQuick3DXrManager12sessionEndedEv')

  def xrOriginChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrManager::xrOriginChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrmanager.html#xrOriginChanged
    """
    #  void QQuick3DXrManager::xrOriginChanged()
    self.uglySide.call('ritual_ZN17QQuick3DXrManager15xrOriginChangedEv')

  def frameReady(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrManager::frameReady()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxrmanager.html#frameReady
    """
    #  void QQuick3DXrManager::frameReady()
    self.uglySide.call('ritual_ZN17QQuick3DXrManager10frameReadyEv')

  def referenceSpaceChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrManager::referenceSpaceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrmanager.html#referenceSpaceChanged
    """
    #  void QQuick3DXrManager::referenceSpaceChanged()
    self.uglySide.call(
        'ritual_ZN17QQuick3DXrManager21referenceSpaceChangedEv',
    )

  def multiViewRenderingEnabledChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrManager::multiViewRenderingEnabledChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrmanager.html
    """
    #  void QQuick3DXrManager::multiViewRenderingEnabledChanged()
    self.uglySide.call(
        'ritual_ZN17QQuick3DXrManager32multiViewRenderingEnabledChangedEv',
    )

  @overload(QEvent)
  @overload(NoneType)
  def event(self, e: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QQuick3DXrManager::event(QEvent *e)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dxrmanager.html#event

    Parameters
    ----------

    e : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QQuick3DXrManager::event(QEvent *e)
    return self.uglySide.call(
        'ritual_ZN17QQuick3DXrManager5eventEP6QEvent', self._addressOf(e),
    )

  def preSetupQuickScene(self) -> None:
    """
    Calls Qt's 'void QQuick3DXrManager::preSetupQuickScene()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dxrmanager.html#preSetupQuickScene
    """
    #  void QQuick3DXrManager::preSetupQuickScene()
    self.uglySide.call('ritual_ZN17QQuick3DXrManager18preSetupQuickSceneEv')

  @staticmethod
  def errorString(*__, **_) -> Never:
    """
    Qt's 'QString QQuick3DXrManager::errorString() const': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: member access into incomplete type 'const
    QQuick3DXrManagerPrivate'.
    """
    raise NotImplementedError(
        "'QQuick3DXrManager.errorString' has no cute function yet. Qt's "
        "'QString QQuick3DXrManager::errorString() const': Qt's library has "
        "no name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type 'const "
        "QQuick3DXrManagerPrivate'.")

  @staticmethod
  def getDefaultClipDistances(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrManager::getDefaultClipDistances(float &nearClip,
    float &farClip) const': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: member access into
    incomplete type 'const QQuick3DXrManagerPrivate'.
    """
    raise NotImplementedError(
        "'QQuick3DXrManager.getDefaultClipDistances' has no cute function "
        "yet. Qt's 'void QQuick3DXrManager::getDefaultClipDistances(float "
        "&nearClip, float &farClip) const': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: member access into incomplete type 'const "
        "QQuick3DXrManagerPrivate'.")

  @staticmethod
  def getFixedFoveationLevel(*__, **_) -> Never:
    """
    Qt's 'QtQuick3DXr::FoveationLevel
    QQuick3DXrManager::getFixedFoveationLevel() const': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: member access into incomplete type 'const
    QQuick3DXrManagerPrivate'.
    """
    raise NotImplementedError(
        "'QQuick3DXrManager.getFixedFoveationLevel' has no cute function "
        "yet. Qt's 'QtQuick3DXr::FoveationLevel "
        "QQuick3DXrManager::getFixedFoveationLevel() const': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: member access into incomplete type 'const "
        "QQuick3DXrManagerPrivate'.")

  @staticmethod
  def getInputManager(*__, **_) -> Never:
    """
    Qt's 'QQuick3DXrInputManager *QQuick3DXrManager::getInputManager()
    const': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: member access into incomplete type
    'const QQuick3DXrManagerPrivate'.
    """
    raise NotImplementedError(
        "'QQuick3DXrManager.getInputManager' has no cute function yet. Qt's "
        "'QQuick3DXrInputManager *QQuick3DXrManager::getInputManager() "
        "const': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: member access into "
        "incomplete type 'const QQuick3DXrManagerPrivate'.")

  @staticmethod
  def getReferenceSpace(*__, **_) -> Never:
    """
    Qt's 'QtQuick3DXr::ReferenceSpace QQuick3DXrManager::getReferenceSpace()
    const': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: member access into incomplete type
    'const QQuick3DXrManagerPrivate'.
    """
    raise NotImplementedError(
        "'QQuick3DXrManager.getReferenceSpace' has no cute function yet. "
        "Qt's 'QtQuick3DXr::ReferenceSpace "
        "QQuick3DXrManager::getReferenceSpace() const': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type 'const "
        "QQuick3DXrManagerPrivate'.")

  @staticmethod
  def initialize(*__, **_) -> Never:
    """
    Qt's 'bool QQuick3DXrManager::initialize()': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file:
    member access into incomplete type 'QQuick3DXrManagerPrivate'.
    """
    raise NotImplementedError(
        "'QQuick3DXrManager.initialize' has no cute function yet. Qt's "
        "'bool QQuick3DXrManager::initialize()': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: member access into incomplete type "
        "'QQuick3DXrManagerPrivate'.")

  @staticmethod
  def isDepthSubmissionEnabled(*__, **_) -> Never:
    """
    Qt's 'bool QQuick3DXrManager::isDepthSubmissionEnabled() const': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type 'const
    QQuick3DXrManagerPrivate'.
    """
    raise NotImplementedError(
        "'QQuick3DXrManager.isDepthSubmissionEnabled' has no cute function "
        "yet. Qt's 'bool QQuick3DXrManager::isDepthSubmissionEnabled() "
        "const': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: member access into "
        "incomplete type 'const QQuick3DXrManagerPrivate'.")

  @staticmethod
  def isMultiViewRenderingEnabled(*__, **_) -> Never:
    """
    Qt's 'bool QQuick3DXrManager::isMultiViewRenderingEnabled() const': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type 'const
    QQuick3DXrManagerPrivate'.
    """
    raise NotImplementedError(
        "'QQuick3DXrManager.isMultiViewRenderingEnabled' has no cute "
        "function yet. Qt's 'bool "
        "QQuick3DXrManager::isMultiViewRenderingEnabled() const': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'const QQuick3DXrManagerPrivate'.")

  @staticmethod
  def isPassthroughEnabled(*__, **_) -> Never:
    """
    Qt's 'bool QQuick3DXrManager::isPassthroughEnabled() const': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: member access into incomplete type 'const
    QQuick3DXrManagerPrivate'.
    """
    raise NotImplementedError(
        "'QQuick3DXrManager.isPassthroughEnabled' has no cute function yet. "
        "Qt's 'bool QQuick3DXrManager::isPassthroughEnabled() const': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'const QQuick3DXrManagerPrivate'.")

  @staticmethod
  def isReady(*__, **_) -> Never:
    """
    Qt's 'bool QQuick3DXrManager::isReady() const': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    member access into incomplete type 'const QQuick3DXrManagerPrivate'.
    """
    raise NotImplementedError(
        "'QQuick3DXrManager.isReady' has no cute function yet. Qt's 'bool "
        "QQuick3DXrManager::isReady() const': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: member access into incomplete type 'const "
        "QQuick3DXrManagerPrivate'.")

  @staticmethod
  def isValid(*__, **_) -> Never:
    """
    Qt's 'bool QQuick3DXrManager::isValid() const': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    member access into incomplete type 'const QQuick3DXrManagerPrivate'.
    """
    raise NotImplementedError(
        "'QQuick3DXrManager.isValid' has no cute function yet. Qt's 'bool "
        "QQuick3DXrManager::isValid() const': Qt's library has no name for "
        "it, and its code in Qt's source does not compile apart from its "
        "file: member access into incomplete type 'const "
        "QQuick3DXrManagerPrivate'.")

  @staticmethod
  def renderFrame(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrManager::renderFrame()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    member access into incomplete type 'QQuick3DXrManagerPrivate'.
    """
    raise NotImplementedError(
        "'QQuick3DXrManager.renderFrame' has no cute function yet. Qt's "
        "'void QQuick3DXrManager::renderFrame()': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: member access into incomplete type "
        "'QQuick3DXrManagerPrivate'.")

  @staticmethod
  def setDepthSubmissionEnabled(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrManager::setDepthSubmissionEnabled(bool enable)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: member access into incomplete type
    'QQuick3DXrManagerPrivate'.
    """
    raise NotImplementedError(
        "'QQuick3DXrManager.setDepthSubmissionEnabled' has no cute function "
        "yet. Qt's 'void QQuick3DXrManager::setDepthSubmissionEnabled(bool "
        "enable)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: member access into "
        "incomplete type 'QQuick3DXrManagerPrivate'.")

  @staticmethod
  def setFixedFoveationLevel(*__, **_) -> Never:
    """
    Qt's 'void
    QQuick3DXrManager::setFixedFoveationLevel(QtQuick3DXr::FoveationLevel
    level)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: unknown type name
    'XrFoveationLevelFB'; did you mean 'QtQuick3DXr::FoveationLevel'?.
    """
    raise NotImplementedError(
        "'QQuick3DXrManager.setFixedFoveationLevel' has no cute function "
        "yet. Qt's 'void "
        "QQuick3DXrManager::setFixedFoveationLevel(QtQuick3DXr::FoveationLev"
        "el level)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: unknown type name "
        "'XrFoveationLevelFB'; did you mean 'QtQuick3DXr::FoveationLevel'?.")

  @staticmethod
  def setMultiViewRenderingEnabled(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrManager::setMultiViewRenderingEnabled(bool enable)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: member access into incomplete type
    'QQuick3DXrManagerPrivate'.
    """
    raise NotImplementedError(
        "'QQuick3DXrManager.setMultiViewRenderingEnabled' has no cute "
        "function yet. Qt's 'void "
        "QQuick3DXrManager::setMultiViewRenderingEnabled(bool enable)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: member access into incomplete "
        "type 'QQuick3DXrManagerPrivate'.")

  @staticmethod
  def setPassthroughEnabled(*__, **_) -> Never:
    """
    Qt's 'bool QQuick3DXrManager::setPassthroughEnabled(bool enabled)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: member access into incomplete type
    'QQuick3DXrManagerPrivate'.
    """
    raise NotImplementedError(
        "'QQuick3DXrManager.setPassthroughEnabled' has no cute function "
        "yet. Qt's 'bool QQuick3DXrManager::setPassthroughEnabled(bool "
        "enabled)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: member access into "
        "incomplete type 'QQuick3DXrManagerPrivate'.")

  @staticmethod
  def setReferenceSpace(*__, **_) -> Never:
    """
    Qt's 'void
    QQuick3DXrManager::setReferenceSpace(QtQuick3DXr::ReferenceSpace
    newReferenceSpace)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: member access into
    incomplete type 'QQuick3DXrManagerPrivate'.
    """
    raise NotImplementedError(
        "'QQuick3DXrManager.setReferenceSpace' has no cute function yet. "
        "Qt's 'void "
        "QQuick3DXrManager::setReferenceSpace(QtQuick3DXr::ReferenceSpace "
        "newReferenceSpace)': Qt's library has no name for it, and its code "
        "in Qt's source does not compile apart from its file: member access "
        "into incomplete type 'QQuick3DXrManagerPrivate'.")

  @staticmethod
  def setSamples(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrManager::setSamples(int samples)': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: member access into incomplete type 'QQuick3DXrManagerPrivate'.
    """
    raise NotImplementedError(
        "'QQuick3DXrManager.setSamples' has no cute function yet. Qt's "
        "'void QQuick3DXrManager::setSamples(int samples)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: member access into incomplete type "
        "'QQuick3DXrManagerPrivate'.")

  @staticmethod
  def setXROrigin(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrManager::setXROrigin(QQuick3DXrOrigin *origin)':
    leans on 'QQuick3DXrManager::update()', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DXrManager.setXROrigin' has no cute function yet. Qt's "
        "'void QQuick3DXrManager::setXROrigin(QQuick3DXrOrigin *origin)': "
        "leans on 'QQuick3DXrManager::update()', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def setupGraphics(*__, **_) -> Never:
    """
    Qt's 'bool QQuick3DXrManager::setupGraphics()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    member access into incomplete type 'QQuick3DXrManagerPrivate'.
    """
    raise NotImplementedError(
        "'QQuick3DXrManager.setupGraphics' has no cute function yet. Qt's "
        "'bool QQuick3DXrManager::setupGraphics()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type "
        "'QQuick3DXrManagerPrivate'.")

  @staticmethod
  def setupQuickScene(*__, **_) -> Never:
    """
    Qt's 'bool QQuick3DXrManager::setupQuickScene()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: member access into incomplete type 'QQuick3DXrManagerPrivate'.
    """
    raise NotImplementedError(
        "'QQuick3DXrManager.setupQuickScene' has no cute function yet. Qt's "
        "'bool QQuick3DXrManager::setupQuickScene()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: member access into incomplete type "
        "'QQuick3DXrManagerPrivate'.")

  @staticmethod
  def supportsPassthrough(*__, **_) -> Never:
    """
    Qt's 'bool QQuick3DXrManager::supportsPassthrough() const': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: member access into incomplete type 'const
    QQuick3DXrManagerPrivate'.
    """
    raise NotImplementedError(
        "'QQuick3DXrManager.supportsPassthrough' has no cute function yet. "
        "Qt's 'bool QQuick3DXrManager::supportsPassthrough() const': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: member access into incomplete type "
        "'const QQuick3DXrManagerPrivate'.")

  @staticmethod
  def teardown(*__, **_) -> Never:
    """
    Qt's 'void QQuick3DXrManager::teardown()': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file:
    member access into incomplete type 'QQuick3DXrManagerPrivate'.
    """
    raise NotImplementedError(
        "'QQuick3DXrManager.teardown' has no cute function yet. Qt's 'void "
        "QQuick3DXrManager::teardown()': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "member access into incomplete type 'QQuick3DXrManagerPrivate'.")
