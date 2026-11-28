"""
QCanFrameProcessor binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSerialBus/qcanframeprocessor.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList, QStringList

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QCanBusFrame, QCanMessageDescription, QCanUniqueIdDescription
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QCanBusFrame = WAIT['QCanBusFrame']
  QCanMessageDescription = WAIT['QCanMessageDescription']
  QCanUniqueIdDescription = WAIT['QCanUniqueIdDescription']


class QCanFrameProcessor(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCanFrameProcessor: a plain Python object standing in
  front of one C++ QCanFrameProcessor.

  What exists
  -----------

  Every function of Qt's QCanFrameProcessor that has a ritual and that Python
  can call so far, 10 names in all: 'parseFrame', 'error', 'errorString',
  'warnings', 'messageDescriptions', 'addMessageDescriptions',
  'setMessageDescriptions', 'clearMessageDescriptions',
  'uniqueIdDescription', 'setUniqueIdDescription'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCanFrameProcessor::~QCanFrameProcessor()': the destructor: Python
    never removes a C++ QCanFrameProcessor.
  - Qt's 'QCanBusFrame QCanFrameProcessor::prepareFrame(QtCanBus::UniqueId
    uniqueId, const QVariantMap &signalValues)': names the enum
    'QtCanBus::UniqueId', whose class cannot be named here.

  What has no ritual
  ------------------

  4 of the 17 functions Qt declares: 4 forbidden.

  What to expect
  --------------

  - The C++ QCanFrameProcessor is created at the first use, not by
    'QCanFrameProcessor(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QCanFrameProcessor.
  - Each name of Qt's QCanFrameProcessor that has no cute function yet,
    'prepareFrame', holds a function that raises 'NotImplementedError', and
    its docstring says why.
  """

  #  The enums Qt writes inside QCanFrameProcessor, each a class in here as
  #  in C++, and the names Qt has for the combinations of its flags enums.

  class Error(CuteNum, scoped=True):
    """
    The enum 'QCanFrameProcessor::Error' of Qt, with the 5 names Qt gives in
    it. C++ keeps these names inside the enum, so the class that holds the
    enum does not have them.
    """

    NULL = Kee[int](0)
    InvalidFrame = Kee[int](1)
    UnsupportedFrameFormat = Kee[int](2)
    Decoding = Kee[int](3)
    Encoding = Kee[int](4)

  #  The classes Qt writes inside QCanFrameProcessor, each a class in here as
  #  in C++.

  class ParseResult(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QCanFrameProcessor::ParseResult: a plain Python
    object standing in front of one C++ QCanFrameProcessor::ParseResult.

    C++ hands a QCanFrameProcessor::ParseResult around as a copy, so every
    C++ QCanFrameProcessor::ParseResult behind a cute one is Python's own: it
    is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QCanFrameProcessor::ParseResult yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QCanFrameProcessor::ParseResult::~ParseResult()': the destructor:
      Python removes its C++ QCanFrameProcessor::ParseResult by it, and has
      no other use for it.

    What to expect
    --------------

    - The C++ QCanFrameProcessor::ParseResult is created at the first use,
      not by 'QCanFrameProcessor::ParseResult(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QCanFrameProcessor::ParseResult back gives a copy
      the ritual made for Python, in a new cute
      QCanFrameProcessor::ParseResult.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QCanFrameProcessor::ParseResult'

    #  Qt's '~QCanFrameProcessor::ParseResult()'. Naming it makes this a
    #  value class: Python owns every C++ QCanFrameProcessor::ParseResult
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN18QCanFrameProcessor11ParseResultD1Ev'

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCanFrameProcessor'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def error(self) -> Error:
    """
    Calls Qt's 'Error QCanFrameProcessor::error() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanframeprocessor.html#error

    Returns
    -------

    Error
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'Error(number)' gives.
    """
    #  Error QCanFrameProcessor::error() const
    return QCanFrameProcessor.Error(self.uglySide.call(
        'ritual_ZNK18QCanFrameProcessor5errorEv',
    ))

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QCanFrameProcessor::errorString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanframeprocessor.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QCanFrameProcessor::errorString() const
    return self.uglySide.call(
        'ritual_ZNK18QCanFrameProcessor11errorStringEv',
    )

  def warnings(self) -> QStringList:
    """
    Calls Qt's 'QStringList QCanFrameProcessor::warnings() const'.

    Qt's own words: https://doc.qt.io/qt-6/qcanframeprocessor.html#warnings

    Returns
    -------

    QStringList
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QStringList QCanFrameProcessor::warnings() const
    address = self.uglySide.call('ritual_ZNK18QCanFrameProcessor8warningsEv')
    return QStringList._cuteOwning(address)

  def messageDescriptions(self) -> QList[QCanMessageDescription]:
    """
    Calls Qt's 'QList<QCanMessageDescription>
    QCanFrameProcessor::messageDescriptions() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanframeprocessor.html#messageDescriptions

    Returns
    -------

    QList[QCanMessageDescription]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QCanMessageDescription>
    #      QCanFrameProcessor::messageDescriptions() const
    address = self.uglySide.call(
        'ritual_ZNK18QCanFrameProcessor19messageDescriptionsEv',
    )
    from . import QCanMessageDescription
    return QList[QCanMessageDescription]._cuteOwning(address)

  def uniqueIdDescription(self) -> QCanUniqueIdDescription:
    """
    Calls Qt's 'QCanUniqueIdDescription
    QCanFrameProcessor::uniqueIdDescription() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanframeprocessor.html#uniqueIdDescription

    Returns
    -------

    QCanUniqueIdDescription
      A new cute QCanUniqueIdDescription around the copy Qt gave back. Python
      owns it.
    """
    #  QCanUniqueIdDescription QCanFrameProcessor::uniqueIdDescription()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK18QCanFrameProcessor19uniqueIdDescriptionEv',
    )
    from . import QCanUniqueIdDescription
    return QCanUniqueIdDescription._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QList[QCanMessageDescription])
  def setMessageDescriptions(
      self,
      descriptions: QList[QCanMessageDescription],
  ) -> None:
    """
    Calls Qt's 'void QCanFrameProcessor::setMessageDescriptions(const
    QList<QCanMessageDescription> &descriptions)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanframeprocessor.html#setMessageDescriptions

    Parameters
    ----------

    descriptions : QList[QCanMessageDescription]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QCanFrameProcessor::setMessageDescriptions(const
    #      QList<QCanMessageDescription> &descriptions)
    self.uglySide.call(
        'ritual_ZN18QCanFrameProcessor22setMessageDescriptionsERK5QListI22Q'
        'CanMessageDescriptionE',
        self._valueOf(descriptions),
    )

  @overload(QCanUniqueIdDescription)
  def setUniqueIdDescription(
      self,
      description: QCanUniqueIdDescription,
  ) -> None:
    """
    Calls Qt's 'void QCanFrameProcessor::setUniqueIdDescription(const
    QCanUniqueIdDescription &description)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanframeprocessor.html#setUniqueIdDescription

    Parameters
    ----------

    description : QCanUniqueIdDescription
      Passed on as a value: Qt reads the C++ QCanUniqueIdDescription, which
      stays Python's own.
    """
    #  void QCanFrameProcessor::setUniqueIdDescription(const
    #      QCanUniqueIdDescription &description)
    self.uglySide.call(
        'ritual_ZN18QCanFrameProcessor22setUniqueIdDescriptionERK23QCanUniq'
        'ueIdDescription',
        self._valueOf(description),
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
    Notes what was given, for Qt's
    'QCanFrameProcessor::QCanFrameProcessor()', which is called at the first
    use.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanframeprocessor.html#QCanFrameProcessor
    """
    #  QCanFrameProcessor::QCanFrameProcessor()
    self._noteCreation(QCanFrameProcessor, lambda: Rituals.call(
        'ritual_ZN18QCanFrameProcessorC1Ev',
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

  @overload(QCanBusFrame)
  def parseFrame(self, frame: QCanBusFrame) -> ParseResult:
    """
    Calls Qt's 'ParseResult QCanFrameProcessor::parseFrame(const QCanBusFrame
    &frame)'.

    Qt's own words: https://doc.qt.io/qt-6/qcanframeprocessor.html#parseFrame

    Parameters
    ----------

    frame : QCanBusFrame
      Passed on as a value: Qt reads the C++ QCanBusFrame, which stays
      Python's own.

    Returns
    -------

    ParseResult
      A new cute QCanFrameProcessor::ParseResult around the copy Qt gave
      back. Python owns it.
    """
    #  ParseResult QCanFrameProcessor::parseFrame(const QCanBusFrame &frame)
    address = self.uglySide.call(
        'ritual_ZN18QCanFrameProcessor10parseFrameERK12QCanBusFrame',
        self._valueOf(frame),
    )
    return QCanFrameProcessor.ParseResult._cuteOwning(address)

  @overload(QList[QCanMessageDescription])
  def addMessageDescriptions(
      self,
      descriptions: QList[QCanMessageDescription],
  ) -> None:
    """
    Calls Qt's 'void QCanFrameProcessor::addMessageDescriptions(const
    QList<QCanMessageDescription> &descriptions)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanframeprocessor.html#addMessageDescriptions

    Parameters
    ----------

    descriptions : QList[QCanMessageDescription]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QCanFrameProcessor::addMessageDescriptions(const
    #      QList<QCanMessageDescription> &descriptions)
    self.uglySide.call(
        'ritual_ZN18QCanFrameProcessor22addMessageDescriptionsERK5QListI22Q'
        'CanMessageDescriptionE',
        self._valueOf(descriptions),
    )

  def clearMessageDescriptions(self) -> None:
    """
    Calls Qt's 'void QCanFrameProcessor::clearMessageDescriptions()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanframeprocessor.html#clearMessageDescriptions
    """
    #  void QCanFrameProcessor::clearMessageDescriptions()
    self.uglySide.call(
        'ritual_ZN18QCanFrameProcessor24clearMessageDescriptionsEv',
    )

  @staticmethod
  def prepareFrame(*__, **_) -> Never:
    """
    Qt's 'QCanBusFrame QCanFrameProcessor::prepareFrame(QtCanBus::UniqueId
    uniqueId, const QVariantMap &signalValues)': names the enum
    'QtCanBus::UniqueId', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QCanFrameProcessor.prepareFrame' has no cute function yet. Qt's "
        "'QCanBusFrame QCanFrameProcessor::prepareFrame(QtCanBus::UniqueId "
        "uniqueId, const QVariantMap &signalValues)': names the enum "
        "'QtCanBus::UniqueId', whose class cannot be named here.")
