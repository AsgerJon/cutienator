//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmltcobjectcreationhelper_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: added by hand, instances of templates of
//  the class: 1. Kept as it is when the generator runs again.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmltcobjectcreationhelper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  qsizetype QQmltcObjectCreationHelper::offset() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK26QQmltcObjectCreationHelper6offsetEv(
    const QQmltcObjectCreationHelper *self) {
  return self->offset();
}

//  QQmltcObjectCreationHelper::QQmltcObjectCreationHelper(QObject **data,
//      qsizetype size)
extern "C" Q_DECL_EXPORT
QQmltcObjectCreationHelper *ritual_ZN26QQmltcObjectCreationHelperC1EPP7QObjectx(
    QObject **data,
    qsizetype size) {
  return new QQmltcObjectCreationHelper(data, size);
}

//  QQmltcObjectCreationHelper::QQmltcObjectCreationHelper(const
//      QQmltcObjectCreationHelper *base, qsizetype localOffset)
extern "C" Q_DECL_EXPORT
QQmltcObjectCreationHelper *ritual_ZN26QQmltcObjectCreationHelperC1EPKS_x(
    const QQmltcObjectCreationHelper *base,
    qsizetype localOffset) {
  return new QQmltcObjectCreationHelper(base, localOffset);
}

//  void QQmltcObjectCreationHelper::set(qsizetype i, QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQmltcObjectCreationHelper3setExP7QObject(
    QQmltcObjectCreationHelper *self,
    qsizetype i,
    QObject *object) {
  self->set(i, object);
}

//  QQmltcObjectCreationHelper::~QQmltcObjectCreationHelper()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QQmltcObjectCreationHelperD1Ev(
    QQmltcObjectCreationHelper *self) {
  delete self;
}

//  QObject *QQmltcObjectCreationHelper::get<QObject>(qsizetype i) const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK26QQmltcObjectCreationHelper3getI7QObjectEEPT_x(
    const QQmltcObjectCreationHelper *self,
    long long i) {
  return self->get<QObject>(static_cast<qsizetype>(i));
}
