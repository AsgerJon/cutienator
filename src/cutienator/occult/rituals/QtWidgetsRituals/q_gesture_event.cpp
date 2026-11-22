//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgesture.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgesture.h>
#include <QtCore/qpoint.h>
#include <cstring>

//  A QGestureEvent that Python can take functions over in. Every QGestureEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQGestureEventCall0)(const void *, bool, int *);
typedef void * (*CuteQGestureEventCall1)(const void *, int *);
class CuteQGestureEvent : public QGestureEvent {
public:
  using QGestureEvent::QGestureEvent;
  CuteQGestureEvent(const QGestureEvent &other) : QGestureEvent(other) {}
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
      CuteQGestureEventCall0 call = reinterpret_cast<CuteQGestureEventCall0>(taken[0]);
      call(this, accepted, &handled);
      if (handled) return;
    }
    QEvent::setAccepted(accepted);
  }

  //  QEvent *QEvent::clone() const
  QEvent *clone() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQGestureEventCall1 call = reinterpret_cast<CuteQGestureEventCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QEvent *>(given);
    }
    return QEvent::clone();
  }
};

//  QGestureEvent::~QGestureEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGestureEventD1Ev(QGestureEvent *self) {
  delete self;
}

//  QGesture *QGestureEvent::gesture(Qt::GestureType type) const
extern "C" Q_DECL_EXPORT
QGesture *ritual_ZNK13QGestureEvent7gestureEN2Qt11GestureTypeE(
    const QGestureEvent *self,
    Qt::GestureType type) {
  return self->gesture(type);
}

//  void QGestureEvent::setAccepted(QGesture *a0, bool a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGestureEvent11setAcceptedEP8QGestureb(
    QGestureEvent *self,
    QGesture *a0,
    bool a1) {
  self->setAccepted(a0, a1);
}

//  void QGestureEvent::accept(QGesture *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGestureEvent6acceptEP8QGesture(
    QGestureEvent *self,
    QGesture *a0) {
  self->accept(a0);
}

//  void QGestureEvent::ignore(QGesture *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGestureEvent6ignoreEP8QGesture(
    QGestureEvent *self,
    QGesture *a0) {
  self->ignore(a0);
}

//  bool QGestureEvent::isAccepted(QGesture *a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QGestureEvent10isAcceptedEP8QGesture(
    const QGestureEvent *self,
    QGesture *a0) {
  return self->isAccepted(a0);
}

//  void QGestureEvent::setAccepted(Qt::GestureType a0, bool a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGestureEvent11setAcceptedEN2Qt11GestureTypeEb(
    QGestureEvent *self,
    Qt::GestureType a0,
    bool a1) {
  self->setAccepted(a0, a1);
}

//  void QGestureEvent::accept(Qt::GestureType a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGestureEvent6acceptEN2Qt11GestureTypeE(
    QGestureEvent *self,
    Qt::GestureType a0) {
  self->accept(a0);
}

//  void QGestureEvent::ignore(Qt::GestureType a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGestureEvent6ignoreEN2Qt11GestureTypeE(
    QGestureEvent *self,
    Qt::GestureType a0) {
  self->ignore(a0);
}

//  bool QGestureEvent::isAccepted(Qt::GestureType a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QGestureEvent10isAcceptedEN2Qt11GestureTypeE(
    const QGestureEvent *self,
    Qt::GestureType a0) {
  return self->isAccepted(a0);
}

//  void QGestureEvent::setWidget(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGestureEvent9setWidgetEP7QWidget(
    QGestureEvent *self,
    QWidget *widget) {
  self->setWidget(widget);
}

//  QWidget *QGestureEvent::widget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK13QGestureEvent6widgetEv(const QGestureEvent *self) {
  return self->widget();
}

//  QPointF QGestureEvent::mapToGraphicsScene(const QPointF &gesturePoint)
//      const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK13QGestureEvent18mapToGraphicsSceneERK7QPointF(
    const QGestureEvent *self,
    const QPointF *gesturePoint) {
  return new QPointF(self->mapToGraphicsScene(*gesturePoint));
}

//  a Python function taken by a CuteQGestureEvent, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGestureEvent(
    QGestureEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGestureEvent *>(self)->take(key, call);
}
