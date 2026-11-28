"""
QPlatformAudioSink binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qaudiosystem_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QPlatformAudioSink to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QtMultimediaPrivate, QPlatformAudioEndpointBase

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


class QPlatformAudioSink(QPlatformAudioEndpointBase):
  """
  The cute side of Qt's QPlatformAudioSink: a plain Python object standing in
  front of one C++ QPlatformAudioSink.

  It is built on the cute 'QPlatformAudioEndpointBase', as Qt's
  QPlatformAudioSink is built on Qt's QPlatformAudioEndpointBase, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QPlatformAudioSink that has a ritual and that Python
  can call so far, 13 names in all: 'metaObject', 'tr', 'start', 'stop',
  'reset', 'suspend', 'resume', 'bytesFree', 'setBufferSize', 'bufferSize',
  'processedUSecs', 'hasCallbackAPI', 'setRole'. It can be made from Python,
  in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPlatformAudioSink::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QPlatformAudioSink::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QPlatformAudioSink::~QPlatformAudioSink()': the destructor: Python
    never removes a C++ QPlatformAudioSink.
  - Qt's 'void QPlatformAudioSink::setNativePeriodFrames(std::
    optional<NativePeriodFrames> a0)': takes a type Python has no way to hand
    over yet.
  - Qt's 'std::optional<NativePeriodFrames>
    QPlatformAudioSink::nativePeriodFrames()': gives a type Python has no way
    to take yet.
  - Qt's 'void QPlatformAudioSink::start(AudioCallback &&a0)': takes a type
    Python has no way to hand over yet.
  - Qt's 'QPlatformAudioSink *QPlatformAudioSink::get(const QAudioSink &a0)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 24 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QPlatformAudioSink is created at the first use, not by
    'QPlatformAudioSink(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlatformAudioSink.
  - Qt tells when it has removed the C++ QPlatformAudioSink. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QPlatformAudioSink that has no cute function yet,
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
    Calls Qt's 'QString QPlatformAudioSink::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformaudiosink.html#tr

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
    #  QString QPlatformAudioSink::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN18QPlatformAudioSink2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformAudioSink'

  #  A C++ QPlatformAudioSink Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlatformAudioSink'

  #  The functions Qt calls itself that QPlatformAudioSink is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'setNativePeriodFrames': (
          'void '
          'QPlatformAudioSink::setNativePeriodFrames(std::optional<NativePe'
          'riodFrames>)',
      ),
      'nativePeriodFrames': (
          'std::optional<NativePeriodFrames> '
          'QPlatformAudioSink::nativePeriodFrames()',
      ),
  }

  #  The functions Qt calls itself that QPlatformAudioSink is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'start': (
          ('_ZN18QPlatformAudioSink5startEP9QIODevice',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore:QIODevice'),
           )),
          ('_ZN18QPlatformAudioSink5startEv',
           ('address', 'address', 'QtCore:QIODevice'),
           ()),
      ),
      'stop': (
          ('_ZN18QPlatformAudioSink4stopEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'reset': (
          ('_ZN18QPlatformAudioSink5resetEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'suspend': (
          ('_ZN18QPlatformAudioSink7suspendEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'resume': (
          ('_ZN18QPlatformAudioSink6resumeEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'bytesFree': (
          ('_ZNK18QPlatformAudioSink9bytesFreeEv',
           ('long long', 'number', ''),
           ()),
      ),
      'setBufferSize': (
          ('_ZN18QPlatformAudioSink13setBufferSizeEx',
           ('nothing', 'nothing', ''),
           (
               ('long long', 'number', ''),
           )),
      ),
      'bufferSize': (
          ('_ZNK18QPlatformAudioSink10bufferSizeEv',
           ('long long', 'number', ''),
           ()),
      ),
      'processedUSecs': (
          ('_ZNK18QPlatformAudioSink14processedUSecsEv',
           ('long long', 'number', ''),
           ()),
      ),
      'hasCallbackAPI': (
          ('_ZN18QPlatformAudioSink14hasCallbackAPIEv',
           ('bool', 'number', ''),
           ()),
      ),
      'setRole': (
          ('_ZN18QPlatformAudioSink7setRoleEN19QtMultimediaPrivate17AudioEn'
           'dpointRoleE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum',
                'QtMultimedia:QPlatformAudioSink.AudioEndpointRole'),
           )),
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
    Calls Qt's 'const QMetaObject *QPlatformAudioSink::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformaudiosink.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPlatformAudioSink::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK18QPlatformAudioSink10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def bytesFree(self) -> int:
    """
    Calls Qt's 'qsizetype QPlatformAudioSink::bytesFree() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformaudiosink.html#bytesFree
    """
    #  qsizetype QPlatformAudioSink::bytesFree() const
    return self.uglySide.call('ritual_ZNK18QPlatformAudioSink9bytesFreeEv')

  def bufferSize(self) -> int:
    """
    Calls Qt's 'qsizetype QPlatformAudioSink::bufferSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformaudiosink.html#bufferSize
    """
    #  qsizetype QPlatformAudioSink::bufferSize() const
    return self.uglySide.call('ritual_ZNK18QPlatformAudioSink10bufferSizeEv')

  def processedUSecs(self) -> int:
    """
    Calls Qt's 'qint64 QPlatformAudioSink::processedUSecs() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudiosink.html#processedUSecs
    """
    #  qint64 QPlatformAudioSink::processedUSecs() const
    return self.uglySide.call(
        'ritual_ZNK18QPlatformAudioSink14processedUSecsEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setBufferSize(self, value: int) -> None:
    """
    Calls Qt's 'void QPlatformAudioSink::setBufferSize(qsizetype value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudiosink.html#setBufferSize

    Parameters
    ----------

    value : int
      Passed on as it is.
    """
    #  void QPlatformAudioSink::setBufferSize(qsizetype value)
    self.uglySide.call(
        'ritual_ZN18QPlatformAudioSink13setBufferSizeEx', value,
    )

  @overload(QtMultimediaPrivate.AudioEndpointRole)
  def setRole(self, a0: QtMultimediaPrivate.AudioEndpointRole) -> None:
    """
    Calls Qt's 'void QPlatformAudioSink::setRole(AudioEndpointRole a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformaudiosink.html#setRole

    Parameters
    ----------

    a0 : QtMultimediaPrivate.AudioEndpointRole
      Passed on as its number.
    """
    #  void QPlatformAudioSink::setRole(AudioEndpointRole a0)
    ritual = (
        'ritual_ZN18QPlatformAudioSink7setRoleEN19QtMultimediaPrivate17Audi'
        'oEndpointRoleE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN18QPlatformAudioSink7setRoleEN19QtMultimediaPrivate'
          '17AudioEndpointRoleE')
    self.uglySide.call(ritual, a0.value)

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
    'QPlatformAudioSink::QPlatformAudioSink(QAudioDevice a0, const
    QAudioFormat &a1, QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudiosink.html#QPlatformAudioSink

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
    #  QPlatformAudioSink::QPlatformAudioSink(QAudioDevice a0, const
    #      QAudioFormat &a1, QObject *parent)
    self._noteCreation(QPlatformAudioSink, lambda: Rituals.call(
        'ritual_ZN18QPlatformAudioSinkC1E12QAudioDeviceRK12QAudioFormatP7QO'
        'bject',
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
    Calls Qt's 'void QPlatformAudioSink::start(QIODevice *device)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformaudiosink.html#start

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QPlatformAudioSink::start(QIODevice *device)
    self.uglySide.call(
        'ritual_ZN18QPlatformAudioSink5startEP9QIODevice',
        self._addressOf(device),
    )

  @overload()
  def start(self) -> Optional[QIODevice]:
    """
    Calls Qt's 'QIODevice *QPlatformAudioSink::start()'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformaudiosink.html#start

    Returns
    -------

    Optional[QIODevice]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QIODevice *QPlatformAudioSink::start()
    address = self.uglySide.call('ritual_ZN18QPlatformAudioSink5startEv')
    from ..QtCore import QIODevice
    return QIODevice._cuteAt(address)

  def stop(self) -> None:
    """
    Calls Qt's 'void QPlatformAudioSink::stop()'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformaudiosink.html#stop
    """
    #  void QPlatformAudioSink::stop()
    self.uglySide.call('ritual_ZN18QPlatformAudioSink4stopEv')

  def reset(self) -> None:
    """
    Calls Qt's 'void QPlatformAudioSink::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformaudiosink.html#reset
    """
    #  void QPlatformAudioSink::reset()
    self.uglySide.call('ritual_ZN18QPlatformAudioSink5resetEv')

  def suspend(self) -> None:
    """
    Calls Qt's 'void QPlatformAudioSink::suspend()'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformaudiosink.html#suspend
    """
    #  void QPlatformAudioSink::suspend()
    self.uglySide.call('ritual_ZN18QPlatformAudioSink7suspendEv')

  def resume(self) -> None:
    """
    Calls Qt's 'void QPlatformAudioSink::resume()'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformaudiosink.html#resume
    """
    #  void QPlatformAudioSink::resume()
    self.uglySide.call('ritual_ZN18QPlatformAudioSink6resumeEv')

  def hasCallbackAPI(self) -> bool:
    """
    Calls Qt's 'bool QPlatformAudioSink::hasCallbackAPI()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudiosink.html#hasCallbackAPI
    """
    #  bool QPlatformAudioSink::hasCallbackAPI()
    ritual = 'ritual_ZN18QPlatformAudioSink14hasCallbackAPIEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN18QPlatformAudioSink14hasCallbackAPIEv'
    return self.uglySide.call(ritual)

  @staticmethod
  def get(*__, **_) -> Never:
    """
    Qt's 'QPlatformAudioSink *QPlatformAudioSink::get(const QAudioSink &a0)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPlatformAudioSink.get' has no cute function yet. Qt's "
        "'QPlatformAudioSink *QPlatformAudioSink::get(const QAudioSink "
        "&a0)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def nativePeriodFrames(*__, **_) -> Never:
    """
    Qt's 'std::optional<NativePeriodFrames>
    QPlatformAudioSink::nativePeriodFrames()': gives a type Python has no way
    to take yet.
    """
    raise NotImplementedError(
        "'QPlatformAudioSink.nativePeriodFrames' has no cute function yet. "
        "Qt's 'std::optional<NativePeriodFrames> "
        "QPlatformAudioSink::nativePeriodFrames()': gives a type Python has "
        "no way to take yet.")

  @staticmethod
  def setNativePeriodFrames(*__, **_) -> Never:
    """
    Qt's 'void QPlatformAudioSink::setNativePeriodFrames(std::
    optional<NativePeriodFrames> a0)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QPlatformAudioSink.setNativePeriodFrames' has no cute function "
        "yet. Qt's 'void "
        "QPlatformAudioSink::setNativePeriodFrames(std::optional<NativePerio"
        "dFrames> a0)': takes a type Python has no way to hand over yet.")
