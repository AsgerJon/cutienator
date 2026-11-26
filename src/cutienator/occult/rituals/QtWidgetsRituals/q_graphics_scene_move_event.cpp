//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicssceneevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
#include <QtWidgets/qgraphicssceneevent.h>
#include <QtCore/qpoint.h>
#include <cstring>

//  A QGraphicsSceneMoveEvent that Python can take functions over in. Every QGraphicsSceneMoveEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQGraphicsSceneMoveEventCall0)(const void *, bool, int *);
typedef void * (*CuteQGraphicsSceneMoveEventCall1)(const void *, int *);
class CuteQGraphicsSceneMoveEvent : public QGraphicsSceneMoveEvent {
public:
  using QGraphicsSceneMoveEvent::QGraphicsSceneMoveEvent;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN6QEvent11setAcceptedEb")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK6QEvent5cloneEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void QEvent::setAccepted(bool accepted)
  void setAccepted(bool accepted) override {
    if (taken[0]) {
      int handled = 0;
      CuteQGraphicsSceneMoveEventCall0 call = reinterpret_cast<CuteQGraphicsSceneMoveEventCall0>(taken[0]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }

  //  QEvent *QEvent::clone() const
  QEvent *clone() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQGraphicsSceneMoveEventCall1 call = reinterpret_cast<CuteQGraphicsSceneMoveEventCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QEvent *>(given);
    }
    return QEvent::clone();
  }
};

//  QGraphicsSceneMoveEventPrivate *QGraphicsSceneMoveEvent::d_func()
extern "C" Q_DECL_EXPORT
QGraphicsSceneMoveEventPrivate *ritual_ZN23QGraphicsSceneMoveEvent6d_funcEv(
    QGraphicsSceneMoveEvent *self) {
  return self->d_func();
}

//  const QGraphicsSceneMoveEventPrivate *QGraphicsSceneMoveEvent::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QGraphicsSceneMoveEventPrivate *ritual_ZNK23QGraphicsSceneMoveEvent6d_funcEv(
    const QGraphicsSceneMoveEvent *self) {
  return self->d_func();
}

//  QGraphicsSceneMoveEvent::QGraphicsSceneMoveEvent()
extern "C" Q_DECL_EXPORT
QGraphicsSceneMoveEvent *ritual_ZN23QGraphicsSceneMoveEventC1Ev() {
  return new CuteQGraphicsSceneMoveEvent();
}

//  QGraphicsSceneMoveEvent::~QGraphicsSceneMoveEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGraphicsSceneMoveEventD1Ev(QGraphicsSceneMoveEvent *self) {
  delete self;
}

//  QPointF QGraphicsSceneMoveEvent::oldPos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK23QGraphicsSceneMoveEvent6oldPosEv(
    const QGraphicsSceneMoveEvent *self) {
  return new QPointF(self->oldPos());
}

//  void QGraphicsSceneMoveEvent::setOldPos(const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGraphicsSceneMoveEvent9setOldPosERK7QPointF(
    QGraphicsSceneMoveEvent *self,
    const QPointF *pos) {
  self->setOldPos(*pos);
}

//  QPointF QGraphicsSceneMoveEvent::newPos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK23QGraphicsSceneMoveEvent6newPosEv(
    const QGraphicsSceneMoveEvent *self) {
  return new QPointF(self->newPos());
}

//  void QGraphicsSceneMoveEvent::setNewPos(const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGraphicsSceneMoveEvent9setNewPosERK7QPointF(
    QGraphicsSceneMoveEvent *self,
    const QPointF *pos) {
  self->setNewPos(*pos);
}

//  a Python function taken by a CuteQGraphicsSceneMoveEvent, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphicsSceneMoveEvent(
    QGraphicsSceneMoveEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphicsSceneMoveEvent *>(self)->take(key, call);
}

#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicsview)
