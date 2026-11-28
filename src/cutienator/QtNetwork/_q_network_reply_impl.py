"""
QNetworkReplyImpl binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetwork/6.12.0/QtNetwork/private/qnetworkreplyimpl_p.h, Qt 6.12.0.
#  Changes made here are lost.
#
#  Qt means QNetworkReplyImpl to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..QtCore import QList
from . import QNetworkReply

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QEvent, QMetaObject
  from . import QNetworkReplyImplPrivate, QSslConfiguration, QSslError
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QEvent = WAIT['QEvent']
  QSslConfiguration = WAIT['QSslConfiguration']
  QSslError = WAIT['QSslError']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QNetworkReplyImpl(QNetworkReply):
  """
  The cute side of Qt's QNetworkReplyImpl: a plain Python object standing in
  front of one C++ QNetworkReplyImpl.

  It is built on the cute 'QNetworkReply', as Qt's QNetworkReplyImpl is built
  on Qt's QNetworkReply, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QNetworkReplyImpl that has a ritual and that Python
  can call so far, 10 names in all: 'metaObject', 'abort', 'close',
  'bytesAvailable', 'setReadBufferSize', 'event', 'd_func',
  'setSslConfigurationImplementation', 'ignoreSslErrors',
  'ignoreSslErrorsImplementation'. None can be made from Python: one comes
  out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'void *QNetworkReplyImpl::qt_metacast(const char *a0)': one of Qt's
    own inner workings.
  - Qt's 'int QNetworkReplyImpl::qt_metacall(QMetaObject::Call a0, int a1,
    void **a2)': one of Qt's own inner workings.
  - Qt's 'QNetworkReplyImpl::~QNetworkReplyImpl()': the destructor: Python
    never removes a C++ QNetworkReplyImpl.
  - Qt's 'qint64 QNetworkReplyImpl::readData(char *data, qint64 maxlen)':
    names 'char', which has no cute class yet.
  - Qt's 'const QNetworkReplyImplPrivate *QNetworkReplyImpl::d_func() const':
    takes in Python what 'QNetworkReplyImplPrivate
    *QNetworkReplyImpl::d_func()' takes.
  - Qt's 'void
    QNetworkReplyImpl::sslConfigurationImplementation(QSslConfiguration
    &configuration) const': takes a type Python has no way to hand over yet.

  What has no ritual
  ------------------

  4 of the 20 functions Qt declares: 2 not a gap; 2 leans on
  'QNetworkReplyImpl.

  What to expect
  --------------

  - The C++ QNetworkReplyImpl is created at the first use, not by
    'QNetworkReplyImpl(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QNetworkReplyImpl.
  - Qt tells when it has removed the C++ QNetworkReplyImpl. Every call on the
    cute object, and every use of it as an argument, then raises
    'RuntimeError', and nothing reaches C++.
  - Each name of Qt's QNetworkReplyImpl that has no cute function yet,
    '__init__', holds a function that raises 'NotImplementedError', and its
    docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QNetworkReplyImpl'

  #  A C++ QNetworkReplyImpl Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QNetworkReplyImpl'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def metaObject(self) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QNetworkReplyImpl::metaObject() const'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreplyimpl.html#metaObject

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QNetworkReplyImpl::metaObject() const
    address = self.uglySide.call(
        'ritual_ZNK17QNetworkReplyImpl10metaObjectEv',
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def bytesAvailable(self) -> int:
    """
    Calls Qt's 'qint64 QNetworkReplyImpl::bytesAvailable() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyimpl.html#bytesAvailable
    """
    #  qint64 QNetworkReplyImpl::bytesAvailable() const
    ritual = 'ritual_ZNK17QNetworkReplyImpl14bytesAvailableEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK17QNetworkReplyImpl14bytesAvailableEv'
    return self.uglySide.call(ritual)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(int)
  def setReadBufferSize(self, size: int) -> None:
    """
    Calls Qt's 'void QNetworkReplyImpl::setReadBufferSize(qint64 size)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyimpl.html#setReadBufferSize

    Parameters
    ----------

    size : int
      Passed on as it is.
    """
    #  void QNetworkReplyImpl::setReadBufferSize(qint64 size)
    ritual = 'ritual_ZN17QNetworkReplyImpl17setReadBufferSizeEx'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QNetworkReplyImpl17setReadBufferSizeEx'
    self.uglySide.call(ritual, size)

  @overload(QSslConfiguration)
  def setSslConfigurationImplementation(
      self,
      configuration: QSslConfiguration,
  ) -> None:
    """
    Calls Qt's 'void
    QNetworkReplyImpl::setSslConfigurationImplementation(const
    QSslConfiguration &configuration)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyimpl.html

    Parameters
    ----------

    configuration : QSslConfiguration
      Passed on as a value: Qt reads the C++ QSslConfiguration, which stays
      Python's own.
    """
    #  void QNetworkReplyImpl::setSslConfigurationImplementation(const
    #      QSslConfiguration &configuration)
    ritual = (
        'ritual_ZN17QNetworkReplyImpl33setSslConfigurationImplementationERK'
        '17QSslConfiguration')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN17QNetworkReplyImpl33setSslConfigurationImplementat'
          'ionERK17QSslConfiguration')
    self.uglySide.call(ritual, self._valueOf(configuration))

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    Qt's 'QNetworkReplyImpl::QNetworkReplyImpl(QObject *parent)': leans on
    'QNetworkReplyImpl::qt_metacall(QMetaObject::Call, int, void**)', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QNetworkReplyImpl.__init__' has no cute function yet. Qt's "
        "'QNetworkReplyImpl::QNetworkReplyImpl(QObject *parent)': leans on "
        "'QNetworkReplyImpl::qt_metacall(QMetaObject::Call, int, void**)', "
        "which Qt's source does not mark for use from outside Qt and has no "
        "code for that could be taken.")

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

  def abort(self) -> None:
    """
    Calls Qt's 'void QNetworkReplyImpl::abort()'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreplyimpl.html#abort
    """
    #  void QNetworkReplyImpl::abort()
    self.uglySide.call('ritual_ZN17QNetworkReplyImpl5abortEv')

  def close(self) -> None:
    """
    Calls Qt's 'void QNetworkReplyImpl::close()'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreplyimpl.html#close
    """
    #  void QNetworkReplyImpl::close()
    self.uglySide.call('ritual_ZN17QNetworkReplyImpl5closeEv')

  @overload(QEvent)
  @overload(NoneType)
  def event(self, a0: Optional[QEvent]) -> bool:
    """
    Calls Qt's 'bool QNetworkReplyImpl::event(QEvent *a0)'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreplyimpl.html#event

    Parameters
    ----------

    a0 : Optional[QEvent]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QNetworkReplyImpl::event(QEvent *a0)
    return self.uglySide.call(
        'ritual_ZN17QNetworkReplyImpl5eventEP6QEvent', self._addressOf(a0),
    )

  def d_func(self) -> Optional[QNetworkReplyImplPrivate]:
    """
    Calls Qt's 'QNetworkReplyImplPrivate *QNetworkReplyImpl::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qnetworkreplyimpl.html#d_func

    Returns
    -------

    Optional[QNetworkReplyImplPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QNetworkReplyImplPrivate *QNetworkReplyImpl::d_func()
    address = self.uglySide.call('ritual_ZN17QNetworkReplyImpl6d_funcEv')
    from . import QNetworkReplyImplPrivate
    return QNetworkReplyImplPrivate._cuteAt(address)

  def ignoreSslErrors(self) -> None:
    """
    Calls Qt's 'void QNetworkReplyImpl::ignoreSslErrors()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyimpl.html#ignoreSslErrors
    """
    #  void QNetworkReplyImpl::ignoreSslErrors()
    ritual = 'ritual_ZN17QNetworkReplyImpl15ignoreSslErrorsEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN17QNetworkReplyImpl15ignoreSslErrorsEv'
    self.uglySide.call(ritual)

  @overload(QList[QSslError])
  def ignoreSslErrorsImplementation(self, errors: QList[QSslError]) -> None:
    """
    Calls Qt's 'void QNetworkReplyImpl::ignoreSslErrorsImplementation(const
    QList<QSslError> &errors)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qnetworkreplyimpl.html

    Parameters
    ----------

    errors : QList[QSslError]
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  void QNetworkReplyImpl::ignoreSslErrorsImplementation(const
    #      QList<QSslError> &errors)
    self.uglySide.call(
        'ritual_ZN17QNetworkReplyImpl29ignoreSslErrorsImplementationERK5QLi'
        'stI9QSslErrorE',
        self._valueOf(errors),
    )
