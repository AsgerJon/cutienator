"""
QXmlSimpleReader binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtCore5Compat/qxml.h, Qt 6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import WAIT
from ..occult import Rituals
from . import QXmlReader

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Optional

  from . import QXmlContentHandler, QXmlDTDHandler, QXmlDeclHandler
  from . import QXmlEntityResolver, QXmlErrorHandler, QXmlInputSource
  from . import QXmlLexicalHandler, QXmlSimpleReaderPrivate
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


class QXmlSimpleReader(QXmlReader):
  """
  The cute side of Qt's QXmlSimpleReader: a plain Python object standing in
  front of one C++ QXmlSimpleReader.

  It is built on the cute 'QXmlReader', as Qt's QXmlSimpleReader is built on
  Qt's QXmlReader, and has everything that class has.

  What exists
  -----------

  Every function of Qt's QXmlSimpleReader that has a ritual and that Python
  can call so far, 18 names in all: 'setFeature', 'hasFeature',
  'hasProperty', 'setEntityResolver', 'entityResolver', 'setDTDHandler',
  'DTDHandler', 'setContentHandler', 'contentHandler', 'setErrorHandler',
  'errorHandler', 'setLexicalHandler', 'lexicalHandler', 'setDeclHandler',
  'declHandler', 'parse', 'parseContinue', 'd_func'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QXmlSimpleReader::~QXmlSimpleReader()': the destructor: Python
    never removes a C++ QXmlSimpleReader.
  - Qt's 'bool QXmlSimpleReader::feature(const QString &name, bool *ok)
    const': takes a number to change where it is.
  - Qt's 'void *QXmlSimpleReader::property(const QString &name, bool *ok)
    const': takes a number to change where it is.
  - Qt's 'void QXmlSimpleReader::setProperty(const QString &name, void
    *value)': names 'void', which has no cute class yet.
  - Qt's 'const QXmlSimpleReaderPrivate *QXmlSimpleReader::d_func() const':
    takes in Python what 'QXmlSimpleReaderPrivate
    *QXmlSimpleReader::d_func()' takes.

  What has no ritual
  ------------------

  2 of the 28 functions Qt declares: 2 forbidden.

  What to expect
  --------------

  - The C++ QXmlSimpleReader is created at the first use, not by
    'QXmlSimpleReader(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QXmlSimpleReader.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QXmlSimpleReader'

  #  A C++ QXmlSimpleReader Python makes is of a C++ class of ours, in which
  #  Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QXmlSimpleReader'

  #  The functions Qt calls itself that QXmlSimpleReader is the first to
  #  declare. A class of a program built on it can write one anew, and Qt
  #  then calls that. For each name: the key C++ knows the function by, what
  #  it gives, and what it takes.
  __virtual_functions__ = {
      'parse': (
          ('_ZN16QXmlSimpleReader5parseEPK15QXmlInputSourceb',
           ('bool', 'number', ''),
           (
               ('address', 'address', 'QtCore5Compat:QXmlInputSource'),
               ('bool', 'number', ''),
           )),
      ),
      'parseContinue': (
          ('_ZN16QXmlSimpleReader13parseContinueEv',
           ('bool', 'number', ''),
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

  @overload(str)
  def hasFeature(self, name: str) -> bool:
    """
    Calls Qt's 'bool QXmlSimpleReader::hasFeature(const QString &name)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlsimplereader.html#hasFeature

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QXmlSimpleReader::hasFeature(const QString &name) const
    ritual = 'ritual_ZNK16QXmlSimpleReader10hasFeatureERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QXmlSimpleReader10hasFeatureERK7QString'
    return self.uglySide.call(ritual, name)

  @overload(str)
  def hasProperty(self, name: str) -> bool:
    """
    Calls Qt's 'bool QXmlSimpleReader::hasProperty(const QString &name)
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlsimplereader.html#hasProperty

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QXmlSimpleReader::hasProperty(const QString &name) const
    ritual = 'ritual_ZNK16QXmlSimpleReader11hasPropertyERK7QString'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QXmlSimpleReader11hasPropertyERK7QString'
    return self.uglySide.call(ritual, name)

  def entityResolver(self) -> Optional[QXmlEntityResolver]:
    """
    Calls Qt's 'QXmlEntityResolver *QXmlSimpleReader::entityResolver()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlsimplereader.html#entityResolver

    Returns
    -------

    Optional[QXmlEntityResolver]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QXmlEntityResolver *QXmlSimpleReader::entityResolver() const
    ritual = 'ritual_ZNK16QXmlSimpleReader14entityResolverEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QXmlSimpleReader14entityResolverEv'
    address = self.uglySide.call(ritual)
    from . import QXmlEntityResolver
    return QXmlEntityResolver._cuteAt(address)

  def DTDHandler(self) -> Optional[QXmlDTDHandler]:
    """
    Calls Qt's 'QXmlDTDHandler *QXmlSimpleReader::DTDHandler() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlsimplereader.html#DTDHandler

    Returns
    -------

    Optional[QXmlDTDHandler]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QXmlDTDHandler *QXmlSimpleReader::DTDHandler() const
    ritual = 'ritual_ZNK16QXmlSimpleReader10DTDHandlerEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QXmlSimpleReader10DTDHandlerEv'
    address = self.uglySide.call(ritual)
    from . import QXmlDTDHandler
    return QXmlDTDHandler._cuteAt(address)

  def contentHandler(self) -> Optional[QXmlContentHandler]:
    """
    Calls Qt's 'QXmlContentHandler *QXmlSimpleReader::contentHandler()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlsimplereader.html#contentHandler

    Returns
    -------

    Optional[QXmlContentHandler]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QXmlContentHandler *QXmlSimpleReader::contentHandler() const
    ritual = 'ritual_ZNK16QXmlSimpleReader14contentHandlerEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QXmlSimpleReader14contentHandlerEv'
    address = self.uglySide.call(ritual)
    from . import QXmlContentHandler
    return QXmlContentHandler._cuteAt(address)

  def errorHandler(self) -> Optional[QXmlErrorHandler]:
    """
    Calls Qt's 'QXmlErrorHandler *QXmlSimpleReader::errorHandler() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlsimplereader.html#errorHandler

    Returns
    -------

    Optional[QXmlErrorHandler]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QXmlErrorHandler *QXmlSimpleReader::errorHandler() const
    ritual = 'ritual_ZNK16QXmlSimpleReader12errorHandlerEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QXmlSimpleReader12errorHandlerEv'
    address = self.uglySide.call(ritual)
    from . import QXmlErrorHandler
    return QXmlErrorHandler._cuteAt(address)

  def lexicalHandler(self) -> Optional[QXmlLexicalHandler]:
    """
    Calls Qt's 'QXmlLexicalHandler *QXmlSimpleReader::lexicalHandler()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlsimplereader.html#lexicalHandler

    Returns
    -------

    Optional[QXmlLexicalHandler]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QXmlLexicalHandler *QXmlSimpleReader::lexicalHandler() const
    ritual = 'ritual_ZNK16QXmlSimpleReader14lexicalHandlerEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QXmlSimpleReader14lexicalHandlerEv'
    address = self.uglySide.call(ritual)
    from . import QXmlLexicalHandler
    return QXmlLexicalHandler._cuteAt(address)

  def declHandler(self) -> Optional[QXmlDeclHandler]:
    """
    Calls Qt's 'QXmlDeclHandler *QXmlSimpleReader::declHandler() const'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlsimplereader.html#declHandler

    Returns
    -------

    Optional[QXmlDeclHandler]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QXmlDeclHandler *QXmlSimpleReader::declHandler() const
    ritual = 'ritual_ZNK16QXmlSimpleReader11declHandlerEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK16QXmlSimpleReader11declHandlerEv'
    address = self.uglySide.call(ritual)
    from . import QXmlDeclHandler
    return QXmlDeclHandler._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str, bool)
  def setFeature(self, name: str, value: bool) -> None:
    """
    Calls Qt's 'void QXmlSimpleReader::setFeature(const QString &name, bool
    value)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlsimplereader.html#setFeature

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    value : bool
      Passed on as it is.
    """
    #  void QXmlSimpleReader::setFeature(const QString &name, bool value)
    ritual = 'ritual_ZN16QXmlSimpleReader10setFeatureERK7QStringb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QXmlSimpleReader10setFeatureERK7QStringb'
    self.uglySide.call(ritual, name, value)

  @overload(QXmlEntityResolver)
  @overload(NoneType)
  def setEntityResolver(self, handler: Optional[QXmlEntityResolver]) -> None:
    """
    Calls Qt's 'void QXmlSimpleReader::setEntityResolver(QXmlEntityResolver
    *handler)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlsimplereader.html#setEntityResolver

    Parameters
    ----------

    handler : Optional[QXmlEntityResolver]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QXmlSimpleReader::setEntityResolver(QXmlEntityResolver *handler)
    ritual = (
        'ritual_ZN16QXmlSimpleReader17setEntityResolverEP18QXmlEntityResolv'
        'er')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QXmlSimpleReader17setEntityResolverEP18QXmlEntity'
          'Resolver')
    self.uglySide.call(
        ritual, self._addressOf(handler, 'QXmlEntityResolver'),
    )

  @overload(QXmlDTDHandler)
  @overload(NoneType)
  def setDTDHandler(self, handler: Optional[QXmlDTDHandler]) -> None:
    """
    Calls Qt's 'void QXmlSimpleReader::setDTDHandler(QXmlDTDHandler
    *handler)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlsimplereader.html#setDTDHandler

    Parameters
    ----------

    handler : Optional[QXmlDTDHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QXmlSimpleReader::setDTDHandler(QXmlDTDHandler *handler)
    ritual = 'ritual_ZN16QXmlSimpleReader13setDTDHandlerEP14QXmlDTDHandler'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QXmlSimpleReader13setDTDHandlerEP14QXmlDTDHandler')
    self.uglySide.call(ritual, self._addressOf(handler, 'QXmlDTDHandler'))

  @overload(QXmlContentHandler)
  @overload(NoneType)
  def setContentHandler(self, handler: Optional[QXmlContentHandler]) -> None:
    """
    Calls Qt's 'void QXmlSimpleReader::setContentHandler(QXmlContentHandler
    *handler)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlsimplereader.html#setContentHandler

    Parameters
    ----------

    handler : Optional[QXmlContentHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QXmlSimpleReader::setContentHandler(QXmlContentHandler *handler)
    ritual = (
        'ritual_ZN16QXmlSimpleReader17setContentHandlerEP18QXmlContentHandl'
        'er')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QXmlSimpleReader17setContentHandlerEP18QXmlConten'
          'tHandler')
    self.uglySide.call(ritual, self._addressOf(handler))

  @overload(QXmlErrorHandler)
  @overload(NoneType)
  def setErrorHandler(self, handler: Optional[QXmlErrorHandler]) -> None:
    """
    Calls Qt's 'void QXmlSimpleReader::setErrorHandler(QXmlErrorHandler
    *handler)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlsimplereader.html#setErrorHandler

    Parameters
    ----------

    handler : Optional[QXmlErrorHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QXmlSimpleReader::setErrorHandler(QXmlErrorHandler *handler)
    ritual = (
        'ritual_ZN16QXmlSimpleReader15setErrorHandlerEP16QXmlErrorHandler')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QXmlSimpleReader15setErrorHandlerEP16QXmlErrorHan'
          'dler')
    self.uglySide.call(ritual, self._addressOf(handler, 'QXmlErrorHandler'))

  @overload(QXmlLexicalHandler)
  @overload(NoneType)
  def setLexicalHandler(self, handler: Optional[QXmlLexicalHandler]) -> None:
    """
    Calls Qt's 'void QXmlSimpleReader::setLexicalHandler(QXmlLexicalHandler
    *handler)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlsimplereader.html#setLexicalHandler

    Parameters
    ----------

    handler : Optional[QXmlLexicalHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QXmlSimpleReader::setLexicalHandler(QXmlLexicalHandler *handler)
    ritual = (
        'ritual_ZN16QXmlSimpleReader17setLexicalHandlerEP18QXmlLexicalHandl'
        'er')
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QXmlSimpleReader17setLexicalHandlerEP18QXmlLexica'
          'lHandler')
    self.uglySide.call(
        ritual, self._addressOf(handler, 'QXmlLexicalHandler'),
    )

  @overload(QXmlDeclHandler)
  @overload(NoneType)
  def setDeclHandler(self, handler: Optional[QXmlDeclHandler]) -> None:
    """
    Calls Qt's 'void QXmlSimpleReader::setDeclHandler(QXmlDeclHandler
    *handler)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlsimplereader.html#setDeclHandler

    Parameters
    ----------

    handler : Optional[QXmlDeclHandler]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QXmlSimpleReader::setDeclHandler(QXmlDeclHandler *handler)
    ritual = 'ritual_ZN16QXmlSimpleReader14setDeclHandlerEP15QXmlDeclHandler'
    if self.uglySide.isOurs():
      ritual = (
          'ritual_own_ZN16QXmlSimpleReader14setDeclHandlerEP15QXmlDeclHandl'
          'er')
    self.uglySide.call(ritual, self._addressOf(handler, 'QXmlDeclHandler'))

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
    Notes what was given, for Qt's 'QXmlSimpleReader::QXmlSimpleReader()',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlsimplereader.html#QXmlSimpleReader
    """
    #  QXmlSimpleReader::QXmlSimpleReader()
    self._noteCreation(QXmlSimpleReader, lambda: Rituals.call(
        'ritual_ZN16QXmlSimpleReaderC1Ev',
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

  @overload(QXmlInputSource)
  def parse(self, input: QXmlInputSource) -> bool:
    """
    Calls Qt's 'bool QXmlSimpleReader::parse(const QXmlInputSource &input)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlsimplereader.html#parse

    Parameters
    ----------

    input : QXmlInputSource
      Passed on as a value: Qt reads the C++ QXmlInputSource, which stays
      Python's own.
    """
    #  bool QXmlSimpleReader::parse(const QXmlInputSource &input)
    ritual = 'ritual_ZN16QXmlSimpleReader5parseERK15QXmlInputSource'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QXmlSimpleReader5parseERK15QXmlInputSource'
    return self.uglySide.call(ritual, self._valueOf(input))

  @overload(NoneType)
  def parse(self, input: Optional[QXmlInputSource]) -> bool:
    """
    Calls Qt's 'bool QXmlSimpleReader::parse(const QXmlInputSource *input)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlsimplereader.html#parse

    Parameters
    ----------

    input : Optional[QXmlInputSource]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QXmlSimpleReader::parse(const QXmlInputSource *input)
    ritual = 'ritual_ZN16QXmlSimpleReader5parseEPK15QXmlInputSource'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QXmlSimpleReader5parseEPK15QXmlInputSource'
    return self.uglySide.call(ritual, self._addressOf(input))

  @overload(QXmlInputSource, bool)
  @overload(NoneType, bool)
  def parse(
      self,
      input: Optional[QXmlInputSource],
      incremental: bool,
  ) -> bool:
    """
    Calls Qt's 'bool QXmlSimpleReader::parse(const QXmlInputSource *input,
    bool incremental)'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlsimplereader.html#parse

    Parameters
    ----------

    input : Optional[QXmlInputSource]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    incremental : bool
      Passed on as it is.
    """
    #  bool QXmlSimpleReader::parse(const QXmlInputSource *input, bool
    #      incremental)
    ritual = 'ritual_ZN16QXmlSimpleReader5parseEPK15QXmlInputSourceb'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QXmlSimpleReader5parseEPK15QXmlInputSourceb'
    return self.uglySide.call(ritual, self._addressOf(input), incremental)

  def parseContinue(self) -> bool:
    """
    Calls Qt's 'bool QXmlSimpleReader::parseContinue()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qxmlsimplereader.html#parseContinue
    """
    #  bool QXmlSimpleReader::parseContinue()
    ritual = 'ritual_ZN16QXmlSimpleReader13parseContinueEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN16QXmlSimpleReader13parseContinueEv'
    return self.uglySide.call(ritual)

  def d_func(self) -> Optional[QXmlSimpleReaderPrivate]:
    """
    Calls Qt's 'QXmlSimpleReaderPrivate *QXmlSimpleReader::d_func()'.

    Qt's own words: https://doc.qt.io/qt-6/qxmlsimplereader.html#d_func

    Returns
    -------

    Optional[QXmlSimpleReaderPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QXmlSimpleReaderPrivate *QXmlSimpleReader::d_func()
    address = self.uglySide.call('ritual_ZN16QXmlSimpleReader6d_funcEv')
    from . import QXmlSimpleReaderPrivate
    return QXmlSimpleReaderPrivate._cuteAt(address)
