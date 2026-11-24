//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qbasicvulkanplatforminstance_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(vulkan)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qbasicvulkanplatforminstance_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qversionnumber.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QBasicPlatformVulkanInstance that Python can take functions over in. Every QBasicPlatformVulkanInstance
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(vulkan) || defined(Q_QDOC)
typedef const QVersionNumber * (*CuteQBasicPlatformVulkanInstanceCall0)(const void *, int *);
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)
#if QT_CONFIG(vulkan) || defined(Q_QDOC)
typedef bool (*CuteQBasicPlatformVulkanInstanceCall1)(const void *, int *);
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)
#if QT_CONFIG(vulkan) || defined(Q_QDOC)
typedef void (*CuteQBasicPlatformVulkanInstanceCall2)(const void *, int *);
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)
#if QT_CONFIG(vulkan) || defined(Q_QDOC)
typedef void (*CuteQBasicPlatformVulkanInstanceCall3)(const void *, QWindow *, int *);
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)
#if QT_CONFIG(vulkan) || defined(Q_QDOC)
typedef void (*CuteQBasicPlatformVulkanInstanceCall4)(const void *, QWindow *, int *);
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)
#if QT_CONFIG(vulkan) || defined(Q_QDOC)
typedef void (*CuteQBasicPlatformVulkanInstanceCall5)(const void *, QWindow *, int *);
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)
#if QT_CONFIG(vulkan) || defined(Q_QDOC)
typedef void (*CuteQBasicPlatformVulkanInstanceCall6)(const void *, QWindow *, int *);
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)
class CuteQBasicPlatformVulkanInstance : public QBasicPlatformVulkanInstance {
public:
  using QBasicPlatformVulkanInstance::QBasicPlatformVulkanInstance;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(vulkan) || defined(Q_QDOC)
    if (!std::strcmp(key, "_ZNK23QPlatformVulkanInstance19supportedApiVersionEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)
#if QT_CONFIG(vulkan) || defined(Q_QDOC)
    if (!std::strcmp(key, "_ZNK23QPlatformVulkanInstance7isValidEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)
#if QT_CONFIG(vulkan) || defined(Q_QDOC)
    if (!std::strcmp(key, "_ZN23QPlatformVulkanInstance21createOrAdoptInstanceEv")) {
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
  //  QVersionNumber QBasicPlatformVulkanInstance::supportedApiVersion()
  //      const
  QVersionNumber supportedApiVersion() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQBasicPlatformVulkanInstanceCall0 call = reinterpret_cast<CuteQBasicPlatformVulkanInstanceCall0>(taken[0]);
      const QVersionNumber * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QBasicPlatformVulkanInstance::supportedApiVersion();
  }
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)

#if QT_CONFIG(vulkan) || defined(Q_QDOC)
  //  bool QBasicPlatformVulkanInstance::isValid() const
  bool isValid() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQBasicPlatformVulkanInstanceCall1 call = reinterpret_cast<CuteQBasicPlatformVulkanInstanceCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QBasicPlatformVulkanInstance::isValid();
  }
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)

#if QT_CONFIG(vulkan) || defined(Q_QDOC)
  //  void QPlatformVulkanInstance::createOrAdoptInstance()
  void createOrAdoptInstance() override {
    if (taken[2]) {
      int handled = 0;
      CuteQBasicPlatformVulkanInstanceCall2 call = reinterpret_cast<CuteQBasicPlatformVulkanInstanceCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)

#if QT_CONFIG(vulkan) || defined(Q_QDOC)
  //  void QPlatformVulkanInstance::presentAboutToBeQueued(QWindow *window)
  void presentAboutToBeQueued(QWindow *window) override {
    if (taken[3]) {
      int handled = 0;
      CuteQBasicPlatformVulkanInstanceCall3 call = reinterpret_cast<CuteQBasicPlatformVulkanInstanceCall3>(taken[3]);
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
      CuteQBasicPlatformVulkanInstanceCall4 call = reinterpret_cast<CuteQBasicPlatformVulkanInstanceCall4>(taken[4]);
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
      CuteQBasicPlatformVulkanInstanceCall5 call = reinterpret_cast<CuteQBasicPlatformVulkanInstanceCall5>(taken[5]);
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
      CuteQBasicPlatformVulkanInstanceCall6 call = reinterpret_cast<CuteQBasicPlatformVulkanInstanceCall6>(taken[6]);
      call(this, window, &handled);
      if (handled) return;
    }
    QPlatformVulkanInstance::endFrame(window);
  }
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)
};

//  QBasicPlatformVulkanInstance::~QBasicPlatformVulkanInstance()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QBasicPlatformVulkanInstanceD1Ev(
    QBasicPlatformVulkanInstance *self) {
  delete self;
}

//  QVersionNumber QBasicPlatformVulkanInstance::supportedApiVersion() const
extern "C" Q_DECL_EXPORT
QVersionNumber *ritual_ZNK28QBasicPlatformVulkanInstance19supportedApiVersionEv(
    const QBasicPlatformVulkanInstance *self) {
  return new QVersionNumber(self->supportedApiVersion());
}

//  bool QBasicPlatformVulkanInstance::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QBasicPlatformVulkanInstance7isValidEv(
    const QBasicPlatformVulkanInstance *self) {
  return self->isValid();
}

//  QByteArrayList QBasicPlatformVulkanInstance::enabledLayers() const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK28QBasicPlatformVulkanInstance13enabledLayersEv(
    const QBasicPlatformVulkanInstance *self) {
  return new QList<QByteArray>(self->enabledLayers());
}

//  QByteArrayList QBasicPlatformVulkanInstance::enabledExtensions() const
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZNK28QBasicPlatformVulkanInstance17enabledExtensionsEv(
    const QBasicPlatformVulkanInstance *self) {
  return new QList<QByteArray>(self->enabledExtensions());
}

//  void QBasicPlatformVulkanInstance::loadVulkanLibrary(const QString
//      &defaultLibraryName, int defaultLibraryVersion)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QBasicPlatformVulkanInstance17loadVulkanLibraryERK7QStringi(
    QBasicPlatformVulkanInstance *self,
    const QString *defaultLibraryName,
    int defaultLibraryVersion) {
  self->loadVulkanLibrary(*defaultLibraryName, defaultLibraryVersion);
}

//  void QBasicPlatformVulkanInstance::init(QLibrary *lib)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QBasicPlatformVulkanInstance4initEP8QLibrary(
    QBasicPlatformVulkanInstance *self,
    QLibrary *lib) {
  self->init(lib);
}

//  void QBasicPlatformVulkanInstance::initInstance(QVulkanInstance
//      *instance, const QByteArrayList &extraExts)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QBasicPlatformVulkanInstance12initInstanceEP15QVulkanInstanceRK5QListI10QByteArrayE(
    QBasicPlatformVulkanInstance *self,
    QVulkanInstance *instance,
    const QList<QByteArray> *extraExts) {
  self->initInstance(instance, *extraExts);
}

//  void QBasicPlatformVulkanInstance::setupDebugOutput()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QBasicPlatformVulkanInstance16setupDebugOutputEv(
    QBasicPlatformVulkanInstance *self) {
  self->setupDebugOutput();
}

//  a Python function taken by a CuteQBasicPlatformVulkanInstance, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QBasicPlatformVulkanInstance(
    QBasicPlatformVulkanInstance *self,
    const char *key,
    void *call) {
  return static_cast<CuteQBasicPlatformVulkanInstance *>(self)->take(key, call);
}

//  QVersionNumber QBasicPlatformVulkanInstance::supportedApiVersion() const
extern "C" Q_DECL_EXPORT
QVersionNumber *ritual_own_ZNK28QBasicPlatformVulkanInstance19supportedApiVersionEv(
    const QBasicPlatformVulkanInstance *self) {
  return new QVersionNumber(
      self->QBasicPlatformVulkanInstance::supportedApiVersion());
}

//  bool QBasicPlatformVulkanInstance::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK28QBasicPlatformVulkanInstance7isValidEv(
    const QBasicPlatformVulkanInstance *self) {
  return self->QBasicPlatformVulkanInstance::isValid();
}

#endif  // QT_CONFIG(vulkan)
