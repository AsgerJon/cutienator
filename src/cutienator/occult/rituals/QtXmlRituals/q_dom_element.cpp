//  Written by dev_tooling.RitualGenerator from the records of QtXml/qdom.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtXml/qtxmlglobal.h>
#if QT_CONFIG(dom)
#include <QtXml/qdom.h>
#include <QtCore/qstring.h>

//  QDomElement::QDomElement()
extern "C" Q_DECL_EXPORT
QDomElement *ritual_ZN11QDomElementC1Ev() {
  return new QDomElement();
}

//  QDomElement::QDomElement(const QDomElement &element)
extern "C" Q_DECL_EXPORT
QDomElement *ritual_ZN11QDomElementC1ERKS_(const QDomElement *element) {
  return new QDomElement(*element);
}

//  QString QDomElement::attribute(const QString &name, const QString
//      &defValue) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QDomElement9attributeERK7QStringS2_(
    const QDomElement *self,
    const QString *name,
    const QString *defValue) {
  return new QString(self->attribute(*name, *defValue));
}

//  void QDomElement::setAttribute(const QString &name, const QString &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDomElement12setAttributeERK7QStringS2_(
    QDomElement *self,
    const QString *name,
    const QString *value) {
  self->setAttribute(*name, *value);
}

//  void QDomElement::setAttribute(const QString &name, qlonglong value)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDomElement12setAttributeERK7QStringx(
    QDomElement *self,
    const QString *name,
    qlonglong value) {
  self->setAttribute(*name, value);
}

//  void QDomElement::setAttribute(const QString &name, qulonglong value)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDomElement12setAttributeERK7QStringy(
    QDomElement *self,
    const QString *name,
    qulonglong value) {
  self->setAttribute(*name, value);
}

//  void QDomElement::setAttribute(const QString &name, int value)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDomElement12setAttributeERK7QStringi(
    QDomElement *self,
    const QString *name,
    int value) {
  self->setAttribute(*name, value);
}

//  void QDomElement::setAttribute(const QString &name, uint value)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDomElement12setAttributeERK7QStringj(
    QDomElement *self,
    const QString *name,
    uint value) {
  self->setAttribute(*name, value);
}

//  void QDomElement::setAttribute(const QString &name, float value)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDomElement12setAttributeERK7QStringf(
    QDomElement *self,
    const QString *name,
    float value) {
  self->setAttribute(*name, value);
}

//  void QDomElement::setAttribute(const QString &name, double value)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDomElement12setAttributeERK7QStringd(
    QDomElement *self,
    const QString *name,
    double value) {
  self->setAttribute(*name, value);
}

//  void QDomElement::removeAttribute(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDomElement15removeAttributeERK7QString(
    QDomElement *self,
    const QString *name) {
  self->removeAttribute(*name);
}

//  QDomAttr QDomElement::attributeNode(const QString &name)
extern "C" Q_DECL_EXPORT
QDomAttr *ritual_ZN11QDomElement13attributeNodeERK7QString(
    QDomElement *self,
    const QString *name) {
  return new QDomAttr(self->attributeNode(*name));
}

//  QDomAttr QDomElement::setAttributeNode(const QDomAttr &newAttr)
extern "C" Q_DECL_EXPORT
QDomAttr *ritual_ZN11QDomElement16setAttributeNodeERK8QDomAttr(
    QDomElement *self,
    const QDomAttr *newAttr) {
  return new QDomAttr(self->setAttributeNode(*newAttr));
}

//  QDomAttr QDomElement::removeAttributeNode(const QDomAttr &oldAttr)
extern "C" Q_DECL_EXPORT
QDomAttr *ritual_ZN11QDomElement19removeAttributeNodeERK8QDomAttr(
    QDomElement *self,
    const QDomAttr *oldAttr) {
  return new QDomAttr(self->removeAttributeNode(*oldAttr));
}

//  QDomNodeList QDomElement::elementsByTagName(const QString &tagname) const
extern "C" Q_DECL_EXPORT
QDomNodeList *ritual_ZNK11QDomElement17elementsByTagNameERK7QString(
    const QDomElement *self,
    const QString *tagname) {
  return new QDomNodeList(self->elementsByTagName(*tagname));
}

//  bool QDomElement::hasAttribute(const QString &name) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QDomElement12hasAttributeERK7QString(
    const QDomElement *self,
    const QString *name) {
  return self->hasAttribute(*name);
}

//  QString QDomElement::attributeNS(const QString &nsURI, const QString
//      &localName, const QString &defValue) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QDomElement11attributeNSERK7QStringS2_S2_(
    const QDomElement *self,
    const QString *nsURI,
    const QString *localName,
    const QString *defValue) {
  return new QString(self->attributeNS(*nsURI, *localName, *defValue));
}

//  void QDomElement::setAttributeNS(const QString &nsURI, const QString
//      &qName, const QString &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDomElement14setAttributeNSERK7QStringS2_S2_(
    QDomElement *self,
    const QString *nsURI,
    const QString *qName,
    const QString *value) {
  self->setAttributeNS(*nsURI, *qName, *value);
}

//  void QDomElement::setAttributeNS(const QString &nsURI, const QString
//      &qName, int value)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDomElement14setAttributeNSERK7QStringS2_i(
    QDomElement *self,
    const QString *nsURI,
    const QString *qName,
    int value) {
  self->setAttributeNS(*nsURI, *qName, value);
}

//  void QDomElement::setAttributeNS(const QString &nsURI, const QString
//      &qName, uint value)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDomElement14setAttributeNSERK7QStringS2_j(
    QDomElement *self,
    const QString *nsURI,
    const QString *qName,
    uint value) {
  self->setAttributeNS(*nsURI, *qName, value);
}

//  void QDomElement::setAttributeNS(const QString &nsURI, const QString
//      &qName, qlonglong value)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDomElement14setAttributeNSERK7QStringS2_x(
    QDomElement *self,
    const QString *nsURI,
    const QString *qName,
    qlonglong value) {
  self->setAttributeNS(*nsURI, *qName, value);
}

//  void QDomElement::setAttributeNS(const QString &nsURI, const QString
//      &qName, qulonglong value)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDomElement14setAttributeNSERK7QStringS2_y(
    QDomElement *self,
    const QString *nsURI,
    const QString *qName,
    qulonglong value) {
  self->setAttributeNS(*nsURI, *qName, value);
}

//  void QDomElement::setAttributeNS(const QString &nsURI, const QString
//      &qName, double value)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDomElement14setAttributeNSERK7QStringS2_d(
    QDomElement *self,
    const QString *nsURI,
    const QString *qName,
    double value) {
  self->setAttributeNS(*nsURI, *qName, value);
}

//  void QDomElement::removeAttributeNS(const QString &nsURI, const QString
//      &localName)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDomElement17removeAttributeNSERK7QStringS2_(
    QDomElement *self,
    const QString *nsURI,
    const QString *localName) {
  self->removeAttributeNS(*nsURI, *localName);
}

//  QDomAttr QDomElement::attributeNodeNS(const QString &nsURI, const QString
//      &localName)
extern "C" Q_DECL_EXPORT
QDomAttr *ritual_ZN11QDomElement15attributeNodeNSERK7QStringS2_(
    QDomElement *self,
    const QString *nsURI,
    const QString *localName) {
  return new QDomAttr(self->attributeNodeNS(*nsURI, *localName));
}

//  QDomAttr QDomElement::setAttributeNodeNS(const QDomAttr &newAttr)
extern "C" Q_DECL_EXPORT
QDomAttr *ritual_ZN11QDomElement18setAttributeNodeNSERK8QDomAttr(
    QDomElement *self,
    const QDomAttr *newAttr) {
  return new QDomAttr(self->setAttributeNodeNS(*newAttr));
}

//  QDomNodeList QDomElement::elementsByTagNameNS(const QString &nsURI, const
//      QString &localName) const
extern "C" Q_DECL_EXPORT
QDomNodeList *ritual_ZNK11QDomElement19elementsByTagNameNSERK7QStringS2_(
    const QDomElement *self,
    const QString *nsURI,
    const QString *localName) {
  return new QDomNodeList(self->elementsByTagNameNS(*nsURI, *localName));
}

//  bool QDomElement::hasAttributeNS(const QString &nsURI, const QString
//      &localName) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QDomElement14hasAttributeNSERK7QStringS2_(
    const QDomElement *self,
    const QString *nsURI,
    const QString *localName) {
  return self->hasAttributeNS(*nsURI, *localName);
}

//  QString QDomElement::tagName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QDomElement7tagNameEv(const QDomElement *self) {
  return new QString(self->tagName());
}

//  void QDomElement::setTagName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDomElement10setTagNameERK7QString(
    QDomElement *self,
    const QString *name) {
  self->setTagName(*name);
}

//  QDomNamedNodeMap QDomElement::attributes() const
extern "C" Q_DECL_EXPORT
QDomNamedNodeMap *ritual_ZNK11QDomElement10attributesEv(
    const QDomElement *self) {
  return new QDomNamedNodeMap(self->attributes());
}

//  QDomNode::NodeType QDomElement::nodeType() const
extern "C" Q_DECL_EXPORT
QDomNode::NodeType ritual_ZNK11QDomElement8nodeTypeEv(
    const QDomElement *self) {
  return self->nodeType();
}

//  QString QDomElement::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QDomElement4textEv(const QDomElement *self) {
  return new QString(self->text());
}

//  QDomElement::QDomElement(QDomElementPrivate *a0)
extern "C" Q_DECL_EXPORT
QDomElement *ritual_ZN11QDomElementC1EP18QDomElementPrivate(
    QDomElementPrivate *a0) {
  return new QDomElement(a0);
}

//  QDomElement::~QDomElement()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QDomElementD1Ev(QDomElement *self) {
  delete self;
}

#endif  // QT_CONFIG(dom)
