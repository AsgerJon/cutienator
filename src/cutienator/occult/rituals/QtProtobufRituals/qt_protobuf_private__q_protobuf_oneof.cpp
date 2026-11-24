//  Written by dev_tooling.RitualGenerator from the records of
//  QtProtobuf/qprotobufoneof.h, Qt 6.12.0. Changes made here are lost.
#include <QtProtobuf/qprotobufoneof.h>
#include <QtCore/qmetatype.h>

//  void QtProtobufPrivate::QProtobufOneof::ensureMetaType(QMetaType lhs,
//      QMetaType rhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtProtobufPrivate14QProtobufOneof14ensureMetaTypeE9QMetaTypeS1_(
    const QMetaType *lhs,
    const QMetaType *rhs) {
  QtProtobufPrivate::QProtobufOneof::ensureMetaType(*lhs, *rhs);
}

//  bool operator==(const QProtobufOneof &lhs, const QProtobufOneof &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QtProtobufPrivateeqERKNS_14QProtobufOneofES2_(
    const QtProtobufPrivate::QProtobufOneof *lhs,
    const QtProtobufPrivate::QProtobufOneof *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QProtobufOneof &lhs, const QProtobufOneof &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QtProtobufPrivateneERKNS_14QProtobufOneofES2_(
    const QtProtobufPrivate::QProtobufOneof *lhs,
    const QtProtobufPrivate::QProtobufOneof *rhs) {
  return operator!=(*lhs, *rhs);
}
