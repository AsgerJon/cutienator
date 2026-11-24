//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/rhi/qrhi.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qrhi.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QRhiVertexInputAttribute::QRhiVertexInputAttribute()
extern "C" Q_DECL_EXPORT
QRhiVertexInputAttribute *ritual_ZN24QRhiVertexInputAttributeC1Ev() {
  return new QRhiVertexInputAttribute();
}

//  QRhiVertexInputAttribute::QRhiVertexInputAttribute(int binding, int
//      location, Format format, quint32 offset, int matrixSlice)
extern "C" Q_DECL_EXPORT
QRhiVertexInputAttribute *ritual_ZN24QRhiVertexInputAttributeC1EiiNS_6FormatEji(
    int binding,
    int location,
    QRhiVertexInputAttribute::Format format,
    quint32 offset,
    int matrixSlice) {
  return new QRhiVertexInputAttribute(
      binding,
      location,
      format,
      offset,
      matrixSlice);
}

//  int QRhiVertexInputAttribute::binding() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QRhiVertexInputAttribute7bindingEv(
    const QRhiVertexInputAttribute *self) {
  return self->binding();
}

//  void QRhiVertexInputAttribute::setBinding(int b)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QRhiVertexInputAttribute10setBindingEi(
    QRhiVertexInputAttribute *self,
    int b) {
  self->setBinding(b);
}

//  int QRhiVertexInputAttribute::location() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QRhiVertexInputAttribute8locationEv(
    const QRhiVertexInputAttribute *self) {
  return self->location();
}

//  void QRhiVertexInputAttribute::setLocation(int loc)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QRhiVertexInputAttribute11setLocationEi(
    QRhiVertexInputAttribute *self,
    int loc) {
  self->setLocation(loc);
}

//  Format QRhiVertexInputAttribute::format() const
extern "C" Q_DECL_EXPORT
QRhiVertexInputAttribute::Format ritual_ZNK24QRhiVertexInputAttribute6formatEv(
    const QRhiVertexInputAttribute *self) {
  return self->format();
}

//  void QRhiVertexInputAttribute::setFormat(Format f)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QRhiVertexInputAttribute9setFormatENS_6FormatE(
    QRhiVertexInputAttribute *self,
    QRhiVertexInputAttribute::Format f) {
  self->setFormat(f);
}

//  quint32 QRhiVertexInputAttribute::offset() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK24QRhiVertexInputAttribute6offsetEv(
    const QRhiVertexInputAttribute *self) {
  return self->offset();
}

//  void QRhiVertexInputAttribute::setOffset(quint32 ofs)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QRhiVertexInputAttribute9setOffsetEj(
    QRhiVertexInputAttribute *self,
    quint32 ofs) {
  self->setOffset(ofs);
}

//  int QRhiVertexInputAttribute::matrixSlice() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QRhiVertexInputAttribute11matrixSliceEv(
    const QRhiVertexInputAttribute *self) {
  return self->matrixSlice();
}

//  void QRhiVertexInputAttribute::setMatrixSlice(int slice)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QRhiVertexInputAttribute14setMatrixSliceEi(
    QRhiVertexInputAttribute *self,
    int slice) {
  self->setMatrixSlice(slice);
}

//  bool operator==(const QRhiVertexInputAttribute &a, const
//      QRhiVertexInputAttribute &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK24QRhiVertexInputAttributeS1_(
    const QRhiVertexInputAttribute *a,
    const QRhiVertexInputAttribute *b) {
  return operator==(*a, *b);
}

//  bool operator!=(const QRhiVertexInputAttribute &a, const
//      QRhiVertexInputAttribute &b)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK24QRhiVertexInputAttributeS1_(
    const QRhiVertexInputAttribute *a,
    const QRhiVertexInputAttribute *b) {
  return operator!=(*a, *b);
}

//  QRhiVertexInputAttribute::~QRhiVertexInputAttribute()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QRhiVertexInputAttributeD1Ev(
    QRhiVertexInputAttribute *self) {
  delete self;
}
