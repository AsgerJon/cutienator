//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4runtimeapi_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4runtimeapi_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QHash>

//  QHash<const void *, const char *> QV4::Runtime::symbolTable()
extern "C" Q_DECL_EXPORT
QHash<const void *, const char *> *ritual_ZN3QV47Runtime11symbolTableEv() {
  return new QHash<const void *, const char *>(QV4::Runtime::symbolTable());
}

//  QV4::Runtime::~Runtime()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV47RuntimeD1Ev(QV4::Runtime *self) {
  delete self;
}

//  a QHash<const void *, const char *> a ritual of QV4::Runtime gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QV4_Runtime__QHash_const_void_const_char(
    QHash<const void *, const char *> *self) {
  delete self;
}
