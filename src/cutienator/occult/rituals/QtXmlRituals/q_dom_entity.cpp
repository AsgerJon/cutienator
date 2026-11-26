//  Written by dev_tooling.RitualGenerator from the records of QtXml/qdom.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtXml/qtxmlglobal.h>
#if QT_CONFIG(dom)
#if QT_CONFIG(dom)
#include <QtXml/qdom.h>
#include <QtCore/qstring.h>

//  QDomEntity::QDomEntity()
extern "C" Q_DECL_EXPORT
QDomEntity *ritual_ZN10QDomEntityC1Ev() {
  return new QDomEntity();
}

//  QDomEntity::QDomEntity(const QDomEntity &entity)
extern "C" Q_DECL_EXPORT
QDomEntity *ritual_ZN10QDomEntityC1ERKS_(const QDomEntity *entity) {
  return new QDomEntity(*entity);
}

//  QDomEntity &QDomEntity::operator=(const QDomEntity &other)
extern "C" Q_DECL_EXPORT
QDomEntity *ritual_ZN10QDomEntityaSERKS_(
    QDomEntity *self,
    const QDomEntity *other) {
  return &(self->operator=(*other));
}

//  QString QDomEntity::publicId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QDomEntity8publicIdEv(const QDomEntity *self) {
  return new QString(self->publicId());
}

//  QString QDomEntity::systemId() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QDomEntity8systemIdEv(const QDomEntity *self) {
  return new QString(self->systemId());
}

//  QString QDomEntity::notationName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QDomEntity12notationNameEv(const QDomEntity *self) {
  return new QString(self->notationName());
}

//  QDomNode::NodeType QDomEntity::nodeType() const
extern "C" Q_DECL_EXPORT
QDomNode::NodeType ritual_ZNK10QDomEntity8nodeTypeEv(
    const QDomEntity *self) {
  return self->nodeType();
}

//  QDomEntity::QDomEntity(QDomEntityPrivate *a0)
extern "C" Q_DECL_EXPORT
QDomEntity *ritual_ZN10QDomEntityC1EP17QDomEntityPrivate(
    QDomEntityPrivate *a0) {
  return new QDomEntity(a0);
}

//  QDomEntity::~QDomEntity()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QDomEntityD1Ev(QDomEntity *self) {
  delete self;
}

#endif  // QT_CONFIG(dom)
#endif  // QT_CONFIG(dom)
