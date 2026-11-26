//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4qobjectwrapper_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4qobjectwrapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  void QV4::Heap::QObjectMethod::markObjects(Heap::Base *b, MarkStack
//      *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap13QObjectMethod11markObjectsEPNS0_4BaseEPNS_9MarkStackE(
    QV4::Heap::Base *b,
    QV4::MarkStack *stack) {
  QV4::Heap::QObjectMethod::markObjects(b, stack);
}

//  void QV4::Heap::QObjectMethod::init(QV4::ExecutionEngine *engine, Object
//      *wrapper, int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap13QObjectMethod4initEPNS_15ExecutionEngineEPNS0_6ObjectEi(
    QV4::Heap::QObjectMethod *self,
    QV4::ExecutionEngine *engine,
    QV4::Heap::Object *wrapper,
    int index) {
  self->init(engine, wrapper, index);
}

//  void QV4::Heap::QObjectMethod::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap13QObjectMethod7destroyEv(
    QV4::Heap::QObjectMethod *self) {
  self->destroy();
}

//  void QV4::Heap::QObjectMethod::ensureMethodsCache(const QMetaObject
//      *thisMeta)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap13QObjectMethod18ensureMethodsCacheEPK11QMetaObject(
    QV4::Heap::QObjectMethod *self,
    const QMetaObject *thisMeta) {
  self->ensureMethodsCache(thisMeta);
}

//  QString QV4::Heap::QObjectMethod::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV44Heap13QObjectMethod4nameEv(
    const QV4::Heap::QObjectMethod *self) {
  return new QString(self->name());
}

//  const QMetaObject *QV4::Heap::QObjectMethod::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK3QV44Heap13QObjectMethod10metaObjectEv(
    const QV4::Heap::QObjectMethod *self) {
  return self->metaObject();
}

//  QObject *QV4::Heap::QObjectMethod::object() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK3QV44Heap13QObjectMethod6objectEv(
    const QV4::Heap::QObjectMethod *self) {
  return self->object();
}

//  bool QV4::Heap::QObjectMethod::isDetached() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV44Heap13QObjectMethod10isDetachedEv(
    const QV4::Heap::QObjectMethod *self) {
  return self->isDetached();
}

//  bool QV4::Heap::QObjectMethod::isAttachedTo(QObject *o) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV44Heap13QObjectMethod12isAttachedToEP7QObject(
    const QV4::Heap::QObjectMethod *self,
    QObject *o) {
  return self->isAttachedTo(o);
}

//  QV4::Heap::QObjectMethod::ThisObjectMode
//      QV4::Heap::QObjectMethod::checkThisObject(const QMetaObject
//      *thisMeta) const
extern "C" Q_DECL_EXPORT
QV4::Heap::QObjectMethod::ThisObjectMode ritual_ZNK3QV44Heap13QObjectMethod15checkThisObjectEPK11QMetaObject(
    const QV4::Heap::QObjectMethod *self,
    const QMetaObject *thisMeta) {
  return self->checkThisObject(thisMeta);
}

//  QV4::Heap::QObjectMethod as the QV4::Heap::QObjectMethodData it is built
//      on
extern "C" Q_DECL_EXPORT
QV4::Heap::QObjectMethodData *ritual_cast_QV4_Heap_QObjectMethod_QV4_Heap_QObjectMethodData(
    QV4::Heap::QObjectMethod *self) {
  return static_cast<QV4::Heap::QObjectMethodData *>(self);
}
