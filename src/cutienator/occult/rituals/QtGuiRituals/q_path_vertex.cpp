//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qpathclipper_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qpathclipper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>

//  QPathVertex::QPathVertex(const QPointF &p, int e)
extern "C" Q_DECL_EXPORT
QPathVertex *ritual_ZN11QPathVertexC1ERK7QPointFi(const QPointF *p, int e) {
  return new QPathVertex(*p, e);
}

//  QPointF QPathVertex::operator QPointF() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK11QPathVertexcv7QPointFEv(const QPathVertex *self) {
  return new QPointF(self->operator QPointF());
}

//  QPathVertex::~QPathVertex()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QPathVertexD1Ev(QPathVertex *self) {
  delete self;
}
