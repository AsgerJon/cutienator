//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4runtimeapi_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4runtimeapi_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::Runtime::MarkCustom::call(const Value &toBeMarked)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV47Runtime10MarkCustom4callERKNS_5ValueE(
    const QV4::Value *toBeMarked) {
  QV4::Runtime::MarkCustom::call(*toBeMarked);
}

//  QV4::Runtime::MarkCustom::~MarkCustom()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV47Runtime10MarkCustomD1Ev(QV4::Runtime::MarkCustom *self) {
  delete self;
}
