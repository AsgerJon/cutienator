//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4dataview_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4dataview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::DataView::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48DataView10__dataTestEv(QV4::DataView *self) {
  self->__dataTest();
}

//  QV4::Heap::DataView *QV4::DataView::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::DataView *ritual_ZNK3QV48DataView11d_uncheckedEv(
    const QV4::DataView *self) {
  return self->d_unchecked();
}

//  QV4::Heap::DataView *QV4::DataView::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::DataView *ritual_ZNK3QV48DataView1dEv(const QV4::DataView *self) {
  return self->d();
}

//  QV4::Object *QV4::DataView::defaultPrototype(QV4::ExecutionEngine *e)
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZN3QV48DataView16defaultPrototypeEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *e) {
  return QV4::DataView::defaultPrototype(e);
}
