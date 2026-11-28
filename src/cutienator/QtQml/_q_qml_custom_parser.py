"""
QQmlCustomParser binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qqmlcustomparser_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QQmlCustomParser to be private: it declares the class in a header
#  it calls private. cutienator does not care. Qt hands objects of the class
#  out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, CuteFlags, MetaCute, WAIT
from ..QtCore import QHash, QList
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QMetaObject
  from . import QQmlError, QQmlTypeLoader

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QQmlCustomParser(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QQmlCustomParser: a plain Python object standing in
  front of one C++ QQmlCustomParser.

  What exists
  -----------

  Every function of Qt's QQmlCustomParser that has a ritual and that Python
  can call so far, 6 names in all: 'clearErrors', 'flags', 'errors', 'error',
  'resolveType', 'typeLoader'. None can be made from Python: one comes out of
  a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QQmlCustomParser::~QQmlCustomParser()': the destructor: Python
    never removes a C++ QQmlCustomParser.
  - Qt's 'void QQmlCustomParser::verifyBindings(const
    QQmlRefPointer<QV4::CompiledData::CompilationUnit> &a0, const QList<const
    QV4::CompiledData::Binding *> &a1)': takes a type Python has no way to
    hand over yet.
  - Qt's 'void QQmlCustomParser::applyBindings(QObject *a0, const
    QQmlRefPointer<QV4::ExecutableCompilationUnit> &a1, const QList<const
    QV4::CompiledData::Binding *> &a2)': takes a type Python has no way to
    hand over yet.
  - Qt's 'int QQmlCustomParser::evaluateEnum(const QString &a0, bool *ok)
    const': takes a number to change where it is.

  What has no ritual
  ------------------

  2 of the 14 functions Qt declares: 2 the class is abstract, so C++ cannot
  make one, and the C++ class of ours does not fill in every function it
  leaves open.

  What to expect
  --------------

  - The C++ QQmlCustomParser is created at the first use, not by
    'QQmlCustomParser(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QQmlCustomParser.
  - Each name of Qt's QQmlCustomParser that has no cute function yet,
    '__init__', 'applyBindings', 'evaluateEnum', 'verifyBindings', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QQmlCustomParser, each a class in here as in
  #  C++, and the names Qt has for the combinations of its flags enums.

  class Flag(CuteFlags):
    """
    The flags enum 'QQmlCustomParser::Flag' of Qt, with the 3 names Qt gives
    in it. Qt names the type of its combinations 'QQmlCustomParser::Flags'.
    """

    NoFlag = 0x0
    AcceptsAttachedProperties = 0x1
    AcceptsSignalHandlers = 0x2

  Flags = Flag

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QQmlCustomParser'

  #  The functions Qt calls itself that QQmlCustomParser is the first to
  #  declare and that cannot be handed to Python yet, each as Qt declares it.
  #  A class of a program that writes one of them anew is refused, since Qt
  #  would never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'verifyBindings': (
          'void QQmlCustomParser::verifyBindings(const '
          'QQmlRefPointer<QV4::CompiledData::CompilationUnit> &, const '
          'QList<const QV4::CompiledData::Binding *> &)',
      ),
      'applyBindings': (
          'void QQmlCustomParser::applyBindings(QObject *, const '
          'QQmlRefPointer<QV4::ExecutableCompilationUnit> &, const '
          'QList<const QV4::CompiledData::Binding *> &)',
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def flags(self) -> Flags:
    """
    Calls Qt's 'Flags QQmlCustomParser::flags() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcustomparser.html#flags

    Returns
    -------

    Flags
      The value standing for the combination Qt gave back.
    """
    #  Flags QQmlCustomParser::flags() const
    return QQmlCustomParser.Flags(self.uglySide.call(
        'ritual_ZNK16QQmlCustomParser5flagsEv',
    ))

  def errors(self) -> QList[QQmlError]:
    """
    Calls Qt's 'QList<QQmlError> QQmlCustomParser::errors() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcustomparser.html#errors

    Returns
    -------

    QList[QQmlError]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QQmlError> QQmlCustomParser::errors() const
    address = self.uglySide.call('ritual_ZNK16QQmlCustomParser6errorsEv')
    from . import QQmlError
    return QList[QQmlError]._cuteOwning(address)

  @overload(str)
  def resolveType(self, a0: str) -> Optional[QMetaObject]:
    """
    Calls Qt's 'const QMetaObject *QQmlCustomParser::resolveType(const
    QString &a0) const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcustomparser.html#resolveType

    Parameters
    ----------

    a0 : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    Optional[QMetaObject]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  const QMetaObject *QQmlCustomParser::resolveType(const QString &a0)
    #      const
    address = self.uglySide.call(
        'ritual_ZNK16QQmlCustomParser11resolveTypeERK7QString', a0,
    )
    from ..QtCore import QMetaObject
    return QMetaObject._cuteAt(address)

  def typeLoader(self) -> Optional[QQmlTypeLoader]:
    """
    Calls Qt's 'QQmlTypeLoader *QQmlCustomParser::typeLoader() const'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcustomparser.html#typeLoader

    Returns
    -------

    Optional[QQmlTypeLoader]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QQmlTypeLoader *QQmlCustomParser::typeLoader() const
    address = self.uglySide.call(
        'ritual_ZNK16QQmlCustomParser10typeLoaderEv',
    )
    from . import QQmlTypeLoader
    return QQmlTypeLoader._cuteAt(address)

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

  @staticmethod
  def __init__(*__, **_) -> Never:
    """
    - Qt's 'QQmlCustomParser::QQmlCustomParser()': the class is abstract, so
      C++ cannot make one, and the C++ class of ours does not fill in every
      function it leaves open.
    - Qt's 'QQmlCustomParser::QQmlCustomParser(Flags f)': the class is
      abstract, so C++ cannot make one, and the C++ class of ours does not
      fill in every function it leaves open.
    """
    raise NotImplementedError(
        "'QQmlCustomParser.__init__' has no cute function yet. Qt's "
        "'QQmlCustomParser::QQmlCustomParser()': the class is abstract, so "
        "C++ cannot make one, and the C++ class of ours does not fill in "
        "every function it leaves open. Qt's "
        "'QQmlCustomParser::QQmlCustomParser(Flags f)': the class is "
        "abstract, so C++ cannot make one, and the C++ class of ours does "
        "not fill in every function it leaves open.")

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

  def clearErrors(self) -> None:
    """
    Calls Qt's 'void QQmlCustomParser::clearErrors()'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcustomparser.html#clearErrors
    """
    #  void QQmlCustomParser::clearErrors()
    self.uglySide.call('ritual_ZN16QQmlCustomParser11clearErrorsEv')

  @overload(WAIT['QV4.CompiledData.Binding'], str)
  @overload(NoneType, str)
  def error(
      self,
      binding: Optional[QV4.CompiledData.Binding],
      description: str,
  ) -> None:
    """
    Calls Qt's 'void QQmlCustomParser::error(const QV4::CompiledData::Binding
    *binding, const QString &description)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcustomparser.html#error

    Parameters
    ----------

    binding : Optional[QV4.CompiledData.Binding]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    description : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlCustomParser::error(const QV4::CompiledData::Binding
    #      *binding, const QString &description)
    self.uglySide.call(
        'ritual_ZN16QQmlCustomParser5errorEPKN3QV412CompiledData7BindingERK'
        '7QString',
        self._addressOf(binding), description,
    )

  @overload(WAIT['QV4.CompiledData.Object'], str)
  def error(
      self,
      object: Optional[QV4.CompiledData.Object],
      description: str,
  ) -> None:
    """
    Calls Qt's 'void QQmlCustomParser::error(const QV4::CompiledData::Object
    *object, const QString &description)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcustomparser.html#error

    Parameters
    ----------

    object : Optional[QV4.CompiledData.Object]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    description : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlCustomParser::error(const QV4::CompiledData::Object *object,
    #      const QString &description)
    self.uglySide.call(
        'ritual_ZN16QQmlCustomParser5errorEPKN3QV412CompiledData6ObjectERK7'
        'QString',
        self._addressOf(object), description,
    )

  @overload(WAIT['QV4.CompiledData.Location'], str)
  def error(
      self,
      location: QV4.CompiledData.Location,
      description: str,
  ) -> None:
    """
    Calls Qt's 'void QQmlCustomParser::error(const
    QV4::CompiledData::Location &location, const QString &description)'.

    Qt's own words: https://doc.qt.io/qt-6/qqmlcustomparser.html#error

    Parameters
    ----------

    location : QV4.CompiledData.Location
      Passed on as a value: Qt reads the C++ QV4::CompiledData::Location,
      which stays Python's own.

    description : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QQmlCustomParser::error(const QV4::CompiledData::Location
    #      &location, const QString &description)
    self.uglySide.call(
        'ritual_ZN16QQmlCustomParser5errorERKN3QV412CompiledData8LocationER'
        'K7QString',
        self._valueOf(location), description,
    )

  @staticmethod
  def applyBindings(*__, **_) -> Never:
    """
    Qt's 'void QQmlCustomParser::applyBindings(QObject *a0, const
    QQmlRefPointer<QV4::ExecutableCompilationUnit> &a1, const QList<const
    QV4::CompiledData::Binding *> &a2)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQmlCustomParser.applyBindings' has no cute function yet. Qt's "
        "'void QQmlCustomParser::applyBindings(QObject *a0, const "
        "QQmlRefPointer<QV4::ExecutableCompilationUnit> &a1, const "
        "QList<const QV4::CompiledData::Binding *> &a2)': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def evaluateEnum(*__, **_) -> Never:
    """
    Qt's 'int QQmlCustomParser::evaluateEnum(const QString &a0, bool *ok)
    const': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QQmlCustomParser.evaluateEnum' has no cute function yet. Qt's "
        "'int QQmlCustomParser::evaluateEnum(const QString &a0, bool *ok) "
        "const': takes a number to change where it is.")

  @staticmethod
  def verifyBindings(*__, **_) -> Never:
    """
    Qt's 'void QQmlCustomParser::verifyBindings(const
    QQmlRefPointer<QV4::CompiledData::CompilationUnit> &a0, const QList<const
    QV4::CompiledData::Binding *> &a1)': takes a type Python has no way to
    hand over yet.
    """
    raise NotImplementedError(
        "'QQmlCustomParser.verifyBindings' has no cute function yet. Qt's "
        "'void QQmlCustomParser::verifyBindings(const "
        "QQmlRefPointer<QV4::CompiledData::CompilationUnit> &a0, const "
        "QList<const QV4::CompiledData::Binding *> &a1)': takes a type "
        "Python has no way to hand over yet.")


#  Qt's 'QHash<int, QQmlCustomParser *>': the QHash from a number to
#  QQmlCustomParser, which 'QHash[int, QQmlCustomParser]' gives. It is
#  completed here, in the file of the class of its values.
QHash.createKind(
    int, QQmlCustomParser, 'address',
    make='ritual_map_make_QHash_int_QQmlCustomParser_ptr',
    put='ritual_map_put_QHash_int_QQmlCustomParser_ptr',
    size='ritual_map_size_QHash_int_QQmlCustomParser_ptr',
    key='ritual_map_key_QHash_int_QQmlCustomParser_ptr',
    value='ritual_map_value_QHash_int_QQmlCustomParser_ptr',
    has='ritual_map_has_QHash_int_QQmlCustomParser_ptr',
    get='ritual_map_get_QHash_int_QQmlCustomParser_ptr',
    drop='ritual_map_drop_QHash_int_QQmlCustomParser_ptr',
)
