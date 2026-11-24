//  Written by dev_tooling.RitualGenerator from the records of
//  QtProtobuf/qprotobuflazymessagepointer.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtProtobuf/qprotobuflazymessagepointer.h>

//  QtProtobufPrivate::QProtobufLazyMessagePointerBase::QProtobufLazyMessageP
//      ointerBase()
extern "C" Q_DECL_EXPORT
QtProtobufPrivate::QProtobufLazyMessagePointerBase *ritual_ZN17QtProtobufPrivate31QProtobufLazyMessagePointerBaseC1Ev() {
  return new QtProtobufPrivate::QProtobufLazyMessagePointerBase();
}

//  QtProtobufPrivate::QProtobufLazyMessagePointerBase::QProtobufLazyMessageP
//      ointerBase(QProtobufMessage *ptr)
extern "C" Q_DECL_EXPORT
QtProtobufPrivate::QProtobufLazyMessagePointerBase *ritual_ZN17QtProtobufPrivate31QProtobufLazyMessagePointerBaseC1EP16QProtobufMessage(
    QProtobufMessage *ptr) {
  return new QtProtobufPrivate::QProtobufLazyMessagePointerBase(ptr);
}

//  QProtobufMessage
//      *QtProtobufPrivate::QProtobufLazyMessagePointerBase::message() const
extern "C" Q_DECL_EXPORT
QProtobufMessage *ritual_ZNK17QtProtobufPrivate31QProtobufLazyMessagePointerBase7messageEv(
    const QtProtobufPrivate::QProtobufLazyMessagePointerBase *self) {
  return self->message();
}

//  void QtProtobufPrivate::QProtobufLazyMessagePointerBase::setMessage(QProt
//      obufMessage *msg) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK17QtProtobufPrivate31QProtobufLazyMessagePointerBase10setMessageEP16QProtobufMessage(
    const QtProtobufPrivate::QProtobufLazyMessagePointerBase *self,
    QProtobufMessage *msg) {
  self->setMessage(msg);
}

//  QtProtobufPrivate::QProtobufLazyMessagePointerBase::~QProtobufLazyMessage
//      PointerBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QtProtobufPrivate31QProtobufLazyMessagePointerBaseD1Ev(
    QtProtobufPrivate::QProtobufLazyMessagePointerBase *self) {
  delete self;
}

//  bool QtProtobufPrivate::QProtobufLazyMessagePointerBase::operator bool()
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QtProtobufPrivate31QProtobufLazyMessagePointerBasecvbEv(
    const QtProtobufPrivate::QProtobufLazyMessagePointerBase *self) {
  return self->operator bool();
}
