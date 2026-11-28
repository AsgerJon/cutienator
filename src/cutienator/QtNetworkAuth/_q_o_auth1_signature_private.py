"""
QOAuth1SignaturePrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtNetworkAuth/6.12.0/QtNetworkAuth/private/qoauth1signature_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QOAuth1SignaturePrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..occult import Rituals
from ..QtCore import QSharedData
from . import QOAuth1Signature

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never

  from ..QtCore import QByteArray


class QOAuth1SignaturePrivate(QSharedData):
  """
  The cute side of Qt's QOAuth1SignaturePrivate: a plain Python object
  standing in front of one C++ QOAuth1SignaturePrivate.

  It is built on the cute 'QSharedData', as Qt's QOAuth1SignaturePrivate is
  built on Qt's QSharedData, and has everything that class has.

  C++ hands a QOAuth1SignaturePrivate around as a copy, so every C++
  QOAuth1SignaturePrivate behind a cute one is Python's own: it is removed,
  by the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QOAuth1SignaturePrivate that has a ritual and that
  Python can call so far, 1 name in all: 'secret'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QOAuth1SignaturePrivate::QOAuth1SignaturePrivate(const QUrl &url,
    QOAuth1Signature::HttpRequestMethod method, const QMultiMap<QString,
    QVariant> &parameters, const QString &clientSharedKey, const QString
    &tokenSecret)': takes a type Python has no way to hand over yet.
  - Qt's 'QOAuth1SignaturePrivate::~QOAuth1SignaturePrivate()': the
    destructor: Python removes its C++ QOAuth1SignaturePrivate by it, and has
    no other use for it.

  What has no ritual
  ------------------

  3 of the 7 functions Qt declares: 2 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 1 leans on
  'QOAuth1SignaturePrivate.

  What to expect
  --------------

  - The C++ QOAuth1SignaturePrivate is created at the first use, not by
    'QOAuth1SignaturePrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QOAuth1SignaturePrivate back gives a copy the ritual
    made for Python, in a new cute QOAuth1SignaturePrivate.
  - Each name of Qt's QOAuth1SignaturePrivate that has no cute function yet,
    'encodeHeaders', 'parameterString', 'signatureBaseString', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QOAuth1SignaturePrivate'

  #  Qt's '~QOAuth1SignaturePrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QOAuth1SignaturePrivate behind a cute one, and
  #  removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN23QOAuth1SignaturePrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def secret(self) -> QByteArray:
    """
    Calls Qt's 'QByteArray QOAuth1SignaturePrivate::secret() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth1signatureprivate.html#secret

    Returns
    -------

    QByteArray
      A new cute QByteArray around the copy Qt gave back. Python owns it.
    """
    #  QByteArray QOAuth1SignaturePrivate::secret() const
    address = self.uglySide.call(
        'ritual_ZNK23QOAuth1SignaturePrivate6secretEv',
    )
    from ..QtCore import QByteArray
    return QByteArray._cuteOwning(address)

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

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's
    'QOAuth1SignaturePrivate::QOAuth1SignaturePrivate()', which is called at
    the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qoauth1signatureprivate.html
    """
    #  QOAuth1SignaturePrivate::QOAuth1SignaturePrivate()
    self._noteCreation(QOAuth1SignaturePrivate, lambda: Rituals.call(
        'ritual_ZN23QOAuth1SignaturePrivateC1Ev',
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

  @staticmethod
  def encodeHeaders(*__, **_) -> Never:
    """
    Qt's 'QByteArray QOAuth1SignaturePrivate::encodeHeaders(const
    QMultiMap<QString, QVariant> &headers)': leans on
    'QOAuth1SignaturePrivate::parameterString(QMultiMap<QString, QVariant>
    const&)', which Qt's source does not mark for use from outside Qt and has
    no code for that could be taken.
    """
    raise NotImplementedError(
        "'QOAuth1SignaturePrivate.encodeHeaders' has no cute function yet. "
        "Qt's 'QByteArray QOAuth1SignaturePrivate::encodeHeaders(const "
        "QMultiMap<QString, QVariant> &headers)': leans on "
        "'QOAuth1SignaturePrivate::parameterString(QMultiMap<QString, "
        "QVariant> const&)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def parameterString(*__, **_) -> Never:
    """
    Qt's 'QByteArray QOAuth1SignaturePrivate::parameterString(const
    QMultiMap<QString, QVariant> &parameters)': Qt's library has no name for
    it, and its code in Qt's source does not compile apart from its file:
    unknown type name 'loggingCategory'; did you mean 'QLoggingCategory'?.
    """
    raise NotImplementedError(
        "'QOAuth1SignaturePrivate.parameterString' has no cute function "
        "yet. Qt's 'QByteArray "
        "QOAuth1SignaturePrivate::parameterString(const QMultiMap<QString, "
        "QVariant> &parameters)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: unknown "
        "type name 'loggingCategory'; did you mean 'QLoggingCategory'?.")

  @staticmethod
  def signatureBaseString(*__, **_) -> Never:
    """
    Qt's 'QByteArray QOAuth1SignaturePrivate::signatureBaseString() const':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: unknown type name 'loggingCategory'; did you
    mean 'QLoggingCategory'?.
    """
    raise NotImplementedError(
        "'QOAuth1SignaturePrivate.signatureBaseString' has no cute function "
        "yet. Qt's 'QByteArray "
        "QOAuth1SignaturePrivate::signatureBaseString() const': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: unknown type name 'loggingCategory'; "
        "did you mean 'QLoggingCategory'?.")
