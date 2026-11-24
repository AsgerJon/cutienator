//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/q3dobject.h, Qt 6.12.0. Changes made here are lost.
#include <QtDataVisualization/q3dobject.h>
#include <QtCore/qstring.h>
#include <QtGui/qvectornd.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Q3DObject that Python can take functions over in. Every Q3DObject
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQ3DObjectCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQ3DObjectCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DObjectCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DObjectCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DObjectCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DObjectCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQ3DObjectCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQ3DObject : public Q3DObject {
public:
  using Q3DObject::Q3DObject;
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
      CuteQ3DObjectCall0 call = reinterpret_cast<CuteQ3DObjectCall0>(taken[0]);
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
      CuteQ3DObjectCall1 call = reinterpret_cast<CuteQ3DObjectCall1>(taken[1]);
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
      CuteQ3DObjectCall2 call = reinterpret_cast<CuteQ3DObjectCall2>(taken[2]);
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
      CuteQ3DObjectCall3 call = reinterpret_cast<CuteQ3DObjectCall3>(taken[3]);
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
      CuteQ3DObjectCall4 call = reinterpret_cast<CuteQ3DObjectCall4>(taken[4]);
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
      CuteQ3DObjectCall5 call = reinterpret_cast<CuteQ3DObjectCall5>(taken[5]);
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
      CuteQ3DObjectCall6 call = reinterpret_cast<CuteQ3DObjectCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Q3DObject::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9Q3DObject10metaObjectEv(
    const Q3DObject *self) {
  return self->metaObject();
}

//  QString Q3DObject::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9Q3DObject2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Q3DObject::tr(s, c, n));
}

//  Q3DObject::Q3DObject(QObject *parent)
extern "C" Q_DECL_EXPORT
Q3DObject *ritual_ZN9Q3DObjectC1EP7QObject(QObject *parent) {
  return new CuteQ3DObject(parent);
}

//  Q3DObject::~Q3DObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN9Q3DObjectD1Ev(Q3DObject *self) {
  delete self;
}

//  Q3DScene *Q3DObject::parentScene()
extern "C" Q_DECL_EXPORT
Q3DScene *ritual_ZN9Q3DObject11parentSceneEv(Q3DObject *self) {
  return self->parentScene();
}

//  QVector3D Q3DObject::position() const
extern "C" Q_DECL_EXPORT
QVector3D *ritual_ZNK9Q3DObject8positionEv(const Q3DObject *self) {
  return new QVector3D(self->position());
}

//  void Q3DObject::setPosition(const QVector3D &position)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Q3DObject11setPositionERK9QVector3D(
    Q3DObject *self,
    const QVector3D *position) {
  self->setPosition(*position);
}

//  void Q3DObject::setDirty(bool dirty)
extern "C" Q_DECL_EXPORT
void ritual_ZN9Q3DObject8setDirtyEb(Q3DObject *self, bool dirty) {
  self->setDirty(dirty);
}

//  bool Q3DObject::isDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9Q3DObject7isDirtyEv(const Q3DObject *self) {
  return self->isDirty();
}

//  a Python function taken by a CuteQ3DObject, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_Q3DObject(Q3DObject *self, const char *key, void *call) {
  return static_cast<CuteQ3DObject *>(self)->take(key, call);
}
