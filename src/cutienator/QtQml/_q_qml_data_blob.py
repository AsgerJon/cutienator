"""
QQmlDataBlob binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmldatablob_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QQmlDataBlob to be private: it declares the class in a header it
#  calls private. cutienator does not care. Qt hands objects of the class out
#  all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList
from . import QQmlJS, QQmlPrivate
from ..QtNetwork import QNetworkReply

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QDateTime, QString, QUrl
  from . import QQmlError, QQmlTypeLoader
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlError = WAIT['QQmlError']
  QQmlTypeLoader = WAIT['QQmlTypeLoader']
  QUrl = WAIT['QUrl']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlDataBlob(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlDataBlob: a plain Python object standing in front
  of one C++ QQmlDataBlob.

  What exists
  -----------

  Every function of Qt's QQmlDataBlob that has a ritual and that Python can
  call so far, 32 names in all: 'startLoading', 'typeLoader',
  'resetTypeLoader', 'type', 'status', 'isNull', 'isLoading', 'isWaiting',
  'isComplete', 'isError', 'isCompleteOrError', 'isAsync', 'progress', 'url',
  'urlString', 'finalUrl', 'finalUrlString', 'errors', 'setError',
  'dataReceived', 'initializeFromCachedUnit', 'done', 'networkError',
  'allDependenciesDone', 'downloadProgressChanged', 'completed', 'tryDone',
  'cancelAllWaitingFor', 'notifyAllWaitingOnMe', 'setStatus', 'setIsAsync',
  'setProgress'. It can be made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlDataBlob::~QQmlDataBlob()': the destructor: Python never
    removes a C++ QQmlDataBlob.
  - Qt's 'void QQmlDataBlob::addDependency(const QQmlDataBlob::Ptr &a0)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QQmlDataBlob::dependencyError(const QQmlDataBlob::Ptr &a0)':
    takes a type Python has no way to hand over yet.
  - Qt's 'void QQmlDataBlob::dependencyComplete(const QQmlDataBlob::Ptr
    &a0)': takes a type Python has no way to hand over yet.
  - Qt's 'void QQmlDataBlob::notifyComplete(const QQmlDataBlob::Ptr &a0)':
    takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 45 functions Qt declares: 4 a template.

  What to expect
  --------------

  - The C++ QQmlDataBlob is created at the first use, not by
    'QQmlDataBlob(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlDataBlob.
  - Each name of Qt's QQmlDataBlob that has no cute function yet,
    'addDependency', 'assertEngineThread', 'assertEngineThreadIfRunning',
    'assertTypeLoaderThread', 'assertTypeLoaderThreadIfRunning',
    'dependencyComplete', 'dependencyError', 'notifyComplete', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQmlDataBlob, each a class in here as in C++,
  #  and the names Qt has for the combinations of its flags enums.

  class Status(CuteNum):
    """
    The enum 'QQmlDataBlob::Status' of Qt, with the 6 names Qt gives in it.
    """

    Null = Kee[int](0)
    Loading = Kee[int](1)
    WaitingForDependencies = Kee[int](2)
    ResolvingDependencies = Kee[int](3)
    Complete = Kee[int](4)
    Error = Kee[int](5)

  class Type(CuteNum):
    """
    The enum 'QQmlDataBlob::Type' of Qt, with the 3 names Qt gives in it.
    """

    QmlFile = Kee[int](0)
    JavaScriptFile = Kee[int](1)
    QmldirFile = Kee[int](2)

  #  The classes Qt writes inside QQmlDataBlob, each a class in here as in
  #  C++.

  class SourceCodeData(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QQmlDataBlob::SourceCodeData: a plain Python object
    standing in front of one C++ QQmlDataBlob::SourceCodeData.

    C++ hands a QQmlDataBlob::SourceCodeData around as a copy, so every C++
    QQmlDataBlob::SourceCodeData behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QQmlDataBlob::SourceCodeData that has a ritual and
    that Python can call so far, 6 names in all: 'readAll',
    'sourceTimeStamp', 'checksum', 'exists', 'isCacheable', 'isValid'. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QQmlDataBlob::SourceCodeData::~SourceCodeData()': the destructor:
      Python removes its C++ QQmlDataBlob::SourceCodeData by it, and has no
      other use for it.

    What to expect
    --------------

    - The C++ QQmlDataBlob::SourceCodeData is created at the first use, not
      by 'QQmlDataBlob::SourceCodeData(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QQmlDataBlob::SourceCodeData back gives a copy the
      ritual made for Python, in a new cute QQmlDataBlob::SourceCodeData.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QString = WAIT['QString']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QQmlDataBlob::SourceCodeData'

    #  Qt's '~QQmlDataBlob::SourceCodeData()'. Naming it makes this a value
    #  class: Python owns every C++ QQmlDataBlob::SourceCodeData behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN12QQmlDataBlob14SourceCodeDataD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload(QString)
    @overload(NoneType)
    def readAll(self, error: Optional[QString]) -> str:
      """
      Calls Qt's 'QString QQmlDataBlob::SourceCodeData::readAll(QString
      *error) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmldatablob-sourcecodedata.html#readAll

      Parameters
      ----------

      error : Optional[QString]
        Passed on as the address of its C++ object. None is passed on as no
        object.

      Returns
      -------

      str
        The text Qt gave back.
      """
      #  QString QQmlDataBlob::SourceCodeData::readAll(QString *error) const
      return self.uglySide.call(
          'ritual_ZNK12QQmlDataBlob14SourceCodeData7readAllEP7QString',
          self._addressOf(error),
      )

    def sourceTimeStamp(self) -> QDateTime:
      """
      Calls Qt's 'QDateTime QQmlDataBlob::SourceCodeData::sourceTimeStamp()
      const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmldatablob-sourcecodedata.html#sourceTimeStamp

      Returns
      -------

      QDateTime
        A new cute QDateTime around the copy Qt gave back. Python owns it.
      """
      #  QDateTime QQmlDataBlob::SourceCodeData::sourceTimeStamp() const
      address = self.uglySide.call(
          'ritual_ZNK12QQmlDataBlob14SourceCodeData15sourceTimeStampEv',
      )
      from ..QtCore import QDateTime
      return QDateTime._cuteOwning(address)

    def checksum(self) -> QByteArray:
      """
      Calls Qt's 'QByteArray QQmlDataBlob::SourceCodeData::checksum() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmldatablob-sourcecodedata.html#checksum

      Returns
      -------

      QByteArray
        A new cute QByteArray around the copy Qt gave back. Python owns it.
      """
      #  QByteArray QQmlDataBlob::SourceCodeData::checksum() const
      address = self.uglySide.call(
          'ritual_ZNK12QQmlDataBlob14SourceCodeData8checksumEv',
      )
      from ..QtCore import QByteArray
      return QByteArray._cuteOwning(address)

    def exists(self) -> bool:
      """
      Calls Qt's 'bool QQmlDataBlob::SourceCodeData::exists() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmldatablob-sourcecodedata.html#exists
      """
      #  bool QQmlDataBlob::SourceCodeData::exists() const
      return self.uglySide.call(
          'ritual_ZNK12QQmlDataBlob14SourceCodeData6existsEv',
      )

    def isCacheable(self) -> bool:
      """
      Calls Qt's 'bool QQmlDataBlob::SourceCodeData::isCacheable() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmldatablob-sourcecodedata.html#isCacheable
      """
      #  bool QQmlDataBlob::SourceCodeData::isCacheable() const
      return self.uglySide.call(
          'ritual_ZNK12QQmlDataBlob14SourceCodeData11isCacheableEv',
      )

    def isValid(self) -> bool:
      """
      Calls Qt's 'bool QQmlDataBlob::SourceCodeData::isValid() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qqmldatablob-sourcecodedata.html#isValid
      """
      #  bool QQmlDataBlob::SourceCodeData::isValid() const
      return self.uglySide.call(
          'ritual_ZNK12QQmlDataBlob14SourceCodeData7isValidEv',
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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlDataBlob'

  #  A C++ QQmlDataBlob Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlDataBlob'

  #  The functions Qt calls itself that QQmlDataBlob is the first to declare
  #  and that cannot be handed to Python yet, each as Qt declares it. A class
  #  of a program that writes one of them anew is refused, since Qt would
  #  never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'dependencyError': (
          'void QQmlDataBlob::dependencyError(const QQmlDataBlob::Ptr &)',
      ),
      'dependencyComplete': (
          'void QQmlDataBlob::dependencyComplete(const QQmlDataBlob::Ptr &)',
      ),
  }

  #  The functions Qt calls itself that QQmlDataBlob is the first to declare.
  #  A class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'dataReceived': (
          ('_ZN12QQmlDataBlob12dataReceivedERKNS_14SourceCodeDataE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtQml:QQmlDataBlob.SourceCodeData'),
           )),
      ),
      'initializeFromCachedUnit': (
          ('_ZN12QQmlDataBlob24initializeFromCachedUnitEPKN11QQmlPrivate13C'
           'achedQmlUnitE',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtQml:QQmlPrivate.CachedQmlUnit'),
           )),
      ),
      'done': (
          ('_ZN12QQmlDataBlob4doneEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'networkError': (
          ('_ZN12QQmlDataBlob12networkErrorEN13QNetworkReply12NetworkErrorE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtNetwork:QNetworkReply.NetworkError'),
           )),
      ),
      'allDependenciesDone': (
          ('_ZN12QQmlDataBlob19allDependenciesDoneEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'downloadProgressChanged': (
          ('_ZN12QQmlDataBlob23downloadProgressChangedEd',
           ('nothing', 'nothing', ''),
           (
               ('double', 'number', ''),
           )),
      ),
      'completed': (
          ('_ZN12QQmlDataBlob9completedEv',
           ('nothing', 'nothing', ''),
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

  def typeLoader(self) -> Optional[QQmlTypeLoader]:
    """
    Calls Qt's 'QQmlTypeLoader *QQmlDataBlob::typeLoader() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldatablob.html#typeLoader

    Returns
    -------

    Optional[QQmlTypeLoader]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlTypeLoader *QQmlDataBlob::typeLoader() const
    address = self.uglySide.call('ritual_ZNK12QQmlDataBlob10typeLoaderEv')
    from . import QQmlTypeLoader
    return QQmlTypeLoader._cuteAt(address)

  def type(self) -> Type:
    """
    Calls Qt's 'Type QQmlDataBlob::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldatablob.html#type

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type QQmlDataBlob::type() const
    return QQmlDataBlob.Type(self.uglySide.call(
        'ritual_ZNK12QQmlDataBlob4typeEv',
    ))

  def status(self) -> Status:
    """
    Calls Qt's 'Status QQmlDataBlob::status() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldatablob.html#status

    Returns
    -------

    Status
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Status(number)' gives.
    """
    #  Status QQmlDataBlob::status() const
    return QQmlDataBlob.Status(self.uglySide.call(
        'ritual_ZNK12QQmlDataBlob6statusEv',
    ))

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QQmlDataBlob::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldatablob.html#isNull
    """
    #  bool QQmlDataBlob::isNull() const
    return self.uglySide.call('ritual_ZNK12QQmlDataBlob6isNullEv')

  def isLoading(self) -> bool:
    """
    Calls Qt's 'bool QQmlDataBlob::isLoading() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldatablob.html#isLoading
    """
    #  bool QQmlDataBlob::isLoading() const
    return self.uglySide.call('ritual_ZNK12QQmlDataBlob9isLoadingEv')

  def isWaiting(self) -> bool:
    """
    Calls Qt's 'bool QQmlDataBlob::isWaiting() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldatablob.html#isWaiting
    """
    #  bool QQmlDataBlob::isWaiting() const
    return self.uglySide.call('ritual_ZNK12QQmlDataBlob9isWaitingEv')

  def isComplete(self) -> bool:
    """
    Calls Qt's 'bool QQmlDataBlob::isComplete() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldatablob.html#isComplete
    """
    #  bool QQmlDataBlob::isComplete() const
    return self.uglySide.call('ritual_ZNK12QQmlDataBlob10isCompleteEv')

  def isError(self) -> bool:
    """
    Calls Qt's 'bool QQmlDataBlob::isError() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldatablob.html#isError
    """
    #  bool QQmlDataBlob::isError() const
    return self.uglySide.call('ritual_ZNK12QQmlDataBlob7isErrorEv')

  def isCompleteOrError(self) -> bool:
    """
    Calls Qt's 'bool QQmlDataBlob::isCompleteOrError() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldatablob.html#isCompleteOrError
    """
    #  bool QQmlDataBlob::isCompleteOrError() const
    return self.uglySide.call(
        'ritual_ZNK12QQmlDataBlob17isCompleteOrErrorEv',
    )

  def isAsync(self) -> bool:
    """
    Calls Qt's 'bool QQmlDataBlob::isAsync() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldatablob.html#isAsync
    """
    #  bool QQmlDataBlob::isAsync() const
    return self.uglySide.call('ritual_ZNK12QQmlDataBlob7isAsyncEv')

  def progress(self) -> float:
    """
    Calls Qt's 'qreal QQmlDataBlob::progress() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldatablob.html#progress
    """
    #  qreal QQmlDataBlob::progress() const
    return self.uglySide.call('ritual_ZNK12QQmlDataBlob8progressEv')

  def url(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQmlDataBlob::url() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldatablob.html#url

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQmlDataBlob::url() const
    address = self.uglySide.call('ritual_ZNK12QQmlDataBlob3urlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def urlString(self) -> str:
    """
    Calls Qt's 'QString QQmlDataBlob::urlString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldatablob.html#urlString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlDataBlob::urlString() const
    return self.uglySide.call('ritual_ZNK12QQmlDataBlob9urlStringEv')

  def finalUrl(self) -> QUrl:
    """
    Calls Qt's 'QUrl QQmlDataBlob::finalUrl() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldatablob.html#finalUrl

    Returns
    -------

    QUrl
      A new cute QUrl around the copy Qt gave back. Python owns it.
    """
    #  QUrl QQmlDataBlob::finalUrl() const
    address = self.uglySide.call('ritual_ZNK12QQmlDataBlob8finalUrlEv')
    from ..QtCore import QUrl
    return QUrl._cuteOwning(address)

  def finalUrlString(self) -> str:
    """
    Calls Qt's 'QString QQmlDataBlob::finalUrlString() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldatablob.html#finalUrlString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlDataBlob::finalUrlString() const
    return self.uglySide.call('ritual_ZNK12QQmlDataBlob14finalUrlStringEv')

  def errors(self) -> QList[QQmlError]:
    """
    Calls Qt's 'QList<QQmlError> QQmlDataBlob::errors() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldatablob.html#errors

    Returns
    -------

    QList[QQmlError]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQmlError> QQmlDataBlob::errors() const
    address = self.uglySide.call('ritual_ZNK12QQmlDataBlob6errorsEv')
    from . import QQmlError
    return QList[QQmlError]._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QQmlError)
  def setError(self, a0: QQmlError) -> None:
    """
    Calls Qt's 'void QQmlDataBlob::setError(const QQmlError &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldatablob.html#setError

    Parameters
    ----------

    a0 : QQmlError
      Passed on as a value: Qt reads the C++ QQmlError, which stays Python's
      own.
    """
    #  void QQmlDataBlob::setError(const QQmlError &a0)
    self.uglySide.call(
        'ritual_ZN12QQmlDataBlob8setErrorERK9QQmlError', self._valueOf(a0),
    )

  @overload(QList[QQmlError])
  def setError(self, errors: QList[QQmlError]) -> None:
    """
    Calls Qt's 'void QQmlDataBlob::setError(const QList<QQmlError> &errors)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldatablob.html#setError

    Parameters
    ----------

    errors : QList[QQmlError]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QQmlDataBlob::setError(const QList<QQmlError> &errors)
    self.uglySide.call(
        'ritual_ZN12QQmlDataBlob8setErrorERK5QListI9QQmlErrorE',
        self._valueOf(errors),
    )

  @overload(WAIT['QQmlJS.DiagnosticMessage'])
  def setError(self, error: QQmlJS.DiagnosticMessage) -> None:
    """
    Calls Qt's 'void QQmlDataBlob::setError(const QQmlJS::DiagnosticMessage
    &error)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldatablob.html#setError

    Parameters
    ----------

    error : QQmlJS.DiagnosticMessage
      Passed on as a value: Qt reads the C++ QQmlJS::DiagnosticMessage, which
      stays Python's own.
    """
    #  void QQmlDataBlob::setError(const QQmlJS::DiagnosticMessage &error)
    self.uglySide.call(
        'ritual_ZN12QQmlDataBlob8setErrorERKN6QQmlJS17DiagnosticMessageE',
        self._valueOf(error),
    )

  @overload(str)
  def setError(self, description: str) -> None:
    """
    Calls Qt's 'void QQmlDataBlob::setError(const QString &description)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldatablob.html#setError

    Parameters
    ----------

    description : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlDataBlob::setError(const QString &description)
    self.uglySide.call(
        'ritual_ZN12QQmlDataBlob8setErrorERK7QString', description,
    )

  @overload(Status)
  def setStatus(self, status: Status) -> bool:
    """
    Calls Qt's 'bool QQmlDataBlob::setStatus(Status status)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldatablob.html#setStatus

    Parameters
    ----------

    status : Status
      Passed on as its number.
    """
    #  bool QQmlDataBlob::setStatus(Status status)
    return self.uglySide.call(
        'ritual_ZN12QQmlDataBlob9setStatusENS_6StatusE', status.value,
    )

  @overload(bool)
  def setIsAsync(self, async_: bool) -> bool:
    """
    Calls Qt's 'bool QQmlDataBlob::setIsAsync(bool async)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldatablob.html#setIsAsync

    Parameters
    ----------

    async_ : bool
      Passed on as it is.
    """
    #  bool QQmlDataBlob::setIsAsync(bool async)
    return self.uglySide.call(
        'ritual_ZN12QQmlDataBlob10setIsAsyncEb', async_,
    )

  @overload(float)
  def setProgress(self, progress: float) -> bool:
    """
    Calls Qt's 'bool QQmlDataBlob::setProgress(qreal progress)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldatablob.html#setProgress

    Parameters
    ----------

    progress : float
      Passed on as it is.
    """
    #  bool QQmlDataBlob::setProgress(qreal progress)
    return self.uglySide.call(
        'ritual_ZN12QQmlDataBlob11setProgressEd', progress,
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

  @overload(QUrl, Type, QQmlTypeLoader)
  @overload(QUrl, Type, NoneType)
  def __init__(
      self,
      a0: QUrl,
      a1: Type,
      manager: Optional[QQmlTypeLoader],
  ) -> None:
    """
    Notes what was given, for Qt's 'QQmlDataBlob::QQmlDataBlob(const QUrl
    &a0, Type a1, QQmlTypeLoader *manager)', which is called at the first
    use.

    Qt's own words: https://doc.qt.io/qt-6/qqmldatablob.html#QQmlDataBlob

    Parameters
    ----------

    a0 : QUrl
      Passed on as a value: Qt reads the C++ QUrl, which stays Python's own.

    a1 : Type
      Passed on as its number.

    manager : Optional[QQmlTypeLoader]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlDataBlob::QQmlDataBlob(const QUrl &a0, Type a1, QQmlTypeLoader
    #      *manager)
    self._noteCreation(QQmlDataBlob, lambda: Rituals.call(
        'ritual_ZN12QQmlDataBlobC1ERK4QUrlNS_4TypeEP14QQmlTypeLoader',
        self._valueOf(a0), a1.value, self._addressOf(manager),
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

  def startLoading(self) -> None:
    """
    Calls Qt's 'void QQmlDataBlob::startLoading()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldatablob.html#startLoading
    """
    #  void QQmlDataBlob::startLoading()
    self.uglySide.call('ritual_ZN12QQmlDataBlob12startLoadingEv')

  def resetTypeLoader(self) -> None:
    """
    Calls Qt's 'void QQmlDataBlob::resetTypeLoader()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldatablob.html#resetTypeLoader
    """
    #  void QQmlDataBlob::resetTypeLoader()
    self.uglySide.call('ritual_ZN12QQmlDataBlob15resetTypeLoaderEv')

  @overload(SourceCodeData)
  def dataReceived(self, a0: SourceCodeData) -> None:
    """
    Calls Qt's 'void QQmlDataBlob::dataReceived(const SourceCodeData &a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldatablob.html#dataReceived

    Parameters
    ----------

    a0 : SourceCodeData
      Passed on as a value: Qt reads the C++ QQmlDataBlob::SourceCodeData,
      which stays Python's own.
    """
    #  void QQmlDataBlob::dataReceived(const SourceCodeData &a0)
    self.uglySide.call(
        'ritual_ZN12QQmlDataBlob12dataReceivedERKNS_14SourceCodeDataE',
        self._valueOf(a0),
    )

  @overload(WAIT['QQmlPrivate.CachedQmlUnit'])
  @overload(NoneType)
  def initializeFromCachedUnit(
      self,
      a0: Optional[QQmlPrivate.CachedQmlUnit],
  ) -> None:
    """
    Calls Qt's 'void QQmlDataBlob::initializeFromCachedUnit(const
    QQmlPrivate::CachedQmlUnit *a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldatablob.html#initializeFromCachedUnit

    Parameters
    ----------

    a0 : Optional[QQmlPrivate.CachedQmlUnit]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlDataBlob::initializeFromCachedUnit(const
    #      QQmlPrivate::CachedQmlUnit *a0)
    self.uglySide.call(
        'ritual_ZN12QQmlDataBlob24initializeFromCachedUnitEPKN11QQmlPrivate'
        '13CachedQmlUnitE',
        self._addressOf(a0),
    )

  def done(self) -> None:
    """
    Calls Qt's 'void QQmlDataBlob::done()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldatablob.html#done
    """
    #  void QQmlDataBlob::done()
    ritual = 'ritual_ZN12QQmlDataBlob4doneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQmlDataBlob4doneEv'
    self.uglySide.call(ritual)

  @overload(QNetworkReply.NetworkError)
  def networkError(self, a0: QNetworkReply.NetworkError) -> None:
    """
    Calls Qt's 'void QQmlDataBlob::networkError(QNetworkReply::NetworkError
    a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldatablob.html#networkError

    Parameters
    ----------

    a0 : QNetworkReply.NetworkError
      Passed on as its number.
    """
    #  void QQmlDataBlob::networkError(QNetworkReply::NetworkError a0)
    ritual = (
        'ritual_ZN12QQmlDataBlob12networkErrorEN13QNetworkReply12NetworkErr'
        'orE')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN12QQmlDataBlob12networkErrorEN13QNetworkReply12Netw'
          'orkErrorE')
    self.uglySide.call(ritual, a0.value)

  def allDependenciesDone(self) -> None:
    """
    Calls Qt's 'void QQmlDataBlob::allDependenciesDone()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldatablob.html#allDependenciesDone
    """
    #  void QQmlDataBlob::allDependenciesDone()
    ritual = 'ritual_ZN12QQmlDataBlob19allDependenciesDoneEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQmlDataBlob19allDependenciesDoneEv'
    self.uglySide.call(ritual)

  @overload(float)
  def downloadProgressChanged(self, a0: float) -> None:
    """
    Calls Qt's 'void QQmlDataBlob::downloadProgressChanged(qreal a0)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldatablob.html#downloadProgressChanged

    Parameters
    ----------

    a0 : float
      Passed on as it is.
    """
    #  void QQmlDataBlob::downloadProgressChanged(qreal a0)
    ritual = 'ritual_ZN12QQmlDataBlob23downloadProgressChangedEd'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQmlDataBlob23downloadProgressChangedEd'
    self.uglySide.call(ritual, a0)

  def completed(self) -> None:
    """
    Calls Qt's 'void QQmlDataBlob::completed()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldatablob.html#completed
    """
    #  void QQmlDataBlob::completed()
    ritual = 'ritual_ZN12QQmlDataBlob9completedEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN12QQmlDataBlob9completedEv'
    self.uglySide.call(ritual)

  def tryDone(self) -> None:
    """
    Calls Qt's 'void QQmlDataBlob::tryDone()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmldatablob.html#tryDone
    """
    #  void QQmlDataBlob::tryDone()
    self.uglySide.call('ritual_ZN12QQmlDataBlob7tryDoneEv')

  def cancelAllWaitingFor(self) -> None:
    """
    Calls Qt's 'void QQmlDataBlob::cancelAllWaitingFor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldatablob.html#cancelAllWaitingFor
    """
    #  void QQmlDataBlob::cancelAllWaitingFor()
    self.uglySide.call('ritual_ZN12QQmlDataBlob19cancelAllWaitingForEv')

  def notifyAllWaitingOnMe(self) -> None:
    """
    Calls Qt's 'void QQmlDataBlob::notifyAllWaitingOnMe()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmldatablob.html#notifyAllWaitingOnMe
    """
    #  void QQmlDataBlob::notifyAllWaitingOnMe()
    self.uglySide.call('ritual_ZN12QQmlDataBlob20notifyAllWaitingOnMeEv')

  @staticmethod
  def addDependency(*__, **_) -> Never:
    """
    Qt's 'void QQmlDataBlob::addDependency(const QQmlDataBlob::Ptr &a0)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlDataBlob.addDependency' has no cute function yet. Qt's 'void "
        "QQmlDataBlob::addDependency(const QQmlDataBlob::Ptr &a0)': takes a "
        "type Python has no way to hand over yet.")

  @staticmethod
  def assertEngineThread(*__, **_) -> Never:
    """
    Qt's 'QQmlDataBlob::assertEngineThread': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QQmlDataBlob.assertEngineThread' has no cute function yet. Qt's "
        "'QQmlDataBlob::assertEngineThread': a template: a pattern and no "
        "single function.")

  @staticmethod
  def assertEngineThreadIfRunning(*__, **_) -> Never:
    """
    Qt's 'QQmlDataBlob::assertEngineThreadIfRunning': a template: a pattern
    and no single function.
    """
    raise NotImplementedError(
        "'QQmlDataBlob.assertEngineThreadIfRunning' has no cute function "
        "yet. Qt's 'QQmlDataBlob::assertEngineThreadIfRunning': a template: "
        "a pattern and no single function.")

  @staticmethod
  def assertTypeLoaderThread(*__, **_) -> Never:
    """
    Qt's 'QQmlDataBlob::assertTypeLoaderThread': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QQmlDataBlob.assertTypeLoaderThread' has no cute function yet. "
        "Qt's 'QQmlDataBlob::assertTypeLoaderThread': a template: a pattern "
        "and no single function.")

  @staticmethod
  def assertTypeLoaderThreadIfRunning(*__, **_) -> Never:
    """
    Qt's 'QQmlDataBlob::assertTypeLoaderThreadIfRunning': a template: a
    pattern and no single function.
    """
    raise NotImplementedError(
        "'QQmlDataBlob.assertTypeLoaderThreadIfRunning' has no cute "
        "function yet. Qt's "
        "'QQmlDataBlob::assertTypeLoaderThreadIfRunning': a template: a "
        "pattern and no single function.")

  @staticmethod
  def dependencyComplete(*__, **_) -> Never:
    """
    Qt's 'void QQmlDataBlob::dependencyComplete(const QQmlDataBlob::Ptr
    &a0)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlDataBlob.dependencyComplete' has no cute function yet. Qt's "
        "'void QQmlDataBlob::dependencyComplete(const QQmlDataBlob::Ptr "
        "&a0)': takes a type Python has no way to hand over yet.")

  @staticmethod
  def dependencyError(*__, **_) -> Never:
    """
    Qt's 'void QQmlDataBlob::dependencyError(const QQmlDataBlob::Ptr &a0)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlDataBlob.dependencyError' has no cute function yet. Qt's "
        "'void QQmlDataBlob::dependencyError(const QQmlDataBlob::Ptr &a0)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def notifyComplete(*__, **_) -> Never:
    """
    Qt's 'void QQmlDataBlob::notifyComplete(const QQmlDataBlob::Ptr &a0)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlDataBlob.notifyComplete' has no cute function yet. Qt's 'void "
        "QQmlDataBlob::notifyComplete(const QQmlDataBlob::Ptr &a0)': takes "
        "a type Python has no way to hand over yet.")
