"""
QCanFrameProcessorPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtSerialBus/6.12.0/QtSerialBus/private/qcanframeprocessor_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QCanFrameProcessorPrivate to be private: it declares the class in
#  a header it calls private. cutienator does not care. Qt hands objects of
#  the class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from . import QCanFrameProcessor

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class QCanFrameProcessorPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QCanFrameProcessorPrivate: a plain Python object
  standing in front of one C++ QCanFrameProcessorPrivate.

  C++ hands a QCanFrameProcessorPrivate around as a copy, so every C++
  QCanFrameProcessorPrivate behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QCanFrameProcessorPrivate that has a ritual and that
  Python can call so far, 3 names in all: 'resetErrors', 'setError',
  'addWarning'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QCanFrameProcessorPrivate *QCanFrameProcessorPrivate::get(const
    QCanFrameProcessor &processor)': takes a type Python has no way to hand
    over yet.
  - Qt's 'QCanFrameProcessorPrivate::~QCanFrameProcessorPrivate()': the
    destructor: Python removes its C++ QCanFrameProcessorPrivate by it, and
    has no other use for it.

  What has no ritual
  ------------------

  5 of the 10 functions Qt declares: 4 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 leans on
  'QCanFrameProcessorPrivate.

  What to expect
  --------------

  - The C++ QCanFrameProcessorPrivate is created at the first use, not by
    'QCanFrameProcessorPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QCanFrameProcessorPrivate back gives a copy the
    ritual made for Python, in a new cute QCanFrameProcessorPrivate.
  - Each name of Qt's QCanFrameProcessorPrivate that has no cute function
    yet, 'decodeSignal', 'encodeSignal', 'extractUniqueId', 'fillUniqueId',
    'get', 'parseData', holds a function that raises 'NotImplementedError',
    and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QCanFrameProcessorPrivate'

  #  Qt's '~QCanFrameProcessorPrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QCanFrameProcessorPrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN25QCanFrameProcessorPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QCanFrameProcessor.Error, str)
  def setError(self, err: QCanFrameProcessor.Error, desc: str) -> None:
    """
    Calls Qt's 'void
    QCanFrameProcessorPrivate::setError(QCanFrameProcessor::Error err, const
    QString &desc)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanframeprocessorprivate.html#setError

    Parameters
    ----------

    err : QCanFrameProcessor.Error
      Passed on as its number.

    desc : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QCanFrameProcessorPrivate::setError(QCanFrameProcessor::Error
    #      err, const QString &desc)
    self.uglySide.call(
        'ritual_ZN25QCanFrameProcessorPrivate8setErrorEN18QCanFrameProcesso'
        'r5ErrorERK7QString',
        err.value, desc,
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

  def resetErrors(self) -> None:
    """
    Calls Qt's 'void QCanFrameProcessorPrivate::resetErrors()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanframeprocessorprivate.html#resetErrors
    """
    #  void QCanFrameProcessorPrivate::resetErrors()
    self.uglySide.call('ritual_ZN25QCanFrameProcessorPrivate11resetErrorsEv')

  @overload(str)
  def addWarning(self, warning: str) -> None:
    """
    Calls Qt's 'void QCanFrameProcessorPrivate::addWarning(const QString
    &warning)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qcanframeprocessorprivate.html#addWarning

    Parameters
    ----------

    warning : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QCanFrameProcessorPrivate::addWarning(const QString &warning)
    self.uglySide.call(
        'ritual_ZN25QCanFrameProcessorPrivate10addWarningERK7QString',
        warning,
    )

  @staticmethod
  def decodeSignal(*__, **_) -> Never:
    """
    Qt's 'QVariant QCanFrameProcessorPrivate::decodeSignal(const QCanBusFrame
    &frame, const QCanSignalDescription &signalDesc)': leans on
    'QCanFrameProcessorPrivate::parseData(unsigned char const*,
    QCanSignalDescription const&)', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QCanFrameProcessorPrivate.decodeSignal' has no cute function yet. "
        "Qt's 'QVariant QCanFrameProcessorPrivate::decodeSignal(const "
        "QCanBusFrame &frame, const QCanSignalDescription &signalDesc)': "
        "leans on 'QCanFrameProcessorPrivate::parseData(unsigned char "
        "const*, QCanSignalDescription const&)', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def encodeSignal(*__, **_) -> Never:
    """
    Qt's 'void QCanFrameProcessorPrivate::encodeSignal(unsigned char *data,
    const QVariant &value, const QCanSignalDescription &signalDesc)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'encodeValue'.
    """
    raise NotImplementedError(
        "'QCanFrameProcessorPrivate.encodeSignal' has no cute function yet. "
        "Qt's 'void QCanFrameProcessorPrivate::encodeSignal(unsigned char "
        "*data, const QVariant &value, const QCanSignalDescription "
        "&signalDesc)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'encodeValue'.")

  @staticmethod
  def extractUniqueId(*__, **_) -> Never:
    """
    Qt's 'std::optional<QtCanBus::UniqueId>
    QCanFrameProcessorPrivate::extractUniqueId(const QCanBusFrame &frame)
    const': Qt's library has no name for it, and its code in Qt's source does
    not compile apart from its file: use of undeclared identifier
    'extractMaxBitNum'.
    """
    raise NotImplementedError(
        "'QCanFrameProcessorPrivate.extractUniqueId' has no cute function "
        "yet. Qt's 'std::optional<QtCanBus::UniqueId> "
        "QCanFrameProcessorPrivate::extractUniqueId(const QCanBusFrame "
        "&frame) const': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'extractMaxBitNum'.")

  @staticmethod
  def fillUniqueId(*__, **_) -> Never:
    """
    Qt's 'bool QCanFrameProcessorPrivate::fillUniqueId(unsigned char *data,
    quint16 sizeInBits, QtCanBus::UniqueId uniqueId)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'extractMaxBitNum'.
    """
    raise NotImplementedError(
        "'QCanFrameProcessorPrivate.fillUniqueId' has no cute function yet. "
        "Qt's 'bool QCanFrameProcessorPrivate::fillUniqueId(unsigned char "
        "*data, quint16 sizeInBits, QtCanBus::UniqueId uniqueId)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'extractMaxBitNum'.")

  @staticmethod
  def get(*__, **_) -> Never:
    """
    Qt's 'QCanFrameProcessorPrivate *QCanFrameProcessorPrivate::get(const
    QCanFrameProcessor &processor)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QCanFrameProcessorPrivate.get' has no cute function yet. Qt's "
        "'QCanFrameProcessorPrivate *QCanFrameProcessorPrivate::get(const "
        "QCanFrameProcessor &processor)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def parseData(*__, **_) -> Never:
    """
    Qt's 'QVariant QCanFrameProcessorPrivate::parseData(const unsigned char
    *data, const QCanSignalDescription &signalDesc)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'extractValue'.
    """
    raise NotImplementedError(
        "'QCanFrameProcessorPrivate.parseData' has no cute function yet. "
        "Qt's 'QVariant QCanFrameProcessorPrivate::parseData(const unsigned "
        "char *data, const QCanSignalDescription &signalDesc)': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'extractValue'.")
