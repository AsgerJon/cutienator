//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qopenglcontext.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qopenglcontext.h>
#include <QtCore/qstring.h>
#include <QtGui/qsurfaceformat.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QOpenGLContext that Python can take functions over in. Every QOpenGLContext
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQOpenGLContextCall0)(const void *, QEvent *, int *);
typedef bool (*CuteQOpenGLContextCall1)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQOpenGLContextCall2)(const void *, QTimerEvent *, int *);
typedef void (*CuteQOpenGLContextCall3)(const void *, QChildEvent *, int *);
typedef void (*CuteQOpenGLContextCall4)(const void *, QEvent *, int *);
typedef void (*CuteQOpenGLContextCall5)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQOpenGLContextCall6)(const void *, const QMetaMethod *, int *);
class CuteQOpenGLContext : public QOpenGLContext {
public:
  using QOpenGLContext::QOpenGLContext;
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
      CuteQOpenGLContextCall0 call = reinterpret_cast<CuteQOpenGLContextCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQOpenGLContextCall1 call = reinterpret_cast<CuteQOpenGLContextCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQOpenGLContextCall2 call = reinterpret_cast<CuteQOpenGLContextCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQOpenGLContextCall3 call = reinterpret_cast<CuteQOpenGLContextCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQOpenGLContextCall4 call = reinterpret_cast<CuteQOpenGLContextCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQOpenGLContextCall5 call = reinterpret_cast<CuteQOpenGLContextCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQOpenGLContextCall6 call = reinterpret_cast<CuteQOpenGLContextCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QOpenGLContext::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QOpenGLContext10metaObjectEv(
    const QOpenGLContext *self) {
  return self->metaObject();
}

//  QString QOpenGLContext::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QOpenGLContext2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QOpenGLContext::tr(s, c, n));
}

//  QOpenGLContext::QOpenGLContext(QObject *parent)
extern "C" Q_DECL_EXPORT
QOpenGLContext *ritual_ZN14QOpenGLContextC1EP7QObject(QObject *parent) {
  return new CuteQOpenGLContext(parent);
}

//  QOpenGLContext::~QOpenGLContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpenGLContextD1Ev(QOpenGLContext *self) {
  delete self;
}

//  void QOpenGLContext::setFormat(const QSurfaceFormat &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpenGLContext9setFormatERK14QSurfaceFormat(
    QOpenGLContext *self,
    const QSurfaceFormat *format) {
  self->setFormat(*format);
}

//  void QOpenGLContext::setShareContext(QOpenGLContext *shareContext)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpenGLContext15setShareContextEPS_(
    QOpenGLContext *self,
    QOpenGLContext *shareContext) {
  self->setShareContext(shareContext);
}

//  void QOpenGLContext::setScreen(QScreen *screen)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpenGLContext9setScreenEP7QScreen(
    QOpenGLContext *self,
    QScreen *screen) {
  self->setScreen(screen);
}

//  bool QOpenGLContext::create()
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QOpenGLContext6createEv(QOpenGLContext *self) {
  return self->create();
}

//  bool QOpenGLContext::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QOpenGLContext7isValidEv(const QOpenGLContext *self) {
  return self->isValid();
}

//  QSurfaceFormat QOpenGLContext::format() const
extern "C" Q_DECL_EXPORT
QSurfaceFormat *ritual_ZNK14QOpenGLContext6formatEv(
    const QOpenGLContext *self) {
  return new QSurfaceFormat(self->format());
}

//  QOpenGLContext *QOpenGLContext::shareContext() const
extern "C" Q_DECL_EXPORT
QOpenGLContext *ritual_ZNK14QOpenGLContext12shareContextEv(
    const QOpenGLContext *self) {
  return self->shareContext();
}

//  QOpenGLContextGroup *QOpenGLContext::shareGroup() const
extern "C" Q_DECL_EXPORT
QOpenGLContextGroup *ritual_ZNK14QOpenGLContext10shareGroupEv(
    const QOpenGLContext *self) {
  return self->shareGroup();
}

//  QScreen *QOpenGLContext::screen() const
extern "C" Q_DECL_EXPORT
QScreen *ritual_ZNK14QOpenGLContext6screenEv(const QOpenGLContext *self) {
  return self->screen();
}

//  bool QOpenGLContext::makeCurrent(QSurface *surface)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QOpenGLContext11makeCurrentEP8QSurface(
    QOpenGLContext *self,
    QSurface *surface) {
  return self->makeCurrent(surface);
}

//  void QOpenGLContext::doneCurrent()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpenGLContext11doneCurrentEv(QOpenGLContext *self) {
  self->doneCurrent();
}

//  void QOpenGLContext::swapBuffers(QSurface *surface)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpenGLContext11swapBuffersEP8QSurface(
    QOpenGLContext *self,
    QSurface *surface) {
  self->swapBuffers(surface);
}

//  QSurface *QOpenGLContext::surface() const
extern "C" Q_DECL_EXPORT
QSurface *ritual_ZNK14QOpenGLContext7surfaceEv(const QOpenGLContext *self) {
  return self->surface();
}

//  QOpenGLContext *QOpenGLContext::currentContext()
extern "C" Q_DECL_EXPORT
QOpenGLContext *ritual_ZN14QOpenGLContext14currentContextEv() {
  return QOpenGLContext::currentContext();
}

//  bool QOpenGLContext::areSharing(QOpenGLContext *first, QOpenGLContext
//      *second)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QOpenGLContext10areSharingEPS_S0_(
    QOpenGLContext *first,
    QOpenGLContext *second) {
  return QOpenGLContext::areSharing(first, second);
}

//  QOpenGLFunctions *QOpenGLContext::functions() const
extern "C" Q_DECL_EXPORT
QOpenGLFunctions *ritual_ZNK14QOpenGLContext9functionsEv(
    const QOpenGLContext *self) {
  return self->functions();
}

//  QOpenGLExtraFunctions *QOpenGLContext::extraFunctions() const
extern "C" Q_DECL_EXPORT
QOpenGLExtraFunctions *ritual_ZNK14QOpenGLContext14extraFunctionsEv(
    const QOpenGLContext *self) {
  return self->extraFunctions();
}

//  bool QOpenGLContext::hasExtension(const QByteArray &extension) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QOpenGLContext12hasExtensionERK10QByteArray(
    const QOpenGLContext *self,
    const QByteArray *extension) {
  return self->hasExtension(*extension);
}

//  OpenGLModuleType QOpenGLContext::openGLModuleType()
extern "C" Q_DECL_EXPORT
QOpenGLContext::OpenGLModuleType ritual_ZN14QOpenGLContext16openGLModuleTypeEv() {
  return QOpenGLContext::openGLModuleType();
}

//  bool QOpenGLContext::isOpenGLES() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QOpenGLContext10isOpenGLESEv(const QOpenGLContext *self) {
  return self->isOpenGLES();
}

//  bool QOpenGLContext::supportsThreadedOpenGL()
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QOpenGLContext22supportsThreadedOpenGLEv() {
  return QOpenGLContext::supportsThreadedOpenGL();
}

//  QOpenGLContext *QOpenGLContext::globalShareContext()
extern "C" Q_DECL_EXPORT
QOpenGLContext *ritual_ZN14QOpenGLContext18globalShareContextEv() {
  return QOpenGLContext::globalShareContext();
}

//  a Python function taken by a CuteQOpenGLContext, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOpenGLContext(
    QOpenGLContext *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOpenGLContext *>(self)->take(key, call);
}
