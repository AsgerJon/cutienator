//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlnotifylist_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlnotifylist_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QQmlNotifyList::layout()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlNotifyList6layoutEv(QQmlNotifyList *self) {
  self->layout();
}

//  void QQmlNotifyList::layout(QQmlNotifierEndpoint *endpoint)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlNotifyList6layoutEP20QQmlNotifierEndpoint(
    QQmlNotifyList *self,
    QQmlNotifierEndpoint *endpoint) {
  self->layout(endpoint);
}

//  QQmlNotifyList::~QQmlNotifyList()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QQmlNotifyListD1Ev(QQmlNotifyList *self) {
  delete self;
}
