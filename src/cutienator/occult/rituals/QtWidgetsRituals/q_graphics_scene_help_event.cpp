//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicssceneevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgraphicssceneevent.h>
#include <QtCore/qpoint.h>
#include <cstring>

//  A QGraphicsSceneHelpEvent that Python can take functions over in. Every QGraphicsSceneHelpEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQGraphicsSceneHelpEventCall0)(const void *, bool, int *);
typedef void * (*CuteQGraphicsSceneHelpEventCall1)(const void *, int *);
class CuteQGraphicsSceneHelpEvent : public QGraphicsSceneHelpEvent {
public:
  using QGraphicsSceneHelpEvent::QGraphicsSceneHelpEvent;
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
      CuteQGraphicsSceneHelpEventCall0 call = reinterpret_cast<CuteQGraphicsSceneHelpEventCall0>(taken[0]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }

  //  QEvent *QEvent::clone() const
  QEvent *clone() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQGraphicsSceneHelpEventCall1 call = reinterpret_cast<CuteQGraphicsSceneHelpEventCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QEvent *>(given);
    }
    return QEvent::clone();
  }
};

//  QGraphicsSceneHelpEvent::QGraphicsSceneHelpEvent(Type type)
extern "C" Q_DECL_EXPORT
QGraphicsSceneHelpEvent *ritual_ZN23QGraphicsSceneHelpEventC1EN6QEvent4TypeE(
    QEvent::Type type) {
  return new CuteQGraphicsSceneHelpEvent(type);
}

//  QGraphicsSceneHelpEvent::~QGraphicsSceneHelpEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGraphicsSceneHelpEventD1Ev(QGraphicsSceneHelpEvent *self) {
  delete self;
}

//  QPointF QGraphicsSceneHelpEvent::scenePos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK23QGraphicsSceneHelpEvent8scenePosEv(
    const QGraphicsSceneHelpEvent *self) {
  return new QPointF(self->scenePos());
}

//  void QGraphicsSceneHelpEvent::setScenePos(const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGraphicsSceneHelpEvent11setScenePosERK7QPointF(
    QGraphicsSceneHelpEvent *self,
    const QPointF *pos) {
  self->setScenePos(*pos);
}

//  QPoint QGraphicsSceneHelpEvent::screenPos() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK23QGraphicsSceneHelpEvent9screenPosEv(
    const QGraphicsSceneHelpEvent *self) {
  return new QPoint(self->screenPos());
}

//  void QGraphicsSceneHelpEvent::setScreenPos(const QPoint &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGraphicsSceneHelpEvent12setScreenPosERK6QPoint(
    QGraphicsSceneHelpEvent *self,
    const QPoint *pos) {
  self->setScreenPos(*pos);
}

//  a Python function taken by a CuteQGraphicsSceneHelpEvent, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphicsSceneHelpEvent(
    QGraphicsSceneHelpEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphicsSceneHelpEvent *>(self)->take(key, call);
}
