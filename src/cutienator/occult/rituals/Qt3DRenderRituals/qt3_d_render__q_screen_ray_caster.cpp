//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qscreenraycaster.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qscreenraycaster.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <Qt3DRender/Qt3DRender>
#include <QtCore/QPoint>

//  A Qt3DRender::QScreenRayCaster that Python can take functions over in. Every Qt3DRender::QScreenRayCaster
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QScreenRayCasterCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QScreenRayCasterCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QScreenRayCasterCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QScreenRayCasterCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QScreenRayCasterCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QScreenRayCasterCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QScreenRayCasterCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QScreenRayCaster : public Qt3DRender::QScreenRayCaster {
public:
  using Qt3DRender::QScreenRayCaster::QScreenRayCaster;
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
      CuteQt3DRender_QScreenRayCasterCall0 call = reinterpret_cast<CuteQt3DRender_QScreenRayCasterCall0>(taken[0]);
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
      CuteQt3DRender_QScreenRayCasterCall1 call = reinterpret_cast<CuteQt3DRender_QScreenRayCasterCall1>(taken[1]);
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
      CuteQt3DRender_QScreenRayCasterCall2 call = reinterpret_cast<CuteQt3DRender_QScreenRayCasterCall2>(taken[2]);
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
      CuteQt3DRender_QScreenRayCasterCall3 call = reinterpret_cast<CuteQt3DRender_QScreenRayCasterCall3>(taken[3]);
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
      CuteQt3DRender_QScreenRayCasterCall4 call = reinterpret_cast<CuteQt3DRender_QScreenRayCasterCall4>(taken[4]);
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
      CuteQt3DRender_QScreenRayCasterCall5 call = reinterpret_cast<CuteQt3DRender_QScreenRayCasterCall5>(taken[5]);
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
      CuteQt3DRender_QScreenRayCasterCall6 call = reinterpret_cast<CuteQt3DRender_QScreenRayCasterCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QScreenRayCaster::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender16QScreenRayCaster10metaObjectEv(
    const Qt3DRender::QScreenRayCaster *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QScreenRayCaster::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender16QScreenRayCaster11qt_metacastEPKc(
    Qt3DRender::QScreenRayCaster *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QScreenRayCaster::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender16QScreenRayCaster11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QScreenRayCaster *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QScreenRayCaster::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender16QScreenRayCaster2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QScreenRayCaster::tr(s, c, n));
}

//  Qt3DRender::QScreenRayCaster::QScreenRayCaster(QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QScreenRayCaster *ritual_ZN10Qt3DRender16QScreenRayCasterC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QScreenRayCaster(parent);
}

//  Qt3DRender::QScreenRayCaster::~QScreenRayCaster()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QScreenRayCasterD1Ev(
    Qt3DRender::QScreenRayCaster *self) {
  delete self;
}

//  QPoint Qt3DRender::QScreenRayCaster::position() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK10Qt3DRender16QScreenRayCaster8positionEv(
    const Qt3DRender::QScreenRayCaster *self) {
  return new QPoint(self->position());
}

//  void Qt3DRender::QScreenRayCaster::setPosition(const QPoint &position)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QScreenRayCaster11setPositionERK6QPoint(
    Qt3DRender::QScreenRayCaster *self,
    const QPoint *position) {
  self->setPosition(*position);
}

//  void Qt3DRender::QScreenRayCaster::trigger()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QScreenRayCaster7triggerEv(
    Qt3DRender::QScreenRayCaster *self) {
  self->trigger();
}

//  void Qt3DRender::QScreenRayCaster::trigger(const QPoint &position)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QScreenRayCaster7triggerERK6QPoint(
    Qt3DRender::QScreenRayCaster *self,
    const QPoint *position) {
  self->trigger(*position);
}

//  Qt3DRender::QAbstractRayCaster::Hits
//      Qt3DRender::QScreenRayCaster::pick(const QPoint &position)
extern "C" Q_DECL_EXPORT
Qt3DRender::QAbstractRayCaster::Hits *ritual_ZN10Qt3DRender16QScreenRayCaster4pickERK6QPoint(
    Qt3DRender::QScreenRayCaster *self,
    const QPoint *position) {
  return new Qt3DRender::QAbstractRayCaster::Hits(self->pick(*position));
}

//  void Qt3DRender::QScreenRayCaster::positionChanged(const QPoint
//      &position)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender16QScreenRayCaster15positionChangedERK6QPoint(
    Qt3DRender::QScreenRayCaster *self,
    const QPoint *position) {
  self->positionChanged(*position);
}

//  Qt3DRender::QScreenRayCaster::QScreenRayCaster(QAbstractRayCasterPrivate
//      &dd, QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QScreenRayCaster *ritual_ZN10Qt3DRender16QScreenRayCasterC1ERNS_25QAbstractRayCasterPrivateEPN8Qt3DCore5QNodeE(
    Qt3DRender::QAbstractRayCasterPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QScreenRayCaster(*dd, parent);
}

//  a Python function taken by a CuteQt3DRender_QScreenRayCaster, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QScreenRayCaster(
    Qt3DRender::QScreenRayCaster *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QScreenRayCaster *>(self)->take(key, call);
}

//  a Qt3DRender::QAbstractRayCaster::Hits a ritual of
//      Qt3DRender::QScreenRayCaster gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_QScreenRayCaster__Qt3DRender_QAbstractRayCaster_Hits(
    Qt3DRender::QAbstractRayCaster::Hits *self) {
  delete self;
}
