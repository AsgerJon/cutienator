//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qcompare.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qcompare.h>

//  QPartialOrdering::QPartialOrdering(Qt::partial_ordering order)
extern "C" Q_DECL_EXPORT
QPartialOrdering *ritual_ZN16QPartialOrderingC1EN2Qt16partial_orderingE(
    const Qt::partial_ordering *order) {
  return new QPartialOrdering(*order);
}

//  QPartialOrdering::QPartialOrdering(Qt::weak_ordering stdorder)
extern "C" Q_DECL_EXPORT
QPartialOrdering *ritual_ZN16QPartialOrderingC1EN2Qt13weak_orderingE(
    const Qt::weak_ordering *stdorder) {
  return new QPartialOrdering(*stdorder);
}

//  QPartialOrdering::QPartialOrdering(Qt::strong_ordering stdorder)
extern "C" Q_DECL_EXPORT
QPartialOrdering *ritual_ZN16QPartialOrderingC1EN2Qt15strong_orderingE(
    const Qt::strong_ordering *stdorder) {
  return new QPartialOrdering(*stdorder);
}

//  Qt::partial_ordering QPartialOrdering::operator partial_ordering() const
extern "C" Q_DECL_EXPORT
Qt::partial_ordering *ritual_ZNK16QPartialOrderingcvN2Qt16partial_orderingEEv(
    const QPartialOrdering *self) {
  return new Qt::partial_ordering(self->operator Qt::partial_ordering());
}

//  QPartialOrdering::~QPartialOrdering()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QPartialOrderingD1Ev(QPartialOrdering *self) {
  delete self;
}
