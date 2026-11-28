"""
QTextToSpeechEngine binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtTextToSpeech/qtexttospeechengine.h, Qt 6.12.0. Changes made here are
#  lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QTextToSpeech, QVoice

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QLocale, QMetaObject, QVariant
  from ..QtMultimedia import QAudioFormat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAudioFormat = WAIT['QAudioFormat']
  QByteArray = WAIT['QByteArray']
  QLocale = WAIT['QLocale']
  QVariant = WAIT['QVariant']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTextToSpeechEngine(QObject):
  """
  The cute side of Qt's QTextToSpeechEngine: a plain Python object standing
  in front of one C++ QTextToSpeechEngine.

  It is built on the cute 'QObject', as Qt's QTextToSpeechEngine is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QTextToSpeechEngine that has a ritual and that
  Python can call so far, 29 names in all: 'metaObject', 'tr',
  'capabilities', 'availableLocales', 'availableVoices', 'say', 'synthesize',
  'stop', 'pause', 'resume', 'rate', 'setRate', 'pitch', 'setPitch',
  'locale', 'setLocale', 'volume', 'setVolume', 'voice', 'setVoice', 'state',
  'errorReason', 'errorString', 'createVoice', 'voiceData', 'stateChanged',
  'errorOccurred', 'sayingWord', 'synthesized'. None can be made from Python:
  one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QTextToSpeechEngine::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QTextToSpeechEngine::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QTextToSpeechEngine::~QTextToSpeechEngine()': the destructor:
    Python never removes a C++ QTextToSpeechEngine.

  What has no ritual
  ------------------

  3 of the 35 functions Qt declares: 2 not a gap; 1 the class is abstract, so
  C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open.

  What to expect
  --------------

  - The C++ QTextToSpeechEngine is created at the first use, not by
    'QTextToSpeechEngine(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTextToSpeechEngine.
  - Qt tells when it has removed the C++ QTextToSpeechEngine. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QTextToSpeechEngine that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

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
    Calls Qt's 'QString QTextToSpeechEngine::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeechengine.html#tr

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
    #  QString QTextToSpeechEngine::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QTextToSpeechEngine2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  @overload(str, QLocale, QVoice.Gender, QVoice.Age, QVariant)
  def createVoice(
      name: str,
      locale: QLocale,
      gender: QVoice.Gender,
      age: QVoice.Age,
      data: QVariant,
  ) -> QVoice:
    """
    Calls Qt's 'QVoice QTextToSpeechEngine::createVoice(const QString &name,
    const QLocale &locale, QVoice::Gender gender, QVoice::Age age, const
    QVariant &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttospeechengine.html#createVoice

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    locale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.

    gender : QVoice.Gender
      Passed on as its number.

    age : QVoice.Age
      Passed on as its number.

    data : QVariant
      Passed on as a value: Qt reads the C++ QVariant, which stays Python's
      own.

    Returns
    -------

    QVoice
      A new cute QVoice around the copy Qt gave back. Python owns it.
    """
    #  QVoice QTextToSpeechEngine::createVoice(const QString &name, const
    #      QLocale &locale, QVoice::Gender gender, QVoice::Age age, const
    #      QVariant &data)
    address = Rituals.call(
        'ritual_ZN19QTextToSpeechEngine11createVoiceERK7QStringRK7QLocaleN6'
        'QVoice6GenderENS6_3AgeERK8QVariant',
        name, CuteMixin._valueOf(locale), gender.value, age.value,
        CuteMixin._valueOf(data),
    )
    return QVoice._cuteOwning(address)

  @staticmethod
  @overload(QVoice)
  def voiceData(voice: QVoice) -> QVariant:
    """
    Calls Qt's 'QVariant QTextToSpeechEngine::voiceData(const QVoice
    &voice)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeechengine.html#voiceData

    Parameters
    ----------

    voice : QVoice
      Passed on as a value: Qt reads the C++ QVoice, which stays Python's
      own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QTextToSpeechEngine::voiceData(const QVoice &voice)
    address = Rituals.call(
        'ritual_ZN19QTextToSpeechEngine9voiceDataERK6QVoice',
        CuteMixin._valueOf(voice),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextToSpeechEngine'

  #  A C++ QTextToSpeechEngine Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTextToSpeechEngine'

  #  The functions Qt calls itself that QTextToSpeechEngine is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'availableLocales': (
          'QList<QLocale> QTextToSpeechEngine::availableLocales() const',
      ),
      'availableVoices': (
          'QList<QVoice> QTextToSpeechEngine::availableVoices() const',
      ),
  }

  #  The functions Qt calls itself that QTextToSpeechEngine is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'capabilities': (
          ('_ZNK19QTextToSpeechEngine12capabilitiesEv',
           ('int', 'flags', 'QtTextToSpeech:QTextToSpeech.Capability'),
           ()),
      ),
      'say': (
          ('_ZN19QTextToSpeechEngine3sayERK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'synthesize': (
          ('_ZN19QTextToSpeechEngine10synthesizeERK7QString',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'stop': (
          ('_ZN19QTextToSpeechEngine4stopEN13QTextToSpeech12BoundaryHintE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtTextToSpeech:QTextToSpeech.BoundaryHint'),
           )),
      ),
      'pause': (
          ('_ZN19QTextToSpeechEngine5pauseEN13QTextToSpeech12BoundaryHintE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtTextToSpeech:QTextToSpeech.BoundaryHint'),
           )),
      ),
      'resume': (
          ('_ZN19QTextToSpeechEngine6resumeEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'rate': (
          ('_ZNK19QTextToSpeechEngine4rateEv',
           ('double', 'number', ''),
           ()),
      ),
      'setRate': (
          ('_ZN19QTextToSpeechEngine7setRateEd',
           ('bool', 'number', ''),
           (
               ('double', 'number', ''),
           )),
      ),
      'pitch': (
          ('_ZNK19QTextToSpeechEngine5pitchEv',
           ('double', 'number', ''),
           ()),
      ),
      'setPitch': (
          ('_ZN19QTextToSpeechEngine8setPitchEd',
           ('bool', 'number', ''),
           (
               ('double', 'number', ''),
           )),
      ),
      'locale': (
          ('_ZNK19QTextToSpeechEngine6localeEv',
           ('address', 'value', 'QtCore:QLocale'),
           ()),
      ),
      'setLocale': (
          ('_ZN19QTextToSpeechEngine9setLocaleERK7QLocale',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtCore:QLocale'),
           )),
      ),
      'volume': (
          ('_ZNK19QTextToSpeechEngine6volumeEv',
           ('double', 'number', ''),
           ()),
      ),
      'setVolume': (
          ('_ZN19QTextToSpeechEngine9setVolumeEd',
           ('bool', 'number', ''),
           (
               ('double', 'number', ''),
           )),
      ),
      'voice': (
          ('_ZNK19QTextToSpeechEngine5voiceEv',
           ('address', 'value', 'QtTextToSpeech:QVoice'),
           ()),
      ),
      'setVoice': (
          ('_ZN19QTextToSpeechEngine8setVoiceERK6QVoice',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtTextToSpeech:QVoice'),
           )),
      ),
      'state': (
          ('_ZNK19QTextToSpeechEngine5stateEv',
           ('int', 'enum', 'QtTextToSpeech:QTextToSpeech.State'),
           ()),
      ),
      'errorReason': (
          ('_ZNK19QTextToSpeechEngine11errorReasonEv',
           ('int', 'enum', 'QtTextToSpeech:QTextToSpeech.ErrorReason'),
           ()),
      ),
      'errorString': (
          ('_ZNK19QTextToSpeechEngine11errorStringEv',
           ('address', 'text', ''),
           ()),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QTextToSpeechEngine::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttospeechengine.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QTextToSpeechEngine::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QTextToSpeechEngine10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def capabilities(self) -> QTextToSpeech.Capabilities:
    """
    Calls Qt's 'QTextToSpeech::Capabilities
    QTextToSpeechEngine::capabilities() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttospeechengine.html#capabilities

    Returns
    -------

    QTextToSpeech.Capabilities
      The value standing for the combination Qt gave back.
    """
    #  QTextToSpeech::Capabilities QTextToSpeechEngine::capabilities() const
    ritual = 'ritual_ZNK19QTextToSpeechEngine12capabilitiesEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QTextToSpeechEngine12capabilitiesEv'
    return QTextToSpeech.Capabilities(self.uglySide.call(ritual))

  def availableLocales(self) -> QList[QLocale]:
    """
    Calls Qt's 'QList<QLocale> QTextToSpeechEngine::availableLocales()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttospeechengine.html#availableLocales

    Returns
    -------

    QList[QLocale]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QLocale> QTextToSpeechEngine::availableLocales() const
    address = self.uglySide.call(
        'ritual_ZNK19QTextToSpeechEngine16availableLocalesEv',
    )
    from ..QtCore import QLocale
    return QList[QLocale]._cuteOwning(address)

  def availableVoices(self) -> QList[QVoice]:
    """
    Calls Qt's 'QList<QVoice> QTextToSpeechEngine::availableVoices() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttospeechengine.html#availableVoices

    Returns
    -------

    QList[QVoice]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QVoice> QTextToSpeechEngine::availableVoices() const
    address = self.uglySide.call(
        'ritual_ZNK19QTextToSpeechEngine15availableVoicesEv',
    )
    return QList[QVoice]._cuteOwning(address)

  def rate(self) -> float:
    """
    Calls Qt's 'double QTextToSpeechEngine::rate() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeechengine.html#rate
    """
    #  double QTextToSpeechEngine::rate() const
    return self.uglySide.call('ritual_ZNK19QTextToSpeechEngine4rateEv')

  def pitch(self) -> float:
    """
    Calls Qt's 'double QTextToSpeechEngine::pitch() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeechengine.html#pitch
    """
    #  double QTextToSpeechEngine::pitch() const
    return self.uglySide.call('ritual_ZNK19QTextToSpeechEngine5pitchEv')

  def locale(self) -> QLocale:
    """
    Calls Qt's 'QLocale QTextToSpeechEngine::locale() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeechengine.html#locale

    Returns
    -------

    QLocale
      A new cute QLocale around the copy Qt gave back. Python owns it.
    """
    #  QLocale QTextToSpeechEngine::locale() const
    address = self.uglySide.call('ritual_ZNK19QTextToSpeechEngine6localeEv')
    from ..QtCore import QLocale
    return QLocale._cuteOwning(address)

  def volume(self) -> float:
    """
    Calls Qt's 'double QTextToSpeechEngine::volume() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeechengine.html#volume
    """
    #  double QTextToSpeechEngine::volume() const
    return self.uglySide.call('ritual_ZNK19QTextToSpeechEngine6volumeEv')

  def voice(self) -> QVoice:
    """
    Calls Qt's 'QVoice QTextToSpeechEngine::voice() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeechengine.html#voice

    Returns
    -------

    QVoice
      A new cute QVoice around the copy Qt gave back. Python owns it.
    """
    #  QVoice QTextToSpeechEngine::voice() const
    address = self.uglySide.call('ritual_ZNK19QTextToSpeechEngine5voiceEv')
    return QVoice._cuteOwning(address)

  def state(self) -> QTextToSpeech.State:
    """
    Calls Qt's 'QTextToSpeech::State QTextToSpeechEngine::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeechengine.html#state

    Returns
    -------

    QTextToSpeech.State
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QTextToSpeech.State(number)' gives.
    """
    #  QTextToSpeech::State QTextToSpeechEngine::state() const
    return QTextToSpeech.State(self.uglySide.call(
        'ritual_ZNK19QTextToSpeechEngine5stateEv',
    ))

  def errorReason(self) -> QTextToSpeech.ErrorReason:
    """
    Calls Qt's 'QTextToSpeech::ErrorReason QTextToSpeechEngine::errorReason()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttospeechengine.html#errorReason

    Returns
    -------

    QTextToSpeech.ErrorReason
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QTextToSpeech.ErrorReason(number)' gives.
    """
    #  QTextToSpeech::ErrorReason QTextToSpeechEngine::errorReason() const
    return QTextToSpeech.ErrorReason(self.uglySide.call(
        'ritual_ZNK19QTextToSpeechEngine11errorReasonEv',
    ))

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QTextToSpeechEngine::errorString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttospeechengine.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextToSpeechEngine::errorString() const
    return self.uglySide.call(
        'ritual_ZNK19QTextToSpeechEngine11errorStringEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(float)
  def setRate(self, rate: float) -> bool:
    """
    Calls Qt's 'bool QTextToSpeechEngine::setRate(double rate)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeechengine.html#setRate

    Parameters
    ----------

    rate : float
      Passed on as it is.
    """
    #  bool QTextToSpeechEngine::setRate(double rate)
    return self.uglySide.call(
        'ritual_ZN19QTextToSpeechEngine7setRateEd', rate,
    )

  @overload(float)
  def setPitch(self, pitch: float) -> bool:
    """
    Calls Qt's 'bool QTextToSpeechEngine::setPitch(double pitch)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeechengine.html#setPitch

    Parameters
    ----------

    pitch : float
      Passed on as it is.
    """
    #  bool QTextToSpeechEngine::setPitch(double pitch)
    return self.uglySide.call(
        'ritual_ZN19QTextToSpeechEngine8setPitchEd', pitch,
    )

  @overload(QLocale)
  def setLocale(self, locale: QLocale) -> bool:
    """
    Calls Qt's 'bool QTextToSpeechEngine::setLocale(const QLocale &locale)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeechengine.html#setLocale

    Parameters
    ----------

    locale : QLocale
      Passed on as a value: Qt reads the C++ QLocale, which stays Python's
      own.
    """
    #  bool QTextToSpeechEngine::setLocale(const QLocale &locale)
    return self.uglySide.call(
        'ritual_ZN19QTextToSpeechEngine9setLocaleERK7QLocale',
        self._valueOf(locale),
    )

  @overload(float)
  def setVolume(self, volume: float) -> bool:
    """
    Calls Qt's 'bool QTextToSpeechEngine::setVolume(double volume)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeechengine.html#setVolume

    Parameters
    ----------

    volume : float
      Passed on as it is.
    """
    #  bool QTextToSpeechEngine::setVolume(double volume)
    return self.uglySide.call(
        'ritual_ZN19QTextToSpeechEngine9setVolumeEd', volume,
    )

  @overload(QVoice)
  def setVoice(self, voice: QVoice) -> bool:
    """
    Calls Qt's 'bool QTextToSpeechEngine::setVoice(const QVoice &voice)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeechengine.html#setVoice

    Parameters
    ----------

    voice : QVoice
      Passed on as a value: Qt reads the C++ QVoice, which stays Python's
      own.
    """
    #  bool QTextToSpeechEngine::setVoice(const QVoice &voice)
    return self.uglySide.call(
        'ritual_ZN19QTextToSpeechEngine8setVoiceERK6QVoice',
        self._valueOf(voice),
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
    Qt's 'QTextToSpeechEngine::QTextToSpeechEngine(QObject *parent)': the
    class is abstract, so C++ cannot make one, and the C++ class of ours does
    not fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QTextToSpeechEngine.__init__' has no cute function yet. Qt's "
        "'QTextToSpeechEngine::QTextToSpeechEngine(QObject *parent)': the "
        "class is abstract, so C++ cannot make one, and the C++ class of "
        "ours does not fill in every function it leaves open.")

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

  @overload(str)
  def say(self, text: str) -> None:
    """
    Calls Qt's 'void QTextToSpeechEngine::say(const QString &text)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeechengine.html#say

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTextToSpeechEngine::say(const QString &text)
    self.uglySide.call('ritual_ZN19QTextToSpeechEngine3sayERK7QString', text)

  @overload(str)
  def synthesize(self, text: str) -> None:
    """
    Calls Qt's 'void QTextToSpeechEngine::synthesize(const QString &text)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttospeechengine.html#synthesize

    Parameters
    ----------

    text : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTextToSpeechEngine::synthesize(const QString &text)
    self.uglySide.call(
        'ritual_ZN19QTextToSpeechEngine10synthesizeERK7QString', text,
    )

  @overload(QTextToSpeech.BoundaryHint)
  def stop(self, boundaryHint: QTextToSpeech.BoundaryHint) -> None:
    """
    Calls Qt's 'void QTextToSpeechEngine::stop(QTextToSpeech::BoundaryHint
    boundaryHint)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeechengine.html#stop

    Parameters
    ----------

    boundaryHint : QTextToSpeech.BoundaryHint
      Passed on as its number.
    """
    #  void QTextToSpeechEngine::stop(QTextToSpeech::BoundaryHint
    #      boundaryHint)
    self.uglySide.call(
        'ritual_ZN19QTextToSpeechEngine4stopEN13QTextToSpeech12BoundaryHint'
        'E',
        boundaryHint.value,
    )

  @overload(QTextToSpeech.BoundaryHint)
  def pause(self, boundaryHint: QTextToSpeech.BoundaryHint) -> None:
    """
    Calls Qt's 'void QTextToSpeechEngine::pause(QTextToSpeech::BoundaryHint
    boundaryHint)'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeechengine.html#pause

    Parameters
    ----------

    boundaryHint : QTextToSpeech.BoundaryHint
      Passed on as its number.
    """
    #  void QTextToSpeechEngine::pause(QTextToSpeech::BoundaryHint
    #      boundaryHint)
    self.uglySide.call(
        'ritual_ZN19QTextToSpeechEngine5pauseEN13QTextToSpeech12BoundaryHin'
        'tE',
        boundaryHint.value,
    )

  def resume(self) -> None:
    """
    Calls Qt's 'void QTextToSpeechEngine::resume()'.

    Qt's own words: https://doc.qt.io/qt-6/qtexttospeechengine.html#resume
    """
    #  void QTextToSpeechEngine::resume()
    self.uglySide.call('ritual_ZN19QTextToSpeechEngine6resumeEv')

  @overload(QTextToSpeech.State)
  def stateChanged(self, state: QTextToSpeech.State) -> None:
    """
    Calls Qt's 'void QTextToSpeechEngine::stateChanged(QTextToSpeech::State
    state)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttospeechengine.html#stateChanged

    Parameters
    ----------

    state : QTextToSpeech.State
      Passed on as its number.
    """
    #  void QTextToSpeechEngine::stateChanged(QTextToSpeech::State state)
    self.uglySide.call(
        'ritual_ZN19QTextToSpeechEngine12stateChangedEN13QTextToSpeech5Stat'
        'eE',
        state.value,
    )

  @overload(QTextToSpeech.ErrorReason, str)
  def errorOccurred(
      self,
      error: QTextToSpeech.ErrorReason,
      errorString: str,
  ) -> None:
    """
    Calls Qt's 'void
    QTextToSpeechEngine::errorOccurred(QTextToSpeech::ErrorReason error,
    const QString &errorString)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttospeechengine.html#errorOccurred

    Parameters
    ----------

    error : QTextToSpeech.ErrorReason
      Passed on as its number.

    errorString : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QTextToSpeechEngine::errorOccurred(QTextToSpeech::ErrorReason
    #      error, const QString &errorString)
    self.uglySide.call(
        'ritual_ZN19QTextToSpeechEngine13errorOccurredEN13QTextToSpeech11Er'
        'rorReasonERK7QString',
        error.value, errorString,
    )

  @overload(str, int, int)
  def sayingWord(self, word: str, start: int, length: int) -> None:
    """
    Calls Qt's 'void QTextToSpeechEngine::sayingWord(const QString &word,
    qsizetype start, qsizetype length)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttospeechengine.html#sayingWord

    Parameters
    ----------

    word : str
      Passed on as it is: a QString is made of it for the call.

    start : int
      Passed on as it is.

    length : int
      Passed on as it is.
    """
    #  void QTextToSpeechEngine::sayingWord(const QString &word, qsizetype
    #      start, qsizetype length)
    self.uglySide.call(
        'ritual_ZN19QTextToSpeechEngine10sayingWordERK7QStringxx',
        word, start, length,
    )

  @overload(QAudioFormat, QByteArray)
  def synthesized(self, format: QAudioFormat, data: QByteArray) -> None:
    """
    Calls Qt's 'void QTextToSpeechEngine::synthesized(const QAudioFormat
    &format, const QByteArray &data)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtexttospeechengine.html#synthesized

    Parameters
    ----------

    format : QAudioFormat
      Passed on as a value: Qt reads the C++ QAudioFormat, which stays
      Python's own.

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.
    """
    #  void QTextToSpeechEngine::synthesized(const QAudioFormat &format,
    #      const QByteArray &data)
    self.uglySide.call(
        'ritual_ZN19QTextToSpeechEngine11synthesizedERK12QAudioFormatRK10QB'
        'yteArray',
        self._valueOf(format), self._valueOf(data),
    )
