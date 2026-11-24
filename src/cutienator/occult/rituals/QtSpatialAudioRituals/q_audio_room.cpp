//  Written by dev_tooling.RitualGenerator from the records of
//  QtSpatialAudio/qaudioroom.h, Qt 6.12.0. Changes made here are lost.
#include <QtSpatialAudio/qaudioroom.h>
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#include <QtGui/qquaternion.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QAudioRoom that Python can take functions over in. Every QAudioRoom
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAudioRoomCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAudioRoomCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAudioRoomCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAudioRoomCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAudioRoomCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAudioRoomCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAudioRoomCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAudioRoom : public QAudioRoom {
public:
  using QAudioRoom::QAudioRoom;
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
      CuteQAudioRoomCall0 call = reinterpret_cast<CuteQAudioRoomCall0>(taken[0]);
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
      CuteQAudioRoomCall1 call = reinterpret_cast<CuteQAudioRoomCall1>(taken[1]);
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
      CuteQAudioRoomCall2 call = reinterpret_cast<CuteQAudioRoomCall2>(taken[2]);
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
      CuteQAudioRoomCall3 call = reinterpret_cast<CuteQAudioRoomCall3>(taken[3]);
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
      CuteQAudioRoomCall4 call = reinterpret_cast<CuteQAudioRoomCall4>(taken[4]);
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
      CuteQAudioRoomCall5 call = reinterpret_cast<CuteQAudioRoomCall5>(taken[5]);
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
      CuteQAudioRoomCall6 call = reinterpret_cast<CuteQAudioRoomCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAudioRoom::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QAudioRoom10metaObjectEv(
    const QAudioRoom *self) {
  return self->metaObject();
}

//  QString QAudioRoom::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QAudioRoom2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAudioRoom::tr(s, c, n));
}

//  QAudioRoom::QAudioRoom(QAudioEngine *engine)
extern "C" Q_DECL_EXPORT
QAudioRoom *ritual_ZN10QAudioRoomC1EP12QAudioEngine(QAudioEngine *engine) {
  return new CuteQAudioRoom(engine);
}

//  QAudioRoom::~QAudioRoom()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QAudioRoomD1Ev(QAudioRoom *self) {
  delete self;
}

//  void QAudioRoom::setPosition(QVector3D pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QAudioRoom11setPositionE9QVector3D(
    QAudioRoom *self,
    const QVector3D *pos) {
  self->setPosition(*pos);
}

//  QVector3D QAudioRoom::position() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK10QAudioRoom8positionEv(const QAudioRoom *self) {
  return new QVector3D(self->position());
}

//  void QAudioRoom::setDimensions(QVector3D dim)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QAudioRoom13setDimensionsE9QVector3D(
    QAudioRoom *self,
    const QVector3D *dim) {
  self->setDimensions(*dim);
}

//  QVector3D QAudioRoom::dimensions() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK10QAudioRoom10dimensionsEv(const QAudioRoom *self) {
  return new QVector3D(self->dimensions());
}

//  void QAudioRoom::setRotation(const QQuaternion &q)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QAudioRoom11setRotationERK11QQuaternion(
    QAudioRoom *self,
    const QQuaternion *q) {
  self->setRotation(*q);
}

//  QQuaternion QAudioRoom::rotation() const
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZNK10QAudioRoom8rotationEv(const QAudioRoom *self) {
  return new QQuaternion(self->rotation());
}

//  void QAudioRoom::setWallMaterial(Wall wall, Material material)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QAudioRoom15setWallMaterialENS_4WallENS_8MaterialE(
    QAudioRoom *self,
    QAudioRoom::Wall wall,
    QAudioRoom::Material material) {
  self->setWallMaterial(wall, material);
}

//  Material QAudioRoom::wallMaterial(Wall wall) const
extern "C" Q_DECL_EXPORT
QAudioRoom::Material ritual_ZNK10QAudioRoom12wallMaterialENS_4WallE(
    const QAudioRoom *self,
    QAudioRoom::Wall wall) {
  return self->wallMaterial(wall);
}

//  void QAudioRoom::setReflectionGain(float factor)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QAudioRoom17setReflectionGainEf(
    QAudioRoom *self,
    float factor) {
  self->setReflectionGain(factor);
}

//  float QAudioRoom::reflectionGain() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10QAudioRoom14reflectionGainEv(const QAudioRoom *self) {
  return self->reflectionGain();
}

//  void QAudioRoom::setReverbGain(float factor)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QAudioRoom13setReverbGainEf(QAudioRoom *self, float factor) {
  self->setReverbGain(factor);
}

//  float QAudioRoom::reverbGain() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10QAudioRoom10reverbGainEv(const QAudioRoom *self) {
  return self->reverbGain();
}

//  void QAudioRoom::setReverbTime(float factor)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QAudioRoom13setReverbTimeEf(QAudioRoom *self, float factor) {
  self->setReverbTime(factor);
}

//  float QAudioRoom::reverbTime() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10QAudioRoom10reverbTimeEv(const QAudioRoom *self) {
  return self->reverbTime();
}

//  void QAudioRoom::setReverbBrightness(float factor)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QAudioRoom19setReverbBrightnessEf(
    QAudioRoom *self,
    float factor) {
  self->setReverbBrightness(factor);
}

//  float QAudioRoom::reverbBrightness() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10QAudioRoom16reverbBrightnessEv(const QAudioRoom *self) {
  return self->reverbBrightness();
}

//  a Python function taken by a CuteQAudioRoom, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAudioRoom(QAudioRoom *self, const char *key, void *call) {
  return static_cast<CuteQAudioRoom *>(self)->take(key, call);
}
