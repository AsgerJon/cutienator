"""
QXmlReader binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore5Compat/qxml.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QXmlContentHandler, QXmlDTDHandler, QXmlDeclHandler
  from . import QXmlEntityResolver, QXmlErrorHandler, QXmlInputSource
  from . import QXmlLexicalHandler
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QXmlContentHandler = WAIT['QXmlContentHandler']
  QXmlDTDHandler = WAIT['QXmlDTDHandler']
  QXmlDeclHandler = WAIT['QXmlDeclHandler']
  QXmlEntityResolver = WAIT['QXmlEntityResolver']
  QXmlErrorHandler = WAIT['QXmlErrorHandler']
  QXmlInputSource = WAIT['QXmlInputSource']
  QXmlLexicalHandler = WAIT['QXmlLexicalHandler']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QXmlReader(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QXmlReader: a plain Python object standing in front
  of one C++ QXmlReader.

  What exists
  -----------

  Every function of Qt's QXmlReader that has a ritual and that Python can
  call so far, 16 names in all: 'setFeature', 'hasFeature', 'hasProperty',
  'setEntityResolver', 'entityResolver', 'setDTDHandler', 'DTDHandler',
  'setContentHandler', 'contentHandler', 'setErrorHandler', 'errorHandler',
  'setLexicalHandler', 'lexicalHandler', 'setDeclHandler', 'declHandler',
  'parse'. None can be made from Python: one comes out of a function of
  another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QXmlReader::~QXmlReader()': the destructor: Python never removes a
    C++ QXmlReader.
  - Qt's 'bool QXmlReader::feature(const QString &name, bool *ok) const':
    takes a number to change where it is.
  - Qt's 'void *QXmlReader::property(const QString &name, bool *ok) const':
    takes a number to change where it is.
  - Qt's 'void QXmlReader::setProperty(const QString &name, void *value)':
    names 'void', which has no cute class yet.

  What to expect
  --------------

  - The C++ QXmlReader is created at the first use, not by 'QXmlReader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QXmlReader.
  - Each name of Qt's QXmlReader that has no cute function yet, 'feature',
    'property', 'setProperty', holds a function that raises
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
  __qt_class__ = 'QXmlReader'

  #  A C++ QXmlReader Python makes is of a C++ class of ours, in which Python
  #  can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QXmlReader'

  #  The functions Qt calls itself that QXmlReader is the first to declare
  #  and that cannot be handed to Python yet, each as Qt declares it. A class
  #  of a program that writes one of them anew is refused, since Qt would
  #  never call what it wrote; see 'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'feature': (
          'bool QXmlReader::feature(const QString &, bool *) const',
      ),
      'property': (
          'void *QXmlReader::property(const QString &, bool *) const',
      ),
      'setProperty': (
          'void QXmlReader::setProperty(const QString &, void *)',
      ),
  }

  #  The functions Qt calls itself that QXmlReader is the first to declare. A
  #  class of a program built on it can write one anew, and Qt then calls
  #  that. For each name: the key C++ knows the function by, what it gives,
  #  and what it takes.
  __virtual_functions__ = {
      'setFeature': (
          ('_ZN10QXmlReader10setFeatureERK7QStringb',
           ('nothing', 'nothing', ''),
           (
               ('address', 'text', ''),
               ('bool', 'number', ''),
           )),
      ),
      'hasFeature': (
          ('_ZNK10QXmlReader10hasFeatureERK7QString',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'hasProperty': (
          ('_ZNK10QXmlReader11hasPropertyERK7QString',
           ('bool', 'number', ''),
           (
               ('address', 'text', ''),
           )),
      ),
      'setEntityResolver': (
          ('_ZN10QXmlReader17setEntityResolverEP18QXmlEntityResolver',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore5Compat:QXmlEntityResolver'),
           )),
      ),
      'entityResolver': (
          ('_ZNK10QXmlReader14entityResolverEv',
           ('address', 'address', 'QtCore5Compat:QXmlEntityResolver'),
           ()),
      ),
      'setDTDHandler': (
          ('_ZN10QXmlReader13setDTDHandlerEP14QXmlDTDHandler',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore5Compat:QXmlDTDHandler'),
           )),
      ),
      'DTDHandler': (
          ('_ZNK10QXmlReader10DTDHandlerEv',
           ('address', 'address', 'QtCore5Compat:QXmlDTDHandler'),
           ()),
      ),
      'setContentHandler': (
          ('_ZN10QXmlReader17setContentHandlerEP18QXmlContentHandler',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore5Compat:QXmlContentHandler'),
           )),
      ),
      'contentHandler': (
          ('_ZNK10QXmlReader14contentHandlerEv',
           ('address', 'address', 'QtCore5Compat:QXmlContentHandler'),
           ()),
      ),
      'setErrorHandler': (
          ('_ZN10QXmlReader15setErrorHandlerEP16QXmlErrorHandler',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore5Compat:QXmlErrorHandler'),
           )),
      ),
      'errorHandler': (
          ('_ZNK10QXmlReader12errorHandlerEv',
           ('address', 'address', 'QtCore5Compat:QXmlErrorHandler'),
           ()),
      ),
      'setLexicalHandler': (
          ('_ZN10QXmlReader17setLexicalHandlerEP18QXmlLexicalHandler',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore5Compat:QXmlLexicalHandler'),
           )),
      ),
      'lexicalHandler': (
          ('_ZNK10QXmlReader14lexicalHandlerEv',
           ('address', 'address', 'QtCore5Compat:QXmlLexicalHandler'),
           ()),
      ),
      'setDeclHandler': (
          ('_ZN10QXmlReader14setDeclHandlerEP15QXmlDeclHandler',
           ('nothing', 'nothing', ''),
           (
               ('address', 'address', 'QtCore5Compat:QXmlDeclHandler'),
           )),
      ),
      'declHandler': (
          ('_ZNK10QXmlReader11declHandlerEv',
           ('address', 'address', 'QtCore5Compat:QXmlDeclHandler'),
           ()),
      ),
      'parse': (
          ('_ZN10QXmlReader5parseERK15QXmlInputSource',
           ('bool', 'number', ''),
           (
               ('address', 'value', 'QtCore5Compat:QXmlInputSource'),
           )),
          ('_ZN10QXmlReader5parseEPK15QXmlInputSource',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtCore5Compat:QXmlInputSource'),
           )),
      ),
  }

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def hasFeature(self, name: str) -> bool:
    """
    Calls Qt's 'bool QXmlReader::hasFeature(const QString &name) const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlreader.html#hasFeature

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QXmlReader::hasFeature(const QString &name) const
    return self.uglySide.call(
        'ritual_ZNK10QXmlReader10hasFeatureERK7QString', name,
    )

  @overload(str)
  def hasProperty(self, name: str) -> bool:
    """
    Calls Qt's 'bool QXmlReader::hasProperty(const QString &name) const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlreader.html#hasProperty

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QXmlReader::hasProperty(const QString &name) const
    return self.uglySide.call(
        'ritual_ZNK10QXmlReader11hasPropertyERK7QString', name,
    )

  def entityResolver(self) -> Optional[QXmlEntityResolver]:
    """
    Calls Qt's 'QXmlEntityResolver *QXmlReader::entityResolver() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlreader.html#entityResolver

    Returns
    -------

    Optional[QXmlEntityResolver]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QXmlEntityResolver *QXmlReader::entityResolver() const
    address = self.uglySide.call('ritual_ZNK10QXmlReader14entityResolverEv')
    from . import QXmlEntityResolver
    return QXmlEntityResolver._cuteAt(address)

  def DTDHandler(self) -> Optional[QXmlDTDHandler]:
    """
    Calls Qt's 'QXmlDTDHandler *QXmlReader::DTDHandler() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlreader.html#DTDHandler

    Returns
    -------

    Optional[QXmlDTDHandler]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QXmlDTDHandler *QXmlReader::DTDHandler() const
    address = self.uglySide.call('ritual_ZNK10QXmlReader10DTDHandlerEv')
    from . import QXmlDTDHandler
    return QXmlDTDHandler._cuteAt(address)

  def contentHandler(self) -> Optional[QXmlContentHandler]:
    """
    Calls Qt's 'QXmlContentHandler *QXmlReader::contentHandler() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlreader.html#contentHandler

    Returns
    -------

    Optional[QXmlContentHandler]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QXmlContentHandler *QXmlReader::contentHandler() const
    address = self.uglySide.call('ritual_ZNK10QXmlReader14contentHandlerEv')
    from . import QXmlContentHandler
    return QXmlContentHandler._cuteAt(address)

  def errorHandler(self) -> Optional[QXmlErrorHandler]:
    """
    Calls Qt's 'QXmlErrorHandler *QXmlReader::errorHandler() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlreader.html#errorHandler

    Returns
    -------

    Optional[QXmlErrorHandler]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QXmlErrorHandler *QXmlReader::errorHandler() const
    address = self.uglySide.call('ritual_ZNK10QXmlReader12errorHandlerEv')
    from . import QXmlErrorHandler
    return QXmlErrorHandler._cuteAt(address)

  def lexicalHandler(self) -> Optional[QXmlLexicalHandler]:
    """
    Calls Qt's 'QXmlLexicalHandler *QXmlReader::lexicalHandler() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlreader.html#lexicalHandler

    Returns
    -------

    Optional[QXmlLexicalHandler]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QXmlLexicalHandler *QXmlReader::lexicalHandler() const
    address = self.uglySide.call('ritual_ZNK10QXmlReader14lexicalHandlerEv')
    from . import QXmlLexicalHandler
    return QXmlLexicalHandler._cuteAt(address)

  def declHandler(self) -> Optional[QXmlDeclHandler]:
    """
    Calls Qt's 'QXmlDeclHandler *QXmlReader::declHandler() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlreader.html#declHandler

    Returns
    -------

    Optional[QXmlDeclHandler]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QXmlDeclHandler *QXmlReader::declHandler() const
    address = self.uglySide.call('ritual_ZNK10QXmlReader11declHandlerEv')
    from . import QXmlDeclHandler
    return QXmlDeclHandler._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str, bool)
  def setFeature(self, name: str, value: bool) -> None:
    """
    Calls Qt's 'void QXmlReader::setFeature(const QString &name, bool
    value)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlreader.html#setFeature

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : bool
      Passed on as it is.
    """
    #  void QXmlReader::setFeature(const QString &name, bool value)
    self.uglySide.call(
        'ritual_ZN10QXmlReader10setFeatureERK7QStringb', name, value,
    )

  @overload(QXmlEntityResolver)
  @overload(NoneType)
  def setEntityResolver(self, handler: Optional[QXmlEntityResolver]) -> None:
    """
    Calls Qt's 'void QXmlReader::setEntityResolver(QXmlEntityResolver
    *handler)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlreader.html#setEntityResolver

    Parameters
    ----------

    handler : Optional[QXmlEntityResolver]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QXmlReader::setEntityResolver(QXmlEntityResolver *handler)
    self.uglySide.call(
        'ritual_ZN10QXmlReader17setEntityResolverEP18QXmlEntityResolver',
        self._addressOf(handler, 'QXmlEntityResolver'),
    )

  @overload(QXmlDTDHandler)
  @overload(NoneType)
  def setDTDHandler(self, handler: Optional[QXmlDTDHandler]) -> None:
    """
    Calls Qt's 'void QXmlReader::setDTDHandler(QXmlDTDHandler *handler)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlreader.html#setDTDHandler

    Parameters
    ----------

    handler : Optional[QXmlDTDHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QXmlReader::setDTDHandler(QXmlDTDHandler *handler)
    self.uglySide.call(
        'ritual_ZN10QXmlReader13setDTDHandlerEP14QXmlDTDHandler',
        self._addressOf(handler, 'QXmlDTDHandler'),
    )

  @overload(QXmlContentHandler)
  @overload(NoneType)
  def setContentHandler(self, handler: Optional[QXmlContentHandler]) -> None:
    """
    Calls Qt's 'void QXmlReader::setContentHandler(QXmlContentHandler
    *handler)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlreader.html#setContentHandler

    Parameters
    ----------

    handler : Optional[QXmlContentHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QXmlReader::setContentHandler(QXmlContentHandler *handler)
    self.uglySide.call(
        'ritual_ZN10QXmlReader17setContentHandlerEP18QXmlContentHandler',
        self._addressOf(handler),
    )

  @overload(QXmlErrorHandler)
  @overload(NoneType)
  def setErrorHandler(self, handler: Optional[QXmlErrorHandler]) -> None:
    """
    Calls Qt's 'void QXmlReader::setErrorHandler(QXmlErrorHandler *handler)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlreader.html#setErrorHandler

    Parameters
    ----------

    handler : Optional[QXmlErrorHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QXmlReader::setErrorHandler(QXmlErrorHandler *handler)
    self.uglySide.call(
        'ritual_ZN10QXmlReader15setErrorHandlerEP16QXmlErrorHandler',
        self._addressOf(handler, 'QXmlErrorHandler'),
    )

  @overload(QXmlLexicalHandler)
  @overload(NoneType)
  def setLexicalHandler(self, handler: Optional[QXmlLexicalHandler]) -> None:
    """
    Calls Qt's 'void QXmlReader::setLexicalHandler(QXmlLexicalHandler
    *handler)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlreader.html#setLexicalHandler

    Parameters
    ----------

    handler : Optional[QXmlLexicalHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QXmlReader::setLexicalHandler(QXmlLexicalHandler *handler)
    self.uglySide.call(
        'ritual_ZN10QXmlReader17setLexicalHandlerEP18QXmlLexicalHandler',
        self._addressOf(handler, 'QXmlLexicalHandler'),
    )

  @overload(QXmlDeclHandler)
  @overload(NoneType)
  def setDeclHandler(self, handler: Optional[QXmlDeclHandler]) -> None:
    """
    Calls Qt's 'void QXmlReader::setDeclHandler(QXmlDeclHandler *handler)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlreader.html#setDeclHandler

    Parameters
    ----------

    handler : Optional[QXmlDeclHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QXmlReader::setDeclHandler(QXmlDeclHandler *handler)
    self.uglySide.call(
        'ritual_ZN10QXmlReader14setDeclHandlerEP15QXmlDeclHandler',
        self._addressOf(handler, 'QXmlDeclHandler'),
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

  @overload(QXmlInputSource)
  def parse(self, input: QXmlInputSource) -> bool:
    """
    Calls Qt's 'bool QXmlReader::parse(const QXmlInputSource &input)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlreader.html#parse

    Parameters
    ----------

    input : QXmlInputSource
      Passed on as a value: Qt reads the C++ QXmlInputSource, which stays
      Python's own.
    """
    #  bool QXmlReader::parse(const QXmlInputSource &input)
    return self.uglySide.call(
        'ritual_ZN10QXmlReader5parseERK15QXmlInputSource',
        self._valueOf(input),
    )

  @overload(NoneType)
  def parse(self, input: Optional[QXmlInputSource]) -> bool:
    """
    Calls Qt's 'bool QXmlReader::parse(const QXmlInputSource *input)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlreader.html#parse

    Parameters
    ----------

    input : Optional[QXmlInputSource]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QXmlReader::parse(const QXmlInputSource *input)
    return self.uglySide.call(
        'ritual_ZN10QXmlReader5parseEPK15QXmlInputSource',
        self._addressOf(input),
    )

  @staticmethod
  def feature(*__, **_) -> Never:
    """
    Qt's 'bool QXmlReader::feature(const QString &name, bool *ok) const':
    takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QXmlReader.feature' has no cute function yet. Qt's 'bool "
        "QXmlReader::feature(const QString &name, bool *ok) const': takes a "
        "number to change where it is.")

  @staticmethod
  def property(*__, **_) -> Never:
    """
    Qt's 'void *QXmlReader::property(const QString &name, bool *ok) const':
    takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QXmlReader.property' has no cute function yet. Qt's 'void "
        "*QXmlReader::property(const QString &name, bool *ok) const': takes "
        "a number to change where it is.")

  @staticmethod
  def setProperty(*__, **_) -> Never:
    """
    Qt's 'void QXmlReader::setProperty(const QString &name, void *value)':
    names 'void', which has no cute class yet.
    """
    raise NotImplementedError(
        "'QXmlReader.setProperty' has no cute function yet. Qt's 'void "
        "QXmlReader::setProperty(const QString &name, void *value)': names "
        "'void', which has no cute class yet.")
