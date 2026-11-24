//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformvulkaninstance.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(vulkan)
#if QT_CONFIG(vulkan) || defined(Q_QDOC)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformvulkaninstance.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qversionnumber.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QPlatformVulkanInstance that Python can take functions over in. Every QPlatformVulkanInstance
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(vulkan) || defined(Q_QDOC)
typedef const QVersionNumber * (*CuteQPlatformVulkanInstanceCall0)(const void *, int *);
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)
#if QT_CONFIG(vulkan) || defined(Q_QDOC)
typedef void (*CuteQPlatformVulkanInstanceCall1)(const void *, int *);
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)
#if QT_CONFIG(vulkan) || defined(Q_QDOC)
typedef bool (*CuteQPlatformVulkanInstanceCall2)(const void *, int *);
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)
#if QT_CONFIG(vulkan) || defined(Q_QDOC)
typedef void (*CuteQPlatformVulkanInstanceCall3)(const void *, QWindow *, int *);
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)
#if QT_CONFIG(vulkan) || defined(Q_QDOC)
typedef void (*CuteQPlatformVulkanInstanceCall4)(const void *, QWindow *, int *);
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)
#if QT_CONFIG(vulkan) || defined(Q_QDOC)
typedef void (*CuteQPlatformVulkanInstanceCall5)(const void *, QWindow *, int *);
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)
#if QT_CONFIG(vulkan) || defined(Q_QDOC)
typedef void (*CuteQPlatformVulkanInstanceCall6)(const void *, QWindow *, int *);
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)
class CuteQPlatformVulkanInstance : public QPlatformVulkanInstance {
public:
  using QPlatformVulkanInstance::QPlatformVulkanInstance;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(vulkan) || defined(Q_QDOC)
    if (!std::strcmp(key, "_ZNK23QPlatformVulkanInstance19supportedApiVersionEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)
#if QT_CONFIG(vulkan) || defined(Q_QDOC)
    if (!std::strcmp(key, "_ZN23QPlatformVulkanInstance21createOrAdoptInstanceEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)
#if QT_CONFIG(vulkan) || defined(Q_QDOC)
    if (!std::strcmp(key, "_ZNK23QPlatformVulkanInstance7isValidEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)
#if QT_CONFIG(vulkan) || defined(Q_QDOC)
    if (!std::strcmp(key, "_ZN23QPlatformVulkanInstance22presentAboutToBeQueuedEP7QWindow")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)
#if QT_CONFIG(vulkan) || defined(Q_QDOC)
    if (!std::strcmp(key, "_ZN23QPlatformVulkanInstance13presentQueuedEP7QWindow")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)
#if QT_CONFIG(vulkan) || defined(Q_QDOC)
    if (!std::strcmp(key, "_ZN23QPlatformVulkanInstance10beginFrameEP7QWindow")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)
#if QT_CONFIG(vulkan) || defined(Q_QDOC)
    if (!std::strcmp(key, "_ZN23QPlatformVulkanInstance8endFrameEP7QWindow")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)
    return false;
  }

#if QT_CONFIG(vulkan) || defined(Q_QDOC)
  //  QVersionNumber QPlatformVulkanInstance::supportedApiVersion() const
  QVersionNumber supportedApiVersion() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlatformVulkanInstanceCall0 call = reinterpret_cast<CuteQPlatformVulkanInstanceCall0>(taken[0]);
      const QVersionNumber * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)

#if QT_CONFIG(vulkan) || defined(Q_QDOC)
  //  void QPlatformVulkanInstance::createOrAdoptInstance()
  void createOrAdoptInstance() override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlatformVulkanInstanceCall1 call = reinterpret_cast<CuteQPlatformVulkanInstanceCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)

#if QT_CONFIG(vulkan) || defined(Q_QDOC)
  //  bool QPlatformVulkanInstance::isValid() const
  bool isValid() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQPlatformVulkanInstanceCall2 call = reinterpret_cast<CuteQPlatformVulkanInstanceCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)

#if QT_CONFIG(vulkan) || defined(Q_QDOC)
  //  void QPlatformVulkanInstance::presentAboutToBeQueued(QWindow *window)
  void presentAboutToBeQueued(QWindow *window) override {
    if (taken[3]) {
      int handled = 0;
      CuteQPlatformVulkanInstanceCall3 call = reinterpret_cast<CuteQPlatformVulkanInstanceCall3>(taken[3]);
      call(this, window, &handled);
      if (handled) return;
    }
    QPlatformVulkanInstance::presentAboutToBeQueued(window);
  }
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)

#if QT_CONFIG(vulkan) || defined(Q_QDOC)
  //  void QPlatformVulkanInstance::presentQueued(QWindow *window)
  void presentQueued(QWindow *window) override {
    if (taken[4]) {
      int handled = 0;
      CuteQPlatformVulkanInstanceCall4 call = reinterpret_cast<CuteQPlatformVulkanInstanceCall4>(taken[4]);
      call(this, window, &handled);
      if (handled) return;
    }
    QPlatformVulkanInstance::presentQueued(window);
  }
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)

#if QT_CONFIG(vulkan) || defined(Q_QDOC)
  //  void QPlatformVulkanInstance::beginFrame(QWindow *window)
  void beginFrame(QWindow *window) override {
    if (taken[5]) {
      int handled = 0;
      CuteQPlatformVulkanInstanceCall5 call = reinterpret_cast<CuteQPlatformVulkanInstanceCall5>(taken[5]);
      call(this, window, &handled);
      if (handled) return;
    }
    QPlatformVulkanInstance::beginFrame(window);
  }
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)

#if QT_CONFIG(vulkan) || defined(Q_QDOC)
  //  void QPlatformVulkanInstance::endFrame(QWindow *window)
  void endFrame(QWindow *window) override {
    if (taken[6]) {
      int handled = 0;
      CuteQPlatformVulkanInstanceCall6 call = reinterpret_cast<CuteQPlatformVulkanInstanceCall6>(taken[6]);
      call(this, window, &handled);
      if (handled) return;
    }
    QPlatformVulkanInstance::endFrame(window);
  }
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)
};

//  QPlatformVulkanInstance::~QPlatformVulkanInstance()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPlatformVulkanInstanceD1Ev(QPlatformVulkanInstance *self) {
  delete self;
}

//  QVersionNumber QPlatformVulkanInstance::supportedApiVersion() const
extern "C" Q_DECL_EXPORT
QVersionNumber *ritual_ZNK23QPlatformVulkanInstance19supportedApiVersionEv(
    const QPlatformVulkanInstance *self) {
  return new QVersionNumber(self->supportedApiVersion());
}

//  void QPlatformVulkanInstance::createOrAdoptInstance()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPlatformVulkanInstance21createOrAdoptInstanceEv(
    QPlatformVulkanInstance *self) {
  self->createOrAdoptInstance();
}

//  bool QPlatformVulkanInstance::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QPlatformVulkanInstance7isValidEv(
    const QPlatformVulkanInstance *self) {
  return self->isValid();
}

//  QByteArrayList QPlatformVulkanInstance::enabledLayers() const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK23QPlatformVulkanInstance13enabledLayersEv(
    const QPlatformVulkanInstance *self) {
  return new QList<QByteArray>(self->enabledLayers());
}

//  QByteArrayList QPlatformVulkanInstance::enabledExtensions() const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK23QPlatformVulkanInstance17enabledExtensionsEv(
    const QPlatformVulkanInstance *self) {
  return new QList<QByteArray>(self->enabledExtensions());
}

//  void QPlatformVulkanInstance::presentAboutToBeQueued(QWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPlatformVulkanInstance22presentAboutToBeQueuedEP7QWindow(
    QPlatformVulkanInstance *self,
    QWindow *window) {
  self->presentAboutToBeQueued(window);
}

//  void QPlatformVulkanInstance::presentQueued(QWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPlatformVulkanInstance13presentQueuedEP7QWindow(
    QPlatformVulkanInstance *self,
    QWindow *window) {
  self->presentQueued(window);
}

//  void QPlatformVulkanInstance::beginFrame(QWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPlatformVulkanInstance10beginFrameEP7QWindow(
    QPlatformVulkanInstance *self,
    QWindow *window) {
  self->beginFrame(window);
}

//  void QPlatformVulkanInstance::endFrame(QWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QPlatformVulkanInstance8endFrameEP7QWindow(
    QPlatformVulkanInstance *self,
    QWindow *window) {
  self->endFrame(window);
}

//  a Python function taken by a CuteQPlatformVulkanInstance, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlatformVulkanInstance(
    QPlatformVulkanInstance *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlatformVulkanInstance *>(self)->take(key, call);
}

//  void QPlatformVulkanInstance::presentAboutToBeQueued(QWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QPlatformVulkanInstance22presentAboutToBeQueuedEP7QWindow(
    QPlatformVulkanInstance *self,
    QWindow *window) {
  self->QPlatformVulkanInstance::presentAboutToBeQueued(window);
}

//  void QPlatformVulkanInstance::presentQueued(QWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QPlatformVulkanInstance13presentQueuedEP7QWindow(
    QPlatformVulkanInstance *self,
    QWindow *window) {
  self->QPlatformVulkanInstance::presentQueued(window);
}

//  void QPlatformVulkanInstance::beginFrame(QWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QPlatformVulkanInstance10beginFrameEP7QWindow(
    QPlatformVulkanInstance *self,
    QWindow *window) {
  self->QPlatformVulkanInstance::beginFrame(window);
}

//  void QPlatformVulkanInstance::endFrame(QWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN23QPlatformVulkanInstance8endFrameEP7QWindow(
    QPlatformVulkanInstance *self,
    QWindow *window) {
  self->QPlatformVulkanInstance::endFrame(window);
}

#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)
#endif  // QT_CONFIG(vulkan)
