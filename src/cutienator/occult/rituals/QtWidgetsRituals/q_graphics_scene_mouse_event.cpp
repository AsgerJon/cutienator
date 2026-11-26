//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicssceneevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#if QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
#include <QtWidgets/qgraphicssceneevent.h>
#include <QtCore/qpoint.h>
#include <cstring>

//  A QGraphicsSceneMouseEvent that Python can take functions over in. Every QGraphicsSceneMouseEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQGraphicsSceneMouseEventCall0)(const void *, bool, int *);
typedef void * (*CuteQGraphicsSceneMouseEventCall1)(const void *, int *);
class CuteQGraphicsSceneMouseEvent : public QGraphicsSceneMouseEvent {
public:
  using QGraphicsSceneMouseEvent::QGraphicsSceneMouseEvent;
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
      CuteQGraphicsSceneMouseEventCall0 call = reinterpret_cast<CuteQGraphicsSceneMouseEventCall0>(taken[0]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }

  //  QEvent *QEvent::clone() const
  QEvent *clone() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQGraphicsSceneMouseEventCall1 call = reinterpret_cast<CuteQGraphicsSceneMouseEventCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QEvent *>(given);
    }
    return QEvent::clone();
  }
};

//  QGraphicsSceneMouseEvent::QGraphicsSceneMouseEvent(Type type)
extern "C" Q_DECL_EXPORT
QGraphicsSceneMouseEvent *ritual_ZN24QGraphicsSceneMouseEventC1EN6QEvent4TypeE(
    QEvent::Type type) {
  return new CuteQGraphicsSceneMouseEvent(type);
}

//  QGraphicsSceneMouseEvent::~QGraphicsSceneMouseEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGraphicsSceneMouseEventD1Ev(
    QGraphicsSceneMouseEvent *self) {
  delete self;
}

//  QPointF QGraphicsSceneMouseEvent::pos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK24QGraphicsSceneMouseEvent3posEv(
    const QGraphicsSceneMouseEvent *self) {
  return new QPointF(self->pos());
}

//  void QGraphicsSceneMouseEvent::setPos(const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGraphicsSceneMouseEvent6setPosERK7QPointF(
    QGraphicsSceneMouseEvent *self,
    const QPointF *pos) {
  self->setPos(*pos);
}

//  QPointF QGraphicsSceneMouseEvent::scenePos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK24QGraphicsSceneMouseEvent8scenePosEv(
    const QGraphicsSceneMouseEvent *self) {
  return new QPointF(self->scenePos());
}

//  void QGraphicsSceneMouseEvent::setScenePos(const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGraphicsSceneMouseEvent11setScenePosERK7QPointF(
    QGraphicsSceneMouseEvent *self,
    const QPointF *pos) {
  self->setScenePos(*pos);
}

//  QPoint QGraphicsSceneMouseEvent::screenPos() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK24QGraphicsSceneMouseEvent9screenPosEv(
    const QGraphicsSceneMouseEvent *self) {
  return new QPoint(self->screenPos());
}

//  void QGraphicsSceneMouseEvent::setScreenPos(const QPoint &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGraphicsSceneMouseEvent12setScreenPosERK6QPoint(
    QGraphicsSceneMouseEvent *self,
    const QPoint *pos) {
  self->setScreenPos(*pos);
}

//  QPointF QGraphicsSceneMouseEvent::buttonDownPos(Qt::MouseButton button)
//      const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK24QGraphicsSceneMouseEvent13buttonDownPosEN2Qt11MouseButtonE(
    const QGraphicsSceneMouseEvent *self,
    Qt::MouseButton button) {
  return new QPointF(self->buttonDownPos(button));
}

//  void QGraphicsSceneMouseEvent::setButtonDownPos(Qt::MouseButton button,
//      const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGraphicsSceneMouseEvent16setButtonDownPosEN2Qt11MouseButtonERK7QPointF(
    QGraphicsSceneMouseEvent *self,
    Qt::MouseButton button,
    const QPointF *pos) {
  self->setButtonDownPos(button, *pos);
}

//  QPointF QGraphicsSceneMouseEvent::buttonDownScenePos(Qt::MouseButton
//      button) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK24QGraphicsSceneMouseEvent18buttonDownScenePosEN2Qt11MouseButtonE(
    const QGraphicsSceneMouseEvent *self,
    Qt::MouseButton button) {
  return new QPointF(self->buttonDownScenePos(button));
}

//  void QGraphicsSceneMouseEvent::setButtonDownScenePos(Qt::MouseButton
//      button, const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGraphicsSceneMouseEvent21setButtonDownScenePosEN2Qt11MouseButtonERK7QPointF(
    QGraphicsSceneMouseEvent *self,
    Qt::MouseButton button,
    const QPointF *pos) {
  self->setButtonDownScenePos(button, *pos);
}

//  QPoint QGraphicsSceneMouseEvent::buttonDownScreenPos(Qt::MouseButton
//      button) const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK24QGraphicsSceneMouseEvent19buttonDownScreenPosEN2Qt11MouseButtonE(
    const QGraphicsSceneMouseEvent *self,
    Qt::MouseButton button) {
  return new QPoint(self->buttonDownScreenPos(button));
}

//  void QGraphicsSceneMouseEvent::setButtonDownScreenPos(Qt::MouseButton
//      button, const QPoint &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGraphicsSceneMouseEvent22setButtonDownScreenPosEN2Qt11MouseButtonERK6QPoint(
    QGraphicsSceneMouseEvent *self,
    Qt::MouseButton button,
    const QPoint *pos) {
  self->setButtonDownScreenPos(button, *pos);
}

//  QPointF QGraphicsSceneMouseEvent::lastPos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK24QGraphicsSceneMouseEvent7lastPosEv(
    const QGraphicsSceneMouseEvent *self) {
  return new QPointF(self->lastPos());
}

//  void QGraphicsSceneMouseEvent::setLastPos(const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGraphicsSceneMouseEvent10setLastPosERK7QPointF(
    QGraphicsSceneMouseEvent *self,
    const QPointF *pos) {
  self->setLastPos(*pos);
}

//  QPointF QGraphicsSceneMouseEvent::lastScenePos() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK24QGraphicsSceneMouseEvent12lastScenePosEv(
    const QGraphicsSceneMouseEvent *self) {
  return new QPointF(self->lastScenePos());
}

//  void QGraphicsSceneMouseEvent::setLastScenePos(const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGraphicsSceneMouseEvent15setLastScenePosERK7QPointF(
    QGraphicsSceneMouseEvent *self,
    const QPointF *pos) {
  self->setLastScenePos(*pos);
}

//  QPoint QGraphicsSceneMouseEvent::lastScreenPos() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK24QGraphicsSceneMouseEvent13lastScreenPosEv(
    const QGraphicsSceneMouseEvent *self) {
  return new QPoint(self->lastScreenPos());
}

//  void QGraphicsSceneMouseEvent::setLastScreenPos(const QPoint &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGraphicsSceneMouseEvent16setLastScreenPosERK6QPoint(
    QGraphicsSceneMouseEvent *self,
    const QPoint *pos) {
  self->setLastScreenPos(*pos);
}

//  Qt::MouseButtons QGraphicsSceneMouseEvent::buttons() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QGraphicsSceneMouseEvent7buttonsEv(
    const QGraphicsSceneMouseEvent *self) {
  return static_cast<int>(self->buttons().toInt());
}

//  void QGraphicsSceneMouseEvent::setButtons(Qt::MouseButtons buttons)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGraphicsSceneMouseEvent10setButtonsE6QFlagsIN2Qt11MouseButtonEE(
    QGraphicsSceneMouseEvent *self,
    int buttons) {
  self->setButtons(QFlags<Qt::MouseButton>::fromInt(buttons));
}

//  Qt::MouseButton QGraphicsSceneMouseEvent::button() const
extern "C" Q_DECL_EXPORT
Qt::MouseButton ritual_ZNK24QGraphicsSceneMouseEvent6buttonEv(
    const QGraphicsSceneMouseEvent *self) {
  return self->button();
}

//  void QGraphicsSceneMouseEvent::setButton(Qt::MouseButton button)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGraphicsSceneMouseEvent9setButtonEN2Qt11MouseButtonE(
    QGraphicsSceneMouseEvent *self,
    Qt::MouseButton button) {
  self->setButton(button);
}

//  Qt::KeyboardModifiers QGraphicsSceneMouseEvent::modifiers() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QGraphicsSceneMouseEvent9modifiersEv(
    const QGraphicsSceneMouseEvent *self) {
  return static_cast<int>(self->modifiers().toInt());
}

//  void QGraphicsSceneMouseEvent::setModifiers(Qt::KeyboardModifiers
//      modifiers)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGraphicsSceneMouseEvent12setModifiersE6QFlagsIN2Qt16KeyboardModifierEE(
    QGraphicsSceneMouseEvent *self,
    int modifiers) {
  self->setModifiers(QFlags<Qt::KeyboardModifier>::fromInt(modifiers));
}

//  Qt::MouseEventSource QGraphicsSceneMouseEvent::source() const
extern "C" Q_DECL_EXPORT
Qt::MouseEventSource ritual_ZNK24QGraphicsSceneMouseEvent6sourceEv(
    const QGraphicsSceneMouseEvent *self) {
  return self->source();
}

//  void QGraphicsSceneMouseEvent::setSource(Qt::MouseEventSource source)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGraphicsSceneMouseEvent9setSourceEN2Qt16MouseEventSourceE(
    QGraphicsSceneMouseEvent *self,
    Qt::MouseEventSource source) {
  self->setSource(source);
}

//  Qt::MouseEventFlags QGraphicsSceneMouseEvent::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QGraphicsSceneMouseEvent5flagsEv(
    const QGraphicsSceneMouseEvent *self) {
  return static_cast<int>(self->flags().toInt());
}

//  void QGraphicsSceneMouseEvent::setFlags(Qt::MouseEventFlags a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGraphicsSceneMouseEvent8setFlagsE6QFlagsIN2Qt14MouseEventFlagEE(
    QGraphicsSceneMouseEvent *self,
    int a0) {
  self->setFlags(QFlags<Qt::MouseEventFlag>::fromInt(a0));
}

//  QGraphicsSceneMouseEventPrivate *QGraphicsSceneMouseEvent::d_func()
extern "C" Q_DECL_EXPORT
QGraphicsSceneMouseEventPrivate *ritual_ZN24QGraphicsSceneMouseEvent6d_funcEv(
    QGraphicsSceneMouseEvent *self) {
  return self->d_func();
}

//  const QGraphicsSceneMouseEventPrivate *QGraphicsSceneMouseEvent::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QGraphicsSceneMouseEventPrivate *ritual_ZNK24QGraphicsSceneMouseEvent6d_funcEv(
    const QGraphicsSceneMouseEvent *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQGraphicsSceneMouseEvent, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphicsSceneMouseEvent(
    QGraphicsSceneMouseEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphicsSceneMouseEvent *>(self)->take(key, call);
}

#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicsview)
