//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicssceneevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(graphicsview)
#include <QtWidgets/qgraphicssceneevent.h>
#include <QtCore/qpoint.h>
#include <cstring>

//  A QGraphicsSceneHoverEvent that Python can take functions over in. Every QGraphicsSceneHoverEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQGraphicsSceneHoverEventCall0)(const void *, bool, int *);
typedef void * (*CuteQGraphicsSceneHoverEventCall1)(const void *, int *);
class CuteQGraphicsSceneHoverEvent : public QGraphicsSceneHoverEvent {
public:
  using QGraphicsSceneHoverEvent::QGraphicsSceneHoverEvent;
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
      CuteQGraphicsSceneHoverEventCall0 call = reinterpret_cast<CuteQGraphicsSceneHoverEventCall0>(taken[0]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }

  //  QEvent *QEvent::clone() const
  QEvent *clone() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQGraphicsSceneHoverEventCall1 call = reinterpret_cast<CuteQGraphicsSceneHoverEventCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QEvent *>(given);
    }
    return QEvent::clone();
  }
};

//  QGraphicsSceneHoverEvent::QGraphicsSceneHoverEvent(Type type)
extern "C" Q_DECL_EXPORT
QGraphicsSceneHoverEvent *ritual_ZN24QGraphicsSceneHoverEventC1EN6QEvent4TypeE(
    QEvent::Type type) {
  return new CuteQGraphicsSceneHoverEvent(type);
}

//  QGraphicsSceneHoverEvent::~QGraphicsSceneHoverEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGraphicsSceneHoverEventD1Ev(
    QGraphicsSceneHoverEvent *self) {
  delete self;
}

//  QPointF QGraphicsSceneHoverEvent::pos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK24QGraphicsSceneHoverEvent3posEv(
    const QGraphicsSceneHoverEvent *self) {
  return new QPointF(self->pos());
}

//  void QGraphicsSceneHoverEvent::setPos(const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGraphicsSceneHoverEvent6setPosERK7QPointF(
    QGraphicsSceneHoverEvent *self,
    const QPointF *pos) {
  self->setPos(*pos);
}

//  QPointF QGraphicsSceneHoverEvent::scenePos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK24QGraphicsSceneHoverEvent8scenePosEv(
    const QGraphicsSceneHoverEvent *self) {
  return new QPointF(self->scenePos());
}

//  void QGraphicsSceneHoverEvent::setScenePos(const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGraphicsSceneHoverEvent11setScenePosERK7QPointF(
    QGraphicsSceneHoverEvent *self,
    const QPointF *pos) {
  self->setScenePos(*pos);
}

//  QPoint QGraphicsSceneHoverEvent::screenPos() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK24QGraphicsSceneHoverEvent9screenPosEv(
    const QGraphicsSceneHoverEvent *self) {
  return new QPoint(self->screenPos());
}

//  void QGraphicsSceneHoverEvent::setScreenPos(const QPoint &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGraphicsSceneHoverEvent12setScreenPosERK6QPoint(
    QGraphicsSceneHoverEvent *self,
    const QPoint *pos) {
  self->setScreenPos(*pos);
}

//  QPointF QGraphicsSceneHoverEvent::lastPos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK24QGraphicsSceneHoverEvent7lastPosEv(
    const QGraphicsSceneHoverEvent *self) {
  return new QPointF(self->lastPos());
}

//  void QGraphicsSceneHoverEvent::setLastPos(const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGraphicsSceneHoverEvent10setLastPosERK7QPointF(
    QGraphicsSceneHoverEvent *self,
    const QPointF *pos) {
  self->setLastPos(*pos);
}

//  QPointF QGraphicsSceneHoverEvent::lastScenePos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK24QGraphicsSceneHoverEvent12lastScenePosEv(
    const QGraphicsSceneHoverEvent *self) {
  return new QPointF(self->lastScenePos());
}

//  void QGraphicsSceneHoverEvent::setLastScenePos(const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGraphicsSceneHoverEvent15setLastScenePosERK7QPointF(
    QGraphicsSceneHoverEvent *self,
    const QPointF *pos) {
  self->setLastScenePos(*pos);
}

//  QPoint QGraphicsSceneHoverEvent::lastScreenPos() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK24QGraphicsSceneHoverEvent13lastScreenPosEv(
    const QGraphicsSceneHoverEvent *self) {
  return new QPoint(self->lastScreenPos());
}

//  void QGraphicsSceneHoverEvent::setLastScreenPos(const QPoint &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGraphicsSceneHoverEvent16setLastScreenPosERK6QPoint(
    QGraphicsSceneHoverEvent *self,
    const QPoint *pos) {
  self->setLastScreenPos(*pos);
}

//  Qt::KeyboardModifiers QGraphicsSceneHoverEvent::modifiers() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QGraphicsSceneHoverEvent9modifiersEv(
    const QGraphicsSceneHoverEvent *self) {
  return static_cast<int>(self->modifiers().toInt());
}

//  void QGraphicsSceneHoverEvent::setModifiers(Qt::KeyboardModifiers
//      modifiers)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGraphicsSceneHoverEvent12setModifiersE6QFlagsIN2Qt16KeyboardModifierEE(
    QGraphicsSceneHoverEvent *self,
    int modifiers) {
  self->setModifiers(QFlags<Qt::KeyboardModifier>::fromInt(modifiers));
}

//  a Python function taken by a CuteQGraphicsSceneHoverEvent, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphicsSceneHoverEvent(
    QGraphicsSceneHoverEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphicsSceneHoverEvent *>(self)->take(key, call);
}

#endif  // QT_CONFIG(graphicsview)
