"""
QPlaybackOptions binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/qplaybackoptions.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QPlaybackOptions(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QPlaybackOptions: a plain Python object standing in
  front of one C++ QPlaybackOptions.

  C++ hands a QPlaybackOptions around as a copy, so every C++
  QPlaybackOptions behind a cute one is Python's own: it is removed, by the
  ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QPlaybackOptions that has a ritual and that Python
  can call so far, 13 names in all: 'resetNetworkTimeout', 'playbackIntent',
  'setPlaybackIntent', 'resetPlaybackIntent', 'probeSize', 'setProbeSize',
  'resetProbeSize', '__eq__', '__ne__', '__lt__', '__gt__', '__le__',
  '__ge__'. It can be made from Python, in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QPlaybackOptions &QPlaybackOptions::operator=(const
    QPlaybackOptions &a0)': assignment: Python binds a name and has no
    operator for it.
  - Qt's 'QPlaybackOptions::QPlaybackOptions(QPlaybackOptions &&a0)': takes a
    type Python has no way to hand over yet.
  - Qt's 'QPlaybackOptions &QPlaybackOptions::operator=(QPlaybackOptions
    &&other)': assignment: Python binds a name and has no operator for it.
  - Qt's 'QPlaybackOptions::~QPlaybackOptions()': the destructor: Python
    removes its C++ QPlaybackOptions by it, and has no other use for it.
  - Qt's 'void QPlaybackOptions::swap(QPlaybackOptions &other)': takes a type
    Python has no way to hand over yet.
  - Qt's 'std::chrono::milliseconds QPlaybackOptions::networkTimeout()
    const': gives a type Python has no way to take yet.
  - Qt's 'void QPlaybackOptions::setNetworkTimeout(std::chrono::milliseconds
    timeout)': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  3 of the 25 functions Qt declares: 3 not a gap.

  What to expect
  --------------

  - The C++ QPlaybackOptions is created at the first use, not by
    'QPlaybackOptions(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QPlaybackOptions back gives a copy the ritual made
    for Python, in a new cute QPlaybackOptions.
  - Each name of Qt's QPlaybackOptions that has no cute function yet,
    'networkTimeout', 'setNetworkTimeout', 'swap', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QPlaybackOptions, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class PlaybackIntent(CuteNum, scoped=True):
    """
    The enum 'QPlaybackOptions::PlaybackIntent' of Qt, with the 2 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Playback = Kee[int](0)
    LowLatencyStreaming = Kee[int](1)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QPlaybackOptions'

  #  Qt's '~QPlaybackOptions()'. Naming it makes this a value class: Python
  #  owns every C++ QPlaybackOptions behind a cute one, and removes it by
  #  this ritual.
  __delete_ritual__ = 'ritual_ZN16QPlaybackOptionsD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def playbackIntent(self) -> PlaybackIntent:
    """
    Calls Qt's 'PlaybackIntent QPlaybackOptions::playbackIntent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaybackoptions.html#playbackIntent

    Returns
    -------

    PlaybackIntent
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'PlaybackIntent(number)'
      gives.
    """
    #  PlaybackIntent QPlaybackOptions::playbackIntent() const
    return QPlaybackOptions.PlaybackIntent(self.uglySide.call(
        'ritual_ZNK16QPlaybackOptions14playbackIntentEv',
    ))

  def probeSize(self) -> int:
    """
    Calls Qt's 'qsizetype QPlaybackOptions::probeSize() const'.

    Qt's own words: https://doc.qt.io/qt-6/qplaybackoptions.html#probeSize
    """
    #  qsizetype QPlaybackOptions::probeSize() const
    return self.uglySide.call('ritual_ZNK16QPlaybackOptions9probeSizeEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(PlaybackIntent)
  def setPlaybackIntent(self, intent: PlaybackIntent) -> None:
    """
    Calls Qt's 'void QPlaybackOptions::setPlaybackIntent(PlaybackIntent
    intent)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaybackoptions.html#setPlaybackIntent

    Parameters
    ----------

    intent : PlaybackIntent
      Passed on as its number.
    """
    #  void QPlaybackOptions::setPlaybackIntent(PlaybackIntent intent)
    self.uglySide.call(
        'ritual_ZN16QPlaybackOptions17setPlaybackIntentENS_14PlaybackIntent'
        'E',
        intent.value,
    )

  @overload(int)
  def setProbeSize(self, probeSizeBytes: int) -> None:
    """
    Calls Qt's 'void QPlaybackOptions::setProbeSize(qsizetype
    probeSizeBytes)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaybackoptions.html#setProbeSize

    Parameters
    ----------

    probeSizeBytes : int
      Passed on as it is.
    """
    #  void QPlaybackOptions::setProbeSize(qsizetype probeSizeBytes)
    self.uglySide.call(
        'ritual_ZN16QPlaybackOptions12setProbeSizeEx', probeSizeBytes,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, rhs: QPlaybackOptions) -> bool:
    """
    Calls Qt's 'bool operator==(const QPlaybackOptions &lhs, const
    QPlaybackOptions &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaybackoptions.html#operator==

    Parameters
    ----------

    rhs : QPlaybackOptions
      Passed on as a value: Qt reads the C++ QPlaybackOptions, which stays
      Python's own.
    """
    #  bool operator==(const QPlaybackOptions &lhs, const QPlaybackOptions
    #      &rhs)
    return Rituals.call(
        'ritual_ZeqRK16QPlaybackOptionsS1_',
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
  def __ne__(self, rhs: QPlaybackOptions) -> bool:
    """
    Calls Qt's 'bool operator!=(const QPlaybackOptions &lhs, const
    QPlaybackOptions &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaybackoptions.html#operator!=

    Parameters
    ----------

    rhs : QPlaybackOptions
      Passed on as a value: Qt reads the C++ QPlaybackOptions, which stays
      Python's own.
    """
    #  bool operator!=(const QPlaybackOptions &lhs, const QPlaybackOptions
    #      &rhs)
    return Rituals.call(
        'ritual_ZneRK16QPlaybackOptionsS1_',
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

  @overload(THIS)
  def __lt__(self, rhs: QPlaybackOptions) -> bool:
    """
    Calls Qt's 'bool operator<(const QPlaybackOptions &lhs, const
    QPlaybackOptions &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaybackoptions.html#operator<

    Parameters
    ----------

    rhs : QPlaybackOptions
      Passed on as a value: Qt reads the C++ QPlaybackOptions, which stays
      Python's own.
    """
    #  bool operator<(const QPlaybackOptions &lhs, const QPlaybackOptions
    #      &rhs)
    return Rituals.call(
        'ritual_ZltRK16QPlaybackOptionsS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __lt__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __gt__(self, rhs: QPlaybackOptions) -> bool:
    """
    Calls Qt's 'bool operator>(const QPlaybackOptions &lhs, const
    QPlaybackOptions &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaybackoptions.html#operator>

    Parameters
    ----------

    rhs : QPlaybackOptions
      Passed on as a value: Qt reads the C++ QPlaybackOptions, which stays
      Python's own.
    """
    #  bool operator>(const QPlaybackOptions &lhs, const QPlaybackOptions
    #      &rhs)
    return Rituals.call(
        'ritual_ZgtRK16QPlaybackOptionsS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __gt__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __le__(self, rhs: QPlaybackOptions) -> bool:
    """
    Calls Qt's 'bool operator<=(const QPlaybackOptions &lhs, const
    QPlaybackOptions &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaybackoptions.html#operator<=

    Parameters
    ----------

    rhs : QPlaybackOptions
      Passed on as a value: Qt reads the C++ QPlaybackOptions, which stays
      Python's own.
    """
    #  bool operator<=(const QPlaybackOptions &lhs, const QPlaybackOptions
    #      &rhs)
    return Rituals.call(
        'ritual_ZleRK16QPlaybackOptionsS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __le__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ge__(self, rhs: QPlaybackOptions) -> bool:
    """
    Calls Qt's 'bool operator>=(const QPlaybackOptions &lhs, const
    QPlaybackOptions &rhs)'.

    Qt's own words: https://doc.qt.io/qt-6/qplaybackoptions.html#operator>=

    Parameters
    ----------

    rhs : QPlaybackOptions
      Passed on as a value: Qt reads the C++ QPlaybackOptions, which stays
      Python's own.
    """
    #  bool operator>=(const QPlaybackOptions &lhs, const QPlaybackOptions
    #      &rhs)
    return Rituals.call(
        'ritual_ZgeRK16QPlaybackOptionsS1_',
        CuteMixin._valueOf(self), CuteMixin._valueOf(rhs),
    )

  @overload.fallback
  def __ge__(self, *args: object) -> object:
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
    Notes what was given, for Qt's 'QPlaybackOptions::QPlaybackOptions()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaybackoptions.html#QPlaybackOptions
    """
    #  QPlaybackOptions::QPlaybackOptions()
    self._noteCreation(QPlaybackOptions, lambda: Rituals.call(
        'ritual_ZN16QPlaybackOptionsC1Ev',
    ))

  @overload(THIS)
  def __init__(self, a0: QPlaybackOptions) -> None:
    """
    Notes what was given, for Qt's 'QPlaybackOptions::QPlaybackOptions(const
    QPlaybackOptions &a0)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaybackoptions.html#QPlaybackOptions

    Parameters
    ----------

    a0 : QPlaybackOptions
      Passed on as a value: Qt reads the C++ QPlaybackOptions, which stays
      Python's own.
    """
    #  QPlaybackOptions::QPlaybackOptions(const QPlaybackOptions &a0)
    self._noteCreation(QPlaybackOptions, lambda: Rituals.call(
        'ritual_ZN16QPlaybackOptionsC1ERKS_', self._valueOf(a0),
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

  def resetNetworkTimeout(self) -> None:
    """
    Calls Qt's 'void QPlaybackOptions::resetNetworkTimeout()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaybackoptions.html#resetNetworkTimeout
    """
    #  void QPlaybackOptions::resetNetworkTimeout()
    self.uglySide.call('ritual_ZN16QPlaybackOptions19resetNetworkTimeoutEv')

  def resetPlaybackIntent(self) -> None:
    """
    Calls Qt's 'void QPlaybackOptions::resetPlaybackIntent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaybackoptions.html#resetPlaybackIntent
    """
    #  void QPlaybackOptions::resetPlaybackIntent()
    self.uglySide.call('ritual_ZN16QPlaybackOptions19resetPlaybackIntentEv')

  def resetProbeSize(self) -> None:
    """
    Calls Qt's 'void QPlaybackOptions::resetProbeSize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qplaybackoptions.html#resetProbeSize
    """
    #  void QPlaybackOptions::resetProbeSize()
    self.uglySide.call('ritual_ZN16QPlaybackOptions14resetProbeSizeEv')

  @staticmethod
  def networkTimeout(*__, **_) -> Never:
    """
    Qt's 'std::chrono::milliseconds QPlaybackOptions::networkTimeout()
    const': gives a type Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QPlaybackOptions.networkTimeout' has no cute function yet. Qt's "
        "'std::chrono::milliseconds QPlaybackOptions::networkTimeout() "
        "const': gives a type Python has no way to take yet.")

  @staticmethod
  def setNetworkTimeout(*__, **_) -> Never:
    """
    Qt's 'void QPlaybackOptions::setNetworkTimeout(std::chrono::milliseconds
    timeout)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPlaybackOptions.setNetworkTimeout' has no cute function yet. "
        "Qt's 'void "
        "QPlaybackOptions::setNetworkTimeout(std::chrono::milliseconds "
        "timeout)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def swap(*__, **_) -> Never:
    """
    Qt's 'void QPlaybackOptions::swap(QPlaybackOptions &other)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QPlaybackOptions.swap' has no cute function yet. Qt's 'void "
        "QPlaybackOptions::swap(QPlaybackOptions &other)': takes a type "
        "Python has no way to hand over yet.")
