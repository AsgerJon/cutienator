"""
QQuick3DSpatialSound binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQuick3DSpatialAudio/6.12.0/QtQuick3DSpatialAudio/private/qquick3dspatialsound_p.h,
#  Qt 6.12.0. Changes made here are lost.
#
#  Qt means QQuick3DSpatialSound to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject, QUrl
  from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSSGRenderGraphObject = WAIT['QSSGRenderGraphObject']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQuick3DSpatialSound(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQuick3DSpatialSound: a plain Python object standing
  in front of one C++ QQuick3DSpatialSound.

  What exists
  -----------

  Every function of Qt's QQuick3DSpatialSound that has a ritual and that
  Python can call so far, 43 names in all: 'metaObject', 'setSource',
  'source', 'setVolume', 'volume', 'setDistanceModel', 'distanceModel',
  'setSize', 'size', 'setDistanceCutoff', 'distanceCutoff',
  'setManualAttenuation', 'manualAttenuation', 'setOcclusionIntensity',
  'occlusionIntensity', 'setDirectivity', 'directivity',
  'setDirectivityOrder', 'directivityOrder', 'setNearFieldGain',
  'nearFieldGain', 'loops', 'setLoops', 'autoPlay', 'setAutoPlay', 'play',
  'pause', 'stop', 'sourceChanged', 'volumeChanged', 'distanceModelChanged',
  'sizeChanged', 'distanceCutoffChanged', 'manualAttenuationChanged',
  'occlusionIntensityChanged', 'directivityChanged',
  'directivityOrderChanged', 'nearFieldGainChanged', 'loopsChanged',
  'autoPlayChanged', 'updatePosition', 'updateRotation', 'updateSpatialNode'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQuick3DSpatialSound::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQuick3DSpatialSound::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QQuick3DSpatialSound::~QQuick3DSpatialSound()': the destructor:
    Python never removes a C++ QQuick3DSpatialSound.

  What has no ritual
  ------------------

  4 of the 50 functions Qt declares: 2 not a gap; 2 leans on
  'QQuick3DSpatialSound.

  What to expect
  --------------

  - The C++ QQuick3DSpatialSound is created at the first use, not by
    'QQuick3DSpatialSound(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQuick3DSpatialSound.
  - Qt tells when it has removed the C++ QQuick3DSpatialSound. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QQuick3DSpatialSound that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The enums Qt writes inside QQuick3DSpatialSound, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class DistanceModel(CuteNum):
    """
    The enum 'QQuick3DSpatialSound::DistanceModel' of Qt, with the 3 names Qt
    gives in it.
    """

    Logarithmic = Kee[int](0)
    Linear = Kee[int](1)
    ManualAttenuation = Kee[int](2)

  class Loops(CuteNum):
    """
    The enum 'QQuick3DSpatialSound::Loops' of Qt, with the 2 names Qt gives
    in it.
    """

    Infinite = Kee[int](-1)
    Once = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQuick3DSpatialSound'

  #  A C++ QQuick3DSpatialSound Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQuick3DSpatialSound'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQuick3DSpatialSound::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspatialsound.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQuick3DSpatialSound::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QQuick3DSpatialSound10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def source(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQuick3DSpatialSound::source() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dspatialsound.html#source

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQuick3DSpatialSound::source() const
    address = self.uglySide.call('ritual_ZNK20QQuick3DSpatialSound6sourceEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def volume(self) -> float:
    """
    Calls Qt's 'float QQuick3DSpatialSound::volume() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dspatialsound.html#volume
    """
    #  float QQuick3DSpatialSound::volume() const
    return self.uglySide.call('ritual_ZNK20QQuick3DSpatialSound6volumeEv')

  def distanceModel(self) -> DistanceModel:
    """
    Calls Qt's 'DistanceModel QQuick3DSpatialSound::distanceModel() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspatialsound.html#distanceModel

    Returns
    -------

    DistanceModel
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'DistanceModel(number)'
      gives.
    """
    #  DistanceModel QQuick3DSpatialSound::distanceModel() const
    return QQuick3DSpatialSound.DistanceModel(self.uglySide.call(
        'ritual_ZNK20QQuick3DSpatialSound13distanceModelEv',
    ))

  def size(self) -> float:
    """
    Calls Qt's 'float QQuick3DSpatialSound::size() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dspatialsound.html#size
    """
    #  float QQuick3DSpatialSound::size() const
    return self.uglySide.call('ritual_ZNK20QQuick3DSpatialSound4sizeEv')

  def distanceCutoff(self) -> float:
    """
    Calls Qt's 'float QQuick3DSpatialSound::distanceCutoff() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspatialsound.html#distanceCutoff
    """
    #  float QQuick3DSpatialSound::distanceCutoff() const
    return self.uglySide.call(
        'ritual_ZNK20QQuick3DSpatialSound14distanceCutoffEv',
    )

  def manualAttenuation(self) -> float:
    """
    Calls Qt's 'float QQuick3DSpatialSound::manualAttenuation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspatialsound.html#manualAttenuation
    """
    #  float QQuick3DSpatialSound::manualAttenuation() const
    return self.uglySide.call(
        'ritual_ZNK20QQuick3DSpatialSound17manualAttenuationEv',
    )

  def occlusionIntensity(self) -> float:
    """
    Calls Qt's 'float QQuick3DSpatialSound::occlusionIntensity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspatialsound.html#occlusionIntensity
    """
    #  float QQuick3DSpatialSound::occlusionIntensity() const
    return self.uglySide.call(
        'ritual_ZNK20QQuick3DSpatialSound18occlusionIntensityEv',
    )

  def directivity(self) -> float:
    """
    Calls Qt's 'float QQuick3DSpatialSound::directivity() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspatialsound.html#directivity
    """
    #  float QQuick3DSpatialSound::directivity() const
    return self.uglySide.call(
        'ritual_ZNK20QQuick3DSpatialSound11directivityEv',
    )

  def directivityOrder(self) -> float:
    """
    Calls Qt's 'float QQuick3DSpatialSound::directivityOrder() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspatialsound.html#directivityOrder
    """
    #  float QQuick3DSpatialSound::directivityOrder() const
    return self.uglySide.call(
        'ritual_ZNK20QQuick3DSpatialSound16directivityOrderEv',
    )

  def nearFieldGain(self) -> float:
    """
    Calls Qt's 'float QQuick3DSpatialSound::nearFieldGain() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspatialsound.html#nearFieldGain
    """
    #  float QQuick3DSpatialSound::nearFieldGain() const
    return self.uglySide.call(
        'ritual_ZNK20QQuick3DSpatialSound13nearFieldGainEv',
    )

  def loops(self) -> int:
    """
    Calls Qt's 'int QQuick3DSpatialSound::loops() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dspatialsound.html#loops
    """
    #  int QQuick3DSpatialSound::loops() const
    return self.uglySide.call('ritual_ZNK20QQuick3DSpatialSound5loopsEv')

  def autoPlay(self) -> bool:
    """
    Calls Qt's 'bool QQuick3DSpatialSound::autoPlay() const'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dspatialsound.html#autoPlay
    """
    #  bool QQuick3DSpatialSound::autoPlay() const
    return self.uglySide.call('ritual_ZNK20QQuick3DSpatialSound8autoPlayEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QUrl)
  def setSource(self, source: QUrl) -> None:
    """
    Calls Qt's 'void QQuick3DSpatialSound::setSource(const QUrl &source)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspatialsound.html#setSource

    Parameters
    ----------

    source : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.
    """
    #  void QQuick3DSpatialSound::setSource(const QUrl &source)
    self.uglySide.call(
        'ritual_ZN20QQuick3DSpatialSound9setSourceERK4QUrl',
        self._valueOf(source),
    )

  @overload(float)
  def setVolume(self, volume: float) -> None:
    """
    Calls Qt's 'void QQuick3DSpatialSound::setVolume(float volume)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspatialsound.html#setVolume

    Parameters
    ----------

    volume : float
      Passed on as it is.
    """
    #  void QQuick3DSpatialSound::setVolume(float volume)
    self.uglySide.call('ritual_ZN20QQuick3DSpatialSound9setVolumeEf', volume)

  @overload(DistanceModel)
  def setDistanceModel(self, model: DistanceModel) -> None:
    """
    Calls Qt's 'void QQuick3DSpatialSound::setDistanceModel(DistanceModel
    model)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspatialsound.html#setDistanceModel

    Parameters
    ----------

    model : DistanceModel
      Passed on as its number.
    """
    #  void QQuick3DSpatialSound::setDistanceModel(DistanceModel model)
    self.uglySide.call(
        'ritual_ZN20QQuick3DSpatialSound16setDistanceModelENS_13DistanceMod'
        'elE',
        model.value,
    )

  @overload(float)
  def setSize(self, min: float) -> None:
    """
    Calls Qt's 'void QQuick3DSpatialSound::setSize(float min)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dspatialsound.html#setSize

    Parameters
    ----------

    min : float
      Passed on as it is.
    """
    #  void QQuick3DSpatialSound::setSize(float min)
    self.uglySide.call('ritual_ZN20QQuick3DSpatialSound7setSizeEf', min)

  @overload(float)
  def setDistanceCutoff(self, max: float) -> None:
    """
    Calls Qt's 'void QQuick3DSpatialSound::setDistanceCutoff(float max)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspatialsound.html#setDistanceCutoff

    Parameters
    ----------

    max : float
      Passed on as it is.
    """
    #  void QQuick3DSpatialSound::setDistanceCutoff(float max)
    self.uglySide.call(
        'ritual_ZN20QQuick3DSpatialSound17setDistanceCutoffEf', max,
    )

  @overload(float)
  def setManualAttenuation(self, attenuation: float) -> None:
    """
    Calls Qt's 'void QQuick3DSpatialSound::setManualAttenuation(float
    attenuation)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspatialsound.html#setManualAttenuation

    Parameters
    ----------

    attenuation : float
      Passed on as it is.
    """
    #  void QQuick3DSpatialSound::setManualAttenuation(float attenuation)
    self.uglySide.call(
        'ritual_ZN20QQuick3DSpatialSound20setManualAttenuationEf',
        attenuation,
    )

  @overload(float)
  def setOcclusionIntensity(self, occlusion: float) -> None:
    """
    Calls Qt's 'void QQuick3DSpatialSound::setOcclusionIntensity(float
    occlusion)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspatialsound.html#setOcclusionIntensity

    Parameters
    ----------

    occlusion : float
      Passed on as it is.
    """
    #  void QQuick3DSpatialSound::setOcclusionIntensity(float occlusion)
    self.uglySide.call(
        'ritual_ZN20QQuick3DSpatialSound21setOcclusionIntensityEf',
        occlusion,
    )

  @overload(float)
  def setDirectivity(self, alpha: float) -> None:
    """
    Calls Qt's 'void QQuick3DSpatialSound::setDirectivity(float alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspatialsound.html#setDirectivity

    Parameters
    ----------

    alpha : float
      Passed on as it is.
    """
    #  void QQuick3DSpatialSound::setDirectivity(float alpha)
    self.uglySide.call(
        'ritual_ZN20QQuick3DSpatialSound14setDirectivityEf', alpha,
    )

  @overload(float)
  def setDirectivityOrder(self, alpha: float) -> None:
    """
    Calls Qt's 'void QQuick3DSpatialSound::setDirectivityOrder(float alpha)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspatialsound.html#setDirectivityOrder

    Parameters
    ----------

    alpha : float
      Passed on as it is.
    """
    #  void QQuick3DSpatialSound::setDirectivityOrder(float alpha)
    self.uglySide.call(
        'ritual_ZN20QQuick3DSpatialSound19setDirectivityOrderEf', alpha,
    )

  @overload(float)
  def setNearFieldGain(self, gain: float) -> None:
    """
    Calls Qt's 'void QQuick3DSpatialSound::setNearFieldGain(float gain)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspatialsound.html#setNearFieldGain

    Parameters
    ----------

    gain : float
      Passed on as it is.
    """
    #  void QQuick3DSpatialSound::setNearFieldGain(float gain)
    self.uglySide.call(
        'ritual_ZN20QQuick3DSpatialSound16setNearFieldGainEf', gain,
    )

  @overload(int)
  def setLoops(self, loops: int) -> None:
    """
    Calls Qt's 'void QQuick3DSpatialSound::setLoops(int loops)'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dspatialsound.html#setLoops

    Parameters
    ----------

    loops : int
      Passed on as it is.
    """
    #  void QQuick3DSpatialSound::setLoops(int loops)
    self.uglySide.call('ritual_ZN20QQuick3DSpatialSound8setLoopsEi', loops)

  @overload(bool)
  def setAutoPlay(self, autoPlay: bool) -> None:
    """
    Calls Qt's 'void QQuick3DSpatialSound::setAutoPlay(bool autoPlay)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspatialsound.html#setAutoPlay

    Parameters
    ----------

    autoPlay : bool
      Passed on as it is.
    """
    #  void QQuick3DSpatialSound::setAutoPlay(bool autoPlay)
    self.uglySide.call(
        'ritual_ZN20QQuick3DSpatialSound11setAutoPlayEb', autoPlay,
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QQuick3DSpatialSound::QQuick3DSpatialSound()': leans on
    'QQuick3DSpatialSound::qt_metacall(QMetaObject::Call, int, void**)',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QQuick3DSpatialSound.__init__' has no cute function yet. Qt's "
        "'QQuick3DSpatialSound::QQuick3DSpatialSound()': leans on "
        "'QQuick3DSpatialSound::qt_metacall(QMetaObject::Call, int, "
        "void**)', which Qt's source does not mark for use from outside Qt "
        "and has no code for that could be taken.")

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

  def play(self) -> None:
    """
    Calls Qt's 'void QQuick3DSpatialSound::play()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dspatialsound.html#play
    """
    #  void QQuick3DSpatialSound::play()
    self.uglySide.call('ritual_ZN20QQuick3DSpatialSound4playEv')

  def pause(self) -> None:
    """
    Calls Qt's 'void QQuick3DSpatialSound::pause()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dspatialsound.html#pause
    """
    #  void QQuick3DSpatialSound::pause()
    self.uglySide.call('ritual_ZN20QQuick3DSpatialSound5pauseEv')

  def stop(self) -> None:
    """
    Calls Qt's 'void QQuick3DSpatialSound::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/qquick3dspatialsound.html#stop
    """
    #  void QQuick3DSpatialSound::stop()
    self.uglySide.call('ritual_ZN20QQuick3DSpatialSound4stopEv')

  def sourceChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSpatialSound::sourceChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspatialsound.html#sourceChanged
    """
    #  void QQuick3DSpatialSound::sourceChanged()
    self.uglySide.call('ritual_ZN20QQuick3DSpatialSound13sourceChangedEv')

  def volumeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSpatialSound::volumeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspatialsound.html#volumeChanged
    """
    #  void QQuick3DSpatialSound::volumeChanged()
    self.uglySide.call('ritual_ZN20QQuick3DSpatialSound13volumeChangedEv')

  def distanceModelChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSpatialSound::distanceModelChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspatialsound.html#distanceModelChanged
    """
    #  void QQuick3DSpatialSound::distanceModelChanged()
    self.uglySide.call(
        'ritual_ZN20QQuick3DSpatialSound20distanceModelChangedEv',
    )

  def sizeChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSpatialSound::sizeChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspatialsound.html#sizeChanged
    """
    #  void QQuick3DSpatialSound::sizeChanged()
    self.uglySide.call('ritual_ZN20QQuick3DSpatialSound11sizeChangedEv')

  def distanceCutoffChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSpatialSound::distanceCutoffChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspatialsound.html#distanceCutoffChanged
    """
    #  void QQuick3DSpatialSound::distanceCutoffChanged()
    self.uglySide.call(
        'ritual_ZN20QQuick3DSpatialSound21distanceCutoffChangedEv',
    )

  def manualAttenuationChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSpatialSound::manualAttenuationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspatialsound.html#manualAttenuationChanged
    """
    #  void QQuick3DSpatialSound::manualAttenuationChanged()
    self.uglySide.call(
        'ritual_ZN20QQuick3DSpatialSound24manualAttenuationChangedEv',
    )

  def occlusionIntensityChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSpatialSound::occlusionIntensityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspatialsound.html
    """
    #  void QQuick3DSpatialSound::occlusionIntensityChanged()
    self.uglySide.call(
        'ritual_ZN20QQuick3DSpatialSound25occlusionIntensityChangedEv',
    )

  def directivityChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSpatialSound::directivityChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspatialsound.html#directivityChanged
    """
    #  void QQuick3DSpatialSound::directivityChanged()
    self.uglySide.call(
        'ritual_ZN20QQuick3DSpatialSound18directivityChangedEv',
    )

  def directivityOrderChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSpatialSound::directivityOrderChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspatialsound.html#directivityOrderChanged
    """
    #  void QQuick3DSpatialSound::directivityOrderChanged()
    self.uglySide.call(
        'ritual_ZN20QQuick3DSpatialSound23directivityOrderChangedEv',
    )

  def nearFieldGainChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSpatialSound::nearFieldGainChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspatialsound.html#nearFieldGainChanged
    """
    #  void QQuick3DSpatialSound::nearFieldGainChanged()
    self.uglySide.call(
        'ritual_ZN20QQuick3DSpatialSound20nearFieldGainChangedEv',
    )

  def loopsChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSpatialSound::loopsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspatialsound.html#loopsChanged
    """
    #  void QQuick3DSpatialSound::loopsChanged()
    self.uglySide.call('ritual_ZN20QQuick3DSpatialSound12loopsChangedEv')

  def autoPlayChanged(self) -> None:
    """
    Calls Qt's 'void QQuick3DSpatialSound::autoPlayChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspatialsound.html#autoPlayChanged
    """
    #  void QQuick3DSpatialSound::autoPlayChanged()
    self.uglySide.call('ritual_ZN20QQuick3DSpatialSound15autoPlayChangedEv')

  def updatePosition(self) -> None:
    """
    Calls Qt's 'void QQuick3DSpatialSound::updatePosition()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspatialsound.html#updatePosition
    """
    #  void QQuick3DSpatialSound::updatePosition()
    self.uglySide.call('ritual_ZN20QQuick3DSpatialSound14updatePositionEv')

  def updateRotation(self) -> None:
    """
    Calls Qt's 'void QQuick3DSpatialSound::updateRotation()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspatialsound.html#updateRotation
    """
    #  void QQuick3DSpatialSound::updateRotation()
    self.uglySide.call('ritual_ZN20QQuick3DSpatialSound14updateRotationEv')

  @overload(QSSGRenderGraphObject)
  @overload(NoneType)
  def updateSpatialNode(
      self,
      a0: Optional[QSSGRenderGraphObject],
  ) -> Optional[QSSGRenderGraphObject]:
    """
    Calls Qt's 'QSSGRenderGraphObject
    *QQuick3DSpatialSound::updateSpatialNode(QSSGRenderGraphObject *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qquick3dspatialsound.html#updateSpatialNode

    Parameters
    ----------

    a0 : Optional[QSSGRenderGraphObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QSSGRenderGraphObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QSSGRenderGraphObject
    #      *QQuick3DSpatialSound::updateSpatialNode(QSSGRenderGraphObject
    #      *a0)
    ritual = (
        'ritual_ZN20QQuick3DSpatialSound17updateSpatialNodeEP21QSSGRenderGr'
        'aphObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QQuick3DSpatialSound17updateSpatialNodeEP21QSSGRe'
          'nderGraphObject')
    address = self.uglySide.call(ritual, self._addressOf(a0))
    from ..QtQuick3DRuntimeRender import QSSGRenderGraphObject
    return QSSGRenderGraphObject._cuteAt(address)
