//  Written by dev_tooling.RitualGenerator from the records of
//  QtProtobuf/qprotobufregistration.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtProtobuf/qprotobufregistration.h>

//  QtProtobuf::ProtoTypeRegistrar::ProtoTypeRegistrar(QtProtobuf::RegisterFu
//      nction initializer)
extern "C" Q_DECL_EXPORT
QtProtobuf::ProtoTypeRegistrar *ritual_ZN10QtProtobuf18ProtoTypeRegistrarC1EPFvvE(
    void *initializer) {
  return new QtProtobuf::ProtoTypeRegistrar(
      reinterpret_cast<QtProtobuf::RegisterFunction>(initializer));
}

//  QtProtobuf::ProtoTypeRegistrar::~ProtoTypeRegistrar()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QtProtobuf18ProtoTypeRegistrarD1Ev(
    QtProtobuf::ProtoTypeRegistrar *self) {
  delete self;
}
