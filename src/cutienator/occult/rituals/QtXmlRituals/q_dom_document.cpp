//  Written by dev_tooling.RitualGenerator from the records of QtXml/qdom.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtXml/qtxmlglobal.h>
#if QT_CONFIG(dom)
#if QT_CONFIG(dom)
#include <QtXml/qdom.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qanystringview.h>

//  QDomDocument::QDomDocument()
extern "C" Q_DECL_EXPORT
QDomDocument *ritual_ZN12QDomDocumentC1Ev() {
  return new QDomDocument();
}

//  QDomDocument::QDomDocument(const QString &name)
extern "C" Q_DECL_EXPORT
QDomDocument *ritual_ZN12QDomDocumentC1ERK7QString(const QString *name) {
  return new QDomDocument(*name);
}

//  QDomDocument::QDomDocument(const QDomDocumentType &doctype)
extern "C" Q_DECL_EXPORT
QDomDocument *ritual_ZN12QDomDocumentC1ERK16QDomDocumentType(
    const QDomDocumentType *doctype) {
  return new QDomDocument(*doctype);
}

//  QDomDocument::QDomDocument(const QDomDocument &document)
extern "C" Q_DECL_EXPORT
QDomDocument *ritual_ZN12QDomDocumentC1ERKS_(const QDomDocument *document) {
  return new QDomDocument(*document);
}

//  QDomDocument::~QDomDocument()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QDomDocumentD1Ev(QDomDocument *self) {
  delete self;
}

//  QDomElement QDomDocument::createElement(const QString &tagName)
extern "C" Q_DECL_EXPORT
QDomElement *ritual_ZN12QDomDocument13createElementERK7QString(
    QDomDocument *self,
    const QString *tagName) {
  return new QDomElement(self->createElement(*tagName));
}

//  QDomDocumentFragment QDomDocument::createDocumentFragment()
extern "C" Q_DECL_EXPORT
QDomDocumentFragment *ritual_ZN12QDomDocument22createDocumentFragmentEv(
    QDomDocument *self) {
  return new QDomDocumentFragment(self->createDocumentFragment());
}

//  QDomText QDomDocument::createTextNode(const QString &data)
extern "C" Q_DECL_EXPORT
QDomText *ritual_ZN12QDomDocument14createTextNodeERK7QString(
    QDomDocument *self,
    const QString *data) {
  return new QDomText(self->createTextNode(*data));
}

//  QDomComment QDomDocument::createComment(const QString &data)
extern "C" Q_DECL_EXPORT
QDomComment *ritual_ZN12QDomDocument13createCommentERK7QString(
    QDomDocument *self,
    const QString *data) {
  return new QDomComment(self->createComment(*data));
}

//  QDomCDATASection QDomDocument::createCDATASection(const QString &data)
extern "C" Q_DECL_EXPORT
QDomCDATASection *ritual_ZN12QDomDocument18createCDATASectionERK7QString(
    QDomDocument *self,
    const QString *data) {
  return new QDomCDATASection(self->createCDATASection(*data));
}

//  QDomProcessingInstruction QDomDocument::createProcessingInstruction(const
//      QString &target, const QString &data)
extern "C" Q_DECL_EXPORT
QDomProcessingInstruction *ritual_ZN12QDomDocument27createProcessingInstructionERK7QStringS2_(
    QDomDocument *self,
    const QString *target,
    const QString *data) {
  return new QDomProcessingInstruction(
      self->createProcessingInstruction(
          *target,
          *data));
}

//  QDomAttr QDomDocument::createAttribute(const QString &name)
extern "C" Q_DECL_EXPORT
QDomAttr *ritual_ZN12QDomDocument15createAttributeERK7QString(
    QDomDocument *self,
    const QString *name) {
  return new QDomAttr(self->createAttribute(*name));
}

//  QDomEntityReference QDomDocument::createEntityReference(const QString
//      &name)
extern "C" Q_DECL_EXPORT
QDomEntityReference *ritual_ZN12QDomDocument21createEntityReferenceERK7QString(
    QDomDocument *self,
    const QString *name) {
  return new QDomEntityReference(self->createEntityReference(*name));
}

//  QDomNodeList QDomDocument::elementsByTagName(const QString &tagname)
//      const
extern "C" Q_DECL_EXPORT
QDomNodeList *ritual_ZNK12QDomDocument17elementsByTagNameERK7QString(
    const QDomDocument *self,
    const QString *tagname) {
  return new QDomNodeList(self->elementsByTagName(*tagname));
}

//  QDomNode QDomDocument::importNode(const QDomNode &importedNode, bool
//      deep)
extern "C" Q_DECL_EXPORT
QDomNode *ritual_ZN12QDomDocument10importNodeERK8QDomNodeb(
    QDomDocument *self,
    const QDomNode *importedNode,
    bool deep) {
  return new QDomNode(self->importNode(*importedNode, deep));
}

//  QDomElement QDomDocument::createElementNS(const QString &nsURI, const
//      QString &qName)
extern "C" Q_DECL_EXPORT
QDomElement *ritual_ZN12QDomDocument15createElementNSERK7QStringS2_(
    QDomDocument *self,
    const QString *nsURI,
    const QString *qName) {
  return new QDomElement(self->createElementNS(*nsURI, *qName));
}

//  QDomAttr QDomDocument::createAttributeNS(const QString &nsURI, const
//      QString &qName)
extern "C" Q_DECL_EXPORT
QDomAttr *ritual_ZN12QDomDocument17createAttributeNSERK7QStringS2_(
    QDomDocument *self,
    const QString *nsURI,
    const QString *qName) {
  return new QDomAttr(self->createAttributeNS(*nsURI, *qName));
}

//  QDomNodeList QDomDocument::elementsByTagNameNS(const QString &nsURI,
//      const QString &localName)
extern "C" Q_DECL_EXPORT
QDomNodeList *ritual_ZN12QDomDocument19elementsByTagNameNSERK7QStringS2_(
    QDomDocument *self,
    const QString *nsURI,
    const QString *localName) {
  return new QDomNodeList(self->elementsByTagNameNS(*nsURI, *localName));
}

//  QDomElement QDomDocument::elementById(const QString &elementId)
extern "C" Q_DECL_EXPORT
QDomElement *ritual_ZN12QDomDocument11elementByIdERK7QString(
    QDomDocument *self,
    const QString *elementId) {
  return new QDomElement(self->elementById(*elementId));
}

//  QDomDocumentType QDomDocument::doctype() const
extern "C" Q_DECL_EXPORT
QDomDocumentType *ritual_ZNK12QDomDocument7doctypeEv(
    const QDomDocument *self) {
  return new QDomDocumentType(self->doctype());
}

//  QDomImplementation QDomDocument::implementation() const
extern "C" Q_DECL_EXPORT
QDomImplementation *ritual_ZNK12QDomDocument14implementationEv(
    const QDomDocument *self) {
  return new QDomImplementation(self->implementation());
}

//  QDomElement QDomDocument::documentElement() const
extern "C" Q_DECL_EXPORT
QDomElement *ritual_ZNK12QDomDocument15documentElementEv(
    const QDomDocument *self) {
  return new QDomElement(self->documentElement());
}

//  QDomNode::NodeType QDomDocument::nodeType() const
extern "C" Q_DECL_EXPORT
QDomNode::NodeType ritual_ZNK12QDomDocument8nodeTypeEv(
    const QDomDocument *self) {
  return self->nodeType();
}

#if QT_DEPRECATED_SINCE(6, 8)
//  bool QDomDocument::setContent(const QByteArray &text, bool
//      namespaceProcessing, QString *errorMsg, int *errorLine, int
//      *errorColumn)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QDomDocument10setContentERK10QByteArraybP7QStringPiS5_(
    QDomDocument *self,
    const QByteArray *text,
    bool namespaceProcessing,
    QString *errorMsg,
    int *errorLine,
    int *errorColumn) {
  return self->setContent(
      *text,
      namespaceProcessing,
      errorMsg,
      errorLine,
      errorColumn);
}
#endif  // QT_DEPRECATED_SINCE(6, 8)

#if QT_DEPRECATED_SINCE(6, 8)
//  bool QDomDocument::setContent(const QString &text, bool
//      namespaceProcessing, QString *errorMsg, int *errorLine, int
//      *errorColumn)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QDomDocument10setContentERK7QStringbPS0_PiS4_(
    QDomDocument *self,
    const QString *text,
    bool namespaceProcessing,
    QString *errorMsg,
    int *errorLine,
    int *errorColumn) {
  return self->setContent(
      *text,
      namespaceProcessing,
      errorMsg,
      errorLine,
      errorColumn);
}
#endif  // QT_DEPRECATED_SINCE(6, 8)

#if QT_DEPRECATED_SINCE(6, 8)
//  bool QDomDocument::setContent(QIODevice *dev, bool namespaceProcessing,
//      QString *errorMsg, int *errorLine, int *errorColumn)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QDomDocument10setContentEP9QIODevicebP7QStringPiS4_(
    QDomDocument *self,
    QIODevice *dev,
    bool namespaceProcessing,
    QString *errorMsg,
    int *errorLine,
    int *errorColumn) {
  return self->setContent(
      dev,
      namespaceProcessing,
      errorMsg,
      errorLine,
      errorColumn);
}
#endif  // QT_DEPRECATED_SINCE(6, 8)

#if QT_DEPRECATED_SINCE(6, 8)
//  bool QDomDocument::setContent(const QByteArray &text, QString *errorMsg,
//      int *errorLine, int *errorColumn)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QDomDocument10setContentERK10QByteArrayP7QStringPiS5_(
    QDomDocument *self,
    const QByteArray *text,
    QString *errorMsg,
    int *errorLine,
    int *errorColumn) {
  return self->setContent(*text, errorMsg, errorLine, errorColumn);
}
#endif  // QT_DEPRECATED_SINCE(6, 8)

#if QT_DEPRECATED_SINCE(6, 8)
//  bool QDomDocument::setContent(const QString &text, QString *errorMsg, int
//      *errorLine, int *errorColumn)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QDomDocument10setContentERK7QStringPS0_PiS4_(
    QDomDocument *self,
    const QString *text,
    QString *errorMsg,
    int *errorLine,
    int *errorColumn) {
  return self->setContent(*text, errorMsg, errorLine, errorColumn);
}
#endif  // QT_DEPRECATED_SINCE(6, 8)

#if QT_DEPRECATED_SINCE(6, 8)
//  bool QDomDocument::setContent(QIODevice *dev, QString *errorMsg, int
//      *errorLine, int *errorColumn)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QDomDocument10setContentEP9QIODeviceP7QStringPiS4_(
    QDomDocument *self,
    QIODevice *dev,
    QString *errorMsg,
    int *errorLine,
    int *errorColumn) {
  return self->setContent(dev, errorMsg, errorLine, errorColumn);
}
#endif  // QT_DEPRECATED_SINCE(6, 8)

#if QT_DEPRECATED_SINCE(6, 8)
//  bool QDomDocument::setContent(QXmlStreamReader *reader, bool
//      namespaceProcessing, QString *errorMsg, int *errorLine, int
//      *errorColumn)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QDomDocument10setContentEP16QXmlStreamReaderbP7QStringPiS4_(
    QDomDocument *self,
    QXmlStreamReader *reader,
    bool namespaceProcessing,
    QString *errorMsg,
    int *errorLine,
    int *errorColumn) {
  return self->setContent(
      reader,
      namespaceProcessing,
      errorMsg,
      errorLine,
      errorColumn);
}
#endif  // QT_DEPRECATED_SINCE(6, 8)

//  ParseResult QDomDocument::setContent(QAnyStringView data, ParseOptions
//      options)
extern "C" Q_DECL_EXPORT
QDomDocument::ParseResult *ritual_ZN12QDomDocument10setContentE14QAnyStringView6QFlagsINS_11ParseOptionEE(
    QDomDocument *self,
    const QString *data,
    int options) {
  return new QDomDocument::ParseResult(
      self->setContent(
          QAnyStringView(*data),
          QFlags<QDomDocument::ParseOption>::fromInt(options)));
}

//  ParseResult QDomDocument::setContent(QIODevice *device, ParseOptions
//      options)
extern "C" Q_DECL_EXPORT
QDomDocument::ParseResult *ritual_ZN12QDomDocument10setContentEP9QIODevice6QFlagsINS_11ParseOptionEE(
    QDomDocument *self,
    QIODevice *device,
    int options) {
  return new QDomDocument::ParseResult(
      self->setContent(
          device,
          QFlags<QDomDocument::ParseOption>::fromInt(options)));
}

//  ParseResult QDomDocument::setContent(QXmlStreamReader *reader,
//      ParseOptions options)
extern "C" Q_DECL_EXPORT
QDomDocument::ParseResult *ritual_ZN12QDomDocument10setContentEP16QXmlStreamReader6QFlagsINS_11ParseOptionEE(
    QDomDocument *self,
    QXmlStreamReader *reader,
    int options) {
  return new QDomDocument::ParseResult(
      self->setContent(
          reader,
          QFlags<QDomDocument::ParseOption>::fromInt(options)));
}

//  QString QDomDocument::toString(int indent) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QDomDocument8toStringEi(
    const QDomDocument *self,
    int indent) {
  return new QString(self->toString(indent));
}

//  QByteArray QDomDocument::toByteArray(int indent) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK12QDomDocument11toByteArrayEi(
    const QDomDocument *self,
    int indent) {
  return new QByteArray(self->toByteArray(indent));
}

//  ParseResult QDomDocument::setContentImpl(const QByteArray &data,
//      ParseOptions options)
extern "C" Q_DECL_EXPORT
QDomDocument::ParseResult *ritual_ZN12QDomDocument14setContentImplERK10QByteArray6QFlagsINS_11ParseOptionEE(
    QDomDocument *self,
    const QByteArray *data,
    int options) {
  return new QDomDocument::ParseResult(
      self->setContentImpl(
          *data,
          QFlags<QDomDocument::ParseOption>::fromInt(options)));
}

//  QDomDocument::QDomDocument(QDomDocumentPrivate *a0)
extern "C" Q_DECL_EXPORT
QDomDocument *ritual_ZN12QDomDocumentC1EP19QDomDocumentPrivate(
    QDomDocumentPrivate *a0) {
  return new QDomDocument(a0);
}

#endif  // QT_CONFIG(dom)
#endif  // QT_CONFIG(dom)
