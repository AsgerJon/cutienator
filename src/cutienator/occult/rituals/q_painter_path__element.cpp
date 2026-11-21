//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qpainterpath.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qpainterpath.h>
#include <QtCore/qpoint.h>

//  bool QPainterPath::Element::isMoveTo() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QPainterPath7Element8isMoveToEv(
    const QPainterPath::Element *self) {
  return self->isMoveTo();
}

//  bool QPainterPath::Element::isLineTo() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QPainterPath7Element8isLineToEv(
    const QPainterPath::Element *self) {
  return self->isLineTo();
}

//  bool QPainterPath::Element::isCurveTo() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QPainterPath7Element9isCurveToEv(
    const QPainterPath::Element *self) {
  return self->isCurveTo();
}

//  QPointF QPainterPath::Element::operator QPointF() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK12QPainterPath7Elementcv7QPointFEv(
    const QPainterPath::Element *self) {
  return new QPointF(self->operator QPointF());
}

//  bool QPainterPath::Element::operator==(const Element &e) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QPainterPath7ElementeqERKS0_(
    const QPainterPath::Element *self,
    const QPainterPath::Element *e) {
  return self->operator==(*e);
}

//  bool QPainterPath::Element::operator!=(const Element &e) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QPainterPath7ElementneERKS0_(
    const QPainterPath::Element *self,
    const QPainterPath::Element *e) {
  return self->operator!=(*e);
}

//  QPainterPath::Element::~Element()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPainterPath7ElementD1Ev(QPainterPath::Element *self) {
  delete self;
}
