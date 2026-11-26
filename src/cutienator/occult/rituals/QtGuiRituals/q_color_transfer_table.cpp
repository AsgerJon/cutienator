//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qcolortransfertable_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qcolortransfertable_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QColorTransferTable::QColorTransferTable()
extern "C" Q_DECL_EXPORT
QColorTransferTable *ritual_ZN19QColorTransferTableC1Ev() {
  return new QColorTransferTable();
}

//  QColorTransferTable::QColorTransferTable(uint32_t size, const
//      QList<uint8_t> &table, Type type)
extern "C" Q_DECL_EXPORT
QColorTransferTable *ritual_ZN19QColorTransferTableC1EjRK5QListIhENS_4TypeE(
    uint32_t size,
    const QList<uint8_t> *table,
    QColorTransferTable::Type type) {
  return new QColorTransferTable(size, *table, type);
}

//  QColorTransferTable::QColorTransferTable(uint32_t size, const
//      QList<uint16_t> &table, Type type)
extern "C" Q_DECL_EXPORT
QColorTransferTable *ritual_ZN19QColorTransferTableC1EjRK5QListItENS_4TypeE(
    uint32_t size,
    const QList<uint16_t> *table,
    QColorTransferTable::Type type) {
  return new QColorTransferTable(size, *table, type);
}

//  bool QColorTransferTable::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QColorTransferTable7isEmptyEv(
    const QColorTransferTable *self) {
  return self->isEmpty();
}

//  bool QColorTransferTable::isIdentity() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QColorTransferTable10isIdentityEv(
    const QColorTransferTable *self) {
  return self->isIdentity();
}

//  bool QColorTransferTable::checkValidity() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QColorTransferTable13checkValidityEv(
    const QColorTransferTable *self) {
  return self->checkValidity();
}

//  bool QColorTransferTable::checkInvertibility() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QColorTransferTable18checkInvertibilityEv(
    const QColorTransferTable *self) {
  return self->checkInvertibility();
}

//  float QColorTransferTable::apply(float x) const
extern "C" Q_DECL_EXPORT
float ritual_ZNK19QColorTransferTable5applyEf(
    const QColorTransferTable *self,
    float x) {
  return self->apply(x);
}

//  float QColorTransferTable::applyInverse(float x, float resultLargerThan)
//      const
extern "C" Q_DECL_EXPORT
float ritual_ZNK19QColorTransferTable12applyInverseEff(
    const QColorTransferTable *self,
    float x,
    float resultLargerThan) {
  return self->applyInverse(x, resultLargerThan);
}

//  bool QColorTransferTable::asColorTransferFunction(QColorTransferFunction
//      *transferFn)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QColorTransferTable23asColorTransferFunctionEP22QColorTransferFunction(
    QColorTransferTable *self,
    QColorTransferFunction *transferFn) {
  return self->asColorTransferFunction(transferFn);
}

//  bool operator!=(const QColorTransferTable &t1, const QColorTransferTable
//      &t2)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK19QColorTransferTableS1_(
    const QColorTransferTable *t1,
    const QColorTransferTable *t2) {
  return operator!=(*t1, *t2);
}

//  bool operator==(const QColorTransferTable &t1, const QColorTransferTable
//      &t2)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK19QColorTransferTableS1_(
    const QColorTransferTable *t1,
    const QColorTransferTable *t2) {
  return operator==(*t1, *t2);
}

//  QColorTransferTable::~QColorTransferTable()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QColorTransferTableD1Ev(QColorTransferTable *self) {
  delete self;
}
