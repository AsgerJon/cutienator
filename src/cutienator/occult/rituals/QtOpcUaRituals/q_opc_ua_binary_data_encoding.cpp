//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuabinarydataencoding.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtOpcUa/qopcuabinarydataencoding.h>

//  QOpcUaBinaryDataEncoding::QOpcUaBinaryDataEncoding(QByteArray *buffer)
extern "C" Q_DECL_EXPORT
QOpcUaBinaryDataEncoding *ritual_ZN24QOpcUaBinaryDataEncodingC1EP10QByteArray(
    QByteArray *buffer) {
  return new QOpcUaBinaryDataEncoding(buffer);
}

//  int QOpcUaBinaryDataEncoding::offset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QOpcUaBinaryDataEncoding6offsetEv(
    const QOpcUaBinaryDataEncoding *self) {
  return self->offset();
}

//  void QOpcUaBinaryDataEncoding::setOffset(int offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QOpcUaBinaryDataEncoding9setOffsetEi(
    QOpcUaBinaryDataEncoding *self,
    int offset) {
  self->setOffset(offset);
}

//  void QOpcUaBinaryDataEncoding::truncateBufferToOffset()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QOpcUaBinaryDataEncoding22truncateBufferToOffsetEv(
    QOpcUaBinaryDataEncoding *self) {
  self->truncateBufferToOffset();
}

//  bool QOpcUaBinaryDataEncoding::enoughData(int requiredSize)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QOpcUaBinaryDataEncoding10enoughDataEi(
    QOpcUaBinaryDataEncoding *self,
    int requiredSize) {
  return self->enoughData(requiredSize);
}

//  QOpcUaBinaryDataEncoding::~QOpcUaBinaryDataEncoding()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QOpcUaBinaryDataEncodingD1Ev(
    QOpcUaBinaryDataEncoding *self) {
  delete self;
}
