//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qpickevent.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qpickevent.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DRender::QPickEvent that Python can take functions over in. Every Qt3DRender::QPickEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QPickEventCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QPickEventCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QPickEventCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QPickEventCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QPickEventCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QPickEventCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QPickEventCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QPickEvent : public Qt3DRender::QPickEvent {
public:
  using Qt3DRender::QPickEvent::QPickEvent;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_QPickEventCall0 call = reinterpret_cast<CuteQt3DRender_QPickEventCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_QPickEventCall1 call = reinterpret_cast<CuteQt3DRender_QPickEventCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DRender_QPickEventCall2 call = reinterpret_cast<CuteQt3DRender_QPickEventCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DRender_QPickEventCall3 call = reinterpret_cast<CuteQt3DRender_QPickEventCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQt3DRender_QPickEventCall4 call = reinterpret_cast<CuteQt3DRender_QPickEventCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQt3DRender_QPickEventCall5 call = reinterpret_cast<CuteQt3DRender_QPickEventCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQt3DRender_QPickEventCall6 call = reinterpret_cast<CuteQt3DRender_QPickEventCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QPickEvent::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender10QPickEvent10metaObjectEv(
    const Qt3DRender::QPickEvent *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QPickEvent::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender10QPickEvent11qt_metacastEPKc(
    Qt3DRender::QPickEvent *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QPickEvent::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender10QPickEvent11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QPickEvent *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QPickEvent::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender10QPickEvent2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QPickEvent::tr(s, c, n));
}

//  Qt3DRender::QPickEvent::QPickEvent()
extern "C" Q_DECL_EXPORT
Qt3DRender::QPickEvent *ritual_ZN10Qt3DRender10QPickEventC1Ev() {
  return new CuteQt3DRender_QPickEvent();
}

//  Qt3DRender::QPickEvent::QPickEvent(const QPointF &position, const
//      QVector3D &worldIntersection, const QVector3D &localIntersection,
//      float distance)
extern "C" Q_DECL_EXPORT
Qt3DRender::QPickEvent *ritual_ZN10Qt3DRender10QPickEventC1ERK7QPointFRK9QVector3DS6_f(
    const QPointF *position,
    const QVector3D *worldIntersection,
    const QVector3D *localIntersection,
    float distance) {
  return new CuteQt3DRender_QPickEvent(
      *position,
      *worldIntersection,
      *localIntersection,
      distance);
}

//  Qt3DRender::QPickEvent::QPickEvent(const QPointF &position, const
//      QVector3D &worldIntersection, const QVector3D &localIntersection,
//      float distance, Buttons button, int buttons, int modifiers)
extern "C" Q_DECL_EXPORT
Qt3DRender::QPickEvent *ritual_ZN10Qt3DRender10QPickEventC1ERK7QPointFRK9QVector3DS6_fNS0_7ButtonsEii(
    const QPointF *position,
    const QVector3D *worldIntersection,
    const QVector3D *localIntersection,
    float distance,
    Qt3DRender::QPickEvent::Buttons button,
    int buttons,
    int modifiers) {
  return new CuteQt3DRender_QPickEvent(
      *position,
      *worldIntersection,
      *localIntersection,
      distance,
      button,
      buttons,
      modifiers);
}

//  Qt3DRender::QPickEvent::~QPickEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QPickEventD1Ev(Qt3DRender::QPickEvent *self) {
  delete self;
}

//  bool Qt3DRender::QPickEvent::isAccepted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender10QPickEvent10isAcceptedEv(
    const Qt3DRender::QPickEvent *self) {
  return self->isAccepted();
}

//  void Qt3DRender::QPickEvent::setAccepted(bool accepted)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QPickEvent11setAcceptedEb(
    Qt3DRender::QPickEvent *self,
    bool accepted) {
  self->setAccepted(accepted);
}

//  QPointF Qt3DRender::QPickEvent::position() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK10Qt3DRender10QPickEvent8positionEv(
    const Qt3DRender::QPickEvent *self) {
  return new QPointF(self->position());
}

//  float Qt3DRender::QPickEvent::distance() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender10QPickEvent8distanceEv(
    const Qt3DRender::QPickEvent *self) {
  return self->distance();
}

//  QVector3D Qt3DRender::QPickEvent::worldIntersection() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK10Qt3DRender10QPickEvent17worldIntersectionEv(
    const Qt3DRender::QPickEvent *self) {
  return new QVector3D(self->worldIntersection());
}

//  QVector3D Qt3DRender::QPickEvent::localIntersection() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK10Qt3DRender10QPickEvent17localIntersectionEv(
    const Qt3DRender::QPickEvent *self) {
  return new QVector3D(self->localIntersection());
}

//  Buttons Qt3DRender::QPickEvent::button() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QPickEvent::Buttons ritual_ZNK10Qt3DRender10QPickEvent6buttonEv(
    const Qt3DRender::QPickEvent *self) {
  return self->button();
}

//  int Qt3DRender::QPickEvent::buttons() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender10QPickEvent7buttonsEv(
    const Qt3DRender::QPickEvent *self) {
  return self->buttons();
}

//  int Qt3DRender::QPickEvent::modifiers() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender10QPickEvent9modifiersEv(
    const Qt3DRender::QPickEvent *self) {
  return self->modifiers();
}

//  QViewport *Qt3DRender::QPickEvent::viewport() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QViewport *ritual_ZNK10Qt3DRender10QPickEvent8viewportEv(
    const Qt3DRender::QPickEvent *self) {
  return self->viewport();
}

//  Qt3DCore::QEntity *Qt3DRender::QPickEvent::entity() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QEntity *ritual_ZNK10Qt3DRender10QPickEvent6entityEv(
    const Qt3DRender::QPickEvent *self) {
  return self->entity();
}

//  void Qt3DRender::QPickEvent::acceptedChanged(bool accepted)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QPickEvent15acceptedChangedEb(
    Qt3DRender::QPickEvent *self,
    bool accepted) {
  self->acceptedChanged(accepted);
}

//  Qt3DRender::QPickEvent::QPickEvent(QObjectPrivate &dd, QObject *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QPickEvent *ritual_ZN10Qt3DRender10QPickEventC1ER14QObjectPrivateP7QObject(
    QObjectPrivate *dd,
    QObject *parent) {
  return new CuteQt3DRender_QPickEvent(*dd, parent);
}

//  QPickEventPrivate *Qt3DRender::QPickEvent::d_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QPickEventPrivate *ritual_ZN10Qt3DRender10QPickEvent6d_funcEv(
    Qt3DRender::QPickEvent *self) {
  return self->d_func();
}

//  const QPickEventPrivate *Qt3DRender::QPickEvent::d_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QPickEventPrivate *ritual_ZNK10Qt3DRender10QPickEvent6d_funcEv(
    const Qt3DRender::QPickEvent *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DRender_QPickEvent, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QPickEvent(
    Qt3DRender::QPickEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QPickEvent *>(self)->take(key, call);
}
