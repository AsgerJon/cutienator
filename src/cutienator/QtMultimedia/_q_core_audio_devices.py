"""
QCoreAudioDevices binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qcoreaudiodevices_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QCoreAudioDevices to be private: it declares the class in a
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


class QCoreAudioDevices(QPlatformAudioDevices):
  """
  The cute side of Qt's QCoreAudioDevices: a plain Python object standing in
  front of one C++ QCoreAudioDevices.

  It is built on the cute 'QPlatformAudioDevices', as Qt's QCoreAudioDevices
  is built on Qt's QPlatformAudioDevices, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QCoreAudioDevices that has a ritual and that Python
  can call so far, 6 names in all: 'createAudioSource', 'createAudioSink',
  'backendName', 'hasCallbackApi', 'findAudioInputs', 'findAudioOutputs'.
  None can be made from Python: one comes out of a function of another class
  that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCoreAudioDevices::~QCoreAudioDevices()': the destructor: Python
    never removes a C++ QCoreAudioDevices.

  What has no ritual
  ------------------

  1 of the 8 functions Qt declares: 1 cannot be called and cannot be called
  through the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QCoreAudioDevices is created at the first use, not by
    'QCoreAudioDevices(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCoreAudioDevices.
  - Qt tells when it has removed the C++ QCoreAudioDevices. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QCoreAudioDevices that has no cute function yet,
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
  __qt_class__ = 'QCoreAudioDevices'

  #  A C++ QCoreAudioDevices Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QCoreAudioDevices'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def backendName(self) -> QLatin1String:
    """
    Calls Qt's 'QLatin1String QCoreAudioDevices::backendName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcoreaudiodevices.html#backendName

    Returns
    -------

    QLatin1String
      A new cute QLatin1String around the copy Qt gave back. Python owns it.
    """
    #  QLatin1String QCoreAudioDevices::backendName() const
    ritual = 'ritual_ZNK17QCoreAudioDevices11backendNameEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QCoreAudioDevices11backendNameEv'
    address = self.uglySide.call(ritual)
    from ..QtCore import QLatin1String
    return QLatin1String._cuteOwning(address)

  def hasCallbackApi(self) -> bool:
    """
    Calls Qt's 'bool QCoreAudioDevices::hasCallbackApi() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreaudiodevices.html#hasCallbackApi
    """
    #  bool QCoreAudioDevices::hasCallbackApi() const
    ritual = 'ritual_ZNK17QCoreAudioDevices14hasCallbackApiEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QCoreAudioDevices14hasCallbackApiEv'
    return self.uglySide.call(ritual)

  def findAudioInputs(self) -> QList[QAudioDevice]:
    """
    Calls Qt's 'QList<QAudioDevice> QCoreAudioDevices::findAudioInputs()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreaudiodevices.html#findAudioInputs

    Returns
    -------

    QList[QAudioDevice]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QAudioDevice> QCoreAudioDevices::findAudioInputs() const
    address = self.uglySide.call(
        'ritual_ZNK17QCoreAudioDevices15findAudioInputsEv',
    )
    from . import QAudioDevice
    return QList[QAudioDevice]._cuteOwning(address)

  def findAudioOutputs(self) -> QList[QAudioDevice]:
    """
    Calls Qt's 'QList<QAudioDevice> QCoreAudioDevices::findAudioOutputs()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreaudiodevices.html#findAudioOutputs

    Returns
    -------

    QList[QAudioDevice]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QAudioDevice> QCoreAudioDevices::findAudioOutputs() const
    address = self.uglySide.call(
        'ritual_ZNK17QCoreAudioDevices16findAudioOutputsEv',
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
    Qt's 'QCoreAudioDevices::QCoreAudioDevices()': cannot be called and
    cannot be called through the meta-object and cannot be copied: no header
    file has its code, Qt's source does not mark it or its class for use from
    outside Qt or writes it 'inline' or nowhere, and it is no signal, slot or
    invokable function giving back nothing, of a class built on QObject, and
    Qt's source has no code for it that could be told from the rest.
    """
    raise NotImplementedError(
        "'QCoreAudioDevices.__init__' has no cute function yet. Qt's "
        "'QCoreAudioDevices::QCoreAudioDevices()': cannot be called and "
        "cannot be called through the meta-object and cannot be copied: no "
        "header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")

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
    *QCoreAudioDevices::createAudioSource(const QAudioDevice &a0, const
    QAudioFormat &a1, QObject *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreaudiodevices.html#createAudioSource

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
    #  QPlatformAudioSource *QCoreAudioDevices::createAudioSource(const
    #      QAudioDevice &a0, const QAudioFormat &a1, QObject *parent)
    ritual = (
        'ritual_ZN17QCoreAudioDevices17createAudioSourceERK12QAudioDeviceRK'
        '12QAudioFormatP7QObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QCoreAudioDevices17createAudioSourceERK12QAudioDe'
          'viceRK12QAudioFormatP7QObject')
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
    Calls Qt's 'QPlatformAudioSink *QCoreAudioDevices::createAudioSink(const
    QAudioDevice &a0, const QAudioFormat &a1, QObject *parent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcoreaudiodevices.html#createAudioSink

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
    #  QPlatformAudioSink *QCoreAudioDevices::createAudioSink(const
    #      QAudioDevice &a0, const QAudioFormat &a1, QObject *parent)
    ritual = (
        'ritual_ZN17QCoreAudioDevices15createAudioSinkERK12QAudioDeviceRK12'
        'QAudioFormatP7QObject')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QCoreAudioDevices15createAudioSinkERK12QAudioDevi'
          'ceRK12QAudioFormatP7QObject')
    address = self.uglySide.call(
        ritual,
        self._valueOf(a0), self._valueOf(a1), self._addressOf(parent,
        'QObject'),
    )
    from . import QPlatformAudioSink
    return QPlatformAudioSink._cuteAt(address)
