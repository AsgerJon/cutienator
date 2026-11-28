"""
QQuickProfiler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick/6.12.0/QtQuick/private/qquickprofiler_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQuickProfiler to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from ..QtQml import QQmlProfilerDefinitions

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QElapsedTimer, QMetaObject, QSize, QUrl
  from . import QQuickProfilerData
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QElapsedTimer = WAIT['QElapsedTimer']
  QQuickProfilerData = WAIT['QQuickProfilerData']
  QSize = WAIT['QSize']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuickProfiler(QObject, QQmlProfilerDefinitions):
  """
  The cute side of Qt's QQuickProfiler: a plain Python object standing in
  front of one C++ QQuickProfiler.

  It is built on the cute 'QObject', as Qt's QQuickProfiler is built on Qt's
  QObject, and has everything that class has. It is built on the cute
  'QQmlProfilerDefinitions' as well, as Qt's QQuickProfiler is built on Qt's
  QQmlProfilerDefinitions too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQuickProfiler that has a ritual and that Python can
  call so far, 13 names in all: 'metaObject', 'tr', 'animationFrame',
  'pixmapLoadingFinished', 'registerAnimationCallback', 'timestamp',
  'initialize', 'dataReady', 'processMessage', 'startProfilingImpl',
  'stopProfilingImpl', 'reportDataImpl', 'setTimer'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuickProfiler::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQuickProfiler::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QQuickProfiler::~QQuickProfiler()': the destructor: Python never
    removes a C++ QQuickProfiler.

  What has no ritual
  ------------------

  11 of the 28 functions Qt declares: 9 a template; 2 not a gap.

  What to expect
  --------------

  - The C++ QQuickProfiler is created at the first use, not by
    'QQuickProfiler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuickProfiler.
  - Qt tells when it has removed the C++ QQuickProfiler. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuickProfiler that has no cute function yet,
    'inputEvent', 'pixmapCountChanged', 'pixmapStateChanged',
    'recordSceneGraphTimestamp', 'reportSceneGraphFrame',
    'skipSceneGraphTimestamps', 'startSceneGraphFrame', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQuickProfiler, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class AnimationThread(CuteNum):
    """
    The enum 'QQuickProfiler::AnimationThread' of Qt, with the 2 names Qt
    gives in it.
    """

    GuiThread = Kee[int](0)
    RenderThread = Kee[int](1)

  class SceneGraphAdaptationLayerStage(CuteNum):
    """
    The enum 'QQuickProfiler::SceneGraphAdaptationLayerStage' of Qt, with the
    3 names Qt gives in it.
    """

    SceneGraphAdaptationLayerStart = Kee[int](0)
    SceneGraphAdaptationLayerGlyphRender = Kee[int](1)
    SceneGraphAdaptationLayerGlyphStore = Kee[int](2)

  class SceneGraphContextStage(CuteNum):
    """
    The enum 'QQuickProfiler::SceneGraphContextStage' of Qt, with the 2 names
    Qt gives in it.
    """

    SceneGraphContextStart = Kee[int](0)
    SceneGraphContextMaterialCompile = Kee[int](1)

  class SceneGraphPolishAndSyncStage(CuteNum):
    """
    The enum 'QQuickProfiler::SceneGraphPolishAndSyncStage' of Qt, with the 5
    names Qt gives in it.
    """

    SceneGraphPolishAndSyncStart = Kee[int](0)
    SceneGraphPolishAndSyncPolish = Kee[int](1)
    SceneGraphPolishAndSyncWait = Kee[int](2)
    SceneGraphPolishAndSyncSync = Kee[int](3)
    SceneGraphPolishAndSyncAnimations = Kee[int](4)

  class SceneGraphPolishStage(CuteNum):
    """
    The enum 'QQuickProfiler::SceneGraphPolishStage' of Qt, with the 2 names
    Qt gives in it.
    """

    SceneGraphPolishStart = Kee[int](0)
    SceneGraphPolishPolish = Kee[int](1)

  class SceneGraphRenderLoopStage(CuteNum):
    """
    The enum 'QQuickProfiler::SceneGraphRenderLoopStage' of Qt, with the 4
    names Qt gives in it.
    """

    SceneGraphRenderLoopStart = Kee[int](0)
    SceneGraphRenderLoopSync = Kee[int](1)
    SceneGraphRenderLoopRender = Kee[int](2)
    SceneGraphRenderLoopSwap = Kee[int](3)

  class SceneGraphRendererStage(CuteNum):
    """
    The enum 'QQuickProfiler::SceneGraphRendererStage' of Qt, with the 5
    names Qt gives in it.
    """

    SceneGraphRendererStart = Kee[int](0)
    SceneGraphRendererPreprocess = Kee[int](1)
    SceneGraphRendererUpdate = Kee[int](2)
    SceneGraphRendererBinding = Kee[int](3)
    SceneGraphRendererRender = Kee[int](4)

  class SceneGraphTextureDeletionStage(CuteNum):
    """
    The enum 'QQuickProfiler::SceneGraphTextureDeletionStage' of Qt, with the
    2 names Qt gives in it.
    """

    SceneGraphTextureDeletionStart = Kee[int](0)
    SceneGraphTextureDeletionDelete = Kee[int](1)

  class SceneGraphTexturePrepareStage(CuteNum):
    """
    The enum 'QQuickProfiler::SceneGraphTexturePrepareStage' of Qt, with the
    6 names Qt gives in it.
    """

    SceneGraphTexturePrepareStart = Kee[int](0)
    SceneGraphTexturePrepareBind = Kee[int](1)
    SceneGraphTexturePrepareConvert = Kee[int](2)
    SceneGraphTexturePrepareSwizzle = Kee[int](3)
    SceneGraphTexturePrepareUpload = Kee[int](4)
    SceneGraphTexturePrepareMipmap = Kee[int](5)

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
    Calls Qt's 'QString QQuickProfiler::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickprofiler.html#tr

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
    #  QString QQuickProfiler::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN14QQuickProfiler2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(int, AnimationThread)
  def animationFrame(delta: int, threadId: AnimationThread) -> None:
    """
    Calls Qt's 'void QQuickProfiler::animationFrame(qint64 delta,
    AnimationThread threadId)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickprofiler.html#animationFrame

    Parameters
    ----------

    delta : int
      Passed on as it is.

    threadId : AnimationThread
      Passed on as its number.
    """
    #  void QQuickProfiler::animationFrame(qint64 delta, AnimationThread
    #      threadId)
    Rituals.call(
        'ritual_ZN14QQuickProfiler14animationFrameExNS_15AnimationThreadE',
        delta, threadId.value,
    )

  @staticmethod
  @overload(QUrl, QSize)
  def pixmapLoadingFinished(url: QUrl, size: QSize) -> None:
    """
    Calls Qt's 'void QQuickProfiler::pixmapLoadingFinished(const QUrl &url,
    const QSize &size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickprofiler.html#pixmapLoadingFinished

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    size : QSize
      Passed on as a value: Qt reads the C++ QSize, which stays Python's own.
    """
    #  void QQuickProfiler::pixmapLoadingFinished(const QUrl &url, const
    #      QSize &size)
    Rituals.call(
        'ritual_ZN14QQuickProfiler21pixmapLoadingFinishedERK4QUrlRK5QSize',
        CuteMixin._valueOf(url), CuteMixin._valueOf(size),
    )

  @staticmethod
  def registerAnimationCallback() -> None:
    """
    Calls Qt's 'void QQuickProfiler::registerAnimationCallback()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickprofiler.html#registerAnimationCallback
    """
    #  void QQuickProfiler::registerAnimationCallback()
    Rituals.call('ritual_ZN14QQuickProfiler25registerAnimationCallbackEv')

  @staticmethod
  @overload(QObject)
  @overload(NoneType)
  def initialize(parent: Optional[QObject]) -> None:
    """
    Calls Qt's 'void QQuickProfiler::initialize(QObject *parent)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickprofiler.html#initialize

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQuickProfiler::initialize(QObject *parent)
    Rituals.call(
        'ritual_ZN14QQuickProfiler10initializeEP7QObject',
        CuteMixin._addressOf(parent, 'QObject'),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuickProfiler'

  #  Qt's QQuickProfiler is built on more than one class. The part of a C++
  #  QQuickProfiler that belongs to a class after the first begins somewhere
  #  inside the object, and the ritual named for that class gives where; see
  #  'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlProfilerDefinitions':
          'ritual_cast_QQuickProfiler_QQmlProfilerDefinitions',
  }

  #  A C++ QQuickProfiler Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuickProfiler'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuickProfiler::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquickprofiler.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuickProfiler::metaObject() const
    address = self.uglySide.call('ritual_ZNK14QQuickProfiler10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QElapsedTimer)
  def setTimer(self, t: QElapsedTimer) -> None:
    """
    Calls Qt's 'void QQuickProfiler::setTimer(const QElapsedTimer &t)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickprofiler.html#setTimer

    Parameters
    ----------

    t : QElapsedTimer
      Passed on as a value: Qt reads the C++ QElapsedTimer, which stays
      Python's own.
    """
    #  void QQuickProfiler::setTimer(const QElapsedTimer &t)
    self.uglySide.call(
        'ritual_ZN14QQuickProfiler8setTimerERK13QElapsedTimer',
        self._valueOf(t),
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

  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject]) -> None:
    """
    Notes what was given, for Qt's 'QQuickProfiler::QQuickProfiler(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qquickprofiler.html#QQuickProfiler

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQuickProfiler::QQuickProfiler(QObject *parent)
    self._noteCreation(QQuickProfiler, lambda: Rituals.call(
        'ritual_ZN14QQuickProfilerC1EP7QObject',
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

  def timestamp(self) -> int:
    """
    Calls Qt's 'qint64 QQuickProfiler::timestamp()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickprofiler.html#timestamp
    """
    #  qint64 QQuickProfiler::timestamp()
    return self.uglySide.call('ritual_ZN14QQuickProfiler9timestampEv')

  @overload(QList[QQuickProfilerData])
  def dataReady(self, data: QList[QQuickProfilerData]) -> None:
    """
    Calls Qt's 'void QQuickProfiler::dataReady(const
    QList<QQuickProfilerData> &data)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickprofiler.html#dataReady

    Parameters
    ----------

    data : QList[QQuickProfilerData]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQuickProfiler::dataReady(const QList<QQuickProfilerData> &data)
    self.uglySide.call(
        'ritual_ZN14QQuickProfiler9dataReadyERK5QListI18QQuickProfilerDataE',
        self._valueOf(data),
    )

  @overload(QQuickProfilerData)
  def processMessage(self, message: QQuickProfilerData) -> None:
    """
    Calls Qt's 'void QQuickProfiler::processMessage(const QQuickProfilerData
    &message)'.

    Qt's own words: https://doc.qt.io/qt-6/qquickprofiler.html#processMessage

    Parameters
    ----------

    message : QQuickProfilerData
      Passed on as a value: Qt reads the C++ QQuickProfilerData, which stays
      Python's own.
    """
    #  void QQuickProfiler::processMessage(const QQuickProfilerData &message)
    self.uglySide.call(
        'ritual_ZN14QQuickProfiler14processMessageERK18QQuickProfilerData',
        self._valueOf(message),
    )

  @overload(int)
  def startProfilingImpl(self, features: int) -> None:
    """
    Calls Qt's 'void QQuickProfiler::startProfilingImpl(quint64 features)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickprofiler.html#startProfilingImpl

    Parameters
    ----------

    features : int
      Passed on as it is.
    """
    #  void QQuickProfiler::startProfilingImpl(quint64 features)
    self.uglySide.call(
        'ritual_ZN14QQuickProfiler18startProfilingImplEy', features,
    )

  def stopProfilingImpl(self) -> None:
    """
    Calls Qt's 'void QQuickProfiler::stopProfilingImpl()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquickprofiler.html#stopProfilingImpl
    """
    #  void QQuickProfiler::stopProfilingImpl()
    self.uglySide.call('ritual_ZN14QQuickProfiler17stopProfilingImplEv')

  def reportDataImpl(self) -> None:
    """
    Calls Qt's 'void QQuickProfiler::reportDataImpl()'.

    Qt's own words: https://doc.qt.io/qt-6/qquickprofiler.html#reportDataImpl
    """
    #  void QQuickProfiler::reportDataImpl()
    self.uglySide.call('ritual_ZN14QQuickProfiler14reportDataImplEv')

  @staticmethod
  def inputEvent(*__, **_) -> Never:
    """
    Qt's 'QQuickProfiler::inputEvent': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QQuickProfiler.inputEvent' has no cute function yet. Qt's "
        "'QQuickProfiler::inputEvent': a template: a pattern and no single "
        "function.")

  @staticmethod
  def pixmapCountChanged(*__, **_) -> Never:
    """
    Qt's 'QQuickProfiler::pixmapCountChanged': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QQuickProfiler.pixmapCountChanged' has no cute function yet. Qt's "
        "'QQuickProfiler::pixmapCountChanged': a template: a pattern and no "
        "single function.")

  @staticmethod
  def pixmapStateChanged(*__, **_) -> Never:
    """
    Qt's 'QQuickProfiler::pixmapStateChanged': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QQuickProfiler.pixmapStateChanged' has no cute function yet. Qt's "
        "'QQuickProfiler::pixmapStateChanged': a template: a pattern and no "
        "single function.")

  @staticmethod
  def recordSceneGraphTimestamp(*__, **_) -> Never:
    """
    Qt's 'QQuickProfiler::recordSceneGraphTimestamp': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'QQuickProfiler.recordSceneGraphTimestamp' has no cute function "
        "yet. Qt's 'QQuickProfiler::recordSceneGraphTimestamp': a template: "
        "a pattern and no single function.")

  @staticmethod
  def reportSceneGraphFrame(*__, **_) -> Never:
    """
    Qt's 'QQuickProfiler::reportSceneGraphFrame': a template: a pattern and
    no single function.
    """
    raise NotImplementedError(
        "'QQuickProfiler.reportSceneGraphFrame' has no cute function yet. "
        "Qt's 'QQuickProfiler::reportSceneGraphFrame': a template: a "
        "pattern and no single function.")

  @staticmethod
  def skipSceneGraphTimestamps(*__, **_) -> Never:
    """
    Qt's 'QQuickProfiler::skipSceneGraphTimestamps': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'QQuickProfiler.skipSceneGraphTimestamps' has no cute function "
        "yet. Qt's 'QQuickProfiler::skipSceneGraphTimestamps': a template: "
        "a pattern and no single function.")

  @staticmethod
  def startSceneGraphFrame(*__, **_) -> Never:
    """
    Qt's 'QQuickProfiler::startSceneGraphFrame': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QQuickProfiler.startSceneGraphFrame' has no cute function yet. "
        "Qt's 'QQuickProfiler::startSceneGraphFrame': a template: a pattern "
        "and no single function.")
