//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/qopengltimerquery.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtOpenGL/qtopenglglobal.h>
#if !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
#include <QtOpenGL/qopengltimerquery.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QOpenGLTimerQuery that Python can take functions over in. Every QOpenGLTimerQuery
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOpenGLTimerQueryCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOpenGLTimerQueryCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpenGLTimerQueryCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpenGLTimerQueryCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpenGLTimerQueryCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpenGLTimerQueryCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpenGLTimerQueryCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQOpenGLTimerQuery : public QOpenGLTimerQuery {
public:
  using QOpenGLTimerQuery::QOpenGLTimerQuery;
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
      CuteQOpenGLTimerQueryCall0 call = reinterpret_cast<CuteQOpenGLTimerQueryCall0>(taken[0]);
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
      CuteQOpenGLTimerQueryCall1 call = reinterpret_cast<CuteQOpenGLTimerQueryCall1>(taken[1]);
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
      CuteQOpenGLTimerQueryCall2 call = reinterpret_cast<CuteQOpenGLTimerQueryCall2>(taken[2]);
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
      CuteQOpenGLTimerQueryCall3 call = reinterpret_cast<CuteQOpenGLTimerQueryCall3>(taken[3]);
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
      CuteQOpenGLTimerQueryCall4 call = reinterpret_cast<CuteQOpenGLTimerQueryCall4>(taken[4]);
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
      CuteQOpenGLTimerQueryCall5 call = reinterpret_cast<CuteQOpenGLTimerQueryCall5>(taken[5]);
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
      CuteQOpenGLTimerQueryCall6 call = reinterpret_cast<CuteQOpenGLTimerQueryCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QOpenGLTimerQuery::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QOpenGLTimerQuery10metaObjectEv(
    const QOpenGLTimerQuery *self) {
  return self->metaObject();
}

//  void *QOpenGLTimerQuery::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QOpenGLTimerQuery11qt_metacastEPKc(
    QOpenGLTimerQuery *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QOpenGLTimerQuery::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QOpenGLTimerQuery11qt_metacallEN11QMetaObject4CallEiPPv(
    QOpenGLTimerQuery *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QOpenGLTimerQuery::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QOpenGLTimerQuery2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QOpenGLTimerQuery::tr(s, c, n));
}

//  QOpenGLTimerQuery::QOpenGLTimerQuery(QObject *parent)
extern "C" Q_DECL_EXPORT
QOpenGLTimerQuery *ritual_ZN17QOpenGLTimerQueryC1EP7QObject(
    QObject *parent) {
  return new CuteQOpenGLTimerQuery(parent);
}

//  QOpenGLTimerQuery::~QOpenGLTimerQuery()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOpenGLTimerQueryD1Ev(QOpenGLTimerQuery *self) {
  delete self;
}

//  bool QOpenGLTimerQuery::create()
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QOpenGLTimerQuery6createEv(QOpenGLTimerQuery *self) {
  return self->create();
}

//  void QOpenGLTimerQuery::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOpenGLTimerQuery7destroyEv(QOpenGLTimerQuery *self) {
  self->destroy();
}

//  bool QOpenGLTimerQuery::isCreated() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QOpenGLTimerQuery9isCreatedEv(
    const QOpenGLTimerQuery *self) {
  return self->isCreated();
}

//  GLuint QOpenGLTimerQuery::objectId() const
extern "C" Q_DECL_EXPORT
GLuint ritual_ZNK17QOpenGLTimerQuery8objectIdEv(
    const QOpenGLTimerQuery *self) {
  return self->objectId();
}

//  void QOpenGLTimerQuery::begin()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOpenGLTimerQuery5beginEv(QOpenGLTimerQuery *self) {
  self->begin();
}

//  void QOpenGLTimerQuery::end()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOpenGLTimerQuery3endEv(QOpenGLTimerQuery *self) {
  self->end();
}

//  GLuint64 QOpenGLTimerQuery::waitForTimestamp() const
extern "C" Q_DECL_EXPORT
GLuint64 ritual_ZNK17QOpenGLTimerQuery16waitForTimestampEv(
    const QOpenGLTimerQuery *self) {
  return self->waitForTimestamp();
}

//  void QOpenGLTimerQuery::recordTimestamp()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QOpenGLTimerQuery15recordTimestampEv(
    QOpenGLTimerQuery *self) {
  self->recordTimestamp();
}

//  bool QOpenGLTimerQuery::isResultAvailable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QOpenGLTimerQuery17isResultAvailableEv(
    const QOpenGLTimerQuery *self) {
  return self->isResultAvailable();
}

//  GLuint64 QOpenGLTimerQuery::waitForResult() const
extern "C" Q_DECL_EXPORT
GLuint64 ritual_ZNK17QOpenGLTimerQuery13waitForResultEv(
    const QOpenGLTimerQuery *self) {
  return self->waitForResult();
}

//  QOpenGLTimerQueryPrivate *QOpenGLTimerQuery::d_func()
extern "C" Q_DECL_EXPORT
QOpenGLTimerQueryPrivate *ritual_ZN17QOpenGLTimerQuery6d_funcEv(
    QOpenGLTimerQuery *self) {
  return self->d_func();
}

//  const QOpenGLTimerQueryPrivate *QOpenGLTimerQuery::d_func() const
extern "C" Q_DECL_EXPORT
const QOpenGLTimerQueryPrivate *ritual_ZNK17QOpenGLTimerQuery6d_funcEv(
    const QOpenGLTimerQuery *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQOpenGLTimerQuery, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOpenGLTimerQuery(
    QOpenGLTimerQuery *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOpenGLTimerQuery *>(self)->take(key, call);
}

#endif  // !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
