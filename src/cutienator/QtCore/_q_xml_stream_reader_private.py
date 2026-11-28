"""
QXmlStreamReaderPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore/6.12.0/QtCore/private/qxmlstream_p.h, Qt 6.12.0. Changes made here
#  are lost.
#
#  Qt means QXmlStreamReaderPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals
from . import QXmlStreamGrammar, QXmlStreamPrivateTagStack, QXmlStreamReader
from . import QtPrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QChar, QLatin1String
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QChar = WAIT['QChar']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QXmlStreamReaderPrivate(QXmlStreamGrammar, QXmlStreamPrivateTagStack):
  """
  The cute side of Qt's QXmlStreamReaderPrivate: a plain Python object
  standing in front of one C++ QXmlStreamReaderPrivate.

  It is built on the cute 'QXmlStreamGrammar', as Qt's
  QXmlStreamReaderPrivate is built on Qt's QXmlStreamGrammar, and has
  everything that class has. It is built on the cute
  'QXmlStreamPrivateTagStack' as well, as Qt's QXmlStreamReaderPrivate is
  built on Qt's QXmlStreamPrivateTagStack too, and has everything that class
  has.

  What exists
  -----------

  Every function of Qt's QXmlStreamReaderPrivate that has a ritual and that
  Python can call so far, 26 names in all: 'q_func', 'init',
  'resolvePublicNamespaces', 'resolveDtd', 'resolveCharRef', 'startDocument',
  'resume', 'entitiesMustBeDeclared', 'reallocateStack', 'clearTextBuffer',
  'symString', 'symView', 'symName', 'symPrefix', 'clearSym',
  'filterCarriageReturn', 'putChar', 'putString', 'putStringLiteral',
  'putReplacement', 'putReplacementInAttributeValue', 'injectToken',
  'resolveUndeclaredEntity', 'raiseError', 'raiseWellFormedError',
  'raiseNamePrefixTooLongError'. It can be made from Python, in 1 way; see
  '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'const QXmlStreamReader *QXmlStreamReaderPrivate::q_func() const':
    takes in Python what 'QXmlStreamReader
    *QXmlStreamReaderPrivate::q_func()' takes.
  - Qt's 'QXmlStreamReaderPrivate::~QXmlStreamReaderPrivate()': the
    destructor: Python never removes a C++ QXmlStreamReaderPrivate.
  - Qt's 'void QXmlStreamReaderPrivate::appendDataWithEncoding(const
    QByteArray &data, QStringDecoder::Encoding enc)': takes a type Python has
    no way to hand over yet.
  - Qt's 'bool QXmlStreamReaderPrivate::referenceEntity(QHash<QStringView,
    Entity> *hash, Entity &entity)': names 'QHash<QStringView,
    QXmlStreamReaderPrivate::Entity>', which has no cute class yet.
  - Qt's 'Value &QXmlStreamReaderPrivate::sym(int index) const': gives a type
    Python has no way to take yet.
  - Qt's 'void QXmlStreamReaderPrivate::setType(const
    QXmlStreamReader::TokenType t)': takes a type Python has no way to hand
    over yet.

  What has no ritual
  ------------------

  28 of the 65 functions Qt declares: 15 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 9 leans on
  'QXmlStreamGrammar; 3 cannot be called and cannot be called through the
  meta-object and cannot be copied; 1 the compiler refuses its ritual as it
  would be written here.

  What to expect
  --------------

  - The C++ QXmlStreamReaderPrivate is created at the first use, not by
    'QXmlStreamReaderPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QXmlStreamReaderPrivate.
  - Each name of Qt's QXmlStreamReaderPrivate that has no cute function yet,
    'appendDataWithEncoding', 'checkPublicLiteral', 'checkStartDocument',
    'checkToken', 'consumeRule', 'fastScanContentCharList',
    'fastScanLiteralContent', 'fastScanNMTOKEN', 'fastScanName',
    'fastScanSpace', 'getChar', 'getChar_helper', 'isValidToken',
    'namespaceForPrefix', 'parse', 'parseEntity', 'parseError', 'peekChar',
    'referenceEntity', 'resolveTag', 'scanAfterDefaultDecl',
    'scanAfterLangleBang', 'scanAttType', 'scanNData', 'scanPublicOrSystem',
    'scanString', 'scanUntil', 'setType', 'sym', 'symQName', 'write', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QXmlStreamReaderPrivate, each a class in here
  #  as in C++, and the names Qt has for the combinations of its flags enums.

  class XmlContext(CuteNum, scoped=True):
    """
    The enum 'QXmlStreamReaderPrivate::XmlContext' of Qt, with the 2 names Qt
    gives in it. C++ keeps these names inside the enum, so the class that
    holds the enum does not have them.
    """

    Prolog = Kee[int](0)
    Body = Kee[int](1)

  #  The classes Qt writes inside QXmlStreamReaderPrivate, each a class in
  #  here as in C++.

  class Attribute(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QXmlStreamReaderPrivate::Attribute: a plain Python
    object standing in front of one C++ QXmlStreamReaderPrivate::Attribute.

    C++ hands a QXmlStreamReaderPrivate::Attribute around as a copy, so every
    C++ QXmlStreamReaderPrivate::Attribute behind a cute one is Python's own:
    it is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    No function of Qt's QXmlStreamReaderPrivate::Attribute yet. None can be
    made from Python: one comes out of a function of another class that gives
    one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QXmlStreamReaderPrivate::Attribute::~Attribute()': the
      destructor: Python removes its C++ QXmlStreamReaderPrivate::Attribute
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QXmlStreamReaderPrivate::Attribute is created at the first use,
      not by 'QXmlStreamReaderPrivate::Attribute(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QXmlStreamReaderPrivate::Attribute back gives a
      copy the ritual made for Python, in a new cute
      QXmlStreamReaderPrivate::Attribute.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QXmlStreamReaderPrivate::Attribute'

    #  Qt's '~QXmlStreamReaderPrivate::Attribute()'. Naming it makes this a
    #  value class: Python owns every C++ QXmlStreamReaderPrivate::Attribute
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN23QXmlStreamReaderPrivate9AttributeD1Ev'

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

  class BufferAndEncoding(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QXmlStreamReaderPrivate::BufferAndEncoding: a plain
    Python object standing in front of one C++
    QXmlStreamReaderPrivate::BufferAndEncoding.

    C++ hands a QXmlStreamReaderPrivate::BufferAndEncoding around as a copy,
    so every C++ QXmlStreamReaderPrivate::BufferAndEncoding behind a cute one
    is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QXmlStreamReaderPrivate::BufferAndEncoding yet. It
    can be made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QXmlStreamReaderPrivate::BufferAndEncoding::BufferAndEncoding(const
      QByteArray &b, QStringDecoder::Encoding e)': takes a type Python has no
      way to hand over yet.
    - Qt's
      'QXmlStreamReaderPrivate::BufferAndEncoding::~BufferAndEncoding()': the
      destructor: Python removes its C++
      QXmlStreamReaderPrivate::BufferAndEncoding by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QXmlStreamReaderPrivate::BufferAndEncoding is created at the
      first use, not by 'QXmlStreamReaderPrivate::BufferAndEncoding(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QXmlStreamReaderPrivate::BufferAndEncoding back
      gives a copy the ritual made for Python, in a new cute
      QXmlStreamReaderPrivate::BufferAndEncoding.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QXmlStreamReaderPrivate::BufferAndEncoding'

    #  Qt's '~QXmlStreamReaderPrivate::BufferAndEncoding()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QXmlStreamReaderPrivate::BufferAndEncoding behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN23QXmlStreamReaderPrivate17BufferAndEncodingD1Ev')

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
      'QXmlStreamReaderPrivate::BufferAndEncoding::BufferAndEncoding()',
      which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qxmlstreamreaderprivate-bufferandencoding.html
      """
      #  QXmlStreamReaderPrivate::BufferAndEncoding::BufferAndEncoding()
      self._noteCreation(
          QXmlStreamReaderPrivate.BufferAndEncoding, lambda: Rituals.call(
              'ritual_ZN23QXmlStreamReaderPrivate17BufferAndEncodingC1Ev',
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

  class DtdAttribute(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QXmlStreamReaderPrivate::DtdAttribute: a plain
    Python object standing in front of one C++
    QXmlStreamReaderPrivate::DtdAttribute.

    C++ hands a QXmlStreamReaderPrivate::DtdAttribute around as a copy, so
    every C++ QXmlStreamReaderPrivate::DtdAttribute behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QXmlStreamReaderPrivate::DtdAttribute yet. None can
    be made from Python: one comes out of a function of another class that
    gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QXmlStreamReaderPrivate::DtdAttribute::~DtdAttribute()': the
      destructor: Python removes its C++
      QXmlStreamReaderPrivate::DtdAttribute by it, and has no other use for
      it.

    What to expect
    --------------

    - The C++ QXmlStreamReaderPrivate::DtdAttribute is created at the first
      use, not by 'QXmlStreamReaderPrivate::DtdAttribute(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QXmlStreamReaderPrivate::DtdAttribute back gives a
      copy the ritual made for Python, in a new cute
      QXmlStreamReaderPrivate::DtdAttribute.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QXmlStreamReaderPrivate::DtdAttribute'

    #  Qt's '~QXmlStreamReaderPrivate::DtdAttribute()'. Naming it makes this
    #  a value class: Python owns every C++
    #  QXmlStreamReaderPrivate::DtdAttribute behind a cute one, and removes
    #  it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN23QXmlStreamReaderPrivate12DtdAttributeD1Ev')

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

  class Entity(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QXmlStreamReaderPrivate::Entity: a plain Python
    object standing in front of one C++ QXmlStreamReaderPrivate::Entity.

    C++ hands a QXmlStreamReaderPrivate::Entity around as a copy, so every
    C++ QXmlStreamReaderPrivate::Entity behind a cute one is Python's own: it
    is removed, by the ritual named in '__delete_ritual__', when the cute
    object goes.

    What exists
    -----------

    Every function of Qt's QXmlStreamReaderPrivate::Entity that has a ritual
    and that Python can call so far, 1 name in all: 'createLiteral'. It can
    be made from Python, in 2 ways; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QXmlStreamReaderPrivate::Entity::~Entity()': the destructor:
      Python removes its C++ QXmlStreamReaderPrivate::Entity by it, and has
      no other use for it.

    What to expect
    --------------

    - The C++ QXmlStreamReaderPrivate::Entity is created at the first use,
      not by 'QXmlStreamReaderPrivate::Entity(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QXmlStreamReaderPrivate::Entity back gives a copy
      the ritual made for Python, in a new cute
      QXmlStreamReaderPrivate::Entity.
    """

    #  The cute classes this class names and is not built on. Each waits
    #  until it is made; see 'WAIT'. A type checker reads the imports at the
    #  top of the file instead.
    if not TYPE_CHECKING:
      QLatin1String = WAIT['QLatin1String']

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    @staticmethod
    @overload(QLatin1String, QLatin1String)
    def createLiteral(
        name: QLatin1String,
        value: QLatin1String,
    ) -> QXmlStreamReaderPrivate.Entity:
      """
      Calls Qt's 'Entity
      QXmlStreamReaderPrivate::Entity::createLiteral(QLatin1StringView name,
      QLatin1StringView value)'.

      Qt's own words:
      https://doc.qt.io/qt-6/qxmlstreamreaderprivate-entity.html

      Parameters
      ----------

      name : QLatin1String
        Passed on as a value: Qt reads the C++ QLatin1String, which stays
        Python's own.

      value : QLatin1String
        Passed on as a value: Qt reads the C++ QLatin1String, which stays
        Python's own.

      Returns
      -------

      QXmlStreamReaderPrivate.Entity
        A new cute QXmlStreamReaderPrivate::Entity around the copy Qt gave
        back. Python owns it.
      """
      #  Entity
      #      QXmlStreamReaderPrivate::Entity::createLiteral(QLatin1StringView
      #      name, QLatin1StringView value)
      address = Rituals.call(
          'ritual_ZN23QXmlStreamReaderPrivate6Entity13createLiteralE13QLati'
          'n1StringS1_',
          CuteMixin._valueOf(name), CuteMixin._valueOf(value),
      )
      return QXmlStreamReaderPrivate.Entity._cuteOwning(address)

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QXmlStreamReaderPrivate::Entity'

    #  Qt's '~QXmlStreamReaderPrivate::Entity()'. Naming it makes this a
    #  value class: Python owns every C++ QXmlStreamReaderPrivate::Entity
    #  behind a cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN23QXmlStreamReaderPrivate6EntityD1Ev'

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
      'QXmlStreamReaderPrivate::Entity::Entity()', which is called at the
      first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qxmlstreamreaderprivate-entity.html#Entity
      """
      #  QXmlStreamReaderPrivate::Entity::Entity()
      self._noteCreation(
          QXmlStreamReaderPrivate.Entity, lambda: Rituals.call(
              'ritual_ZN23QXmlStreamReaderPrivate6EntityC1Ev',
          ))

    @overload(str, str)
    def __init__(self, name: str, value: str) -> None:
      """
      Notes what was given, for Qt's
      'QXmlStreamReaderPrivate::Entity::Entity(const QString &name, const
      QString &value)', which is called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qxmlstreamreaderprivate-entity.html#Entity

      Parameters
      ----------

      name : str
        Passed on as it is: a QString is made of it for the call.

      value : str
        Passed on as it is: a QString is made of it for the call.
      """
      #  QXmlStreamReaderPrivate::Entity::Entity(const QString &name, const
      #      QString &value)
      self._noteCreation(
          QXmlStreamReaderPrivate.Entity, lambda: Rituals.call(
              'ritual_ZN23QXmlStreamReaderPrivate6EntityC1ERK7QStringS3_',
              name, value,
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

  class EntityDeclaration(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QXmlStreamReaderPrivate::EntityDeclaration: a plain
    Python object standing in front of one C++
    QXmlStreamReaderPrivate::EntityDeclaration.

    C++ hands a QXmlStreamReaderPrivate::EntityDeclaration around as a copy,
    so every C++ QXmlStreamReaderPrivate::EntityDeclaration behind a cute one
    is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    Every function of Qt's QXmlStreamReaderPrivate::EntityDeclaration that
    has a ritual and that Python can call so far, 1 name in all: 'clear'.
    None can be made from Python: one comes out of a function of another
    class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QXmlStreamReaderPrivate::EntityDeclaration::~EntityDeclaration()': the
      destructor: Python removes its C++
      QXmlStreamReaderPrivate::EntityDeclaration by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QXmlStreamReaderPrivate::EntityDeclaration is created at the
      first use, not by 'QXmlStreamReaderPrivate::EntityDeclaration(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QXmlStreamReaderPrivate::EntityDeclaration back
      gives a copy the ritual made for Python, in a new cute
      QXmlStreamReaderPrivate::EntityDeclaration.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QXmlStreamReaderPrivate::EntityDeclaration'

    #  Qt's '~QXmlStreamReaderPrivate::EntityDeclaration()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QXmlStreamReaderPrivate::EntityDeclaration behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN23QXmlStreamReaderPrivate17EntityDeclarationD1Ev')

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

    def clear(self) -> None:
      """
      Calls Qt's 'void QXmlStreamReaderPrivate::EntityDeclaration::clear()'.

      Qt's own words:
      https://doc.qt.io/qt-6/qxmlstreamreaderprivate-entitydeclaration.html
      """
      #  void QXmlStreamReaderPrivate::EntityDeclaration::clear()
      self.uglySide.call(
          'ritual_ZN23QXmlStreamReaderPrivate17EntityDeclaration5clearEv',
      )

  class NotationDeclaration(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QXmlStreamReaderPrivate::NotationDeclaration: a
    plain Python object standing in front of one C++
    QXmlStreamReaderPrivate::NotationDeclaration.

    C++ hands a QXmlStreamReaderPrivate::NotationDeclaration around as a
    copy, so every C++ QXmlStreamReaderPrivate::NotationDeclaration behind a
    cute one is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QXmlStreamReaderPrivate::NotationDeclaration yet.
    None can be made from Python: one comes out of a function of another
    class that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's
      'QXmlStreamReaderPrivate::NotationDeclaration::~NotationDeclaration()':
      the destructor: Python removes its C++
      QXmlStreamReaderPrivate::NotationDeclaration by it, and has no other
      use for it.

    What to expect
    --------------

    - The C++ QXmlStreamReaderPrivate::NotationDeclaration is created at the
      first use, not by 'QXmlStreamReaderPrivate::NotationDeclaration(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QXmlStreamReaderPrivate::NotationDeclaration back
      gives a copy the ritual made for Python, in a new cute
      QXmlStreamReaderPrivate::NotationDeclaration.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QXmlStreamReaderPrivate::NotationDeclaration'

    #  Qt's '~QXmlStreamReaderPrivate::NotationDeclaration()'. Naming it
    #  makes this a value class: Python owns every C++
    #  QXmlStreamReaderPrivate::NotationDeclaration behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN23QXmlStreamReaderPrivate19NotationDeclarationD1Ev')

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

  class QEntityReference(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QXmlStreamReaderPrivate::QEntityReference: a plain
    Python object standing in front of one C++
    QXmlStreamReaderPrivate::QEntityReference.

    C++ hands a QXmlStreamReaderPrivate::QEntityReference around as a copy,
    so every C++ QXmlStreamReaderPrivate::QEntityReference behind a cute one
    is Python's own: it is removed, by the ritual named in
    '__delete_ritual__', when the cute object goes.

    What exists
    -----------

    No function of Qt's QXmlStreamReaderPrivate::QEntityReference yet. None
    can be made from Python: one comes out of a function of another class
    that gives one back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QXmlStreamReaderPrivate::QEntityReference::~QEntityReference()':
      the destructor: Python removes its C++
      QXmlStreamReaderPrivate::QEntityReference by it, and has no other use
      for it.

    What to expect
    --------------

    - The C++ QXmlStreamReaderPrivate::QEntityReference is created at the
      first use, not by 'QXmlStreamReaderPrivate::QEntityReference(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QXmlStreamReaderPrivate::QEntityReference back
      gives a copy the ritual made for Python, in a new cute
      QXmlStreamReaderPrivate::QEntityReference.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QXmlStreamReaderPrivate::QEntityReference'

    #  Qt's '~QXmlStreamReaderPrivate::QEntityReference()'. Naming it makes
    #  this a value class: Python owns every C++
    #  QXmlStreamReaderPrivate::QEntityReference behind a cute one, and
    #  removes it by this ritual.
    __delete_ritual__ = (
        'ritual_ZN23QXmlStreamReaderPrivate16QEntityReferenceD1Ev')

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

  class Value(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QXmlStreamReaderPrivate::Value: a plain Python
    object standing in front of one C++ QXmlStreamReaderPrivate::Value.

    C++ hands a QXmlStreamReaderPrivate::Value around as a copy, so every C++
    QXmlStreamReaderPrivate::Value behind a cute one is Python's own: it is
    removed, by the ritual named in '__delete_ritual__', when the cute object
    goes.

    What exists
    -----------

    No function of Qt's QXmlStreamReaderPrivate::Value yet. None can be made
    from Python: one comes out of a function of another class that gives one
    back.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QXmlStreamReaderPrivate::Value::~Value()': the destructor: Python
      removes its C++ QXmlStreamReaderPrivate::Value by it, and has no other
      use for it.

    What to expect
    --------------

    - The C++ QXmlStreamReaderPrivate::Value is created at the first use, not
      by 'QXmlStreamReaderPrivate::Value(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QXmlStreamReaderPrivate::Value back gives a copy
      the ritual made for Python, in a new cute
      QXmlStreamReaderPrivate::Value.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QXmlStreamReaderPrivate::Value'

    #  Qt's '~QXmlStreamReaderPrivate::Value()'. Naming it makes this a value
    #  class: Python owns every C++ QXmlStreamReaderPrivate::Value behind a
    #  cute one, and removes it by this ritual.
    __delete_ritual__ = 'ritual_ZN23QXmlStreamReaderPrivate5ValueD1Ev'

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
  __qt_class__ = 'QXmlStreamReaderPrivate'

  #  Qt's QXmlStreamReaderPrivate is built on more than one class. The part
  #  of a C++ QXmlStreamReaderPrivate that belongs to a class after the first
  #  begins somewhere inside the object, and the ritual named for that class
  #  gives where; see 'CuteMixin._addressAs'.
  __cast_rituals__ = {
      'QXmlStreamPrivateTagStack':
          'ritual_cast_QXmlStreamReaderPrivate_QXmlStreamPrivateTagStack',
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def entitiesMustBeDeclared(self) -> bool:
    """
    Calls Qt's 'bool QXmlStreamReaderPrivate::entitiesMustBeDeclared()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreaderprivate.html
    """
    #  bool QXmlStreamReaderPrivate::entitiesMustBeDeclared() const
    return self.uglySide.call(
        'ritual_ZNK23QXmlStreamReaderPrivate22entitiesMustBeDeclaredEv',
    )

  @overload(int)
  def symView(self, index: int) -> str:
    """
    Calls Qt's 'QStringView QXmlStreamReaderPrivate::symView(int index)
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreaderprivate.html#symView

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QStringView QXmlStreamReaderPrivate::symView(int index) const
    return self.uglySide.call(
        'ritual_ZNK23QXmlStreamReaderPrivate7symViewEi', index,
    )

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

  @overload(QXmlStreamReader)
  @overload(NoneType)
  def __init__(self, q: Optional[QXmlStreamReader]) -> None:
    """
    Notes what was given, for Qt's
    'QXmlStreamReaderPrivate::QXmlStreamReaderPrivate(QXmlStreamReader *q)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreaderprivate.html

    Parameters
    ----------

    q : Optional[QXmlStreamReader]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QXmlStreamReaderPrivate::QXmlStreamReaderPrivate(QXmlStreamReader *q)
    self._noteCreation(QXmlStreamReaderPrivate, lambda: Rituals.call(
        'ritual_ZN23QXmlStreamReaderPrivateC1EP16QXmlStreamReader',
        self._addressOf(q),
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

  def q_func(self) -> Optional[QXmlStreamReader]:
    """
    Calls Qt's 'QXmlStreamReader *QXmlStreamReaderPrivate::q_func()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreaderprivate.html#q_func

    Returns
    -------

    Optional[QXmlStreamReader]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QXmlStreamReader *QXmlStreamReaderPrivate::q_func()
    address = self.uglySide.call(
        'ritual_ZN23QXmlStreamReaderPrivate6q_funcEv',
    )
    return QXmlStreamReader._cuteAt(address)

  def init(self) -> None:
    """
    Calls Qt's 'void QXmlStreamReaderPrivate::init()'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlstreamreaderprivate.html#init
    """
    #  void QXmlStreamReaderPrivate::init()
    self.uglySide.call('ritual_ZN23QXmlStreamReaderPrivate4initEv')

  def resolvePublicNamespaces(self) -> None:
    """
    Calls Qt's 'void QXmlStreamReaderPrivate::resolvePublicNamespaces()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreaderprivate.html
    """
    #  void QXmlStreamReaderPrivate::resolvePublicNamespaces()
    self.uglySide.call(
        'ritual_ZN23QXmlStreamReaderPrivate23resolvePublicNamespacesEv',
    )

  def resolveDtd(self) -> None:
    """
    Calls Qt's 'void QXmlStreamReaderPrivate::resolveDtd()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreaderprivate.html#resolveDtd
    """
    #  void QXmlStreamReaderPrivate::resolveDtd()
    self.uglySide.call('ritual_ZN23QXmlStreamReaderPrivate10resolveDtdEv')

  @overload(int)
  def resolveCharRef(self, symbolIndex: int) -> int:
    """
    Calls Qt's 'uint QXmlStreamReaderPrivate::resolveCharRef(int
    symbolIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreaderprivate.html#resolveCharRef

    Parameters
    ----------

    symbolIndex : int
      Passed on as it is.
    """
    #  uint QXmlStreamReaderPrivate::resolveCharRef(int symbolIndex)
    return self.uglySide.call(
        'ritual_ZN23QXmlStreamReaderPrivate14resolveCharRefEi', symbolIndex,
    )

  def startDocument(self) -> None:
    """
    Calls Qt's 'void QXmlStreamReaderPrivate::startDocument()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreaderprivate.html#startDocument
    """
    #  void QXmlStreamReaderPrivate::startDocument()
    self.uglySide.call('ritual_ZN23QXmlStreamReaderPrivate13startDocumentEv')

  @overload(int)
  def resume(self, rule: int) -> None:
    """
    Calls Qt's 'void QXmlStreamReaderPrivate::resume(int rule)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreaderprivate.html#resume

    Parameters
    ----------

    rule : int
      Passed on as it is.
    """
    #  void QXmlStreamReaderPrivate::resume(int rule)
    self.uglySide.call('ritual_ZN23QXmlStreamReaderPrivate6resumeEi', rule)

  def reallocateStack(self) -> None:
    """
    Calls Qt's 'void QXmlStreamReaderPrivate::reallocateStack()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreaderprivate.html#reallocateStack
    """
    #  void QXmlStreamReaderPrivate::reallocateStack()
    self.uglySide.call(
        'ritual_ZN23QXmlStreamReaderPrivate15reallocateStackEv',
    )

  def clearTextBuffer(self) -> None:
    """
    Calls Qt's 'void QXmlStreamReaderPrivate::clearTextBuffer()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreaderprivate.html#clearTextBuffer
    """
    #  void QXmlStreamReaderPrivate::clearTextBuffer()
    self.uglySide.call(
        'ritual_ZN23QXmlStreamReaderPrivate15clearTextBufferEv',
    )

  @overload(int)
  def symString(self, index: int) -> QtPrivate.XmlStringRef:
    """
    Calls Qt's 'XmlStringRef QXmlStreamReaderPrivate::symString(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreaderprivate.html#symString

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QtPrivate.XmlStringRef
      A new cute QtPrivate::XmlStringRef around the copy Qt gave back. Python
      owns it.
    """
    #  XmlStringRef QXmlStreamReaderPrivate::symString(int index)
    address = self.uglySide.call(
        'ritual_ZN23QXmlStreamReaderPrivate9symStringEi', index,
    )
    return QtPrivate.XmlStringRef._cuteOwning(address)

  @overload(Value)
  def symString(self, symbol: Value) -> QtPrivate.XmlStringRef:
    """
    Calls Qt's 'XmlStringRef QXmlStreamReaderPrivate::symString(const Value
    &symbol)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreaderprivate.html#symString

    Parameters
    ----------

    symbol : Value
      Passed on as a value: Qt reads the C++ QXmlStreamReaderPrivate::Value,
      which stays Python's own.

    Returns
    -------

    QtPrivate.XmlStringRef
      A new cute QtPrivate::XmlStringRef around the copy Qt gave back. Python
      owns it.
    """
    #  XmlStringRef QXmlStreamReaderPrivate::symString(const Value &symbol)
    address = self.uglySide.call(
        'ritual_ZN23QXmlStreamReaderPrivate9symStringERKNS_5ValueE',
        self._valueOf(symbol),
    )
    return QtPrivate.XmlStringRef._cuteOwning(address)

  @overload(int)
  def symName(self, index: int) -> QtPrivate.XmlStringRef:
    """
    Calls Qt's 'XmlStringRef QXmlStreamReaderPrivate::symName(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreaderprivate.html#symName

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QtPrivate.XmlStringRef
      A new cute QtPrivate::XmlStringRef around the copy Qt gave back. Python
      owns it.
    """
    #  XmlStringRef QXmlStreamReaderPrivate::symName(int index)
    address = self.uglySide.call(
        'ritual_ZN23QXmlStreamReaderPrivate7symNameEi', index,
    )
    return QtPrivate.XmlStringRef._cuteOwning(address)

  @overload(Value)
  def symName(self, symbol: Value) -> QtPrivate.XmlStringRef:
    """
    Calls Qt's 'XmlStringRef QXmlStreamReaderPrivate::symName(const Value
    &symbol)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreaderprivate.html#symName

    Parameters
    ----------

    symbol : Value
      Passed on as a value: Qt reads the C++ QXmlStreamReaderPrivate::Value,
      which stays Python's own.

    Returns
    -------

    QtPrivate.XmlStringRef
      A new cute QtPrivate::XmlStringRef around the copy Qt gave back. Python
      owns it.
    """
    #  XmlStringRef QXmlStreamReaderPrivate::symName(const Value &symbol)
    address = self.uglySide.call(
        'ritual_ZN23QXmlStreamReaderPrivate7symNameERKNS_5ValueE',
        self._valueOf(symbol),
    )
    return QtPrivate.XmlStringRef._cuteOwning(address)

  @overload(int)
  def symPrefix(self, index: int) -> QtPrivate.XmlStringRef:
    """
    Calls Qt's 'XmlStringRef QXmlStreamReaderPrivate::symPrefix(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreaderprivate.html#symPrefix

    Parameters
    ----------

    index : int
      Passed on as it is.

    Returns
    -------

    QtPrivate.XmlStringRef
      A new cute QtPrivate::XmlStringRef around the copy Qt gave back. Python
      owns it.
    """
    #  XmlStringRef QXmlStreamReaderPrivate::symPrefix(int index)
    address = self.uglySide.call(
        'ritual_ZN23QXmlStreamReaderPrivate9symPrefixEi', index,
    )
    return QtPrivate.XmlStringRef._cuteOwning(address)

  @overload(Value)
  def symPrefix(self, symbol: Value) -> QtPrivate.XmlStringRef:
    """
    Calls Qt's 'XmlStringRef QXmlStreamReaderPrivate::symPrefix(const Value
    &symbol)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreaderprivate.html#symPrefix

    Parameters
    ----------

    symbol : Value
      Passed on as a value: Qt reads the C++ QXmlStreamReaderPrivate::Value,
      which stays Python's own.

    Returns
    -------

    QtPrivate.XmlStringRef
      A new cute QtPrivate::XmlStringRef around the copy Qt gave back. Python
      owns it.
    """
    #  XmlStringRef QXmlStreamReaderPrivate::symPrefix(const Value &symbol)
    address = self.uglySide.call(
        'ritual_ZN23QXmlStreamReaderPrivate9symPrefixERKNS_5ValueE',
        self._valueOf(symbol),
    )
    return QtPrivate.XmlStringRef._cuteOwning(address)

  def clearSym(self) -> None:
    """
    Calls Qt's 'void QXmlStreamReaderPrivate::clearSym()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreaderprivate.html#clearSym
    """
    #  void QXmlStreamReaderPrivate::clearSym()
    self.uglySide.call('ritual_ZN23QXmlStreamReaderPrivate8clearSymEv')

  def filterCarriageReturn(self) -> int:
    """
    Calls Qt's 'uint QXmlStreamReaderPrivate::filterCarriageReturn()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreaderprivate.html#filterCarriageReturn
    """
    #  uint QXmlStreamReaderPrivate::filterCarriageReturn()
    return self.uglySide.call(
        'ritual_ZN23QXmlStreamReaderPrivate20filterCarriageReturnEv',
    )

  @overload(int)
  def putChar(self, c: int) -> None:
    """
    Calls Qt's 'void QXmlStreamReaderPrivate::putChar(uint c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreaderprivate.html#putChar

    Parameters
    ----------

    c : int
      Passed on as it is.
    """
    #  void QXmlStreamReaderPrivate::putChar(uint c)
    self.uglySide.call('ritual_ZN23QXmlStreamReaderPrivate7putCharEj', c)

  @overload(QChar)
  def putChar(self, c: QChar) -> None:
    """
    Calls Qt's 'void QXmlStreamReaderPrivate::putChar(QChar c)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreaderprivate.html#putChar

    Parameters
    ----------

    c : QChar
      Passed on as a value: Qt reads the C++ QChar, which stays Python's own.
    """
    #  void QXmlStreamReaderPrivate::putChar(QChar c)
    self.uglySide.call(
        'ritual_ZN23QXmlStreamReaderPrivate7putCharE5QChar',
        self._valueOf(c),
    )

  @overload(str)
  @overload(str, int)
  def putString(self, s: str, from_: int = 0) -> None:
    """
    Calls Qt's 'void QXmlStreamReaderPrivate::putString(QStringView s,
    qsizetype from)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreaderprivate.html#putString

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.

    from_ : int
      Passed on as it is. May be left out, as in Qt: it is then 0.
    """
    #  void QXmlStreamReaderPrivate::putString(QStringView s, qsizetype from)
    self.uglySide.call(
        'ritual_ZN23QXmlStreamReaderPrivate9putStringE11QStringViewx',
        s, from_,
    )

  @overload(str)
  def putStringLiteral(self, s: str) -> None:
    """
    Calls Qt's 'void QXmlStreamReaderPrivate::putStringLiteral(QStringView
    s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreaderprivate.html#putStringLiteral

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QXmlStreamReaderPrivate::putStringLiteral(QStringView s)
    self.uglySide.call(
        'ritual_ZN23QXmlStreamReaderPrivate16putStringLiteralE11QStringView',
        s,
    )

  @overload(str)
  def putReplacement(self, s: str) -> None:
    """
    Calls Qt's 'void QXmlStreamReaderPrivate::putReplacement(QStringView s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreaderprivate.html#putReplacement

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QXmlStreamReaderPrivate::putReplacement(QStringView s)
    self.uglySide.call(
        'ritual_ZN23QXmlStreamReaderPrivate14putReplacementE11QStringView',
        s,
    )

  @overload(str)
  def putReplacementInAttributeValue(self, s: str) -> None:
    """
    Calls Qt's 'void
    QXmlStreamReaderPrivate::putReplacementInAttributeValue(QStringView s)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreaderprivate.html

    Parameters
    ----------

    s : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QXmlStreamReaderPrivate::putReplacementInAttributeValue(
    #      QStringView s)
    self.uglySide.call(
        'ritual_ZN23QXmlStreamReaderPrivate30putReplacementInAttributeValue'
        'E11QStringView',
        s,
    )

  @overload(int)
  def injectToken(self, tokenToInject: int) -> None:
    """
    Calls Qt's 'void QXmlStreamReaderPrivate::injectToken(ushort
    tokenToInject)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreaderprivate.html#injectToken

    Parameters
    ----------

    tokenToInject : int
      Passed on as it is.
    """
    #  void QXmlStreamReaderPrivate::injectToken(ushort tokenToInject)
    self.uglySide.call(
        'ritual_ZN23QXmlStreamReaderPrivate11injectTokenEt', tokenToInject,
    )

  @overload(str)
  def resolveUndeclaredEntity(self, name: str) -> str:
    """
    Calls Qt's 'QString
    QXmlStreamReaderPrivate::resolveUndeclaredEntity(const QString &name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreaderprivate.html

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QXmlStreamReaderPrivate::resolveUndeclaredEntity(const QString
    #      &name)
    return self.uglySide.call(
        'ritual_ZN23QXmlStreamReaderPrivate23resolveUndeclaredEntityERK7QSt'
        'ring',
        name,
    )

  @overload(QXmlStreamReader.Error)
  @overload(QXmlStreamReader.Error, str)
  def raiseError(
      self,
      error: QXmlStreamReader.Error,
      message: str = '',
  ) -> None:
    """
    Calls Qt's 'void
    QXmlStreamReaderPrivate::raiseError(QXmlStreamReader::Error error, const
    QString &message)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreaderprivate.html#raiseError

    Parameters
    ----------

    error : QXmlStreamReader.Error
      Passed on as its number.

    message : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.
    """
    #  void QXmlStreamReaderPrivate::raiseError(QXmlStreamReader::Error
    #      error, const QString &message)
    self.uglySide.call(
        'ritual_ZN23QXmlStreamReaderPrivate10raiseErrorEN16QXmlStreamReader'
        '5ErrorERK7QString',
        error.value, message,
    )

  @overload(str)
  def raiseWellFormedError(self, message: str) -> None:
    """
    Calls Qt's 'void QXmlStreamReaderPrivate::raiseWellFormedError(const
    QString &message)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreaderprivate.html#raiseWellFormedError

    Parameters
    ----------

    message : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QXmlStreamReaderPrivate::raiseWellFormedError(const QString
    #      &message)
    self.uglySide.call(
        'ritual_ZN23QXmlStreamReaderPrivate20raiseWellFormedErrorERK7QStrin'
        'g',
        message,
    )

  def raiseNamePrefixTooLongError(self) -> None:
    """
    Calls Qt's 'void QXmlStreamReaderPrivate::raiseNamePrefixTooLongError()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlstreamreaderprivate.html
    """
    #  void QXmlStreamReaderPrivate::raiseNamePrefixTooLongError()
    self.uglySide.call(
        'ritual_ZN23QXmlStreamReaderPrivate27raiseNamePrefixTooLongErrorEv',
    )

  @staticmethod
  def appendDataWithEncoding(*__, **_) -> Never:
    """
    Qt's 'void QXmlStreamReaderPrivate::appendDataWithEncoding(const
    QByteArray &data, QStringDecoder::Encoding enc)': takes a type Python has
    no way to hand over yet.
    """
    raise NotImplementedError(
        "'QXmlStreamReaderPrivate.appendDataWithEncoding' has no cute "
        "function yet. Qt's 'void "
        "QXmlStreamReaderPrivate::appendDataWithEncoding(const QByteArray "
        "&data, QStringDecoder::Encoding enc)': takes a type Python has no "
        "way to hand over yet.")

  @staticmethod
  def checkPublicLiteral(*__, **_) -> Never:
    """
    Qt's 'void QXmlStreamReaderPrivate::checkPublicLiteral(QStringView
    publicId)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'isAsciiLetterOrNumber'; did you mean
    'QtMiscUtils::isAsciiLetterOrNumber'?.
    """
    raise NotImplementedError(
        "'QXmlStreamReaderPrivate.checkPublicLiteral' has no cute function "
        "yet. Qt's 'void "
        "QXmlStreamReaderPrivate::checkPublicLiteral(QStringView "
        "publicId)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'isAsciiLetterOrNumber'; did you mean "
        "'QtMiscUtils::isAsciiLetterOrNumber'?.")

  @staticmethod
  def checkStartDocument(*__, **_) -> Never:
    """
    Qt's 'bool QXmlStreamReaderPrivate::checkStartDocument()': leans on
    'QXmlStreamGrammar::spell', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QXmlStreamReaderPrivate.checkStartDocument' has no cute function "
        "yet. Qt's 'bool QXmlStreamReaderPrivate::checkStartDocument()': "
        "leans on 'QXmlStreamGrammar::spell', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def checkToken(*__, **_) -> Never:
    """
    Qt's 'void QXmlStreamReaderPrivate::checkToken()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'contextString'.
    """
    raise NotImplementedError(
        "'QXmlStreamReaderPrivate.checkToken' has no cute function yet. "
        "Qt's 'void QXmlStreamReaderPrivate::checkToken()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'contextString'.")

  @staticmethod
  def consumeRule(*__, **_) -> Never:
    """
    Qt's 'void QXmlStreamReaderPrivate::consumeRule(int a0)': cannot be
    called and cannot be called through the meta-object and cannot be copied:
    no header file has its code, Qt's source does not mark it or its class
    for use from outside Qt or writes it 'inline' or nowhere, and it is no
    signal, slot or invokable function giving back nothing, of a class built
    on QObject, and Qt's source has no code for it that could be told from
    the rest.
    """
    raise NotImplementedError(
        "'QXmlStreamReaderPrivate.consumeRule' has no cute function yet. "
        "Qt's 'void QXmlStreamReaderPrivate::consumeRule(int a0)': cannot "
        "be called and cannot be called through the meta-object and cannot "
        "be copied: no header file has its code, Qt's source does not mark "
        "it or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest.")

  @staticmethod
  def fastScanContentCharList(*__, **_) -> Never:
    """
    Qt's 'qsizetype QXmlStreamReaderPrivate::fastScanContentCharList()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'StreamEOF'.
    """
    raise NotImplementedError(
        "'QXmlStreamReaderPrivate.fastScanContentCharList' has no cute "
        "function yet. Qt's 'qsizetype "
        "QXmlStreamReaderPrivate::fastScanContentCharList()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'StreamEOF'.")

  @staticmethod
  def fastScanLiteralContent(*__, **_) -> Never:
    """
    Qt's 'qsizetype QXmlStreamReaderPrivate::fastScanLiteralContent()': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'StreamEOF'.
    """
    raise NotImplementedError(
        "'QXmlStreamReaderPrivate.fastScanLiteralContent' has no cute "
        "function yet. Qt's 'qsizetype "
        "QXmlStreamReaderPrivate::fastScanLiteralContent()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'StreamEOF'.")

  @staticmethod
  def fastScanNMTOKEN(*__, **_) -> Never:
    """
    Qt's 'qsizetype QXmlStreamReaderPrivate::fastScanNMTOKEN()': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'StreamEOF'.
    """
    raise NotImplementedError(
        "'QXmlStreamReaderPrivate.fastScanNMTOKEN' has no cute function "
        "yet. Qt's 'qsizetype QXmlStreamReaderPrivate::fastScanNMTOKEN()': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'StreamEOF'.")

  @staticmethod
  def fastScanName(*__, **_) -> Never:
    """
    Qt's 'std::optional<qsizetype>
    QXmlStreamReaderPrivate::fastScanName(Value *val)': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'StreamEOF'.
    """
    raise NotImplementedError(
        "'QXmlStreamReaderPrivate.fastScanName' has no cute function yet. "
        "Qt's 'std::optional<qsizetype> "
        "QXmlStreamReaderPrivate::fastScanName(Value *val)': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'StreamEOF'.")

  @staticmethod
  def fastScanSpace(*__, **_) -> Never:
    """
    Qt's 'qsizetype QXmlStreamReaderPrivate::fastScanSpace()': Qt's library
    has no name for it, and its code in Qt's source does not compile apart
    from its file: use of undeclared identifier 'StreamEOF'.
    """
    raise NotImplementedError(
        "'QXmlStreamReaderPrivate.fastScanSpace' has no cute function yet. "
        "Qt's 'qsizetype QXmlStreamReaderPrivate::fastScanSpace()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'StreamEOF'.")

  @staticmethod
  def getChar(*__, **_) -> Never:
    """
    Qt's 'uint QXmlStreamReaderPrivate::getChar()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'StreamEOF'.
    """
    raise NotImplementedError(
        "'QXmlStreamReaderPrivate.getChar' has no cute function yet. Qt's "
        "'uint QXmlStreamReaderPrivate::getChar()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'StreamEOF'.")

  @staticmethod
  def getChar_helper(*__, **_) -> Never:
    """
    Qt's 'uint QXmlStreamReaderPrivate::getChar_helper()': Qt's library has
    no name for it, and its code in Qt's source does not compile apart from
    its file: use of undeclared identifier 'StreamEOF'.
    """
    raise NotImplementedError(
        "'QXmlStreamReaderPrivate.getChar_helper' has no cute function yet. "
        "Qt's 'uint QXmlStreamReaderPrivate::getChar_helper()': Qt's "
        "library has no name for it, and its code in Qt's source does not "
        "compile apart from its file: use of undeclared identifier "
        "'StreamEOF'.")

  @staticmethod
  def isValidToken(*__, **_) -> Never:
    """
    Qt's 'bool
    QXmlStreamReaderPrivate::isValidToken(QXmlStreamReader::TokenType type)':
    Qt's library has no name for it, and its code in Qt's source does not
    compile apart from its file: use of undeclared identifier
    'isTokenAllowedInContext'.
    """
    raise NotImplementedError(
        "'QXmlStreamReaderPrivate.isValidToken' has no cute function yet. "
        "Qt's 'bool "
        "QXmlStreamReaderPrivate::isValidToken(QXmlStreamReader::TokenType "
        "type)': Qt's library has no name for it, and its code in Qt's "
        "source does not compile apart from its file: use of undeclared "
        "identifier 'isTokenAllowedInContext'.")

  @staticmethod
  def namespaceForPrefix(*__, **_) -> Never:
    """
    Qt's 'XmlStringRef
    QXmlStreamReaderPrivate::namespaceForPrefix(QStringView prefix)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: unknown type name 'XmlStringRef'.
    """
    raise NotImplementedError(
        "'QXmlStreamReaderPrivate.namespaceForPrefix' has no cute function "
        "yet. Qt's 'XmlStringRef "
        "QXmlStreamReaderPrivate::namespaceForPrefix(QStringView prefix)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: unknown type name 'XmlStringRef'.")

  @staticmethod
  def parse(*__, **_) -> Never:
    """
    Qt's 'bool QXmlStreamReaderPrivate::parse()': leans on
    'QXmlStreamGrammar::action_info', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QXmlStreamReaderPrivate.parse' has no cute function yet. Qt's "
        "'bool QXmlStreamReaderPrivate::parse()': leans on "
        "'QXmlStreamGrammar::action_info', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def parseEntity(*__, **_) -> Never:
    """
    Qt's 'void QXmlStreamReaderPrivate::parseEntity(const QString &value)':
    leans on 'QXmlStreamGrammar::action_info', which Qt's source does not
    mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QXmlStreamReaderPrivate.parseEntity' has no cute function yet. "
        "Qt's 'void QXmlStreamReaderPrivate::parseEntity(const QString "
        "&value)': leans on 'QXmlStreamGrammar::action_info', which Qt's "
        "source does not mark for use from outside Qt and has no code for "
        "that could be taken.")

  @staticmethod
  def parseError(*__, **_) -> Never:
    """
    Qt's 'void QXmlStreamReaderPrivate::parseError()': leans on
    'QXmlStreamGrammar::action_info', which Qt's source does not mark for use
    from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QXmlStreamReaderPrivate.parseError' has no cute function yet. "
        "Qt's 'void QXmlStreamReaderPrivate::parseError()': leans on "
        "'QXmlStreamGrammar::action_info', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def peekChar(*__, **_) -> Never:
    """
    Qt's 'uint QXmlStreamReaderPrivate::peekChar()': Qt's library has no name
    for it, and its code in Qt's source does not compile apart from its file:
    use of undeclared identifier 'StreamEOF'.
    """
    raise NotImplementedError(
        "'QXmlStreamReaderPrivate.peekChar' has no cute function yet. Qt's "
        "'uint QXmlStreamReaderPrivate::peekChar()': Qt's library has no "
        "name for it, and its code in Qt's source does not compile apart "
        "from its file: use of undeclared identifier 'StreamEOF'.")

  @staticmethod
  def referenceEntity(*__, **_) -> Never:
    """
    Qt's 'bool QXmlStreamReaderPrivate::referenceEntity(QHash<QStringView,
    Entity> *hash, Entity &entity)': names 'QHash<QStringView,
    QXmlStreamReaderPrivate::Entity>', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QXmlStreamReaderPrivate.referenceEntity' has no cute function "
        "yet. Qt's 'bool "
        "QXmlStreamReaderPrivate::referenceEntity(QHash<QStringView, "
        "Entity> *hash, Entity &entity)': names 'QHash<QStringView, "
        "QXmlStreamReaderPrivate::Entity>', which has no cute class yet.")

  @staticmethod
  def resolveTag(*__, **_) -> Never:
    """
    Qt's 'void QXmlStreamReaderPrivate::resolveTag()': Qt's library has no
    name for it, and its code in Qt's source does not compile apart from its
    file: use of undeclared identifier 'AttributeName'; did you mean
    'Attribute'?.
    """
    raise NotImplementedError(
        "'QXmlStreamReaderPrivate.resolveTag' has no cute function yet. "
        "Qt's 'void QXmlStreamReaderPrivate::resolveTag()': Qt's library "
        "has no name for it, and its code in Qt's source does not compile "
        "apart from its file: use of undeclared identifier 'AttributeName'; "
        "did you mean 'Attribute'?.")

  @staticmethod
  def scanAfterDefaultDecl(*__, **_) -> Never:
    """
    Qt's 'bool QXmlStreamReaderPrivate::scanAfterDefaultDecl()': leans on
    'QXmlStreamGrammar::spell', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QXmlStreamReaderPrivate.scanAfterDefaultDecl' has no cute "
        "function yet. Qt's 'bool "
        "QXmlStreamReaderPrivate::scanAfterDefaultDecl()': leans on "
        "'QXmlStreamGrammar::spell', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def scanAfterLangleBang(*__, **_) -> Never:
    """
    Qt's 'bool QXmlStreamReaderPrivate::scanAfterLangleBang()': leans on
    'QXmlStreamGrammar::spell', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QXmlStreamReaderPrivate.scanAfterLangleBang' has no cute function "
        "yet. Qt's 'bool QXmlStreamReaderPrivate::scanAfterLangleBang()': "
        "leans on 'QXmlStreamGrammar::spell', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def scanAttType(*__, **_) -> Never:
    """
    Qt's 'bool QXmlStreamReaderPrivate::scanAttType()': leans on
    'QXmlStreamGrammar::spell', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QXmlStreamReaderPrivate.scanAttType' has no cute function yet. "
        "Qt's 'bool QXmlStreamReaderPrivate::scanAttType()': leans on "
        "'QXmlStreamGrammar::spell', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def scanNData(*__, **_) -> Never:
    """
    Qt's 'bool QXmlStreamReaderPrivate::scanNData()': leans on
    'QXmlStreamGrammar::spell', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QXmlStreamReaderPrivate.scanNData' has no cute function yet. Qt's "
        "'bool QXmlStreamReaderPrivate::scanNData()': leans on "
        "'QXmlStreamGrammar::spell', which Qt's source does not mark for "
        "use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def scanPublicOrSystem(*__, **_) -> Never:
    """
    Qt's 'bool QXmlStreamReaderPrivate::scanPublicOrSystem()': leans on
    'QXmlStreamGrammar::spell', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QXmlStreamReaderPrivate.scanPublicOrSystem' has no cute function "
        "yet. Qt's 'bool QXmlStreamReaderPrivate::scanPublicOrSystem()': "
        "leans on 'QXmlStreamGrammar::spell', which Qt's source does not "
        "mark for use from outside Qt and has no code for that could be "
        "taken.")

  @staticmethod
  def scanString(*__, **_) -> Never:
    """
    Qt's 'bool QXmlStreamReaderPrivate::scanString(const char *str, short
    tokenToInject, bool requireSpace)': Qt's library has no name for it, and
    its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'StreamEOF'.
    """
    raise NotImplementedError(
        "'QXmlStreamReaderPrivate.scanString' has no cute function yet. "
        "Qt's 'bool QXmlStreamReaderPrivate::scanString(const char *str, "
        "short tokenToInject, bool requireSpace)': Qt's library has no name "
        "for it, and its code in Qt's source does not compile apart from "
        "its file: use of undeclared identifier 'StreamEOF'.")

  @staticmethod
  def scanUntil(*__, **_) -> Never:
    """
    Qt's 'bool QXmlStreamReaderPrivate::scanUntil(const char *str, short
    tokenToInject)': Qt's library has no name for it, and its code in Qt's
    source does not compile apart from its file: use of undeclared identifier
    'StreamEOF'.
    """
    raise NotImplementedError(
        "'QXmlStreamReaderPrivate.scanUntil' has no cute function yet. Qt's "
        "'bool QXmlStreamReaderPrivate::scanUntil(const char *str, short "
        "tokenToInject)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'StreamEOF'.")

  @staticmethod
  def setType(*__, **_) -> Never:
    """
    Qt's 'void QXmlStreamReaderPrivate::setType(const
    QXmlStreamReader::TokenType t)': takes a type Python has no way to hand
    over yet.
    """
    raise NotImplementedError(
        "'QXmlStreamReaderPrivate.setType' has no cute function yet. Qt's "
        "'void QXmlStreamReaderPrivate::setType(const "
        "QXmlStreamReader::TokenType t)': takes a type Python has no way to "
        "hand over yet.")

  @staticmethod
  def sym(*__, **_) -> Never:
    """
    Qt's 'Value &QXmlStreamReaderPrivate::sym(int index) const': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QXmlStreamReaderPrivate.sym' has no cute function yet. Qt's "
        "'Value &QXmlStreamReaderPrivate::sym(int index) const': gives a "
        "type Python has no way to take yet.")

  @staticmethod
  def symQName(*__, **_) -> Never:
    """
    Qt's 'R QXmlStreamReaderPrivate::symQName(int index)': the compiler
    refuses its ritual as it would be written here: unknown type name 'R'.
    """
    raise NotImplementedError(
        "'QXmlStreamReaderPrivate.symQName' has no cute function yet. Qt's "
        "'R QXmlStreamReaderPrivate::symQName(int index)': the compiler "
        "refuses its ritual as it would be written here: unknown type name "
        "'R'.")

  @staticmethod
  def write(*__, **_) -> Never:
    """
    - Qt's 'void QXmlStreamReaderPrivate::write(const QString &a0)': cannot
      be called and cannot be called through the meta-object and cannot be
      copied: no header file has its code, Qt's source does not mark it or
      its class for use from outside Qt or writes it 'inline' or nowhere, and
      it is no signal, slot or invokable function giving back nothing, of a
      class built on QObject, and Qt's source has no code for it that could
      be told from the rest.
    - Qt's 'void QXmlStreamReaderPrivate::write(const char *a0)': cannot be
      called and cannot be called through the meta-object and cannot be
      copied: no header file has its code, Qt's source does not mark it or
      its class for use from outside Qt or writes it 'inline' or nowhere, and
      it is no signal, slot or invokable function giving back nothing, of a
      class built on QObject, and Qt's source has no code for it that could
      be told from the rest.
    """
    raise NotImplementedError(
        "'QXmlStreamReaderPrivate.write' has no cute function yet. Qt's "
        "'void QXmlStreamReaderPrivate::write(const QString &a0)': cannot "
        "be called and cannot be called through the meta-object and cannot "
        "be copied: no header file has its code, Qt's source does not mark "
        "it or its class for use from outside Qt or writes it 'inline' or "
        "nowhere, and it is no signal, slot or invokable function giving "
        "back nothing, of a class built on QObject, and Qt's source has no "
        "code for it that could be told from the rest. Qt's 'void "
        "QXmlStreamReaderPrivate::write(const char *a0)': cannot be called "
        "and cannot be called through the meta-object and cannot be copied: "
        "no header file has its code, Qt's source does not mark it or its "
        "class for use from outside Qt or writes it 'inline' or nowhere, "
        "and it is no signal, slot or invokable function giving back "
        "nothing, of a class built on QObject, and Qt's source has no code "
        "for it that could be told from the rest.")
