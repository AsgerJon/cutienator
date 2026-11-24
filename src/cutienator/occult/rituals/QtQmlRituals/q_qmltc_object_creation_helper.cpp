//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmltcobjectcreationhelper_p.h, Qt 6.12.0.
//  Changes made here are lost.
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
