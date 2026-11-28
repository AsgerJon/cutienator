"""
QQmlGrpcChannelOptions binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtGrpcQuick/6.12.0/QtGrpcQuick/private/qqmlgrpcchanneloptions_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQmlGrpcChannelOptions to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, WAIT
from ..occult import Rituals
from ..QtCore import QObject
from ..QtGrpc import QtGrpc

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from ..QtCore import QMetaObject
  from . import QQmlGrpcMetadata
  from ..QtGrpc import QGrpcChannelOptions
  from ..QtQmlNetwork import QQmlSslConfiguration
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlGrpcMetadata = WAIT['QQmlGrpcMetadata']
  QQmlSslConfiguration = WAIT['QQmlSslConfiguration']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlGrpcChannelOptions(QObject):
  """
  The cute side of Qt's QQmlGrpcChannelOptions: a plain Python object
  standing in front of one C++ QQmlGrpcChannelOptions.

  It is built on the cute 'QObject', as Qt's QQmlGrpcChannelOptions is built
  on Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QQmlGrpcChannelOptions that has a ritual and that
  Python can call so far, 15 names in all: 'metaObject', 'tr', 'options',
  'deadlineTimeout', 'setDeadlineTimeout', 'metadata', 'setMetadata',
  'serializationFormat', 'setSerializationFormat', 'sslConfiguration',
  'setSslConfiguration', 'deadlineTimeoutChanged', 'metadataChanged',
  'serializationFormatChanged', 'sslConfigurationChanged'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QQmlGrpcChannelOptions::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QQmlGrpcChannelOptions::qt_metacall(QMetaObject::Call a0, int
    a1, void **a2)': one of Qt's own inner workings.
  - Qt's 'QQmlGrpcChannelOptions::~QQmlGrpcChannelOptions()': the destructor:
    Python never removes a C++ QQmlGrpcChannelOptions.
  - Qt's 'QQmlGrpcChannelOptionsPrivate *QQmlGrpcChannelOptions::d_func()':
    gives 'QQmlGrpcChannelOptionsPrivate', which has no cute class yet.
  - Qt's 'const QQmlGrpcChannelOptionsPrivate
    *QQmlGrpcChannelOptions::d_func() const': gives
    'QQmlGrpcChannelOptionsPrivate', which has no cute class yet.

  What has no ritual
  ------------------

  7 of the 28 functions Qt declares: 5 forbidden; 2 not a gap.

  What to expect
  --------------

  - The C++ QQmlGrpcChannelOptions is created at the first use, not by
    'QQmlGrpcChannelOptions(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlGrpcChannelOptions.
  - Qt tells when it has removed the C++ QQmlGrpcChannelOptions. Every call
    on the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  """

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
    Calls Qt's 'QString QQmlGrpcChannelOptions::tr(const char *s, const char
    *c, int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlgrpcchanneloptions.html#tr

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
    #  QString QQmlGrpcChannelOptions::tr(const char *s, const char *c, int
    #      n)
    return Rituals.call(
        'ritual_ZN22QQmlGrpcChannelOptions2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlGrpcChannelOptions'

  #  A C++ QQmlGrpcChannelOptions Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QQmlGrpcChannelOptions'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlGrpcChannelOptions::metaObject()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlgrpcchanneloptions.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlGrpcChannelOptions::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK22QQmlGrpcChannelOptions10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def options(self) -> QGrpcChannelOptions:
    """
    Calls Qt's 'const QGrpcChannelOptions &QQmlGrpcChannelOptions::options()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlgrpcchanneloptions.html#options

    Returns
    -------

    QGrpcChannelOptions
      A new cute QGrpcChannelOptions around the copy Qt gave back. Python
      owns it.
    """
    #  const QGrpcChannelOptions &QQmlGrpcChannelOptions::options() const
    address = self.uglySide.call(
        'ritual_ZNKR22QQmlGrpcChannelOptions7optionsEv',
    )
    from ..QtGrpc import QGrpcChannelOptions
    return QGrpcChannelOptions._cuteOwning(address)

  def deadlineTimeout(self) -> int:
    """
    Calls Qt's 'qint64 QQmlGrpcChannelOptions::deadlineTimeout() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlgrpcchanneloptions.html#deadlineTimeout
    """
    #  qint64 QQmlGrpcChannelOptions::deadlineTimeout() const
    return self.uglySide.call(
        'ritual_ZNK22QQmlGrpcChannelOptions15deadlineTimeoutEv',
    )

  def metadata(self) -> Optional[QQmlGrpcMetadata]:
    """
    Calls Qt's 'QQmlGrpcMetadata *QQmlGrpcChannelOptions::metadata() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlgrpcchanneloptions.html#metadata

    Returns
    -------

    Optional[QQmlGrpcMetadata]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlGrpcMetadata *QQmlGrpcChannelOptions::metadata() const
    address = self.uglySide.call(
        'ritual_ZNK22QQmlGrpcChannelOptions8metadataEv',
    )
    from . import QQmlGrpcMetadata
    return QQmlGrpcMetadata._cuteAt(address)

  def serializationFormat(self) -> QtGrpc.SerializationFormat:
    """
    Calls Qt's 'QtGrpc::SerializationFormat
    QQmlGrpcChannelOptions::serializationFormat() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlgrpcchanneloptions.html#serializationFormat

    Returns
    -------

    QtGrpc.SerializationFormat
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QtGrpc.SerializationFormat(number)' gives.
    """
    #  QtGrpc::SerializationFormat
    #      QQmlGrpcChannelOptions::serializationFormat() const
    return QtGrpc.SerializationFormat(self.uglySide.call(
        'ritual_ZNK22QQmlGrpcChannelOptions19serializationFormatEv',
    ))

  def sslConfiguration(self) -> QQmlSslConfiguration:
    """
    Calls Qt's 'QQmlSslConfiguration
    QQmlGrpcChannelOptions::sslConfiguration() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlgrpcchanneloptions.html#sslConfiguration

    Returns
    -------

    QQmlSslConfiguration
      A new cute QQmlSslConfiguration around the copy Qt gave back. Python
      owns it.
    """
    #  QQmlSslConfiguration QQmlGrpcChannelOptions::sslConfiguration() const
    address = self.uglySide.call(
        'ritual_ZNK22QQmlGrpcChannelOptions16sslConfigurationEv',
    )
    from ..QtQmlNetwork import QQmlSslConfiguration
    return QQmlSslConfiguration._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setDeadlineTimeout(self, value: int) -> None:
    """
    Calls Qt's 'void QQmlGrpcChannelOptions::setDeadlineTimeout(qint64
    value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlgrpcchanneloptions.html#setDeadlineTimeout

    Parameters
    ----------

    value : int
      Passed on as it is.
    """
    #  void QQmlGrpcChannelOptions::setDeadlineTimeout(qint64 value)
    self.uglySide.call(
        'ritual_ZN22QQmlGrpcChannelOptions18setDeadlineTimeoutEx', value,
    )

  @overload(QQmlGrpcMetadata)
  @overload(NoneType)
  def setMetadata(self, value: Optional[QQmlGrpcMetadata]) -> None:
    """
    Calls Qt's 'void QQmlGrpcChannelOptions::setMetadata(QQmlGrpcMetadata
    *value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlgrpcchanneloptions.html#setMetadata

    Parameters
    ----------

    value : Optional[QQmlGrpcMetadata]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QQmlGrpcChannelOptions::setMetadata(QQmlGrpcMetadata *value)
    self.uglySide.call(
        'ritual_ZN22QQmlGrpcChannelOptions11setMetadataEP16QQmlGrpcMetadata',
        self._addressOf(value),
    )

  @overload(QtGrpc.SerializationFormat)
  def setSerializationFormat(
      self,
      format: QtGrpc.SerializationFormat,
  ) -> None:
    """
    Calls Qt's 'void QQmlGrpcChannelOptions::setSerializationFormat(QtGrpc::
    SerializationFormat format)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlgrpcchanneloptions.html#setSerializationFormat

    Parameters
    ----------

    format : QtGrpc.SerializationFormat
      Passed on as its number.
    """
    #  void QQmlGrpcChannelOptions::setSerializationFormat(QtGrpc::
    #      SerializationFormat format)
    self.uglySide.call(
        'ritual_ZN22QQmlGrpcChannelOptions22setSerializationFormatEN6QtGrpc'
        '19SerializationFormatE',
        format.value,
    )

  @overload(QQmlSslConfiguration)
  def setSslConfiguration(self, config: QQmlSslConfiguration) -> None:
    """
    Calls Qt's 'void QQmlGrpcChannelOptions::setSslConfiguration(const
    QQmlSslConfiguration &config)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlgrpcchanneloptions.html#setSslConfiguration

    Parameters
    ----------

    config : QQmlSslConfiguration
      Passed on as a value: Qt reads the C++ QQmlSslConfiguration, which
      stays Python's own.
    """
    #  void QQmlGrpcChannelOptions::setSslConfiguration(const
    #      QQmlSslConfiguration &config)
    self.uglySide.call(
        'ritual_ZN22QQmlGrpcChannelOptions19setSslConfigurationERK20QQmlSsl'
        'Configuration',
        self._valueOf(config),
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
  @overload(QObject)
  @overload(NoneType)
  def __init__(self, parent: Optional[QObject] = None) -> None:
    """
    Notes what was given, for Qt's
    'QQmlGrpcChannelOptions::QQmlGrpcChannelOptions(QObject *parent)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlgrpcchanneloptions.html#QQmlGrpcChannelOptions

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QQmlGrpcChannelOptions::QQmlGrpcChannelOptions(QObject *parent)
    self._noteCreation(QQmlGrpcChannelOptions, lambda: Rituals.call(
        'ritual_ZN22QQmlGrpcChannelOptionsC1EP7QObject',
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

  def deadlineTimeoutChanged(self) -> None:
    """
    Calls Qt's 'void QQmlGrpcChannelOptions::deadlineTimeoutChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlgrpcchanneloptions.html#deadlineTimeoutChanged
    """
    #  void QQmlGrpcChannelOptions::deadlineTimeoutChanged()
    self.uglySide.call(
        'ritual_ZN22QQmlGrpcChannelOptions22deadlineTimeoutChangedEv',
    )

  def metadataChanged(self) -> None:
    """
    Calls Qt's 'void QQmlGrpcChannelOptions::metadataChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlgrpcchanneloptions.html#metadataChanged
    """
    #  void QQmlGrpcChannelOptions::metadataChanged()
    self.uglySide.call(
        'ritual_ZN22QQmlGrpcChannelOptions15metadataChangedEv',
    )

  def serializationFormatChanged(self) -> None:
    """
    Calls Qt's 'void QQmlGrpcChannelOptions::serializationFormatChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlgrpcchanneloptions.html
    """
    #  void QQmlGrpcChannelOptions::serializationFormatChanged()
    self.uglySide.call(
        'ritual_ZN22QQmlGrpcChannelOptions26serializationFormatChangedEv',
    )

  def sslConfigurationChanged(self) -> None:
    """
    Calls Qt's 'void QQmlGrpcChannelOptions::sslConfigurationChanged()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmlgrpcchanneloptions.html
    """
    #  void QQmlGrpcChannelOptions::sslConfigurationChanged()
    self.uglySide.call(
        'ritual_ZN22QQmlGrpcChannelOptions23sslConfigurationChangedEv',
    )
