"""
QPulseAudioDevices binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qpulseaudiodevices_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QPulseAudioDevices to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QList, QObject
from . import QPlatformAudioDevices

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

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


class QPulseAudioDevices(QPlatformAudioDevices):
  """
  The cute side of Qt's QPulseAudioDevices: a plain Python object standing in
  front of one C++ QPulseAudioDevices.

  It is built on the cute 'QPlatformAudioDevices', as Qt's QPulseAudioDevices
  is built on Qt's QPlatformAudioDevices, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QPulseAudioDevices that has a ritual and that Python
  can call so far, 6 names in all: 'createAudioSource', 'createAudioSink',
  'backendName', 'hasCallbackApi', 'findAudioInputs', 'findAudioOutputs'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPulseAudioDevices::~QPulseAudioDevices()': the destructor: Python
    never removes a C++ QPulseAudioDevices.

  What has no ritual
  ------------------

  1 of the 8 functions Qt declares: 1 leans on 'QPulseAudioContextManager.

  What to expect
  --------------

  - The C++ QPulseAudioDevices is created at the first use, not by
    'QPulseAudioDevices(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QPulseAudioDevices.
  - Qt tells when it has removed the C++ QPulseAudioDevices. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QPulseAudioDevices that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPulseAudioDevices'

  #  A C++ QPulseAudioDevices Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QPulseAudioDevices'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def backendName(self) -> QLatin1String:
    """
    Calls Qt's 'QLatin1String QPulseAudioDevices::backendName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpulseaudiodevices.html#backendName

    Returns
    -------

    QLatin1String
      A new cute QLatin1String around the copy Qt gave back. Python owns it.
    """
    #  QLatin1String QPulseAudioDevices::backendName() const
    ritual = 'ritual_ZNK18QPulseAudioDevices11backendNameEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QPulseAudioDevices11backendNameEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QLatin1String
    return QLatin1String._cuteOwning(address)

  def hasCallbackApi(self) -> bool:
    """
    Calls Qt's 'bool QPulseAudioDevices::hasCallbackApi() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpulseaudiodevices.html#hasCallbackApi
    """
    #  bool QPulseAudioDevices::hasCallbackApi() const
    ritual = 'ritual_ZNK18QPulseAudioDevices14hasCallbackApiEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK18QPulseAudioDevices14hasCallbackApiEv'
    return self.uglySide.call(ritual)

  def findAudioInputs(self) -> QList[QAudioDevice]:
    """
    Calls Qt's 'QList<QAudioDevice> QPulseAudioDevices::findAudioInputs()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpulseaudiodevices.html#findAudioInputs

    Returns
    -------

    QList[QAudioDevice]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QAudioDevice> QPulseAudioDevices::findAudioInputs() const
    address = self.uglySide.call(
        'ritual_ZNK18QPulseAudioDevices15findAudioInputsEv',
    )
    from . import QAudioDevice
    return QList[QAudioDevice]._cuteOwning(address)

  def findAudioOutputs(self) -> QList[QAudioDevice]:
    """
    Calls Qt's 'QList<QAudioDevice> QPulseAudioDevices::findAudioOutputs()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpulseaudiodevices.html#findAudioOutputs

    Returns
    -------

    QList[QAudioDevice]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QAudioDevice> QPulseAudioDevices::findAudioOutputs() const
    address = self.uglySide.call(
        'ritual_ZNK18QPulseAudioDevices16findAudioOutputsEv',
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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QPulseAudioDevices::QPulseAudioDevices()': leans on
    'QPulseAudioContextManager::staticMetaObject', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QPulseAudioDevices.__init__' has no cute function yet. Qt's "
        "'QPulseAudioDevices::QPulseAudioDevices()': leans on "
        "'QPulseAudioContextManager::staticMetaObject', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

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
    *QPulseAudioDevices::createAudioSource(const QAudioDevice &a0, const
    QAudioFormat &a1, QObject *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpulseaudiodevices.html#createAudioSource

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
    #  QPlatformAudioSource *QPulseAudioDevices::createAudioSource(const
    #      QAudioDevice &a0, const QAudioFormat &a1, QObject *parent)
    address = self.uglySide.call(
        'ritual_ZN18QPulseAudioDevices17createAudioSourceERK12QAudioDeviceR'
        'K12QAudioFormatP7QObject',
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
    Calls Qt's 'QPlatformAudioSink *QPulseAudioDevices::createAudioSink(const
    QAudioDevice &a0, const QAudioFormat &a1, QObject *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qpulseaudiodevices.html#createAudioSink

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
    #  QPlatformAudioSink *QPulseAudioDevices::createAudioSink(const
    #      QAudioDevice &a0, const QAudioFormat &a1, QObject *parent)
    address = self.uglySide.call(
        'ritual_ZN18QPulseAudioDevices15createAudioSinkERK12QAudioDeviceRK1'
        '2QAudioFormatP7QObject',
        self._valueOf(a0), self._valueOf(a1), self._addressOf(parent,
        'QObject'),
    )
    from . import QPlatformAudioSink
    return QPlatformAudioSink._cuteAt(address)
