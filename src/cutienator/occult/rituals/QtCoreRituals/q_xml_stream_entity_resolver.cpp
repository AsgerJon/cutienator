//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qxmlstream.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qxmlstream.h>
#include <QtCore/qstring.h>

//  QXmlStreamEntityResolver::QXmlStreamEntityResolver()
extern "C" Q_DECL_EXPORT
QXmlStreamEntityResolver *ritual_ZN24QXmlStreamEntityResolverC1Ev() {
  return new QXmlStreamEntityResolver();
}

//  QXmlStreamEntityResolver::~QXmlStreamEntityResolver()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QXmlStreamEntityResolverD1Ev(
    QXmlStreamEntityResolver *self) {
  delete self;
}

//  QString QXmlStreamEntityResolver::resolveEntity(const QString &publicId,
//      const QString &systemId)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QXmlStreamEntityResolver13resolveEntityERK7QStringS2_(
    QXmlStreamEntityResolver *self,
    const QString *publicId,
    const QString *systemId) {
  return new QString(self->resolveEntity(*publicId, *systemId));
}

//  QString QXmlStreamEntityResolver::resolveUndeclaredEntity(const QString
//      &name)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QXmlStreamEntityResolver23resolveUndeclaredEntityERK7QString(
    QXmlStreamEntityResolver *self,
    const QString *name) {
  return new QString(self->resolveUndeclaredEntity(*name));
}
