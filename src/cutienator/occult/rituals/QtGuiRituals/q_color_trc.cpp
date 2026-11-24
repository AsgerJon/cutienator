//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qcolortrc_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qcolortrc_p.h>
#include <QtGui/6.12.0/QtGui/private/qcolortransferfunction_p.h>
#include <QtGui/6.12.0/QtGui/private/qcolortransfertable_p.h>
#include <QtGui/6.12.0/QtGui/private/qcolortransfergeneric_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QColorTrc::QColorTrc()
extern "C" Q_DECL_EXPORT
QColorTrc *ritual_ZN9QColorTrcC1Ev() {
  return new QColorTrc();
}

//  QColorTrc::QColorTrc(const QColorTransferFunction &fun)
extern "C" Q_DECL_EXPORT
QColorTrc *ritual_ZN9QColorTrcC1ERK22QColorTransferFunction(
    const QColorTransferFunction *fun) {
  return new QColorTrc(*fun);
}

//  QColorTrc::QColorTrc(const QColorTransferTable &table)
extern "C" Q_DECL_EXPORT
QColorTrc *ritual_ZN9QColorTrcC1ERK19QColorTransferTable(
    const QColorTransferTable *table) {
  return new QColorTrc(*table);
}

//  QColorTrc::QColorTrc(const QColorTransferGenericFunction &hdr)
extern "C" Q_DECL_EXPORT
QColorTrc *ritual_ZN9QColorTrcC1ERK29QColorTransferGenericFunction(
    const QColorTransferGenericFunction *hdr) {
  return new QColorTrc(*hdr);
}

//  bool QColorTrc::isIdentity() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QColorTrc10isIdentityEv(const QColorTrc *self) {
  return self->isIdentity();
}

//  bool QColorTrc::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QColorTrc7isValidEv(const QColorTrc *self) {
  return self->isValid();
}

//  float QColorTrc::apply(float x) const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9QColorTrc5applyEf(const QColorTrc *self, float x) {
  return self->apply(x);
}

//  float QColorTrc::applyExtended(float x) const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9QColorTrc13applyExtendedEf(const QColorTrc *self, float x) {
  return self->applyExtended(x);
}

//  float QColorTrc::applyInverse(float x) const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9QColorTrc12applyInverseEf(const QColorTrc *self, float x) {
  return self->applyInverse(x);
}

//  float QColorTrc::applyInverseExtended(float x) const
extern "C" Q_DECL_EXPORT
float ritual_ZNK9QColorTrc20applyInverseExtendedEf(
    const QColorTrc *self,
    float x) {
  return self->applyInverseExtended(x);
}

//  const QColorTransferTable &QColorTrc::table() const
extern "C" Q_DECL_EXPORT
QColorTransferTable *ritual_ZNK9QColorTrc5tableEv(const QColorTrc *self) {
  return new QColorTransferTable(self->table());
}

//  const QColorTransferFunction &QColorTrc::fun() const
extern "C" Q_DECL_EXPORT
QColorTransferFunction *ritual_ZNK9QColorTrc3funEv(const QColorTrc *self) {
  return new QColorTransferFunction(self->fun());
}

//  const QColorTransferGenericFunction &QColorTrc::hdr() const
extern "C" Q_DECL_EXPORT
QColorTransferGenericFunction *ritual_ZNK9QColorTrc3hdrEv(
    const QColorTrc *self) {
  return new QColorTransferGenericFunction(self->hdr());
}

//  Type QColorTrc::type() const
extern "C" Q_DECL_EXPORT
QColorTrc::Type ritual_ZNK9QColorTrc4typeEv(const QColorTrc *self) {
  return self->type();
}

//  bool operator==(const QColorTrc &lhs, const QColorTrc &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK9QColorTrcS1_(const QColorTrc *lhs, const QColorTrc *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QColorTrc &lhs, const QColorTrc &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK9QColorTrcS1_(const QColorTrc *lhs, const QColorTrc *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QColorTrc::~QColorTrc()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QColorTrcD1Ev(QColorTrc *self) {
  delete self;
}
