"""
QQmlProfiler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlprofiler_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QQmlProfiler to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject
from . import QQmlProfilerDefinitions, QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QElapsedTimer, QMetaObject, QUrl
  from . import QQmlBoundSignalExpression, QQmlDataBlob, QQmlSourceLocation
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QElapsedTimer = WAIT['QElapsedTimer']
  QQmlBoundSignalExpression = WAIT['QQmlBoundSignalExpression']
  QQmlDataBlob = WAIT['QQmlDataBlob']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlProfiler(QObject, QQmlProfilerDefinitions):
  """
  The cute side of Qt's QQmlProfiler: a plain Python object standing in front
  of one C++ QQmlProfiler.

  It is built on the cute 'QObject', as Qt's QQmlProfiler is built on Qt's
  QObject, and has everything that class has. It is built on the cute
  'QQmlProfilerDefinitions' as well, as Qt's QQmlProfiler is built on Qt's
  QQmlProfilerDefinitions too, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlProfiler that has a ritual and that Python can
  call so far, 11 names in all: 'metaObject', 'tr', 'startBinding',
  'startCompiling', 'startHandlingSignal', 'startCreating', 'updateCreating',
  'startProfiling', 'stopProfiling', 'reportData', 'setTimer'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlProfiler::qt_metacast(const char *a0)': one of Qt's own
    inner workings.
  - Qt's 'int QQmlProfiler::qt_metacall(QMetaObject::Call a0, int a1, void
    **a2)': one of Qt's own inner workings.
  - Qt's 'void QQmlProfiler::dataReady(const QList<QQmlProfilerData> &a0,
    const QQmlProfiler::LocationHash &a1)': takes a type Python has no way to
    hand over yet.

  What has no ritual
  ------------------

  4 of the 19 functions Qt declares: 2 not a gap; 2 a template.

  What to expect
  --------------

  - The C++ QQmlProfiler is created at the first use, not by
    'QQmlProfiler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlProfiler.
  - Qt tells when it has removed the C++ QQmlProfiler. Every call on the cute
    object, and every use of it as an argument, then raises 'RuntimeError',
    and nothing reaches C++.
  - Each name of Qt's QQmlProfiler that has no cute function yet,
    'dataReady', 'endRange', 'id', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QQmlProfiler, each a class in here as in
  #  C++.

  class Location(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlProfiler::Location: a plain Python object
    standing in front of one C++ QQmlProfiler::Location.

    C++ hands a QQmlProfiler::Location around as a copy, so every C++
    QQmlProfiler::Location behind a cute one is Python's own: it is removed,
    by the ritual named in '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QQmlProfiler::Location yet. It can be made from
    Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlProfiler::Location::~Location()': the destructor: Python
      removes its C++ QQmlProfiler::Location by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QQmlProfiler::Location is created at the first use, not by
      'QQmlProfiler::Location(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlProfiler::Location back gives a copy the ritual
      made for Python, in a new cute QQmlProfiler::Location.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QQmlSourceLocation = WAIT['QQmlSourceLocation']
      QUrl = WAIT['QUrl']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlProfiler::Location'

    #  Qt's '~QQmlProfiler::Location()'. Naming it makes this a value class:
    #  Python owns every C++ QQmlProfiler::Location behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN12QQmlProfiler8LocationD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
    @overload(QQmlSourceLocation)
    @overload(QQmlSourceLocation, QUrl)
    def __init__(
        self,
        location: Optional[QQmlSourceLocation] = None,
        url: Optional[QUrl] = None,
    ) -> None:
      """
      Notes what was given, for Qt's 'QQmlProfiler::Location::Location(const
      QQmlSourceLocation &location, const QUrl &url)', which is called at the
      first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlprofiler-location.html#Location

      Parameters
      ----------

      location : Optional[QQmlSourceLocation]
        Passed on as a value: Qt reads the C++ QQmlSourceLocation, which
        stays Python's own. May be left out, as in Qt: a new
        'QQmlSourceLocation()' is then passed on.

      url : Optional[QUrl]
        Passed on as a value: Qt reads the C++ QUrl, which stays Python's
        own. May be left out, as in Qt: a new 'QUrl()' is then passed on.
      """
      #  QQmlProfiler::Location::Location(const QQmlSourceLocation &location,
      #      const QUrl &url)
      if location is None:
        from . import QQmlSourceLocation
        location = QQmlSourceLocation()
      if url is None:
        from ..QtCore import QUrl
        url = QUrl()
      self._noteCreation(QQmlProfiler.Location, lambda: Rituals.call(
          'ritual_ZN12QQmlProfiler8LocationC1ERK18QQmlSourceLocationRK4QUrl',
          self._valueOf(location), self._valueOf(url),
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

  class RefLocation(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlProfiler::RefLocation: a plain Python object
    standing in front of one C++ QQmlProfiler::RefLocation.

    C++ hands a QQmlProfiler::RefLocation around as a copy, so every C++
    QQmlProfiler::RefLocation behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QQmlProfiler::RefLocation that has a ritual and
    that Python can call so far, 4 names in all: 'addref', 'release',
    'isValid', 'isNull'. It can be made from Python, in 6 ways; see
    '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'RefLocation &QQmlProfiler::RefLocation::operator=(const
      RefLocation &other)': assignment: Python binds a name and has no
      operator for it.
    - Qt's 'QQmlProfiler::RefLocation::~RefLocation()': the destructor:
      Python removes its C++ QQmlProfiler::RefLocation by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QQmlProfiler::RefLocation is created at the first use, not by
      'QQmlProfiler::RefLocation(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlProfiler::RefLocation back gives a copy the
      ritual made for Python, in a new cute QQmlProfiler::RefLocation.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QQmlBoundSignalExpression = WAIT['QQmlBoundSignalExpression']
      QQmlDataBlob = WAIT['QQmlDataBlob']
      QUrl = WAIT['QUrl']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlProfiler::RefLocation'

    #  Qt's '~QQmlProfiler::RefLocation()'. Naming it makes this a value
    #  class: Python owns every C++ QQmlProfiler::RefLocation behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN12QQmlProfiler11RefLocationD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def isValid(self) -> bool:
      """
      Calls Qt's 'bool QQmlProfiler::RefLocation::isValid() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlprofiler-reflocation.html#isValid
      """
      #  bool QQmlProfiler::RefLocation::isValid() const
      return self.uglySide.call(
          'ritual_ZNK12QQmlProfiler11RefLocation7isValidEv',
      )

    def isNull(self) -> bool:
      """
      Calls Qt's 'bool QQmlProfiler::RefLocation::isNull() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlprofiler-reflocation.html#isNull
      """
      #  bool QQmlProfiler::RefLocation::isNull() const
      return self.uglySide.call(
          'ritual_ZNK12QQmlProfiler11RefLocation6isNullEv',
      )

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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
      'QQmlProfiler::RefLocation::RefLocation()', which is called at the
      first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlprofiler-reflocation.html#RefLocation
      """
      #  QQmlProfiler::RefLocation::RefLocation()
      self._noteCreation(QQmlProfiler.RefLocation, lambda: Rituals.call(
          'ritual_ZN12QQmlProfiler11RefLocationC1Ev',
      ))

    @overload(WAIT['QV4.Function'])
    @overload(NoneType)
    def __init__(self, ref: Optional[QV4.Function]) -> None:
      """
      Notes what was given, for Qt's
      'QQmlProfiler::RefLocation::RefLocation(QV4::Function *ref)', which is
      called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlprofiler-reflocation.html#RefLocation

      Parameters
      ----------

      ref : Optional[QV4.Function]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  QQmlProfiler::RefLocation::RefLocation(QV4::Function *ref)
      self._noteCreation(QQmlProfiler.RefLocation, lambda: Rituals.call(
          'ritual_ZN12QQmlProfiler11RefLocationC1EPN3QV48FunctionE',
          self._addressOf(ref),
      ))

    @overload(
        WAIT['QV4.ExecutableCompilationUnit'], QUrl,
        WAIT['QV4.CompiledData.Object'], str,
    )
    @overload(WAIT['QV4.ExecutableCompilationUnit'], QUrl, NoneType, str)
    @overload(NoneType, QUrl, WAIT['QV4.CompiledData.Object'], str)
    @overload(NoneType, QUrl, NoneType, str)
    def __init__(
        self,
        ref: Optional[QV4.ExecutableCompilationUnit],
        url: QUrl,
        obj: Optional[QV4.CompiledData.Object],
        type: str,
    ) -> None:
      """
      Notes what was given, for Qt's
      'QQmlProfiler::RefLocation::RefLocation(QV4::ExecutableCompilationUnit
      *ref, const QUrl &url, const QV4::CompiledData::Object *obj, const
      QString &type)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlprofiler-reflocation.html#RefLocation

      Parameters
      ----------

      ref : Optional[QV4.ExecutableCompilationUnit]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      url : QUrl
        Passed on as a value: Qt reads the C++ QUrl, which stays Python's
        own.

      obj : Optional[QV4.CompiledData.Object]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      type : str
        Passed on as it is: a QString is made of it for the call.
      """
      #  QQmlProfiler::RefLocation::RefLocation(QV4::
      #      ExecutableCompilationUnit *ref, const QUrl &url, const
      #      QV4::CompiledData::Object *obj, const QString &type)
      self._noteCreation(QQmlProfiler.RefLocation, lambda: Rituals.call(
          'ritual_ZN12QQmlProfiler11RefLocationC1EPN3QV425ExecutableCompila'
          'tionUnitERK4QUrlPKNS1_12CompiledData6ObjectERK7QString',
          self._addressOf(ref), self._valueOf(url), self._addressOf(obj),
          type,
      ))

    @overload(QQmlBoundSignalExpression)
    def __init__(self, ref: Optional[QQmlBoundSignalExpression]) -> None:
      """
      Notes what was given, for Qt's
      'QQmlProfiler::RefLocation::RefLocation(QQmlBoundSignalExpression
      *ref)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlprofiler-reflocation.html#RefLocation

      Parameters
      ----------

      ref : Optional[QQmlBoundSignalExpression]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  QQmlProfiler::RefLocation::RefLocation(QQmlBoundSignalExpression
      #      *ref)
      self._noteCreation(QQmlProfiler.RefLocation, lambda: Rituals.call(
          'ritual_ZN12QQmlProfiler11RefLocationC1EP25QQmlBoundSignalExpress'
          'ion',
          self._addressOf(ref),
      ))

    @overload(QQmlDataBlob)
    def __init__(self, ref: Optional[QQmlDataBlob]) -> None:
      """
      Notes what was given, for Qt's
      'QQmlProfiler::RefLocation::RefLocation(QQmlDataBlob *ref)', which is
      called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlprofiler-reflocation.html#RefLocation

      Parameters
      ----------

      ref : Optional[QQmlDataBlob]
        Passed on as the address of its C++ object. None is passed on as no
        object.
      """
      #  QQmlProfiler::RefLocation::RefLocation(QQmlDataBlob *ref)
      self._noteCreation(QQmlProfiler.RefLocation, lambda: Rituals.call(
          'ritual_ZN12QQmlProfiler11RefLocationC1EP12QQmlDataBlob',
          self._addressOf(ref),
      ))

    @overload(THIS)
    def __init__(self, other: QQmlProfiler.RefLocation) -> None:
      """
      Notes what was given, for Qt's
      'QQmlProfiler::RefLocation::RefLocation(const RefLocation &other)',
      which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlprofiler-reflocation.html#RefLocation

      Parameters
      ----------

      other : QQmlProfiler.RefLocation
        Passed on as a value: Qt reads the C++ QQmlProfiler::RefLocation,
        which stays Python's own.
      """
      #  QQmlProfiler::RefLocation::RefLocation(const RefLocation &other)
      self._noteCreation(QQmlProfiler.RefLocation, lambda: Rituals.call(
          'ritual_ZN12QQmlProfiler11RefLocationC1ERKS0_',
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

    def addref(self) -> None:
      """
      Calls Qt's 'void QQmlProfiler::RefLocation::addref()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlprofiler-reflocation.html#addref
      """
      #  void QQmlProfiler::RefLocation::addref()
      self.uglySide.call('ritual_ZN12QQmlProfiler11RefLocation6addrefEv')

    def release(self) -> None:
      """
      Calls Qt's 'void QQmlProfiler::RefLocation::release()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmlprofiler-reflocation.html#release
      """
      #  void QQmlProfiler::RefLocation::release()
      self.uglySide.call('ritual_ZN12QQmlProfiler11RefLocation7releaseEv')

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
    Calls Qt's 'QString QQmlProfiler::tr(const char *s, const char *c, int
    n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlprofiler.html#tr

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
    #  QString QQmlProfiler::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN12QQmlProfiler2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlProfiler'

  #  Qt's QQmlProfiler is built on more than one class. The part of a C++
  #  QQmlProfiler that belongs to a class after the first begins somewhere
  #  inside the object, and the ritual named for that class gives where; see
  #  'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QQmlProfilerDefinitions':
          'ritual_cast_QQmlProfiler_QQmlProfilerDefinitions',
  }

  #  A C++ QQmlProfiler Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlProfiler'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlProfiler::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlprofiler.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlProfiler::metaObject() const
    address = self.uglySide.call('ritual_ZNK12QQmlProfiler10metaObjectEv')
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QElapsedTimer)
  def setTimer(self, timer: QElapsedTimer) -> None:
    """
    Calls Qt's 'void QQmlProfiler::setTimer(const QElapsedTimer &timer)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlprofiler.html#setTimer

    Parameters
    ----------

    timer : QElapsedTimer
      Passed on as a value: Qt reads the C++ QElapsedTimer, which stays
      Python's own.
    """
    #  void QQmlProfiler::setTimer(const QElapsedTimer &timer)
    self.uglySide.call(
        'ritual_ZN12QQmlProfiler8setTimerERK13QElapsedTimer',
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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QQmlProfiler::QQmlProfiler()', which is
    called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qqmlprofiler.html#QQmlProfiler
    """
    #  QQmlProfiler::QQmlProfiler()
    self._noteCreation(QQmlProfiler, lambda: Rituals.call(
        'ritual_ZN12QQmlProfilerC1Ev',
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

  @overload(WAIT['QV4.Function'])
  @overload(NoneType)
  def startBinding(self, function: Optional[QV4.Function]) -> None:
    """
    Calls Qt's 'void QQmlProfiler::startBinding(QV4::Function *function)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlprofiler.html#startBinding

    Parameters
    ----------

    function : Optional[QV4.Function]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlProfiler::startBinding(QV4::Function *function)
    self.uglySide.call(
        'ritual_ZN12QQmlProfiler12startBindingEPN3QV48FunctionE',
        self._addressOf(function),
    )

  @overload(QQmlDataBlob)
  @overload(NoneType)
  def startCompiling(self, blob: Optional[QQmlDataBlob]) -> None:
    """
    Calls Qt's 'void QQmlProfiler::startCompiling(QQmlDataBlob *blob)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlprofiler.html#startCompiling

    Parameters
    ----------

    blob : Optional[QQmlDataBlob]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlProfiler::startCompiling(QQmlDataBlob *blob)
    self.uglySide.call(
        'ritual_ZN12QQmlProfiler14startCompilingEP12QQmlDataBlob',
        self._addressOf(blob),
    )

  @overload(QQmlBoundSignalExpression)
  @overload(NoneType)
  def startHandlingSignal(
      self,
      expression: Optional[QQmlBoundSignalExpression],
  ) -> None:
    """
    Calls Qt's 'void
    QQmlProfiler::startHandlingSignal(QQmlBoundSignalExpression
    *expression)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlprofiler.html#startHandlingSignal

    Parameters
    ----------

    expression : Optional[QQmlBoundSignalExpression]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlProfiler::startHandlingSignal(QQmlBoundSignalExpression
    #      *expression)
    self.uglySide.call(
        'ritual_ZN12QQmlProfiler19startHandlingSignalEP25QQmlBoundSignalExp'
        'ression',
        self._addressOf(expression),
    )

  @overload(WAIT['QV4.CompiledData.Object'])
  @overload(NoneType)
  def startCreating(self, obj: Optional[QV4.CompiledData.Object]) -> None:
    """
    Calls Qt's 'void QQmlProfiler::startCreating(const
    QV4::CompiledData::Object *obj)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlprofiler.html#startCreating

    Parameters
    ----------

    obj : Optional[QV4.CompiledData.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlProfiler::startCreating(const QV4::CompiledData::Object *obj)
    self.uglySide.call(
        'ritual_ZN12QQmlProfiler13startCreatingEPKN3QV412CompiledData6Objec'
        'tE',
        self._addressOf(obj),
    )

  @overload(
      WAIT['QV4.CompiledData.Object'], WAIT['QV4.ExecutableCompilationUnit'],
      QUrl, str,
  )
  @overload(WAIT['QV4.CompiledData.Object'], NoneType, QUrl, str)
  @overload(NoneType, WAIT['QV4.ExecutableCompilationUnit'], QUrl, str)
  @overload(NoneType, NoneType, QUrl, str)
  def updateCreating(
      self,
      obj: Optional[QV4.CompiledData.Object],
      ref: Optional[QV4.ExecutableCompilationUnit],
      url: QUrl,
      type: str,
  ) -> None:
    """
    Calls Qt's 'void QQmlProfiler::updateCreating(const
    QV4::CompiledData::Object *obj, QV4::ExecutableCompilationUnit *ref,
    const QUrl &url, const QString &type)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlprofiler.html#updateCreating

    Parameters
    ----------

    obj : Optional[QV4.CompiledData.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    ref : Optional[QV4.ExecutableCompilationUnit]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    url : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    type : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlProfiler::updateCreating(const QV4::CompiledData::Object
    #      *obj, QV4::ExecutableCompilationUnit *ref, const QUrl &url, const
    #      QString &type)
    self.uglySide.call(
        'ritual_ZN12QQmlProfiler14updateCreatingEPKN3QV412CompiledData6Obje'
        'ctEPNS0_25ExecutableCompilationUnitERK4QUrlRK7QString',
        self._addressOf(obj), self._addressOf(ref), self._valueOf(url), type,
    )

  @overload(int)
  def startProfiling(self, features: int) -> None:
    """
    Calls Qt's 'void QQmlProfiler::startProfiling(quint64 features)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlprofiler.html#startProfiling

    Parameters
    ----------

    features : int
      Passed on as it is.
    """
    #  void QQmlProfiler::startProfiling(quint64 features)
    self.uglySide.call('ritual_ZN12QQmlProfiler14startProfilingEy', features)

  def stopProfiling(self) -> None:
    """
    Calls Qt's 'void QQmlProfiler::stopProfiling()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlprofiler.html#stopProfiling
    """
    #  void QQmlProfiler::stopProfiling()
    self.uglySide.call('ritual_ZN12QQmlProfiler13stopProfilingEv')

  def reportData(self) -> None:
    """
    Calls Qt's 'void QQmlProfiler::reportData()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlprofiler.html#reportData
    """
    #  void QQmlProfiler::reportData()
    self.uglySide.call('ritual_ZN12QQmlProfiler10reportDataEv')

  @staticmethod
  def dataReady(*__, **_) -> Never:
    """
    Qt's 'void QQmlProfiler::dataReady(const QList<QQmlProfilerData> &a0,
    const QQmlProfiler::LocationHash &a1)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQmlProfiler.dataReady' has no cute function yet. Qt's 'void "
        "QQmlProfiler::dataReady(const QList<QQmlProfilerData> &a0, const "
        "QQmlProfiler::LocationHash &a1)': takes a type Python has no way "
        "to hand over yet.")

  @staticmethod
  def endRange(*__, **_) -> Never:
    """
    Qt's 'QQmlProfiler::endRange': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QQmlProfiler.endRange' has no cute function yet. Qt's "
        "'QQmlProfiler::endRange': a template: a pattern and no single "
        "function.")

  @staticmethod
  def id(*__, **_) -> Never:
    """
    Qt's 'QQmlProfiler::id': a template: a pattern and no single function.
    """
    raise NotImplementedError(
        "'QQmlProfiler.id' has no cute function yet. Qt's "
        "'QQmlProfiler::id': a template: a pattern and no single function.")
