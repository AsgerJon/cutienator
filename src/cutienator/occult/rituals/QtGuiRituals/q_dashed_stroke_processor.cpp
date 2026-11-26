//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qtriangulatingstroker_p.h, Qt 6.12.0. Edited
//  by hand on 2026-11-25: added by hand, rituals for functions the generator
//  leaves out: 1. Kept as it is when the generator runs again.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtriangulatingstroker_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpen.h>
#include <QtCore/qrect.h>

//  QDashedStrokeProcessor::QDashedStrokeProcessor()
extern "C" Q_DECL_EXPORT
QDashedStrokeProcessor *ritual_ZN22QDashedStrokeProcessorC1Ev() {
  return new QDashedStrokeProcessor();
}

//  void QDashedStrokeProcessor::process(const QVectorPath &path, const QPen
//      &pen, const QRectF &clip, QPainter::RenderHints hints)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDashedStrokeProcessor7processERK11QVectorPathRK4QPenRK6QRectF6QFlagsIN8QPainter10RenderHintEE(
    QDashedStrokeProcessor *self,
    const QVectorPath *path,
    const QPen *pen,
    const QRectF *clip,
    int hints) {
  self->process(
      *path,
      *pen,
      *clip,
      QFlags<QPainter::RenderHint>::fromInt(hints));
}

//  void QDashedStrokeProcessor::addElement(QPainterPath::ElementType type,
//      qreal x, qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDashedStrokeProcessor10addElementEN12QPainterPath11ElementTypeEdd(
    QDashedStrokeProcessor *self,
    QPainterPath::ElementType type,
    qreal x,
    qreal y) {
  self->addElement(type, x, y);
}

//  int QDashedStrokeProcessor::elementCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QDashedStrokeProcessor12elementCountEv(
    const QDashedStrokeProcessor *self) {
  return self->elementCount();
}

//  QPainterPath::ElementType *QDashedStrokeProcessor::elementTypes() const
extern "C" Q_DECL_EXPORT
QPainterPath::ElementType *ritual_ZNK22QDashedStrokeProcessor12elementTypesEv(
    const QDashedStrokeProcessor *self) {
  return self->elementTypes();
}

//  void QDashedStrokeProcessor::setInvScale(qreal invScale)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDashedStrokeProcessor11setInvScaleEd(
    QDashedStrokeProcessor *self,
    qreal invScale) {
  self->setInvScale(invScale);
}

//  qreal *QDashedStrokeProcessor::points() const
extern "C" Q_DECL_EXPORT
qreal *ritual_ZNK22QDashedStrokeProcessor6pointsEv(
    const QDashedStrokeProcessor *self) {
  return self->points();
}
