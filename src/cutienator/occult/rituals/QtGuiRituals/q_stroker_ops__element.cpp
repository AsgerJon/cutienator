//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qstroker_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qstroker_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool QStrokerOps::Element::isMoveTo() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QStrokerOps7Element8isMoveToEv(
    const QStrokerOps::Element *self) {
  return self->isMoveTo();
}

//  bool QStrokerOps::Element::isLineTo() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QStrokerOps7Element8isLineToEv(
    const QStrokerOps::Element *self) {
  return self->isLineTo();
}

//  bool QStrokerOps::Element::isCurveTo() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QStrokerOps7Element9isCurveToEv(
    const QStrokerOps::Element *self) {
  return self->isCurveTo();
}

//  qfixed2d QStrokerOps::Element::operator qfixed2d()
extern "C" Q_DECL_EXPORT
qfixed2d *ritual_ZN11QStrokerOps7Elementcv8qfixed2dEv(
    QStrokerOps::Element *self) {
  return new qfixed2d(self->operator qfixed2d());
}

//  QStrokerOps::Element::~Element()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QStrokerOps7ElementD1Ev(QStrokerOps::Element *self) {
  delete self;
}
