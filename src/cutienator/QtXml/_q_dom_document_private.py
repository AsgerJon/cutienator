"""
QDomDocumentPrivate binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtXml/6.12.0/QtXml/private/qdom_p.h, Qt 6.12.0. Changes made here are
#  lost.
#
#  Qt means QDomDocumentPrivate to be private: it declares the class in a
#  header it calls private. cutienator does not care. Qt hands objects of the
#  class out all the same, and a class we are handed is a class we have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from . import QDomNode, QDomNodePrivate

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QDomDocumentTypePrivate, QDomElementPrivate
  from . import QDomImplementationPrivate


class QDomDocumentPrivate(QDomNodePrivate):
  """
  The cute side of Qt's QDomDocumentPrivate: a plain Python object standing
  in front of one C++ QDomDocumentPrivate.

  It is built on the cute 'QDomNodePrivate', as Qt's QDomDocumentPrivate is
  built on Qt's QDomNodePrivate, and has everything that class has.

  C++ hands a QDomDocumentPrivate around as a copy, so every C++
  QDomDocumentPrivate behind a cute one is Python's own: it is removed, by
  the ritual named in '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDomDocumentPrivate that has a ritual and that
  Python can call so far, 6 names in all: 'doctype', 'implementation',
  'documentElement', 'cloneNode', 'nodeType', 'clear'. None can be made from
  Python: one comes out of a function of another class that gives one back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDomDocumentPrivate::~QDomDocumentPrivate()': the destructor:
    Python removes its C++ QDomDocumentPrivate by it, and has no other use
    for it.
  - Qt's 'void QDomDocumentPrivate::saveDocument(QTextStream &stream, const
    int indent, QDomNode::EncodingPolicy encUsed) const': takes a type Python
    has no way to hand over yet.

  What has no ritual
  ------------------

  16 of the 24 functions Qt declares: 5 Qt's library has no name for it, and
  its code in Qt's source does not compile apart from its file; 4 leans on
  'QDomNodePrivate; 4 leans on 'QDomImplementationPrivate; 2 leans on
  'QDomDocumentFragmentPrivate; 1 leans on 'QDomDocumentTypePrivate.

  What to expect
  --------------

  - The C++ QDomDocumentPrivate is created at the first use, not by
    'QDomDocumentPrivate(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDomDocumentPrivate back gives a copy the ritual made
    for Python, in a new cute QDomDocumentPrivate.
  - Each name of Qt's QDomDocumentPrivate that has no cute function yet,
    '__init__', 'createAttribute', 'createAttributeNS', 'createCDATASection',
    'createComment', 'createDocumentFragment', 'createElement',
    'createElementNS', 'createEntityReference',
    'createProcessingInstruction', 'createTextNode', 'importNode',
    'saveDocument', 'setContent', holds a function that raises
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
  __qt_class__ = 'QDomDocumentPrivate'

  #  A C++ QDomDocumentPrivate Python makes is of a C++ class of ours, in
  #  which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QDomDocumentPrivate'

  #  Qt's '~QDomDocumentPrivate()'. Naming it makes this a value class:
  #  Python owns every C++ QDomDocumentPrivate behind a cute one, and removes
  #  it by this ritual.
  __delete_ritual__ = 'ritual_ZN19QDomDocumentPrivateD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def nodeType(self) -> QDomNode.NodeType:
    """
    Calls Qt's 'QDomNode::NodeType QDomDocumentPrivate::nodeType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomdocumentprivate.html#nodeType

    Returns
    -------

    QDomNode.NodeType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that
      'QDomNode.NodeType(number)' gives.
    """
    #  QDomNode::NodeType QDomDocumentPrivate::nodeType() const
    ritual = 'ritual_ZNK19QDomDocumentPrivate8nodeTypeEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZNK19QDomDocumentPrivate8nodeTypeEv'
    return QDomNode.NodeType(self.uglySide.call(ritual))

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
    - Qt's 'QDomDocumentPrivate::QDomDocumentPrivate()': leans on
      'QDomNodePrivate::QDomNodePrivate(QDomDocumentPrivate*,
      QDomNodePrivate*)', which Qt's source does not mark for use from
      outside Qt and has no code for that could be taken.
    - Qt's 'QDomDocumentPrivate::QDomDocumentPrivate(const QString &name)':
      leans on 'QDomNodePrivate::QDomNodePrivate(QDomDocumentPrivate*,
      QDomNodePrivate*)', which Qt's source does not mark for use from
      outside Qt and has no code for that could be taken.
    - Qt's 'QDomDocumentPrivate::QDomDocumentPrivate(QDomDocumentTypePrivate
      *dt)': leans on 'QDomNodePrivate::QDomNodePrivate(QDomDocumentPrivate*,
      QDomNodePrivate*)', which Qt's source does not mark for use from
      outside Qt and has no code for that could be taken.
    - Qt's 'QDomDocumentPrivate::QDomDocumentPrivate(QDomDocumentPrivate *n,
      bool deep)': leans on
      'QDomNodePrivate::QDomNodePrivate(QDomNodePrivate*, bool)', which Qt's
      source does not mark for use from outside Qt and has no code for that
      could be taken.
    """
    raise NotImplementedError(
        "'QDomDocumentPrivate.__init__' has no cute function yet. Qt's "
        "'QDomDocumentPrivate::QDomDocumentPrivate()': leans on "
        "'QDomNodePrivate::QDomNodePrivate(QDomDocumentPrivate*, "
        "QDomNodePrivate*)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken. Qt's "
        "'QDomDocumentPrivate::QDomDocumentPrivate(const QString &name)': "
        "leans on 'QDomNodePrivate::QDomNodePrivate(QDomDocumentPrivate*, "
        "QDomNodePrivate*)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken. Qt's "
        "'QDomDocumentPrivate::QDomDocumentPrivate(QDomDocumentTypePrivate "
        "*dt)': leans on "
        "'QDomNodePrivate::QDomNodePrivate(QDomDocumentPrivate*, "
        "QDomNodePrivate*)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken. Qt's "
        "'QDomDocumentPrivate::QDomDocumentPrivate(QDomDocumentPrivate *n, "
        "bool deep)': leans on "
        "'QDomNodePrivate::QDomNodePrivate(QDomNodePrivate*, bool)', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

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

  def doctype(self) -> Optional[QDomDocumentTypePrivate]:
    """
    Calls Qt's 'QDomDocumentTypePrivate *QDomDocumentPrivate::doctype()'.

    Qt's own words: https://doc.qt.io/qt-6/qdomdocumentprivate.html#doctype

    Returns
    -------

    Optional[QDomDocumentTypePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDomDocumentTypePrivate *QDomDocumentPrivate::doctype()
    address = self.uglySide.call('ritual_ZN19QDomDocumentPrivate7doctypeEv')
    from . import QDomDocumentTypePrivate
    return QDomDocumentTypePrivate._cuteAt(address)

  def implementation(self) -> Optional[QDomImplementationPrivate]:
    """
    Calls Qt's 'QDomImplementationPrivate
    *QDomDocumentPrivate::implementation()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomdocumentprivate.html#implementation

    Returns
    -------

    Optional[QDomImplementationPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDomImplementationPrivate *QDomDocumentPrivate::implementation()
    address = self.uglySide.call(
        'ritual_ZN19QDomDocumentPrivate14implementationEv',
    )
    from . import QDomImplementationPrivate
    return QDomImplementationPrivate._cuteAt(address)

  def documentElement(self) -> Optional[QDomElementPrivate]:
    """
    Calls Qt's 'QDomElementPrivate *QDomDocumentPrivate::documentElement()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomdocumentprivate.html#documentElement

    Returns
    -------

    Optional[QDomElementPrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDomElementPrivate *QDomDocumentPrivate::documentElement()
    address = self.uglySide.call(
        'ritual_ZN19QDomDocumentPrivate15documentElementEv',
    )
    from . import QDomElementPrivate
    return QDomElementPrivate._cuteAt(address)

  @overload()
  @overload(bool)
  def cloneNode(self, deep: bool = True) -> Optional[QDomNodePrivate]:
    """
    Calls Qt's 'QDomNodePrivate *QDomDocumentPrivate::cloneNode(bool deep)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomdocumentprivate.html#cloneNode

    Parameters
    ----------

    deep : bool
      Passed on as it is. May be left out, as in Qt: it is then True.

    Returns
    -------

    Optional[QDomNodePrivate]
      The cute object standing for what Qt gave back. None when Qt gave back
      no object.
    """
    #  QDomNodePrivate *QDomDocumentPrivate::cloneNode(bool deep)
    address = self.uglySide.call(
        'ritual_ZN19QDomDocumentPrivate9cloneNodeEb', deep,
    )
    return QDomNodePrivate._cuteAt(address)

  def clear(self) -> None:
    """
    Calls Qt's 'void QDomDocumentPrivate::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qdomdocumentprivate.html#clear
    """
    #  void QDomDocumentPrivate::clear()
    ritual = 'ritual_ZN19QDomDocumentPrivate5clearEv'
    if self.uglySide.isOurs():
      ritual = 'ritual_own_ZN19QDomDocumentPrivate5clearEv'
    self.uglySide.call(ritual)

  @staticmethod
  def createAttribute(*__, **_) -> Never:
    """
    Qt's 'QDomAttrPrivate *QDomDocumentPrivate::createAttribute(const QString
    &name)': Qt's library has no name for it, and its code in Qt's source
    does not compile apart from its file: use of undeclared identifier
    'fixedXmlName'.
    """
    raise NotImplementedError(
        "'QDomDocumentPrivate.createAttribute' has no cute function yet. "
        "Qt's 'QDomAttrPrivate *QDomDocumentPrivate::createAttribute(const "
        "QString &name)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'fixedXmlName'.")

  @staticmethod
  def createAttributeNS(*__, **_) -> Never:
    """
    Qt's 'QDomAttrPrivate *QDomDocumentPrivate::createAttributeNS(const
    QString &nsURI, const QString &qName)': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'fixedXmlName'.
    """
    raise NotImplementedError(
        "'QDomDocumentPrivate.createAttributeNS' has no cute function yet. "
        "Qt's 'QDomAttrPrivate "
        "*QDomDocumentPrivate::createAttributeNS(const QString &nsURI, "
        "const QString &qName)': Qt's library has no name for it, and its "
        "code in Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'fixedXmlName'.")

  @staticmethod
  def createCDATASection(*__, **_) -> Never:
    """
    Qt's 'QDomCDATASectionPrivate
    *QDomDocumentPrivate::createCDATASection(const QString &data)': leans on
    'QDomImplementationPrivate::invalidDataPolicy', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDomDocumentPrivate.createCDATASection' has no cute function yet. "
        "Qt's 'QDomCDATASectionPrivate "
        "*QDomDocumentPrivate::createCDATASection(const QString &data)': "
        "leans on 'QDomImplementationPrivate::invalidDataPolicy', which "
        "Qt's source does not mark for use from outside Qt and has no code "
        "for that could be taken.")

  @staticmethod
  def createComment(*__, **_) -> Never:
    """
    Qt's 'QDomCommentPrivate *QDomDocumentPrivate::createComment(const
    QString &data)': leans on 'QDomImplementationPrivate::invalidDataPolicy',
    which Qt's source does not mark for use from outside Qt and has no code
    for that could be taken.
    """
    raise NotImplementedError(
        "'QDomDocumentPrivate.createComment' has no cute function yet. Qt's "
        "'QDomCommentPrivate *QDomDocumentPrivate::createComment(const "
        "QString &data)': leans on "
        "'QDomImplementationPrivate::invalidDataPolicy', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def createDocumentFragment(*__, **_) -> Never:
    """
    Qt's 'QDomDocumentFragmentPrivate
    *QDomDocumentPrivate::createDocumentFragment()': leans on
    'QDomDocumentFragmentPrivate::QDomDocumentFragmentPrivate(
    QDomDocumentPrivate*, QDomNodePrivate*)', which Qt's source does not mark
    for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDomDocumentPrivate.createDocumentFragment' has no cute function "
        "yet. Qt's 'QDomDocumentFragmentPrivate "
        "*QDomDocumentPrivate::createDocumentFragment()': leans on "
        "'QDomDocumentFragmentPrivate::QDomDocumentFragmentPrivate(QDomDocum"
        "entPrivate*, QDomNodePrivate*)', which Qt's source does not mark "
        "for use from outside Qt and has no code for that could be taken.")

  @staticmethod
  def createElement(*__, **_) -> Never:
    """
    Qt's 'QDomElementPrivate *QDomDocumentPrivate::createElement(const
    QString &tagName)': leans on
    'QDomImplementationPrivate::invalidDataPolicy', which Qt's source does
    not mark for use from outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDomDocumentPrivate.createElement' has no cute function yet. Qt's "
        "'QDomElementPrivate *QDomDocumentPrivate::createElement(const "
        "QString &tagName)': leans on "
        "'QDomImplementationPrivate::invalidDataPolicy', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def createElementNS(*__, **_) -> Never:
    """
    Qt's 'QDomElementPrivate *QDomDocumentPrivate::createElementNS(const
    QString &nsURI, const QString &qName)': Qt's library has no name for it,
    and its code in Qt's source does not compile apart from its file: use of
    undeclared identifier 'fixedXmlName'.
    """
    raise NotImplementedError(
        "'QDomDocumentPrivate.createElementNS' has no cute function yet. "
        "Qt's 'QDomElementPrivate "
        "*QDomDocumentPrivate::createElementNS(const QString &nsURI, const "
        "QString &qName)': Qt's library has no name for it, and its code in "
        "Qt's source does not compile apart from its file: use of "
        "undeclared identifier 'fixedXmlName'.")

  @staticmethod
  def createEntityReference(*__, **_) -> Never:
    """
    Qt's 'QDomEntityReferencePrivate
    *QDomDocumentPrivate::createEntityReference(const QString &name)': Qt's
    library has no name for it, and its code in Qt's source does not compile
    apart from its file: use of undeclared identifier 'fixedXmlName'.
    """
    raise NotImplementedError(
        "'QDomDocumentPrivate.createEntityReference' has no cute function "
        "yet. Qt's 'QDomEntityReferencePrivate "
        "*QDomDocumentPrivate::createEntityReference(const QString &name)': "
        "Qt's library has no name for it, and its code in Qt's source does "
        "not compile apart from its file: use of undeclared identifier "
        "'fixedXmlName'.")

  @staticmethod
  def createProcessingInstruction(*__, **_) -> Never:
    """
    Qt's 'QDomProcessingInstructionPrivate
    *QDomDocumentPrivate::createProcessingInstruction(const QString &target,
    const QString &data)': Qt's library has no name for it, and its code in
    Qt's source does not compile apart from its file: use of undeclared
    identifier 'fixedXmlName'.
    """
    raise NotImplementedError(
        "'QDomDocumentPrivate.createProcessingInstruction' has no cute "
        "function yet. Qt's 'QDomProcessingInstructionPrivate "
        "*QDomDocumentPrivate::createProcessingInstruction(const QString "
        "&target, const QString &data)': Qt's library has no name for it, "
        "and its code in Qt's source does not compile apart from its file: "
        "use of undeclared identifier 'fixedXmlName'.")

  @staticmethod
  def createTextNode(*__, **_) -> Never:
    """
    Qt's 'QDomTextPrivate *QDomDocumentPrivate::createTextNode(const QString
    &data)': leans on 'QDomImplementationPrivate::invalidDataPolicy', which
    Qt's source does not mark for use from outside Qt and has no code for
    that could be taken.
    """
    raise NotImplementedError(
        "'QDomDocumentPrivate.createTextNode' has no cute function yet. "
        "Qt's 'QDomTextPrivate *QDomDocumentPrivate::createTextNode(const "
        "QString &data)': leans on "
        "'QDomImplementationPrivate::invalidDataPolicy', which Qt's source "
        "does not mark for use from outside Qt and has no code for that "
        "could be taken.")

  @staticmethod
  def importNode(*__, **_) -> Never:
    """
    Qt's 'QDomNodePrivate *QDomDocumentPrivate::importNode(QDomNodePrivate
    *importedNode, bool deep)': leans on
    'QDomDocumentFragmentPrivate::QDomDocumentFragmentPrivate(
    QDomNodePrivate*, bool)', which Qt's source does not mark for use from
    outside Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDomDocumentPrivate.importNode' has no cute function yet. Qt's "
        "'QDomNodePrivate *QDomDocumentPrivate::importNode(QDomNodePrivate "
        "*importedNode, bool deep)': leans on "
        "'QDomDocumentFragmentPrivate::QDomDocumentFragmentPrivate(QDomNodeP"
        "rivate*, bool)', which Qt's source does not mark for use from "
        "outside Qt and has no code for that could be taken.")

  @staticmethod
  def saveDocument(*__, **_) -> Never:
    """
    Qt's 'void QDomDocumentPrivate::saveDocument(QTextStream &stream, const
    int indent, QDomNode::EncodingPolicy encUsed) const': takes a type Python
    has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDomDocumentPrivate.saveDocument' has no cute function yet. Qt's "
        "'void QDomDocumentPrivate::saveDocument(QTextStream &stream, const "
        "int indent, QDomNode::EncodingPolicy encUsed) const': takes a type "
        "Python has no way to hand over yet.")

  @staticmethod
  def setContent(*__, **_) -> Never:
    """
    Qt's 'QDomDocument::ParseResult
    QDomDocumentPrivate::setContent(QXmlStreamReader *reader,
    QDomDocument::ParseOptions options)': leans on
    'QDomDocumentTypePrivate::QDomDocumentTypePrivate(QDomDocumentPrivate*,
    QDomNodePrivate*)', which Qt's source does not mark for use from outside
    Qt and has no code for that could be taken.
    """
    raise NotImplementedError(
        "'QDomDocumentPrivate.setContent' has no cute function yet. Qt's "
        "'QDomDocument::ParseResult "
        "QDomDocumentPrivate::setContent(QXmlStreamReader *reader, "
        "QDomDocument::ParseOptions options)': leans on "
        "'QDomDocumentTypePrivate::QDomDocumentTypePrivate(QDomDocumentPriva"
        "te*, QDomNodePrivate*)', which Qt's source does not mark for use "
        "from outside Qt and has no code for that could be taken.")
