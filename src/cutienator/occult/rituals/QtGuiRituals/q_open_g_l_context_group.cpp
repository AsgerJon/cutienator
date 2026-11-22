//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qopenglcontext.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qopenglcontext.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QOpenGLContextGroup that Python can take functions over in. Every QOpenGLContextGroup
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQOpenGLContextGroupCall0)(const void *, QEvent *, int *);
typedef bool (*CuteQOpenGLContextGroupCall1)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQOpenGLContextGroupCall2)(const void *, QTimerEvent *, int *);
typedef void (*CuteQOpenGLContextGroupCall3)(const void *, QChildEvent *, int *);
typedef void (*CuteQOpenGLContextGroupCall4)(const void *, QEvent *, int *);
typedef void (*CuteQOpenGLContextGroupCall5)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQOpenGLContextGroupCall6)(const void *, const QMetaMethod *, int *);
class CuteQOpenGLContextGroup : public QOpenGLContextGroup {
public:
  using QOpenGLContextGroup::QOpenGLContextGroup;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
    return false;
  }

  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQOpenGLContextGroupCall0 call = reinterpret_cast<CuteQOpenGLContextGroupCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQOpenGLContextGroupCall1 call = reinterpret_cast<CuteQOpenGLContextGroupCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQOpenGLContextGroupCall2 call = reinterpret_cast<CuteQOpenGLContextGroupCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQOpenGLContextGroupCall3 call = reinterpret_cast<CuteQOpenGLContextGroupCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQOpenGLContextGroupCall4 call = reinterpret_cast<CuteQOpenGLContextGroupCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQOpenGLContextGroupCall5 call = reinterpret_cast<CuteQOpenGLContextGroupCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQOpenGLContextGroupCall6 call = reinterpret_cast<CuteQOpenGLContextGroupCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QOpenGLContextGroup::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QOpenGLContextGroup10metaObjectEv(
    const QOpenGLContextGroup *self) {
  return self->metaObject();
}

//  QString QOpenGLContextGroup::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QOpenGLContextGroup2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QOpenGLContextGroup::tr(s, c, n));
}

//  QOpenGLContextGroup::~QOpenGLContextGroup()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QOpenGLContextGroupD1Ev(QOpenGLContextGroup *self) {
  delete self;
}

//  QOpenGLContextGroup *QOpenGLContextGroup::currentContextGroup()
extern "C" Q_DECL_EXPORT
QOpenGLContextGroup *ritual_ZN19QOpenGLContextGroup19currentContextGroupEv() {
  return QOpenGLContextGroup::currentContextGroup();
}

//  a Python function taken by a CuteQOpenGLContextGroup, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOpenGLContextGroup(
    QOpenGLContextGroup *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOpenGLContextGroup *>(self)->take(key, call);
}
