"""
QDtlsClientVerifier binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/qdtls.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QCryptographicHash, QObject

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QByteArray, QMetaObject
  from . import QDtlsClientVerifierPrivate, QHostAddress, QUdpSocket
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QByteArray = WAIT['QByteArray']
  QHostAddress = WAIT['QHostAddress']
  QUdpSocket = WAIT['QUdpSocket']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDtlsClientVerifier(QObject):
  """
  The cute side of Qt's QDtlsClientVerifier: a plain Python object standing
  in front of one C++ QDtlsClientVerifier.

  It is built on the cute 'QObject', as Qt's QDtlsClientVerifier is built on
  Qt's QObject, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QDtlsClientVerifier that has a ritual and that
  Python can call so far, 8 names in all: 'metaObject', 'tr',
  'setCookieGeneratorParameters', 'cookieGeneratorParameters',
  'verifyClient', 'verifiedHello', 'dtlsErrorString', 'd_func'. It can be
  made from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QDtlsClientVerifier::qt_metacast(const char *a0)': one of
    Qt's own inner workings.
  - Qt's 'int QDtlsClientVerifier::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QDtlsClientVerifier::~QDtlsClientVerifier()': the destructor:
    Python never removes a C++ QDtlsClientVerifier.
  - Qt's 'QDtlsError QDtlsClientVerifier::dtlsError() const': gives the enum
    'QDtlsError', whose class cannot be named here.
  - Qt's 'const QDtlsClientVerifierPrivate *QDtlsClientVerifier::d_func()
    const': takes in Python what 'QDtlsClientVerifierPrivate
    *QDtlsClientVerifier::d_func()' takes.

  What has no ritual
  ------------------

  4 of the 18 functions Qt declares: 2 not a gap; 2 forbidden.

  What to expect
  --------------

  - The C++ QDtlsClientVerifier is created at the first use, not by
    'QDtlsClientVerifier(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QDtlsClientVerifier.
  - Qt tells when it has removed the C++ QDtlsClientVerifier. Every call on
    the cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QDtlsClientVerifier that has no cute function yet,
    'dtlsError', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  #  The classes Qt writes inside QDtlsClientVerifier, each a class in here
  #  as in C++.

  class GeneratorParameters(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QDtlsClientVerifier::GeneratorParameters: a plain
    Python object standing in front of one C++
    QDtlsClientVerifier::GeneratorParameters.

    C++ hands a QDtlsClientVerifier::GeneratorParameters around as a copy, so
    every C++ QDtlsClientVerifier::GeneratorParameters behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QDtlsClientVerifier::GeneratorParameters yet. It can
    be made from Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QDtlsClientVerifier::GeneratorParameters::~GeneratorParameters()': the
      destructor: Python removes its C++
      QDtlsClientVerifier::GeneratorParameters by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QDtlsClientVerifier::GeneratorParameters is created at the
      first use, not by 'QDtlsClientVerifier::GeneratorParameters(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QDtlsClientVerifier::GeneratorParameters back gives
      a copy the ritual made for Python, in a new cute
      QDtlsClientVerifier::GeneratorParameters.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QByteArray = WAIT['QByteArray']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QDtlsClientVerifier::GeneratorParameters'

    #  Qt's '~QDtlsClientVerifier::GeneratorParameters()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QDtlsClientVerifier::GeneratorParameters behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN19QDtlsClientVerifier19GeneratorParametersD1Ev')

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
    def __init__(self) -> None:
      """
      Notes what was given, for Qt's
      'QDtlsClientVerifier::GeneratorParameters::GeneratorParameters()',
      which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qdtlsclientverifier-generatorparameters.html
      """
      #  QDtlsClientVerifier::GeneratorParameters::GeneratorParameters()
      self._noteCreation(
          QDtlsClientVerifier.GeneratorParameters, lambda: Rituals.call(
              'ritual_ZN19QDtlsClientVerifier19GeneratorParametersC1Ev',
          ))

    @overload(QCryptographicHash.Algorithm, QByteArray)
    def __init__(
        self,
        a: QCryptographicHash.Algorithm,
        s: QByteArray,
    ) -> None:
      """
      Notes what was given, for Qt's
      'QDtlsClientVerifier::GeneratorParameters::GeneratorParameters(
      QCryptographicHash::Algorithm a, const QByteArray &s)', which is called
      at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qdtlsclientverifier-generatorparameters.html

      Parameters
      ----------

      a : QCryptographicHash.Algorithm
        Passed on as its number.

      s : QByteArray
        Passed on as a value: Qt reads the C++ QByteArray, which stays
        Python's own.
      """
      #  QDtlsClientVerifier::GeneratorParameters::GeneratorParameters(
      #      QCryptographicHash::Algorithm a, const QByteArray &s)
      self._noteCreation(
          QDtlsClientVerifier.GeneratorParameters, lambda: Rituals.call(
              'ritual_ZN19QDtlsClientVerifier19GeneratorParametersC1EN18QCr'
              'yptographicHash9AlgorithmERK10QByteArray',
              a.value, self._valueOf(s),
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
    Calls Qt's 'QString QDtlsClientVerifier::tr(const char *s, const char *c,
    int n)'.

    Qt's own words: https://doc.qt.io/qt-6/qdtlsclientverifier.html#tr

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
    #  QString QDtlsClientVerifier::tr(const char *s, const char *c, int n)
    return Rituals.call(
        'ritual_ZN19QDtlsClientVerifier2trEPKcS1_i',
        CuteMixin._bytesOf(s), CuteMixin._bytesOf(c), n,
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDtlsClientVerifier'

  #  A C++ QDtlsClientVerifier Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDtlsClientVerifier'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QDtlsClientVerifier::metaObject() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdtlsclientverifier.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QDtlsClientVerifier::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK19QDtlsClientVerifier10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def cookieGeneratorParameters(self) -> GeneratorParameters:
    """
    Calls Qt's 'GeneratorParameters
    QDtlsClientVerifier::cookieGeneratorParameters() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdtlsclientverifier.html#cookieGeneratorParameters

    Returns
    -------

    GeneratorParameters
      A new cute QDtlsClientVerifier::GeneratorParameters around the copy Qt
      gave back. Python owns it.
    """
    #  GeneratorParameters QDtlsClientVerifier::cookieGeneratorParameters()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK19QDtlsClientVerifier25cookieGeneratorParametersEv',
    )
    return QDtlsClientVerifier.GeneratorParameters._cuteOwning(address)

  def verifiedHello(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QDtlsClientVerifier::verifiedHello() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdtlsclientverifier.html#verifiedHello

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QDtlsClientVerifier::verifiedHello() const
    address = self.uglySide.call(
        'ritual_ZNK19QDtlsClientVerifier13verifiedHelloEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

  def dtlsErrorString(self) -> str:
    """
    Calls Qt's 'QString QDtlsClientVerifier::dtlsErrorString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdtlsclientverifier.html#dtlsErrorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDtlsClientVerifier::dtlsErrorString() const
    return self.uglySide.call(
        'ritual_ZNK19QDtlsClientVerifier15dtlsErrorStringEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(GeneratorParameters)
  def setCookieGeneratorParameters(
      self,
      params: GeneratorParameters,
  ) -> bool:
    """
    Calls Qt's 'bool QDtlsClientVerifier::setCookieGeneratorParameters(const
    GeneratorParameters &params)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdtlsclientverifier.html

    Parameters
    ----------

    params : GeneratorParameters
      Passed on as a value: Qt reads the C++
      QDtlsClientVerifier::GeneratorParameters, which stays Python's own.
    """
    #  bool QDtlsClientVerifier::setCookieGeneratorParameters(const
    #      GeneratorParameters &params)
    return self.uglySide.call(
        'ritual_ZN19QDtlsClientVerifier28setCookieGeneratorParametersERKNS_'
        '19GeneratorParametersE',
        self._valueOf(params),
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
    'QDtlsClientVerifier::QDtlsClientVerifier(QObject *parent)', which is
    called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qdtlsclientverifier.html#QDtlsClientVerifier

    Parameters
    ----------

    parent : Optional[QObject]
      Passed on as the address of its C++ object. None is passed on as no
      object. May be left out, as in Qt: it is then None.
    """
    #  QDtlsClientVerifier::QDtlsClientVerifier(QObject *parent)
    self._noteCreation(QDtlsClientVerifier, lambda: Rituals.call(
        'ritual_ZN19QDtlsClientVerifierC1EP7QObject',
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

  @overload(QUdpSocket, QByteArray, QHostAddress, int)
  @overload(NoneType, QByteArray, QHostAddress, int)
  def verifyClient(
      self,
      socket: Optional[QUdpSocket],
      dgram: QByteArray,
      address: QHostAddress,
      port: int,
  ) -> bool:
    """
    Calls Qt's 'bool QDtlsClientVerifier::verifyClient(QUdpSocket *socket,
    const QByteArray &dgram, const QHostAddress &address, quint16 port)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdtlsclientverifier.html#verifyClient

    Parameters
    ----------

    socket : Optional[QUdpSocket]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    dgram : QByteArray
      Passed on as a value: Qt reads the C++ QByteArray, which stays Python's
      own.

    address : QHostAddress
      Passed on as a value: Qt reads the C++ QHostAddress, which stays
      Python's own.

    port : int
      Passed on as it is.
    """
    #  bool QDtlsClientVerifier::verifyClient(QUdpSocket *socket, const
    #      QByteArray &dgram, const QHostAddress &address, quint16 port)
    return self.uglySide.call(
        'ritual_ZN19QDtlsClientVerifier12verifyClientEP10QUdpSocketRK10QByt'
        'eArrayRK12QHostAddresst',
        self._addressOf(socket), self._valueOf(dgram),
        self._valueOf(address), port,
    )

  def d_func(self) -> Optional[QDtlsClientVerifierPrivate]:
    """
    Calls Qt's 'QDtlsClientVerifierPrivate *QDtlsClientVerifier::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qdtlsclientverifier.html#d_func

    Returns
    -------

    Optional[QDtlsClientVerifierPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDtlsClientVerifierPrivate *QDtlsClientVerifier::d_func()
    address = self.uglySide.call('ritual_ZN19QDtlsClientVerifier6d_funcEv')
    from . import QDtlsClientVerifierPrivate
    return QDtlsClientVerifierPrivate._cuteAt(address)

  @staticmethod
  def dtlsError(*__, **_) -> Never:
    """
    Qt's 'QDtlsError QDtlsClientVerifier::dtlsError() const': gives the enum
    'QDtlsError', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QDtlsClientVerifier.dtlsError' has no cute function yet. Qt's "
        "'QDtlsError QDtlsClientVerifier::dtlsError() const': gives the "
        "enum 'QDtlsError', whose class cannot be named here.")
