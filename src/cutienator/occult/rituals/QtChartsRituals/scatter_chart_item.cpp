//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/scatterchartitem_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCharts/qchartglobal.h>
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#if QT_CONFIG(charts_scatter_chart)
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/scatterchartitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtGui/qpen.h>
#include <QtGui/qbrush.h>

//  Only a class built on ScatterChartItem may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnScatterChartItem : ScatterChartItem {
  using ScatterChartItem::updateGeometry;
  using ScatterChartItem::mousePressEvent;
  using ScatterChartItem::hoverMoveEvent;
  using ScatterChartItem::mouseReleaseEvent;
  using ScatterChartItem::mouseDoubleClickEvent;
};

//  const QMetaObject *ScatterChartItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16ScatterChartItem10metaObjectEv(
    const ScatterChartItem *self) {
  return self->metaObject();
}

//  QString ScatterChartItem::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16ScatterChartItem2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(ScatterChartItem::tr(s, c, n));
}

//  ScatterChartItem::ScatterChartItem(QScatterSeries *series, QGraphicsItem
//      *item)
extern "C" Q_DECL_EXPORT
ScatterChartItem *ritual_ZN16ScatterChartItemC1EP14QScatterSeriesP13QGraphicsItem(
    QScatterSeries *series,
    QGraphicsItem *item) {
  return new ScatterChartItem(series, item);
}

//  QRectF ScatterChartItem::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK16ScatterChartItem12boundingRectEv(
    const ScatterChartItem *self) {
  return new QRectF(self->boundingRect());
}

//  void ScatterChartItem::paint(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN16ScatterChartItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    ScatterChartItem *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->paint(painter, option, widget);
}

//  void ScatterChartItem::setPen(const QPen &pen)
extern "C" Q_DECL_EXPORT
void ritual_ZN16ScatterChartItem6setPenERK4QPen(
    ScatterChartItem *self,
    const QPen *pen) {
  self->setPen(*pen);
}

//  void ScatterChartItem::setBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN16ScatterChartItem8setBrushERK6QBrush(
    ScatterChartItem *self,
    const QBrush *brush) {
  self->setBrush(*brush);
}

//  void ScatterChartItem::markerSelected(QGraphicsItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN16ScatterChartItem14markerSelectedEP13QGraphicsItem(
    ScatterChartItem *self,
    QGraphicsItem *item) {
  self->markerSelected(item);
}

//  void ScatterChartItem::markerHovered(QGraphicsItem *item, bool state)
extern "C" Q_DECL_EXPORT
void ritual_ZN16ScatterChartItem13markerHoveredEP13QGraphicsItemb(
    ScatterChartItem *self,
    QGraphicsItem *item,
    bool state) {
  self->markerHovered(item, state);
}

//  void ScatterChartItem::markerPressed(QGraphicsItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN16ScatterChartItem13markerPressedEP13QGraphicsItem(
    ScatterChartItem *self,
    QGraphicsItem *item) {
  self->markerPressed(item);
}

//  void ScatterChartItem::markerReleased(QGraphicsItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN16ScatterChartItem14markerReleasedEP13QGraphicsItem(
    ScatterChartItem *self,
    QGraphicsItem *item) {
  self->markerReleased(item);
}

//  void ScatterChartItem::markerDoubleClicked(QGraphicsItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN16ScatterChartItem19markerDoubleClickedEP13QGraphicsItem(
    ScatterChartItem *self,
    QGraphicsItem *item) {
  self->markerDoubleClicked(item);
}

//  void ScatterChartItem::handleMarkerMouseReleaseEvent(QGraphicsItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN16ScatterChartItem29handleMarkerMouseReleaseEventEP13QGraphicsItem(
    ScatterChartItem *self,
    QGraphicsItem *item) {
  self->handleMarkerMouseReleaseEvent(item);
}

//  void ScatterChartItem::setMousePressed(bool pressed)
extern "C" Q_DECL_EXPORT
void ritual_ZN16ScatterChartItem15setMousePressedEb(
    ScatterChartItem *self,
    bool pressed) {
  self->setMousePressed(pressed);
}

//  bool ScatterChartItem::mousePressed()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16ScatterChartItem12mousePressedEv(ScatterChartItem *self) {
  return self->mousePressed();
}

//  void ScatterChartItem::handleSeriesUpdated()
extern "C" Q_DECL_EXPORT
void ritual_ZN16ScatterChartItem19handleSeriesUpdatedEv(
    ScatterChartItem *self) {
  self->handleSeriesUpdated();
}

//  void ScatterChartItem::createPoints(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN16ScatterChartItem12createPointsEi(
    ScatterChartItem *self,
    int count) {
  self->createPoints(count);
}

//  void ScatterChartItem::deletePoints(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN16ScatterChartItem12deletePointsEi(
    ScatterChartItem *self,
    int count) {
  self->deletePoints(count);
}

//  void ScatterChartItem::resizeMarker(QGraphicsItem *marker, const int
//      size)
extern "C" Q_DECL_EXPORT
void ritual_ZN16ScatterChartItem12resizeMarkerEP13QGraphicsItemi(
    ScatterChartItem *self,
    QGraphicsItem *marker,
    int size) {
  self->resizeMarker(marker, size);
}

//  void ScatterChartItem::updateGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN16ScatterChartItem14updateGeometryEv(ScatterChartItem *self) {
  self->updateGeometry();
}

//  void ScatterChartItem::mousePressEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16ScatterChartItem15mousePressEventEP24QGraphicsSceneMouseEvent(
    ScatterChartItem *self,
    QGraphicsSceneMouseEvent *event) {
  self->mousePressEvent(event);
}

//  void ScatterChartItem::hoverMoveEvent(QGraphicsSceneHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16ScatterChartItem14hoverMoveEventEP24QGraphicsSceneHoverEvent(
    ScatterChartItem *self,
    QGraphicsSceneHoverEvent *event) {
  self->hoverMoveEvent(event);
}

//  void ScatterChartItem::mouseReleaseEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16ScatterChartItem17mouseReleaseEventEP24QGraphicsSceneMouseEvent(
    ScatterChartItem *self,
    QGraphicsSceneMouseEvent *event) {
  self->mouseReleaseEvent(event);
}

//  void ScatterChartItem::mouseDoubleClickEvent(QGraphicsSceneMouseEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN16ScatterChartItem21mouseDoubleClickEventEP24QGraphicsSceneMouseEvent(
    ScatterChartItem *self,
    QGraphicsSceneMouseEvent *event) {
  self->mouseDoubleClickEvent(event);
}

//  QRectF ScatterChartItem::boundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK16ScatterChartItem12boundingRectEv(
    const ScatterChartItem *self) {
  return new QRectF(self->ScatterChartItem::boundingRect());
}

//  void ScatterChartItem::paint(QPainter *painter, const
//      QStyleOptionGraphicsItem *option, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16ScatterChartItem5paintEP8QPainterPK24QStyleOptionGraphicsItemP7QWidget(
    ScatterChartItem *self,
    QPainter *painter,
    const QStyleOptionGraphicsItem *option,
    QWidget *widget) {
  self->ScatterChartItem::paint(painter, option, widget);
}

//  void ScatterChartItem::handleSeriesUpdated()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16ScatterChartItem19handleSeriesUpdatedEv(
    ScatterChartItem *self) {
  self->ScatterChartItem::handleSeriesUpdated();
}

//  void ScatterChartItem::updateGeometry()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16ScatterChartItem14updateGeometryEv(
    ScatterChartItem *self) {
  static_cast<OwnScatterChartItem *>(self)->OwnScatterChartItem::updateGeometry();
}

//  void ScatterChartItem::mousePressEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16ScatterChartItem15mousePressEventEP24QGraphicsSceneMouseEvent(
    ScatterChartItem *self,
    QGraphicsSceneMouseEvent *event) {
  static_cast<OwnScatterChartItem *>(self)->OwnScatterChartItem::mousePressEvent(
      event);
}

//  void ScatterChartItem::hoverMoveEvent(QGraphicsSceneHoverEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16ScatterChartItem14hoverMoveEventEP24QGraphicsSceneHoverEvent(
    ScatterChartItem *self,
    QGraphicsSceneHoverEvent *event) {
  static_cast<OwnScatterChartItem *>(self)->OwnScatterChartItem::hoverMoveEvent(
      event);
}

//  void ScatterChartItem::mouseReleaseEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16ScatterChartItem17mouseReleaseEventEP24QGraphicsSceneMouseEvent(
    ScatterChartItem *self,
    QGraphicsSceneMouseEvent *event) {
  static_cast<OwnScatterChartItem *>(self)->OwnScatterChartItem::mouseReleaseEvent(
      event);
}

//  void ScatterChartItem::mouseDoubleClickEvent(QGraphicsSceneMouseEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16ScatterChartItem21mouseDoubleClickEventEP24QGraphicsSceneMouseEvent(
    ScatterChartItem *self,
    QGraphicsSceneMouseEvent *event) {
  static_cast<OwnScatterChartItem *>(self)->OwnScatterChartItem::mouseDoubleClickEvent(
      event);
}

#endif  // QT_CONFIG(charts_scatter_chart)
