"""
QNearFieldTarget binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNfc/qnearfieldtarget.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteFlags, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList, QObject, QSharedData

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QByteArray, QMetaObject, QVariant
  from . import QNdefMessage, QNearFieldTargetPrivate
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QNdefMessage = WAIT['QNdefMessage']
  QNearFieldTargetPrivate = WAIT['QNearFieldTargetPrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QNearFieldTarget(QObject):
  """
  The cute side of Qt's QNearFieldTarget: a plain Python object standing in
  front of one C++ QNearFieldTarget.

  It is built on the cute 'QObject', as Qt's QNearFieldTarget is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QNearFieldTarget that has a ritual and that Python
  can call so far, 18 names in all: 'metaObject', 'tr', 'd_func', 'uid',
  'type', 'accessMethods', 'disconnect', 'hasNdefMessage',
  'readNdefMessages', 'writeNdefMessages', 'maxCommandLength', 'sendCommand',
  'waitForRequestCompleted', 'requestResponse', 'disconnected',
  'ndefMessageRead', 'requestCompleted', 'error'. It can be made from Python,
  in 2 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QNearFieldTarget::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QNearFieldTarget::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'const QNearFieldTargetPrivate *QNearFieldTarget::d_func() const':
    takes in Python what 'QNearFieldTargetPrivate
    *QNearFieldTarget::d_func()' takes.
  - Qt's 'QNearFieldTarget::~QNearFieldTarget()': the destructor: Python
    never removes a C++ QNearFieldTarget.

  What has no ritual
  ------------------

  2 of the 26 functions Qt declares: 2 not a gap.

  What to expect
  --------------

  - The C++ QNearFieldTarget is created at the first use, not by
    'QNearFieldTarget(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNearFieldTarget.
  - Qt tells when it has removed the C++ QNearFieldTarget. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

  #  The enums Qt writes inside QNearFieldTarget, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class AccessMethod(CuteFlags):
    """
    The flags enum 'QNearFieldTarget::AccessMethod' of Qt, with the 4 names
    Qt gives in it. Qt names the type of its combinations
    'QNearFieldTarget::AccessMethods'.
    """

    UnknownAccess = 0x0
    NdefAccess = 0x1
    TagTypeSpecificAccess = 0x2
    AnyAccess = 0xff

  AccessMethods = AccessMethod

  class Error(CuteNum):
    """
    The enum 'QNearFieldTarget::Error' of Qt, with the 13 names Qt gives in
    it.
    """

    NoError = Kee[int](0)
    UnknownError = Kee[int](1)
    UnsupportedError = Kee[int](2)
    TargetOutOfRangeError = Kee[int](3)
    NoResponseError = Kee[int](4)
    ChecksumMismatchError = Kee[int](5)
    InvalidParametersError = Kee[int](6)
    ConnectionError = Kee[int](7)
    NdefReadError = Kee[int](8)
    NdefWriteError = Kee[int](9)
    CommandError = Kee[int](10)
    TimeoutError = Kee[int](11)
    UnsupportedTargetError = Kee[int](12)

  class Type(CuteNum):
    """
    The enum 'QNearFieldTarget::Type' of Qt, with the 8 names Qt gives in it.
    """

    ProprietaryTag = Kee[int](0)
    NfcTagType1 = Kee[int](1)
    NfcTagType2 = Kee[int](2)
    NfcTagType3 = Kee[int](3)
    NfcTagType4 = Kee[int](4)
    NfcTagType4A = Kee[int](5)
    NfcTagType4B = Kee[int](6)
    MifareTag = Kee[int](7)

  #  The classes Qt writes inside QNearFieldTarget, each a class in here as
  #  in C++.

  class RequestId(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QNearFieldTarget::RequestId: a plain Python object
    standing in front of one C++ QNearFieldTarget::RequestId.

    C++ hands a QNearFieldTarget::RequestId around as a copy, so every C++
    QNearFieldTarget::RequestId behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QNearFieldTarget::RequestId that has a ritual and
    that Python can call so far, 5 names in all: 'isValid', 'refCount',
    '__lt__', '__eq__', '__ne__'. It can be made from Python, in 2 ways; see
    '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QNearFieldTarget::RequestId::RequestId(RequestIdPrivate *p)':
      names 'QNearFieldTarget::RequestIdPrivate', which stands beside this
      class inside 'QNearFieldTarget' and cannot be named from here.
    - Qt's 'QNearFieldTarget::RequestId::~RequestId()': the destructor:
      Python removes its C++ QNearFieldTarget::RequestId by it, and has no
      other use for it.
    - Qt's 'RequestId &QNearFieldTarget::RequestId::operator=(const RequestId
      &other)': assignment: Python binds a name and has no operator for it.

    What to expect
    --------------

    - The C++ QNearFieldTarget::RequestId is created at the first use, not by
      'QNearFieldTarget::RequestId(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QNearFieldTarget::RequestId back gives a copy the
      ritual made for Python, in a new cute QNearFieldTarget::RequestId.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QNearFieldTarget::RequestId'

    #  Qt's '~QNearFieldTarget::RequestId()'. Naming it makes this a value
    #  class: Python owns every C++ QNearFieldTarget::RequestId behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN16QNearFieldTarget9RequestIdD1Ev'

    #  Fallback Variables

    #  Private Variables

    #  Public Variables

    #  Virtual Variables

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    def isValid(self) -> bool:
      """
      Calls Qt's 'bool QNearFieldTarget::RequestId::isValid() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qnearfieldtarget-requestid.html#isValid
      """
      #  bool QNearFieldTarget::RequestId::isValid() const
      return self.uglySide.call(
          'ritual_ZNK16QNearFieldTarget9RequestId7isValidEv',
      )

    def refCount(self) -> int:
      """
      Calls Qt's 'int QNearFieldTarget::RequestId::refCount() const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qnearfieldtarget-requestid.html#refCount
      """
      #  int QNearFieldTarget::RequestId::refCount() const
      return self.uglySide.call(
          'ritual_ZNK16QNearFieldTarget9RequestId8refCountEv',
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

    @overload(THIS)
    def __lt__(self, other: QNearFieldTarget.RequestId) -> bool:
      """
      Calls Qt's 'bool QNearFieldTarget::RequestId::operator<(const RequestId
      &other) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qnearfieldtarget-requestid.html#operator<

      Parameters
      ----------

      other : QNearFieldTarget.RequestId
        Passed on as a value: Qt reads the C++ QNearFieldTarget::RequestId,
        which stays Python's own.
      """
      #  bool QNearFieldTarget::RequestId::operator<(const RequestId &other)
      #      const
      return self.uglySide.call(
          'ritual_ZNK16QNearFieldTarget9RequestIdltERKS0_',
          self._valueOf(other),
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
    def __eq__(self, other: QNearFieldTarget.RequestId) -> bool:
      """
      Calls Qt's 'bool QNearFieldTarget::RequestId::operator==(const
      RequestId &other) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qnearfieldtarget-requestid.html#operator==

      Parameters
      ----------

      other : QNearFieldTarget.RequestId
        Passed on as a value: Qt reads the C++ QNearFieldTarget::RequestId,
        which stays Python's own.
      """
      #  bool QNearFieldTarget::RequestId::operator==(const RequestId &other)
      #      const
      return self.uglySide.call(
          'ritual_ZNK16QNearFieldTarget9RequestIdeqERKS0_',
          self._valueOf(other),
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
    def __ne__(self, other: QNearFieldTarget.RequestId) -> bool:
      """
      Calls Qt's 'bool QNearFieldTarget::RequestId::operator!=(const
      RequestId &other) const'.

      Qt's own words:
      https://doc.qt.io/qt-6/qnearfieldtarget-requestid.html#operator!=

      Parameters
      ----------

      other : QNearFieldTarget.RequestId
        Passed on as a value: Qt reads the C++ QNearFieldTarget::RequestId,
        which stays Python's own.
      """
      #  bool QNearFieldTarget::RequestId::operator!=(const RequestId &other)
      #      const
      return self.uglySide.call(
          'ritual_ZNK16QNearFieldTarget9RequestIdneERKS0_',
          self._valueOf(other),
      )

    @overload.fallback
    def __ne__(self, *args: object) -> object:
      """
      Tells Python that no function of this name takes what it was
      handed, with Python's own word for it. Python then asks the
      other side of the operator.
      """
      return NotImplemented

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @overload()
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QNearFieldTarget::RequestId::RequestId()', which is called at the
      first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qnearfieldtarget-requestid.html#RequestId
      """
      #  QNearFieldTarget::RequestId::RequestId()
      self._noteCreation(QNearFieldTarget.RequestId, lambda: Rituals.call(
          'ritual_ZN16QNearFieldTarget9RequestIdC1Ev',
      ))

    @overload(THIS)
    def __init__(self, other: QNearFieldTarget.RequestId) -> None:
      """
      Notes what was given, for Qt's
      'QNearFieldTarget::RequestId::RequestId(const RequestId &other)', which
      is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qnearfieldtarget-requestid.html#RequestId

      Parameters
      ----------

      other : QNearFieldTarget.RequestId
        Passed on as a value: Qt reads the C++ QNearFieldTarget::RequestId,
        which stays Python's own.
      """
      #  QNearFieldTarget::RequestId::RequestId(const RequestId &other)
      self._noteCreation(QNearFieldTarget.RequestId, lambda: Rituals.call(
          'ritual_ZN16QNearFieldTarget9RequestIdC1ERKS0_',
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

  class RequestIdPrivate(QSharedData):
    """
    The cute side of Qt's QNearFieldTarget::RequestIdPrivate: a plain Python
    object standing in front of one C++ QNearFieldTarget::RequestIdPrivate.

    It is built on the cute 'QSharedData', as Qt's
    QNearFieldTarget::RequestIdPrivate is built on Qt's QSharedData, and has
    everything that class has.

    C++ hands a QNearFieldTarget::RequestIdPrivate around as a copy, so every
    C++ QNearFieldTarget::RequestIdPrivate behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QNearFieldTarget::RequestIdPrivate yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QNearFieldTarget::RequestIdPrivate::~RequestIdPrivate()': the
      destructor: Python removes its C++ QNearFieldTarget::RequestIdPrivate
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QNearFieldTarget::RequestIdPrivate is created at the first use,
      not by 'QNearFieldTarget::RequestIdPrivate(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QNearFieldTarget::RequestIdPrivate back gives a
      copy the ritual made for Python, in a new cute
      QNearFieldTarget::RequestIdPrivate.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QNearFieldTarget::RequestIdPrivate'

    #  Qt's '~QNearFieldTarget::RequestIdPrivate()'. Naming it makes this a
    #  value class: Python owns every C++ QNearFieldTarget::RequestIdPrivate
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN16QNearFieldTarget16RequestIdPrivateD1Ev'

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
    Calls Qt's 'QString QNearFieldTarget::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qnearfieldtarget.html#tr

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
    #  QString QNearFieldTarget::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN16QNearFieldTarget2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNearFieldTarget'

  #  A C++ QNearFieldTarget Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QNearFieldTarget'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QNearFieldTarget::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnearfieldtarget.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QNearFieldTarget::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK16QNearFieldTarget10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def uid(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QNearFieldTarget::uid() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnearfieldtarget.html#uid

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QNearFieldTarget::uid() const
    address = self.uglySide.call('ritual_ZNK16QNearFieldTarget3uidEv')
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def type(self) -> Type:
    """
    Calls Qt's 'Type QNearFieldTarget::type() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnearfieldtarget.html#type

    Returns
    -------

    Type
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Type(number)' gives.
    """
    #  Type QNearFieldTarget::type() const
    return QNearFieldTarget.Type(self.uglySide.call(
        'ritual_ZNK16QNearFieldTarget4typeEv',
    ))

  def accessMethods(self) -> AccessMethods:
    """
    Calls Qt's 'AccessMethods QNearFieldTarget::accessMethods() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnearfieldtarget.html#accessMethods

    Returns
    -------

    AccessMethods
      The value standing for the combination Qt gave back.
    """
    #  AccessMethods QNearFieldTarget::accessMethods() const
    return QNearFieldTarget.AccessMethods(self.uglySide.call(
        'ritual_ZNK16QNearFieldTarget13accessMethodsEv',
    ))

  def maxCommandLength(self) -> int:
    """
    Calls Qt's 'int QNearFieldTarget::maxCommandLength() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnearfieldtarget.html#maxCommandLength
    """
    #  int QNearFieldTarget::maxCommandLength() const
    return self.uglySide.call(
        'ritual_ZNK16QNearFieldTarget16maxCommandLengthEv',
    )

  @overload(RequestId)
  def requestResponse(self, id: RequestId) -> QVariant:
    """
    Calls Qt's 'QVariant QNearFieldTarget::requestResponse(const RequestId
    &id) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnearfieldtarget.html#requestResponse

    Parameters
    ----------

    id : RequestId
      Passed on as a value: Qt reads the C++ QNearFieldTarget::RequestId,
      which stays Python's own.

    Returns
    -------

    QVariant
      A new cute QVariant around the copy Qt gave back. Python owns it.
    """
    #  QVariant QNearFieldTarget::requestResponse(const RequestId &id) const
    address = self.uglySide.call(
        'ritual_ZNK16QNearFieldTarget15requestResponseERKNS_9RequestIdE',
        self._valueOf(id),
    )
    from ..QtCore import QVariant
    return QVariant._cuteOwning(address)

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

  @overload(QNearFieldTargetPrivate)
  @overload(QNearFieldTargetPrivate, QObject)
  @overload(QNearFieldTargetPrivate, NoneType)
  @overload(NoneType, QObject)
  @overload(NoneType, NoneType)
  def __init__(
      self,
      backend: Optional[QNearFieldTargetPrivate],
      parent: Optional[QObject] = None,
  ) -> None:
    """
    Notes what was given, for Qt's
    'QNearFieldTarget::QNearFieldTarget(QNearFieldTargetPrivate *backend,
    QObject *parent)', which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnearfieldtarget.html#QNearFieldTarget

    Parameters
    ----------

    backend : Optional[QNearFieldTargetPrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QNearFieldTarget::QNearFieldTarget(QNearFieldTargetPrivate *backend,
    #      QObject *parent)
    self._noteCreation(QNearFieldTarget, lambda: Rituals.call(
        'ritual_ZN16QNearFieldTargetC1EP23QNearFieldTargetPrivateP7QObject',
        self._addressOf(backend), self._addressOf(parent, 'QObject'),
    ))

  @overload()
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QNearFieldTarget::QNearFieldTarget(QObject *parent)', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qnearfieldtarget.html#QNearFieldTarget

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QNearFieldTarget::QNearFieldTarget(QObject *parent)
    self._noteCreation(QNearFieldTarget, lambda: Rituals.call(
        'ritual_ZN16QNearFieldTargetC1EP7QObject',
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

  def d_func(self) -> Optional[QNearFieldTargetPrivate]:
    """
    Calls Qt's 'QNearFieldTargetPrivate *QNearFieldTarget::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qnearfieldtarget.html#d_func

    Returns
    -------

    Optional[QNearFieldTargetPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNearFieldTargetPrivate *QNearFieldTarget::d_func()
    address = self.uglySide.call('ritual_ZN16QNearFieldTarget6d_funcEv')
    from . import QNearFieldTargetPrivate
    return QNearFieldTargetPrivate._cuteAt(address)

  def disconnect(self) -> bool:
    """
    Calls Qt's 'bool QNearFieldTarget::disconnect()'.

    Qt's own words: https://doc.qt.io/qt-6/qnearfieldtarget.html#disconnect
    """
    #  bool QNearFieldTarget::disconnect()
    return self.uglySide.call('ritual_ZN16QNearFieldTarget10disconnectEv')

  def hasNdefMessage(self) -> bool:
    """
    Calls Qt's 'bool QNearFieldTarget::hasNdefMessage()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnearfieldtarget.html#hasNdefMessage
    """
    #  bool QNearFieldTarget::hasNdefMessage()
    return self.uglySide.call(
        'ritual_ZN16QNearFieldTarget14hasNdefMessageEv',
    )

  def readNdefMessages(self) -> RequestId:
    """
    Calls Qt's 'RequestId QNearFieldTarget::readNdefMessages()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnearfieldtarget.html#readNdefMessages

    Returns
    -------

    RequestId
      A new cute QNearFieldTarget::RequestId around the copy Qt gave back.
      Python owns it.
    """
    #  RequestId QNearFieldTarget::readNdefMessages()
    address = self.uglySide.call(
        'ritual_ZN16QNearFieldTarget16readNdefMessagesEv',
    )
    return QNearFieldTarget.RequestId._cuteOwning(address)

  @overload(QList[QNdefMessage])
  def writeNdefMessages(self, messages: QList[QNdefMessage]) -> RequestId:
    """
    Calls Qt's 'RequestId QNearFieldTarget::writeNdefMessages(const
    QList<QNdefMessage> &messages)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnearfieldtarget.html#writeNdefMessages

    Parameters
    ----------

    messages : QList[QNdefMessage]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    Returns
    -------

    RequestId
      A new cute QNearFieldTarget::RequestId around the copy Qt gave back.
      Python owns it.
    """
    #  RequestId QNearFieldTarget::writeNdefMessages(const
    #      QList<QNdefMessage> &messages)
    address = self.uglySide.call(
        'ritual_ZN16QNearFieldTarget17writeNdefMessagesERK5QListI12QNdefMes'
        'sageE',
        self._valueOf(messages),
    )
    return QNearFieldTarget.RequestId._cuteOwning(address)

  @overload(QByteArray)
  def sendCommand(self, command: QByteArray) -> RequestId:
    """
    Calls Qt's 'RequestId QNearFieldTarget::sendCommand(const QByteArray
    &command)'.

    Qt's own words: https://doc.qt.io/qt-6/qnearfieldtarget.html#sendCommand

    Parameters
    ----------

    command : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    Returns
    -------

    RequestId
      A new cute QNearFieldTarget::RequestId around the copy Qt gave back.
      Python owns it.
    """
    #  RequestId QNearFieldTarget::sendCommand(const QByteArray &command)
    address = self.uglySide.call(
        'ritual_ZN16QNearFieldTarget11sendCommandERK10QByteArray',
        self._valueOf(command),
    )
    return QNearFieldTarget.RequestId._cuteOwning(address)

  @overload(RequestId)
  @overload(RequestId, int)
  def waitForRequestCompleted(
      self,
      id: RequestId,
      msecs: int = 5000,
  ) -> bool:
    """
    Calls Qt's 'bool QNearFieldTarget::waitForRequestCompleted(const
    RequestId &id, int msecs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnearfieldtarget.html#waitForRequestCompleted

    Parameters
    ----------

    id : RequestId
      Passed on as a value: Qt reads the C++ QNearFieldTarget::RequestId,
      which stays Python's own.

    msecs : int
      Passed on as it is. May be left out, as in Qt: it is then 5000.
    """
    #  bool QNearFieldTarget::waitForRequestCompleted(const RequestId &id,
    #      int msecs)
    return self.uglySide.call(
        'ritual_ZN16QNearFieldTarget23waitForRequestCompletedERKNS_9Request'
        'IdEi',
        self._valueOf(id), msecs,
    )

  def disconnected(self) -> None:
    """
    Calls Qt's 'void QNearFieldTarget::disconnected()'.

    Qt's own words: https://doc.qt.io/qt-6/qnearfieldtarget.html#disconnected
    """
    #  void QNearFieldTarget::disconnected()
    self.uglySide.call('ritual_ZN16QNearFieldTarget12disconnectedEv')

  @overload(QNdefMessage)
  def ndefMessageRead(self, message: QNdefMessage) -> None:
    """
    Calls Qt's 'void QNearFieldTarget::ndefMessageRead(const QNdefMessage
    &message)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnearfieldtarget.html#ndefMessageRead

    Parameters
    ----------

    message : QNdefMessage
      Passed on as a value: Qt reads the C++ QNdefMessage, which stays
      Python's own.
    """
    #  void QNearFieldTarget::ndefMessageRead(const QNdefMessage &message)
    self.uglySide.call(
        'ritual_ZN16QNearFieldTarget15ndefMessageReadERK12QNdefMessage',
        self._valueOf(message),
    )

  @overload(RequestId)
  def requestCompleted(self, id: RequestId) -> None:
    """
    Calls Qt's 'void QNearFieldTarget::requestCompleted(const
    QNearFieldTarget::RequestId &id)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnearfieldtarget.html#requestCompleted

    Parameters
    ----------

    id : RequestId
      Passed on as a value: Qt reads the C++ QNearFieldTarget::RequestId,
      which stays Python's own.
    """
    #  void QNearFieldTarget::requestCompleted(const
    #      QNearFieldTarget::RequestId &id)
    self.uglySide.call(
        'ritual_ZN16QNearFieldTarget16requestCompletedERKNS_9RequestIdE',
        self._valueOf(id),
    )

  @overload(Error, RequestId)
  def error(self, error: Error, id: RequestId) -> None:
    """
    Calls Qt's 'void QNearFieldTarget::error(QNearFieldTarget::Error error,
    const QNearFieldTarget::RequestId &id)'.

    Qt's own words: https://doc.qt.io/qt-6/qnearfieldtarget.html#error

    Parameters
    ----------

    error : Error
      Passed on as its number.

    id : RequestId
      Passed on as a value: Qt reads the C++ QNearFieldTarget::RequestId,
      which stays Python's own.
    """
    #  void QNearFieldTarget::error(QNearFieldTarget::Error error, const
    #      QNearFieldTarget::RequestId &id)
    self.uglySide.call(
        'ritual_ZN16QNearFieldTarget5errorENS_5ErrorERKNS_9RequestIdE',
        error.value, self._valueOf(id),
    )
