//  Written by dev_tooling.RitualGenerator from the records of
//  QtProtobuf/qprotobufmessage.h, Qt 6.12.0. Changes made here are lost.
#include <QtProtobuf/qprotobufmessage.h>
#include <QtCore/qmetatype.h>

//  QProtobufMapEntryBase::QProtobufMapEntryBase(QMetaType key, QMetaType
//      value, StaticMetaCallFn metaCall)
extern "C" Q_DECL_EXPORT
QProtobufMapEntryBase *ritual_ZN21QProtobufMapEntryBaseC1E9QMetaTypeS0_PFvP7QObjectN11QMetaObject4CallEiPPvE(
    const QMetaType *key,
    const QMetaType *value,
    void *metaCall) {
  return new QProtobufMapEntryBase(
      *key,
      *value,
      reinterpret_cast<QProtobufMapEntryBase::StaticMetaCallFn>(metaCall));
}

//  QProtobufMapEntryBase::~QProtobufMapEntryBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QProtobufMapEntryBaseD1Ev(QProtobufMapEntryBase *self) {
  delete self;
}

//  QProtobufMapEntryBasePrivate *QProtobufMapEntryBase::d_func()
extern "C" Q_DECL_EXPORT
QProtobufMapEntryBasePrivate *ritual_ZN21QProtobufMapEntryBase6d_funcEv(
    QProtobufMapEntryBase *self) {
  return self->d_func();
}

//  const QProtobufMapEntryBasePrivate *QProtobufMapEntryBase::d_func() const
extern "C" Q_DECL_EXPORT
const QProtobufMapEntryBasePrivate *ritual_ZNK21QProtobufMapEntryBase6d_funcEv(
    const QProtobufMapEntryBase *self) {
  return self->d_func();
}
