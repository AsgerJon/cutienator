//  Written by dev_tooling.RitualGenerator from the records of
//  QtCoap/qcoapresourcediscoveryreply.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtCoap/qcoapresourcediscoveryreply.h>
#include <QtCore/qstring.h>
#include <QtCoap/qcoapresource.h>
#include <QtCoap/qcoaprequest.h>
#include <QtCore/qlist.h>

//  const QMetaObject *QCoapResourceDiscoveryReply::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QCoapResourceDiscoveryReply10metaObjectEv(
    const QCoapResourceDiscoveryReply *self) {
  return self->metaObject();
}

//  QString QCoapResourceDiscoveryReply::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN27QCoapResourceDiscoveryReply2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QCoapResourceDiscoveryReply::tr(s, c, n));
}

//  QList<QCoapResource> QCoapResourceDiscoveryReply::resources() const
extern "C" Q_DECL_EXPORT
QList<QCoapResource> *ritual_ZNK27QCoapResourceDiscoveryReply9resourcesEv(
    const QCoapResourceDiscoveryReply *self) {
  return new QList<QCoapResource>(self->resources());
}

//  QCoapResourceDiscoveryReply::QCoapResourceDiscoveryReply(const
//      QCoapRequest &request, QObject *parent)
extern "C" Q_DECL_EXPORT
QCoapResourceDiscoveryReply *ritual_ZN27QCoapResourceDiscoveryReplyC1ERK12QCoapRequestP7QObject(
    const QCoapRequest *request,
    QObject *parent) {
  return new QCoapResourceDiscoveryReply(*request, parent);
}

//  QCoapResourceDiscoveryReplyPrivate *QCoapResourceDiscoveryReply::d_func()
extern "C" Q_DECL_EXPORT
QCoapResourceDiscoveryReplyPrivate *ritual_ZN27QCoapResourceDiscoveryReply6d_funcEv(
    QCoapResourceDiscoveryReply *self) {
  return self->d_func();
}

//  const QCoapResourceDiscoveryReplyPrivate
//      *QCoapResourceDiscoveryReply::d_func() const
extern "C" Q_DECL_EXPORT
const QCoapResourceDiscoveryReplyPrivate *ritual_ZNK27QCoapResourceDiscoveryReply6d_funcEv(
    const QCoapResourceDiscoveryReply *self) {
  return self->d_func();
}
