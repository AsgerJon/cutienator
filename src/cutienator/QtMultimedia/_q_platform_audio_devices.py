"""
QPlatformAudioDevices binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qplatformaudiodevices_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QPlatformAudioDevices to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QLatin1String, QMetaObject
  from . import QAudioDevice, QAudioFormat, QPlatformAudioSink
  from . import QPlatformAudioSource
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAudioDevice = WAIT['QAudioDevice']
  QAudioFormat = WAIT['QAudioFormat']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QPlatformAudioDevices(QObject):
  """
  The cute side of Qt's QPlatformAudioDevices: a plain Python object standing
  in front of one C++ QPlatformAudioDevices.

  It is built on the cute 'QObject', as Qt's QPlatformAudioDevices is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPlatformAudioDevices that has a ritual and that
  Python can call so far, 16 names in all: 'metaObject', 'tr', 'audioInputs',
  'audioOutputs', 'createAudioSource', 'createAudioSink', 'audioInputDevice',
  'audioOutputDevice', 'backendName', 'hasCallbackApi', 'findAudioInputs',
  'findAudioOutputs', 'onAudioInputsChanged', 'onAudioOutputsChanged',
  'updateAudioInputsCache', 'updateAudioOutputsCache'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QPlatformAudioDevices::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QPlatformAudioDevices::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QPlatformAudioDevices::~QPlatformAudioDevices()': the destructor:
    Python never removes a C++ QPlatformAudioDevices.
  - Qt's 'std::unique_ptr<QPlatformAudioDevices>
    QPlatformAudioDevices::create()': gives a type Python has no way to take
    yet.
  - Qt's 'void QPlatformAudioDevices::audioInputsChanged(PrivateTag a0)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QPlatformAudioDevices::audioOutputsChanged(PrivateTag a0)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 26 functions Qt declares: 2 not a gap; 1 cannot be called and
  cannot be called through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QPlatformAudioDevices is created at the first use, not by
    'QPlatformAudioDevices(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPlatformAudioDevices.
  - Qt tells when it has removed the C++ QPlatformAudioDevices. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QPlatformAudioDevices that has no cute function yet,
    'audioInputsChanged', 'audioOutputsChanged', 'create',
    'initVideoDevicesConnection', holds a function that raises
    'NotImplementedError', and its docstring says why.
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
    Calls Qt's 'QString QPlatformAudioDevices::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qplatformaudiodevices.html#tr

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
    #  QString QPlatformAudioDevices::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN21QPlatformAudioDevices2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlatformAudioDevices'

  #  A C++ QPlatformAudioDevices Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPlatformAudioDevices'

  #  The functions Qt calls itself that QPlatformAudioDevices is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'findAudioInputs': (
          'QList<QAudioDevice> QPlatformAudioDevices::findAudioInputs() '
          'const',
      ),
      'findAudioOutputs': (
          'QList<QAudioDevice> QPlatformAudioDevices::findAudioOutputs() '
          'const',
      ),
  }

  #  The functions Qt calls itself that QPlatformAudioDevices is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'createAudioSource': (
          ('_ZN21QPlatformAudioDevices17createAudioSourceERK12QAudioDeviceR'
           'K12QAudioFormatP7QObject',
           ('address', 'address', 'QtMultimedia:QPlatformAudioSource'),
           (
               ('address', 'value', 'QtMultimedia:QAudioDevice'),
               ('address', 'value', 'QtMultimedia:QAudioFormat'),
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'createAudioSink': (
          ('_ZN21QPlatformAudioDevices15createAudioSinkERK12QAudioDeviceRK1'
           '2QAudioFormatP7QObject',
           ('address', 'address', 'QtMultimedia:QPlatformAudioSink'),
           (
               ('address', 'value', 'QtMultimedia:QAudioDevice'),
               ('address', 'value', 'QtMultimedia:QAudioFormat'),
               ('address', 'address', 'QtCore:QObject'),
           )),
      ),
      'backendName': (
          ('_ZNK21QPlatformAudioDevices11backendNameEv',
           ('address', 'value', 'QtCore:QLatin1String'),
           ()),
      ),
      'hasCallbackApi': (
          ('_ZNK21QPlatformAudioDevices14hasCallbackApiEv',
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
    Calls Qt's 'const QMetaObject *QPlatformAudioDevices::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudiodevices.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QPlatformAudioDevices::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK21QPlatformAudioDevices10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def audioInputs(self) -> QList[QAudioDevice]:
    """
    Calls Qt's 'QList<QAudioDevice> QPlatformAudioDevices::audioInputs()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudiodevices.html#audioInputs

    Returns
    -------

    QList[QAudioDevice]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QAudioDevice> QPlatformAudioDevices::audioInputs() const
    address = self.uglySide.call(
        'ritual_ZNK21QPlatformAudioDevices11audioInputsEv',
    )
    from . import QAudioDevice
    return QList[QAudioDevice]._cuteOwning(address)

  def audioOutputs(self) -> QList[QAudioDevice]:
    """
    Calls Qt's 'QList<QAudioDevice> QPlatformAudioDevices::audioOutputs()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudiodevices.html#audioOutputs

    Returns
    -------

    QList[QAudioDevice]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QAudioDevice> QPlatformAudioDevices::audioOutputs() const
    address = self.uglySide.call(
        'ritual_ZNK21QPlatformAudioDevices12audioOutputsEv',
    )
    from . import QAudioDevice
    return QList[QAudioDevice]._cuteOwning(address)

  def backendName(self) -> QLatin1String:
    """
    Calls Qt's 'QLatin1String QPlatformAudioDevices::backendName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudiodevices.html#backendName

    Returns
    -------

    QLatin1String
      A new cute QLatin1String around the copy Qt gave back. Python owns it.
    """
    #  QLatin1String QPlatformAudioDevices::backendName() const
    ritual = 'ritual_ZNK21QPlatformAudioDevices11backendNameEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QPlatformAudioDevices11backendNameEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QLatin1String
    return QLatin1String._cuteOwning(address)

  def hasCallbackApi(self) -> bool:
    """
    Calls Qt's 'bool QPlatformAudioDevices::hasCallbackApi() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudiodevices.html#hasCallbackApi
    """
    #  bool QPlatformAudioDevices::hasCallbackApi() const
    ritual = 'ritual_ZNK21QPlatformAudioDevices14hasCallbackApiEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK21QPlatformAudioDevices14hasCallbackApiEv'
    return self.uglySide.call(ritual)

  def findAudioInputs(self) -> QList[QAudioDevice]:
    """
    Calls Qt's 'QList<QAudioDevice> QPlatformAudioDevices::findAudioInputs()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudiodevices.html#findAudioInputs

    Returns
    -------

    QList[QAudioDevice]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QAudioDevice> QPlatformAudioDevices::findAudioInputs() const
    address = self.uglySide.call(
        'ritual_ZNK21QPlatformAudioDevices15findAudioInputsEv',
    )
    from . import QAudioDevice
    return QList[QAudioDevice]._cuteOwning(address)

  def findAudioOutputs(self) -> QList[QAudioDevice]:
    """
    Calls Qt's 'QList<QAudioDevice> QPlatformAudioDevices::findAudioOutputs()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudiodevices.html#findAudioOutputs

    Returns
    -------

    QList[QAudioDevice]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QAudioDevice> QPlatformAudioDevices::findAudioOutputs() const
    address = self.uglySide.call(
        'ritual_ZNK21QPlatformAudioDevices16findAudioOutputsEv',
    )
    from . import QAudioDevice
    return QList[QAudioDevice]._cuteOwning(address)

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QPlatformAudioDevices::QPlatformAudioDevices()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudiodevices.html#QPlatformAudioDevices
    """
    #  QPlatformAudioDevices::QPlatformAudioDevices()
    self._noteCreation(QPlatformAudioDevices, lambda: Rituals.call(
        'ritual_ZN21QPlatformAudioDevicesC1Ev',
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

  @overload(QAudioDevice, QAudioFormat, QObject)
  @overload(QAudioDevice, QAudioFormat, NoneType)
  def createAudioSource(
      self,
      a0: QAudioDevice,
      a1: QAudioFormat,
      parent: Optional[QObject],
  ) -> Optional[QPlatformAudioSource]:
    """
    Calls Qt's 'QPlatformAudioSource
    *QPlatformAudioDevices::createAudioSource(const QAudioDevice &a0, const
    QAudioFormat &a1, QObject *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudiodevices.html#createAudioSource

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

    Returns
    -------

    Optional[QPlatformAudioSource]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformAudioSource *QPlatformAudioDevices::createAudioSource(const
    #      QAudioDevice &a0, const QAudioFormat &a1, QObject *parent)
    ritual = (
        'ritual_ZN21QPlatformAudioDevices17createAudioSourceERK12QAudioDevi'
        'ceRK12QAudioFormatP7QObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QPlatformAudioDevices17createAudioSourceERK12QAud'
          'ioDeviceRK12QAudioFormatP7QObject')
    address = self.uglySide.call(
        ritual,
        self._valueOf(a0), self._valueOf(a1), self._addressOf(parent,
        'QObject'),
    )
    from . import QPlatformAudioSource
    return QPlatformAudioSource._cuteAt(address)

  @overload(QAudioDevice, QAudioFormat, QObject)
  @overload(QAudioDevice, QAudioFormat, NoneType)
  def createAudioSink(
      self,
      a0: QAudioDevice,
      a1: QAudioFormat,
      parent: Optional[QObject],
  ) -> Optional[QPlatformAudioSink]:
    """
    Calls Qt's 'QPlatformAudioSink
    *QPlatformAudioDevices::createAudioSink(const QAudioDevice &a0, const
    QAudioFormat &a1, QObject *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudiodevices.html#createAudioSink

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

    Returns
    -------

    Optional[QPlatformAudioSink]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformAudioSink *QPlatformAudioDevices::createAudioSink(const
    #      QAudioDevice &a0, const QAudioFormat &a1, QObject *parent)
    ritual = (
        'ritual_ZN21QPlatformAudioDevices15createAudioSinkERK12QAudioDevice'
        'RK12QAudioFormatP7QObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN21QPlatformAudioDevices15createAudioSinkERK12QAudio'
          'DeviceRK12QAudioFormatP7QObject')
    address = self.uglySide.call(
        ritual,
        self._valueOf(a0), self._valueOf(a1), self._addressOf(parent,
        'QObject'),
    )
    from . import QPlatformAudioSink
    return QPlatformAudioSink._cuteAt(address)

  @overload(QAudioFormat, QAudioDevice, QObject)
  @overload(QAudioFormat, QAudioDevice, NoneType)
  def audioInputDevice(
      self,
      a0: QAudioFormat,
      a1: QAudioDevice,
      parent: Optional[QObject],
  ) -> Optional[QPlatformAudioSource]:
    """
    Calls Qt's 'QPlatformAudioSource
    *QPlatformAudioDevices::audioInputDevice(QAudioFormat a0, const
    QAudioDevice &a1, QObject *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudiodevices.html#audioInputDevice

    Parameters
    ----------

    a0 : QAudioFormat
      Passed on as a value: Qt reads the C++ QAudioFormat, which stays
      Python's own.

    a1 : QAudioDevice
      Passed on as a value: Qt reads the C++ QAudioDevice, which stays
      Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QPlatformAudioSource]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformAudioSource
    #      *QPlatformAudioDevices::audioInputDevice(QAudioFormat a0, const
    #      QAudioDevice &a1, QObject *parent)
    address = self.uglySide.call(
        'ritual_ZN21QPlatformAudioDevices16audioInputDeviceE12QAudioFormatR'
        'K12QAudioDeviceP7QObject',
        self._valueOf(a0), self._valueOf(a1), self._addressOf(parent,
        'QObject'),
    )
    from . import QPlatformAudioSource
    return QPlatformAudioSource._cuteAt(address)

  @overload(QAudioFormat, QAudioDevice, QObject)
  @overload(QAudioFormat, QAudioDevice, NoneType)
  def audioOutputDevice(
      self,
      a0: QAudioFormat,
      a1: QAudioDevice,
      parent: Optional[QObject],
  ) -> Optional[QPlatformAudioSink]:
    """
    Calls Qt's 'QPlatformAudioSink
    *QPlatformAudioDevices::audioOutputDevice(QAudioFormat a0, const
    QAudioDevice &a1, QObject *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudiodevices.html#audioOutputDevice

    Parameters
    ----------

    a0 : QAudioFormat
      Passed on as a value: Qt reads the C++ QAudioFormat, which stays
      Python's own.

    a1 : QAudioDevice
      Passed on as a value: Qt reads the C++ QAudioDevice, which stays
      Python's own.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QPlatformAudioSink]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QPlatformAudioSink
    #      *QPlatformAudioDevices::audioOutputDevice(QAudioFormat a0, const
    #      QAudioDevice &a1, QObject *parent)
    address = self.uglySide.call(
        'ritual_ZN21QPlatformAudioDevices17audioOutputDeviceE12QAudioFormat'
        'RK12QAudioDeviceP7QObject',
        self._valueOf(a0), self._valueOf(a1), self._addressOf(parent,
        'QObject'),
    )
    from . import QPlatformAudioSink
    return QPlatformAudioSink._cuteAt(address)

  def onAudioInputsChanged(self) -> None:
    """
    Calls Qt's 'void QPlatformAudioDevices::onAudioInputsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudiodevices.html#onAudioInputsChanged
    """
    #  void QPlatformAudioDevices::onAudioInputsChanged()
    self.uglySide.call(
        'ritual_ZN21QPlatformAudioDevices20onAudioInputsChangedEv',
    )

  def onAudioOutputsChanged(self) -> None:
    """
    Calls Qt's 'void QPlatformAudioDevices::onAudioOutputsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudiodevices.html#onAudioOutputsChanged
    """
    #  void QPlatformAudioDevices::onAudioOutputsChanged()
    self.uglySide.call(
        'ritual_ZN21QPlatformAudioDevices21onAudioOutputsChangedEv',
    )

  def updateAudioInputsCache(self) -> None:
    """
    Calls Qt's 'void QPlatformAudioDevices::updateAudioInputsCache()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudiodevices.html#updateAudioInputsCache
    """
    #  void QPlatformAudioDevices::updateAudioInputsCache()
    self.uglySide.call(
        'ritual_ZN21QPlatformAudioDevices22updateAudioInputsCacheEv',
    )

  def updateAudioOutputsCache(self) -> None:
    """
    Calls Qt's 'void QPlatformAudioDevices::updateAudioOutputsCache()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplatformaudiodevices.html#updateAudioOutputsCache
    """
    #  void QPlatformAudioDevices::updateAudioOutputsCache()
    self.uglySide.call(
        'ritual_ZN21QPlatformAudioDevices23updateAudioOutputsCacheEv',
    )

  @staticmethod
  def audioInputsChanged(*__, **_) -> Never:
    """
    Qt's 'void QPlatformAudioDevices::audioInputsChanged(PrivateTag a0)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPlatformAudioDevices.audioInputsChanged' has no cute function "
        "yet. Qt's 'void "
        "QPlatformAudioDevices::audioInputsChanged(PrivateTag a0)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def audioOutputsChanged(*__, **_) -> Never:
    """
    Qt's 'void QPlatformAudioDevices::audioOutputsChanged(PrivateTag a0)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPlatformAudioDevices.audioOutputsChanged' has no cute function "
        "yet. Qt's 'void "
        "QPlatformAudioDevices::audioOutputsChanged(PrivateTag a0)': takes "
        "a type Python has no way to hand over yet.")

  @staticmethod
  def create(*__, **_) -> Never:
    """
    Qt's 'std::unique_ptr<QPlatformAudioDevices>
    QPlatformAudioDevices::create()': gives a type Python has no way to take
    yet.
    """
    raise NotImplementedError(
        "'QPlatformAudioDevices.create' has no cute function yet. Qt's "
        "'std::unique_ptr<QPlatformAudioDevices> "
        "QPlatformAudioDevices::create()': gives a type Python has no way "
        "to take yet.")

  @staticmethod
  def initVideoDevicesConnection(*__, **_) -> Never:
    """
    Qt's 'void QPlatformAudioDevices::initVideoDevicesConnection()': cannot
    be called and cannot be called through the meta-object and cannot be
    copied: no header file has its code, Qt's source does not mark it or its
    class for use from outside Qt or writes it 'inline' or nowhere, and it is
    no signal, slot or invokable function giving back nothing, of a class
    built on QObject, and Qt's source has no code for it that could be told
    from the rest.
    """
    raise NotImplementedError(
        "'QPlatformAudioDevices.initVideoDevicesConnection' has no cute "
        "function yet. Qt's 'void "
        "QPlatformAudioDevices::initVideoDevicesConnection()': cannot be "
        "called and cannot be called through the meta-object and cannot be "
        "copied: no header file has its code, Qt's source does not mark it "
        "or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")
