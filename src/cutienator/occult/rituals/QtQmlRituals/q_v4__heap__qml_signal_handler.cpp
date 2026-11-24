//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4qobjectwrapper_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4qobjectwrapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::Heap::QmlSignalHandler::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap16QmlSignalHandler7destroyEv(
    QV4::Heap::QmlSignalHandler *self) {
  self->destroy();
}

//  QObject *QV4::Heap::QmlSignalHandler::object() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK3QV44Heap16QmlSignalHandler6objectEv(
    const QV4::Heap::QmlSignalHandler *self) {
  return self->object();
}

//  void QV4::Heap::QmlSignalHandler::setObject(QObject *o)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap16QmlSignalHandler9setObjectEP7QObject(
    QV4::Heap::QmlSignalHandler *self,
    QObject *o) {
  self->setObject(o);
}
