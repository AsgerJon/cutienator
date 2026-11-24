//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmlsasourcelocation_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmlsasourcelocation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/qqmlsasourcelocation.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmljssourcelocation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const QQmlJS::SourceLocation
//      &QQmlSA::SourceLocationPrivate::sourceLocation(const
//      QQmlSA::SourceLocation &sourceLocation)
extern "C" Q_DECL_EXPORT
QQmlJS::SourceLocation *ritual_ZN6QQmlSA21SourceLocationPrivate14sourceLocationERKNS_14SourceLocationE(
    const QQmlSA::SourceLocation *sourceLocation) {
  return new QQmlJS::SourceLocation(
      QQmlSA::SourceLocationPrivate::sourceLocation(
          *sourceLocation));
}

//  QQmlSA::SourceLocation
//      QQmlSA::SourceLocationPrivate::createQQmlSASourceLocation(const
//      QQmlJS::SourceLocation &jsLocation)
extern "C" Q_DECL_EXPORT
QQmlSA::SourceLocation *ritual_ZN6QQmlSA21SourceLocationPrivate26createQQmlSASourceLocationERKN6QQmlJS14SourceLocationE(
    const QQmlJS::SourceLocation *jsLocation) {
  return new QQmlSA::SourceLocation(
      QQmlSA::SourceLocationPrivate::createQQmlSASourceLocation(
          *jsLocation));
}

//  qsizetype QQmlSA::SourceLocationPrivate::sizeOfSourceLocation()
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN6QQmlSA21SourceLocationPrivate20sizeOfSourceLocationEv() {
  return QQmlSA::SourceLocationPrivate::sizeOfSourceLocation();
}

//  QQmlSA::SourceLocationPrivate::~SourceLocationPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlSA21SourceLocationPrivateD1Ev(
    QQmlSA::SourceLocationPrivate *self) {
  delete self;
}
