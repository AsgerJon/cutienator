//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlnotifier_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlnotifier_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQmlNotifier::QQmlNotifier()
extern "C" Q_DECL_EXPORT
QQmlNotifier *ritual_ZN12QQmlNotifierC1Ev() {
  return new QQmlNotifier();
}

//  QQmlNotifier::~QQmlNotifier()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlNotifierD1Ev(QQmlNotifier *self) {
  delete self;
}

//  void QQmlNotifier::notify()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlNotifier6notifyEv(QQmlNotifier *self) {
  self->notify();
}

//  void QQmlNotifier::connect(QQmlNotifierEndpoint *endpoint)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlNotifier7connectEP20QQmlNotifierEndpoint(
    QQmlNotifier *self,
    QQmlNotifierEndpoint *endpoint) {
  self->connect(endpoint);
}

//  void QQmlNotifier::notify(QQmlData *ddata, int notifierIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQmlNotifier6notifyEP8QQmlDatai(
    QQmlData *ddata,
    int notifierIndex) {
  QQmlNotifier::notify(ddata, notifierIndex);
}
