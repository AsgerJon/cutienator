//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qpaintengine.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qpaintengine.h>
#include <QtGui/qpen.h>
#include <QtGui/qbrush.h>
#include <QtCore/qpoint.h>
#include <QtGui/qfont.h>
#include <QtGui/qtransform.h>
#include <QtGui/qregion.h>
#include <QtGui/qpainterpath.h>

//  QPaintEngine::DirtyFlags QPaintEngineState::state() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QPaintEngineState5stateEv(const QPaintEngineState *self) {
  return static_cast<int>(self->state().toInt());
}

//  QPen QPaintEngineState::pen() const
extern "C" Q_DECL_EXPORT
QPen *ritual_ZNK17QPaintEngineState3penEv(const QPaintEngineState *self) {
  return new QPen(self->pen());
}

//  QBrush QPaintEngineState::brush() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK17QPaintEngineState5brushEv(
    const QPaintEngineState *self) {
  return new QBrush(self->brush());
}

//  QPointF QPaintEngineState::brushOrigin() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK17QPaintEngineState11brushOriginEv(
    const QPaintEngineState *self) {
  return new QPointF(self->brushOrigin());
}

//  QBrush QPaintEngineState::backgroundBrush() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK17QPaintEngineState15backgroundBrushEv(
    const QPaintEngineState *self) {
  return new QBrush(self->backgroundBrush());
}

//  Qt::BGMode QPaintEngineState::backgroundMode() const
extern "C" Q_DECL_EXPORT
Qt::BGMode ritual_ZNK17QPaintEngineState14backgroundModeEv(
    const QPaintEngineState *self) {
  return self->backgroundMode();
}

//  QFont QPaintEngineState::font() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK17QPaintEngineState4fontEv(const QPaintEngineState *self) {
  return new QFont(self->font());
}

//  QTransform QPaintEngineState::transform() const
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZNK17QPaintEngineState9transformEv(
    const QPaintEngineState *self) {
  return new QTransform(self->transform());
}

//  Qt::ClipOperation QPaintEngineState::clipOperation() const
extern "C" Q_DECL_EXPORT
Qt::ClipOperation ritual_ZNK17QPaintEngineState13clipOperationEv(
    const QPaintEngineState *self) {
  return self->clipOperation();
}

//  QRegion QPaintEngineState::clipRegion() const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK17QPaintEngineState10clipRegionEv(
    const QPaintEngineState *self) {
  return new QRegion(self->clipRegion());
}

//  QPainterPath QPaintEngineState::clipPath() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK17QPaintEngineState8clipPathEv(
    const QPaintEngineState *self) {
  return new QPainterPath(self->clipPath());
}

//  bool QPaintEngineState::isClipEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QPaintEngineState13isClipEnabledEv(
    const QPaintEngineState *self) {
  return self->isClipEnabled();
}

//  QPainter::RenderHints QPaintEngineState::renderHints() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QPaintEngineState11renderHintsEv(
    const QPaintEngineState *self) {
  return static_cast<int>(self->renderHints().toInt());
}

//  QPainter::CompositionMode QPaintEngineState::compositionMode() const
extern "C" Q_DECL_EXPORT
QPainter::CompositionMode ritual_ZNK17QPaintEngineState15compositionModeEv(
    const QPaintEngineState *self) {
  return self->compositionMode();
}

//  qreal QPaintEngineState::opacity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QPaintEngineState7opacityEv(
    const QPaintEngineState *self) {
  return self->opacity();
}

//  QPainter *QPaintEngineState::painter() const
extern "C" Q_DECL_EXPORT
QPainter *ritual_ZNK17QPaintEngineState7painterEv(
    const QPaintEngineState *self) {
  return self->painter();
}

//  bool QPaintEngineState::brushNeedsResolving() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QPaintEngineState19brushNeedsResolvingEv(
    const QPaintEngineState *self) {
  return self->brushNeedsResolving();
}

//  bool QPaintEngineState::penNeedsResolving() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QPaintEngineState17penNeedsResolvingEv(
    const QPaintEngineState *self) {
  return self->penNeedsResolving();
}

//  QPaintEngineState::~QPaintEngineState()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPaintEngineStateD1Ev(QPaintEngineState *self) {
  delete self;
}
