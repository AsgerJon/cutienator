//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4enginebase_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4enginebase_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Heap::InternalClass *QV4::EngineBase::internalClasses(InternalClassType
//      icType)
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZN3QV410EngineBase15internalClassesENS0_17InternalClassTypeE(
    QV4::EngineBase *self,
    QV4::EngineBase::InternalClassType icType) {
  return self->internalClasses(icType);
}

//  QV4::EngineBase::~EngineBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV410EngineBaseD1Ev(QV4::EngineBase *self) {
  delete self;
}
