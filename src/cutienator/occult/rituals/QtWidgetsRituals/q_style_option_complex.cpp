//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qstyleoption.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qstyleoption.h>

//  QStyleOptionComplex::QStyleOptionComplex(int version, int type)
extern "C" Q_DECL_EXPORT
QStyleOptionComplex *ritual_ZN19QStyleOptionComplexC1Eii(
    int version,
    int type) {
  return new QStyleOptionComplex(version, type);
}

//  QStyleOptionComplex::QStyleOptionComplex(const QStyleOptionComplex
//      &other)
extern "C" Q_DECL_EXPORT
QStyleOptionComplex *ritual_ZN19QStyleOptionComplexC1ERKS_(
    const QStyleOptionComplex *other) {
  return new QStyleOptionComplex(*other);
}

//  QStyleOptionComplex &QStyleOptionComplex::operator=(const
//      QStyleOptionComplex &a0)
extern "C" Q_DECL_EXPORT
QStyleOptionComplex *ritual_ZN19QStyleOptionComplexaSERKS_(
    QStyleOptionComplex *self,
    const QStyleOptionComplex *a0) {
  return &(self->operator=(*a0));
}

//  QStyleOptionComplex::~QStyleOptionComplex()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QStyleOptionComplexD1Ev(QStyleOptionComplex *self) {
  delete self;
}
