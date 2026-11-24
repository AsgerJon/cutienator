//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmlsa_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmlsa_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QQmlSA::PassManagerPrivate::PassManagerPrivate(QQmlJSImportVisitor
//      *visitor, QQmlJSTypeResolver *resolver)
extern "C" Q_DECL_EXPORT
QQmlSA::PassManagerPrivate *ritual_ZN6QQmlSA18PassManagerPrivateC1EP19QQmlJSImportVisitorP18QQmlJSTypeResolver(
    QQmlJSImportVisitor *visitor,
    QQmlJSTypeResolver *resolver) {
  return new QQmlSA::PassManagerPrivate(visitor, resolver);
}

//  PassManagerPrivate *QQmlSA::PassManagerPrivate::get(PassManager *manager)
extern "C" Q_DECL_EXPORT
QQmlSA::PassManagerPrivate *ritual_ZN6QQmlSA18PassManagerPrivate3getEPNS_11PassManagerE(
    QQmlSA::PassManager *manager) {
  return QQmlSA::PassManagerPrivate::get(manager);
}

//  const PassManagerPrivate *QQmlSA::PassManagerPrivate::get(const
//      PassManager *manager)
extern "C" Q_DECL_EXPORT
const QQmlSA::PassManagerPrivate *ritual_ZN6QQmlSA18PassManagerPrivate3getEPKNS_11PassManagerE(
    const QQmlSA::PassManager *manager) {
  return QQmlSA::PassManagerPrivate::get(manager);
}

//  PassManager
//      *QQmlSA::PassManagerPrivate::createPassManager(QQmlJSImportVisitor
//      *visitor, QQmlJSTypeResolver *resolver)
extern "C" Q_DECL_EXPORT
QQmlSA::PassManager *ritual_ZN6QQmlSA18PassManagerPrivate17createPassManagerEP19QQmlJSImportVisitorP18QQmlJSTypeResolver(
    QQmlJSImportVisitor *visitor,
    QQmlJSTypeResolver *resolver) {
  return QQmlSA::PassManagerPrivate::createPassManager(visitor, resolver);
}

//  void QQmlSA::PassManagerPrivate::deletePassManager(PassManager *q)
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA18PassManagerPrivate17deletePassManagerEPNS_11PassManagerE(
    QQmlSA::PassManager *q) {
  QQmlSA::PassManagerPrivate::deletePassManager(q);
}
