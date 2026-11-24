//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuarange.h, Qt 6.12.0. Changes made here are lost.
#include <QtOpcUa/qopcuarange.h>
#include <QtCore/qvariant.h>

//  QOpcUaRange::QOpcUaRange()
extern "C" Q_DECL_EXPORT
QOpcUaRange *ritual_ZN11QOpcUaRangeC1Ev() {
  return new QOpcUaRange();
}

//  QOpcUaRange::QOpcUaRange(const QOpcUaRange &a0)
extern "C" Q_DECL_EXPORT
QOpcUaRange *ritual_ZN11QOpcUaRangeC1ERKS_(const QOpcUaRange *a0) {
  return new QOpcUaRange(*a0);
}

//  QOpcUaRange::QOpcUaRange(double low, double high)
extern "C" Q_DECL_EXPORT
QOpcUaRange *ritual_ZN11QOpcUaRangeC1Edd(double low, double high) {
  return new QOpcUaRange(low, high);
}

//  bool QOpcUaRange::operator==(const QOpcUaRange &rhs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QOpcUaRangeeqERKS_(
    const QOpcUaRange *self,
    const QOpcUaRange *rhs) {
  return self->operator==(*rhs);
}

//  QVariant QOpcUaRange::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK11QOpcUaRangecv8QVariantEv(const QOpcUaRange *self) {
  return new QVariant(self->operator QVariant());
}

//  QOpcUaRange::~QOpcUaRange()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QOpcUaRangeD1Ev(QOpcUaRange *self) {
  delete self;
}

//  double QOpcUaRange::low() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK11QOpcUaRange3lowEv(const QOpcUaRange *self) {
  return self->low();
}

//  void QOpcUaRange::setLow(double low)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QOpcUaRange6setLowEd(QOpcUaRange *self, double low) {
  self->setLow(low);
}

//  double QOpcUaRange::high() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK11QOpcUaRange4highEv(const QOpcUaRange *self) {
  return self->high();
}

//  void QOpcUaRange::setHigh(double high)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QOpcUaRange7setHighEd(QOpcUaRange *self, double high) {
  self->setHigh(high);
}
