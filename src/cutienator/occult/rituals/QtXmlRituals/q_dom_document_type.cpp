//  Written by dev_tooling.RitualGenerator from the records of QtXml/qdom.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtXml/qtxmlglobal.h>
#if QT_CONFIG(dom)
#if QT_CONFIG(dom)
#include <QtXml/qdom.h>
#include <QtCore/qstring.h>

//  QDomDocumentType::QDomDocumentType()
extern "C" Q_DECL_EXPORT
QDomDocumentType *ritual_ZN16QDomDocumentTypeC1Ev() {
  return new QDomDocumentType();
}

//  QDomDocumentType::QDomDocumentType(const QDomDocumentType &documentType)
extern "C" Q_DECL_EXPORT
QDomDocumentType *ritual_ZN16QDomDocumentTypeC1ERKS_(
    const QDomDocumentType *documentType) {
  return new QDomDocumentType(*documentType);
}

//  QDomDocumentType &QDomDocumentType::operator=(const QDomDocumentType
//      &other)
extern "C" Q_DECL_EXPORT
QDomDocumentType *ritual_ZN16QDomDocumentTypeaSERKS_(
    QDomDocumentType *self,
    const QDomDocumentType *other) {
  return &(self->operator=(*other));
}

//  QString QDomDocumentType::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QDomDocumentType4nameEv(const QDomDocumentType *self) {
  return new QString(self->name());
}

//  QDomNamedNodeMap QDomDocumentType::entities() const
extern "C" Q_DECL_EXPORT
QDomNamedNodeMap *ritual_ZNK16QDomDocumentType8entitiesEv(
    const QDomDocumentType *self) {
  return new QDomNamedNodeMap(self->entities());
}

//  QDomNamedNodeMap QDomDocumentType::notations() const
extern "C" Q_DECL_EXPORT
QDomNamedNodeMap *ritual_ZNK16QDomDocumentType9notationsEv(
    const QDomDocumentType *self) {
  return new QDomNamedNodeMap(self->notations());
}

//  QString QDomDocumentType::publicId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QDomDocumentType8publicIdEv(
    const QDomDocumentType *self) {
  return new QString(self->publicId());
}

//  QString QDomDocumentType::systemId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QDomDocumentType8systemIdEv(
    const QDomDocumentType *self) {
  return new QString(self->systemId());
}

//  QString QDomDocumentType::internalSubset() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK16QDomDocumentType14internalSubsetEv(
    const QDomDocumentType *self) {
  return new QString(self->internalSubset());
}

//  QDomNode::NodeType QDomDocumentType::nodeType() const
extern "C" Q_DECL_EXPORT
QDomNode::NodeType ritual_ZNK16QDomDocumentType8nodeTypeEv(
    const QDomDocumentType *self) {
  return self->nodeType();
}

//  QDomDocumentType::QDomDocumentType(QDomDocumentTypePrivate *a0)
extern "C" Q_DECL_EXPORT
QDomDocumentType *ritual_ZN16QDomDocumentTypeC1EP23QDomDocumentTypePrivate(
    QDomDocumentTypePrivate *a0) {
  return new QDomDocumentType(a0);
}

//  QDomDocumentType::~QDomDocumentType()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDomDocumentTypeD1Ev(QDomDocumentType *self) {
  delete self;
}

#endif  // QT_CONFIG(dom)
#endif  // QT_CONFIG(dom)
