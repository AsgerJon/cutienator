"""
QPlatformAudioSource binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qaudiosystem_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QPlatformAudioSource to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QPlatformAudioEndpointBase

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QIODevice, QMetaObject
  from . import QAudioDevice, QAudioFormat
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAudioDevice = WAIT['QAudioDevice']
  QAudioFormat = WAIT['QAudioFormat']
  QIODevice = WAIT['QIODevice']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlatformAudioSource(QPlatformAudioEndpointBase):
  """
  The cute side of Qt's QPlatformAudioSource: a plain Python object standing
  in front of one C++ QPlatformAudioSource.

  It is built on the cute 'QPlatformAudioEndpointBase', as Qt's
  QPlatformAudioSource is built on Qt's QPlatformAudioEndpointBase, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QPlatformAudioSource that has a ritual and that
  Python can call so far, 12 names in all: 'metaObject', 'tr', 'start',
  'stop', 'reset', 'suspend', 'resume', 'bytesReady', 'setBufferSize',
  'bufferSize', 'processedUSecs', 'hasCallbackAPI'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPlatformAudioSource::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QPlatformAudioSource::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QPlatformAudioSource::~QPlatformAudioSource()': the destructor:
    Python never removes a C++ QPlatformAudioSource.
  - Qt's 'void QPlatformAudioSource::setNativePeriodFrames(std::
    optional<NativePeriodFrames> a0)': takes a type Python has no way to hand
    over yet.
  - Qt's 'std::optional<NativePeriodFrames>
    QPlatformAudioSource::nativePeriodFrames()': gives a type Python has no
    way to take yet.
  - Qt's 'void QPlatformAudioSource::start(AudioCallback &&a0)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QPlatformAudioSource *QPlatformAudioSource::get(const QAudioSource
    &a0)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 23 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QPlatformAudioSource is created at the first use, not by
    'QPlatformAudioSource(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlatformAudioSource.
  - Qt tells when it has removed the C++ QPlatformAudioSource. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QPlatformAudioSource that has no cute function yet,
    'get', 'nativePeriodFrames', 'setNativePeriodFrames', holds a function
    that raises 'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QPlatformAudioSource::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformaudiosource.html#tr

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
    #  QString QPlatformAudioSource::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN20QPlatformAudioSource2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformAudioSource'

  #  A C++ QPlatformAudioSource Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlatformAudioSource'

  #  The functions Qt calls itself that QPlatformAudioSource is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'setNativePeriodFrames': (
          'void '
          'QPlatformAudioSource::setNativePeriodFrames(std::optional<Native'
          'PeriodFrames>)',
      ),
      'nativePeriodFrames': (
          'std::optional<NativePeriodFrames> '
          'QPlatformAudioSource::nativePeriodFrames()',
      ),
  }

  #  The functions Qt calls itself that QPlatformAudioSource is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'start': (
          ('_ZN20QPlatformAudioSource5startEP9QIODevice',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QIODevice'),
           )),
          ('_ZN20QPlatformAudioSource5startEv',
           ('address', 'address', 'QtCore:QIODevice'),
           ()),
      ),
      'stop': (
          ('_ZN20QPlatformAudioSource4stopEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'reset': (
          ('_ZN20QPlatformAudioSource5resetEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'suspend': (
          ('_ZN20QPlatformAudioSource7suspendEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'resume': (
          ('_ZN20QPlatformAudioSource6resumeEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'bytesReady': (
          ('_ZNK20QPlatformAudioSource10bytesReadyEv',
           ('long long', 'number', ''),
           ()),
      ),
      'setBufferSize': (
          ('_ZN20QPlatformAudioSource13setBufferSizeEx',
           ('nothing', 'nothing', ''),
           (
               ('long long', 'number', ''),
           )),
      ),
      'bufferSize': (
          ('_ZNK20QPlatformAudioSource10bufferSizeEv',
           ('long long', 'number', ''),
           ()),
      ),
      'processedUSecs': (
          ('_ZNK20QPlatformAudioSource14processedUSecsEv',
           ('long long', 'number', ''),
           ()),
      ),
      'hasCallbackAPI': (
          ('_ZN20QPlatformAudioSource14hasCallbackAPIEv',
           ('bool', 'number', ''),
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
    Calls Qt's 'const QMetaObject *QPlatformAudioSource::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudiosource.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPlatformAudioSource::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK20QPlatformAudioSource10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def bytesReady(self) -> int:
    """
    Calls Qt's 'qsizetype QPlatformAudioSource::bytesReady() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudiosource.html#bytesReady
    """
    #  qsizetype QPlatformAudioSource::bytesReady() const
    return self.uglySide.call(
        'ritual_ZNK20QPlatformAudioSource10bytesReadyEv',
    )

  def bufferSize(self) -> int:
    """
    Calls Qt's 'qsizetype QPlatformAudioSource::bufferSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudiosource.html#bufferSize
    """
    #  qsizetype QPlatformAudioSource::bufferSize() const
    return self.uglySide.call(
        'ritual_ZNK20QPlatformAudioSource10bufferSizeEv',
    )

  def processedUSecs(self) -> int:
    """
    Calls Qt's 'qint64 QPlatformAudioSource::processedUSecs() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudiosource.html#processedUSecs
    """
    #  qint64 QPlatformAudioSource::processedUSecs() const
    return self.uglySide.call(
        'ritual_ZNK20QPlatformAudioSource14processedUSecsEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setBufferSize(self, value: int) -> None:
    """
    Calls Qt's 'void QPlatformAudioSource::setBufferSize(qsizetype value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudiosource.html#setBufferSize

    Parameters
    ----------

    value : int
      Passed on as it is.
    """
    #  void QPlatformAudioSource::setBufferSize(qsizetype value)
    self.uglySide.call(
        'ritual_ZN20QPlatformAudioSource13setBufferSizeEx', value,
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

  @overload(QAudioDevice, QAudioFormat, QObject)
  @overload(QAudioDevice, QAudioFormat, NoneType)
  def __init__(
      self,
      a0: QAudioDevice,
      a1: QAudioFormat,
      parent: Optional[QObject],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QPlatformAudioSource::QPlatformAudioSource(QAudioDevice a0, const
    QAudioFormat &a1, QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudiosource.html#QPlatformAudioSource

    Parameters
    ----------

    a0 : QAudioDevice
      Passed on as a value: Qt reads the C++ QAudioDevice, which stays
      Python's own.

    a1 : QAudioFormat
      Passed on as a value: Qt reads the C++ QAudioFormat, which stays
      Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QPlatformAudioSource::QPlatformAudioSource(QAudioDevice a0, const
    #      QAudioFormat &a1, QObject *parent)
    self._noteCreation(QPlatformAudioSource, lambda: Rituals.call(
        'ritual_ZN20QPlatformAudioSourceC1E12QAudioDeviceRK12QAudioFormatP7'
        'QObject',
        self._valueOf(a0), self._valueOf(a1), self._addressOf(parent,
        'QObject'),
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

  @overload(QIODevice)
  @overload(NoneType)
  def start(self, device: Optional[QIODevice]) -> None:
    """
    Calls Qt's 'void QPlatformAudioSource::start(QIODevice *device)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformaudiosource.html#start

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlatformAudioSource::start(QIODevice *device)
    self.uglySide.call(
        'ritual_ZN20QPlatformAudioSource5startEP9QIODevice',
        self._addressOf(device),
    )

  @overload()
  def start(self) -> Optional[QIODevice]:
    """
    Calls Qt's 'QIODevice *QPlatformAudioSource::start()'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformaudiosource.html#start

    Returns
    -------

    Optional[QIODevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIODevice *QPlatformAudioSource::start()
    address = self.uglySide.call('ritual_ZN20QPlatformAudioSource5startEv')
    from ..QtCore import QIODevice
    return QIODevice._cuteAt(address)

  def stop(self) -> None:
    """
    Calls Qt's 'void QPlatformAudioSource::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformaudiosource.html#stop
    """
    #  void QPlatformAudioSource::stop()
    self.uglySide.call('ritual_ZN20QPlatformAudioSource4stopEv')

  def reset(self) -> None:
    """
    Calls Qt's 'void QPlatformAudioSource::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformaudiosource.html#reset
    """
    #  void QPlatformAudioSource::reset()
    self.uglySide.call('ritual_ZN20QPlatformAudioSource5resetEv')

  def suspend(self) -> None:
    """
    Calls Qt's 'void QPlatformAudioSource::suspend()'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformaudiosource.html#suspend
    """
    #  void QPlatformAudioSource::suspend()
    self.uglySide.call('ritual_ZN20QPlatformAudioSource7suspendEv')

  def resume(self) -> None:
    """
    Calls Qt's 'void QPlatformAudioSource::resume()'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformaudiosource.html#resume
    """
    #  void QPlatformAudioSource::resume()
    self.uglySide.call('ritual_ZN20QPlatformAudioSource6resumeEv')

  def hasCallbackAPI(self) -> bool:
    """
    Calls Qt's 'bool QPlatformAudioSource::hasCallbackAPI()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudiosource.html#hasCallbackAPI
    """
    #  bool QPlatformAudioSource::hasCallbackAPI()
    ritual = 'ritual_ZN20QPlatformAudioSource14hasCallbackAPIEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN20QPlatformAudioSource14hasCallbackAPIEv'
    return self.uglySide.call(ritual)

  @staticmethod
  def get(*__, **_) -> Never:
    """
    Qt's 'QPlatformAudioSource *QPlatformAudioSource::get(const QAudioSource
    &a0)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPlatformAudioSource.get' has no cute function yet. Qt's "
        "'QPlatformAudioSource *QPlatformAudioSource::get(const "
        "QAudioSource &a0)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def nativePeriodFrames(*__, **_) -> Never:
    """
    Qt's 'std::optional<NativePeriodFrames>
    QPlatformAudioSource::nativePeriodFrames()': gives a type Python has no
    way to take yet.
    """
    raise NotImplementedError(
        "'QPlatformAudioSource.nativePeriodFrames' has no cute function "
        "yet. Qt's 'std::optional<NativePeriodFrames> "
        "QPlatformAudioSource::nativePeriodFrames()': gives a type Python "
        "has no way to take yet.")

  @staticmethod
  def setNativePeriodFrames(*__, **_) -> Never:
    """
    Qt's 'void QPlatformAudioSource::setNativePeriodFrames(std::
    optional<NativePeriodFrames> a0)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QPlatformAudioSource.setNativePeriodFrames' has no cute function "
        "yet. Qt's 'void "
        "QPlatformAudioSource::setNativePeriodFrames(std::optional<NativePer"
        "iodFrames> a0)': takes a type Python has no way to hand over yet.")
