"""
QTlsPrivate::DtlsBase binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qtlsbackend_p.h, Qt 6.12.0. Changes
#  made here are lost.
#
#  Qt means QTlsPrivate::DtlsBase to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from . import QDtlsClientVerifier

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from . import QSslConfiguration
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QSslConfiguration = WAIT['QSslConfiguration']


class DtlsBase(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QTlsPrivate::DtlsBase: a plain Python object standing
  in front of one C++ QTlsPrivate::DtlsBase.

  What exists
  -----------

  Every function of Qt's QTlsPrivate::DtlsBase that has a ritual and that
  Python can call so far, 6 names in all: 'errorString', 'clearDtlsError',
  'setConfiguration', 'configuration', 'setCookieGeneratorParameters',
  'cookieGeneratorParameters'. None can be made from Python: one comes out of
  a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QTlsPrivate::DtlsBase::~DtlsBase()': the destructor: Python never
    removes a C++ QTlsPrivate::DtlsBase.
  - Qt's 'void QTlsPrivate::DtlsBase::setDtlsError(QDtlsError code, const
    QString &description)': names the enum 'QDtlsError', whose class cannot
    be named here.
  - Qt's 'QDtlsError QTlsPrivate::DtlsBase::error() const': gives the enum
    'QDtlsError', whose class cannot be named here.

  What to expect
  --------------

  - The C++ QTlsPrivate::DtlsBase is created at the first use, not by
    'QTlsPrivate::DtlsBase(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QTlsPrivate::DtlsBase.
  - Each name of Qt's QTlsPrivate::DtlsBase that has no cute function yet,
    'error', 'setDtlsError', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QTlsPrivate::DtlsBase'

  #  A C++ QTlsPrivate::DtlsBase Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QTlsPrivate_DtlsBase'

  #  The functions Qt calls itself that QTlsPrivate::DtlsBase is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'setDtlsError': (
          'void QTlsPrivate::DtlsBase::setDtlsError(QDtlsError, const '
          'QString &)',
      ),
      'error': (
          'QDtlsError QTlsPrivate::DtlsBase::error() const',
      ),
  }

  #  The functions Qt calls itself that QTlsPrivate::DtlsBase is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'errorString': (
          ('_ZNK11QTlsPrivate8DtlsBase11errorStringEv',
           ('address', 'text', ''),
           ()),
      ),
      'clearDtlsError': (
          ('_ZN11QTlsPrivate8DtlsBase14clearDtlsErrorEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'setConfiguration': (
          ('_ZN11QTlsPrivate8DtlsBase16setConfigurationERK17QSslConfigurati'
           'on',
           ('nothing', 'nothing', ''),
           (
               ('address', 'value', 'QtNetwork:QSslConfiguration'),
           )),
      ),
      'configuration': (
          ('_ZNK11QTlsPrivate8DtlsBase13configurationEv',
           ('address', 'value', 'QtNetwork:QSslConfiguration'),
           ()),
      ),
      'setCookieGeneratorParameters': (
          ('_ZN11QTlsPrivate8DtlsBase28setCookieGeneratorParametersERKN19QD'
           'tlsClientVerifier19GeneratorParametersE',
           ('bool', 'number', ''),
           (
               ('address', 'value',
                'QtNetwork:QDtlsClientVerifier.GeneratorParameters'),
           )),
      ),
      'cookieGeneratorParameters': (
          ('_ZNK11QTlsPrivate8DtlsBase25cookieGeneratorParametersEv',
           ('address', 'value',
            'QtNetwork:QDtlsClientVerifier.GeneratorParameters'),
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

  def errorString(self) -> str:
    """
    Calls Qt's 'QString QTlsPrivate::DtlsBase::errorString() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-dtlsbase.html#errorString

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QTlsPrivate::DtlsBase::errorString() const
    return self.uglySide.call(
        'ritual_ZNK11QTlsPrivate8DtlsBase11errorStringEv',
    )

  def configuration(self) -> QSslConfiguration:
    """
    Calls Qt's 'QSslConfiguration QTlsPrivate::DtlsBase::configuration()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-dtlsbase.html#configuration

    Returns
    -------

    QSslConfiguration
      A new cute QSslConfiguration around the copy Qt gave back. Python owns
      it.
    """
    #  QSslConfiguration QTlsPrivate::DtlsBase::configuration() const
    address = self.uglySide.call(
        'ritual_ZNK11QTlsPrivate8DtlsBase13configurationEv',
    )
    from . import QSslConfiguration
    return QSslConfiguration._cuteOwning(address)

  def cookieGeneratorParameters(
      self,
  ) -> QDtlsClientVerifier.GeneratorParameters:
    """
    Calls Qt's 'GenParams QTlsPrivate::DtlsBase::cookieGeneratorParameters()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-dtlsbase.html

    Returns
    -------

    QDtlsClientVerifier.GeneratorParameters
      A new cute QDtlsClientVerifier::GeneratorParameters around the copy Qt
      gave back. Python owns it.
    """
    #  GenParams QTlsPrivate::DtlsBase::cookieGeneratorParameters() const
    address = self.uglySide.call(
        'ritual_ZNK11QTlsPrivate8DtlsBase25cookieGeneratorParametersEv',
    )
    return QDtlsClientVerifier.GeneratorParameters._cuteOwning(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(QSslConfiguration)
  def setConfiguration(self, configuration: QSslConfiguration) -> None:
    """
    Calls Qt's 'void QTlsPrivate::DtlsBase::setConfiguration(const
    QSslConfiguration &configuration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-dtlsbase.html#setConfiguration

    Parameters
    ----------

    configuration : QSslConfiguration
      Passed on as a value: Qt reads the C++ QSslConfiguration, which stays
      Python's own.
    """
    #  void QTlsPrivate::DtlsBase::setConfiguration(const QSslConfiguration
    #      &configuration)
    self.uglySide.call(
        'ritual_ZN11QTlsPrivate8DtlsBase16setConfigurationERK17QSslConfigur'
        'ation',
        self._valueOf(configuration),
    )

  @overload(QDtlsClientVerifier.GeneratorParameters)
  def setCookieGeneratorParameters(
      self,
      params: QDtlsClientVerifier.GeneratorParameters,
  ) -> bool:
    """
    Calls Qt's 'bool
    QTlsPrivate::DtlsBase::setCookieGeneratorParameters(const GenParams
    &params)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-dtlsbase.html

    Parameters
    ----------

    params : QDtlsClientVerifier.GeneratorParameters
      Passed on as a value: Qt reads the C++
      QDtlsClientVerifier::GeneratorParameters, which stays Python's own.
    """
    #  bool QTlsPrivate::DtlsBase::setCookieGeneratorParameters(const
    #      GenParams &params)
    return self.uglySide.call(
        'ritual_ZN11QTlsPrivate8DtlsBase28setCookieGeneratorParametersERKN1'
        '9QDtlsClientVerifier19GeneratorParametersE',
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

  def clearDtlsError(self) -> None:
    """
    Calls Qt's 'void QTlsPrivate::DtlsBase::clearDtlsError()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qtlsprivate-dtlsbase.html#clearDtlsError
    """
    #  void QTlsPrivate::DtlsBase::clearDtlsError()
    self.uglySide.call('ritual_ZN11QTlsPrivate8DtlsBase14clearDtlsErrorEv')

  @staticmethod
  def error(*__, **_) -> Never:
    """
    Qt's 'QDtlsError QTlsPrivate::DtlsBase::error() const': gives the enum
    'QDtlsError', whose class cannot be named here.
    """
    raise NotImplementedError(
        "'QTlsPrivate.DtlsBase.error' has no cute function yet. Qt's "
        "'QDtlsError QTlsPrivate::DtlsBase::error() const': gives the enum "
        "'QDtlsError', whose class cannot be named here.")

  @staticmethod
  def setDtlsError(*__, **_) -> Never:
    """
    Qt's 'void QTlsPrivate::DtlsBase::setDtlsError(QDtlsError code, const
    QString &description)': names the enum 'QDtlsError', whose class cannot
    be named here.
    """
    raise NotImplementedError(
        "'QTlsPrivate.DtlsBase.setDtlsError' has no cute function yet. Qt's "
        "'void QTlsPrivate::DtlsBase::setDtlsError(QDtlsError code, const "
        "QString &description)': names the enum 'QDtlsError', whose class "
        "cannot be named here.")
