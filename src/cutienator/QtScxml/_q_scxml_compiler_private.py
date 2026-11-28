"""
QScxmlCompilerPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtScxml/6.12.0/QtScxml/private/qscxmlcompiler_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QScxmlCompilerPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute, WAIT
from ..occult import Rituals
from ..QtCore import QList, QStringList
from . import DocumentModel, QScxmlCompiler

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from ..QtCore import QString, QXmlStreamAttributes, QXmlStreamReader
  from . import QScxmlError, QScxmlStateMachine
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QScxmlStateMachine = WAIT['QScxmlStateMachine']
  QString = WAIT['QString']
  QXmlStreamAttributes = WAIT['QXmlStreamAttributes']
  QXmlStreamReader = WAIT['QXmlStreamReader']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QScxmlCompilerPrivate(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QScxmlCompilerPrivate: a plain Python object standing
  in front of one C++ QScxmlCompilerPrivate.

  What exists
  -----------

  Every function of Qt's QScxmlCompilerPrivate that has a ritual and that
  Python can call so far, 76 names in all: 'get', 'verifyDocument',
  'scxmlDocument', 'fileName', 'setFileName', 'loader', 'setLoader',
  'readDocument', 'parseSubDocument', 'parseSubElement', 'errors',
  'addError', 'instantiateStateMachine', 'instantiateDataModel',
  'currentParent', 'xmlLocation', 'maybeId', 'lastIf', 'checkAttributes',
  'preReadElementScxml', 'preReadElementState', 'preReadElementParallel',
  'preReadElementInitial', 'preReadElementTransition', 'preReadElementFinal',
  'preReadElementHistory', 'preReadElementOnEntry', 'preReadElementOnExit',
  'preReadElementRaise', 'preReadElementIf', 'preReadElementElseIf',
  'preReadElementElse', 'preReadElementForeach', 'preReadElementLog',
  'preReadElementDataModel', 'preReadElementData', 'preReadElementAssign',
  'preReadElementDoneData', 'preReadElementContent', 'preReadElementParam',
  'preReadElementScript', 'preReadElementSend', 'preReadElementCancel',
  'preReadElementInvoke', 'preReadElementFinalize', 'postReadElementScxml',
  'postReadElementState', 'postReadElementParallel',
  'postReadElementInitial', 'postReadElementTransition',
  'postReadElementFinal', 'postReadElementHistory', 'postReadElementOnEntry',
  'postReadElementOnExit', 'postReadElementRaise', 'postReadElementIf',
  'postReadElementElseIf', 'postReadElementElse', 'postReadElementForeach',
  'postReadElementLog', 'postReadElementDataModel', 'postReadElementData',
  'postReadElementAssign', 'postReadElementDoneData',
  'postReadElementContent', 'postReadElementParam', 'postReadElementScript',
  'postReadElementSend', 'postReadElementCancel', 'postReadElementInvoke',
  'postReadElementFinalize', 'readElement', 'resetDocument',
  'currentStateUp', 'flushInstruction', 'hasPrevious'. It can be made from
  Python, in 1 way; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QByteArray QScxmlCompilerPrivate::load(const QString &name, bool
    *ok)': takes a number to change where it is.
  - Qt's 'bool QScxmlCompilerPrivate::checkAttributes(const
    QXmlStreamAttributes &attributes,
    QScxmlCompilerPrivate::ParserState::Kind kind)': names the enum
    'QScxmlCompilerPrivate::ParserState::Kind', whose class cannot be named
    here.
  - Qt's 'ParserState &QScxmlCompilerPrivate::current()': gives a type Python
    has no way to take yet.
  - Qt's 'ParserState &QScxmlCompilerPrivate::previous()': gives a type
    Python has no way to take yet.

  What to expect
  --------------

  - The C++ QScxmlCompilerPrivate is created at the first use, not by
    'QScxmlCompilerPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QScxmlCompilerPrivate.
  - Each name of Qt's QScxmlCompilerPrivate that has no cute function yet,
    'current', 'load', 'previous', holds a function that raises
    'NotImplementedError', and its docstring says why.
  """

  #  The classes Qt writes inside QScxmlCompilerPrivate, each a class in here
  #  as in C++.

  class DefaultLoader(CuteMixin, metaclass=MetaCute):
    """
    The cute side of Qt's QScxmlCompilerPrivate::DefaultLoader: a plain
    Python object standing in front of one C++
    QScxmlCompilerPrivate::DefaultLoader.

    C++ hands a QScxmlCompilerPrivate::DefaultLoader around as a copy, so
    every C++ QScxmlCompilerPrivate::DefaultLoader behind a cute one is
    Python's own: it is removed, by the ritual named in '__delete_ritual__',
    when the cute object goes.

    What exists
    -----------

    No function of Qt's QScxmlCompilerPrivate::DefaultLoader yet. It can be
    made from Python, in 1 way; see '__init__'.

    What has a ritual and is left out, and why
    ------------------------------------------

    - Qt's 'QByteArray QScxmlCompilerPrivate::DefaultLoader::load(const
      QString &name, const QString &baseDir, QStringList *errors)': names
      'QStringList', which has no cute class yet.
    - Qt's 'QScxmlCompilerPrivate::DefaultLoader::~DefaultLoader()': the
      destructor: Python removes its C++ QScxmlCompilerPrivate::DefaultLoader
      by it, and has no other use for it.

    What to expect
    --------------

    - The C++ QScxmlCompilerPrivate::DefaultLoader is created at the first
      use, not by 'QScxmlCompilerPrivate::DefaultLoader(...)'.
    - A wrong argument is refused in Python, with 'DispatchException', and
      never reaches C++.
    - None is taken wherever Qt takes an object by its address, or text as C
      has it, and is passed on as nothing. Whether Qt can do with nothing
      there is as in C++.
    - A function giving a QScxmlCompilerPrivate::DefaultLoader back gives a
      copy the ritual made for Python, in a new cute
      QScxmlCompilerPrivate::DefaultLoader.
    """

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

    #  Class Variables
    #  The class of Qt this class stands for.
    __qt_class__ = 'QScxmlCompilerPrivate::DefaultLoader'

    #  Qt's '~QScxmlCompilerPrivate::DefaultLoader()'. Naming it makes this a
    #  value class: Python owns every C++
    #  QScxmlCompilerPrivate::DefaultLoader behind a cute one, and removes it
    #  by this ritual.
    __delete_ritual__ = 'ritual_ZN21QScxmlCompilerPrivate13DefaultLoaderD1Ev'

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
      'QScxmlCompilerPrivate::DefaultLoader::DefaultLoader()', which is
      called at the first use.

      Qt's own words:
      https://doc.qt.io/qt-6/qscxmlcompilerprivate-defaultloader.html
      """
      #  QScxmlCompilerPrivate::DefaultLoader::DefaultLoader()
      self._noteCreation(
          QScxmlCompilerPrivate.DefaultLoader, lambda: Rituals.call(
              'ritual_ZN21QScxmlCompilerPrivate13DefaultLoaderC1Ev',
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
  @overload(QScxmlCompiler)
  @overload(NoneType)
  def get(
      compiler: Optional[QScxmlCompiler],
  ) -> Optional[QScxmlCompilerPrivate]:
    """
    Calls Qt's 'QScxmlCompilerPrivate
    *QScxmlCompilerPrivate::get(QScxmlCompiler *compiler)'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#get

    Parameters
    ----------

    compiler : Optional[QScxmlCompiler]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    Returns
    -------

    Optional[QScxmlCompilerPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScxmlCompilerPrivate *QScxmlCompilerPrivate::get(QScxmlCompiler
    #      *compiler)
    address = Rituals.call(
        'ritual_ZN21QScxmlCompilerPrivate3getEP14QScxmlCompiler',
        CuteMixin._addressOf(compiler),
    )
    return QScxmlCompilerPrivate._cuteAt(address)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QScxmlCompilerPrivate'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def scxmlDocument(self) -> Optional[DocumentModel.ScxmlDocument]:
    """
    Calls Qt's 'DocumentModel::ScxmlDocument
    *QScxmlCompilerPrivate::scxmlDocument() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#scxmlDocument

    Returns
    -------

    Optional[DocumentModel.ScxmlDocument]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DocumentModel::ScxmlDocument *QScxmlCompilerPrivate::scxmlDocument()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK21QScxmlCompilerPrivate13scxmlDocumentEv',
    )
    return DocumentModel.ScxmlDocument._cuteAt(address)

  def fileName(self) -> str:
    """
    Calls Qt's 'QString QScxmlCompilerPrivate::fileName() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#fileName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QScxmlCompilerPrivate::fileName() const
    return self.uglySide.call('ritual_ZNK21QScxmlCompilerPrivate8fileNameEv')

  def loader(self) -> Optional[QScxmlCompiler.Loader]:
    """
    Calls Qt's 'QScxmlCompiler::Loader *QScxmlCompilerPrivate::loader()
    const'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#loader

    Returns
    -------

    Optional[QScxmlCompiler.Loader]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScxmlCompiler::Loader *QScxmlCompilerPrivate::loader() const
    address = self.uglySide.call(
        'ritual_ZNK21QScxmlCompilerPrivate6loaderEv',
    )
    return QScxmlCompiler.Loader._cuteAt(address)

  def errors(self) -> QList[QScxmlError]:
    """
    Calls Qt's 'QList<QScxmlError> QScxmlCompilerPrivate::errors() const'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#errors

    Returns
    -------

    QList[QScxmlError]
      A new cute list around the copy Qt gave back. Python owns it.
    """
    #  QList<QScxmlError> QScxmlCompilerPrivate::errors() const
    address = self.uglySide.call(
        'ritual_ZNK21QScxmlCompilerPrivate6errorsEv',
    )
    from . import QScxmlError
    return QList[QScxmlError]._cuteOwning(address)

  def instantiateStateMachine(self) -> Optional[QScxmlStateMachine]:
    """
    Calls Qt's 'QScxmlStateMachine
    *QScxmlCompilerPrivate::instantiateStateMachine() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#instantiateStateMachine

    Returns
    -------

    Optional[QScxmlStateMachine]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QScxmlStateMachine *QScxmlCompilerPrivate::instantiateStateMachine()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK21QScxmlCompilerPrivate23instantiateStateMachineEv',
    )
    from . import QScxmlStateMachine
    return QScxmlStateMachine._cuteAt(address)

  def currentParent(self) -> Optional[DocumentModel.AbstractState]:
    """
    Calls Qt's 'DocumentModel::AbstractState
    *QScxmlCompilerPrivate::currentParent() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#currentParent

    Returns
    -------

    Optional[DocumentModel.AbstractState]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DocumentModel::AbstractState *QScxmlCompilerPrivate::currentParent()
    #      const
    address = self.uglySide.call(
        'ritual_ZNK21QScxmlCompilerPrivate13currentParentEv',
    )
    return DocumentModel.AbstractState._cuteAt(address)

  def xmlLocation(self) -> DocumentModel.XmlLocation:
    """
    Calls Qt's 'DocumentModel::XmlLocation
    QScxmlCompilerPrivate::xmlLocation() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#xmlLocation

    Returns
    -------

    DocumentModel.XmlLocation
      A new cute DocumentModel::XmlLocation around the copy Qt gave back.
      Python owns it.
    """
    #  DocumentModel::XmlLocation QScxmlCompilerPrivate::xmlLocation() const
    address = self.uglySide.call(
        'ritual_ZNK21QScxmlCompilerPrivate11xmlLocationEv',
    )
    return DocumentModel.XmlLocation._cuteOwning(address)

  def hasPrevious(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::hasPrevious() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#hasPrevious
    """
    #  bool QScxmlCompilerPrivate::hasPrevious() const
    return self.uglySide.call(
        'ritual_ZNK21QScxmlCompilerPrivate11hasPreviousEv',
    )

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setFileName(self, fileName: str) -> None:
    """
    Calls Qt's 'void QScxmlCompilerPrivate::setFileName(const QString
    &fileName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#setFileName

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QScxmlCompilerPrivate::setFileName(const QString &fileName)
    self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate11setFileNameERK7QString', fileName,
    )

  @overload(QScxmlCompiler.Loader)
  @overload(NoneType)
  def setLoader(self, loader: Optional[QScxmlCompiler.Loader]) -> None:
    """
    Calls Qt's 'void QScxmlCompilerPrivate::setLoader(QScxmlCompiler::Loader
    *loader)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#setLoader

    Parameters
    ----------

    loader : Optional[QScxmlCompiler.Loader]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScxmlCompilerPrivate::setLoader(QScxmlCompiler::Loader *loader)
    self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate9setLoaderEPN14QScxmlCompiler6Load'
        'erE',
        self._addressOf(loader),
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

  @overload(QXmlStreamReader)
  @overload(NoneType)
  def __init__(self, reader: Optional[QXmlStreamReader]) -> None:
    """
    Notes what was given, for Qt's
    'QScxmlCompilerPrivate::QScxmlCompilerPrivate(QXmlStreamReader *reader)',
    which is called at the first use.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#QScxmlCompilerPrivate

    Parameters
    ----------

    reader : Optional[QXmlStreamReader]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QScxmlCompilerPrivate::QScxmlCompilerPrivate(QXmlStreamReader *reader)
    self._noteCreation(QScxmlCompilerPrivate, lambda: Rituals.call(
        'ritual_ZN21QScxmlCompilerPrivateC1EP16QXmlStreamReader',
        self._addressOf(reader),
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

  def verifyDocument(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::verifyDocument()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#verifyDocument
    """
    #  bool QScxmlCompilerPrivate::verifyDocument()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate14verifyDocumentEv',
    )

  def readDocument(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::readDocument()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#readDocument
    """
    #  bool QScxmlCompilerPrivate::readDocument()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate12readDocumentEv',
    )

  @overload(WAIT['DocumentModel.Invoke'], QXmlStreamReader, str)
  @overload(WAIT['DocumentModel.Invoke'], NoneType, str)
  @overload(NoneType, QXmlStreamReader, str)
  @overload(NoneType, NoneType, str)
  def parseSubDocument(
      self,
      parentInvoke: Optional[DocumentModel.Invoke],
      reader: Optional[QXmlStreamReader],
      fileName: str,
  ) -> None:
    """
    Calls Qt's 'void
    QScxmlCompilerPrivate::parseSubDocument(DocumentModel::Invoke
    *parentInvoke, QXmlStreamReader *reader, const QString &fileName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#parseSubDocument

    Parameters
    ----------

    parentInvoke : Optional[DocumentModel.Invoke]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    reader : Optional[QXmlStreamReader]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    fileName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QScxmlCompilerPrivate::parseSubDocument(DocumentModel::Invoke
    #      *parentInvoke, QXmlStreamReader *reader, const QString &fileName)
    self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate16parseSubDocumentEPN13DocumentMod'
        'el6InvokeEP16QXmlStreamReaderRK7QString',
        self._addressOf(parentInvoke), self._addressOf(reader), fileName,
    )

  @overload(WAIT['DocumentModel.Invoke'], QXmlStreamReader, str)
  @overload(WAIT['DocumentModel.Invoke'], NoneType, str)
  @overload(NoneType, QXmlStreamReader, str)
  @overload(NoneType, NoneType, str)
  def parseSubElement(
      self,
      parentInvoke: Optional[DocumentModel.Invoke],
      reader: Optional[QXmlStreamReader],
      fileName: str,
  ) -> bool:
    """
    Calls Qt's 'bool
    QScxmlCompilerPrivate::parseSubElement(DocumentModel::Invoke
    *parentInvoke, QXmlStreamReader *reader, const QString &fileName)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#parseSubElement

    Parameters
    ----------

    parentInvoke : Optional[DocumentModel.Invoke]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    reader : Optional[QXmlStreamReader]
      Passed on as the address of its C++ object. None is passed on as no
      object.

    fileName : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QScxmlCompilerPrivate::parseSubElement(DocumentModel::Invoke
    #      *parentInvoke, QXmlStreamReader *reader, const QString &fileName)
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate15parseSubElementEPN13DocumentMode'
        'l6InvokeEP16QXmlStreamReaderRK7QString',
        self._addressOf(parentInvoke), self._addressOf(reader), fileName,
    )

  @overload(str)
  def addError(self, msg: str) -> None:
    """
    Calls Qt's 'void QScxmlCompilerPrivate::addError(const QString &msg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#addError

    Parameters
    ----------

    msg : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QScxmlCompilerPrivate::addError(const QString &msg)
    self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate8addErrorERK7QString', msg,
    )

  @overload(str, WAIT['DocumentModel.XmlLocation'], str)
  def addError(
      self,
      fileName: str,
      location: DocumentModel.XmlLocation,
      msg: str,
  ) -> None:
    """
    Calls Qt's 'void QScxmlCompilerPrivate::addError(const QString &fileName,
    const DocumentModel::XmlLocation &location, const QString &msg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#addError

    Parameters
    ----------

    fileName : str
      Passed on as it is: a QString is made of it for the call.

    location : DocumentModel.XmlLocation
      Passed on as a value: Qt reads the C++ DocumentModel::XmlLocation,
      which stays Python's own.

    msg : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QScxmlCompilerPrivate::addError(const QString &fileName, const
    #      DocumentModel::XmlLocation &location, const QString &msg)
    self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate8addErrorERK7QStringRKN13DocumentM'
        'odel11XmlLocationES2_',
        fileName, self._valueOf(location), msg,
    )

  @overload(QScxmlStateMachine)
  @overload(NoneType)
  def instantiateDataModel(
      self,
      stateMachine: Optional[QScxmlStateMachine],
  ) -> None:
    """
    Calls Qt's 'void
    QScxmlCompilerPrivate::instantiateDataModel(QScxmlStateMachine
    *stateMachine) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#instantiateDataModel

    Parameters
    ----------

    stateMachine : Optional[QScxmlStateMachine]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  void QScxmlCompilerPrivate::instantiateDataModel(QScxmlStateMachine
    #      *stateMachine) const
    self.uglySide.call(
        'ritual_ZNK21QScxmlCompilerPrivate20instantiateDataModelEP18QScxmlS'
        'tateMachine',
        self._addressOf(stateMachine),
    )

  @overload(QXmlStreamAttributes, QString)
  @overload(QXmlStreamAttributes, NoneType)
  def maybeId(
      self,
      attributes: QXmlStreamAttributes,
      id: Optional[QString],
  ) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::maybeId(const
    QXmlStreamAttributes &attributes, QString *id)'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#maybeId

    Parameters
    ----------

    attributes : QXmlStreamAttributes
      Passed on as a value: Qt reads the C++ QXmlStreamAttributes, which
      stays Python's own.

    id : Optional[QString]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  bool QScxmlCompilerPrivate::maybeId(const QXmlStreamAttributes
    #      &attributes, QString *id)
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate7maybeIdERK20QXmlStreamAttributesP'
        '7QString',
        self._valueOf(attributes), self._addressOf(id),
    )

  def lastIf(self) -> Optional[DocumentModel.If]:
    """
    Calls Qt's 'DocumentModel::If *QScxmlCompilerPrivate::lastIf()'.

    Qt's own words: https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#lastIf

    Returns
    -------

    Optional[DocumentModel.If]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  DocumentModel::If *QScxmlCompilerPrivate::lastIf()
    address = self.uglySide.call('ritual_ZN21QScxmlCompilerPrivate6lastIfEv')
    return DocumentModel.If._cuteAt(address)

  @overload(QXmlStreamAttributes, QStringList, QStringList)
  def checkAttributes(
      self,
      attributes: QXmlStreamAttributes,
      requiredNames: QStringList,
      optionalNames: QStringList,
  ) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::checkAttributes(const
    QXmlStreamAttributes &attributes, const QStringList &requiredNames, const
    QStringList &optionalNames)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#checkAttributes

    Parameters
    ----------

    attributes : QXmlStreamAttributes
      Passed on as a value: Qt reads the C++ QXmlStreamAttributes, which
      stays Python's own.

    requiredNames : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.

    optionalNames : QStringList
      Passed on as a list of Qt: Qt reads the C++ list, which stays Python's
      own. A list or tuple of Python is made into one first, and refused when
      an element does not fit.
    """
    #  bool QScxmlCompilerPrivate::checkAttributes(const QXmlStreamAttributes
    #      &attributes, const QStringList &requiredNames, const QStringList
    #      &optionalNames)
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate15checkAttributesERK20QXmlStreamAt'
        'tributesRK5QListI7QStringES7_',
        self._valueOf(attributes), self._valueOf(requiredNames),
        self._valueOf(optionalNames),
    )

  def preReadElementScxml(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::preReadElementScxml()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#preReadElementScxml
    """
    #  bool QScxmlCompilerPrivate::preReadElementScxml()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate19preReadElementScxmlEv',
    )

  def preReadElementState(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::preReadElementState()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#preReadElementState
    """
    #  bool QScxmlCompilerPrivate::preReadElementState()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate19preReadElementStateEv',
    )

  def preReadElementParallel(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::preReadElementParallel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#preReadElementParallel
    """
    #  bool QScxmlCompilerPrivate::preReadElementParallel()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate22preReadElementParallelEv',
    )

  def preReadElementInitial(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::preReadElementInitial()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#preReadElementInitial
    """
    #  bool QScxmlCompilerPrivate::preReadElementInitial()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate21preReadElementInitialEv',
    )

  def preReadElementTransition(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::preReadElementTransition()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html
    """
    #  bool QScxmlCompilerPrivate::preReadElementTransition()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate24preReadElementTransitionEv',
    )

  def preReadElementFinal(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::preReadElementFinal()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#preReadElementFinal
    """
    #  bool QScxmlCompilerPrivate::preReadElementFinal()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate19preReadElementFinalEv',
    )

  def preReadElementHistory(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::preReadElementHistory()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#preReadElementHistory
    """
    #  bool QScxmlCompilerPrivate::preReadElementHistory()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate21preReadElementHistoryEv',
    )

  def preReadElementOnEntry(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::preReadElementOnEntry()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#preReadElementOnEntry
    """
    #  bool QScxmlCompilerPrivate::preReadElementOnEntry()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate21preReadElementOnEntryEv',
    )

  def preReadElementOnExit(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::preReadElementOnExit()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#preReadElementOnExit
    """
    #  bool QScxmlCompilerPrivate::preReadElementOnExit()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate20preReadElementOnExitEv',
    )

  def preReadElementRaise(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::preReadElementRaise()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#preReadElementRaise
    """
    #  bool QScxmlCompilerPrivate::preReadElementRaise()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate19preReadElementRaiseEv',
    )

  def preReadElementIf(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::preReadElementIf()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#preReadElementIf
    """
    #  bool QScxmlCompilerPrivate::preReadElementIf()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate16preReadElementIfEv',
    )

  def preReadElementElseIf(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::preReadElementElseIf()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#preReadElementElseIf
    """
    #  bool QScxmlCompilerPrivate::preReadElementElseIf()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate20preReadElementElseIfEv',
    )

  def preReadElementElse(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::preReadElementElse()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#preReadElementElse
    """
    #  bool QScxmlCompilerPrivate::preReadElementElse()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate18preReadElementElseEv',
    )

  def preReadElementForeach(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::preReadElementForeach()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#preReadElementForeach
    """
    #  bool QScxmlCompilerPrivate::preReadElementForeach()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate21preReadElementForeachEv',
    )

  def preReadElementLog(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::preReadElementLog()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#preReadElementLog
    """
    #  bool QScxmlCompilerPrivate::preReadElementLog()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate17preReadElementLogEv',
    )

  def preReadElementDataModel(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::preReadElementDataModel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#preReadElementDataModel
    """
    #  bool QScxmlCompilerPrivate::preReadElementDataModel()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate23preReadElementDataModelEv',
    )

  def preReadElementData(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::preReadElementData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#preReadElementData
    """
    #  bool QScxmlCompilerPrivate::preReadElementData()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate18preReadElementDataEv',
    )

  def preReadElementAssign(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::preReadElementAssign()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#preReadElementAssign
    """
    #  bool QScxmlCompilerPrivate::preReadElementAssign()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate20preReadElementAssignEv',
    )

  def preReadElementDoneData(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::preReadElementDoneData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#preReadElementDoneData
    """
    #  bool QScxmlCompilerPrivate::preReadElementDoneData()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate22preReadElementDoneDataEv',
    )

  def preReadElementContent(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::preReadElementContent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#preReadElementContent
    """
    #  bool QScxmlCompilerPrivate::preReadElementContent()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate21preReadElementContentEv',
    )

  def preReadElementParam(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::preReadElementParam()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#preReadElementParam
    """
    #  bool QScxmlCompilerPrivate::preReadElementParam()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate19preReadElementParamEv',
    )

  def preReadElementScript(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::preReadElementScript()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#preReadElementScript
    """
    #  bool QScxmlCompilerPrivate::preReadElementScript()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate20preReadElementScriptEv',
    )

  def preReadElementSend(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::preReadElementSend()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#preReadElementSend
    """
    #  bool QScxmlCompilerPrivate::preReadElementSend()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate18preReadElementSendEv',
    )

  def preReadElementCancel(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::preReadElementCancel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#preReadElementCancel
    """
    #  bool QScxmlCompilerPrivate::preReadElementCancel()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate20preReadElementCancelEv',
    )

  def preReadElementInvoke(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::preReadElementInvoke()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#preReadElementInvoke
    """
    #  bool QScxmlCompilerPrivate::preReadElementInvoke()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate20preReadElementInvokeEv',
    )

  def preReadElementFinalize(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::preReadElementFinalize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#preReadElementFinalize
    """
    #  bool QScxmlCompilerPrivate::preReadElementFinalize()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate22preReadElementFinalizeEv',
    )

  def postReadElementScxml(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::postReadElementScxml()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#postReadElementScxml
    """
    #  bool QScxmlCompilerPrivate::postReadElementScxml()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate20postReadElementScxmlEv',
    )

  def postReadElementState(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::postReadElementState()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#postReadElementState
    """
    #  bool QScxmlCompilerPrivate::postReadElementState()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate20postReadElementStateEv',
    )

  def postReadElementParallel(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::postReadElementParallel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#postReadElementParallel
    """
    #  bool QScxmlCompilerPrivate::postReadElementParallel()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate23postReadElementParallelEv',
    )

  def postReadElementInitial(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::postReadElementInitial()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#postReadElementInitial
    """
    #  bool QScxmlCompilerPrivate::postReadElementInitial()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate22postReadElementInitialEv',
    )

  def postReadElementTransition(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::postReadElementTransition()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html
    """
    #  bool QScxmlCompilerPrivate::postReadElementTransition()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate25postReadElementTransitionEv',
    )

  def postReadElementFinal(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::postReadElementFinal()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#postReadElementFinal
    """
    #  bool QScxmlCompilerPrivate::postReadElementFinal()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate20postReadElementFinalEv',
    )

  def postReadElementHistory(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::postReadElementHistory()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#postReadElementHistory
    """
    #  bool QScxmlCompilerPrivate::postReadElementHistory()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate22postReadElementHistoryEv',
    )

  def postReadElementOnEntry(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::postReadElementOnEntry()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#postReadElementOnEntry
    """
    #  bool QScxmlCompilerPrivate::postReadElementOnEntry()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate22postReadElementOnEntryEv',
    )

  def postReadElementOnExit(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::postReadElementOnExit()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#postReadElementOnExit
    """
    #  bool QScxmlCompilerPrivate::postReadElementOnExit()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate21postReadElementOnExitEv',
    )

  def postReadElementRaise(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::postReadElementRaise()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#postReadElementRaise
    """
    #  bool QScxmlCompilerPrivate::postReadElementRaise()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate20postReadElementRaiseEv',
    )

  def postReadElementIf(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::postReadElementIf()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#postReadElementIf
    """
    #  bool QScxmlCompilerPrivate::postReadElementIf()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate17postReadElementIfEv',
    )

  def postReadElementElseIf(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::postReadElementElseIf()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#postReadElementElseIf
    """
    #  bool QScxmlCompilerPrivate::postReadElementElseIf()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate21postReadElementElseIfEv',
    )

  def postReadElementElse(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::postReadElementElse()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#postReadElementElse
    """
    #  bool QScxmlCompilerPrivate::postReadElementElse()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate19postReadElementElseEv',
    )

  def postReadElementForeach(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::postReadElementForeach()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#postReadElementForeach
    """
    #  bool QScxmlCompilerPrivate::postReadElementForeach()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate22postReadElementForeachEv',
    )

  def postReadElementLog(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::postReadElementLog()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#postReadElementLog
    """
    #  bool QScxmlCompilerPrivate::postReadElementLog()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate18postReadElementLogEv',
    )

  def postReadElementDataModel(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::postReadElementDataModel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html
    """
    #  bool QScxmlCompilerPrivate::postReadElementDataModel()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate24postReadElementDataModelEv',
    )

  def postReadElementData(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::postReadElementData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#postReadElementData
    """
    #  bool QScxmlCompilerPrivate::postReadElementData()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate19postReadElementDataEv',
    )

  def postReadElementAssign(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::postReadElementAssign()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#postReadElementAssign
    """
    #  bool QScxmlCompilerPrivate::postReadElementAssign()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate21postReadElementAssignEv',
    )

  def postReadElementDoneData(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::postReadElementDoneData()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#postReadElementDoneData
    """
    #  bool QScxmlCompilerPrivate::postReadElementDoneData()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate23postReadElementDoneDataEv',
    )

  def postReadElementContent(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::postReadElementContent()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#postReadElementContent
    """
    #  bool QScxmlCompilerPrivate::postReadElementContent()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate22postReadElementContentEv',
    )

  def postReadElementParam(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::postReadElementParam()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#postReadElementParam
    """
    #  bool QScxmlCompilerPrivate::postReadElementParam()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate20postReadElementParamEv',
    )

  def postReadElementScript(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::postReadElementScript()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#postReadElementScript
    """
    #  bool QScxmlCompilerPrivate::postReadElementScript()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate21postReadElementScriptEv',
    )

  def postReadElementSend(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::postReadElementSend()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#postReadElementSend
    """
    #  bool QScxmlCompilerPrivate::postReadElementSend()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate19postReadElementSendEv',
    )

  def postReadElementCancel(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::postReadElementCancel()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#postReadElementCancel
    """
    #  bool QScxmlCompilerPrivate::postReadElementCancel()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate21postReadElementCancelEv',
    )

  def postReadElementInvoke(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::postReadElementInvoke()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#postReadElementInvoke
    """
    #  bool QScxmlCompilerPrivate::postReadElementInvoke()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate21postReadElementInvokeEv',
    )

  def postReadElementFinalize(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::postReadElementFinalize()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#postReadElementFinalize
    """
    #  bool QScxmlCompilerPrivate::postReadElementFinalize()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate23postReadElementFinalizeEv',
    )

  def readElement(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::readElement()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#readElement
    """
    #  bool QScxmlCompilerPrivate::readElement()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate11readElementEv',
    )

  def resetDocument(self) -> None:
    """
    Calls Qt's 'void QScxmlCompilerPrivate::resetDocument()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#resetDocument
    """
    #  void QScxmlCompilerPrivate::resetDocument()
    self.uglySide.call('ritual_ZN21QScxmlCompilerPrivate13resetDocumentEv')

  def currentStateUp(self) -> None:
    """
    Calls Qt's 'void QScxmlCompilerPrivate::currentStateUp()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#currentStateUp
    """
    #  void QScxmlCompilerPrivate::currentStateUp()
    self.uglySide.call('ritual_ZN21QScxmlCompilerPrivate14currentStateUpEv')

  def flushInstruction(self) -> bool:
    """
    Calls Qt's 'bool QScxmlCompilerPrivate::flushInstruction()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qscxmlcompilerprivate.html#flushInstruction
    """
    #  bool QScxmlCompilerPrivate::flushInstruction()
    return self.uglySide.call(
        'ritual_ZN21QScxmlCompilerPrivate16flushInstructionEv',
    )

  @staticmethod
  def current(*__, **_) -> Never:
    """
    Qt's 'ParserState &QScxmlCompilerPrivate::current()': gives a type Python
    has no way to take yet.
    """
    raise NotImplementedError(
        "'QScxmlCompilerPrivate.current' has no cute function yet. Qt's "
        "'ParserState &QScxmlCompilerPrivate::current()': gives a type "
        "Python has no way to take yet.")

  @staticmethod
  def load(*__, **_) -> Never:
    """
    Qt's 'QByteArray QScxmlCompilerPrivate::load(const QString &name, bool
    *ok)': takes a number to change where it is.
    """
    raise NotImplementedError(
        "'QScxmlCompilerPrivate.load' has no cute function yet. Qt's "
        "'QByteArray QScxmlCompilerPrivate::load(const QString &name, bool "
        "*ok)': takes a number to change where it is.")

  @staticmethod
  def previous(*__, **_) -> Never:
    """
    Qt's 'ParserState &QScxmlCompilerPrivate::previous()': gives a type
    Python has no way to take yet.
    """
    raise NotImplementedError(
        "'QScxmlCompilerPrivate.previous' has no cute function yet. Qt's "
        "'ParserState &QScxmlCompilerPrivate::previous()': gives a type "
        "Python has no way to take yet.")
