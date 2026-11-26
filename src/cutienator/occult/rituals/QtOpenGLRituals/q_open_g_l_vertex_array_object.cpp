//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/qopenglvertexarrayobject.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtOpenGL/qtopenglglobal.h>
#if !defined(QT_NO_OPENGL)
#include <QtOpenGL/qopenglvertexarrayobject.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QOpenGLVertexArrayObject that Python can take functions over in. Every QOpenGLVertexArrayObject
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOpenGLVertexArrayObjectCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOpenGLVertexArrayObjectCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpenGLVertexArrayObjectCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpenGLVertexArrayObjectCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpenGLVertexArrayObjectCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpenGLVertexArrayObjectCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpenGLVertexArrayObjectCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQOpenGLVertexArrayObject : public QOpenGLVertexArrayObject {
public:
  using QOpenGLVertexArrayObject::QOpenGLVertexArrayObject;
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
      CuteQOpenGLVertexArrayObjectCall0 call = reinterpret_cast<CuteQOpenGLVertexArrayObjectCall0>(taken[0]);
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
      CuteQOpenGLVertexArrayObjectCall1 call = reinterpret_cast<CuteQOpenGLVertexArrayObjectCall1>(taken[1]);
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
      CuteQOpenGLVertexArrayObjectCall2 call = reinterpret_cast<CuteQOpenGLVertexArrayObjectCall2>(taken[2]);
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
      CuteQOpenGLVertexArrayObjectCall3 call = reinterpret_cast<CuteQOpenGLVertexArrayObjectCall3>(taken[3]);
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
      CuteQOpenGLVertexArrayObjectCall4 call = reinterpret_cast<CuteQOpenGLVertexArrayObjectCall4>(taken[4]);
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
      CuteQOpenGLVertexArrayObjectCall5 call = reinterpret_cast<CuteQOpenGLVertexArrayObjectCall5>(taken[5]);
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
      CuteQOpenGLVertexArrayObjectCall6 call = reinterpret_cast<CuteQOpenGLVertexArrayObjectCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QOpenGLVertexArrayObject::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QOpenGLVertexArrayObject10metaObjectEv(
    const QOpenGLVertexArrayObject *self) {
  return self->metaObject();
}

//  void *QOpenGLVertexArrayObject::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24QOpenGLVertexArrayObject11qt_metacastEPKc(
    QOpenGLVertexArrayObject *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QOpenGLVertexArrayObject::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN24QOpenGLVertexArrayObject11qt_metacallEN11QMetaObject4CallEiPPv(
    QOpenGLVertexArrayObject *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QOpenGLVertexArrayObject::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN24QOpenGLVertexArrayObject2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QOpenGLVertexArrayObject::tr(s, c, n));
}

//  QOpenGLVertexArrayObject::QOpenGLVertexArrayObject(QObject *parent)
extern "C" Q_DECL_EXPORT
QOpenGLVertexArrayObject *ritual_ZN24QOpenGLVertexArrayObjectC1EP7QObject(
    QObject *parent) {
  return new CuteQOpenGLVertexArrayObject(parent);
}

//  QOpenGLVertexArrayObject::~QOpenGLVertexArrayObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QOpenGLVertexArrayObjectD1Ev(
    QOpenGLVertexArrayObject *self) {
  delete self;
}

//  bool QOpenGLVertexArrayObject::create()
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QOpenGLVertexArrayObject6createEv(
    QOpenGLVertexArrayObject *self) {
  return self->create();
}

//  void QOpenGLVertexArrayObject::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QOpenGLVertexArrayObject7destroyEv(
    QOpenGLVertexArrayObject *self) {
  self->destroy();
}

//  bool QOpenGLVertexArrayObject::isCreated() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QOpenGLVertexArrayObject9isCreatedEv(
    const QOpenGLVertexArrayObject *self) {
  return self->isCreated();
}

//  GLuint QOpenGLVertexArrayObject::objectId() const
extern "C" Q_DECL_EXPORT
GLuint ritual_ZNK24QOpenGLVertexArrayObject8objectIdEv(
    const QOpenGLVertexArrayObject *self) {
  return self->objectId();
}

//  void QOpenGLVertexArrayObject::bind()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QOpenGLVertexArrayObject4bindEv(
    QOpenGLVertexArrayObject *self) {
  self->bind();
}

//  void QOpenGLVertexArrayObject::release()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QOpenGLVertexArrayObject7releaseEv(
    QOpenGLVertexArrayObject *self) {
  self->release();
}

//  QOpenGLVertexArrayObjectPrivate *QOpenGLVertexArrayObject::d_func()
extern "C" Q_DECL_EXPORT
QOpenGLVertexArrayObjectPrivate *ritual_ZN24QOpenGLVertexArrayObject6d_funcEv(
    QOpenGLVertexArrayObject *self) {
  return self->d_func();
}

//  const QOpenGLVertexArrayObjectPrivate *QOpenGLVertexArrayObject::d_func()
//      const
extern "C" Q_DECL_EXPORT
const QOpenGLVertexArrayObjectPrivate *ritual_ZNK24QOpenGLVertexArrayObject6d_funcEv(
    const QOpenGLVertexArrayObject *self) {
  return self->d_func();
}

//  QOpenGLVertexArrayObject::QOpenGLVertexArrayObject(QOpenGLVertexArrayObje
//      ctPrivate &dd)
extern "C" Q_DECL_EXPORT
QOpenGLVertexArrayObject *ritual_ZN24QOpenGLVertexArrayObjectC1ER31QOpenGLVertexArrayObjectPrivate(
    QOpenGLVertexArrayObjectPrivate *dd) {
  return new CuteQOpenGLVertexArrayObject(*dd);
}

//  a Python function taken by a CuteQOpenGLVertexArrayObject, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOpenGLVertexArrayObject(
    QOpenGLVertexArrayObject *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOpenGLVertexArrayObject *>(self)->take(key, call);
}

#endif  // !defined(QT_NO_OPENGL)
