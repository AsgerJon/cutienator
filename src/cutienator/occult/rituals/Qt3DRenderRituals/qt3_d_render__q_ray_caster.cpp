//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/qraycaster.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DRender/qraycaster.h>
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <Qt3DRender/Qt3DRender>
#include <QtGui/QVector3D>

//  A Qt3DRender::QRayCaster that Python can take functions over in. Every Qt3DRender::QRayCaster
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QRayCasterCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_QRayCasterCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QRayCasterCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QRayCasterCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QRayCasterCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QRayCasterCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_QRayCasterCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_QRayCaster : public Qt3DRender::QRayCaster {
public:
  using Qt3DRender::QRayCaster::QRayCaster;
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
      CuteQt3DRender_QRayCasterCall0 call = reinterpret_cast<CuteQt3DRender_QRayCasterCall0>(taken[0]);
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
      CuteQt3DRender_QRayCasterCall1 call = reinterpret_cast<CuteQt3DRender_QRayCasterCall1>(taken[1]);
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
      CuteQt3DRender_QRayCasterCall2 call = reinterpret_cast<CuteQt3DRender_QRayCasterCall2>(taken[2]);
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
      CuteQt3DRender_QRayCasterCall3 call = reinterpret_cast<CuteQt3DRender_QRayCasterCall3>(taken[3]);
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
      CuteQt3DRender_QRayCasterCall4 call = reinterpret_cast<CuteQt3DRender_QRayCasterCall4>(taken[4]);
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
      CuteQt3DRender_QRayCasterCall5 call = reinterpret_cast<CuteQt3DRender_QRayCasterCall5>(taken[5]);
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
      CuteQt3DRender_QRayCasterCall6 call = reinterpret_cast<CuteQt3DRender_QRayCasterCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::QRayCaster::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender10QRayCaster10metaObjectEv(
    const Qt3DRender::QRayCaster *self) {
  return self->metaObject();
}

//  void *Qt3DRender::QRayCaster::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender10QRayCaster11qt_metacastEPKc(
    Qt3DRender::QRayCaster *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::QRayCaster::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender10QRayCaster11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::QRayCaster *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::QRayCaster::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender10QRayCaster2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::QRayCaster::tr(s, c, n));
}

//  Qt3DRender::QRayCaster::QRayCaster(QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QRayCaster *ritual_ZN10Qt3DRender10QRayCasterC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QRayCaster(parent);
}

//  Qt3DRender::QRayCaster::~QRayCaster()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QRayCasterD1Ev(Qt3DRender::QRayCaster *self) {
  delete self;
}

//  QVector3D Qt3DRender::QRayCaster::origin() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK10Qt3DRender10QRayCaster6originEv(
    const Qt3DRender::QRayCaster *self) {
  return new QVector3D(self->origin());
}

//  QVector3D Qt3DRender::QRayCaster::direction() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK10Qt3DRender10QRayCaster9directionEv(
    const Qt3DRender::QRayCaster *self) {
  return new QVector3D(self->direction());
}

//  float Qt3DRender::QRayCaster::length() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender10QRayCaster6lengthEv(
    const Qt3DRender::QRayCaster *self) {
  return self->length();
}

//  void Qt3DRender::QRayCaster::setOrigin(const QVector3D &origin)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QRayCaster9setOriginERK9QVector3D(
    Qt3DRender::QRayCaster *self,
    const QVector3D *origin) {
  self->setOrigin(*origin);
}

//  void Qt3DRender::QRayCaster::setDirection(const QVector3D &direction)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QRayCaster12setDirectionERK9QVector3D(
    Qt3DRender::QRayCaster *self,
    const QVector3D *direction) {
  self->setDirection(*direction);
}

//  void Qt3DRender::QRayCaster::setLength(float length)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QRayCaster9setLengthEf(
    Qt3DRender::QRayCaster *self,
    float length) {
  self->setLength(length);
}

//  void Qt3DRender::QRayCaster::trigger()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QRayCaster7triggerEv(
    Qt3DRender::QRayCaster *self) {
  self->trigger();
}

//  void Qt3DRender::QRayCaster::trigger(const QVector3D &origin, const
//      QVector3D &direction, float length)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QRayCaster7triggerERK9QVector3DS3_f(
    Qt3DRender::QRayCaster *self,
    const QVector3D *origin,
    const QVector3D *direction,
    float length) {
  self->trigger(*origin, *direction, length);
}

//  Qt3DRender::QAbstractRayCaster::Hits Qt3DRender::QRayCaster::pick(const
//      QVector3D &origin, const QVector3D &direction, float length)
extern "C" Q_DECL_EXPORT
Qt3DRender::QAbstractRayCaster::Hits *ritual_ZN10Qt3DRender10QRayCaster4pickERK9QVector3DS3_f(
    Qt3DRender::QRayCaster *self,
    const QVector3D *origin,
    const QVector3D *direction,
    float length) {
  return new Qt3DRender::QAbstractRayCaster::Hits(
      self->pick(
          *origin,
          *direction,
          length));
}

//  void Qt3DRender::QRayCaster::originChanged(const QVector3D &origin)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QRayCaster13originChangedERK9QVector3D(
    Qt3DRender::QRayCaster *self,
    const QVector3D *origin) {
  self->originChanged(*origin);
}

//  void Qt3DRender::QRayCaster::directionChanged(const QVector3D &direction)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QRayCaster16directionChangedERK9QVector3D(
    Qt3DRender::QRayCaster *self,
    const QVector3D *direction) {
  self->directionChanged(*direction);
}

//  void Qt3DRender::QRayCaster::lengthChanged(float length)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender10QRayCaster13lengthChangedEf(
    Qt3DRender::QRayCaster *self,
    float length) {
  self->lengthChanged(length);
}

//  Qt3DRender::QRayCaster::QRayCaster(QAbstractRayCasterPrivate &dd, QNode
//      *parent)
extern "C" Q_DECL_EXPORT
Qt3DRender::QRayCaster *ritual_ZN10Qt3DRender10QRayCasterC1ERNS_25QAbstractRayCasterPrivateEPN8Qt3DCore5QNodeE(
    Qt3DRender::QAbstractRayCasterPrivate *dd,
    Qt3DCore::QNode *parent) {
  return new CuteQt3DRender_QRayCaster(*dd, parent);
}

//  a Python function taken by a CuteQt3DRender_QRayCaster, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QRayCaster(
    Qt3DRender::QRayCaster *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QRayCaster *>(self)->take(key, call);
}

//  a Qt3DRender::QAbstractRayCaster::Hits a ritual of Qt3DRender::QRayCaster
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_QRayCaster__Qt3DRender_QAbstractRayCaster_Hits(
    Qt3DRender::QAbstractRayCaster::Hits *self) {
  delete self;
}
