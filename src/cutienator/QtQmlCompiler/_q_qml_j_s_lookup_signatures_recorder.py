"""
QQmlJSLookupSignaturesRecorder binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljslookupsignatures_p.h, Qt
#  6.12.0. Changes made here are lost.
#
#  Qt means QQmlJSLookupSignaturesRecorder to be private: it declares the
#  class in a header it calls private. cutienator does not care. Qt hands
#  objects of the class out all the same, and a class we are handed is a
#  class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QQmlJSTypeResolver
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QQmlJSTypeResolver = WAIT['QQmlJSTypeResolver']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlJSLookupSignaturesRecorder(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlJSLookupSignaturesRecorder: a plain Python object
  standing in front of one C++ QQmlJSLookupSignaturesRecorder.

  C++ hands a QQmlJSLookupSignaturesRecorder around as a copy, so every C++
  QQmlJSLookupSignaturesRecorder behind a cute one is Python's own: it is
  removed, by the ritual named in '__delete_ritual__', when the cute object
  goes.

  What exists
  -----------

  Every function of Qt's QQmlJSLookupSignaturesRecorder that has a ritual and
  that Python can call so far, 1 name in all: 'rejectMessage'. It can be made
  from Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlPrivate::AOTLookupValidation::LookupSignatures
    QQmlJSLookupSignaturesRecorder::signatures() const': gives a type Python
    has no way to take yet.
  - Qt's 'bool QQmlJSLookupSignaturesRecorder::recordPropertyLookup(const
    QQmlJSScope::ConstPtr &base, const QQmlJSMetaProperty &prop)': takes a
    type Python has no way to hand over yet.
  - Qt's 'bool QQmlJSLookupSignaturesRecorder::recordMethodLookup(const
    QQmlJSScope::ConstPtr &base, const QQmlJSMetaMethod &method)': takes a
    type Python has no way to hand over yet.
  - Qt's 'bool QQmlJSLookupSignaturesRecorder::recordEnumKeyLookup(const
    QQmlJSScope::ConstPtr &base, const QQmlJSMetaEnum &metaEnum, const
    QString &keyName)': takes a type Python has no way to hand over yet.
  - Qt's 'bool QQmlJSLookupSignaturesRecorder::cantDesync(const
    QQmlJSScope::ConstPtr &base) const': takes a type Python has no way to
    hand over yet.
  - Qt's 'bool QQmlJSLookupSignaturesRecorder::safeBase(const
    QQmlJSScope::ConstPtr &base) const': takes a type Python has no way to
    hand over yet.
  - Qt's 'bool QQmlJSLookupSignaturesRecorder::isUnnamedCompositeType(const
    QQmlJSScope::ConstPtr &type) const': takes a type Python has no way to
    hand over yet.
  - Qt's 'std::optional<QQmlPrivate::AOTLookupValidation::Type>
    QQmlJSLookupSignaturesRecorder::type(const QQmlJSScope::ConstPtr &type)':
    takes a type Python has no way to hand over yet.
  - Qt's 'QQmlJSLookupSignaturesRecorder::~QQmlJSLookupSignaturesRecorder()':
    the destructor: Python removes its C++ QQmlJSLookupSignaturesRecorder by
    it, and has no other use for it.

  What to expect
  --------------

  - The C++ QQmlJSLookupSignaturesRecorder is created at the first use, not
    by 'QQmlJSLookupSignaturesRecorder(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QQmlJSLookupSignaturesRecorder back gives a copy the
    ritual made for Python, in a new cute QQmlJSLookupSignaturesRecorder.
  - Each name of Qt's QQmlJSLookupSignaturesRecorder that has no cute
    function yet, 'cantDesync', 'isUnnamedCompositeType',
    'recordEnumKeyLookup', 'recordMethodLookup', 'recordPropertyLookup',
    'safeBase', 'signatures', 'type', holds a function that raises
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
  __qt_class__ = 'QQmlJSLookupSignaturesRecorder'

  #  Qt's '~QQmlJSLookupSignaturesRecorder()'. Naming it makes this a value
  #  class: Python owns every C++ QQmlJSLookupSignaturesRecorder behind a
  #  cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN30QQmlJSLookupSignaturesRecorderD1Ev'

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

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str, QQmlJSTypeResolver)
  @overload(str, NoneType)
  def __init__(
      self,
      currentFilePath: str,
      typeResolver: Optional[QQmlJSTypeResolver],
  ) -> None:
    """
    Notes what was given, for Qt's
    'QQmlJSLookupSignaturesRecorder::QQmlJSLookupSignaturesRecorder(const
    QString &currentFilePath, const QQmlJSTypeResolver *typeResolver)', which
    is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljslookupsignaturesrecorder.html

    Parameters
    ----------

    currentFilePath : str
      Passed on as it is: a QString is made of it for the call.

    typeResolver : Optional[QQmlJSTypeResolver]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QQmlJSLookupSignaturesRecorder::QQmlJSLookupSignaturesRecorder(const
    #      QString &currentFilePath, const QQmlJSTypeResolver *typeResolver)
    self._noteCreation(QQmlJSLookupSignaturesRecorder, lambda: Rituals.call(
        'ritual_ZN30QQmlJSLookupSignaturesRecorderC1ERK7QStringPK18QQmlJSTy'
        'peResolver',
        currentFilePath, self._addressOf(typeResolver),
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

  def rejectMessage(self) -> str:
    """
    Calls Qt's 'QString QQmlJSLookupSignaturesRecorder::rejectMessage()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qqmljslookupsignaturesrecorder.html#rejectMessage

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QQmlJSLookupSignaturesRecorder::rejectMessage()
    return self.uglySide.call(
        'ritual_ZN30QQmlJSLookupSignaturesRecorder13rejectMessageEv',
    )

  @staticmethod
  def cantDesync(*__, **_) -> Never:
    """
    Qt's 'bool QQmlJSLookupSignaturesRecorder::cantDesync(const
    QQmlJSScope::ConstPtr &base) const': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSLookupSignaturesRecorder.cantDesync' has no cute function "
        "yet. Qt's 'bool QQmlJSLookupSignaturesRecorder::cantDesync(const "
        "QQmlJSScope::ConstPtr &base) const': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def isUnnamedCompositeType(*__, **_) -> Never:
    """
    Qt's 'bool QQmlJSLookupSignaturesRecorder::isUnnamedCompositeType(const
    QQmlJSScope::ConstPtr &type) const': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSLookupSignaturesRecorder.isUnnamedCompositeType' has no "
        "cute function yet. Qt's 'bool "
        "QQmlJSLookupSignaturesRecorder::isUnnamedCompositeType(const "
        "QQmlJSScope::ConstPtr &type) const': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def recordEnumKeyLookup(*__, **_) -> Never:
    """
    Qt's 'bool QQmlJSLookupSignaturesRecorder::recordEnumKeyLookup(const
    QQmlJSScope::ConstPtr &base, const QQmlJSMetaEnum &metaEnum, const
    QString &keyName)': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSLookupSignaturesRecorder.recordEnumKeyLookup' has no cute "
        "function yet. Qt's 'bool "
        "QQmlJSLookupSignaturesRecorder::recordEnumKeyLookup(const "
        "QQmlJSScope::ConstPtr &base, const QQmlJSMetaEnum &metaEnum, const "
        "QString &keyName)': takes a type Python has no way to hand over "
        "yet.")

  @staticmethod
  def recordMethodLookup(*__, **_) -> Never:
    """
    Qt's 'bool QQmlJSLookupSignaturesRecorder::recordMethodLookup(const
    QQmlJSScope::ConstPtr &base, const QQmlJSMetaMethod &method)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSLookupSignaturesRecorder.recordMethodLookup' has no cute "
        "function yet. Qt's 'bool "
        "QQmlJSLookupSignaturesRecorder::recordMethodLookup(const "
        "QQmlJSScope::ConstPtr &base, const QQmlJSMetaMethod &method)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def recordPropertyLookup(*__, **_) -> Never:
    """
    Qt's 'bool QQmlJSLookupSignaturesRecorder::recordPropertyLookup(const
    QQmlJSScope::ConstPtr &base, const QQmlJSMetaProperty &prop)': takes a
    type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSLookupSignaturesRecorder.recordPropertyLookup' has no cute "
        "function yet. Qt's 'bool "
        "QQmlJSLookupSignaturesRecorder::recordPropertyLookup(const "
        "QQmlJSScope::ConstPtr &base, const QQmlJSMetaProperty &prop)': "
        "takes a type Python has no way to hand over yet.")

  @staticmethod
  def safeBase(*__, **_) -> Never:
    """
    Qt's 'bool QQmlJSLookupSignaturesRecorder::safeBase(const
    QQmlJSScope::ConstPtr &base) const': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSLookupSignaturesRecorder.safeBase' has no cute function "
        "yet. Qt's 'bool QQmlJSLookupSignaturesRecorder::safeBase(const "
        "QQmlJSScope::ConstPtr &base) const': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def signatures(*__, **_) -> Never:
    """
    Qt's 'QQmlPrivate::AOTLookupValidation::LookupSignatures
    QQmlJSLookupSignaturesRecorder::signatures() const': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QQmlJSLookupSignaturesRecorder.signatures' has no cute function "
        "yet. Qt's 'QQmlPrivate::AOTLookupValidation::LookupSignatures "
        "QQmlJSLookupSignaturesRecorder::signatures() const': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def type(*__, **_) -> Never:
    """
    Qt's 'std::optional<QQmlPrivate::AOTLookupValidation::Type>
    QQmlJSLookupSignaturesRecorder::type(const QQmlJSScope::ConstPtr &type)':
    takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QQmlJSLookupSignaturesRecorder.type' has no cute function yet. "
        "Qt's 'std::optional<QQmlPrivate::AOTLookupValidation::Type> "
        "QQmlJSLookupSignaturesRecorder::type(const QQmlJSScope::ConstPtr "
        "&type)': takes a type Python has no way to hand over yet.")
