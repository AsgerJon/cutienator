//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qsgrendererinterface.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/QtQuick>
#include <QtQuick/qsgrendererinterface.h>
#include <cstring>

//  A QSGRendererInterface that Python can take functions over in. Every QSGRendererInterface
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSGRendererInterfaceCall0)(const void *, int *);
typedef void * (*CuteQSGRendererInterfaceCall1)(const void *, QQuickWindow *, int, int *);
typedef int (*CuteQSGRendererInterfaceCall2)(const void *, int *);
typedef int (*CuteQSGRendererInterfaceCall3)(const void *, int *);
typedef int (*CuteQSGRendererInterfaceCall4)(const void *, int *);
class CuteQSGRendererInterface : public QSGRendererInterface {
public:
  using QSGRendererInterface::QSGRendererInterface;
  void *taken[5] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK20QSGRendererInterface11graphicsApiEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QSGRendererInterface11getResourceEP12QQuickWindowNS_8ResourceE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QSGRendererInterface10shaderTypeEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QSGRendererInterface21shaderCompilationTypeEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QSGRendererInterface16shaderSourceTypeEv")) {
      taken[4] = call;
      return true;
    }
    return false;
  }

  //  GraphicsApi QSGRendererInterface::graphicsApi() const
  QSGRendererInterface::GraphicsApi graphicsApi() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGRendererInterfaceCall0 call = reinterpret_cast<CuteQSGRendererInterfaceCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSGRendererInterface::GraphicsApi>(given);
    }
    return {};
  }

  //  void *QSGRendererInterface::getResource(QQuickWindow *window,
  //      Resource resource) const
  void *getResource(
      QQuickWindow *window,
      QSGRendererInterface::Resource resource) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGRendererInterfaceCall1 call = reinterpret_cast<CuteQSGRendererInterfaceCall1>(taken[1]);
      void * given = call(this, window, static_cast<int>(resource), &handled);
      if (handled) return static_cast<void *>(given);
    }
    return QSGRendererInterface::getResource(window, resource);
  }

  //  ShaderType QSGRendererInterface::shaderType() const
  QSGRendererInterface::ShaderType shaderType() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGRendererInterfaceCall2 call = reinterpret_cast<CuteQSGRendererInterfaceCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSGRendererInterface::ShaderType>(given);
    }
    return {};
  }

  //  ShaderCompilationTypes QSGRendererInterface::shaderCompilationType()
  //      const
  QSGRendererInterface::ShaderCompilationTypes shaderCompilationType() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGRendererInterfaceCall3 call = reinterpret_cast<CuteQSGRendererInterfaceCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return QFlags<QSGRendererInterface::ShaderCompilationType>::fromInt(given);
    }
    return {};
  }

  //  ShaderSourceTypes QSGRendererInterface::shaderSourceType() const
  QSGRendererInterface::ShaderSourceTypes shaderSourceType() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGRendererInterfaceCall4 call = reinterpret_cast<CuteQSGRendererInterfaceCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return QFlags<QSGRendererInterface::ShaderSourceType>::fromInt(given);
    }
    return {};
  }
};

//  QSGRendererInterface::~QSGRendererInterface()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QSGRendererInterfaceD1Ev(QSGRendererInterface *self) {
  delete self;
}

//  GraphicsApi QSGRendererInterface::graphicsApi() const
extern "C" Q_DECL_EXPORT
QSGRendererInterface::GraphicsApi ritual_ZNK20QSGRendererInterface11graphicsApiEv(
    const QSGRendererInterface *self) {
  return self->graphicsApi();
}

//  void *QSGRendererInterface::getResource(QQuickWindow *window, Resource
//      resource) const
extern "C" Q_DECL_EXPORT
void *ritual_ZNK20QSGRendererInterface11getResourceEP12QQuickWindowNS_8ResourceE(
    const QSGRendererInterface *self,
    QQuickWindow *window,
    QSGRendererInterface::Resource resource) {
  return self->getResource(window, resource);
}

//  void *QSGRendererInterface::getResource(QQuickWindow *window, const char
//      *resource) const
extern "C" Q_DECL_EXPORT
void *ritual_ZNK20QSGRendererInterface11getResourceEP12QQuickWindowPKc(
    const QSGRendererInterface *self,
    QQuickWindow *window,
    const char *resource) {
  return self->getResource(window, resource);
}

//  ShaderType QSGRendererInterface::shaderType() const
extern "C" Q_DECL_EXPORT
QSGRendererInterface::ShaderType ritual_ZNK20QSGRendererInterface10shaderTypeEv(
    const QSGRendererInterface *self) {
  return self->shaderType();
}

//  ShaderCompilationTypes QSGRendererInterface::shaderCompilationType()
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QSGRendererInterface21shaderCompilationTypeEv(
    const QSGRendererInterface *self) {
  return static_cast<int>(self->shaderCompilationType().toInt());
}

//  ShaderSourceTypes QSGRendererInterface::shaderSourceType() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QSGRendererInterface16shaderSourceTypeEv(
    const QSGRendererInterface *self) {
  return static_cast<int>(self->shaderSourceType().toInt());
}

//  bool QSGRendererInterface::isApiRhiBased(GraphicsApi api)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QSGRendererInterface13isApiRhiBasedENS_11GraphicsApiE(
    QSGRendererInterface::GraphicsApi api) {
  return QSGRendererInterface::isApiRhiBased(api);
}

//  a Python function taken by a CuteQSGRendererInterface, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGRendererInterface(
    QSGRendererInterface *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGRendererInterface *>(self)->take(key, call);
}

//  void *QSGRendererInterface::getResource(QQuickWindow *window, Resource
//      resource) const
extern "C" Q_DECL_EXPORT
void *ritual_own_ZNK20QSGRendererInterface11getResourceEP12QQuickWindowNS_8ResourceE(
    const QSGRendererInterface *self,
    QQuickWindow *window,
    QSGRendererInterface::Resource resource) {
  return self->QSGRendererInterface::getResource(window, resource);
}
