"""
QAndroidAudioDevices binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qandroidaudiodevices_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QAndroidAudioDevices to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QPlatformAudioDevices

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QLatin1String
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


class QAndroidAudioDevices(QPlatformAudioDevices):
  """
  The cute side of Qt's QAndroidAudioDevices: a plain Python object standing
  in front of one C++ QAndroidAudioDevices.

  It is built on the cute 'QPlatformAudioDevices', as Qt's
  QAndroidAudioDevices is built on Qt's QPlatformAudioDevices, and has
  everything that class has.

  What exists
  -----------

  Every function of Qt's QAndroidAudioDevices that has a ritual and that
  Python can call so far, 7 names in all: 'createAudioSource',
  'createAudioSink', 'backendName', 'hasCallbackApi',
  'registerNativeMethods', 'findAudioInputs', 'findAudioOutputs'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QAndroidAudioDevices::~QAndroidAudioDevices()': the destructor:
    Python never removes a C++ QAndroidAudioDevices.

  What to expect
  --------------

  - The C++ QAndroidAudioDevices is created at the first use, not by
    'QAndroidAudioDevices(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QAndroidAudioDevices.
  - Qt tells when it has removed the C++ QAndroidAudioDevices. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def registerNativeMethods() -> bool:
    """
    Calls Qt's 'bool QAndroidAudioDevices::registerNativeMethods()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qandroidaudiodevices.html#registerNativeMethods
    """
    #  bool QAndroidAudioDevices::registerNativeMethods()
    return Rituals.call(
        'ritual_ZN20QAndroidAudioDevices21registerNativeMethodsEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QAndroidAudioDevices'

  #  A C++ QAndroidAudioDevices Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QAndroidAudioDevices'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def backendName(self) -> QLatin1String:
    """
    Calls Qt's 'QLatin1String QAndroidAudioDevices::backendName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qandroidaudiodevices.html#backendName

    Returns
    -------

    QLatin1String
      A new cute QLatin1String around the copy Qt gave back. Python owns it.
    """
    #  QLatin1String QAndroidAudioDevices::backendName() const
    ritual = 'ritual_ZNK20QAndroidAudioDevices11backendNameEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QAndroidAudioDevices11backendNameEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QLatin1String
    return QLatin1String._cuteOwning(address)

  def hasCallbackApi(self) -> bool:
    """
    Calls Qt's 'bool QAndroidAudioDevices::hasCallbackApi() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qandroidaudiodevices.html#hasCallbackApi
    """
    #  bool QAndroidAudioDevices::hasCallbackApi() const
    ritual = 'ritual_ZNK20QAndroidAudioDevices14hasCallbackApiEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK20QAndroidAudioDevices14hasCallbackApiEv'
    return self.uglySide.call(ritual)

  def findAudioInputs(self) -> QList[QAudioDevice]:
    """
    Calls Qt's 'QList<QAudioDevice> QAndroidAudioDevices::findAudioInputs()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qandroidaudiodevices.html#findAudioInputs

    Returns
    -------

    QList[QAudioDevice]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QAudioDevice> QAndroidAudioDevices::findAudioInputs() const
    address = self.uglySide.call(
        'ritual_ZNK20QAndroidAudioDevices15findAudioInputsEv',
    )
    from . import QAudioDevice
    return QList[QAudioDevice]._cuteOwning(address)

  def findAudioOutputs(self) -> QList[QAudioDevice]:
    """
    Calls Qt's 'QList<QAudioDevice> QAndroidAudioDevices::findAudioOutputs()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qandroidaudiodevices.html#findAudioOutputs

    Returns
    -------

    QList[QAudioDevice]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QAudioDevice> QAndroidAudioDevices::findAudioOutputs() const
    address = self.uglySide.call(
        'ritual_ZNK20QAndroidAudioDevices16findAudioOutputsEv',
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
    'QAndroidAudioDevices::QAndroidAudioDevices()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qandroidaudiodevices.html#QAndroidAudioDevices
    """
    #  QAndroidAudioDevices::QAndroidAudioDevices()
    self._noteCreation(QAndroidAudioDevices, lambda: Rituals.call(
        'ritual_ZN20QAndroidAudioDevicesC1Ev',
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
    *QAndroidAudioDevices::createAudioSource(const QAudioDevice &a0, const
    QAudioFormat &a1, QObject *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qandroidaudiodevices.html#createAudioSource

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
    #  QPlatformAudioSource *QAndroidAudioDevices::createAudioSource(const
    #      QAudioDevice &a0, const QAudioFormat &a1, QObject *parent)
    ritual = (
        'ritual_ZN20QAndroidAudioDevices17createAudioSourceERK12QAudioDevic'
        'eRK12QAudioFormatP7QObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QAndroidAudioDevices17createAudioSourceERK12QAudi'
          'oDeviceRK12QAudioFormatP7QObject')
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
    *QAndroidAudioDevices::createAudioSink(const QAudioDevice &a0, const
    QAudioFormat &a1, QObject *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qandroidaudiodevices.html#createAudioSink

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
    #  QPlatformAudioSink *QAndroidAudioDevices::createAudioSink(const
    #      QAudioDevice &a0, const QAudioFormat &a1, QObject *parent)
    ritual = (
        'ritual_ZN20QAndroidAudioDevices15createAudioSinkERK12QAudioDeviceR'
        'K12QAudioFormatP7QObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN20QAndroidAudioDevices15createAudioSinkERK12QAudioD'
          'eviceRK12QAudioFormatP7QObject')
    address = self.uglySide.call(
        ritual,
        self._valueOf(a0), self._valueOf(a1), self._addressOf(parent,
        'QObject'),
    )
    from . import QPlatformAudioSink
    return QPlatformAudioSink._cuteAt(address)
