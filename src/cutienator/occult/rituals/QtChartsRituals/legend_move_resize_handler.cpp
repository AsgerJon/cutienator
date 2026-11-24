//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/legendmoveresizehandler_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/legendmoveresizehandler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>

//  LegendMoveResizeHandler::LegendMoveResizeHandler(QLegend *legend)
extern "C" Q_DECL_EXPORT
LegendMoveResizeHandler *ritual_ZN23LegendMoveResizeHandlerC1EP7QLegend(
    QLegend *legend) {
  return new LegendMoveResizeHandler(legend);
}

//  LegendMoveResizeHandler::~LegendMoveResizeHandler()
extern "C" Q_DECL_EXPORT
void ritual_ZN23LegendMoveResizeHandlerD1Ev(LegendMoveResizeHandler *self) {
  delete self;
}

//  bool LegendMoveResizeHandler::shouldShowMoveHint() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23LegendMoveResizeHandler18shouldShowMoveHintEv(
    const LegendMoveResizeHandler *self) {
  return self->shouldShowMoveHint();
}

//  void LegendMoveResizeHandler::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN23LegendMoveResizeHandler5resetEv(
    LegendMoveResizeHandler *self) {
  self->reset();
}

//  void
//      LegendMoveResizeHandler::handleMousePressEvent(QGraphicsSceneMouseEve
//      nt *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN23LegendMoveResizeHandler21handleMousePressEventEP24QGraphicsSceneMouseEvent(
    LegendMoveResizeHandler *self,
    QGraphicsSceneMouseEvent *event) {
  self->handleMousePressEvent(event);
}

//  void
//      LegendMoveResizeHandler::handleMouseMoveEvent(QGraphicsSceneMouseEven
//      t *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN23LegendMoveResizeHandler20handleMouseMoveEventEP24QGraphicsSceneMouseEvent(
    LegendMoveResizeHandler *self,
    QGraphicsSceneMouseEvent *event) {
  self->handleMouseMoveEvent(event);
}

//  void
//      LegendMoveResizeHandler::handleMouseReleaseEvent(QGraphicsSceneMouseE
//      vent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN23LegendMoveResizeHandler23handleMouseReleaseEventEP24QGraphicsSceneMouseEvent(
    LegendMoveResizeHandler *self,
    QGraphicsSceneMouseEvent *event) {
  self->handleMouseReleaseEvent(event);
}

//  void
//      LegendMoveResizeHandler::handleHoverEnterEvent(QGraphicsSceneHoverEve
//      nt *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN23LegendMoveResizeHandler21handleHoverEnterEventEP24QGraphicsSceneHoverEvent(
    LegendMoveResizeHandler *self,
    QGraphicsSceneHoverEvent *event) {
  self->handleHoverEnterEvent(event);
}

//  void
//      LegendMoveResizeHandler::handleHoverMoveEvent(QGraphicsSceneHoverEven
//      t *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN23LegendMoveResizeHandler20handleHoverMoveEventEP24QGraphicsSceneHoverEvent(
    LegendMoveResizeHandler *self,
    QGraphicsSceneHoverEvent *event) {
  self->handleHoverMoveEvent(event);
}

//  void
//      LegendMoveResizeHandler::handleHoverLeaveEvent(QGraphicsSceneHoverEve
//      nt *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN23LegendMoveResizeHandler21handleHoverLeaveEventEP24QGraphicsSceneHoverEvent(
    LegendMoveResizeHandler *self,
    QGraphicsSceneHoverEvent *event) {
  self->handleHoverLeaveEvent(event);
}

//  void LegendMoveResizeHandler::setMouseCursor()
extern "C" Q_DECL_EXPORT
void ritual_ZN23LegendMoveResizeHandler14setMouseCursorEv(
    LegendMoveResizeHandler *self) {
  self->setMouseCursor();
}

//  void LegendMoveResizeHandler::setMouseCursor(MousePosition mpos)
extern "C" Q_DECL_EXPORT
void ritual_ZN23LegendMoveResizeHandler14setMouseCursorENS_13MousePositionE(
    LegendMoveResizeHandler *self,
    LegendMoveResizeHandler::MousePosition mpos) {
  self->setMouseCursor(mpos);
}

//  void LegendMoveResizeHandler::determineMousePosition(QPointF fromPoint)
extern "C" Q_DECL_EXPORT
void ritual_ZN23LegendMoveResizeHandler22determineMousePositionE7QPointF(
    LegendMoveResizeHandler *self,
    const QPointF *fromPoint) {
  self->determineMousePosition(*fromPoint);
}
