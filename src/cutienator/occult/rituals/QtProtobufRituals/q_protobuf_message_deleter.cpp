//  Written by dev_tooling.RitualGenerator from the records of
//  QtProtobuf/qprotobufmessage.h, Qt 6.12.0. Changes made here are lost.
#include <QtProtobuf/qprotobufmessage.h>

//  void QProtobufMessageDeleter::operator()(QProtobufMessage *ptr) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK23QProtobufMessageDeleterclEP16QProtobufMessage(
    const QProtobufMessageDeleter *self,
    QProtobufMessage *ptr) {
  self->operator()(ptr);
}

//  QProtobufMessageDeleter::~QProtobufMessageDeleter()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QProtobufMessageDeleterD1Ev(QProtobufMessageDeleter *self) {
  delete self;
}
