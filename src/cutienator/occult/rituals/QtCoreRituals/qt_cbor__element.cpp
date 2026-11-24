//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qcborvalue_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qcborvalue_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QtCbor::Element::Element(qint64 v, QCborValue::Type t, ValueFlags f)
extern "C" Q_DECL_EXPORT
QtCbor::Element *ritual_ZN6QtCbor7ElementC1ExN10QCborValue4TypeE6QFlagsINS0_9ValueFlagEE(
    qint64 v,
    QCborValue::Type t,
    int f) {
  return new QtCbor::Element(
      v,
      t,
      QFlags<QtCbor::Element::ValueFlag>::fromInt(f));
}

//  QtCbor::Element::Element(QCborContainerPrivate *d, QCborValue::Type t,
//      ValueFlags f)
extern "C" Q_DECL_EXPORT
QtCbor::Element *ritual_ZN6QtCbor7ElementC1EP21QCborContainerPrivateN10QCborValue4TypeE6QFlagsINS0_9ValueFlagEE(
    QCborContainerPrivate *d,
    QCborValue::Type t,
    int f) {
  return new QtCbor::Element(
      d,
      t,
      QFlags<QtCbor::Element::ValueFlag>::fromInt(f));
}

//  double QtCbor::Element::fpvalue() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK6QtCbor7Element7fpvalueEv(const QtCbor::Element *self) {
  return self->fpvalue();
}

//  QtCbor::Element::~Element()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QtCbor7ElementD1Ev(QtCbor::Element *self) {
  delete self;
}
