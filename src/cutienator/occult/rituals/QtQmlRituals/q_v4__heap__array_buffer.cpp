//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4arraybuffer_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4arraybuffer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>

//  void QV4::Heap::ArrayBuffer::init(size_t length)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap11ArrayBuffer4initEm(
    QV4::Heap::ArrayBuffer *self,
    size_t length) {
  self->init(length);
}

//  void QV4::Heap::ArrayBuffer::init(const QByteArray &array)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap11ArrayBuffer4initERK10QByteArray(
    QV4::Heap::ArrayBuffer *self,
    const QByteArray *array) {
  self->init(*array);
}
