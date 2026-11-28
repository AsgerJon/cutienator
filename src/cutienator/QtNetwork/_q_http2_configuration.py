"""
QHttp2Configuration binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qhttp2configuration.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QHttp2Configuration(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QHttp2Configuration: a plain Python object standing
  in front of one C++ QHttp2Configuration.

  C++ hands a QHttp2Configuration around as a copy, so every C++
  QHttp2Configuration behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QHttp2Configuration that has a ritual and that
  Python can call so far, 15 names in all: 'setServerPushEnabled',
  'serverPushEnabled', 'setHuffmanCompressionEnabled',
  'huffmanCompressionEnabled', 'setSessionReceiveWindowSize',
  'sessionReceiveWindowSize', 'setStreamReceiveWindowSize',
  'streamReceiveWindowSize', 'setMaxFrameSize', 'maxFrameSize',
  'setMaxConcurrentStreams', 'maxConcurrentStreams', 'isEqual', '__eq__',
  '__ne__'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QHttp2Configuration::QHttp2Configuration(QHttp2Configuration
    &&other)': takes a type Python has no way to hand over yet.
  - Qt's 'QHttp2Configuration &QHttp2Configuration::operator=(const
    QHttp2Configuration &other)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QHttp2Configuration
    &QHttp2Configuration::operator=(QHttp2Configuration &&other)':
    assignment: Python binds a name and has no operator for it.
  - Qt's 'QHttp2Configuration::~QHttp2Configuration()': the destructor:
    Python removes its C++ QHttp2Configuration by it, and has no other use
    for it.
  - Qt's 'void QHttp2Configuration::swap(QHttp2Configuration &other)': takes
    a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QHttp2Configuration is created at the first use, not by
    'QHttp2Configuration(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QHttp2Configuration back gives a copy the ritual made
    for Python, in a new cute QHttp2Configuration.
  - Each name of Qt's QHttp2Configuration that has no cute function yet,
    'swap', holds a function that raises 'NotImplementedError', and its
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
  __qt_class__ = 'QHttp2Configuration'

  #  Qt's '~QHttp2Configuration()'. Naming it makes this a value class:
  #  Python owns every C++ QHttp2Configuration behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QHttp2ConfigurationD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def serverPushEnabled(self) -> bool:
    """
    Calls Qt's 'bool QHttp2Configuration::serverPushEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2configuration.html#serverPushEnabled
    """
    #  bool QHttp2Configuration::serverPushEnabled() const
    return self.uglySide.call(
        'ritual_ZNK19QHttp2Configuration17serverPushEnabledEv',
    )

  def huffmanCompressionEnabled(self) -> bool:
    """
    Calls Qt's 'bool QHttp2Configuration::huffmanCompressionEnabled() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2configuration.html#huffmanCompressionEnabled
    """
    #  bool QHttp2Configuration::huffmanCompressionEnabled() const
    return self.uglySide.call(
        'ritual_ZNK19QHttp2Configuration25huffmanCompressionEnabledEv',
    )

  def sessionReceiveWindowSize(self) -> int:
    """
    Calls Qt's 'unsigned int QHttp2Configuration::sessionReceiveWindowSize()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2configuration.html#sessionReceiveWindowSize
    """
    #  unsigned int QHttp2Configuration::sessionReceiveWindowSize() const
    return self.uglySide.call(
        'ritual_ZNK19QHttp2Configuration24sessionReceiveWindowSizeEv',
    )

  def streamReceiveWindowSize(self) -> int:
    """
    Calls Qt's 'unsigned int QHttp2Configuration::streamReceiveWindowSize()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2configuration.html#streamReceiveWindowSize
    """
    #  unsigned int QHttp2Configuration::streamReceiveWindowSize() const
    return self.uglySide.call(
        'ritual_ZNK19QHttp2Configuration23streamReceiveWindowSizeEv',
    )

  def maxFrameSize(self) -> int:
    """
    Calls Qt's 'unsigned int QHttp2Configuration::maxFrameSize() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2configuration.html#maxFrameSize
    """
    #  unsigned int QHttp2Configuration::maxFrameSize() const
    return self.uglySide.call(
        'ritual_ZNK19QHttp2Configuration12maxFrameSizeEv',
    )

  def maxConcurrentStreams(self) -> int:
    """
    Calls Qt's 'unsigned int QHttp2Configuration::maxConcurrentStreams()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2configuration.html#maxConcurrentStreams
    """
    #  unsigned int QHttp2Configuration::maxConcurrentStreams() const
    return self.uglySide.call(
        'ritual_ZNK19QHttp2Configuration20maxConcurrentStreamsEv',
    )

  @overload(THIS)
  def isEqual(self, other: QHttp2Configuration) -> bool:
    """
    Calls Qt's 'bool QHttp2Configuration::isEqual(const QHttp2Configuration
    &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qhttp2configuration.html#isEqual

    Parameters
    ----------

    other : QHttp2Configuration
      Passed on as a value: Qt reads the C++ QHttp2Configuration, which stays
      Python's own.
    """
    #  bool QHttp2Configuration::isEqual(const QHttp2Configuration &other)
    #      const
    return self.uglySide.call(
        'ritual_ZNK19QHttp2Configuration7isEqualERKS_', self._valueOf(other),
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(bool)
  def setServerPushEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QHttp2Configuration::setServerPushEnabled(bool enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2configuration.html#setServerPushEnabled

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QHttp2Configuration::setServerPushEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN19QHttp2Configuration20setServerPushEnabledEb', enable,
    )

  @overload(bool)
  def setHuffmanCompressionEnabled(self, enable: bool) -> None:
    """
    Calls Qt's 'void QHttp2Configuration::setHuffmanCompressionEnabled(bool
    enable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2configuration.html

    Parameters
    ----------

    enable : bool
      Passed on as it is.
    """
    #  void QHttp2Configuration::setHuffmanCompressionEnabled(bool enable)
    self.uglySide.call(
        'ritual_ZN19QHttp2Configuration28setHuffmanCompressionEnabledEb',
        enable,
    )

  @overload(int)
  def setSessionReceiveWindowSize(self, size: int) -> bool:
    """
    Calls Qt's 'bool
    QHttp2Configuration::setSessionReceiveWindowSize(unsigned int size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2configuration.html

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  bool QHttp2Configuration::setSessionReceiveWindowSize(unsigned int
    #      size)
    return self.uglySide.call(
        'ritual_ZN19QHttp2Configuration27setSessionReceiveWindowSizeEj',
        size,
    )

  @overload(int)
  def setStreamReceiveWindowSize(self, size: int) -> bool:
    """
    Calls Qt's 'bool QHttp2Configuration::setStreamReceiveWindowSize(unsigned
    int size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2configuration.html

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  bool QHttp2Configuration::setStreamReceiveWindowSize(unsigned int
    #      size)
    return self.uglySide.call(
        'ritual_ZN19QHttp2Configuration26setStreamReceiveWindowSizeEj', size,
    )

  @overload(int)
  def setMaxFrameSize(self, size: int) -> bool:
    """
    Calls Qt's 'bool QHttp2Configuration::setMaxFrameSize(unsigned int
    size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2configuration.html#setMaxFrameSize

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  bool QHttp2Configuration::setMaxFrameSize(unsigned int size)
    return self.uglySide.call(
        'ritual_ZN19QHttp2Configuration15setMaxFrameSizeEj', size,
    )

  @overload(int)
  def setMaxConcurrentStreams(self, value: int) -> None:
    """
    Calls Qt's 'void QHttp2Configuration::setMaxConcurrentStreams(unsigned
    int value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2configuration.html#setMaxConcurrentStreams

    Parameters
    ----------

    value : int
      Passed on as it is.
    """
    #  void QHttp2Configuration::setMaxConcurrentStreams(unsigned int value)
    self.uglySide.call(
        'ritual_ZN19QHttp2Configuration23setMaxConcurrentStreamsEj', value,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QHttp2Configuration) -> bool:
    """
    Calls Qt's 'bool operator==(const QHttp2Configuration &lhs, const
    QHttp2Configuration &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2configuration.html#operator==

    Parameters
    ----------

    rhs : QHttp2Configuration
      Passed on as a value: Qt reads the C++ QHttp2Configuration, which stays
      Python's own.
    """
    #  bool operator==(const QHttp2Configuration &lhs, const
    #      QHttp2Configuration &rhs)
    return Rituals.call(
        'ritual_ZeqRK19QHttp2ConfigurationS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, rhs: QHttp2Configuration) -> bool:
    """
    Calls Qt's 'bool operator!=(const QHttp2Configuration &lhs, const
    QHttp2Configuration &rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2configuration.html#operator!=

    Parameters
    ----------

    rhs : QHttp2Configuration
      Passed on as a value: Qt reads the C++ QHttp2Configuration, which stays
      Python's own.
    """
    #  bool operator!=(const QHttp2Configuration &lhs, const
    #      QHttp2Configuration &rhs)
    return Rituals.call(
        'ritual_ZneRK19QHttp2ConfigurationS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QHttp2Configuration::QHttp2Configuration()', which is called at the
    first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2configuration.html#QHttp2Configuration
    """
    #  QHttp2Configuration::QHttp2Configuration()
    self._noteCreation(QHttp2Configuration, lambda: Rituals.call(
        'ritual_ZN19QHttp2ConfigurationC1Ev',
    ))

  @overload(THIS)
  def __init__(self, other: QHttp2Configuration) -> None:
    """
    Notes what was given, for Qt's
    'QHttp2Configuration::QHttp2Configuration(const QHttp2Configuration
    &other)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qhttp2configuration.html#QHttp2Configuration

    Parameters
    ----------

    other : QHttp2Configuration
      Passed on as a value: Qt reads the C++ QHttp2Configuration, which stays
      Python's own.
    """
    #  QHttp2Configuration::QHttp2Configuration(const QHttp2Configuration
    #      &other)
    self._noteCreation(QHttp2Configuration, lambda: Rituals.call(
        'ritual_ZN19QHttp2ConfigurationC1ERKS_', self._valueOf(other),
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

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QHttp2Configuration::swap(QHttp2Configuration &other)': takes
    a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QHttp2Configuration.swap' has no cute function yet. Qt's 'void "
        "QHttp2Configuration::swap(QHttp2Configuration &other)': takes a "
        "type Python has no way to hand over yet.")
