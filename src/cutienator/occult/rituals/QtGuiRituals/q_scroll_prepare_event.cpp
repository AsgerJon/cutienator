//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qevent.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <cstring>

//  A QScrollPrepareEvent that Python can take functions over in. Every QScrollPrepareEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQScrollPrepareEventCall0)(const void *, int *);
typedef void (*CuteQScrollPrepareEventCall1)(const void *, bool, int *);
class CuteQScrollPrepareEvent : public QScrollPrepareEvent {
public:
  using QScrollPrepareEvent::QScrollPrepareEvent;
  CuteQScrollPrepareEvent(const QScrollPrepareEvent & other) : QScrollPrepareEvent(other) {}
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK6QEvent5cloneEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN6QEvent11setAcceptedEb")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  QScrollPrepareEvent *QScrollPrepareEvent::clone() const
  QScrollPrepareEvent *clone() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQScrollPrepareEventCall0 call = reinterpret_cast<CuteQScrollPrepareEventCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QScrollPrepareEvent *>(given);
    }
    return QScrollPrepareEvent::clone();
  }

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[1]) {
      int handled = 0;
      CuteQScrollPrepareEventCall1 call = reinterpret_cast<CuteQScrollPrepareEventCall1>(taken[1]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }
};

//  QScrollPrepareEvent::QScrollPrepareEvent(const QScrollPrepareEvent &a0)
extern "C" Q_DECL_EXPORT
QScrollPrepareEvent *ritual_ZN19QScrollPrepareEventC1ERKS_(
    const QScrollPrepareEvent *a0) {
  return new CuteQScrollPrepareEvent(*a0);
}

//  QScrollPrepareEvent &QScrollPrepareEvent::operator=(const
//      QScrollPrepareEvent &other)
extern "C" Q_DECL_EXPORT
QScrollPrepareEvent *ritual_ZN19QScrollPrepareEventaSERKS_(
    QScrollPrepareEvent *self,
    const QScrollPrepareEvent *other) {
  return &(self->operator=(*other));
}

//  QScrollPrepareEvent *QScrollPrepareEvent::clone() const
extern "C" Q_DECL_EXPORT
QScrollPrepareEvent *ritual_ZNK19QScrollPrepareEvent5cloneEv(
    const QScrollPrepareEvent *self) {
  return self->clone();
}

//  QScrollPrepareEvent::~QScrollPrepareEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QScrollPrepareEventD1Ev(QScrollPrepareEvent *self) {
  delete self;
}

//  QScrollPrepareEvent::QScrollPrepareEvent(const QPointF &startPos)
extern "C" Q_DECL_EXPORT
QScrollPrepareEvent *ritual_ZN19QScrollPrepareEventC1ERK7QPointF(
    const QPointF *startPos) {
  return new CuteQScrollPrepareEvent(*startPos);
}

//  QPointF QScrollPrepareEvent::startPos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK19QScrollPrepareEvent8startPosEv(
    const QScrollPrepareEvent *self) {
  return new QPointF(self->startPos());
}

//  QSizeF QScrollPrepareEvent::viewportSize() const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK19QScrollPrepareEvent12viewportSizeEv(
    const QScrollPrepareEvent *self) {
  return new QSizeF(self->viewportSize());
}

//  QRectF QScrollPrepareEvent::contentPosRange() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK19QScrollPrepareEvent15contentPosRangeEv(
    const QScrollPrepareEvent *self) {
  return new QRectF(self->contentPosRange());
}

//  QPointF QScrollPrepareEvent::contentPos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK19QScrollPrepareEvent10contentPosEv(
    const QScrollPrepareEvent *self) {
  return new QPointF(self->contentPos());
}

//  void QScrollPrepareEvent::setViewportSize(const QSizeF &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QScrollPrepareEvent15setViewportSizeERK6QSizeF(
    QScrollPrepareEvent *self,
    const QSizeF *size) {
  self->setViewportSize(*size);
}

//  void QScrollPrepareEvent::setContentPosRange(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QScrollPrepareEvent18setContentPosRangeERK6QRectF(
    QScrollPrepareEvent *self,
    const QRectF *rect) {
  self->setContentPosRange(*rect);
}

//  void QScrollPrepareEvent::setContentPos(const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QScrollPrepareEvent13setContentPosERK7QPointF(
    QScrollPrepareEvent *self,
    const QPointF *pos) {
  self->setContentPos(*pos);
}

//  a Python function taken by a CuteQScrollPrepareEvent, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QScrollPrepareEvent(
    QScrollPrepareEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQScrollPrepareEvent *>(self)->take(key, call);
}

//  QScrollPrepareEvent *QScrollPrepareEvent::clone() const
extern "C" Q_DECL_EXPORT
QScrollPrepareEvent *ritual_own_ZNK19QScrollPrepareEvent5cloneEv(
    const QScrollPrepareEvent *self) {
  return self->QScrollPrepareEvent::clone();
}
