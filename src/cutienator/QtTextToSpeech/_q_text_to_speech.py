"""
QTextToSpeech binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtTextToSpeech/qtexttospeech.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, WAIT
from ..occult import Rituals
from ..QtCore import QList, QMap, QObject, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QLocale, QMetaObject, QVariant
  from . import QTextToSpeechPrivate, QVoice
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QLocale = WAIT['QLocale']
  QVariant = WAIT['QVariant']
  QVoice = WAIT['QVoice']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTextToSpeech(QObject):
  """
  The cute side of Qt's QTextToSpeech: a plain Python object standing in
  front of one C++ QTextToSpeech.

  It is built on the cute 'QObject', as Qt's QTextToSpeech is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTextToSpeech that has a ritual and that Python can
  call so far, 38 names in all: 'metaObject', 'tr', 'd_func', 'setEngine',
  'engine', 'engineCapabilities', 'state', 'errorReason', 'errorString',
  'availableLocales', 'locale', 'voice', 'availableVoices', 'rate', 'pitch',
  'volume', 'availableEngines', 'say', 'enqueue', 'stop', 'pause', 'resume',
  'setLocale', 'setRate', 'setPitch', 'setVolume', 'setVoice',
  'engineChanged', 'stateChanged', 'errorOccurred', 'localeChanged',
  'rateChanged', 'pitchChanged', 'volumeChanged', 'voiceChanged',
  'sayingWord', 'aboutToSynthesize', 'allVoices'. It can be made from Python,
  in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QTextToSpeech::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QTextToSpeech::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'const QTextToSpeechPrivate *QTextToSpeech::d_func() const': takes
    in Python what 'QTextToSpeechPrivate *QTextToSpeech::d_func()' takes.
  - Qt's 'QTextToSpeech::~QTextToSpeech()': the destructor: Python never
    removes a C++ QTextToSpeech.
  - Qt's 'void QTextToSpeech::synthesizeImpl(const QString &text,
    QtPrivate::QSlotObjectBase *slotObj, const QObject *context,
    SynthesizeOverload overload)': names the enum
    'QTextToSpeech::SynthesizeOverload', whose class cannot be named here.

  What has no ritual
  ------------------

  8 of the 54 functions Qt declares: 4 a template; 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QTextToSpeech is created at the first use, not by
    'QTextToSpeech(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTextToSpeech.
  - Qt tells when it has removed the C++ QTextToSpeech. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QTextToSpeech that has no cute function yet,
    'findVoices', 'synthesize', 'synthesizeImpl', 'voiceMatches', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QTextToSpeech, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class BoundaryHint(CuteNum, scoped=True):
    """
    The enum 'QTextToSpeech::BoundaryHint' of Qt, with the 5 names Qt gives
    in it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    Default = Kee[int](0)
    Immediate = Kee[int](1)
    Word = Kee[int](2)
    Sentence = Kee[int](3)
    Utterance = Kee[int](4)

  class Capability(CuteFlags, scoped=True):
    """
    The flags enum 'QTextToSpeech::Capability' of Qt, with the 5 names Qt
    gives in it. Qt names the type of its combinations
    'QTextToSpeech::Capabilities'. C++ keeps these names inside the enum, so
    the class that holds the enum does not have them.
    """

    NULL = 0x0
    Speak = 0x1
    PauseResume = 0x2
    WordByWordProgress = 0x4
    Synthesize = 0x8

  Capabilities = Capability

  class ErrorReason(CuteNum, scoped=True):
    """
    The enum 'QTextToSpeech::ErrorReason' of Qt, with the 5 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    NoError = Kee[int](0)
    Initialization = Kee[int](1)
    Configuration = Kee[int](2)
    Input = Kee[int](3)
    Playback = Kee[int](4)

  class State(CuteNum):
    """
    The enum 'QTextToSpeech::State' of Qt, with the 5 names Qt gives in it.
    """

    Ready = Kee[int](0)
    Speaking = Kee[int](1)
    Paused = Kee[int](2)
    Error = Kee[int](3)
    Synthesizing = Kee[int](4)

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
    Calls Qt's 'QString QTextToSpeech::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeech.html#tr

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
    #  QString QTextToSpeech::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QTextToSpeech2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def availableEngines() -> QStringList:
    """
    Calls Qt's 'QStringList QTextToSpeech::availableEngines()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttospeech.html#availableEngines

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QTextToSpeech::availableEngines()
    address = Rituals.call('ritual_ZN13QTextToSpeech16availableEnginesEv')
    return QStringList._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextToSpeech'

  #  A C++ QTextToSpeech Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTextToSpeech'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QTextToSpeech::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeech.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QTextToSpeech::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QTextToSpeech10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def engine(self) -> str:
    """
    Calls Qt's 'QString QTextToSpeech::engine() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeech.html#engine

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextToSpeech::engine() const
    return self.uglySide.call('ritual_ZNK13QTextToSpeech6engineEv')

  def engineCapabilities(self) -> Capabilities:
    """
    Calls Qt's 'QTextToSpeech::Capabilities
    QTextToSpeech::engineCapabilities() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttospeech.html#engineCapabilities

    Returns
    -------

    Capabilities
      The value standing for the combination Qt gave back.
    """
    #  QTextToSpeech::Capabilities QTextToSpeech::engineCapabilities() const
    return QTextToSpeech.Capabilities(self.uglySide.call(
        'ritual_ZNK13QTextToSpeech18engineCapabilitiesEv',
    ))

  def state(self) -> State:
    """
    Calls Qt's 'QTextToSpeech::State QTextToSpeech::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeech.html#state

    Returns
    -------

    State
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'State(number)' gives.
    """
    #  QTextToSpeech::State QTextToSpeech::state() const
    return QTextToSpeech.State(self.uglySide.call(
        'ritual_ZNK13QTextToSpeech5stateEv',
    ))

  def errorReason(self) -> ErrorReason:
    """
    Calls Qt's 'QTextToSpeech::ErrorReason QTextToSpeech::errorReason()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeech.html#errorReason

    Returns
    -------

    ErrorReason
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'ErrorReason(number)'
      gives.
    """
    #  QTextToSpeech::ErrorReason QTextToSpeech::errorReason() const
    return QTextToSpeech.ErrorReason(self.uglySide.call(
        'ritual_ZNK13QTextToSpeech11errorReasonEv',
    ))

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QTextToSpeech::errorString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeech.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextToSpeech::errorString() const
    return self.uglySide.call('ritual_ZNK13QTextToSpeech11errorStringEv')

  def availableLocales(self) -> QList[QLocale]:
    """
    Calls Qt's 'QList<QLocale> QTextToSpeech::availableLocales() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttospeech.html#availableLocales

    Returns
    -------

    QList[QLocale]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QLocale> QTextToSpeech::availableLocales() const
    address = self.uglySide.call(
        'ritual_ZNK13QTextToSpeech16availableLocalesEv',
    )
    from ..QtCore import QLocale
    return QList[QLocale]._cuteOwning(address)

  def locale(self) -> QLocale:
    """
    Calls Qt's 'QLocale QTextToSpeech::locale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeech.html#locale

    Returns
    -------

    QLocale
      A new cute QLocale around the copy Qt gave back. Python owns it.
    """
    #  QLocale QTextToSpeech::locale() const
    address = self.uglySide.call('ritual_ZNK13QTextToSpeech6localeEv')
    from ..QtCore import QLocale
    return QLocale._cuteOwning(address)

  def voice(self) -> QVoice:
    """
    Calls Qt's 'QVoice QTextToSpeech::voice() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeech.html#voice

    Returns
    -------

    QVoice
      A new cute QVoice around the copy Qt gave back. Python owns it.
    """
    #  QVoice QTextToSpeech::voice() const
    address = self.uglySide.call('ritual_ZNK13QTextToSpeech5voiceEv')
    from . import QVoice
    return QVoice._cuteOwning(address)

  def availableVoices(self) -> QList[QVoice]:
    """
    Calls Qt's 'QList<QVoice> QTextToSpeech::availableVoices() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeech.html#availableVoices

    Returns
    -------

    QList[QVoice]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QVoice> QTextToSpeech::availableVoices() const
    address = self.uglySide.call(
        'ritual_ZNK13QTextToSpeech15availableVoicesEv',
    )
    from . import QVoice
    return QList[QVoice]._cuteOwning(address)

  def rate(self) -> float:
    """
    Calls Qt's 'double QTextToSpeech::rate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeech.html#rate
    """
    #  double QTextToSpeech::rate() const
    return self.uglySide.call('ritual_ZNK13QTextToSpeech4rateEv')

  def pitch(self) -> float:
    """
    Calls Qt's 'double QTextToSpeech::pitch() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeech.html#pitch
    """
    #  double QTextToSpeech::pitch() const
    return self.uglySide.call('ritual_ZNK13QTextToSpeech5pitchEv')

  def volume(self) -> float:
    """
    Calls Qt's 'double QTextToSpeech::volume() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeech.html#volume
    """
    #  double QTextToSpeech::volume() const
    return self.uglySide.call('ritual_ZNK13QTextToSpeech6volumeEv')

  @overload(QLocale)
  @overload(NoneType)
  def allVoices(self, locale: Optional[QLocale]) -> QList[QVoice]:
    """
    Calls Qt's 'QList<QVoice> QTextToSpeech::allVoices(const QLocale *locale)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeech.html#allVoices

    Parameters
    ----------

    locale : Optional[QLocale]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    QList[QVoice]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QVoice> QTextToSpeech::allVoices(const QLocale *locale) const
    address = self.uglySide.call(
        'ritual_ZNK13QTextToSpeech9allVoicesEPK7QLocale',
        self._addressOf(locale),
    )
    from . import QVoice
    return QList[QVoice]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str, QMap[str, QVariant])
  def setEngine(self, engine: str, params: QMap[str, QVariant]) -> bool:
    """
    Calls Qt's 'bool QTextToSpeech::setEngine(const QString &engine, const
    QVariantMap &params)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeech.html#setEngine

    Parameters
    ----------

    engine : str
      Passed on as it is: a QString is made of it for the call.

    params : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.
    """
    #  bool QTextToSpeech::setEngine(const QString &engine, const QVariantMap
    #      &params)
    return self.uglySide.call(
        'ritual_ZN13QTextToSpeech9setEngineERK7QStringRK4QMapIS0_8QVariantE',
        engine, self._valueOf(params),
    )

  @overload(QLocale)
  def setLocale(self, locale: QLocale) -> None:
    """
    Calls Qt's 'void QTextToSpeech::setLocale(const QLocale &locale)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeech.html#setLocale

    Parameters
    ----------

    locale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  void QTextToSpeech::setLocale(const QLocale &locale)
    self.uglySide.call(
        'ritual_ZN13QTextToSpeech9setLocaleERK7QLocale',
        self._valueOf(locale),
    )

  @overload(float)
  def setRate(self, rate: float) -> None:
    """
    Calls Qt's 'void QTextToSpeech::setRate(double rate)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeech.html#setRate

    Parameters
    ----------

    rate : float
      Passed on as it is.
    """
    #  void QTextToSpeech::setRate(double rate)
    self.uglySide.call('ritual_ZN13QTextToSpeech7setRateEd', rate)

  @overload(float)
  def setPitch(self, pitch: float) -> None:
    """
    Calls Qt's 'void QTextToSpeech::setPitch(double pitch)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeech.html#setPitch

    Parameters
    ----------

    pitch : float
      Passed on as it is.
    """
    #  void QTextToSpeech::setPitch(double pitch)
    self.uglySide.call('ritual_ZN13QTextToSpeech8setPitchEd', pitch)

  @overload(float)
  def setVolume(self, volume: float) -> None:
    """
    Calls Qt's 'void QTextToSpeech::setVolume(double volume)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeech.html#setVolume

    Parameters
    ----------

    volume : float
      Passed on as it is.
    """
    #  void QTextToSpeech::setVolume(double volume)
    self.uglySide.call('ritual_ZN13QTextToSpeech9setVolumeEd', volume)

  @overload(QVoice)
  def setVoice(self, voice: QVoice) -> None:
    """
    Calls Qt's 'void QTextToSpeech::setVoice(const QVoice &voice)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeech.html#setVoice

    Parameters
    ----------

    voice : QVoice
      Passed on as a value: Qt reads the C++ QVoice, which stays Python's
      own.
    """
    #  void QTextToSpeech::setVoice(const QVoice &voice)
    self.uglySide.call(
        'ritual_ZN13QTextToSpeech8setVoiceERK6QVoice', self._valueOf(voice),
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QTextToSpeech::QTextToSpeech(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeech.html#QTextToSpeech

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QTextToSpeech::QTextToSpeech(QObject *parent)
    self._noteCreation(QTextToSpeech, lambda: Rituals.call(
        'ritual_ZN13QTextToSpeechC1EP7QObject',
        self._addressOf(parent, 'QObject'),
    ))

  @overload(str)
  @overload(str, QObject)
  @overload(str, NoneType)
  def __init__(self, engine: str, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QTextToSpeech::QTextToSpeech(const
    QString &engine, QObject *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeech.html#QTextToSpeech

    Parameters
    ----------

    engine : str
      Passed on as it is: a QString is made of it for the call.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QTextToSpeech::QTextToSpeech(const QString &engine, QObject *parent)
    self._noteCreation(QTextToSpeech, lambda: Rituals.call(
        'ritual_ZN13QTextToSpeechC1ERK7QStringP7QObject',
        engine, self._addressOf(parent, 'QObject'),
    ))

  @overload(str, QMap[str, QVariant])
  @overload(str, QMap[str, QVariant], QObject)
  @overload(str, QMap[str, QVariant], NoneType)
  def __init__(
      self,
      engine: str,
      params: QMap[str, QVariant],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's 'QTextToSpeech::QTextToSpeech(const
    QString &engine, const QVariantMap &params, QObject *parent)', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeech.html#QTextToSpeech

    Parameters
    ----------

    engine : str
      Passed on as it is: a QString is made of it for the call.

    params : QMap[str, QVariant]
      Passed on as a map of Qt: Qt reads the C++ map, which stays Python's
      own. A dict of Python is made into one first, and refused when a key or
      a value does not fit.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QTextToSpeech::QTextToSpeech(const QString &engine, const QVariantMap
    #      &params, QObject *parent)
    self._noteCreation(QTextToSpeech, lambda: Rituals.call(
        'ritual_ZN13QTextToSpeechC1ERK7QStringRK4QMapIS0_8QVariantEP7QObjec'
        't',
        engine, self._valueOf(params), self._addressOf(parent, 'QObject'),
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

  def d_func(self) -> Optional[QTextToSpeechPrivate]:
    """
    Calls Qt's 'QTextToSpeechPrivate *QTextToSpeech::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeech.html#d_func

    Returns
    -------

    Optional[QTextToSpeechPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextToSpeechPrivate *QTextToSpeech::d_func()
    address = self.uglySide.call('ritual_ZN13QTextToSpeech6d_funcEv')
    from . import QTextToSpeechPrivate
    return QTextToSpeechPrivate._cuteAt(address)

  @overload(str)
  def say(self, text: str) -> None:
    """
    Calls Qt's 'void QTextToSpeech::say(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeech.html#say

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTextToSpeech::say(const QString &text)
    self.uglySide.call('ritual_ZN13QTextToSpeech3sayERK7QString', text)

  @overload(str)
  def enqueue(self, text: str) -> int:
    """
    Calls Qt's 'qsizetype QTextToSpeech::enqueue(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeech.html#enqueue

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  qsizetype QTextToSpeech::enqueue(const QString &text)
    return self.uglySide.call(
        'ritual_ZN13QTextToSpeech7enqueueERK7QString', text,
    )

  @overload()
  @overload(BoundaryHint)
  def stop(self, boundaryHint: BoundaryHint = BoundaryHint.Default) -> None:
    """
    Calls Qt's 'void QTextToSpeech::stop(QTextToSpeech::BoundaryHint
    boundaryHint)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeech.html#stop

    Parameters
    ----------

    boundaryHint : BoundaryHint
      Passed on as its number. May be left out, as in Qt: it is then
      BoundaryHint.Default.
    """
    #  void QTextToSpeech::stop(QTextToSpeech::BoundaryHint boundaryHint)
    self.uglySide.call(
        'ritual_ZN13QTextToSpeech4stopENS_12BoundaryHintE',
        boundaryHint.value,
    )

  @overload()
  @overload(BoundaryHint)
  def pause(self, boundaryHint: BoundaryHint = BoundaryHint.Default) -> None:
    """
    Calls Qt's 'void QTextToSpeech::pause(QTextToSpeech::BoundaryHint
    boundaryHint)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeech.html#pause

    Parameters
    ----------

    boundaryHint : BoundaryHint
      Passed on as its number. May be left out, as in Qt: it is then
      BoundaryHint.Default.
    """
    #  void QTextToSpeech::pause(QTextToSpeech::BoundaryHint boundaryHint)
    self.uglySide.call(
        'ritual_ZN13QTextToSpeech5pauseENS_12BoundaryHintE',
        boundaryHint.value,
    )

  def resume(self) -> None:
    """
    Calls Qt's 'void QTextToSpeech::resume()'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeech.html#resume
    """
    #  void QTextToSpeech::resume()
    self.uglySide.call('ritual_ZN13QTextToSpeech6resumeEv')

  @overload(str)
  def engineChanged(self, engine: str) -> None:
    """
    Calls Qt's 'void QTextToSpeech::engineChanged(const QString &engine)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeech.html#engineChanged

    Parameters
    ----------

    engine : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTextToSpeech::engineChanged(const QString &engine)
    self.uglySide.call(
        'ritual_ZN13QTextToSpeech13engineChangedERK7QString', engine,
    )

  @overload(State)
  def stateChanged(self, state: State) -> None:
    """
    Calls Qt's 'void QTextToSpeech::stateChanged(QTextToSpeech::State
    state)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeech.html#stateChanged

    Parameters
    ----------

    state : State
      Passed on as its number.
    """
    #  void QTextToSpeech::stateChanged(QTextToSpeech::State state)
    self.uglySide.call(
        'ritual_ZN13QTextToSpeech12stateChangedENS_5StateE', state.value,
    )

  @overload(ErrorReason, str)
  def errorOccurred(self, error: ErrorReason, errorString: str) -> None:
    """
    Calls Qt's 'void QTextToSpeech::errorOccurred(QTextToSpeech::ErrorReason
    error, const QString &errorString)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeech.html#errorOccurred

    Parameters
    ----------

    error : ErrorReason
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTextToSpeech::errorOccurred(QTextToSpeech::ErrorReason error,
    #      const QString &errorString)
    self.uglySide.call(
        'ritual_ZN13QTextToSpeech13errorOccurredENS_11ErrorReasonERK7QStrin'
        'g',
        error.value, errorString,
    )

  @overload(QLocale)
  def localeChanged(self, locale: QLocale) -> None:
    """
    Calls Qt's 'void QTextToSpeech::localeChanged(const QLocale &locale)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeech.html#localeChanged

    Parameters
    ----------

    locale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  void QTextToSpeech::localeChanged(const QLocale &locale)
    self.uglySide.call(
        'ritual_ZN13QTextToSpeech13localeChangedERK7QLocale',
        self._valueOf(locale),
    )

  @overload(float)
  def rateChanged(self, rate: float) -> None:
    """
    Calls Qt's 'void QTextToSpeech::rateChanged(double rate)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeech.html#rateChanged

    Parameters
    ----------

    rate : float
      Passed on as it is.
    """
    #  void QTextToSpeech::rateChanged(double rate)
    self.uglySide.call('ritual_ZN13QTextToSpeech11rateChangedEd', rate)

  @overload(float)
  def pitchChanged(self, pitch: float) -> None:
    """
    Calls Qt's 'void QTextToSpeech::pitchChanged(double pitch)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeech.html#pitchChanged

    Parameters
    ----------

    pitch : float
      Passed on as it is.
    """
    #  void QTextToSpeech::pitchChanged(double pitch)
    self.uglySide.call('ritual_ZN13QTextToSpeech12pitchChangedEd', pitch)

  @overload(float)
  def volumeChanged(self, volume: float) -> None:
    """
    Calls Qt's 'void QTextToSpeech::volumeChanged(double volume)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeech.html#volumeChanged

    Parameters
    ----------

    volume : float
      Passed on as it is.
    """
    #  void QTextToSpeech::volumeChanged(double volume)
    self.uglySide.call('ritual_ZN13QTextToSpeech13volumeChangedEd', volume)

  @overload(QVoice)
  def voiceChanged(self, voice: QVoice) -> None:
    """
    Calls Qt's 'void QTextToSpeech::voiceChanged(const QVoice &voice)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeech.html#voiceChanged

    Parameters
    ----------

    voice : QVoice
      Passed on as a value: Qt reads the C++ QVoice, which stays Python's
      own.
    """
    #  void QTextToSpeech::voiceChanged(const QVoice &voice)
    self.uglySide.call(
        'ritual_ZN13QTextToSpeech12voiceChangedERK6QVoice',
        self._valueOf(voice),
    )

  @overload(str, int, int, int)
  def sayingWord(self, word: str, id: int, start: int, length: int) -> None:
    """
    Calls Qt's 'void QTextToSpeech::sayingWord(const QString &word, qsizetype
    id, qsizetype start, qsizetype length)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeech.html#sayingWord

    Parameters
    ----------

    word : str
      Passed on as it is: a QString is made of it for the call.

    id : int
      Passed on as it is.

    start : int
      Passed on as it is.

    length : int
      Passed on as it is.
    """
    #  void QTextToSpeech::sayingWord(const QString &word, qsizetype id,
    #      qsizetype start, qsizetype length)
    self.uglySide.call(
        'ritual_ZN13QTextToSpeech10sayingWordERK7QStringxxx',
        word, id, start, length,
    )

  @overload(int)
  def aboutToSynthesize(self, id: int) -> None:
    """
    Calls Qt's 'void QTextToSpeech::aboutToSynthesize(qsizetype id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttospeech.html#aboutToSynthesize

    Parameters
    ----------

    id : int
      Passed on as it is.
    """
    #  void QTextToSpeech::aboutToSynthesize(qsizetype id)
    self.uglySide.call('ritual_ZN13QTextToSpeech17aboutToSynthesizeEx', id)

  @staticmethod
  def findVoices(*__, **_) -> Never:
    """
    Qt's 'QTextToSpeech::findVoices': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QTextToSpeech.findVoices' has no cute function yet. Qt's "
        "'QTextToSpeech::findVoices': a template: a pattern and no single "
        "function.")

  @staticmethod
  def synthesize(*__, **_) -> Never:
    """
    Qt's 'QTextToSpeech::synthesize': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QTextToSpeech.synthesize' has no cute function yet. Qt's "
        "'QTextToSpeech::synthesize': a template: a pattern and no single "
        "function.")

  @staticmethod
  def synthesizeImpl(*__, **_) -> Never:
    """
    Qt's 'void QTextToSpeech::synthesizeImpl(const QString &text,
    QtPrivate::QSlotObjectBase *slotObj, const QObject *context,
    SynthesizeOverload overload)': names the enum
    'QTextToSpeech::SynthesizeOverload', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QTextToSpeech.synthesizeImpl' has no cute function yet. Qt's "
        "'void QTextToSpeech::synthesizeImpl(const QString &text, "
        "QtPrivate::QSlotObjectBase *slotObj, const QObject *context, "
        "SynthesizeOverload overload)': names the enum "
        "'QTextToSpeech::SynthesizeOverload', whose class cannot be named "
        "here.")

  @staticmethod
  def voiceMatches(*__, **_) -> Never:
    """
    Qt's 'QTextToSpeech::voiceMatches': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QTextToSpeech.voiceMatches' has no cute function yet. Qt's "
        "'QTextToSpeech::voiceMatches': a template: a pattern and no single "
        "function.")
