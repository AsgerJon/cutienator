//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4regexpobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4regexpobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  const QV4::VTable *QV4::RegExpObject::staticVTable()
extern "C" Q_DECL_EXPORT
const QV4::VTable *ritual_ZN3QV412RegExpObject12staticVTableEv() {
  return QV4::RegExpObject::staticVTable();
}

//  void QV4::RegExpObject::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412RegExpObject10__dataTestEv(QV4::RegExpObject *self) {
  self->__dataTest();
}

//  QV4::Heap::RegExpObject *QV4::RegExpObject::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::RegExpObject *ritual_ZNK3QV412RegExpObject11d_uncheckedEv(
    const QV4::RegExpObject *self) {
  return self->d_unchecked();
}

//  QV4::Heap::RegExpObject *QV4::RegExpObject::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::RegExpObject *ritual_ZNK3QV412RegExpObject1dEv(
    const QV4::RegExpObject *self) {
  return self->d();
}

//  Heap::InternalClass
//      *QV4::RegExpObject::defaultInternalClass(QV4::EngineBase *e)
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZN3QV412RegExpObject20defaultInternalClassEPNS_10EngineBaseE(
    QV4::EngineBase *e) {
  return QV4::RegExpObject::defaultInternalClass(e);
}

//  QV4::Object *QV4::RegExpObject::defaultPrototype(QV4::ExecutionEngine *e)
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZN3QV412RegExpObject16defaultPrototypeEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *e) {
  return QV4::RegExpObject::defaultPrototype(e);
}

//  int QV4::RegExpObject::lastIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV412RegExpObject9lastIndexEv(const QV4::RegExpObject *self) {
  return self->lastIndex();
}

//  void QV4::RegExpObject::setLastIndex(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412RegExpObject12setLastIndexEi(
    QV4::RegExpObject *self,
    int index) {
  self->setLastIndex(index);
}

//  QString QV4::RegExpObject::source() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK3QV412RegExpObject6sourceEv(
    const QV4::RegExpObject *self) {
  return new QString(self->source());
}
