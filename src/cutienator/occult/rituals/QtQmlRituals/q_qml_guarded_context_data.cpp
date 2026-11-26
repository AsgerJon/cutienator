//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlguardedcontextdata_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlguardedcontextdata_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQmlGuardedContextData::QQmlGuardedContextData()
extern "C" Q_DECL_EXPORT
QQmlGuardedContextData *ritual_ZN22QQmlGuardedContextDataC1Ev() {
  return new QQmlGuardedContextData();
}

//  QQmlGuardedContextData::~QQmlGuardedContextData()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlGuardedContextDataD1Ev(QQmlGuardedContextData *self) {
  delete self;
}

//  QQmlGuardedContextData::QQmlGuardedContextData(QQmlGuardedContextData
//      &&a0)
extern "C" Q_DECL_EXPORT
QQmlGuardedContextData *ritual_ZN22QQmlGuardedContextDataC1EOS_(
    QQmlGuardedContextData *a0) {
  return new QQmlGuardedContextData(std::move(*a0));
}

//  QQmlGuardedContextData
//      &QQmlGuardedContextData::operator=(QQmlGuardedContextData &&a0)
extern "C" Q_DECL_EXPORT
QQmlGuardedContextData *ritual_ZN22QQmlGuardedContextDataaSEOS_(
    QQmlGuardedContextData *self,
    QQmlGuardedContextData *a0) {
  return &(self->operator=(std::move(*a0)));
}

//  QQmlGuardedContextData::QQmlGuardedContextData(QQmlRefPointer<QQmlContext
//      Data> data)
extern "C" Q_DECL_EXPORT
QQmlGuardedContextData *ritual_ZN22QQmlGuardedContextDataC1E14QQmlRefPointerI15QQmlContextDataE(
    const QQmlRefPointer<QQmlContextData> *data) {
  return new QQmlGuardedContextData(*data);
}

//  QQmlGuardedContextData
//      &QQmlGuardedContextData::operator=(QQmlRefPointer<QQmlContextData> d)
extern "C" Q_DECL_EXPORT
QQmlGuardedContextData *ritual_ZN22QQmlGuardedContextDataaSE14QQmlRefPointerI15QQmlContextDataE(
    QQmlGuardedContextData *self,
    const QQmlRefPointer<QQmlContextData> *d) {
  return &(self->operator=(*d));
}

//  QQmlRefPointer<QQmlContextData> QQmlGuardedContextData::contextData()
//      const
extern "C" Q_DECL_EXPORT
QQmlRefPointer<QQmlContextData> *ritual_ZNK22QQmlGuardedContextData11contextDataEv(
    const QQmlGuardedContextData *self) {
  return new QQmlRefPointer<QQmlContextData>(self->contextData());
}

//  void
//      QQmlGuardedContextData::setContextData(QQmlRefPointer<QQmlContextData
//      > contextData)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlGuardedContextData14setContextDataE14QQmlRefPointerI15QQmlContextDataE(
    QQmlGuardedContextData *self,
    const QQmlRefPointer<QQmlContextData> *contextData) {
  self->setContextData(*contextData);
}

//  bool QQmlGuardedContextData::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QQmlGuardedContextData6isNullEv(
    const QQmlGuardedContextData *self) {
  return self->isNull();
}

//  const QQmlRefPointer<QQmlContextData> &QQmlGuardedContextData::operator
//      const QQmlRefPointer<QQmlContextData> &() const
extern "C" Q_DECL_EXPORT
const QQmlRefPointer<QQmlContextData> *ritual_ZNK22QQmlGuardedContextDatacvRK14QQmlRefPointerI15QQmlContextDataEEv(
    const QQmlGuardedContextData *self) {
  return &(self->operator const QQmlRefPointer<QQmlContextData> &());
}

//  QQmlContextData &QQmlGuardedContextData::operator*() const
extern "C" Q_DECL_EXPORT
QQmlContextData *ritual_ZNK22QQmlGuardedContextDatadeEv(
    const QQmlGuardedContextData *self) {
  return &(self->operator*());
}

//  QQmlContextData *QQmlGuardedContextData::operator->() const
extern "C" Q_DECL_EXPORT
QQmlContextData *ritual_ZNK22QQmlGuardedContextDataptEv(
    const QQmlGuardedContextData *self) {
  return self->operator->();
}

//  QQmlGuardedContextData *QQmlGuardedContextData::next() const
extern "C" Q_DECL_EXPORT
QQmlGuardedContextData *ritual_ZNK22QQmlGuardedContextData4nextEv(
    const QQmlGuardedContextData *self) {
  return self->next();
}

//  void QQmlGuardedContextData::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlGuardedContextData5resetEv(
    QQmlGuardedContextData *self) {
  self->reset();
}

//  void QQmlGuardedContextData::unlink()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQmlGuardedContextData6unlinkEv(
    QQmlGuardedContextData *self) {
  self->unlink();
}

//  a QQmlRefPointer<QQmlContextData> a ritual of QQmlGuardedContextData gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlGuardedContextData__QQmlRefPointer_QQmlContextData(
    QQmlRefPointer<QQmlContextData> *self) {
  delete self;
}
