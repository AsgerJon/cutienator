//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlvme_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlvme_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QQmlVME::enableComponentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QQmlVME23enableComponentCompleteEv() {
  QQmlVME::enableComponentComplete();
}

//  void QQmlVME::disableComponentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QQmlVME24disableComponentCompleteEv() {
  QQmlVME::disableComponentComplete();
}

//  bool QQmlVME::componentCompleteEnabled()
extern "C" Q_DECL_EXPORT
bool ritual_ZN7QQmlVME24componentCompleteEnabledEv() {
  return QQmlVME::componentCompleteEnabled();
}

//  QQmlVME::~QQmlVME()
extern "C" Q_DECL_EXPORT
void ritual_ZN7QQmlVMED1Ev(QQmlVME *self) {
  delete self;
}
