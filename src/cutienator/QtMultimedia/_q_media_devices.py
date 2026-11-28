"""
QMediaDevices binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/qmediadevices.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaMethod, QMetaObject
  from . import QAudioDevice, QCameraDevice
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QMetaMethod = WAIT['QMetaMethod']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QMediaDevices(QObject):
  """
  The cute side of Qt's QMediaDevices: a plain Python object standing in
  front of one C++ QMediaDevices.

  It is built on the cute 'QObject', as Qt's QMediaDevices is built on Qt's
  QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QMediaDevices that has a ritual and that Python can
  call so far, 12 names in all: 'metaObject', 'tr', 'audioInputs',
  'audioOutputs', 'videoInputs', 'defaultAudioInput', 'defaultAudioOutput',
  'defaultVideoInput', 'audioInputsChanged', 'audioOutputsChanged',
  'videoInputsChanged', 'connectNotify'. It can be made from Python, in 1
  way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QMediaDevices::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QMediaDevices::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'QMediaDevices::~QMediaDevices()': the destructor: Python never
    removes a C++ QMediaDevices.

  What has no ritual
  ------------------

  2 of the 18 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QMediaDevices is created at the first use, not by
    'QMediaDevices(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QMediaDevices.
  - Qt tells when it has removed the C++ QMediaDevices. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
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
    Calls Qt's 'QString QMediaDevices::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qmediadevices.html#tr

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
    #  QString QMediaDevices::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN13QMediaDevices2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  @staticmethod
  def audioInputs() -> QList[QAudioDevice]:
    """
    Calls Qt's 'QList<QAudioDevice> QMediaDevices::audioInputs()'.

    Qt's own words: https://doc.qt.io/qt-6/qmediadevices.html#audioInputs

    Returns
    -------

    QList[QAudioDevice]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QAudioDevice> QMediaDevices::audioInputs()
    address = Rituals.call('ritual_ZN13QMediaDevices11audioInputsEv')
    from . import QAudioDevice
    return QList[QAudioDevice]._cuteOwning(address)

  @staticmethod
  def audioOutputs() -> QList[QAudioDevice]:
    """
    Calls Qt's 'QList<QAudioDevice> QMediaDevices::audioOutputs()'.

    Qt's own words: https://doc.qt.io/qt-6/qmediadevices.html#audioOutputs

    Returns
    -------

    QList[QAudioDevice]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QAudioDevice> QMediaDevices::audioOutputs()
    address = Rituals.call('ritual_ZN13QMediaDevices12audioOutputsEv')
    from . import QAudioDevice
    return QList[QAudioDevice]._cuteOwning(address)

  @staticmethod
  def videoInputs() -> QList[QCameraDevice]:
    """
    Calls Qt's 'QList<QCameraDevice> QMediaDevices::videoInputs()'.

    Qt's own words: https://doc.qt.io/qt-6/qmediadevices.html#videoInputs

    Returns
    -------

    QList[QCameraDevice]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QCameraDevice> QMediaDevices::videoInputs()
    address = Rituals.call('ritual_ZN13QMediaDevices11videoInputsEv')
    from . import QCameraDevice
    return QList[QCameraDevice]._cuteOwning(address)

  @staticmethod
  def defaultAudioInput() -> QAudioDevice:
    """
    Calls Qt's 'QAudioDevice QMediaDevices::defaultAudioInput()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediadevices.html#defaultAudioInput

    Returns
    -------

    QAudioDevice
      A new cute QAudioDevice around the copy Qt gave back. Python owns it.
    """
    #  QAudioDevice QMediaDevices::defaultAudioInput()
    address = Rituals.call('ritual_ZN13QMediaDevices17defaultAudioInputEv')
    from . import QAudioDevice
    return QAudioDevice._cuteOwning(address)

  @staticmethod
  def defaultAudioOutput() -> QAudioDevice:
    """
    Calls Qt's 'QAudioDevice QMediaDevices::defaultAudioOutput()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediadevices.html#defaultAudioOutput

    Returns
    -------

    QAudioDevice
      A new cute QAudioDevice around the copy Qt gave back. Python owns it.
    """
    #  QAudioDevice QMediaDevices::defaultAudioOutput()
    address = Rituals.call('ritual_ZN13QMediaDevices18defaultAudioOutputEv')
    from . import QAudioDevice
    return QAudioDevice._cuteOwning(address)

  @staticmethod
  def defaultVideoInput() -> QCameraDevice:
    """
    Calls Qt's 'QCameraDevice QMediaDevices::defaultVideoInput()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediadevices.html#defaultVideoInput

    Returns
    -------

    QCameraDevice
      A new cute QCameraDevice around the copy Qt gave back. Python owns it.
    """
    #  QCameraDevice QMediaDevices::defaultVideoInput()
    address = Rituals.call('ritual_ZN13QMediaDevices17defaultVideoInputEv')
    from . import QCameraDevice
    return QCameraDevice._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QMediaDevices'

  #  A C++ QMediaDevices Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QMediaDevices'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QMediaDevices::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qmediadevices.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QMediaDevices::metaObject() const
    address = self.uglySide.call('ritual_ZNK13QMediaDevices10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's 'QMediaDevices::QMediaDevices(QObject
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qmediadevices.html#QMediaDevices

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QMediaDevices::QMediaDevices(QObject *parent)
    self._noteCreation(QMediaDevices, lambda: Rituals.call(
        'ritual_ZN13QMediaDevicesC1EP7QObject',
        self._addressOf(parent, 'QObject'),
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

  def audioInputsChanged(self) -> None:
    """
    Calls Qt's 'void QMediaDevices::audioInputsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediadevices.html#audioInputsChanged
    """
    #  void QMediaDevices::audioInputsChanged()
    self.uglySide.call('ritual_ZN13QMediaDevices18audioInputsChangedEv')

  def audioOutputsChanged(self) -> None:
    """
    Calls Qt's 'void QMediaDevices::audioOutputsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediadevices.html#audioOutputsChanged
    """
    #  void QMediaDevices::audioOutputsChanged()
    self.uglySide.call('ritual_ZN13QMediaDevices19audioOutputsChangedEv')

  def videoInputsChanged(self) -> None:
    """
    Calls Qt's 'void QMediaDevices::videoInputsChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qmediadevices.html#videoInputsChanged
    """
    #  void QMediaDevices::videoInputsChanged()
    self.uglySide.call('ritual_ZN13QMediaDevices18videoInputsChangedEv')

  @overload(QMetaMethod)
  def connectNotify(self, signal: QMetaMethod) -> None:
    """
    Calls Qt's 'void QMediaDevices::connectNotify(const QMetaMethod
    &signal)'.

    Qt's own words: https://doc.qt.io/qt-6/qmediadevices.html#connectNotify

    Parameters
    ----------

    signal : QMetaMethod
      Passed on as a value: Qt reads the C++ QMetaMethod, which stays
      Python's own.
    """
    #  void QMediaDevices::connectNotify(const QMetaMethod &signal)
    ritual = 'ritual_ZN13QMediaDevices13connectNotifyERK11QMetaMethod'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN13QMediaDevices13connectNotifyERK11QMetaMethod'
    self.uglySide.call(ritual, self._valueOf(signal))
