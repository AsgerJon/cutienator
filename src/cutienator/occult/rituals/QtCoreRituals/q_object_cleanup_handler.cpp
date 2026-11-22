//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qobjectcleanuphandler.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qobjectcleanuphandler.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QObjectCleanupHandler::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QObjectCleanupHandler10metaObjectEv(
    const QObjectCleanupHandler *self) {
  return self->metaObject();
}

//  QString QObjectCleanupHandler::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QObjectCleanupHandler2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QObjectCleanupHandler::tr(s, c, n));
}

//  QObjectCleanupHandler::QObjectCleanupHandler()
extern "C" Q_DECL_EXPORT
QObjectCleanupHandler *ritual_ZN21QObjectCleanupHandlerC1Ev() {
  return new QObjectCleanupHandler();
}

//  QObjectCleanupHandler::~QObjectCleanupHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QObjectCleanupHandlerD1Ev(QObjectCleanupHandler *self) {
  delete self;
}

//  QObject *QObjectCleanupHandler::add(QObject *object)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN21QObjectCleanupHandler3addEP7QObject(
    QObjectCleanupHandler *self,
    QObject *object) {
  return self->add(object);
}

//  void QObjectCleanupHandler::remove(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QObjectCleanupHandler6removeEP7QObject(
    QObjectCleanupHandler *self,
    QObject *object) {
  self->remove(object);
}

//  bool QObjectCleanupHandler::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QObjectCleanupHandler7isEmptyEv(
    const QObjectCleanupHandler *self) {
  return self->isEmpty();
}

//  void QObjectCleanupHandler::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QObjectCleanupHandler5clearEv(QObjectCleanupHandler *self) {
  self->clear();
}
