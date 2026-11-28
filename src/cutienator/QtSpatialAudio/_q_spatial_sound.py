"""
QSpatialSound binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSpatialAudio/qspatialsound.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject, QUrl
  from ..QtGui import QQuaternion, QVector3D
  from . import QAudioEngine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAudioEngine = WAIT['QAudioEngine']
  QQuaternion = WAIT['QQuaternion']
  QUrl = WAIT['QUrl']
  QVector3D = WAIT['QVector3D']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSpatialSound(QObject):
  """
  The cute side of Qt's QSpatialSound: a plain Python object standing in
  front of one C++ QSpatialSound.

  It is built on the cute 'QObject', as Qt's QSpatialSound is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QSpatialSound that has a ritual and that Python can
  call so far, 48 names in all: 'metaObject', 'tr', 'setSource', 'source',
  'loops', 'setLoops', 'autoPlay', 'setAutoPlay', 'setPosition', 'position',
  'setRotation', 'rotation', 'setVolume', 'volume', 'setDistanceModel',
  'distanceModel', 'setSize', 'size', 'setDistanceCutoff', 'distanceCutoff',
  'setManualAttenuation', 'manualAttenuation', 'setOcclusionIntensity',
  'occlusionIntensity', 'setDirectivity', 'directivity',
  'setDirectivityOrder', 'directivityOrder', 'setNearFieldGain',
  'nearFieldGain', 'engine', 'sourceChanged', 'loopsChanged',
  'autoPlayChanged', 'positionChanged', 'rotationChanged', 'volumeChanged',
  'distanceModelChanged', 'sizeChanged', 'distanceCutoffChanged',
  'manualAttenuationChanged', 'occlusionIntensityChanged',
  'directivityChanged', 'directivityOrderChanged', 'nearFieldGainChanged',
  'play', 'pause', 'stop'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QSpatialSound::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QSpatialSound::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QSpatialSound::~QSpatialSound()': the destructor: Python never
    removes a C++ QSpatialSound.
  - Qt's 'QSpatialSoundPrivate *QSpatialSound::d_func()': gives
    'QSpatialSoundPrivate', which has no cute class yet.
  - Qt's 'const QSpatialSoundPrivate *QSpatialSound::d_func() const': gives
    'QSpatialSoundPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  2 of the 56 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QSpatialSound is created at the first use, not by
    'QSpatialSound(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QSpatialSound.
  - Qt tells when it has removed the C++ QSpatialSound. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QSpatialSound, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class DistanceModel(CuteNum, scoped=True):
    """
    The enum 'QSpatialSound::DistanceModel' of Qt, with the 3 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Logarithmic = Kee[int](0)
    Linear = Kee[int](1)
    ManualAttenuation = Kee[int](2)

  class Loops(CuteNum):
    """
    The enum 'QSpatialSound::Loops' of Qt, with the 2 names Qt gives in it.
    """

    Infinite = Kee[int](-1)
    Once = Kee[int](1)

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
    Calls Qt's 'QString QSpatialSound::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qspatialsound.html#tr

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
    #  QString QSpatialSound::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QSpatialSound2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSpatialSound'

  #  A C++ QSpatialSound Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QSpatialSound'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QSpatialSound::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qspatialsound.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QSpatialSound::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QSpatialSound10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def source(self) -> QUrl:
    """
    Calls Qt's 'QUrl QSpatialSound::source() const'.

    Qt's own words: https://doc.qt.io/qt-6/qspatialsound.html#source

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QSpatialSound::source() const
    address = self.uglySide.call('ritual_ZNK13QSpatialSound6sourceEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def loops(self) -> int:
    """
    Calls Qt's 'int QSpatialSound::loops() const'.

    Qt's own words: https://doc.qt.io/qt-6/qspatialsound.html#loops
    """
    #  int QSpatialSound::loops() const
    return self.uglySide.call('ritual_ZNK13QSpatialSound5loopsEv')

  def autoPlay(self) -> bool:
    """
    Calls Qt's 'bool QSpatialSound::autoPlay() const'.

    Qt's own words: https://doc.qt.io/qt-6/qspatialsound.html#autoPlay
    """
    #  bool QSpatialSound::autoPlay() const
    return self.uglySide.call('ritual_ZNK13QSpatialSound8autoPlayEv')

  def position(self) -> QVector3D:
    """
    Calls Qt's 'QVector3D QSpatialSound::position() const'.

    Qt's own words: https://doc.qt.io/qt-6/qspatialsound.html#position

    Returns
    -------

    QVector3D
      A new cute QVector3D around the copy Qt gave back. Python owns it.
    """
    #  QVector3D QSpatialSound::position() const
    address = self.uglySide.call('ritual_ZNK13QSpatialSound8positionEv')
    from ..QtGui import QVector3D
    return QVector3D._cuteOwning(address)

  def rotation(self) -> QQuaternion:
    """
    Calls Qt's 'QQuaternion QSpatialSound::rotation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qspatialsound.html#rotation

    Returns
    -------

    QQuaternion
      A new cute QQuaternion around the copy Qt gave back. Python owns it.
    """
    #  QQuaternion QSpatialSound::rotation() const
    address = self.uglySide.call('ritual_ZNK13QSpatialSound8rotationEv')
    from ..QtGui import QQuaternion
    return QQuaternion._cuteOwning(address)

  def volume(self) -> float:
    """
    Calls Qt's 'float QSpatialSound::volume() const'.

    Qt's own words: https://doc.qt.io/qt-6/qspatialsound.html#volume
    """
    #  float QSpatialSound::volume() const
    return self.uglySide.call('ritual_ZNK13QSpatialSound6volumeEv')

  def distanceModel(self) -> DistanceModel:
    """
    Calls Qt's 'DistanceModel QSpatialSound::distanceModel() const'.

    Qt's own words: https://doc.qt.io/qt-6/qspatialsound.html#distanceModel

    Returns
    -------

    DistanceModel
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'DistanceModel(number)'
      gives.
    """
    #  DistanceModel QSpatialSound::distanceModel() const
    return QSpatialSound.DistanceModel(self.uglySide.call(
        'ritual_ZNK13QSpatialSound13distanceModelEv',
    ))

  def size(self) -> float:
    """
    Calls Qt's 'float QSpatialSound::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qspatialsound.html#size
    """
    #  float QSpatialSound::size() const
    return self.uglySide.call('ritual_ZNK13QSpatialSound4sizeEv')

  def distanceCutoff(self) -> float:
    """
    Calls Qt's 'float QSpatialSound::distanceCutoff() const'.

    Qt's own words: https://doc.qt.io/qt-6/qspatialsound.html#distanceCutoff
    """
    #  float QSpatialSound::distanceCutoff() const
    return self.uglySide.call('ritual_ZNK13QSpatialSound14distanceCutoffEv')

  def manualAttenuation(self) -> float:
    """
    Calls Qt's 'float QSpatialSound::manualAttenuation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspatialsound.html#manualAttenuation
    """
    #  float QSpatialSound::manualAttenuation() const
    return self.uglySide.call(
        'ritual_ZNK13QSpatialSound17manualAttenuationEv',
    )

  def occlusionIntensity(self) -> float:
    """
    Calls Qt's 'float QSpatialSound::occlusionIntensity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspatialsound.html#occlusionIntensity
    """
    #  float QSpatialSound::occlusionIntensity() const
    return self.uglySide.call(
        'ritual_ZNK13QSpatialSound18occlusionIntensityEv',
    )

  def directivity(self) -> float:
    """
    Calls Qt's 'float QSpatialSound::directivity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qspatialsound.html#directivity
    """
    #  float QSpatialSound::directivity() const
    return self.uglySide.call('ritual_ZNK13QSpatialSound11directivityEv')

  def directivityOrder(self) -> float:
    """
    Calls Qt's 'float QSpatialSound::directivityOrder() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspatialsound.html#directivityOrder
    """
    #  float QSpatialSound::directivityOrder() const
    return self.uglySide.call(
        'ritual_ZNK13QSpatialSound16directivityOrderEv',
    )

  def nearFieldGain(self) -> float:
    """
    Calls Qt's 'float QSpatialSound::nearFieldGain() const'.

    Qt's own words: https://doc.qt.io/qt-6/qspatialsound.html#nearFieldGain
    """
    #  float QSpatialSound::nearFieldGain() const
    return self.uglySide.call('ritual_ZNK13QSpatialSound13nearFieldGainEv')

  def engine(self) -> Optional[QAudioEngine]:
    """
    Calls Qt's 'QAudioEngine *QSpatialSound::engine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qspatialsound.html#engine

    Returns
    -------

    Optional[QAudioEngine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QAudioEngine *QSpatialSound::engine() const
    address = self.uglySide.call('ritual_ZNK13QSpatialSound6engineEv')
    from . import QAudioEngine
    return QAudioEngine._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setSource(self, url: QUrl) -> None:
    """
    Calls Qt's 'void QSpatialSound::setSource(const QUrl &url)'.

    Qt's own words: https://doc.qt.io/qt-6/qspatialsound.html#setSource

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QSpatialSound::setSource(const QUrl &url)
    self.uglySide.call(
        'ritual_ZN13QSpatialSound9setSourceERK4QUrl', self._valueOf(url),
    )

  @overload(int)
  def setLoops(self, loops: int) -> None:
    """
    Calls Qt's 'void QSpatialSound::setLoops(int loops)'.

    Qt's own words: https://doc.qt.io/qt-6/qspatialsound.html#setLoops

    Parameters
    ----------

    loops : int
      Passed on as it is.
    """
    #  void QSpatialSound::setLoops(int loops)
    self.uglySide.call('ritual_ZN13QSpatialSound8setLoopsEi', loops)

  @overload(bool)
  def setAutoPlay(self, autoPlay: bool) -> None:
    """
    Calls Qt's 'void QSpatialSound::setAutoPlay(bool autoPlay)'.

    Qt's own words: https://doc.qt.io/qt-6/qspatialsound.html#setAutoPlay

    Parameters
    ----------

    autoPlay : bool
      Passed on as it is.
    """
    #  void QSpatialSound::setAutoPlay(bool autoPlay)
    self.uglySide.call('ritual_ZN13QSpatialSound11setAutoPlayEb', autoPlay)

  @overload(QVector3D)
  def setPosition(self, pos: QVector3D) -> None:
    """
    Calls Qt's 'void QSpatialSound::setPosition(QVector3D pos)'.

    Qt's own words: https://doc.qt.io/qt-6/qspatialsound.html#setPosition

    Parameters
    ----------

    pos : QVector3D
      Passed on as a value: Qt reads the C++ QVector3D, which stays Python's
      own.
    """
    #  void QSpatialSound::setPosition(QVector3D pos)
    self.uglySide.call(
        'ritual_ZN13QSpatialSound11setPositionE9QVector3D',
        self._valueOf(pos),
    )

  @overload(QQuaternion)
  def setRotation(self, q: QQuaternion) -> None:
    """
    Calls Qt's 'void QSpatialSound::setRotation(const QQuaternion &q)'.

    Qt's own words: https://doc.qt.io/qt-6/qspatialsound.html#setRotation

    Parameters
    ----------

    q : QQuaternion
      Passed on as a value: Qt reads the C++ QQuaternion, which stays
      Python's own.
    """
    #  void QSpatialSound::setRotation(const QQuaternion &q)
    self.uglySide.call(
        'ritual_ZN13QSpatialSound11setRotationERK11QQuaternion',
        self._valueOf(q),
    )

  @overload(float)
  def setVolume(self, volume: float) -> None:
    """
    Calls Qt's 'void QSpatialSound::setVolume(float volume)'.

    Qt's own words: https://doc.qt.io/qt-6/qspatialsound.html#setVolume

    Parameters
    ----------

    volume : float
      Passed on as it is.
    """
    #  void QSpatialSound::setVolume(float volume)
    self.uglySide.call('ritual_ZN13QSpatialSound9setVolumeEf', volume)

  @overload(DistanceModel)
  def setDistanceModel(self, model: DistanceModel) -> None:
    """
    Calls Qt's 'void QSpatialSound::setDistanceModel(DistanceModel model)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspatialsound.html#setDistanceModel

    Parameters
    ----------

    model : DistanceModel
      Passed on as its number.
    """
    #  void QSpatialSound::setDistanceModel(DistanceModel model)
    self.uglySide.call(
        'ritual_ZN13QSpatialSound16setDistanceModelENS_13DistanceModelE',
        model.value,
    )

  @overload(float)
  def setSize(self, size: float) -> None:
    """
    Calls Qt's 'void QSpatialSound::setSize(float size)'.

    Qt's own words: https://doc.qt.io/qt-6/qspatialsound.html#setSize

    Parameters
    ----------

    size : float
      Passed on as it is.
    """
    #  void QSpatialSound::setSize(float size)
    self.uglySide.call('ritual_ZN13QSpatialSound7setSizeEf', size)

  @overload(float)
  def setDistanceCutoff(self, cutoff: float) -> None:
    """
    Calls Qt's 'void QSpatialSound::setDistanceCutoff(float cutoff)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspatialsound.html#setDistanceCutoff

    Parameters
    ----------

    cutoff : float
      Passed on as it is.
    """
    #  void QSpatialSound::setDistanceCutoff(float cutoff)
    self.uglySide.call(
        'ritual_ZN13QSpatialSound17setDistanceCutoffEf', cutoff,
    )

  @overload(float)
  def setManualAttenuation(self, attenuation: float) -> None:
    """
    Calls Qt's 'void QSpatialSound::setManualAttenuation(float attenuation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspatialsound.html#setManualAttenuation

    Parameters
    ----------

    attenuation : float
      Passed on as it is.
    """
    #  void QSpatialSound::setManualAttenuation(float attenuation)
    self.uglySide.call(
        'ritual_ZN13QSpatialSound20setManualAttenuationEf', attenuation,
    )

  @overload(float)
  def setOcclusionIntensity(self, occlusion: float) -> None:
    """
    Calls Qt's 'void QSpatialSound::setOcclusionIntensity(float occlusion)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspatialsound.html#setOcclusionIntensity

    Parameters
    ----------

    occlusion : float
      Passed on as it is.
    """
    #  void QSpatialSound::setOcclusionIntensity(float occlusion)
    self.uglySide.call(
        'ritual_ZN13QSpatialSound21setOcclusionIntensityEf', occlusion,
    )

  @overload(float)
  def setDirectivity(self, alpha: float) -> None:
    """
    Calls Qt's 'void QSpatialSound::setDirectivity(float alpha)'.

    Qt's own words: https://doc.qt.io/qt-6/qspatialsound.html#setDirectivity

    Parameters
    ----------

    alpha : float
      Passed on as it is.
    """
    #  void QSpatialSound::setDirectivity(float alpha)
    self.uglySide.call('ritual_ZN13QSpatialSound14setDirectivityEf', alpha)

  @overload(float)
  def setDirectivityOrder(self, alpha: float) -> None:
    """
    Calls Qt's 'void QSpatialSound::setDirectivityOrder(float alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspatialsound.html#setDirectivityOrder

    Parameters
    ----------

    alpha : float
      Passed on as it is.
    """
    #  void QSpatialSound::setDirectivityOrder(float alpha)
    self.uglySide.call(
        'ritual_ZN13QSpatialSound19setDirectivityOrderEf', alpha,
    )

  @overload(float)
  def setNearFieldGain(self, gain: float) -> None:
    """
    Calls Qt's 'void QSpatialSound::setNearFieldGain(float gain)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspatialsound.html#setNearFieldGain

    Parameters
    ----------

    gain : float
      Passed on as it is.
    """
    #  void QSpatialSound::setNearFieldGain(float gain)
    self.uglySide.call('ritual_ZN13QSpatialSound16setNearFieldGainEf', gain)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QAudioEngine)
  @overload(NoneType)
  def __init__(self, engine: Optional[QAudioEngine]) -> None:
    """
    Notes what was given, for Qt's 'QSpatialSound::QSpatialSound(QAudioEngine
    *engine)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qspatialsound.html#QSpatialSound

    Parameters
    ----------

    engine : Optional[QAudioEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QSpatialSound::QSpatialSound(QAudioEngine *engine)
    self._noteCreation(QSpatialSound, lambda: Rituals.call(
        'ritual_ZN13QSpatialSoundC1EP12QAudioEngine',
        self._addressOf(engine),
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

  def sourceChanged(self) -> None:
    """
    Calls Qt's 'void QSpatialSound::sourceChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qspatialsound.html#sourceChanged
    """
    #  void QSpatialSound::sourceChanged()
    self.uglySide.call('ritual_ZN13QSpatialSound13sourceChangedEv')

  def loopsChanged(self) -> None:
    """
    Calls Qt's 'void QSpatialSound::loopsChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qspatialsound.html#loopsChanged
    """
    #  void QSpatialSound::loopsChanged()
    self.uglySide.call('ritual_ZN13QSpatialSound12loopsChangedEv')

  def autoPlayChanged(self) -> None:
    """
    Calls Qt's 'void QSpatialSound::autoPlayChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qspatialsound.html#autoPlayChanged
    """
    #  void QSpatialSound::autoPlayChanged()
    self.uglySide.call('ritual_ZN13QSpatialSound15autoPlayChangedEv')

  def positionChanged(self) -> None:
    """
    Calls Qt's 'void QSpatialSound::positionChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qspatialsound.html#positionChanged
    """
    #  void QSpatialSound::positionChanged()
    self.uglySide.call('ritual_ZN13QSpatialSound15positionChangedEv')

  def rotationChanged(self) -> None:
    """
    Calls Qt's 'void QSpatialSound::rotationChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qspatialsound.html#rotationChanged
    """
    #  void QSpatialSound::rotationChanged()
    self.uglySide.call('ritual_ZN13QSpatialSound15rotationChangedEv')

  def volumeChanged(self) -> None:
    """
    Calls Qt's 'void QSpatialSound::volumeChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qspatialsound.html#volumeChanged
    """
    #  void QSpatialSound::volumeChanged()
    self.uglySide.call('ritual_ZN13QSpatialSound13volumeChangedEv')

  def distanceModelChanged(self) -> None:
    """
    Calls Qt's 'void QSpatialSound::distanceModelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspatialsound.html#distanceModelChanged
    """
    #  void QSpatialSound::distanceModelChanged()
    self.uglySide.call('ritual_ZN13QSpatialSound20distanceModelChangedEv')

  def sizeChanged(self) -> None:
    """
    Calls Qt's 'void QSpatialSound::sizeChanged()'.

    Qt's own words: https://doc.qt.io/qt-6/qspatialsound.html#sizeChanged
    """
    #  void QSpatialSound::sizeChanged()
    self.uglySide.call('ritual_ZN13QSpatialSound11sizeChangedEv')

  def distanceCutoffChanged(self) -> None:
    """
    Calls Qt's 'void QSpatialSound::distanceCutoffChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspatialsound.html#distanceCutoffChanged
    """
    #  void QSpatialSound::distanceCutoffChanged()
    self.uglySide.call('ritual_ZN13QSpatialSound21distanceCutoffChangedEv')

  def manualAttenuationChanged(self) -> None:
    """
    Calls Qt's 'void QSpatialSound::manualAttenuationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspatialsound.html#manualAttenuationChanged
    """
    #  void QSpatialSound::manualAttenuationChanged()
    self.uglySide.call(
        'ritual_ZN13QSpatialSound24manualAttenuationChangedEv',
    )

  def occlusionIntensityChanged(self) -> None:
    """
    Calls Qt's 'void QSpatialSound::occlusionIntensityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspatialsound.html#occlusionIntensityChanged
    """
    #  void QSpatialSound::occlusionIntensityChanged()
    self.uglySide.call(
        'ritual_ZN13QSpatialSound25occlusionIntensityChangedEv',
    )

  def directivityChanged(self) -> None:
    """
    Calls Qt's 'void QSpatialSound::directivityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspatialsound.html#directivityChanged
    """
    #  void QSpatialSound::directivityChanged()
    self.uglySide.call('ritual_ZN13QSpatialSound18directivityChangedEv')

  def directivityOrderChanged(self) -> None:
    """
    Calls Qt's 'void QSpatialSound::directivityOrderChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspatialsound.html#directivityOrderChanged
    """
    #  void QSpatialSound::directivityOrderChanged()
    self.uglySide.call('ritual_ZN13QSpatialSound23directivityOrderChangedEv')

  def nearFieldGainChanged(self) -> None:
    """
    Calls Qt's 'void QSpatialSound::nearFieldGainChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qspatialsound.html#nearFieldGainChanged
    """
    #  void QSpatialSound::nearFieldGainChanged()
    self.uglySide.call('ritual_ZN13QSpatialSound20nearFieldGainChangedEv')

  def play(self) -> None:
    """
    Calls Qt's 'void QSpatialSound::play()'.

    Qt's own words: https://doc.qt.io/qt-6/qspatialsound.html#play
    """
    #  void QSpatialSound::play()
    self.uglySide.call('ritual_ZN13QSpatialSound4playEv')

  def pause(self) -> None:
    """
    Calls Qt's 'void QSpatialSound::pause()'.

    Qt's own words: https://doc.qt.io/qt-6/qspatialsound.html#pause
    """
    #  void QSpatialSound::pause()
    self.uglySide.call('ritual_ZN13QSpatialSound5pauseEv')

  def stop(self) -> None:
    """
    Calls Qt's 'void QSpatialSound::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/qspatialsound.html#stop
    """
    #  void QSpatialSound::stop()
    self.uglySide.call('ritual_ZN13QSpatialSound4stopEv')
