//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicssceneevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
#include <QtWidgets/qgraphicssceneevent.h>
#include <QtCore/qpoint.h>
#include <cstring>

//  A QGraphicsSceneWheelEvent that Python can take functions over in. Every QGraphicsSceneWheelEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQGraphicsSceneWheelEventCall0)(const void *, bool, int *);
typedef void * (*CuteQGraphicsSceneWheelEventCall1)(const void *, int *);
class CuteQGraphicsSceneWheelEvent : public QGraphicsSceneWheelEvent {
public:
  using QGraphicsSceneWheelEvent::QGraphicsSceneWheelEvent;
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
      CuteQGraphicsSceneWheelEventCall0 call = reinterpret_cast<CuteQGraphicsSceneWheelEventCall0>(taken[0]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }

  //  QEvent *QEvent::clone() const
  QEvent *clone() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQGraphicsSceneWheelEventCall1 call = reinterpret_cast<CuteQGraphicsSceneWheelEventCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QEvent *>(given);
    }
    return QEvent::clone();
  }
};

//  QGraphicsSceneWheelEvent::QGraphicsSceneWheelEvent(Type type)
extern "C" Q_DECL_EXPORT
QGraphicsSceneWheelEvent *ritual_ZN24QGraphicsSceneWheelEventC1EN6QEvent4TypeE(
    QEvent::Type type) {
  return new CuteQGraphicsSceneWheelEvent(type);
}

//  QGraphicsSceneWheelEvent::~QGraphicsSceneWheelEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGraphicsSceneWheelEventD1Ev(
    QGraphicsSceneWheelEvent *self) {
  delete self;
}

//  QPointF QGraphicsSceneWheelEvent::pos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK24QGraphicsSceneWheelEvent3posEv(
    const QGraphicsSceneWheelEvent *self) {
  return new QPointF(self->pos());
}

//  void QGraphicsSceneWheelEvent::setPos(const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGraphicsSceneWheelEvent6setPosERK7QPointF(
    QGraphicsSceneWheelEvent *self,
    const QPointF *pos) {
  self->setPos(*pos);
}

//  QPointF QGraphicsSceneWheelEvent::scenePos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK24QGraphicsSceneWheelEvent8scenePosEv(
    const QGraphicsSceneWheelEvent *self) {
  return new QPointF(self->scenePos());
}

//  void QGraphicsSceneWheelEvent::setScenePos(const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGraphicsSceneWheelEvent11setScenePosERK7QPointF(
    QGraphicsSceneWheelEvent *self,
    const QPointF *pos) {
  self->setScenePos(*pos);
}

//  QPoint QGraphicsSceneWheelEvent::screenPos() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK24QGraphicsSceneWheelEvent9screenPosEv(
    const QGraphicsSceneWheelEvent *self) {
  return new QPoint(self->screenPos());
}

//  void QGraphicsSceneWheelEvent::setScreenPos(const QPoint &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGraphicsSceneWheelEvent12setScreenPosERK6QPoint(
    QGraphicsSceneWheelEvent *self,
    const QPoint *pos) {
  self->setScreenPos(*pos);
}

//  Qt::MouseButtons QGraphicsSceneWheelEvent::buttons() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QGraphicsSceneWheelEvent7buttonsEv(
    const QGraphicsSceneWheelEvent *self) {
  return static_cast<int>(self->buttons().toInt());
}

//  void QGraphicsSceneWheelEvent::setButtons(Qt::MouseButtons buttons)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGraphicsSceneWheelEvent10setButtonsE6QFlagsIN2Qt11MouseButtonEE(
    QGraphicsSceneWheelEvent *self,
    int buttons) {
  self->setButtons(QFlags<Qt::MouseButton>::fromInt(buttons));
}

//  Qt::KeyboardModifiers QGraphicsSceneWheelEvent::modifiers() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QGraphicsSceneWheelEvent9modifiersEv(
    const QGraphicsSceneWheelEvent *self) {
  return static_cast<int>(self->modifiers().toInt());
}

//  void QGraphicsSceneWheelEvent::setModifiers(Qt::KeyboardModifiers
//      modifiers)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGraphicsSceneWheelEvent12setModifiersE6QFlagsIN2Qt16KeyboardModifierEE(
    QGraphicsSceneWheelEvent *self,
    int modifiers) {
  self->setModifiers(QFlags<Qt::KeyboardModifier>::fromInt(modifiers));
}

//  int QGraphicsSceneWheelEvent::delta() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QGraphicsSceneWheelEvent5deltaEv(
    const QGraphicsSceneWheelEvent *self) {
  return self->delta();
}

//  void QGraphicsSceneWheelEvent::setDelta(int delta)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGraphicsSceneWheelEvent8setDeltaEi(
    QGraphicsSceneWheelEvent *self,
    int delta) {
  self->setDelta(delta);
}

//  Qt::Orientation QGraphicsSceneWheelEvent::orientation() const
extern "C" Q_DECL_EXPORT
Qt::Orientation ritual_ZNK24QGraphicsSceneWheelEvent11orientationEv(
    const QGraphicsSceneWheelEvent *self) {
  return self->orientation();
}

//  void QGraphicsSceneWheelEvent::setOrientation(Qt::Orientation
//      orientation)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGraphicsSceneWheelEvent14setOrientationEN2Qt11OrientationE(
    QGraphicsSceneWheelEvent *self,
    Qt::Orientation orientation) {
  self->setOrientation(orientation);
}

//  Qt::ScrollPhase QGraphicsSceneWheelEvent::phase() const
extern "C" Q_DECL_EXPORT
Qt::ScrollPhase ritual_ZNK24QGraphicsSceneWheelEvent5phaseEv(
    const QGraphicsSceneWheelEvent *self) {
  return self->phase();
}

//  void QGraphicsSceneWheelEvent::setPhase(Qt::ScrollPhase scrollPhase)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGraphicsSceneWheelEvent8setPhaseEN2Qt11ScrollPhaseE(
    QGraphicsSceneWheelEvent *self,
    Qt::ScrollPhase scrollPhase) {
  self->setPhase(scrollPhase);
}

//  QPoint QGraphicsSceneWheelEvent::pixelDelta() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK24QGraphicsSceneWheelEvent10pixelDeltaEv(
    const QGraphicsSceneWheelEvent *self) {
  return new QPoint(self->pixelDelta());
}

//  void QGraphicsSceneWheelEvent::setPixelDelta(QPoint delta)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGraphicsSceneWheelEvent13setPixelDeltaE6QPoint(
    QGraphicsSceneWheelEvent *self,
    const QPoint *delta) {
  self->setPixelDelta(*delta);
}

//  bool QGraphicsSceneWheelEvent::isInverted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QGraphicsSceneWheelEvent10isInvertedEv(
    const QGraphicsSceneWheelEvent *self) {
  return self->isInverted();
}

//  void QGraphicsSceneWheelEvent::setInverted(bool inverted)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGraphicsSceneWheelEvent11setInvertedEb(
    QGraphicsSceneWheelEvent *self,
    bool inverted) {
  self->setInverted(inverted);
}

//  QGraphicsSceneWheelEventPrivate *QGraphicsSceneWheelEvent::d_func()
extern "C" Q_DECL_EXPORT
QGraphicsSceneWheelEventPrivate *ritual_ZN24QGraphicsSceneWheelEvent6d_funcEv(
    QGraphicsSceneWheelEvent *self) {
  return self->d_func();
}

//  const QGraphicsSceneWheelEventPrivate *QGraphicsSceneWheelEvent::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QGraphicsSceneWheelEventPrivate *ritual_ZNK24QGraphicsSceneWheelEvent6d_funcEv(
    const QGraphicsSceneWheelEvent *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQGraphicsSceneWheelEvent, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphicsSceneWheelEvent(
    QGraphicsSceneWheelEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphicsSceneWheelEvent *>(self)->take(key, call);
}

#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicsview)
