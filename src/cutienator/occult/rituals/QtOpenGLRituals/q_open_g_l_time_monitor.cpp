//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/qopengltimerquery.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtOpenGL/qtopenglglobal.h>
#if !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
#include <QtOpenGL/qopengltimerquery.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QList>

//  A QOpenGLTimeMonitor that Python can take functions over in. Every QOpenGLTimeMonitor
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOpenGLTimeMonitorCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOpenGLTimeMonitorCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpenGLTimeMonitorCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpenGLTimeMonitorCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpenGLTimeMonitorCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpenGLTimeMonitorCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpenGLTimeMonitorCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQOpenGLTimeMonitor : public QOpenGLTimeMonitor {
public:
  using QOpenGLTimeMonitor::QOpenGLTimeMonitor;
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
      CuteQOpenGLTimeMonitorCall0 call = reinterpret_cast<CuteQOpenGLTimeMonitorCall0>(taken[0]);
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
      CuteQOpenGLTimeMonitorCall1 call = reinterpret_cast<CuteQOpenGLTimeMonitorCall1>(taken[1]);
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
      CuteQOpenGLTimeMonitorCall2 call = reinterpret_cast<CuteQOpenGLTimeMonitorCall2>(taken[2]);
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
      CuteQOpenGLTimeMonitorCall3 call = reinterpret_cast<CuteQOpenGLTimeMonitorCall3>(taken[3]);
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
      CuteQOpenGLTimeMonitorCall4 call = reinterpret_cast<CuteQOpenGLTimeMonitorCall4>(taken[4]);
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
      CuteQOpenGLTimeMonitorCall5 call = reinterpret_cast<CuteQOpenGLTimeMonitorCall5>(taken[5]);
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
      CuteQOpenGLTimeMonitorCall6 call = reinterpret_cast<CuteQOpenGLTimeMonitorCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QOpenGLTimeMonitor::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QOpenGLTimeMonitor10metaObjectEv(
    const QOpenGLTimeMonitor *self) {
  return self->metaObject();
}

//  void *QOpenGLTimeMonitor::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18QOpenGLTimeMonitor11qt_metacastEPKc(
    QOpenGLTimeMonitor *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QOpenGLTimeMonitor::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QOpenGLTimeMonitor11qt_metacallEN11QMetaObject4CallEiPPv(
    QOpenGLTimeMonitor *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QOpenGLTimeMonitor::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QOpenGLTimeMonitor2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QOpenGLTimeMonitor::tr(s, c, n));
}

//  QOpenGLTimeMonitor::QOpenGLTimeMonitor(QObject *parent)
extern "C" Q_DECL_EXPORT
QOpenGLTimeMonitor *ritual_ZN18QOpenGLTimeMonitorC1EP7QObject(
    QObject *parent) {
  return new CuteQOpenGLTimeMonitor(parent);
}

//  QOpenGLTimeMonitor::~QOpenGLTimeMonitor()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QOpenGLTimeMonitorD1Ev(QOpenGLTimeMonitor *self) {
  delete self;
}

//  void QOpenGLTimeMonitor::setSampleCount(int sampleCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QOpenGLTimeMonitor14setSampleCountEi(
    QOpenGLTimeMonitor *self,
    int sampleCount) {
  self->setSampleCount(sampleCount);
}

//  int QOpenGLTimeMonitor::sampleCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QOpenGLTimeMonitor11sampleCountEv(
    const QOpenGLTimeMonitor *self) {
  return self->sampleCount();
}

//  bool QOpenGLTimeMonitor::create()
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QOpenGLTimeMonitor6createEv(QOpenGLTimeMonitor *self) {
  return self->create();
}

//  void QOpenGLTimeMonitor::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QOpenGLTimeMonitor7destroyEv(QOpenGLTimeMonitor *self) {
  self->destroy();
}

//  bool QOpenGLTimeMonitor::isCreated() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QOpenGLTimeMonitor9isCreatedEv(
    const QOpenGLTimeMonitor *self) {
  return self->isCreated();
}

//  QList<GLuint> QOpenGLTimeMonitor::objectIds() const
extern "C" Q_DECL_EXPORT
QList<GLuint> *ritual_ZNK18QOpenGLTimeMonitor9objectIdsEv(
    const QOpenGLTimeMonitor *self) {
  return new QList<GLuint>(self->objectIds());
}

//  int QOpenGLTimeMonitor::recordSample()
extern "C" Q_DECL_EXPORT
int ritual_ZN18QOpenGLTimeMonitor12recordSampleEv(QOpenGLTimeMonitor *self) {
  return self->recordSample();
}

//  bool QOpenGLTimeMonitor::isResultAvailable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QOpenGLTimeMonitor17isResultAvailableEv(
    const QOpenGLTimeMonitor *self) {
  return self->isResultAvailable();
}

//  QList<GLuint64> QOpenGLTimeMonitor::waitForSamples() const
extern "C" Q_DECL_EXPORT
QList<GLuint64> *ritual_ZNK18QOpenGLTimeMonitor14waitForSamplesEv(
    const QOpenGLTimeMonitor *self) {
  return new QList<GLuint64>(self->waitForSamples());
}

//  QList<GLuint64> QOpenGLTimeMonitor::waitForIntervals() const
extern "C" Q_DECL_EXPORT
QList<GLuint64> *ritual_ZNK18QOpenGLTimeMonitor16waitForIntervalsEv(
    const QOpenGLTimeMonitor *self) {
  return new QList<GLuint64>(self->waitForIntervals());
}

//  void QOpenGLTimeMonitor::reset()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QOpenGLTimeMonitor5resetEv(QOpenGLTimeMonitor *self) {
  self->reset();
}

//  QOpenGLTimeMonitorPrivate *QOpenGLTimeMonitor::d_func()
extern "C" Q_DECL_EXPORT
QOpenGLTimeMonitorPrivate *ritual_ZN18QOpenGLTimeMonitor6d_funcEv(
    QOpenGLTimeMonitor *self) {
  return self->d_func();
}

//  const QOpenGLTimeMonitorPrivate *QOpenGLTimeMonitor::d_func() const
extern "C" Q_DECL_EXPORT
const QOpenGLTimeMonitorPrivate *ritual_ZNK18QOpenGLTimeMonitor6d_funcEv(
    const QOpenGLTimeMonitor *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQOpenGLTimeMonitor, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOpenGLTimeMonitor(
    QOpenGLTimeMonitor *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOpenGLTimeMonitor *>(self)->take(key, call);
}

//  a QList<GLuint> a ritual of QOpenGLTimeMonitor gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QOpenGLTimeMonitor__QList_GLuint(QList<GLuint> *self) {
  delete self;
}

//  a QList<GLuint64> a ritual of QOpenGLTimeMonitor gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QOpenGLTimeMonitor__QList_GLuint64(QList<GLuint64> *self) {
  delete self;
}

#endif  // !defined(QT_NO_OPENGL) && !QT_CONFIG(opengles2)
