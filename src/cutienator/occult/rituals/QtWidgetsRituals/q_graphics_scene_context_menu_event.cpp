//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicssceneevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
#include <QtWidgets/qgraphicssceneevent.h>
#include <QtCore/qpoint.h>
#include <cstring>

//  A QGraphicsSceneContextMenuEvent that Python can take functions over in. Every QGraphicsSceneContextMenuEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQGraphicsSceneContextMenuEventCall0)(const void *, bool, int *);
typedef void * (*CuteQGraphicsSceneContextMenuEventCall1)(const void *, int *);
class CuteQGraphicsSceneContextMenuEvent : public QGraphicsSceneContextMenuEvent {
public:
  using QGraphicsSceneContextMenuEvent::QGraphicsSceneContextMenuEvent;
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
      CuteQGraphicsSceneContextMenuEventCall0 call = reinterpret_cast<CuteQGraphicsSceneContextMenuEventCall0>(taken[0]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }

  //  QEvent *QEvent::clone() const
  QEvent *clone() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQGraphicsSceneContextMenuEventCall1 call = reinterpret_cast<CuteQGraphicsSceneContextMenuEventCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QEvent *>(given);
    }
    return QEvent::clone();
  }
};

//  QGraphicsSceneContextMenuEvent::QGraphicsSceneContextMenuEvent(Type type)
extern "C" Q_DECL_EXPORT
QGraphicsSceneContextMenuEvent *ritual_ZN30QGraphicsSceneContextMenuEventC1EN6QEvent4TypeE(
    QEvent::Type type) {
  return new CuteQGraphicsSceneContextMenuEvent(type);
}

//  QGraphicsSceneContextMenuEvent::~QGraphicsSceneContextMenuEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QGraphicsSceneContextMenuEventD1Ev(
    QGraphicsSceneContextMenuEvent *self) {
  delete self;
}

//  QPointF QGraphicsSceneContextMenuEvent::pos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK30QGraphicsSceneContextMenuEvent3posEv(
    const QGraphicsSceneContextMenuEvent *self) {
  return new QPointF(self->pos());
}

//  void QGraphicsSceneContextMenuEvent::setPos(const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QGraphicsSceneContextMenuEvent6setPosERK7QPointF(
    QGraphicsSceneContextMenuEvent *self,
    const QPointF *pos) {
  self->setPos(*pos);
}

//  QPointF QGraphicsSceneContextMenuEvent::scenePos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK30QGraphicsSceneContextMenuEvent8scenePosEv(
    const QGraphicsSceneContextMenuEvent *self) {
  return new QPointF(self->scenePos());
}

//  void QGraphicsSceneContextMenuEvent::setScenePos(const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QGraphicsSceneContextMenuEvent11setScenePosERK7QPointF(
    QGraphicsSceneContextMenuEvent *self,
    const QPointF *pos) {
  self->setScenePos(*pos);
}

//  QPoint QGraphicsSceneContextMenuEvent::screenPos() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK30QGraphicsSceneContextMenuEvent9screenPosEv(
    const QGraphicsSceneContextMenuEvent *self) {
  return new QPoint(self->screenPos());
}

//  void QGraphicsSceneContextMenuEvent::setScreenPos(const QPoint &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QGraphicsSceneContextMenuEvent12setScreenPosERK6QPoint(
    QGraphicsSceneContextMenuEvent *self,
    const QPoint *pos) {
  self->setScreenPos(*pos);
}

//  Qt::KeyboardModifiers QGraphicsSceneContextMenuEvent::modifiers() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK30QGraphicsSceneContextMenuEvent9modifiersEv(
    const QGraphicsSceneContextMenuEvent *self) {
  return static_cast<int>(self->modifiers().toInt());
}

//  void QGraphicsSceneContextMenuEvent::setModifiers(Qt::KeyboardModifiers
//      modifiers)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QGraphicsSceneContextMenuEvent12setModifiersE6QFlagsIN2Qt16KeyboardModifierEE(
    QGraphicsSceneContextMenuEvent *self,
    int modifiers) {
  self->setModifiers(QFlags<Qt::KeyboardModifier>::fromInt(modifiers));
}

//  Reason QGraphicsSceneContextMenuEvent::reason() const
extern "C" Q_DECL_EXPORT
QGraphicsSceneContextMenuEvent::Reason ritual_ZNK30QGraphicsSceneContextMenuEvent6reasonEv(
    const QGraphicsSceneContextMenuEvent *self) {
  return self->reason();
}

//  void QGraphicsSceneContextMenuEvent::setReason(Reason reason)
extern "C" Q_DECL_EXPORT
void ritual_ZN30QGraphicsSceneContextMenuEvent9setReasonENS_6ReasonE(
    QGraphicsSceneContextMenuEvent *self,
    QGraphicsSceneContextMenuEvent::Reason reason) {
  self->setReason(reason);
}

//  QGraphicsSceneContextMenuEventPrivate
//      *QGraphicsSceneContextMenuEvent::d_func()
extern "C" Q_DECL_EXPORT
QGraphicsSceneContextMenuEventPrivate *ritual_ZN30QGraphicsSceneContextMenuEvent6d_funcEv(
    QGraphicsSceneContextMenuEvent *self) {
  return self->d_func();
}

//  const QGraphicsSceneContextMenuEventPrivate
//      *QGraphicsSceneContextMenuEvent::d_func() const
extern "C" Q_DECL_EXPORT
const QGraphicsSceneContextMenuEventPrivate *ritual_ZNK30QGraphicsSceneContextMenuEvent6d_funcEv(
    const QGraphicsSceneContextMenuEvent *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQGraphicsSceneContextMenuEvent, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphicsSceneContextMenuEvent(
    QGraphicsSceneContextMenuEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphicsSceneContextMenuEvent *>(self)->take(key, call);
}

#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicsview)
