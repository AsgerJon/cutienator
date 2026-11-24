//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qpropertyprivate.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qpropertyprivate.h>

//  QtPrivate::BindingFunctionVTable::~BindingFunctionVTable()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QtPrivate21BindingFunctionVTableD1Ev(
    QtPrivate::BindingFunctionVTable *self) {
  delete self;
}
