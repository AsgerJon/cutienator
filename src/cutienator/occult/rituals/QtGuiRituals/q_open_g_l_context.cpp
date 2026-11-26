//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qopenglcontext.h, Qt 6.12.0. Edited by hand on 2026-11-25: added by
//  hand, instances of templates of the class: 4. Kept as it is when the
//  generator runs again.
#include <QtGui/qtguiglobal.h>
#if !defined(QT_NO_OPENGL)
#include <QtGui/qopenglcontext.h>
#include <QtCore/qstring.h>
#include <QtGui/qsurfaceformat.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtCore/QSet>
#include <QtCore/QByteArray>
#include <functional>
#include <QtGui/qopenglcontext_platform.h>

//  A QOpenGLContext that Python can take functions over in. Every QOpenGLContext
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOpenGLContextCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOpenGLContextCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpenGLContextCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpenGLContextCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpenGLContextCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpenGLContextCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpenGLContextCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQOpenGLContext : public QOpenGLContext {
public:
  using QOpenGLContext::QOpenGLContext;
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
      CuteQOpenGLContextCall0 call = reinterpret_cast<CuteQOpenGLContextCall0>(taken[0]);
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
      CuteQOpenGLContextCall1 call = reinterpret_cast<CuteQOpenGLContextCall1>(taken[1]);
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
      CuteQOpenGLContextCall2 call = reinterpret_cast<CuteQOpenGLContextCall2>(taken[2]);
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
      CuteQOpenGLContextCall3 call = reinterpret_cast<CuteQOpenGLContextCall3>(taken[3]);
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
      CuteQOpenGLContextCall4 call = reinterpret_cast<CuteQOpenGLContextCall4>(taken[4]);
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
      CuteQOpenGLContextCall5 call = reinterpret_cast<CuteQOpenGLContextCall5>(taken[5]);
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
      CuteQOpenGLContextCall6 call = reinterpret_cast<CuteQOpenGLContextCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QOpenGLContext::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QOpenGLContext10metaObjectEv(
    const QOpenGLContext *self) {
  return self->metaObject();
}

//  void *QOpenGLContext::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN14QOpenGLContext11qt_metacastEPKc(
    QOpenGLContext *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QOpenGLContext::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN14QOpenGLContext11qt_metacallEN11QMetaObject4CallEiPPv(
    QOpenGLContext *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QOpenGLContext::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QOpenGLContext2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QOpenGLContext::tr(s, c, n));
}

//  QOpenGLContextPrivate *QOpenGLContext::d_func()
extern "C" Q_DECL_EXPORT
QOpenGLContextPrivate *ritual_ZN14QOpenGLContext6d_funcEv(
    QOpenGLContext *self) {
  return self->d_func();
}

//  const QOpenGLContextPrivate *QOpenGLContext::d_func() const
extern "C" Q_DECL_EXPORT
const QOpenGLContextPrivate *ritual_ZNK14QOpenGLContext6d_funcEv(
    const QOpenGLContext *self) {
  return self->d_func();
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

//  GLuint QOpenGLContext::defaultFramebufferObject() const
extern "C" Q_DECL_EXPORT
GLuint ritual_ZNK14QOpenGLContext24defaultFramebufferObjectEv(
    const QOpenGLContext *self) {
  return self->defaultFramebufferObject();
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

//  QFunctionPointer QOpenGLContext::getProcAddress(const QByteArray
//      &procName) const
extern "C" Q_DECL_EXPORT
void *ritual_ZNK14QOpenGLContext14getProcAddressERK10QByteArray(
    const QOpenGLContext *self,
    const QByteArray *procName) {
  return reinterpret_cast<void *>(self->getProcAddress(*procName));
}

//  QFunctionPointer QOpenGLContext::getProcAddress(const char *procName)
//      const
extern "C" Q_DECL_EXPORT
void *ritual_ZNK14QOpenGLContext14getProcAddressEPKc(
    const QOpenGLContext *self,
    const char *procName) {
  return reinterpret_cast<void *>(self->getProcAddress(procName));
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

//  QPlatformOpenGLContext *QOpenGLContext::handle() const
extern "C" Q_DECL_EXPORT
QPlatformOpenGLContext *ritual_ZNK14QOpenGLContext6handleEv(
    const QOpenGLContext *self) {
  return self->handle();
}

//  QPlatformOpenGLContext *QOpenGLContext::shareHandle() const
extern "C" Q_DECL_EXPORT
QPlatformOpenGLContext *ritual_ZNK14QOpenGLContext11shareHandleEv(
    const QOpenGLContext *self) {
  return self->shareHandle();
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

//  QSet<QByteArray> QOpenGLContext::extensions() const
extern "C" Q_DECL_EXPORT
QSet<QByteArray> *ritual_ZNK14QOpenGLContext10extensionsEv(
    const QOpenGLContext *self) {
  return new QSet<QByteArray>(self->extensions());
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

//  void *QOpenGLContext::resolveInterface(const char *name, int revision)
//      const
extern "C" Q_DECL_EXPORT
void *ritual_ZNK14QOpenGLContext16resolveInterfaceEPKci(
    const QOpenGLContext *self,
    const char *name,
    int revision) {
  return self->resolveInterface(name, revision);
}

//  void QOpenGLContext::aboutToBeDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpenGLContext18aboutToBeDestroyedEv(QOpenGLContext *self) {
  self->aboutToBeDestroyed();
}

//  QOpenGLTextureHelper *QOpenGLContext::textureFunctions() const
extern "C" Q_DECL_EXPORT
QOpenGLTextureHelper *ritual_ZNK14QOpenGLContext16textureFunctionsEv(
    const QOpenGLContext *self) {
  return self->textureFunctions();
}

//  void QOpenGLContext::setTextureFunctions(QOpenGLTextureHelper
//      *textureFuncs, std::function<void ()> destroyCallback)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpenGLContext19setTextureFunctionsEP20QOpenGLTextureHelperSt8functionIFvvEE(
    QOpenGLContext *self,
    QOpenGLTextureHelper *textureFuncs,
    const std::function<void ()> *destroyCallback) {
  self->setTextureFunctions(textureFuncs, *destroyCallback);
}

//  void QOpenGLContext::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QOpenGLContext7destroyEv(QOpenGLContext *self) {
  self->destroy();
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

//  QList<QOpenGLContext *>::QList()
extern "C" Q_DECL_EXPORT
QList<QOpenGLContext *> *ritual_list_make_QOpenGLContext_ptr() {
  return new QList<QOpenGLContext *>();
}

//  void QList<QOpenGLContext *>::append(const QOpenGLContext * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QOpenGLContext_ptr(
    QList<QOpenGLContext *> *self,
    QOpenGLContext *element) {
  self->append(element);
}

//  qsizetype QList<QOpenGLContext *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QOpenGLContext_ptr(
    const QList<QOpenGLContext *> *self) {
  return self->size();
}

//  const QOpenGLContext * &QList<QOpenGLContext *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QOpenGLContext *ritual_list_at_QOpenGLContext_ptr(
    const QList<QOpenGLContext *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QOpenGLContext *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QOpenGLContext_ptr(QList<QOpenGLContext *> *self) {
  delete self;
}

//  a QSet<QByteArray> a ritual of QOpenGLContext gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QOpenGLContext__QSet_QByteArray(QSet<QByteArray> *self) {
  delete self;
}

#if defined(Q_OS_MACOS)
//  QNativeInterface::QCocoaGLContext
//      *QOpenGLContext::nativeInterface<QNativeInterface::QCocoaGLContext>()
//      const
extern "C" Q_DECL_EXPORT
QNativeInterface::QCocoaGLContext *ritual_ZNK14QOpenGLContext15nativeInterfaceIN16QNativeInterface15QCocoaGLContextENS1_7Private15NativeInterfaceIS2_EES_Lb1EEEPT_v(
    const QOpenGLContext *self) {
  return self->nativeInterface<QNativeInterface::QCocoaGLContext>();
}
#endif  // defined(Q_OS_MACOS)

#if defined(Q_OS_WIN)
//  QNativeInterface::QWGLContext
//      *QOpenGLContext::nativeInterface<QNativeInterface::QWGLContext>()
//      const
extern "C" Q_DECL_EXPORT
QNativeInterface::QWGLContext *ritual_ZNK14QOpenGLContext15nativeInterfaceIN16QNativeInterface11QWGLContextENS1_7Private15NativeInterfaceIS2_EES_Lb1EEEPT_v(
    const QOpenGLContext *self) {
  return self->nativeInterface<QNativeInterface::QWGLContext>();
}
#endif  // defined(Q_OS_WIN)

#if QT_CONFIG(xcb_glx_plugin)
//  QNativeInterface::QGLXContext
//      *QOpenGLContext::nativeInterface<QNativeInterface::QGLXContext>()
//      const
extern "C" Q_DECL_EXPORT
QNativeInterface::QGLXContext *ritual_ZNK14QOpenGLContext15nativeInterfaceIN16QNativeInterface11QGLXContextENS1_7Private15NativeInterfaceIS2_EES_Lb1EEEPT_v(
    const QOpenGLContext *self) {
  return self->nativeInterface<QNativeInterface::QGLXContext>();
}
#endif  // QT_CONFIG(xcb_glx_plugin)

#if QT_CONFIG(egl)
//  QNativeInterface::QEGLContext
//      *QOpenGLContext::nativeInterface<QNativeInterface::QEGLContext>()
//      const
extern "C" Q_DECL_EXPORT
QNativeInterface::QEGLContext *ritual_ZNK14QOpenGLContext15nativeInterfaceIN16QNativeInterface11QEGLContextENS1_7Private15NativeInterfaceIS2_EES_Lb1EEEPT_v(
    const QOpenGLContext *self) {
  return self->nativeInterface<QNativeInterface::QEGLContext>();
}
#endif  // QT_CONFIG(egl)

#endif  // !defined(QT_NO_OPENGL)
