//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/legendscroller_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/legendscroller_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>

//  const QMetaObject *LegendScroller::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14LegendScroller10metaObjectEv(
    const LegendScroller *self) {
  return self->metaObject();
}

//  void *LegendScroller::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14LegendScroller11qt_metacastEPKc(
    LegendScroller *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int LegendScroller::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14LegendScroller11qt_metacallEN11QMetaObject4CallEiPPv(
    LegendScroller *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString LegendScroller::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14LegendScroller2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(LegendScroller::tr(s, c, n));
}

//  LegendScroller::LegendScroller(QChart *chart)
extern "C" Q_DECL_EXPORT
LegendScroller *ritual_ZN14LegendScrollerC1EP6QChart(QChart *chart) {
  return new LegendScroller(chart);
}

//  void LegendScroller::paint(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN14LegendScroller5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    LegendScroller *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->paint(painter, option, widget);
}

//  void LegendScroller::setOffset(const QPointF &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN14LegendScroller9setOffsetERK7QPointF(
    LegendScroller *self,
    const QPointF *point) {
  self->setOffset(*point);
}

//  QPointF LegendScroller::offset() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK14LegendScroller6offsetEv(const LegendScroller *self) {
  return new QPointF(self->offset());
}

//  void LegendScroller::mousePressEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14LegendScroller15mousePressEventEP24QGraphicsSceneMouseEvent(
    LegendScroller *self,
    QGraphicsSceneMouseEvent *event) {
  self->mousePressEvent(event);
}

//  void LegendScroller::mouseMoveEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14LegendScroller14mouseMoveEventEP24QGraphicsSceneMouseEvent(
    LegendScroller *self,
    QGraphicsSceneMouseEvent *event) {
  self->mouseMoveEvent(event);
}

//  void LegendScroller::mouseReleaseEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14LegendScroller17mouseReleaseEventEP24QGraphicsSceneMouseEvent(
    LegendScroller *self,
    QGraphicsSceneMouseEvent *event) {
  self->mouseReleaseEvent(event);
}

//  void LegendScroller::mouseDoubleClickEvent(QGraphicsSceneMouseEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14LegendScroller21mouseDoubleClickEventEP24QGraphicsSceneMouseEvent(
    LegendScroller *self,
    QGraphicsSceneMouseEvent *event) {
  self->mouseDoubleClickEvent(event);
}

//  void LegendScroller::hoverEnterEvent(QGraphicsSceneHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14LegendScroller15hoverEnterEventEP24QGraphicsSceneHoverEvent(
    LegendScroller *self,
    QGraphicsSceneHoverEvent *event) {
  self->hoverEnterEvent(event);
}

//  void LegendScroller::hoverMoveEvent(QGraphicsSceneHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14LegendScroller14hoverMoveEventEP24QGraphicsSceneHoverEvent(
    LegendScroller *self,
    QGraphicsSceneHoverEvent *event) {
  self->hoverMoveEvent(event);
}

//  void LegendScroller::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14LegendScroller15hoverLeaveEventEP24QGraphicsSceneHoverEvent(
    LegendScroller *self,
    QGraphicsSceneHoverEvent *event) {
  self->hoverLeaveEvent(event);
}

//  void LegendScroller::handleInteractiveChanged(bool interactive)
extern "C" Q_DECL_EXPORT
void ritual_ZN14LegendScroller24handleInteractiveChangedEb(
    LegendScroller *self,
    bool interactive) {
  self->handleInteractiveChanged(interactive);
}

//  void LegendScroller::updateForResizerChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN14LegendScroller22updateForResizerChangeEv(
    LegendScroller *self) {
  self->updateForResizerChange();
}

//  void LegendScroller::handleDetached(bool attached)
extern "C" Q_DECL_EXPORT
void ritual_ZN14LegendScroller14handleDetachedEb(
    LegendScroller *self,
    bool attached) {
  self->handleDetached(attached);
}

//  LegendScroller as the Scroller it is built on
extern "C" Q_DECL_EXPORT
Scroller *ritual_cast_LegendScroller_Scroller(LegendScroller *self) {
  return static_cast<Scroller *>(self);
}

//  void LegendScroller::paint(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14LegendScroller5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    LegendScroller *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->LegendScroller::paint(painter, option, widget);
}

//  void LegendScroller::setOffset(const QPointF &point)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14LegendScroller9setOffsetERK7QPointF(
    LegendScroller *self,
    const QPointF *point) {
  self->LegendScroller::setOffset(*point);
}

//  QPointF LegendScroller::offset() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_own_ZNK14LegendScroller6offsetEv(
    const LegendScroller *self) {
  return new QPointF(self->LegendScroller::offset());
}

//  void LegendScroller::mousePressEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14LegendScroller15mousePressEventEP24QGraphicsSceneMouseEvent(
    LegendScroller *self,
    QGraphicsSceneMouseEvent *event) {
  self->LegendScroller::mousePressEvent(event);
}

//  void LegendScroller::mouseMoveEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14LegendScroller14mouseMoveEventEP24QGraphicsSceneMouseEvent(
    LegendScroller *self,
    QGraphicsSceneMouseEvent *event) {
  self->LegendScroller::mouseMoveEvent(event);
}

//  void LegendScroller::mouseReleaseEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14LegendScroller17mouseReleaseEventEP24QGraphicsSceneMouseEvent(
    LegendScroller *self,
    QGraphicsSceneMouseEvent *event) {
  self->LegendScroller::mouseReleaseEvent(event);
}

//  void LegendScroller::mouseDoubleClickEvent(QGraphicsSceneMouseEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14LegendScroller21mouseDoubleClickEventEP24QGraphicsSceneMouseEvent(
    LegendScroller *self,
    QGraphicsSceneMouseEvent *event) {
  self->LegendScroller::mouseDoubleClickEvent(event);
}

//  void LegendScroller::hoverEnterEvent(QGraphicsSceneHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14LegendScroller15hoverEnterEventEP24QGraphicsSceneHoverEvent(
    LegendScroller *self,
    QGraphicsSceneHoverEvent *event) {
  self->LegendScroller::hoverEnterEvent(event);
}

//  void LegendScroller::hoverMoveEvent(QGraphicsSceneHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14LegendScroller14hoverMoveEventEP24QGraphicsSceneHoverEvent(
    LegendScroller *self,
    QGraphicsSceneHoverEvent *event) {
  self->LegendScroller::hoverMoveEvent(event);
}

//  void LegendScroller::hoverLeaveEvent(QGraphicsSceneHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14LegendScroller15hoverLeaveEventEP24QGraphicsSceneHoverEvent(
    LegendScroller *self,
    QGraphicsSceneHoverEvent *event) {
  self->LegendScroller::hoverLeaveEvent(event);
}
