"""
QSample binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtMultimedia/6.12.0/QtMultimedia/private/qsamplecache_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QSample to be private: it declares the class in a header it calls
#  private. cutienator does not care. Qt hands objects of the class out all
#  the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QUrl
  from . import QAudioFormat, QSampleCache
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QAudioFormat = WAIT['QAudioFormat']
  QByteArray = WAIT['QByteArray']
  QSampleCache = WAIT['QSampleCache']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QSample(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QSample: a plain Python object standing in front of
  one C++ QSample.

  C++ hands a QSample around as a copy, so every C++ QSample behind a cute
  one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QSample that has a ritual and that Python can call
  so far, 7 names in all: 'state', 'data', 'format', 'frameCount',
  'setError', 'setData', 'clearParent'. It can be made from Python, in 3
  ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QSample::~QSample()': the destructor: Python removes its C++
    QSample by it, and has no other use for it.
  - Qt's 'QSpan<const float> QSample::dataAsFloatSpan() const': gives a type
    Python has no way to take yet.
  - Qt's 'QSample::QSample(QUrl url, QSampleCache *parent,
    std::optional<SampleRate> targetSampleRate)': takes a type Python has no
    way to hand over yet.

  What to expect
  --------------

  - The C++ QSample is created at the first use, not by 'QSample(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QSample back gives a copy the ritual made for Python,
    in a new cute QSample.
  - Each name of Qt's QSample that has no cute function yet,
    'dataAsFloatSpan', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  #  The enums Qt writes inside QSample, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class State(CuteNum):
    """The enum 'QSample::State' of Qt, with the 3 names Qt gives in it."""

    Creating = Kee[int](0)
    Error = Kee[int](1)
    Ready = Kee[int](2)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QSample'

  #  Qt's '~QSample()'. Naming it makes this a value class: Python owns every
  #  C++ QSample behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN7QSampleD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def state(self) -> State:
    """
    Calls Qt's 'State QSample::state() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsample.html#state

    Returns
    -------

    State
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'State(number)' gives.
    """
    #  State QSample::state() const
    return QSample.State(self.uglySide.call('ritual_ZNK7QSample5stateEv'))

  def data(self) -> QByteArray:
    """
    Calls Qt's 'const QByteArray &QSample::data() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsample.html#data

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  const QByteArray &QSample::data() const
    address = self.uglySide.call('ritual_ZNK7QSample4dataEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def format(self) -> QAudioFormat:
    """
    Calls Qt's 'const QAudioFormat &QSample::format() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsample.html#format

    Returns
    -------

    QAudioFormat
      A new cute QAudioFormat around the copy Qt gave back. Python owns it.
    """
    #  const QAudioFormat &QSample::format() const
    address = self.uglySide.call('ritual_ZNK7QSample6formatEv')
    from . import QAudioFormat
    return QAudioFormat._cuteOwning(address)

  def frameCount(self) -> int:
    """
    Calls Qt's 'qsizetype QSample::frameCount() const'.

    Qt's own words: https://doc.qt.io/qt-6/qsample.html#frameCount
    """
    #  qsizetype QSample::frameCount() const
    return self.uglySide.call('ritual_ZNK7QSample10frameCountEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def setError(self) -> None:
    """
    Calls Qt's 'void QSample::setError()'.

    Qt's own words: https://doc.qt.io/qt-6/qsample.html#setError
    """
    #  void QSample::setError()
    self.uglySide.call('ritual_ZN7QSample8setErrorEv')

  @overload(QByteArray, QAudioFormat)
  def setData(self, a0: QByteArray, a1: QAudioFormat) -> None:
    """
    Calls Qt's 'void QSample::setData(QByteArray a0, QAudioFormat a1)'.

    Qt's own words: https://doc.qt.io/qt-6/qsample.html#setData

    Parameters
    ----------

    a0 : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    a1 : QAudioFormat
      Passed on as a value: Qt reads the C++ QAudioFormat, which stays
      Python's own.
    """
    #  void QSample::setData(QByteArray a0, QAudioFormat a1)
    self.uglySide.call(
        'ritual_ZN7QSample7setDataE10QByteArray12QAudioFormat',
        self._valueOf(a0), self._valueOf(a1),
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

  @overload(QUrl, QSampleCache)
  @overload(QUrl, NoneType)
  def __init__(self, url: QUrl, parent: Optional[QSampleCache]) -> None:
    """
    Notes what was given, for Qt's 'QSample::QSample(QUrl url, QSampleCache
    *parent)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsample.html#QSample

    Parameters
    ----------

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    parent : Optional[QSampleCache]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QSample::QSample(QUrl url, QSampleCache *parent)
    self._noteCreation(QSample, lambda: Rituals.call(
        'ritual_ZN7QSampleC1E4QUrlP12QSampleCache',
        self._valueOf(url), self._addressOf(parent),
    ))

  @overload(QByteArray, QAudioFormat)
  def __init__(self, data: QByteArray, format: QAudioFormat) -> None:
    """
    Notes what was given, for Qt's 'QSample::QSample(QByteArray data,
    QAudioFormat format)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsample.html#QSample

    Parameters
    ----------

    data : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    format : QAudioFormat
      Passed on as a value: Qt reads the C++ QAudioFormat, which stays
      Python's own.
    """
    #  QSample::QSample(QByteArray data, QAudioFormat format)
    self._noteCreation(QSample, lambda: Rituals.call(
        'ritual_ZN7QSampleC1E10QByteArray12QAudioFormat',
        self._valueOf(data), self._valueOf(format),
    ))

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QSample::QSample()', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qsample.html#QSample
    """
    #  QSample::QSample()
    self._noteCreation(QSample, lambda: Rituals.call(
        'ritual_ZN7QSampleC1Ev',
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

  def clearParent(self) -> None:
    """
    Calls Qt's 'void QSample::clearParent()'.

    Qt's own words: https://doc.qt.io/qt-6/qsample.html#clearParent
    """
    #  void QSample::clearParent()
    self.uglySide.call('ritual_ZN7QSample11clearParentEv')

  @staticmethod
  def dataAsFloatSpan(*__, **_) -> Never:
    """
    Qt's 'QSpan<const float> QSample::dataAsFloatSpan() const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QSample.dataAsFloatSpan' has no cute function yet. Qt's "
        "'QSpan<const float> QSample::dataAsFloatSpan() const': gives a "
        "type Python has no way to take yet.")
