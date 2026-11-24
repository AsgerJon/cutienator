//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DInput/qmouseevent.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <Qt3DInput/qt3dinput_global.h>
#if QT_CONFIG(wheelevent)
#include <Qt3DInput/qmouseevent.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DInput::QWheelEvent that Python can take functions over in. Every Qt3DInput::QWheelEvent
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DInput_QWheelEventCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DInput_QWheelEventCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QWheelEventCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QWheelEventCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QWheelEventCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QWheelEventCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DInput_QWheelEventCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DInput_QWheelEvent : public Qt3DInput::QWheelEvent {
public:
  using Qt3DInput::QWheelEvent::QWheelEvent;
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
      CuteQt3DInput_QWheelEventCall0 call = reinterpret_cast<CuteQt3DInput_QWheelEventCall0>(taken[0]);
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
      CuteQt3DInput_QWheelEventCall1 call = reinterpret_cast<CuteQt3DInput_QWheelEventCall1>(taken[1]);
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
      CuteQt3DInput_QWheelEventCall2 call = reinterpret_cast<CuteQt3DInput_QWheelEventCall2>(taken[2]);
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
      CuteQt3DInput_QWheelEventCall3 call = reinterpret_cast<CuteQt3DInput_QWheelEventCall3>(taken[3]);
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
      CuteQt3DInput_QWheelEventCall4 call = reinterpret_cast<CuteQt3DInput_QWheelEventCall4>(taken[4]);
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
      CuteQt3DInput_QWheelEventCall5 call = reinterpret_cast<CuteQt3DInput_QWheelEventCall5>(taken[5]);
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
      CuteQt3DInput_QWheelEventCall6 call = reinterpret_cast<CuteQt3DInput_QWheelEventCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DInput::QWheelEvent::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9Qt3DInput11QWheelEvent10metaObjectEv(
    const Qt3DInput::QWheelEvent *self) {
  return self->metaObject();
}

//  QString Qt3DInput::QWheelEvent::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9Qt3DInput11QWheelEvent2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DInput::QWheelEvent::tr(s, c, n));
}

//  int Qt3DInput::QWheelEvent::x() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9Qt3DInput11QWheelEvent1xEv(
    const Qt3DInput::QWheelEvent *self) {
  return self->x();
}

//  int Qt3DInput::QWheelEvent::y() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK9Qt3DInput11QWheelEvent1yEv(
    const Qt3DInput::QWheelEvent *self) {
  return self->y();
}

//  QPoint Qt3DInput::QWheelEvent::angleDelta() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK9Qt3DInput11QWheelEvent10angleDeltaEv(
    const Qt3DInput::QWheelEvent *self) {
  return new QPoint(self->angleDelta());
}

//  bool Qt3DInput::QWheelEvent::isAccepted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9Qt3DInput11QWheelEvent10isAcceptedEv(
    const Qt3DInput::QWheelEvent *self) {
  return self->isAccepted();
}

//  void Qt3DInput::QWheelEvent::setAccepted(bool accepted)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Qt3DInput11QWheelEvent11setAcceptedEb(
    Qt3DInput::QWheelEvent *self,
    bool accepted) {
  self->setAccepted(accepted);
}

//  QEvent::Type Qt3DInput::QWheelEvent::type() const
extern "C" Q_DECL_EXPORT
QEvent::Type ritual_ZNK9Qt3DInput11QWheelEvent4typeEv(
    const Qt3DInput::QWheelEvent *self) {
  return self->type();
}

//  a Python function taken by a CuteQt3DInput_QWheelEvent, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DInput_QWheelEvent(
    Qt3DInput::QWheelEvent *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DInput_QWheelEvent *>(self)->take(key, call);
}

#endif  // QT_CONFIG(wheelevent)
