//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qvarlengtharray.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qvarlengtharray.h>

//  QVLABaseBase::QVLABaseBase()
extern "C" Q_DECL_EXPORT
QVLABaseBase *ritual_ZN12QVLABaseBaseC1Ev() {
  return new QVLABaseBase();
}

//  QVLABaseBase::~QVLABaseBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QVLABaseBaseD1Ev(QVLABaseBase *self) {
  delete self;
}

//  void QVLABaseBase::verify(qsizetype pos, qsizetype n) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK12QVLABaseBase6verifyExx(
    const QVLABaseBase *self,
    qsizetype pos,
    qsizetype n) {
  self->verify(pos, n);
}

//  size_type QVLABaseBase::capacity() const
extern "C" Q_DECL_EXPORT
QVLABaseBase::size_type ritual_ZNK12QVLABaseBase8capacityEv(
    const QVLABaseBase *self) {
  return self->capacity();
}

//  size_type QVLABaseBase::size() const
extern "C" Q_DECL_EXPORT
QVLABaseBase::size_type ritual_ZNK12QVLABaseBase4sizeEv(
    const QVLABaseBase *self) {
  return self->size();
}

//  bool QVLABaseBase::empty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QVLABaseBase5emptyEv(const QVLABaseBase *self) {
  return self->empty();
}
