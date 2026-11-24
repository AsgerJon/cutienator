//  Written by dev_tooling.RitualGenerator from the records of QtXml/qdom.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtXml/qtxmlglobal.h>
#if QT_CONFIG(dom)
#if QT_CONFIG(dom)
#include <QtXml/qdom.h>
#include <QtCore/qstring.h>

//  QDomNode::QDomNode()
extern "C" Q_DECL_EXPORT
QDomNode *ritual_ZN8QDomNodeC1Ev() {
  return new QDomNode();
}

//  QDomNode::QDomNode(const QDomNode &node)
extern "C" Q_DECL_EXPORT
QDomNode *ritual_ZN8QDomNodeC1ERKS_(const QDomNode *node) {
  return new QDomNode(*node);
}

//  bool QDomNode::operator==(const QDomNode &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QDomNodeeqERKS_(
    const QDomNode *self,
    const QDomNode *other) {
  return self->operator==(*other);
}

//  bool QDomNode::operator!=(const QDomNode &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QDomNodeneERKS_(
    const QDomNode *self,
    const QDomNode *other) {
  return self->operator!=(*other);
}

//  QDomNode::~QDomNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QDomNodeD1Ev(QDomNode *self) {
  delete self;
}

//  QDomNode QDomNode::insertBefore(const QDomNode &newChild, const QDomNode
//      &refChild)
extern "C" Q_DECL_EXPORT
QDomNode *ritual_ZN8QDomNode12insertBeforeERKS_S1_(
    QDomNode *self,
    const QDomNode *newChild,
    const QDomNode *refChild) {
  return new QDomNode(self->insertBefore(*newChild, *refChild));
}

//  QDomNode QDomNode::insertAfter(const QDomNode &newChild, const QDomNode
//      &refChild)
extern "C" Q_DECL_EXPORT
QDomNode *ritual_ZN8QDomNode11insertAfterERKS_S1_(
    QDomNode *self,
    const QDomNode *newChild,
    const QDomNode *refChild) {
  return new QDomNode(self->insertAfter(*newChild, *refChild));
}

//  QDomNode QDomNode::replaceChild(const QDomNode &newChild, const QDomNode
//      &oldChild)
extern "C" Q_DECL_EXPORT
QDomNode *ritual_ZN8QDomNode12replaceChildERKS_S1_(
    QDomNode *self,
    const QDomNode *newChild,
    const QDomNode *oldChild) {
  return new QDomNode(self->replaceChild(*newChild, *oldChild));
}

//  QDomNode QDomNode::removeChild(const QDomNode &oldChild)
extern "C" Q_DECL_EXPORT
QDomNode *ritual_ZN8QDomNode11removeChildERKS_(
    QDomNode *self,
    const QDomNode *oldChild) {
  return new QDomNode(self->removeChild(*oldChild));
}

//  QDomNode QDomNode::appendChild(const QDomNode &newChild)
extern "C" Q_DECL_EXPORT
QDomNode *ritual_ZN8QDomNode11appendChildERKS_(
    QDomNode *self,
    const QDomNode *newChild) {
  return new QDomNode(self->appendChild(*newChild));
}

//  bool QDomNode::hasChildNodes() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QDomNode13hasChildNodesEv(const QDomNode *self) {
  return self->hasChildNodes();
}

//  QDomNode QDomNode::cloneNode(bool deep) const
extern "C" Q_DECL_EXPORT
QDomNode *ritual_ZNK8QDomNode9cloneNodeEb(const QDomNode *self, bool deep) {
  return new QDomNode(self->cloneNode(deep));
}

//  void QDomNode::normalize()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QDomNode9normalizeEv(QDomNode *self) {
  self->normalize();
}

//  bool QDomNode::isSupported(const QString &feature, const QString
//      &version) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QDomNode11isSupportedERK7QStringS2_(
    const QDomNode *self,
    const QString *feature,
    const QString *version) {
  return self->isSupported(*feature, *version);
}

//  QString QDomNode::nodeName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QDomNode8nodeNameEv(const QDomNode *self) {
  return new QString(self->nodeName());
}

//  NodeType QDomNode::nodeType() const
extern "C" Q_DECL_EXPORT
QDomNode::NodeType ritual_ZNK8QDomNode8nodeTypeEv(const QDomNode *self) {
  return self->nodeType();
}

//  QDomNode QDomNode::parentNode() const
extern "C" Q_DECL_EXPORT
QDomNode *ritual_ZNK8QDomNode10parentNodeEv(const QDomNode *self) {
  return new QDomNode(self->parentNode());
}

//  QDomNodeList QDomNode::childNodes() const
extern "C" Q_DECL_EXPORT
QDomNodeList *ritual_ZNK8QDomNode10childNodesEv(const QDomNode *self) {
  return new QDomNodeList(self->childNodes());
}

//  QDomNode QDomNode::firstChild() const
extern "C" Q_DECL_EXPORT
QDomNode *ritual_ZNK8QDomNode10firstChildEv(const QDomNode *self) {
  return new QDomNode(self->firstChild());
}

//  QDomNode QDomNode::lastChild() const
extern "C" Q_DECL_EXPORT
QDomNode *ritual_ZNK8QDomNode9lastChildEv(const QDomNode *self) {
  return new QDomNode(self->lastChild());
}

//  QDomNode QDomNode::previousSibling() const
extern "C" Q_DECL_EXPORT
QDomNode *ritual_ZNK8QDomNode15previousSiblingEv(const QDomNode *self) {
  return new QDomNode(self->previousSibling());
}

//  QDomNode QDomNode::nextSibling() const
extern "C" Q_DECL_EXPORT
QDomNode *ritual_ZNK8QDomNode11nextSiblingEv(const QDomNode *self) {
  return new QDomNode(self->nextSibling());
}

//  QDomNamedNodeMap QDomNode::attributes() const
extern "C" Q_DECL_EXPORT
QDomNamedNodeMap *ritual_ZNK8QDomNode10attributesEv(const QDomNode *self) {
  return new QDomNamedNodeMap(self->attributes());
}

//  QDomDocument QDomNode::ownerDocument() const
extern "C" Q_DECL_EXPORT
QDomDocument *ritual_ZNK8QDomNode13ownerDocumentEv(const QDomNode *self) {
  return new QDomDocument(self->ownerDocument());
}

//  QString QDomNode::namespaceURI() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QDomNode12namespaceURIEv(const QDomNode *self) {
  return new QString(self->namespaceURI());
}

//  QString QDomNode::localName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QDomNode9localNameEv(const QDomNode *self) {
  return new QString(self->localName());
}

//  bool QDomNode::hasAttributes() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QDomNode13hasAttributesEv(const QDomNode *self) {
  return self->hasAttributes();
}

//  QString QDomNode::nodeValue() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QDomNode9nodeValueEv(const QDomNode *self) {
  return new QString(self->nodeValue());
}

//  void QDomNode::setNodeValue(const QString &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QDomNode12setNodeValueERK7QString(
    QDomNode *self,
    const QString *value) {
  self->setNodeValue(*value);
}

//  QString QDomNode::prefix() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QDomNode6prefixEv(const QDomNode *self) {
  return new QString(self->prefix());
}

//  void QDomNode::setPrefix(const QString &pre)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QDomNode9setPrefixERK7QString(
    QDomNode *self,
    const QString *pre) {
  self->setPrefix(*pre);
}

//  bool QDomNode::isAttr() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QDomNode6isAttrEv(const QDomNode *self) {
  return self->isAttr();
}

//  bool QDomNode::isCDATASection() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QDomNode14isCDATASectionEv(const QDomNode *self) {
  return self->isCDATASection();
}

//  bool QDomNode::isDocumentFragment() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QDomNode18isDocumentFragmentEv(const QDomNode *self) {
  return self->isDocumentFragment();
}

//  bool QDomNode::isDocument() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QDomNode10isDocumentEv(const QDomNode *self) {
  return self->isDocument();
}

//  bool QDomNode::isDocumentType() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QDomNode14isDocumentTypeEv(const QDomNode *self) {
  return self->isDocumentType();
}

//  bool QDomNode::isElement() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QDomNode9isElementEv(const QDomNode *self) {
  return self->isElement();
}

//  bool QDomNode::isEntityReference() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QDomNode17isEntityReferenceEv(const QDomNode *self) {
  return self->isEntityReference();
}

//  bool QDomNode::isText() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QDomNode6isTextEv(const QDomNode *self) {
  return self->isText();
}

//  bool QDomNode::isEntity() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QDomNode8isEntityEv(const QDomNode *self) {
  return self->isEntity();
}

//  bool QDomNode::isNotation() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QDomNode10isNotationEv(const QDomNode *self) {
  return self->isNotation();
}

//  bool QDomNode::isProcessingInstruction() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QDomNode23isProcessingInstructionEv(const QDomNode *self) {
  return self->isProcessingInstruction();
}

//  bool QDomNode::isCharacterData() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QDomNode15isCharacterDataEv(const QDomNode *self) {
  return self->isCharacterData();
}

//  bool QDomNode::isComment() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QDomNode9isCommentEv(const QDomNode *self) {
  return self->isComment();
}

//  QDomNode QDomNode::namedItem(const QString &name) const
extern "C" Q_DECL_EXPORT
QDomNode *ritual_ZNK8QDomNode9namedItemERK7QString(
    const QDomNode *self,
    const QString *name) {
  return new QDomNode(self->namedItem(*name));
}

//  bool QDomNode::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QDomNode6isNullEv(const QDomNode *self) {
  return self->isNull();
}

//  void QDomNode::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QDomNode5clearEv(QDomNode *self) {
  self->clear();
}

//  QDomAttr QDomNode::toAttr() const
extern "C" Q_DECL_EXPORT
QDomAttr *ritual_ZNK8QDomNode6toAttrEv(const QDomNode *self) {
  return new QDomAttr(self->toAttr());
}

//  QDomCDATASection QDomNode::toCDATASection() const
extern "C" Q_DECL_EXPORT
QDomCDATASection *ritual_ZNK8QDomNode14toCDATASectionEv(
    const QDomNode *self) {
  return new QDomCDATASection(self->toCDATASection());
}

//  QDomDocumentFragment QDomNode::toDocumentFragment() const
extern "C" Q_DECL_EXPORT
QDomDocumentFragment *ritual_ZNK8QDomNode18toDocumentFragmentEv(
    const QDomNode *self) {
  return new QDomDocumentFragment(self->toDocumentFragment());
}

//  QDomDocument QDomNode::toDocument() const
extern "C" Q_DECL_EXPORT
QDomDocument *ritual_ZNK8QDomNode10toDocumentEv(const QDomNode *self) {
  return new QDomDocument(self->toDocument());
}

//  QDomDocumentType QDomNode::toDocumentType() const
extern "C" Q_DECL_EXPORT
QDomDocumentType *ritual_ZNK8QDomNode14toDocumentTypeEv(
    const QDomNode *self) {
  return new QDomDocumentType(self->toDocumentType());
}

//  QDomElement QDomNode::toElement() const
extern "C" Q_DECL_EXPORT
QDomElement *ritual_ZNK8QDomNode9toElementEv(const QDomNode *self) {
  return new QDomElement(self->toElement());
}

//  QDomEntityReference QDomNode::toEntityReference() const
extern "C" Q_DECL_EXPORT
QDomEntityReference *ritual_ZNK8QDomNode17toEntityReferenceEv(
    const QDomNode *self) {
  return new QDomEntityReference(self->toEntityReference());
}

//  QDomText QDomNode::toText() const
extern "C" Q_DECL_EXPORT
QDomText *ritual_ZNK8QDomNode6toTextEv(const QDomNode *self) {
  return new QDomText(self->toText());
}

//  QDomEntity QDomNode::toEntity() const
extern "C" Q_DECL_EXPORT
QDomEntity *ritual_ZNK8QDomNode8toEntityEv(const QDomNode *self) {
  return new QDomEntity(self->toEntity());
}

//  QDomNotation QDomNode::toNotation() const
extern "C" Q_DECL_EXPORT
QDomNotation *ritual_ZNK8QDomNode10toNotationEv(const QDomNode *self) {
  return new QDomNotation(self->toNotation());
}

//  QDomProcessingInstruction QDomNode::toProcessingInstruction() const
extern "C" Q_DECL_EXPORT
QDomProcessingInstruction *ritual_ZNK8QDomNode23toProcessingInstructionEv(
    const QDomNode *self) {
  return new QDomProcessingInstruction(self->toProcessingInstruction());
}

//  QDomCharacterData QDomNode::toCharacterData() const
extern "C" Q_DECL_EXPORT
QDomCharacterData *ritual_ZNK8QDomNode15toCharacterDataEv(
    const QDomNode *self) {
  return new QDomCharacterData(self->toCharacterData());
}

//  QDomComment QDomNode::toComment() const
extern "C" Q_DECL_EXPORT
QDomComment *ritual_ZNK8QDomNode9toCommentEv(const QDomNode *self) {
  return new QDomComment(self->toComment());
}

//  QDomElement QDomNode::firstChildElement(const QString &tagName, const
//      QString &namespaceURI) const
extern "C" Q_DECL_EXPORT
QDomElement *ritual_ZNK8QDomNode17firstChildElementERK7QStringS2_(
    const QDomNode *self,
    const QString *tagName,
    const QString *namespaceURI) {
  return new QDomElement(self->firstChildElement(*tagName, *namespaceURI));
}

//  QDomElement QDomNode::lastChildElement(const QString &tagName, const
//      QString &namespaceURI) const
extern "C" Q_DECL_EXPORT
QDomElement *ritual_ZNK8QDomNode16lastChildElementERK7QStringS2_(
    const QDomNode *self,
    const QString *tagName,
    const QString *namespaceURI) {
  return new QDomElement(self->lastChildElement(*tagName, *namespaceURI));
}

//  QDomElement QDomNode::previousSiblingElement(const QString &tagName,
//      const QString &namespaceURI) const
extern "C" Q_DECL_EXPORT
QDomElement *ritual_ZNK8QDomNode22previousSiblingElementERK7QStringS2_(
    const QDomNode *self,
    const QString *tagName,
    const QString *namespaceURI) {
  return new QDomElement(
      self->previousSiblingElement(
          *tagName,
          *namespaceURI));
}

//  QDomElement QDomNode::nextSiblingElement(const QString &taName, const
//      QString &namespaceURI) const
extern "C" Q_DECL_EXPORT
QDomElement *ritual_ZNK8QDomNode18nextSiblingElementERK7QStringS2_(
    const QDomNode *self,
    const QString *taName,
    const QString *namespaceURI) {
  return new QDomElement(self->nextSiblingElement(*taName, *namespaceURI));
}

//  int QDomNode::lineNumber() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QDomNode10lineNumberEv(const QDomNode *self) {
  return self->lineNumber();
}

//  int QDomNode::columnNumber() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK8QDomNode12columnNumberEv(const QDomNode *self) {
  return self->columnNumber();
}

//  QDomNode::QDomNode(QDomNodePrivate *a0)
extern "C" Q_DECL_EXPORT
QDomNode *ritual_ZN8QDomNodeC1EP15QDomNodePrivate(QDomNodePrivate *a0) {
  return new QDomNode(a0);
}

#endif  // QT_CONFIG(dom)
#endif  // QT_CONFIG(dom)
