//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4calldata_p.h, Qt 6.12.0. Edited by hand on
//  2026-11-25: added by hand, instances of templates of the class: 2. Kept
//  as it is when the generator runs again.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4calldata_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  int QV4::CallData::argc() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV48CallData4argcEv(const QV4::CallData *self) {
  return self->argc();
}

//  void QV4::CallData::setArgc(int argc)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48CallData7setArgcEi(QV4::CallData *self, int argc) {
  self->setArgc(argc);
}

//  ReturnedValue QV4::CallData::argument(int i) const
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZNK3QV48CallData8argumentEi(
    const QV4::CallData *self,
    int i) {
  return self->argument(i);
}

//  int QV4::CallData::HeaderSize()
extern "C" Q_DECL_EXPORT
int ritual_ZN3QV48CallData10HeaderSizeEv() {
  return QV4::CallData::HeaderSize();
}

//  QV4::CallData::~CallData()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48CallDataD1Ev(QV4::CallData *self) {
  delete self;
}

//  QV4::Value *QV4::CallData::argValues<QV4::Value>()
extern "C" Q_DECL_EXPORT
QV4::Value *ritual_ZN3QV48CallData9argValuesINS_5ValueEEEPT_v(
    QV4::CallData *self) {
  return self->argValues<QV4::Value>();
}

//  const QV4::Value *QV4::CallData::argValues<QV4::Value>() const
extern "C" Q_DECL_EXPORT
const QV4::Value *ritual_ZNK3QV48CallData9argValuesINS_5ValueEEEPKT_v(
    const QV4::CallData *self) {
  return self->argValues<QV4::Value>();
}
