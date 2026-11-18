//  Apache-2.0 license
//  Copyright (c) 2026 Asger Jon Vistisen
//
//  q_byte_array.cpp: just enough of QByteArray to read text back.
//  A function returning text hands over the address of a QByteArray;
//  these three let Python find its bytes, count them, and delete it.
#include <QtCore/QByteArray>

//  Qt: const char *constData() const
extern "C" const char *QByteArray_constData(QByteArray *self) {
  return self->constData();
}

//  Qt: qsizetype size() const
extern "C" long long QByteArray_size(QByteArray *self) {
  return self->size();
}

//  Qt: ~QByteArray()
extern "C" void QByteArray_delete(QByteArray *self) {
  delete self;
}
