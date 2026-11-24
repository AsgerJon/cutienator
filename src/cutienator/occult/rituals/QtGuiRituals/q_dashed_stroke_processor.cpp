//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qtriangulatingstroker_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtriangulatingstroker_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QDashedStrokeProcessor::QDashedStrokeProcessor()
extern "C" Q_DECL_EXPORT
QDashedStrokeProcessor *ritual_ZN22QDashedStrokeProcessorC1Ev() {
  return new QDashedStrokeProcessor();
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

//  void QDashedStrokeProcessor::setInvScale(qreal invScale)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDashedStrokeProcessor11setInvScaleEd(
    QDashedStrokeProcessor *self,
    qreal invScale) {
  self->setInvScale(invScale);
}
