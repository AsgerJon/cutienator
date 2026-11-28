"""
QV4::Profiling::Profiler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4profiling_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QV4::Profiling::Profiler to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QElapsedTimer, QMetaObject
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QElapsedTimer = WAIT['QElapsedTimer']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class Profiler(QObject):
  """
  The cute side of Qt's QV4::Profiling::Profiler: a plain Python object
  standing in front of one C++ QV4::Profiling::Profiler.

  It is built on the cute 'QObject', as Qt's QV4::Profiling::Profiler is
  built on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QV4::Profiling::Profiler that has a ritual and that
  Python can call so far, 8 names in all: 'metaObject', 'tr', 'trackAlloc',
  'trackDealloc', 'stopProfiling', 'startProfiling', 'reportData',
  'setTimer'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QV4::Profiling::Profiler::qt_metacast(const char *a0)': one
    of Qt's own inner workings.
  - Qt's 'int QV4::Profiling::Profiler::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'void QV4::Profiling::Profiler::dataReady(const
    QV4::Profiling::FunctionLocationHash &a0, const
    QList<QV4::Profiling::FunctionCallProperties> &a1, const
    QList<QV4::Profiling::MemoryAllocationProperties> &a2)': takes a type
    Python has no way to hand over yet.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QV4::Profiling::Profiler is created at the first use, not by
    'QV4::Profiling::Profiler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::Profiling::Profiler.
  - Qt tells when it has removed the C++ QV4::Profiling::Profiler. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QV4::Profiling::Profiler that has no cute function yet,
    'dataReady', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The classes Qt writes inside QV4::Profiling::Profiler, each a class in
  #  here as in C++.

  class SentMarker(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QV4::Profiling::Profiler::SentMarker: a plain
    Python object standing in front of one C++
    QV4::Profiling::Profiler::SentMarker.

    C++ hands a QV4::Profiling::Profiler::SentMarker around as a copy, so
    every C++ QV4::Profiling::Profiler::SentMarker behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    Every function of Qt's QV4::Profiling::Profiler::SentMarker that has a
    ritual and that Python can call so far, 2 names in all: 'setFunction',
    'isValid'. It can be made from Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QV4::Profiling::Profiler::SentMarker::~SentMarker()': the
      destructor: Python removes its C++ QV4::Profiling::Profiler::SentMarker
      by it, and has no other use for it.
    - Qt's 'SentMarker &QV4::Profiling::Profiler::SentMarker::operator=(const
      SentMarker &other)': assignment: Python binds a name and has no
      operator for it.

    What to expect
    --------------

    - The C++ QV4::Profiling::Profiler::SentMarker is created at the first
      use, not by 'QV4::Profiling::Profiler::SentMarker(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QV4::Profiling::Profiler::SentMarker back gives a
      copy the ritual made for Python, in a new cute
      QV4::Profiling::Profiler::SentMarker.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QV4::Profiling::Profiler::SentMarker'

    #  Qt's '~QV4::Profiling::Profiler::SentMarker()'. Naming it makes this a
    #  value class: Python owns every C++
    #  QV4::Profiling::Profiler::SentMarker behind a cute one, and removes it
    #  by this ritual.
    __delete_ritual__ = 'ritual_ZN3QV49Profiling8Profiler10SentMarkerD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def isValid(self) -> bool:
      """
      Calls Qt's 'bool QV4::Profiling::Profiler::SentMarker::isValid()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-profiling-profiler-sentmarker.html#isValid
      """
      #  bool QV4::Profiling::Profiler::SentMarker::isValid() const
      return self.uglySide.call(
          'ritual_ZNK3QV49Profiling8Profiler10SentMarker7isValidEv',
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(WAIT['QV4.Function'])
    @overload(NoneType)
    def setFunction(self, function: Optional[QV4.Function]) -> None:
      """
      Calls Qt's 'void
      QV4::Profiling::Profiler::SentMarker::setFunction(Function *function)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-profiling-profiler-sentmarker.html

      Parameters
      ----------

      function : Optional[QV4.Function]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  void QV4::Profiling::Profiler::SentMarker::setFunction(Function
      #      *function)
      self.uglySide.call(
          'ritual_ZN3QV49Profiling8Profiler10SentMarker11setFunctionEPNS_8F'
          'unctionE',
          self._addressOf(function),
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QV4::Profiling::Profiler::SentMarker::SentMarker()', which is called
      at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-profiling-profiler-sentmarker.html
      """
      #  QV4::Profiling::Profiler::SentMarker::SentMarker()
      self._noteCreation(Profiler.SentMarker, lambda: Rituals.call(
          'ritual_ZN3QV49Profiling8Profiler10SentMarkerC1Ev',
      ))

    @overload(THIS)
    def __init__(self, other: Profiler.SentMarker) -> None:
      """
      Notes what was given, for Qt's
      'QV4::Profiling::Profiler::SentMarker::SentMarker(const SentMarker
      &other)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qv4-profiling-profiler-sentmarker.html

      Parameters
      ----------

      other : Profiler.SentMarker
        Passed on as a value: Qt reads the C++
        QV4::Profiling::Profiler::SentMarker, which stays Python's own.
      """
      #  QV4::Profiling::Profiler::SentMarker::SentMarker(const SentMarker
      #      &other)
      self._noteCreation(Profiler.SentMarker, lambda: Rituals.call(
          'ritual_ZN3QV49Profiling8Profiler10SentMarkerC1ERKS2_',
          self._valueOf(other),
      ))

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  DOMAIN SPECIFIC  # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  OPTIONAL METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  REQUIRED METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PARENT METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  PUBLIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    Calls Qt's 'QString QV4::Profiling::Profiler::tr(const char *s, const
    char *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qv4-profiling-profiler.html#tr

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
    #  QString QV4::Profiling::Profiler::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN3QV49Profiling8Profiler2trEPKcS3_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Profiling::Profiler'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QV4::Profiling::Profiler::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-profiling-profiler.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QV4::Profiling::Profiler::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK3QV49Profiling8Profiler10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QElapsedTimer)
  def setTimer(self, timer: QElapsedTimer) -> None:
    """
    Calls Qt's 'void QV4::Profiling::Profiler::setTimer(const QElapsedTimer
    &timer)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-profiling-profiler.html#setTimer

    Parameters
    ----------

    timer : QElapsedTimer
      Passed on as a value: Qt reads the C++ QElapsedTimer, which stays
      Python's own.
    """
    #  void QV4::Profiling::Profiler::setTimer(const QElapsedTimer &timer)
    self.uglySide.call(
        'ritual_ZN3QV49Profiling8Profiler8setTimerERK13QElapsedTimer',
        self._valueOf(timer),
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

  @overload(WAIT['QV4.ExecutionEngine'])
  @overload(NoneType)
  def __init__(self, engine: Optional[QV4.ExecutionEngine]) -> None:
    """
    Notes what was given, for Qt's
    'QV4::Profiling::Profiler::Profiler(QV4::ExecutionEngine *engine)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-profiling-profiler.html#Profiler

    Parameters
    ----------

    engine : Optional[QV4.ExecutionEngine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QV4::Profiling::Profiler::Profiler(QV4::ExecutionEngine *engine)
    self._noteCreation(Profiler, lambda: Rituals.call(
        'ritual_ZN3QV49Profiling8ProfilerC1EPNS_15ExecutionEngineE',
        self._addressOf(engine),
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

  @overload(int, QV4.Profiling.MemoryType)
  def trackAlloc(self, size: int, type: QV4.Profiling.MemoryType) -> bool:
    """
    Calls Qt's 'bool QV4::Profiling::Profiler::trackAlloc(size_t size,
    MemoryType type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-profiling-profiler.html#trackAlloc

    Parameters
    ----------

    size : int
      Passed on as it is.

    type : QV4.Profiling.MemoryType
      Passed on as its number.
    """
    #  bool QV4::Profiling::Profiler::trackAlloc(size_t size, MemoryType
    #      type)
    return self.uglySide.call(
        'ritual_ZN3QV49Profiling8Profiler10trackAllocEmNS0_10MemoryTypeE',
        size, type.value,
    )

  @overload(int, QV4.Profiling.MemoryType)
  def trackDealloc(self, size: int, type: QV4.Profiling.MemoryType) -> bool:
    """
    Calls Qt's 'bool QV4::Profiling::Profiler::trackDealloc(size_t size,
    MemoryType type)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-profiling-profiler.html#trackDealloc

    Parameters
    ----------

    size : int
      Passed on as it is.

    type : QV4.Profiling.MemoryType
      Passed on as its number.
    """
    #  bool QV4::Profiling::Profiler::trackDealloc(size_t size, MemoryType
    #      type)
    return self.uglySide.call(
        'ritual_ZN3QV49Profiling8Profiler12trackDeallocEmNS0_10MemoryTypeE',
        size, type.value,
    )

  def stopProfiling(self) -> None:
    """
    Calls Qt's 'void QV4::Profiling::Profiler::stopProfiling()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-profiling-profiler.html#stopProfiling
    """
    #  void QV4::Profiling::Profiler::stopProfiling()
    self.uglySide.call('ritual_ZN3QV49Profiling8Profiler13stopProfilingEv')

  @overload(int)
  def startProfiling(self, features: int) -> None:
    """
    Calls Qt's 'void QV4::Profiling::Profiler::startProfiling(quint64
    features)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-profiling-profiler.html#startProfiling

    Parameters
    ----------

    features : int
      Passed on as it is.
    """
    #  void QV4::Profiling::Profiler::startProfiling(quint64 features)
    self.uglySide.call(
        'ritual_ZN3QV49Profiling8Profiler14startProfilingEy', features,
    )

  def reportData(self) -> None:
    """
    Calls Qt's 'void QV4::Profiling::Profiler::reportData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-profiling-profiler.html#reportData
    """
    #  void QV4::Profiling::Profiler::reportData()
    self.uglySide.call('ritual_ZN3QV49Profiling8Profiler10reportDataEv')

  @staticmethod
  def dataReady(*__, **_) -> Never:
    """
    Qt's 'void QV4::Profiling::Profiler::dataReady(const
    QV4::Profiling::FunctionLocationHash &a0, const
    QList<QV4::Profiling::FunctionCallProperties> &a1, const
    QList<QV4::Profiling::MemoryAllocationProperties> &a2)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QV4.Profiling.Profiler.dataReady' has no cute function yet. Qt's "
        "'void QV4::Profiling::Profiler::dataReady(const "
        "QV4::Profiling::FunctionLocationHash &a0, const "
        "QList<QV4::Profiling::FunctionCallProperties> &a1, const "
        "QList<QV4::Profiling::MemoryAllocationProperties> &a2)': takes a "
        "type Python has no way to hand over yet.")
