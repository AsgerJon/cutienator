"""
QDomNode binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of QtXml/qdom.h, Qt
#  6.12.0. Changes made here are lost.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.core.sentinels import THIS
from worktoy.dispatch import overload
from worktoy.keenum import Kee

from ..cute import CuteMixin, CuteNum, MetaCute, WAIT
from ..occult import Rituals

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never, Optional

  from . import QDomAttr, QDomCDATASection, QDomCharacterData, QDomComment
  from . import QDomDocument, QDomDocumentFragment, QDomDocumentType
  from . import QDomElement, QDomEntity, QDomEntityReference
  from . import QDomNamedNodeMap, QDomNodeList, QDomNodePrivate, QDomNotation
  from . import QDomProcessingInstruction, QDomText
else:
  #  The cute classes this file names and is not built on. Each is brought in
  #  by the program that uses it, and a signature naming it waits until then;
  #  see 'WAIT'.
  QDomNodePrivate = WAIT['QDomNodePrivate']

#  The class of None, for a signature that takes None in the place of an
#  object or of text.
NoneType = type(None)


class QDomNode(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QDomNode: a plain Python object standing in front of
  one C++ QDomNode.

  C++ hands a QDomNode around as a copy, so every C++ QDomNode behind a cute
  one is Python's own: it is removed, by the ritual named in
  '__delete_ritual__', when the cute object goes.

  What exists
  -----------

  Every function of Qt's QDomNode that has a ritual and that Python can call
  so far, 63 names in all: '__eq__', '__ne__', 'insertBefore', 'insertAfter',
  'replaceChild', 'removeChild', 'appendChild', 'hasChildNodes', 'cloneNode',
  'normalize', 'isSupported', 'nodeName', 'nodeType', 'parentNode',
  'childNodes', 'firstChild', 'lastChild', 'previousSibling', 'nextSibling',
  'attributes', 'ownerDocument', 'namespaceURI', 'localName',
  'hasAttributes', 'nodeValue', 'setNodeValue', 'prefix', 'setPrefix',
  'isAttr', 'isCDATASection', 'isDocumentFragment', 'isDocument',
  'isDocumentType', 'isElement', 'isEntityReference', 'isText', 'isEntity',
  'isNotation', 'isProcessingInstruction', 'isCharacterData', 'isComment',
  'namedItem', 'isNull', 'clear', 'toAttr', 'toCDATASection',
  'toDocumentFragment', 'toDocument', 'toDocumentType', 'toElement',
  'toEntityReference', 'toText', 'toEntity', 'toNotation',
  'toProcessingInstruction', 'toCharacterData', 'toComment',
  'firstChildElement', 'lastChildElement', 'previousSiblingElement',
  'nextSiblingElement', 'lineNumber', 'columnNumber'. It can be made from
  Python, in 3 ways; see '__init__'.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QDomNode &QDomNode::operator=(const QDomNode &other)': assignment:
    Python binds a name and has no operator for it.
  - Qt's 'QDomNode::~QDomNode()': the destructor: Python removes its C++
    QDomNode by it, and has no other use for it.
  - Qt's 'void QDomNode::save(QTextStream &a0, int a1, EncodingPolicy a2)
    const': takes a type Python has no way to hand over yet.

  What to expect
  --------------

  - The C++ QDomNode is created at the first use, not by 'QDomNode(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - A function giving a QDomNode back gives a copy the ritual made for
    Python, in a new cute QDomNode.
  - Each name of Qt's QDomNode that has no cute function yet, 'save', holds a
    function that raises 'NotImplementedError', and its docstring says why.
  """

  #  The enums Qt writes inside QDomNode, each a class in here as in C++, and
  #  the names Qt has for the combinations of its flags enums.

  class EncodingPolicy(CuteNum):
    """
    The enum 'QDomNode::EncodingPolicy' of Qt, with the 2 names Qt gives in
    it.
    """

    EncodingFromDocument = Kee[int](1)
    EncodingFromTextStream = Kee[int](2)

  class NodeType(CuteNum):
    """
    The enum 'QDomNode::NodeType' of Qt, with the 14 names Qt gives in it.
    """

    ElementNode = Kee[int](1)
    AttributeNode = Kee[int](2)
    TextNode = Kee[int](3)
    CDATASectionNode = Kee[int](4)
    EntityReferenceNode = Kee[int](5)
    EntityNode = Kee[int](6)
    ProcessingInstructionNode = Kee[int](7)
    CommentNode = Kee[int](8)
    DocumentNode = Kee[int](9)
    DocumentTypeNode = Kee[int](10)
    DocumentFragmentNode = Kee[int](11)
    NotationNode = Kee[int](12)
    BaseNode = Kee[int](21)
    CharacterDataNode = Kee[int](22)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QDomNode'

  #  Qt's '~QDomNode()'. Naming it makes this a value class: Python owns
  #  every C++ QDomNode behind a cute one, and removes it by this ritual.
  __delete_ritual__ = 'ritual_ZN8QDomNodeD1Ev'

  #  Fallback Variables

  #  Private Variables

  #  Public Variables

  #  Virtual Variables

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  GETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  def hasChildNodes(self) -> bool:
    """
    Calls Qt's 'bool QDomNode::hasChildNodes() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#hasChildNodes
    """
    #  bool QDomNode::hasChildNodes() const
    return self.uglySide.call('ritual_ZNK8QDomNode13hasChildNodesEv')

  @overload()
  @overload(bool)
  def cloneNode(self, deep: bool = True) -> QDomNode:
    """
    Calls Qt's 'QDomNode QDomNode::cloneNode(bool deep) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#cloneNode

    Parameters
    ----------

    deep : bool
      Passed on as it is. May be left out, as in Qt: it is then True.

    Returns
    -------

    QDomNode
      A new cute QDomNode around the copy Qt gave back. Python owns it.
    """
    #  QDomNode QDomNode::cloneNode(bool deep) const
    address = self.uglySide.call('ritual_ZNK8QDomNode9cloneNodeEb', deep)
    return QDomNode._cuteOwning(address)

  @overload(str, str)
  def isSupported(self, feature: str, version: str) -> bool:
    """
    Calls Qt's 'bool QDomNode::isSupported(const QString &feature, const
    QString &version) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#isSupported

    Parameters
    ----------

    feature : str
      Passed on as it is: a QString is made of it for the call.

    version : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  bool QDomNode::isSupported(const QString &feature, const QString
    #      &version) const
    return self.uglySide.call(
        'ritual_ZNK8QDomNode11isSupportedERK7QStringS2_', feature, version,
    )

  def nodeName(self) -> str:
    """
    Calls Qt's 'QString QDomNode::nodeName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#nodeName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDomNode::nodeName() const
    return self.uglySide.call('ritual_ZNK8QDomNode8nodeNameEv')

  def nodeType(self) -> NodeType:
    """
    Calls Qt's 'NodeType QDomNode::nodeType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#nodeType

    Returns
    -------

    NodeType
      The member standing for the number Qt gave back. For a number Qt gives
      no name it is the member without a name that 'NodeType(number)' gives.
    """
    #  NodeType QDomNode::nodeType() const
    return QDomNode.NodeType(self.uglySide.call(
        'ritual_ZNK8QDomNode8nodeTypeEv',
    ))

  def parentNode(self) -> QDomNode:
    """
    Calls Qt's 'QDomNode QDomNode::parentNode() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#parentNode

    Returns
    -------

    QDomNode
      A new cute QDomNode around the copy Qt gave back. Python owns it.
    """
    #  QDomNode QDomNode::parentNode() const
    address = self.uglySide.call('ritual_ZNK8QDomNode10parentNodeEv')
    return QDomNode._cuteOwning(address)

  def childNodes(self) -> QDomNodeList:
    """
    Calls Qt's 'QDomNodeList QDomNode::childNodes() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#childNodes

    Returns
    -------

    QDomNodeList
      A new cute QDomNodeList around the copy Qt gave back. Python owns it.
    """
    #  QDomNodeList QDomNode::childNodes() const
    address = self.uglySide.call('ritual_ZNK8QDomNode10childNodesEv')
    from . import QDomNodeList
    return QDomNodeList._cuteOwning(address)

  def firstChild(self) -> QDomNode:
    """
    Calls Qt's 'QDomNode QDomNode::firstChild() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#firstChild

    Returns
    -------

    QDomNode
      A new cute QDomNode around the copy Qt gave back. Python owns it.
    """
    #  QDomNode QDomNode::firstChild() const
    address = self.uglySide.call('ritual_ZNK8QDomNode10firstChildEv')
    return QDomNode._cuteOwning(address)

  def lastChild(self) -> QDomNode:
    """
    Calls Qt's 'QDomNode QDomNode::lastChild() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#lastChild

    Returns
    -------

    QDomNode
      A new cute QDomNode around the copy Qt gave back. Python owns it.
    """
    #  QDomNode QDomNode::lastChild() const
    address = self.uglySide.call('ritual_ZNK8QDomNode9lastChildEv')
    return QDomNode._cuteOwning(address)

  def previousSibling(self) -> QDomNode:
    """
    Calls Qt's 'QDomNode QDomNode::previousSibling() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#previousSibling

    Returns
    -------

    QDomNode
      A new cute QDomNode around the copy Qt gave back. Python owns it.
    """
    #  QDomNode QDomNode::previousSibling() const
    address = self.uglySide.call('ritual_ZNK8QDomNode15previousSiblingEv')
    return QDomNode._cuteOwning(address)

  def nextSibling(self) -> QDomNode:
    """
    Calls Qt's 'QDomNode QDomNode::nextSibling() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#nextSibling

    Returns
    -------

    QDomNode
      A new cute QDomNode around the copy Qt gave back. Python owns it.
    """
    #  QDomNode QDomNode::nextSibling() const
    address = self.uglySide.call('ritual_ZNK8QDomNode11nextSiblingEv')
    return QDomNode._cuteOwning(address)

  def attributes(self) -> QDomNamedNodeMap:
    """
    Calls Qt's 'QDomNamedNodeMap QDomNode::attributes() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#attributes

    Returns
    -------

    QDomNamedNodeMap
      A new cute QDomNamedNodeMap around the copy Qt gave back. Python owns
      it.
    """
    #  QDomNamedNodeMap QDomNode::attributes() const
    address = self.uglySide.call('ritual_ZNK8QDomNode10attributesEv')
    from . import QDomNamedNodeMap
    return QDomNamedNodeMap._cuteOwning(address)

  def ownerDocument(self) -> QDomDocument:
    """
    Calls Qt's 'QDomDocument QDomNode::ownerDocument() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#ownerDocument

    Returns
    -------

    QDomDocument
      A new cute QDomDocument around the copy Qt gave back. Python owns it.
    """
    #  QDomDocument QDomNode::ownerDocument() const
    address = self.uglySide.call('ritual_ZNK8QDomNode13ownerDocumentEv')
    from . import QDomDocument
    return QDomDocument._cuteOwning(address)

  def namespaceURI(self) -> str:
    """
    Calls Qt's 'QString QDomNode::namespaceURI() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#namespaceURI

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDomNode::namespaceURI() const
    return self.uglySide.call('ritual_ZNK8QDomNode12namespaceURIEv')

  def localName(self) -> str:
    """
    Calls Qt's 'QString QDomNode::localName() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#localName

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDomNode::localName() const
    return self.uglySide.call('ritual_ZNK8QDomNode9localNameEv')

  def hasAttributes(self) -> bool:
    """
    Calls Qt's 'bool QDomNode::hasAttributes() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#hasAttributes
    """
    #  bool QDomNode::hasAttributes() const
    return self.uglySide.call('ritual_ZNK8QDomNode13hasAttributesEv')

  def nodeValue(self) -> str:
    """
    Calls Qt's 'QString QDomNode::nodeValue() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#nodeValue

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDomNode::nodeValue() const
    return self.uglySide.call('ritual_ZNK8QDomNode9nodeValueEv')

  def prefix(self) -> str:
    """
    Calls Qt's 'QString QDomNode::prefix() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#prefix

    Returns
    -------

    str
      The text Qt gave back.
    """
    #  QString QDomNode::prefix() const
    return self.uglySide.call('ritual_ZNK8QDomNode6prefixEv')

  def isAttr(self) -> bool:
    """
    Calls Qt's 'bool QDomNode::isAttr() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#isAttr
    """
    #  bool QDomNode::isAttr() const
    return self.uglySide.call('ritual_ZNK8QDomNode6isAttrEv')

  def isCDATASection(self) -> bool:
    """
    Calls Qt's 'bool QDomNode::isCDATASection() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#isCDATASection
    """
    #  bool QDomNode::isCDATASection() const
    return self.uglySide.call('ritual_ZNK8QDomNode14isCDATASectionEv')

  def isDocumentFragment(self) -> bool:
    """
    Calls Qt's 'bool QDomNode::isDocumentFragment() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#isDocumentFragment
    """
    #  bool QDomNode::isDocumentFragment() const
    return self.uglySide.call('ritual_ZNK8QDomNode18isDocumentFragmentEv')

  def isDocument(self) -> bool:
    """
    Calls Qt's 'bool QDomNode::isDocument() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#isDocument
    """
    #  bool QDomNode::isDocument() const
    return self.uglySide.call('ritual_ZNK8QDomNode10isDocumentEv')

  def isDocumentType(self) -> bool:
    """
    Calls Qt's 'bool QDomNode::isDocumentType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#isDocumentType
    """
    #  bool QDomNode::isDocumentType() const
    return self.uglySide.call('ritual_ZNK8QDomNode14isDocumentTypeEv')

  def isElement(self) -> bool:
    """
    Calls Qt's 'bool QDomNode::isElement() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#isElement
    """
    #  bool QDomNode::isElement() const
    return self.uglySide.call('ritual_ZNK8QDomNode9isElementEv')

  def isEntityReference(self) -> bool:
    """
    Calls Qt's 'bool QDomNode::isEntityReference() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#isEntityReference
    """
    #  bool QDomNode::isEntityReference() const
    return self.uglySide.call('ritual_ZNK8QDomNode17isEntityReferenceEv')

  def isText(self) -> bool:
    """
    Calls Qt's 'bool QDomNode::isText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#isText
    """
    #  bool QDomNode::isText() const
    return self.uglySide.call('ritual_ZNK8QDomNode6isTextEv')

  def isEntity(self) -> bool:
    """
    Calls Qt's 'bool QDomNode::isEntity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#isEntity
    """
    #  bool QDomNode::isEntity() const
    return self.uglySide.call('ritual_ZNK8QDomNode8isEntityEv')

  def isNotation(self) -> bool:
    """
    Calls Qt's 'bool QDomNode::isNotation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#isNotation
    """
    #  bool QDomNode::isNotation() const
    return self.uglySide.call('ritual_ZNK8QDomNode10isNotationEv')

  def isProcessingInstruction(self) -> bool:
    """
    Calls Qt's 'bool QDomNode::isProcessingInstruction() const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomnode.html#isProcessingInstruction
    """
    #  bool QDomNode::isProcessingInstruction() const
    return self.uglySide.call(
        'ritual_ZNK8QDomNode23isProcessingInstructionEv',
    )

  def isCharacterData(self) -> bool:
    """
    Calls Qt's 'bool QDomNode::isCharacterData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#isCharacterData
    """
    #  bool QDomNode::isCharacterData() const
    return self.uglySide.call('ritual_ZNK8QDomNode15isCharacterDataEv')

  def isComment(self) -> bool:
    """
    Calls Qt's 'bool QDomNode::isComment() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#isComment
    """
    #  bool QDomNode::isComment() const
    return self.uglySide.call('ritual_ZNK8QDomNode9isCommentEv')

  @overload(str)
  def namedItem(self, name: str) -> QDomNode:
    """
    Calls Qt's 'QDomNode QDomNode::namedItem(const QString &name) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#namedItem

    Parameters
    ----------

    name : str
      Passed on as it is: a QString is made of it for the call.

    Returns
    -------

    QDomNode
      A new cute QDomNode around the copy Qt gave back. Python owns it.
    """
    #  QDomNode QDomNode::namedItem(const QString &name) const
    address = self.uglySide.call(
        'ritual_ZNK8QDomNode9namedItemERK7QString', name,
    )
    return QDomNode._cuteOwning(address)

  def isNull(self) -> bool:
    """
    Calls Qt's 'bool QDomNode::isNull() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#isNull
    """
    #  bool QDomNode::isNull() const
    return self.uglySide.call('ritual_ZNK8QDomNode6isNullEv')

  def toAttr(self) -> QDomAttr:
    """
    Calls Qt's 'QDomAttr QDomNode::toAttr() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#toAttr

    Returns
    -------

    QDomAttr
      A new cute QDomAttr around the copy Qt gave back. Python owns it.
    """
    #  QDomAttr QDomNode::toAttr() const
    address = self.uglySide.call('ritual_ZNK8QDomNode6toAttrEv')
    from . import QDomAttr
    return QDomAttr._cuteOwning(address)

  def toCDATASection(self) -> QDomCDATASection:
    """
    Calls Qt's 'QDomCDATASection QDomNode::toCDATASection() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#toCDATASection

    Returns
    -------

    QDomCDATASection
      A new cute QDomCDATASection around the copy Qt gave back. Python owns
      it.
    """
    #  QDomCDATASection QDomNode::toCDATASection() const
    address = self.uglySide.call('ritual_ZNK8QDomNode14toCDATASectionEv')
    from . import QDomCDATASection
    return QDomCDATASection._cuteOwning(address)

  def toDocumentFragment(self) -> QDomDocumentFragment:
    """
    Calls Qt's 'QDomDocumentFragment QDomNode::toDocumentFragment() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#toDocumentFragment

    Returns
    -------

    QDomDocumentFragment
      A new cute QDomDocumentFragment around the copy Qt gave back. Python
      owns it.
    """
    #  QDomDocumentFragment QDomNode::toDocumentFragment() const
    address = self.uglySide.call('ritual_ZNK8QDomNode18toDocumentFragmentEv')
    from . import QDomDocumentFragment
    return QDomDocumentFragment._cuteOwning(address)

  def toDocument(self) -> QDomDocument:
    """
    Calls Qt's 'QDomDocument QDomNode::toDocument() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#toDocument

    Returns
    -------

    QDomDocument
      A new cute QDomDocument around the copy Qt gave back. Python owns it.
    """
    #  QDomDocument QDomNode::toDocument() const
    address = self.uglySide.call('ritual_ZNK8QDomNode10toDocumentEv')
    from . import QDomDocument
    return QDomDocument._cuteOwning(address)

  def toDocumentType(self) -> QDomDocumentType:
    """
    Calls Qt's 'QDomDocumentType QDomNode::toDocumentType() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#toDocumentType

    Returns
    -------

    QDomDocumentType
      A new cute QDomDocumentType around the copy Qt gave back. Python owns
      it.
    """
    #  QDomDocumentType QDomNode::toDocumentType() const
    address = self.uglySide.call('ritual_ZNK8QDomNode14toDocumentTypeEv')
    from . import QDomDocumentType
    return QDomDocumentType._cuteOwning(address)

  def toElement(self) -> QDomElement:
    """
    Calls Qt's 'QDomElement QDomNode::toElement() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#toElement

    Returns
    -------

    QDomElement
      A new cute QDomElement around the copy Qt gave back. Python owns it.
    """
    #  QDomElement QDomNode::toElement() const
    address = self.uglySide.call('ritual_ZNK8QDomNode9toElementEv')
    from . import QDomElement
    return QDomElement._cuteOwning(address)

  def toEntityReference(self) -> QDomEntityReference:
    """
    Calls Qt's 'QDomEntityReference QDomNode::toEntityReference() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#toEntityReference

    Returns
    -------

    QDomEntityReference
      A new cute QDomEntityReference around the copy Qt gave back. Python
      owns it.
    """
    #  QDomEntityReference QDomNode::toEntityReference() const
    address = self.uglySide.call('ritual_ZNK8QDomNode17toEntityReferenceEv')
    from . import QDomEntityReference
    return QDomEntityReference._cuteOwning(address)

  def toText(self) -> QDomText:
    """
    Calls Qt's 'QDomText QDomNode::toText() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#toText

    Returns
    -------

    QDomText
      A new cute QDomText around the copy Qt gave back. Python owns it.
    """
    #  QDomText QDomNode::toText() const
    address = self.uglySide.call('ritual_ZNK8QDomNode6toTextEv')
    from . import QDomText
    return QDomText._cuteOwning(address)

  def toEntity(self) -> QDomEntity:
    """
    Calls Qt's 'QDomEntity QDomNode::toEntity() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#toEntity

    Returns
    -------

    QDomEntity
      A new cute QDomEntity around the copy Qt gave back. Python owns it.
    """
    #  QDomEntity QDomNode::toEntity() const
    address = self.uglySide.call('ritual_ZNK8QDomNode8toEntityEv')
    from . import QDomEntity
    return QDomEntity._cuteOwning(address)

  def toNotation(self) -> QDomNotation:
    """
    Calls Qt's 'QDomNotation QDomNode::toNotation() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#toNotation

    Returns
    -------

    QDomNotation
      A new cute QDomNotation around the copy Qt gave back. Python owns it.
    """
    #  QDomNotation QDomNode::toNotation() const
    address = self.uglySide.call('ritual_ZNK8QDomNode10toNotationEv')
    from . import QDomNotation
    return QDomNotation._cuteOwning(address)

  def toProcessingInstruction(self) -> QDomProcessingInstruction:
    """
    Calls Qt's 'QDomProcessingInstruction QDomNode::toProcessingInstruction()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomnode.html#toProcessingInstruction

    Returns
    -------

    QDomProcessingInstruction
      A new cute QDomProcessingInstruction around the copy Qt gave back.
      Python owns it.
    """
    #  QDomProcessingInstruction QDomNode::toProcessingInstruction() const
    address = self.uglySide.call(
        'ritual_ZNK8QDomNode23toProcessingInstructionEv',
    )
    from . import QDomProcessingInstruction
    return QDomProcessingInstruction._cuteOwning(address)

  def toCharacterData(self) -> QDomCharacterData:
    """
    Calls Qt's 'QDomCharacterData QDomNode::toCharacterData() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#toCharacterData

    Returns
    -------

    QDomCharacterData
      A new cute QDomCharacterData around the copy Qt gave back. Python owns
      it.
    """
    #  QDomCharacterData QDomNode::toCharacterData() const
    address = self.uglySide.call('ritual_ZNK8QDomNode15toCharacterDataEv')
    from . import QDomCharacterData
    return QDomCharacterData._cuteOwning(address)

  def toComment(self) -> QDomComment:
    """
    Calls Qt's 'QDomComment QDomNode::toComment() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#toComment

    Returns
    -------

    QDomComment
      A new cute QDomComment around the copy Qt gave back. Python owns it.
    """
    #  QDomComment QDomNode::toComment() const
    address = self.uglySide.call('ritual_ZNK8QDomNode9toCommentEv')
    from . import QDomComment
    return QDomComment._cuteOwning(address)

  @overload()
  @overload(str)
  @overload(str, str)
  def firstChildElement(
      self,
      tagName: str = '',
      namespaceURI: str = '',
  ) -> QDomElement:
    """
    Calls Qt's 'QDomElement QDomNode::firstChildElement(const QString
    &tagName, const QString &namespaceURI) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#firstChildElement

    Parameters
    ----------

    tagName : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    namespaceURI : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    QDomElement
      A new cute QDomElement around the copy Qt gave back. Python owns it.
    """
    #  QDomElement QDomNode::firstChildElement(const QString &tagName, const
    #      QString &namespaceURI) const
    address = self.uglySide.call(
        'ritual_ZNK8QDomNode17firstChildElementERK7QStringS2_',
        tagName, namespaceURI,
    )
    from . import QDomElement
    return QDomElement._cuteOwning(address)

  @overload()
  @overload(str)
  @overload(str, str)
  def lastChildElement(
      self,
      tagName: str = '',
      namespaceURI: str = '',
  ) -> QDomElement:
    """
    Calls Qt's 'QDomElement QDomNode::lastChildElement(const QString
    &tagName, const QString &namespaceURI) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#lastChildElement

    Parameters
    ----------

    tagName : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    namespaceURI : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    QDomElement
      A new cute QDomElement around the copy Qt gave back. Python owns it.
    """
    #  QDomElement QDomNode::lastChildElement(const QString &tagName, const
    #      QString &namespaceURI) const
    address = self.uglySide.call(
        'ritual_ZNK8QDomNode16lastChildElementERK7QStringS2_',
        tagName, namespaceURI,
    )
    from . import QDomElement
    return QDomElement._cuteOwning(address)

  @overload()
  @overload(str)
  @overload(str, str)
  def previousSiblingElement(
      self,
      tagName: str = '',
      namespaceURI: str = '',
  ) -> QDomElement:
    """
    Calls Qt's 'QDomElement QDomNode::previousSiblingElement(const QString
    &tagName, const QString &namespaceURI) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qdomnode.html#previousSiblingElement

    Parameters
    ----------

    tagName : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    namespaceURI : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    QDomElement
      A new cute QDomElement around the copy Qt gave back. Python owns it.
    """
    #  QDomElement QDomNode::previousSiblingElement(const QString &tagName,
    #      const QString &namespaceURI) const
    address = self.uglySide.call(
        'ritual_ZNK8QDomNode22previousSiblingElementERK7QStringS2_',
        tagName, namespaceURI,
    )
    from . import QDomElement
    return QDomElement._cuteOwning(address)

  @overload()
  @overload(str)
  @overload(str, str)
  def nextSiblingElement(
      self,
      taName: str = '',
      namespaceURI: str = '',
  ) -> QDomElement:
    """
    Calls Qt's 'QDomElement QDomNode::nextSiblingElement(const QString
    &taName, const QString &namespaceURI) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#nextSiblingElement

    Parameters
    ----------

    taName : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    namespaceURI : str
      Passed on as it is: a QString is made of it for the call. May be left
      out, as in Qt: it is then ''.

    Returns
    -------

    QDomElement
      A new cute QDomElement around the copy Qt gave back. Python owns it.
    """
    #  QDomElement QDomNode::nextSiblingElement(const QString &taName, const
    #      QString &namespaceURI) const
    address = self.uglySide.call(
        'ritual_ZNK8QDomNode18nextSiblingElementERK7QStringS2_',
        taName, namespaceURI,
    )
    from . import QDomElement
    return QDomElement._cuteOwning(address)

  def lineNumber(self) -> int:
    """
    Calls Qt's 'int QDomNode::lineNumber() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#lineNumber
    """
    #  int QDomNode::lineNumber() const
    return self.uglySide.call('ritual_ZNK8QDomNode10lineNumberEv')

  def columnNumber(self) -> int:
    """
    Calls Qt's 'int QDomNode::columnNumber() const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#columnNumber
    """
    #  int QDomNode::columnNumber() const
    return self.uglySide.call('ritual_ZNK8QDomNode12columnNumberEv')

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  SETTERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(str)
  def setNodeValue(self, value: str) -> None:
    """
    Calls Qt's 'void QDomNode::setNodeValue(const QString &value)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#setNodeValue

    Parameters
    ----------

    value : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDomNode::setNodeValue(const QString &value)
    self.uglySide.call('ritual_ZN8QDomNode12setNodeValueERK7QString', value)

  @overload(str)
  def setPrefix(self, pre: str) -> None:
    """
    Calls Qt's 'void QDomNode::setPrefix(const QString &pre)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#setPrefix

    Parameters
    ----------

    pre : str
      Passed on as it is: a QString is made of it for the call.
    """
    #  void QDomNode::setPrefix(const QString &pre)
    self.uglySide.call('ritual_ZN8QDomNode9setPrefixERK7QString', pre)

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NOTIFIERS  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  Python API   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload(THIS)
  def __eq__(self, other: QDomNode) -> bool:
    """
    Calls Qt's 'bool QDomNode::operator==(const QDomNode &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#operator==

    Parameters
    ----------

    other : QDomNode
      Passed on as a value: Qt reads the C++ QDomNode, which stays Python's
      own.
    """
    #  bool QDomNode::operator==(const QDomNode &other) const
    return self.uglySide.call(
        'ritual_ZNK8QDomNodeeqERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __eq__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  @overload(THIS)
  def __ne__(self, other: QDomNode) -> bool:
    """
    Calls Qt's 'bool QDomNode::operator!=(const QDomNode &other) const'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#operator!=

    Parameters
    ----------

    other : QDomNode
      Passed on as a value: Qt reads the C++ QDomNode, which stays Python's
      own.
    """
    #  bool QDomNode::operator!=(const QDomNode &other) const
    return self.uglySide.call(
        'ritual_ZNK8QDomNodeneERKS_', self._valueOf(other),
    )

  @overload.fallback
  def __ne__(self, *args: object) -> object:
    """
    Tells Python that no function of this name takes what it was
    handed, with Python's own word for it. Python then asks the
    other side of the operator.
    """
    return NotImplemented

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  CONSTRUCTORS   # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  @overload()
  def __init__(self) -> None:
    """
    Notes what was given, for Qt's 'QDomNode::QDomNode()', which is called at
    the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#QDomNode
    """
    #  QDomNode::QDomNode()
    self._noteCreation(QDomNode, lambda: Rituals.call(
        'ritual_ZN8QDomNodeC1Ev',
    ))

  @overload(THIS)
  def __init__(self, node: QDomNode) -> None:
    """
    Notes what was given, for Qt's 'QDomNode::QDomNode(const QDomNode
    &node)', which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#QDomNode

    Parameters
    ----------

    node : QDomNode
      Passed on as a value: Qt reads the C++ QDomNode, which stays Python's
      own.
    """
    #  QDomNode::QDomNode(const QDomNode &node)
    self._noteCreation(QDomNode, lambda: Rituals.call(
        'ritual_ZN8QDomNodeC1ERKS_', self._valueOf(node),
    ))

  @overload(QDomNodePrivate)
  @overload(NoneType)
  def __init__(self, a0: Optional[QDomNodePrivate]) -> None:
    """
    Notes what was given, for Qt's 'QDomNode::QDomNode(QDomNodePrivate *a0)',
    which is called at the first use.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#QDomNode

    Parameters
    ----------

    a0 : Optional[QDomNodePrivate]
      Passed on as the address of its C++ object. None is passed on as no
      object.
    """
    #  QDomNode::QDomNode(QDomNodePrivate *a0)
    self._noteCreation(QDomNode, lambda: Rituals.call(
        'ritual_ZN8QDomNodeC1EP15QDomNodePrivate', self._addressOf(a0),
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

  @overload(THIS, THIS)
  def insertBefore(self, newChild: QDomNode, refChild: QDomNode) -> QDomNode:
    """
    Calls Qt's 'QDomNode QDomNode::insertBefore(const QDomNode &newChild,
    const QDomNode &refChild)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#insertBefore

    Parameters
    ----------

    newChild : QDomNode
      Passed on as a value: Qt reads the C++ QDomNode, which stays Python's
      own.

    refChild : QDomNode
      Passed on as a value: Qt reads the C++ QDomNode, which stays Python's
      own.

    Returns
    -------

    QDomNode
      A new cute QDomNode around the copy Qt gave back. Python owns it.
    """
    #  QDomNode QDomNode::insertBefore(const QDomNode &newChild, const
    #      QDomNode &refChild)
    address = self.uglySide.call(
        'ritual_ZN8QDomNode12insertBeforeERKS_S1_',
        self._valueOf(newChild), self._valueOf(refChild),
    )
    return QDomNode._cuteOwning(address)

  @overload(THIS, THIS)
  def insertAfter(self, newChild: QDomNode, refChild: QDomNode) -> QDomNode:
    """
    Calls Qt's 'QDomNode QDomNode::insertAfter(const QDomNode &newChild,
    const QDomNode &refChild)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#insertAfter

    Parameters
    ----------

    newChild : QDomNode
      Passed on as a value: Qt reads the C++ QDomNode, which stays Python's
      own.

    refChild : QDomNode
      Passed on as a value: Qt reads the C++ QDomNode, which stays Python's
      own.

    Returns
    -------

    QDomNode
      A new cute QDomNode around the copy Qt gave back. Python owns it.
    """
    #  QDomNode QDomNode::insertAfter(const QDomNode &newChild, const
    #      QDomNode &refChild)
    address = self.uglySide.call(
        'ritual_ZN8QDomNode11insertAfterERKS_S1_',
        self._valueOf(newChild), self._valueOf(refChild),
    )
    return QDomNode._cuteOwning(address)

  @overload(THIS, THIS)
  def replaceChild(self, newChild: QDomNode, oldChild: QDomNode) -> QDomNode:
    """
    Calls Qt's 'QDomNode QDomNode::replaceChild(const QDomNode &newChild,
    const QDomNode &oldChild)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#replaceChild

    Parameters
    ----------

    newChild : QDomNode
      Passed on as a value: Qt reads the C++ QDomNode, which stays Python's
      own.

    oldChild : QDomNode
      Passed on as a value: Qt reads the C++ QDomNode, which stays Python's
      own.

    Returns
    -------

    QDomNode
      A new cute QDomNode around the copy Qt gave back. Python owns it.
    """
    #  QDomNode QDomNode::replaceChild(const QDomNode &newChild, const
    #      QDomNode &oldChild)
    address = self.uglySide.call(
        'ritual_ZN8QDomNode12replaceChildERKS_S1_',
        self._valueOf(newChild), self._valueOf(oldChild),
    )
    return QDomNode._cuteOwning(address)

  @overload(THIS)
  def removeChild(self, oldChild: QDomNode) -> QDomNode:
    """
    Calls Qt's 'QDomNode QDomNode::removeChild(const QDomNode &oldChild)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#removeChild

    Parameters
    ----------

    oldChild : QDomNode
      Passed on as a value: Qt reads the C++ QDomNode, which stays Python's
      own.

    Returns
    -------

    QDomNode
      A new cute QDomNode around the copy Qt gave back. Python owns it.
    """
    #  QDomNode QDomNode::removeChild(const QDomNode &oldChild)
    address = self.uglySide.call(
        'ritual_ZN8QDomNode11removeChildERKS_', self._valueOf(oldChild),
    )
    return QDomNode._cuteOwning(address)

  @overload(THIS)
  def appendChild(self, newChild: QDomNode) -> QDomNode:
    """
    Calls Qt's 'QDomNode QDomNode::appendChild(const QDomNode &newChild)'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#appendChild

    Parameters
    ----------

    newChild : QDomNode
      Passed on as a value: Qt reads the C++ QDomNode, which stays Python's
      own.

    Returns
    -------

    QDomNode
      A new cute QDomNode around the copy Qt gave back. Python owns it.
    """
    #  QDomNode QDomNode::appendChild(const QDomNode &newChild)
    address = self.uglySide.call(
        'ritual_ZN8QDomNode11appendChildERKS_', self._valueOf(newChild),
    )
    return QDomNode._cuteOwning(address)

  def normalize(self) -> None:
    """
    Calls Qt's 'void QDomNode::normalize()'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#normalize
    """
    #  void QDomNode::normalize()
    self.uglySide.call('ritual_ZN8QDomNode9normalizeEv')

  def clear(self) -> None:
    """
    Calls Qt's 'void QDomNode::clear()'.

    Qt's own words: https://doc.qt.io/qt-6/qdomnode.html#clear
    """
    #  void QDomNode::clear()
    self.uglySide.call('ritual_ZN8QDomNode5clearEv')

  @staticmethod
  def save(*__, **_) -> Never:
    """
    Qt's 'void QDomNode::save(QTextStream &a0, int a1, EncodingPolicy a2)
    const': takes a type Python has no way to hand over yet.
    """
    raise NotImplementedError(
        "'QDomNode.save' has no cute function yet. Qt's 'void "
        "QDomNode::save(QTextStream &a0, int a1, EncodingPolicy a2) const': "
        "takes a type Python has no way to hand over yet.")
