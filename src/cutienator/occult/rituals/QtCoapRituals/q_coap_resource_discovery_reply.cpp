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

//  void *QCoapResourceDiscoveryReply::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN27QCoapResourceDiscoveryReply11qt_metacastEPKc(
    QCoapResourceDiscoveryReply *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QCoapResourceDiscoveryReply::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN27QCoapResourceDiscoveryReply11qt_metacallEN11QMetaObject4CallEiPPv(
    QCoapResourceDiscoveryReply *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  void QCoapResourceDiscoveryReply::discovered(QCoapResourceDiscoveryReply
//      *reply, QList<QCoapResource> resources)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QCoapResourceDiscoveryReply10discoveredEPS_5QListI13QCoapResourceE(
    QCoapResourceDiscoveryReply *self,
    QCoapResourceDiscoveryReply *reply,
    const QList<QCoapResource> *resources) {
  self->discovered(reply, *resources);
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
