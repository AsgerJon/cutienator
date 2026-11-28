"""
QTextStreamPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qtextstream_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QTextStreamPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QChar, QIODevice, QTextStream
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QChar = WAIT['QChar']
  QIODevice = WAIT['QIODevice']
  QTextStream = WAIT['QTextStream']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QTextStreamPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTextStreamPrivate: a plain Python object standing in
  front of one C++ QTextStreamPrivate.

  What exists
  -----------

  Every function of Qt's QTextStreamPrivate that has a ritual and that Python
  can call so far, 15 names in all: 'q_func', 'reset', 'setupDevice',
  'disconnectFromDevice', 'read', 'readPtr', 'consumeLastToken', 'consume',
  'saveConverterState', 'restoreToSavedConverterState', 'getChar',
  'ungetChar', 'padding', 'resetReadBuffer', 'flushWriteBuffer'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QTextStream *QTextStreamPrivate::q_func() const': takes in
    Python what 'QTextStream *QTextStreamPrivate::q_func()' takes.
  - Qt's 'QTextStreamPrivate::~QTextStreamPrivate()': the destructor: Python
    never removes a C++ QTextStreamPrivate.
  - Qt's 'bool QTextStreamPrivate::scan(const QChar **ptr, qsizetype
    *tokenLength, qsizetype maxlen, TokenDelimiter delimiter)': takes a type
    Python has no way to hand over yet.
  - Qt's 'bool QTextStreamPrivate::getReal(double *f)': takes a number to
    change where it is.

  What has no ritual
  ------------------

  13 of the 33 functions Qt declares: 8 leans on 'void QTextStreamPrivate; 3
  Qt's library has no name for it, and its code in Qt's source does not
  compile apart from its file; 2 a template.

  What to expect
  --------------

  - The C++ QTextStreamPrivate is created at the first use, not by
    'QTextStreamPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTextStreamPrivate.
  - Each name of Qt's QTextStreamPrivate that has no cute function yet,
    'fillReadBuffer', 'getNumber', 'getReal', 'putChar', 'putNumber',
    'putString', 'putStringImpl', 'scan', 'write', 'writeImpl',
    'writePadding', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QTextStreamPrivate, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class NumberParsingStatus(CuteNum):
    """
    The enum 'QTextStreamPrivate::NumberParsingStatus' of Qt, with the 3
    names Qt gives in it.
    """

    npsOk = Kee[int](0)
    npsMissingDigit = Kee[int](1)
    npsInvalidPrefix = Kee[int](2)

  class PutStringMode(CuteNum, scoped=True):
    """
    The enum 'QTextStreamPrivate::PutStringMode' of Qt, with the 2 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    String = Kee[int](0)
    Number = Kee[int](1)

  class TokenDelimiter(CuteNum):
    """
    The enum 'QTextStreamPrivate::TokenDelimiter' of Qt, with the 3 names Qt
    gives in it.
    """

    Space = Kee[int](0)
    NotSpace = Kee[int](1)
    EndOfLine = Kee[int](2)

  #  The classes Qt writes inside QTextStreamPrivate, each a class in here as
  #  in C++.

  class PaddingResult(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QTextStreamPrivate::PaddingResult: a plain Python
    object standing in front of one C++ QTextStreamPrivate::PaddingResult.

    C++ hands a QTextStreamPrivate::PaddingResult around as a copy, so every
    C++ QTextStreamPrivate::PaddingResult behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QTextStreamPrivate::PaddingResult yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QTextStreamPrivate::PaddingResult::~PaddingResult()': the
      destructor: Python removes its C++ QTextStreamPrivate::PaddingResult by
      it, and has no other use for it.

    What to expect
    --------------

    - The C++ QTextStreamPrivate::PaddingResult is created at the first use,
      not by 'QTextStreamPrivate::PaddingResult(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QTextStreamPrivate::PaddingResult back gives a copy
      the ritual made for Python, in a new cute
      QTextStreamPrivate::PaddingResult.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QTextStreamPrivate::PaddingResult'

    #  Qt's '~QTextStreamPrivate::PaddingResult()'. Naming it makes this a
    #  value class: Python owns every C++ QTextStreamPrivate::PaddingResult
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN18QTextStreamPrivate13PaddingResultD1Ev'

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

  class Params(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QTextStreamPrivate::Params: a plain Python object
    standing in front of one C++ QTextStreamPrivate::Params.

    C++ hands a QTextStreamPrivate::Params around as a copy, so every C++
    QTextStreamPrivate::Params behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    Every function of Qt's QTextStreamPrivate::Params that has a ritual and
    that Python can call so far, 1 name in all: 'reset'. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QTextStreamPrivate::Params::~Params()': the destructor: Python
      removes its C++ QTextStreamPrivate::Params by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QTextStreamPrivate::Params is created at the first use, not by
      'QTextStreamPrivate::Params(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QTextStreamPrivate::Params back gives a copy the
      ritual made for Python, in a new cute QTextStreamPrivate::Params.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QTextStreamPrivate::Params'

    #  Qt's '~QTextStreamPrivate::Params()'. Naming it makes this a value
    #  class: Python owns every C++ QTextStreamPrivate::Params behind a cute
    #  one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN18QTextStreamPrivate6ParamsD1Ev'

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

    def reset(self) -> None:
      """
      Calls Qt's 'void QTextStreamPrivate::Params::reset()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qtextstreamprivate-params.html#reset
      """
      #  void QTextStreamPrivate::Params::reset()
      self.uglySide.call('ritual_ZN18QTextStreamPrivate6Params5resetEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTextStreamPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def readPtr(self) -> Optional[QChar]:
    """
    Calls Qt's 'const QChar *QTextStreamPrivate::readPtr() const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextstreamprivate.html#readPtr

    Returns
    -------

    Optional[QChar]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QChar *QTextStreamPrivate::readPtr() const
    address = self.uglySide.call('ritual_ZNK18QTextStreamPrivate7readPtrEv')
    from . import QChar
    return QChar._cuteAt(address)

  @overload(int)
  def padding(self, len: int) -> PaddingResult:
    """
    Calls Qt's 'PaddingResult QTextStreamPrivate::padding(qsizetype len)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qtextstreamprivate.html#padding

    Parameters
    ----------

    len : int
      Passed on as it is.

    Returns
    -------

    PaddingResult
      A new cute QTextStreamPrivate::PaddingResult around the copy Qt gave
      back. Python owns it.
    """
    #  PaddingResult QTextStreamPrivate::padding(qsizetype len) const
    address = self.uglySide.call(
        'ritual_ZNK18QTextStreamPrivate7paddingEx', len,
    )
    return QTextStreamPrivate.PaddingResult._cuteOwning(address)

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

  @overload(QTextStream)
  @overload(NoneType)
  def __init__(self, q_ptr: Optional[QTextStream]) -> None:
    """
    Notes what was given, for Qt's
    'QTextStreamPrivate::QTextStreamPrivate(QTextStream *q_ptr)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextstreamprivate.html#QTextStreamPrivate

    Parameters
    ----------

    q_ptr : Optional[QTextStream]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QTextStreamPrivate::QTextStreamPrivate(QTextStream *q_ptr)
    self._noteCreation(QTextStreamPrivate, lambda: Rituals.call(
        'ritual_ZN18QTextStreamPrivateC1EP11QTextStream',
        self._addressOf(q_ptr),
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

  def q_func(self) -> Optional[QTextStream]:
    """
    Calls Qt's 'QTextStream *QTextStreamPrivate::q_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextstreamprivate.html#q_func

    Returns
    -------

    Optional[QTextStream]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QTextStream *QTextStreamPrivate::q_func()
    address = self.uglySide.call('ritual_ZN18QTextStreamPrivate6q_funcEv')
    from . import QTextStream
    return QTextStream._cuteAt(address)

  def reset(self) -> None:
    """
    Calls Qt's 'void QTextStreamPrivate::reset()'.

    Qt's own words: https://doc.qt.io/qt-6/qtextstreamprivate.html#reset
    """
    #  void QTextStreamPrivate::reset()
    self.uglySide.call('ritual_ZN18QTextStreamPrivate5resetEv')

  @overload(QIODevice)
  @overload(NoneType)
  def setupDevice(self, device: Optional[QIODevice]) -> None:
    """
    Calls Qt's 'void QTextStreamPrivate::setupDevice(QIODevice *device)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextstreamprivate.html#setupDevice

    Parameters
    ----------

    device : Optional[QIODevice]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QTextStreamPrivate::setupDevice(QIODevice *device)
    self.uglySide.call(
        'ritual_ZN18QTextStreamPrivate11setupDeviceEP9QIODevice',
        self._addressOf(device),
    )

  def disconnectFromDevice(self) -> None:
    """
    Calls Qt's 'void QTextStreamPrivate::disconnectFromDevice()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextstreamprivate.html#disconnectFromDevice
    """
    #  void QTextStreamPrivate::disconnectFromDevice()
    self.uglySide.call(
        'ritual_ZN18QTextStreamPrivate20disconnectFromDeviceEv',
    )

  @overload(int)
  def read(self, maxlen: int) -> str:
    """
    Calls Qt's 'QString QTextStreamPrivate::read(qsizetype maxlen)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextstreamprivate.html#read

    Parameters
    ----------

    maxlen : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTextStreamPrivate::read(qsizetype maxlen)
    return self.uglySide.call('ritual_ZN18QTextStreamPrivate4readEx', maxlen)

  def consumeLastToken(self) -> None:
    """
    Calls Qt's 'void QTextStreamPrivate::consumeLastToken()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextstreamprivate.html#consumeLastToken
    """
    #  void QTextStreamPrivate::consumeLastToken()
    self.uglySide.call('ritual_ZN18QTextStreamPrivate16consumeLastTokenEv')

  @overload(int)
  def consume(self, nchars: int) -> None:
    """
    Calls Qt's 'void QTextStreamPrivate::consume(qsizetype nchars)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextstreamprivate.html#consume

    Parameters
    ----------

    nchars : int
      Passed on as it is.
    """
    #  void QTextStreamPrivate::consume(qsizetype nchars)
    self.uglySide.call('ritual_ZN18QTextStreamPrivate7consumeEx', nchars)

  @overload(int)
  def saveConverterState(self, newPos: int) -> None:
    """
    Calls Qt's 'void QTextStreamPrivate::saveConverterState(qint64 newPos)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextstreamprivate.html#saveConverterState

    Parameters
    ----------

    newPos : int
      Passed on as it is.
    """
    #  void QTextStreamPrivate::saveConverterState(qint64 newPos)
    self.uglySide.call(
        'ritual_ZN18QTextStreamPrivate18saveConverterStateEx', newPos,
    )

  def restoreToSavedConverterState(self) -> None:
    """
    Calls Qt's 'void QTextStreamPrivate::restoreToSavedConverterState()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextstreamprivate.html
    """
    #  void QTextStreamPrivate::restoreToSavedConverterState()
    self.uglySide.call(
        'ritual_ZN18QTextStreamPrivate28restoreToSavedConverterStateEv',
    )

  @overload(QChar)
  @overload(NoneType)
  def getChar(self, ch: Optional[QChar]) -> bool:
    """
    Calls Qt's 'bool QTextStreamPrivate::getChar(QChar *ch)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextstreamprivate.html#getChar

    Parameters
    ----------

    ch : Optional[QChar]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QTextStreamPrivate::getChar(QChar *ch)
    return self.uglySide.call(
        'ritual_ZN18QTextStreamPrivate7getCharEP5QChar', self._addressOf(ch),
    )

  @overload(QChar)
  def ungetChar(self, ch: QChar) -> None:
    """
    Calls Qt's 'void QTextStreamPrivate::ungetChar(QChar ch)'.

    Qt's own words: https://doc.qt.io/qt-6/qtextstreamprivate.html#ungetChar

    Parameters
    ----------

    ch : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  void QTextStreamPrivate::ungetChar(QChar ch)
    self.uglySide.call(
        'ritual_ZN18QTextStreamPrivate9ungetCharE5QChar', self._valueOf(ch),
    )

  def resetReadBuffer(self) -> None:
    """
    Calls Qt's 'void QTextStreamPrivate::resetReadBuffer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextstreamprivate.html#resetReadBuffer
    """
    #  void QTextStreamPrivate::resetReadBuffer()
    self.uglySide.call('ritual_ZN18QTextStreamPrivate15resetReadBufferEv')

  def flushWriteBuffer(self) -> None:
    """
    Calls Qt's 'void QTextStreamPrivate::flushWriteBuffer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtextstreamprivate.html#flushWriteBuffer
    """
    #  void QTextStreamPrivate::flushWriteBuffer()
    self.uglySide.call('ritual_ZN18QTextStreamPrivate16flushWriteBufferEv')

  @staticmethod
  def fillReadBuffer(*__, **_) -> Never:
    """
    Qt's 'bool QTextStreamPrivate::fillReadBuffer(qint64 maxBytes)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier
    'QTEXTSTREAM_BUFFERSIZE'.
    """
    raise NotImplementedError(
        "'QTextStreamPrivate.fillReadBuffer' has no cute function yet. Qt's "
        "'bool QTextStreamPrivate::fillReadBuffer(qint64 maxBytes)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'QTEXTSTREAM_BUFFERSIZE'.")

  @staticmethod
  def getNumber(*__, **_) -> Never:
    """
    Qt's 'NumberParsingStatus QTextStreamPrivate::getNumber(qulonglong *l)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier 'isOctalDigit';
    did you mean 'QtMiscUtils::isOctalDigit'?.
    """
    raise NotImplementedError(
        "'QTextStreamPrivate.getNumber' has no cute function yet. Qt's "
        "'NumberParsingStatus QTextStreamPrivate::getNumber(qulonglong "
        "*l)': Qt's library has no name for it, and its code in Qt's source "
        "does not compile apart from its file: use of undeclared identifier "
        "'isOctalDigit'; did you mean 'QtMiscUtils::isOctalDigit'?.")

  @staticmethod
  def getReal(*__, **_) -> Never:
    """
    Qt's 'bool QTextStreamPrivate::getReal(double *f)': takes a number to
    change where it is.
    """
    raise NotImplementedError(
        "'QTextStreamPrivate.getReal' has no cute function yet. Qt's 'bool "
        "QTextStreamPrivate::getReal(double *f)': takes a number to change "
        "where it is.")

  @staticmethod
  def putChar(*__, **_) -> Never:
    """
    Qt's 'void QTextStreamPrivate::putChar(QChar ch)': leans on 'void
    QTextStreamPrivate::putStringImpl<QStringView>(QStringView,
    QTextStreamPrivate::PutStringMode)', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QTextStreamPrivate.putChar' has no cute function yet. Qt's 'void "
        "QTextStreamPrivate::putChar(QChar ch)': leans on 'void "
        "QTextStreamPrivate::putStringImpl<QStringView>(QStringView, "
        "QTextStreamPrivate::PutStringMode)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def putNumber(*__, **_) -> Never:
    """
    Qt's 'void QTextStreamPrivate::putNumber(qulonglong number, bool
    negative)': leans on 'void
    QTextStreamPrivate::putStringImpl<QStringView>(QStringView,
    QTextStreamPrivate::PutStringMode)', which Qt's source does not mark for
    use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QTextStreamPrivate.putNumber' has no cute function yet. Qt's "
        "'void QTextStreamPrivate::putNumber(qulonglong number, bool "
        "negative)': leans on 'void "
        "QTextStreamPrivate::putStringImpl<QStringView>(QStringView, "
        "QTextStreamPrivate::PutStringMode)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def putString(*__, **_) -> Never:
    """
    - Qt's 'void QTextStreamPrivate::putString(QStringView string,
      PutStringMode a1)': leans on 'void
      QTextStreamPrivate::putStringImpl<QStringView>(QStringView,
      QTextStreamPrivate::PutStringMode)', which Qt's source does not mark
      for use from outside Qt and has no code for that could be taken.
    - Qt's 'void QTextStreamPrivate::putString(QLatin1StringView data,
      PutStringMode a1)': leans on 'void
      QTextStreamPrivate::putStringImpl<QLatin1String>(QLatin1String,
      QTextStreamPrivate::PutStringMode)', which Qt's source does not mark
      for use from outside Qt and has no code for that could be taken.
    - Qt's 'void QTextStreamPrivate::putString(QUtf8StringView data,
      PutStringMode a1)': leans on 'void
      QTextStreamPrivate::putStringImpl<QStringView>(QStringView,
      QTextStreamPrivate::PutStringMode)', which Qt's source does not mark
      for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QTextStreamPrivate.putString' has no cute function yet. Qt's "
        "'void QTextStreamPrivate::putString(QStringView string, "
        "PutStringMode a1)': leans on 'void "
        "QTextStreamPrivate::putStringImpl<QStringView>(QStringView, "
        "QTextStreamPrivate::PutStringMode)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken. Qt's 'void QTextStreamPrivate::putString(QLatin1StringView "
        "data, PutStringMode a1)': leans on 'void "
        "QTextStreamPrivate::putStringImpl<QLatin1String>(QLatin1String, "
        "QTextStreamPrivate::PutStringMode)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken. Qt's 'void QTextStreamPrivate::putString(QUtf8StringView "
        "data, PutStringMode a1)': leans on 'void "
        "QTextStreamPrivate::putStringImpl<QStringView>(QStringView, "
        "QTextStreamPrivate::PutStringMode)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def putStringImpl(*__, **_) -> Never:
    """
    Qt's 'QTextStreamPrivate::putStringImpl': a template: a pattern and no
    single function.
    """
    raise NotImplementedError(
        "'QTextStreamPrivate.putStringImpl' has no cute function yet. Qt's "
        "'QTextStreamPrivate::putStringImpl': a template: a pattern and no "
        "single function.")

  @staticmethod
  def scan(*__, **_) -> Never:
    """
    Qt's 'bool QTextStreamPrivate::scan(const QChar **ptr, qsizetype
    *tokenLength, qsizetype maxlen, TokenDelimiter delimiter)': takes a type
    Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QTextStreamPrivate.scan' has no cute function yet. Qt's 'bool "
        "QTextStreamPrivate::scan(const QChar **ptr, qsizetype "
        "*tokenLength, qsizetype maxlen, TokenDelimiter delimiter)': takes "
        "a type Python has no way to hand over yet.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    - Qt's 'void QTextStreamPrivate::write(QStringView data)': leans on 'void
      QTextStreamPrivate::writeImpl<QStringView>(QStringView)', which Qt's
      source does not mark for use from outside Qt and has no code for that
      could be taken.
    - Qt's 'void QTextStreamPrivate::write(QChar ch)': leans on 'void
      QTextStreamPrivate::writeImpl<QChar>(QChar)', which Qt's source does
      not mark for use from outside Qt and has no code for that could be
      taken.
    - Qt's 'void QTextStreamPrivate::write(QLatin1StringView data)': leans on
      'void QTextStreamPrivate::writeImpl<QLatin1String>(QLatin1String)',
      which Qt's source does not mark for use from outside Qt and has no code
      for that could be taken.
    """
    raise NotImplementedError(
        "'QTextStreamPrivate.write' has no cute function yet. Qt's 'void "
        "QTextStreamPrivate::write(QStringView data)': leans on 'void "
        "QTextStreamPrivate::writeImpl<QStringView>(QStringView)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken. Qt's 'void "
        "QTextStreamPrivate::write(QChar ch)': leans on 'void "
        "QTextStreamPrivate::writeImpl<QChar>(QChar)', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken. Qt's 'void "
        "QTextStreamPrivate::write(QLatin1StringView data)': leans on 'void "
        "QTextStreamPrivate::writeImpl<QLatin1String>(QLatin1String)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

  @staticmethod
  def writeImpl(*__, **_) -> Never:
    """
    Qt's 'QTextStreamPrivate::writeImpl': a template: a pattern and no single
    function.
    """
    raise NotImplementedError(
        "'QTextStreamPrivate.writeImpl' has no cute function yet. Qt's "
        "'QTextStreamPrivate::writeImpl': a template: a pattern and no "
        "single function.")

  @staticmethod
  def writePadding(*__, **_) -> Never:
    """
    Qt's 'void QTextStreamPrivate::writePadding(qsizetype len)': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'QTEXTSTREAM_BUFFERSIZE'.
    """
    raise NotImplementedError(
        "'QTextStreamPrivate.writePadding' has no cute function yet. Qt's "
        "'void QTextStreamPrivate::writePadding(qsizetype len)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'QTEXTSTREAM_BUFFERSIZE'.")
