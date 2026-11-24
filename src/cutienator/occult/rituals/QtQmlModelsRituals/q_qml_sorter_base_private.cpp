//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmlsorterbase_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_sfpm_model) && QT_CONFIG(proxymodel)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmlsorterbase_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQmlSorterBase *QQmlSorterBasePrivate::q_func()
extern "C" Q_DECL_EXPORT
QQmlSorterBase *ritual_ZN21QQmlSorterBasePrivate6q_funcEv(
    QQmlSorterBasePrivate *self) {
  return self->q_func();
}

//  const QQmlSorterBase *QQmlSorterBasePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQmlSorterBase *ritual_ZNK21QQmlSorterBasePrivate6q_funcEv(
    const QQmlSorterBasePrivate *self) {
  return self->q_func();
}

//  QQmlSorterBasePrivate::QQmlSorterBasePrivate()
extern "C" Q_DECL_EXPORT
QQmlSorterBasePrivate *ritual_ZN21QQmlSorterBasePrivateC1Ev() {
  return new QQmlSorterBasePrivate();
}

//  QQmlSorterBasePrivate::~QQmlSorterBasePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQmlSorterBasePrivateD1Ev(QQmlSorterBasePrivate *self) {
  delete self;
}

#endif  // QT_CONFIG(qml_sfpm_model) && QT_CONFIG(proxymodel)
