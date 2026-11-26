//  Written by dev_tooling.RitualGenerator from the records of
//  QtCharts/6.12.0/QtCharts/private/scroller_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCharts/6.12.0/QtCharts/private/qchartglobal_p.h>
#include <QtCharts/QtCharts>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCharts/6.12.0/QtCharts/private/scroller_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <cstring>

//  A Scroller that Python can take functions over in. Every Scroller
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteScrollerCall0)(const void *, const QPointF *, int *);
typedef const QPointF * (*CuteScrollerCall1)(const void *, int *);
class CuteScroller : public Scroller {
public:
  using Scroller::Scroller;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Scroller9setOffsetERK7QPointF")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8Scroller6offsetEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void Scroller::setOffset(const QPointF &point)
  void setOffset(const QPointF &point) override {
    if (taken[0]) {
      int handled = 0;
      CuteScrollerCall0 call = reinterpret_cast<CuteScrollerCall0>(taken[0]);
      call(this, &point, &handled);
      if (handled) return;
    }
  }

  //  QPointF Scroller::offset() const
  QPointF offset() const override {
    if (taken[1]) {
      int handled = 0;
      CuteScrollerCall1 call = reinterpret_cast<CuteScrollerCall1>(taken[1]);
      const QPointF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
};

//  Scroller::Scroller()
extern "C" Q_DECL_EXPORT
Scroller *ritual_ZN8ScrollerC1Ev() {
  return new CuteScroller();
}

//  Scroller::~Scroller()
extern "C" Q_DECL_EXPORT
void ritual_ZN8ScrollerD1Ev(Scroller *self) {
  delete self;
}

//  void Scroller::setOffset(const QPointF &point)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Scroller9setOffsetERK7QPointF(
    Scroller *self,
    const QPointF *point) {
  self->setOffset(*point);
}

//  QPointF Scroller::offset() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK8Scroller6offsetEv(const Scroller *self) {
  return new QPointF(self->offset());
}

//  void Scroller::move(const QPointF &delta)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Scroller4moveERK7QPointF(
    Scroller *self,
    const QPointF *delta) {
  self->move(*delta);
}

//  void Scroller::scrollTo(const QPointF &delta)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Scroller8scrollToERK7QPointF(
    Scroller *self,
    const QPointF *delta) {
  self->scrollTo(*delta);
}

//  void Scroller::handleMousePressEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Scroller21handleMousePressEventEP24QGraphicsSceneMouseEvent(
    Scroller *self,
    QGraphicsSceneMouseEvent *event) {
  self->handleMousePressEvent(event);
}

//  void Scroller::handleMouseMoveEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Scroller20handleMouseMoveEventEP24QGraphicsSceneMouseEvent(
    Scroller *self,
    QGraphicsSceneMouseEvent *event) {
  self->handleMouseMoveEvent(event);
}

//  void Scroller::handleMouseReleaseEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Scroller23handleMouseReleaseEventEP24QGraphicsSceneMouseEvent(
    Scroller *self,
    QGraphicsSceneMouseEvent *event) {
  self->handleMouseReleaseEvent(event);
}

//  void Scroller::scrollTick()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Scroller10scrollTickEv(Scroller *self) {
  self->scrollTick();
}

//  void Scroller::startTicker(int interval)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Scroller11startTickerEi(Scroller *self, int interval) {
  self->startTicker(interval);
}

//  void Scroller::stopTicker()
extern "C" Q_DECL_EXPORT
void ritual_ZN8Scroller10stopTickerEv(Scroller *self) {
  self->stopTicker();
}

//  void Scroller::lowerSpeed(QPointF &speed, qreal maxSpeed)
extern "C" Q_DECL_EXPORT
void ritual_ZN8Scroller10lowerSpeedER7QPointFd(
    Scroller *self,
    QPointF *speed,
    qreal maxSpeed) {
  self->lowerSpeed(*speed, maxSpeed);
}

//  a Python function taken by a CuteScroller, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_Scroller(Scroller *self, const char *key, void *call) {
  return static_cast<CuteScroller *>(self)->take(key, call);
}
