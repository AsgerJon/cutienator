//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformintegration.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformintegration.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#include <QtGui/qicon.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QPlatformIntegration may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQPlatformIntegration : QPlatformIntegration {
  using QPlatformIntegration::queryKeyboardModifiers;
};

//  A QPlatformIntegration that Python can take functions over in. Every QPlatformIntegration
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQPlatformIntegrationCall0)(const void *, int, int *);
typedef void * (*CuteQPlatformIntegrationCall1)(const void *, int, int *);
typedef void * (*CuteQPlatformIntegrationCall2)(const void *, QWindow *, int *);
typedef void * (*CuteQPlatformIntegrationCall3)(const void *, QWindow *, WId, int *);
typedef void * (*CuteQPlatformIntegrationCall4)(const void *, QWindow *, int *);
#if !defined(QT_NO_OPENGL)
typedef void * (*CuteQPlatformIntegrationCall5)(const void *, QOpenGLContext *, int *);
#endif  // !defined(QT_NO_OPENGL)
typedef void * (*CuteQPlatformIntegrationCall6)(const void *, QPaintDevice *, int *);
typedef void * (*CuteQPlatformIntegrationCall7)(const void *, int *);
typedef void (*CuteQPlatformIntegrationCall8)(const void *, int *);
typedef void (*CuteQPlatformIntegrationCall9)(const void *, int *);
typedef void * (*CuteQPlatformIntegrationCall10)(const void *, int *);
#if !defined(QT_NO_CLIPBOARD)
typedef void * (*CuteQPlatformIntegrationCall11)(const void *, int *);
#endif  // !defined(QT_NO_CLIPBOARD)
#if QT_CONFIG(draganddrop)
typedef void * (*CuteQPlatformIntegrationCall12)(const void *, int *);
#endif  // QT_CONFIG(draganddrop)
typedef void * (*CuteQPlatformIntegrationCall13)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef void * (*CuteQPlatformIntegrationCall14)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef void * (*CuteQPlatformIntegrationCall15)(const void *, int *);
typedef void * (*CuteQPlatformIntegrationCall16)(const void *, int *);
typedef const QVariant * (*CuteQPlatformIntegrationCall17)(const void *, int, int *);
typedef int (*CuteQPlatformIntegrationCall18)(const void *, int, int *);
typedef int (*CuteQPlatformIntegrationCall19)(const void *, int *);
typedef void * (*CuteQPlatformIntegrationCall20)(const void *, int *);
typedef void * (*CuteQPlatformIntegrationCall21)(const void *, const QString *, int *);
typedef void * (*CuteQPlatformIntegrationCall22)(const void *, QOffscreenSurface *, int *);
#if !defined(QT_NO_SESSIONMANAGER)
typedef void * (*CuteQPlatformIntegrationCall23)(const void *, const QString *, const QString *, int *);
#endif  // !defined(QT_NO_SESSIONMANAGER)
typedef void (*CuteQPlatformIntegrationCall24)(const void *, int *);
#if !defined(QT_NO_OPENGL)
typedef int (*CuteQPlatformIntegrationCall25)(const void *, int *);
#endif  // !defined(QT_NO_OPENGL)
typedef void (*CuteQPlatformIntegrationCall26)(const void *, const QIcon *, int *);
typedef void (*CuteQPlatformIntegrationCall27)(const void *, qint64, int *);
typedef void (*CuteQPlatformIntegrationCall28)(const void *, int *);
typedef void (*CuteQPlatformIntegrationCall29)(const void *, int *);
#if QT_CONFIG(vulkan) || defined(Q_QDOC)
typedef void * (*CuteQPlatformIntegrationCall30)(const void *, QVulkanInstance *, int *);
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)
class CuteQPlatformIntegration : public QPlatformIntegration {
public:
  using QPlatformIntegration::QPlatformIntegration;
  void *taken[31] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK20QPlatformIntegration13hasCapabilityENS_10CapabilityE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QPlatformIntegration20createPlatformPixmapEN15QPlatformPixmap9PixelTypeE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QPlatformIntegration20createPlatformWindowEP7QWindow")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QPlatformIntegration19createForeignWindowEP7QWindowy")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QPlatformIntegration26createPlatformBackingStoreEP7QWindow")) {
      taken[4] = call;
      return true;
    }
#if !defined(QT_NO_OPENGL)
    if (!std::strcmp(key, "_ZNK20QPlatformIntegration27createPlatformOpenGLContextEP14QOpenGLContext")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_OPENGL)
    if (!std::strcmp(key, "_ZNK20QPlatformIntegration22createImagePaintEngineEP12QPaintDevice")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QPlatformIntegration21createEventDispatcherEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QPlatformIntegration10initializeEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QPlatformIntegration7destroyEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QPlatformIntegration12fontDatabaseEv")) {
      taken[10] = call;
      return true;
    }
#if !defined(QT_NO_CLIPBOARD)
    if (!std::strcmp(key, "_ZNK20QPlatformIntegration9clipboardEv")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_CLIPBOARD)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZNK20QPlatformIntegration4dragEv")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZNK20QPlatformIntegration12inputContextEv")) {
      taken[13] = call;
      return true;
    }
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QPlatformIntegration13accessibilityEv")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK20QPlatformIntegration15nativeInterfaceEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QPlatformIntegration8servicesEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QPlatformIntegration9styleHintENS_9StyleHintE")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QPlatformIntegration18defaultWindowStateE6QFlagsIN2Qt10WindowTypeEE")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QPlatformIntegration22queryKeyboardModifiersEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QPlatformIntegration9keyMapperEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QPlatformIntegration19createPlatformThemeERK7QString")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QPlatformIntegration30createPlatformOffscreenSurfaceEP17QOffscreenSurface")) {
      taken[22] = call;
      return true;
    }
#if !defined(QT_NO_SESSIONMANAGER)
    if (!std::strcmp(key, "_ZNK20QPlatformIntegration28createPlatformSessionManagerERK7QStringS2_")) {
      taken[23] = call;
      return true;
    }
#endif  // !defined(QT_NO_SESSIONMANAGER)
    if (!std::strcmp(key, "_ZN20QPlatformIntegration4syncEv")) {
      taken[24] = call;
      return true;
    }
#if !defined(QT_NO_OPENGL)
    if (!std::strcmp(key, "_ZN20QPlatformIntegration16openGLModuleTypeEv")) {
      taken[25] = call;
      return true;
    }
#endif  // !defined(QT_NO_OPENGL)
    if (!std::strcmp(key, "_ZNK20QPlatformIntegration18setApplicationIconERK5QIcon")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QPlatformIntegration19setApplicationBadgeEx")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QPlatformIntegration4beepEv")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QPlatformIntegration4quitEv")) {
      taken[29] = call;
      return true;
    }
#if QT_CONFIG(vulkan) || defined(Q_QDOC)
    if (!std::strcmp(key, "_ZNK20QPlatformIntegration28createPlatformVulkanInstanceEP15QVulkanInstance")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)
    return false;
  }

  //  bool QPlatformIntegration::hasCapability(Capability cap) const
  bool hasCapability(QPlatformIntegration::Capability cap) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlatformIntegrationCall0 call = reinterpret_cast<CuteQPlatformIntegrationCall0>(taken[0]);
      bool given = call(this, static_cast<int>(cap), &handled);
      if (handled) return given;
    }
    return QPlatformIntegration::hasCapability(cap);
  }

  //  QPlatformPixmap *QPlatformIntegration::createPlatformPixmap(QPlatform
  //      Pixmap::PixelType type) const
  QPlatformPixmap *createPlatformPixmap(
      QPlatformPixmap::PixelType type) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlatformIntegrationCall1 call = reinterpret_cast<CuteQPlatformIntegrationCall1>(taken[1]);
      void * given = call(this, static_cast<int>(type), &handled);
      if (handled) return static_cast<QPlatformPixmap *>(given);
    }
    return QPlatformIntegration::createPlatformPixmap(type);
  }

  //  QPlatformWindow *QPlatformIntegration::createPlatformWindow(QWindow
  //      *window) const
  QPlatformWindow *createPlatformWindow(QWindow *window) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQPlatformIntegrationCall2 call = reinterpret_cast<CuteQPlatformIntegrationCall2>(taken[2]);
      void * given = call(this, window, &handled);
      if (handled) return static_cast<QPlatformWindow *>(given);
    }
    return {};
  }

  //  QPlatformWindow *QPlatformIntegration::createForeignWindow(QWindow
  //      *a0, WId a1) const
  QPlatformWindow *createForeignWindow(QWindow *a0, WId a1) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQPlatformIntegrationCall3 call = reinterpret_cast<CuteQPlatformIntegrationCall3>(taken[3]);
      void * given = call(this, a0, a1, &handled);
      if (handled) return static_cast<QPlatformWindow *>(given);
    }
    return QPlatformIntegration::createForeignWindow(a0, a1);
  }

  //  QPlatformBackingStore
  //      *QPlatformIntegration::createPlatformBackingStore(QWindow
  //      *window) const
  QPlatformBackingStore *createPlatformBackingStore(
      QWindow *window) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQPlatformIntegrationCall4 call = reinterpret_cast<CuteQPlatformIntegrationCall4>(taken[4]);
      void * given = call(this, window, &handled);
      if (handled) return static_cast<QPlatformBackingStore *>(given);
    }
    return {};
  }

#if !defined(QT_NO_OPENGL)
  //  QPlatformOpenGLContext
  //      *QPlatformIntegration::createPlatformOpenGLContext(QOpenGLContext
  //      *context) const
  QPlatformOpenGLContext *createPlatformOpenGLContext(
      QOpenGLContext *context) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQPlatformIntegrationCall5 call = reinterpret_cast<CuteQPlatformIntegrationCall5>(taken[5]);
      void * given = call(this, context, &handled);
      if (handled) return static_cast<QPlatformOpenGLContext *>(given);
    }
    return QPlatformIntegration::createPlatformOpenGLContext(context);
  }
#endif  // !defined(QT_NO_OPENGL)

  //  QPaintEngine
  //      *QPlatformIntegration::createImagePaintEngine(QPaintDevice
  //      *paintDevice) const
  QPaintEngine *createImagePaintEngine(
      QPaintDevice *paintDevice) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQPlatformIntegrationCall6 call = reinterpret_cast<CuteQPlatformIntegrationCall6>(taken[6]);
      void * given = call(this, paintDevice, &handled);
      if (handled) return static_cast<QPaintEngine *>(given);
    }
    return QPlatformIntegration::createImagePaintEngine(paintDevice);
  }

  //  QAbstractEventDispatcher
  //      *QPlatformIntegration::createEventDispatcher() const
  QAbstractEventDispatcher *createEventDispatcher() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQPlatformIntegrationCall7 call = reinterpret_cast<CuteQPlatformIntegrationCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAbstractEventDispatcher *>(given);
    }
    return {};
  }

  //  void QPlatformIntegration::initialize()
  void initialize() override {
    if (taken[8]) {
      int handled = 0;
      CuteQPlatformIntegrationCall8 call = reinterpret_cast<CuteQPlatformIntegrationCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QPlatformIntegration::initialize();
  }

  //  void QPlatformIntegration::destroy()
  void destroy() override {
    if (taken[9]) {
      int handled = 0;
      CuteQPlatformIntegrationCall9 call = reinterpret_cast<CuteQPlatformIntegrationCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QPlatformIntegration::destroy();
  }

  //  QPlatformFontDatabase *QPlatformIntegration::fontDatabase() const
  QPlatformFontDatabase *fontDatabase() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQPlatformIntegrationCall10 call = reinterpret_cast<CuteQPlatformIntegrationCall10>(taken[10]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformFontDatabase *>(given);
    }
    return QPlatformIntegration::fontDatabase();
  }

#if !defined(QT_NO_CLIPBOARD)
  //  QPlatformClipboard *QPlatformIntegration::clipboard() const
  QPlatformClipboard *clipboard() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQPlatformIntegrationCall11 call = reinterpret_cast<CuteQPlatformIntegrationCall11>(taken[11]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformClipboard *>(given);
    }
    return QPlatformIntegration::clipboard();
  }
#endif  // !defined(QT_NO_CLIPBOARD)

#if QT_CONFIG(draganddrop)
  //  QPlatformDrag *QPlatformIntegration::drag() const
  QPlatformDrag *drag() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQPlatformIntegrationCall12 call = reinterpret_cast<CuteQPlatformIntegrationCall12>(taken[12]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformDrag *>(given);
    }
    return QPlatformIntegration::drag();
  }
#endif  // QT_CONFIG(draganddrop)

  //  QPlatformInputContext *QPlatformIntegration::inputContext() const
  QPlatformInputContext *inputContext() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQPlatformIntegrationCall13 call = reinterpret_cast<CuteQPlatformIntegrationCall13>(taken[13]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformInputContext *>(given);
    }
    return QPlatformIntegration::inputContext();
  }

#if QT_CONFIG(accessibility)
  //  QPlatformAccessibility *QPlatformIntegration::accessibility() const
  QPlatformAccessibility *accessibility() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQPlatformIntegrationCall14 call = reinterpret_cast<CuteQPlatformIntegrationCall14>(taken[14]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformAccessibility *>(given);
    }
    return QPlatformIntegration::accessibility();
  }
#endif  // QT_CONFIG(accessibility)

  //  QPlatformNativeInterface *QPlatformIntegration::nativeInterface()
  //      const
  QPlatformNativeInterface *nativeInterface() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQPlatformIntegrationCall15 call = reinterpret_cast<CuteQPlatformIntegrationCall15>(taken[15]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformNativeInterface *>(given);
    }
    return QPlatformIntegration::nativeInterface();
  }

  //  QPlatformServices *QPlatformIntegration::services() const
  QPlatformServices *services() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQPlatformIntegrationCall16 call = reinterpret_cast<CuteQPlatformIntegrationCall16>(taken[16]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformServices *>(given);
    }
    return QPlatformIntegration::services();
  }

  //  QVariant QPlatformIntegration::styleHint(StyleHint hint) const
  QVariant styleHint(QPlatformIntegration::StyleHint hint) const override {
    if (taken[17]) {
      int handled = 0;
      CuteQPlatformIntegrationCall17 call = reinterpret_cast<CuteQPlatformIntegrationCall17>(taken[17]);
      const QVariant * given = call(this, static_cast<int>(hint), &handled);
      if (handled && given) return *given;
    }
    return QPlatformIntegration::styleHint(hint);
  }

  //  Qt::WindowState
  //      QPlatformIntegration::defaultWindowState(Qt::WindowFlags a0)
  //      const
  Qt::WindowState defaultWindowState(Qt::WindowFlags a0) const override {
    if (taken[18]) {
      int handled = 0;
      CuteQPlatformIntegrationCall18 call = reinterpret_cast<CuteQPlatformIntegrationCall18>(taken[18]);
      int given = call(this, static_cast<int>(a0.toInt()), &handled);
      if (handled) return static_cast<Qt::WindowState>(given);
    }
    return QPlatformIntegration::defaultWindowState(a0);
  }

  //  Qt::KeyboardModifiers QPlatformIntegration::queryKeyboardModifiers()
  //      const
  Qt::KeyboardModifiers queryKeyboardModifiers() const override {
    if (taken[19]) {
      int handled = 0;
      CuteQPlatformIntegrationCall19 call = reinterpret_cast<CuteQPlatformIntegrationCall19>(taken[19]);
      int given = call(this, &handled);
      if (handled) return QFlags<Qt::KeyboardModifier>::fromInt(given);
    }
    return QPlatformIntegration::queryKeyboardModifiers();
  }

  //  QPlatformKeyMapper *QPlatformIntegration::keyMapper() const
  QPlatformKeyMapper *keyMapper() const override {
    if (taken[20]) {
      int handled = 0;
      CuteQPlatformIntegrationCall20 call = reinterpret_cast<CuteQPlatformIntegrationCall20>(taken[20]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformKeyMapper *>(given);
    }
    return QPlatformIntegration::keyMapper();
  }

  //  QPlatformTheme *QPlatformIntegration::createPlatformTheme(const
  //      QString &name) const
  QPlatformTheme *createPlatformTheme(const QString &name) const override {
    if (taken[21]) {
      int handled = 0;
      CuteQPlatformIntegrationCall21 call = reinterpret_cast<CuteQPlatformIntegrationCall21>(taken[21]);
      void * given = call(this, &name, &handled);
      if (handled) return static_cast<QPlatformTheme *>(given);
    }
    return QPlatformIntegration::createPlatformTheme(name);
  }

  //  QPlatformOffscreenSurface *QPlatformIntegration::createPlatformOffscr
  //      eenSurface(QOffscreenSurface *surface) const
  QPlatformOffscreenSurface *createPlatformOffscreenSurface(
      QOffscreenSurface *surface) const override {
    if (taken[22]) {
      int handled = 0;
      CuteQPlatformIntegrationCall22 call = reinterpret_cast<CuteQPlatformIntegrationCall22>(taken[22]);
      void * given = call(this, surface, &handled);
      if (handled) return static_cast<QPlatformOffscreenSurface *>(given);
    }
    return QPlatformIntegration::createPlatformOffscreenSurface(surface);
  }

#if !defined(QT_NO_SESSIONMANAGER)
  //  QPlatformSessionManager
  //      *QPlatformIntegration::createPlatformSessionManager(const QString
  //      &id, const QString &key) const
  QPlatformSessionManager *createPlatformSessionManager(
      const QString &id,
      const QString &key) const override {
    if (taken[23]) {
      int handled = 0;
      CuteQPlatformIntegrationCall23 call = reinterpret_cast<CuteQPlatformIntegrationCall23>(taken[23]);
      void * given = call(this, &id, &key, &handled);
      if (handled) return static_cast<QPlatformSessionManager *>(given);
    }
    return QPlatformIntegration::createPlatformSessionManager(id, key);
  }
#endif  // !defined(QT_NO_SESSIONMANAGER)

  //  void QPlatformIntegration::sync()
  void sync() override {
    if (taken[24]) {
      int handled = 0;
      CuteQPlatformIntegrationCall24 call = reinterpret_cast<CuteQPlatformIntegrationCall24>(taken[24]);
      call(this, &handled);
      if (handled) return;
    }
    QPlatformIntegration::sync();
  }

#if !defined(QT_NO_OPENGL)
  //  QOpenGLContext::OpenGLModuleType
  //      QPlatformIntegration::openGLModuleType()
  QOpenGLContext::OpenGLModuleType openGLModuleType() override {
    if (taken[25]) {
      int handled = 0;
      CuteQPlatformIntegrationCall25 call = reinterpret_cast<CuteQPlatformIntegrationCall25>(taken[25]);
      int given = call(this, &handled);
      if (handled) return static_cast<QOpenGLContext::OpenGLModuleType>(given);
    }
    return QPlatformIntegration::openGLModuleType();
  }
#endif  // !defined(QT_NO_OPENGL)

  //  void QPlatformIntegration::setApplicationIcon(const QIcon &icon)
  //      const
  void setApplicationIcon(const QIcon &icon) const override {
    if (taken[26]) {
      int handled = 0;
      CuteQPlatformIntegrationCall26 call = reinterpret_cast<CuteQPlatformIntegrationCall26>(taken[26]);
      call(this, &icon, &handled);
      if (handled) return;
    }
    QPlatformIntegration::setApplicationIcon(icon);
  }

  //  void QPlatformIntegration::setApplicationBadge(qint64 number)
  void setApplicationBadge(qint64 number) override {
    if (taken[27]) {
      int handled = 0;
      CuteQPlatformIntegrationCall27 call = reinterpret_cast<CuteQPlatformIntegrationCall27>(taken[27]);
      call(this, number, &handled);
      if (handled) return;
    }
    QPlatformIntegration::setApplicationBadge(number);
  }

  //  void QPlatformIntegration::beep() const
  void beep() const override {
    if (taken[28]) {
      int handled = 0;
      CuteQPlatformIntegrationCall28 call = reinterpret_cast<CuteQPlatformIntegrationCall28>(taken[28]);
      call(this, &handled);
      if (handled) return;
    }
    QPlatformIntegration::beep();
  }

  //  void QPlatformIntegration::quit() const
  void quit() const override {
    if (taken[29]) {
      int handled = 0;
      CuteQPlatformIntegrationCall29 call = reinterpret_cast<CuteQPlatformIntegrationCall29>(taken[29]);
      call(this, &handled);
      if (handled) return;
    }
    QPlatformIntegration::quit();
  }

#if QT_CONFIG(vulkan) || defined(Q_QDOC)
  //  QPlatformVulkanInstance
  //      *QPlatformIntegration::createPlatformVulkanInstance(QVulkanInstan
  //      ce *instance) const
  QPlatformVulkanInstance *createPlatformVulkanInstance(
      QVulkanInstance *instance) const override {
    if (taken[30]) {
      int handled = 0;
      CuteQPlatformIntegrationCall30 call = reinterpret_cast<CuteQPlatformIntegrationCall30>(taken[30]);
      void * given = call(this, instance, &handled);
      if (handled) return static_cast<QPlatformVulkanInstance *>(given);
    }
    return QPlatformIntegration::createPlatformVulkanInstance(instance);
  }
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)
};

//  QPlatformIntegration::~QPlatformIntegration()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformIntegrationD1Ev(QPlatformIntegration *self) {
  delete self;
}

//  bool QPlatformIntegration::hasCapability(Capability cap) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QPlatformIntegration13hasCapabilityENS_10CapabilityE(
    const QPlatformIntegration *self,
    QPlatformIntegration::Capability cap) {
  return self->hasCapability(cap);
}

//  QPlatformPixmap
//      *QPlatformIntegration::createPlatformPixmap(QPlatformPixmap::PixelTyp
//      e type) const
extern "C" Q_DECL_EXPORT
QPlatformPixmap *ritual_ZNK20QPlatformIntegration20createPlatformPixmapEN15QPlatformPixmap9PixelTypeE(
    const QPlatformIntegration *self,
    QPlatformPixmap::PixelType type) {
  return self->createPlatformPixmap(type);
}

//  QPlatformWindow *QPlatformIntegration::createPlatformWindow(QWindow
//      *window) const
extern "C" Q_DECL_EXPORT
QPlatformWindow *ritual_ZNK20QPlatformIntegration20createPlatformWindowEP7QWindow(
    const QPlatformIntegration *self,
    QWindow *window) {
  return self->createPlatformWindow(window);
}

//  QPlatformWindow *QPlatformIntegration::createForeignWindow(QWindow *a0,
//      WId a1) const
extern "C" Q_DECL_EXPORT
QPlatformWindow *ritual_ZNK20QPlatformIntegration19createForeignWindowEP7QWindowy(
    const QPlatformIntegration *self,
    QWindow *a0,
    WId a1) {
  return self->createForeignWindow(a0, a1);
}

//  QPlatformBackingStore
//      *QPlatformIntegration::createPlatformBackingStore(QWindow *window)
//      const
extern "C" Q_DECL_EXPORT
QPlatformBackingStore *ritual_ZNK20QPlatformIntegration26createPlatformBackingStoreEP7QWindow(
    const QPlatformIntegration *self,
    QWindow *window) {
  return self->createPlatformBackingStore(window);
}

#if !defined(QT_NO_OPENGL)
//  QPlatformOpenGLContext
//      *QPlatformIntegration::createPlatformOpenGLContext(QOpenGLContext
//      *context) const
extern "C" Q_DECL_EXPORT
QPlatformOpenGLContext *ritual_ZNK20QPlatformIntegration27createPlatformOpenGLContextEP14QOpenGLContext(
    const QPlatformIntegration *self,
    QOpenGLContext *context) {
  return self->createPlatformOpenGLContext(context);
}
#endif  // !defined(QT_NO_OPENGL)

//  QPlatformSharedGraphicsCache
//      *QPlatformIntegration::createPlatformSharedGraphicsCache(const char
//      *cacheId) const
extern "C" Q_DECL_EXPORT
QPlatformSharedGraphicsCache *ritual_ZNK20QPlatformIntegration33createPlatformSharedGraphicsCacheEPKc(
    const QPlatformIntegration *self,
    const char *cacheId) {
  return self->createPlatformSharedGraphicsCache(cacheId);
}

//  QPaintEngine *QPlatformIntegration::createImagePaintEngine(QPaintDevice
//      *paintDevice) const
extern "C" Q_DECL_EXPORT
QPaintEngine *ritual_ZNK20QPlatformIntegration22createImagePaintEngineEP12QPaintDevice(
    const QPlatformIntegration *self,
    QPaintDevice *paintDevice) {
  return self->createImagePaintEngine(paintDevice);
}

//  QAbstractEventDispatcher *QPlatformIntegration::createEventDispatcher()
//      const
extern "C" Q_DECL_EXPORT
QAbstractEventDispatcher *ritual_ZNK20QPlatformIntegration21createEventDispatcherEv(
    const QPlatformIntegration *self) {
  return self->createEventDispatcher();
}

//  void QPlatformIntegration::initialize()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformIntegration10initializeEv(
    QPlatformIntegration *self) {
  self->initialize();
}

//  void QPlatformIntegration::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformIntegration7destroyEv(QPlatformIntegration *self) {
  self->destroy();
}

//  QPlatformFontDatabase *QPlatformIntegration::fontDatabase() const
extern "C" Q_DECL_EXPORT
QPlatformFontDatabase *ritual_ZNK20QPlatformIntegration12fontDatabaseEv(
    const QPlatformIntegration *self) {
  return self->fontDatabase();
}

#if !defined(QT_NO_CLIPBOARD)
//  QPlatformClipboard *QPlatformIntegration::clipboard() const
extern "C" Q_DECL_EXPORT
QPlatformClipboard *ritual_ZNK20QPlatformIntegration9clipboardEv(
    const QPlatformIntegration *self) {
  return self->clipboard();
}
#endif  // !defined(QT_NO_CLIPBOARD)

#if QT_CONFIG(draganddrop)
//  QPlatformDrag *QPlatformIntegration::drag() const
extern "C" Q_DECL_EXPORT
QPlatformDrag *ritual_ZNK20QPlatformIntegration4dragEv(
    const QPlatformIntegration *self) {
  return self->drag();
}
#endif  // QT_CONFIG(draganddrop)

//  QPlatformInputContext *QPlatformIntegration::inputContext() const
extern "C" Q_DECL_EXPORT
QPlatformInputContext *ritual_ZNK20QPlatformIntegration12inputContextEv(
    const QPlatformIntegration *self) {
  return self->inputContext();
}

#if QT_CONFIG(accessibility)
//  QPlatformAccessibility *QPlatformIntegration::accessibility() const
extern "C" Q_DECL_EXPORT
QPlatformAccessibility *ritual_ZNK20QPlatformIntegration13accessibilityEv(
    const QPlatformIntegration *self) {
  return self->accessibility();
}
#endif  // QT_CONFIG(accessibility)

//  QPlatformNativeInterface *QPlatformIntegration::nativeInterface() const
extern "C" Q_DECL_EXPORT
QPlatformNativeInterface *ritual_ZNK20QPlatformIntegration15nativeInterfaceEv(
    const QPlatformIntegration *self) {
  return self->nativeInterface();
}

//  QPlatformServices *QPlatformIntegration::services() const
extern "C" Q_DECL_EXPORT
QPlatformServices *ritual_ZNK20QPlatformIntegration8servicesEv(
    const QPlatformIntegration *self) {
  return self->services();
}

//  QVariant QPlatformIntegration::styleHint(StyleHint hint) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK20QPlatformIntegration9styleHintENS_9StyleHintE(
    const QPlatformIntegration *self,
    QPlatformIntegration::StyleHint hint) {
  return new QVariant(self->styleHint(hint));
}

//  Qt::WindowState QPlatformIntegration::defaultWindowState(Qt::WindowFlags
//      a0) const
extern "C" Q_DECL_EXPORT
Qt::WindowState ritual_ZNK20QPlatformIntegration18defaultWindowStateE6QFlagsIN2Qt10WindowTypeEE(
    const QPlatformIntegration *self,
    int a0) {
  return self->defaultWindowState(QFlags<Qt::WindowType>::fromInt(a0));
}

//  Qt::KeyboardModifiers QPlatformIntegration::queryKeyboardModifiers()
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QPlatformIntegration22queryKeyboardModifiersEv(
    const QPlatformIntegration *self) {
  return static_cast<int>(self->queryKeyboardModifiers().toInt());
}

//  QPlatformKeyMapper *QPlatformIntegration::keyMapper() const
extern "C" Q_DECL_EXPORT
QPlatformKeyMapper *ritual_ZNK20QPlatformIntegration9keyMapperEv(
    const QPlatformIntegration *self) {
  return self->keyMapper();
}

//  QStringList QPlatformIntegration::themeNames() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK20QPlatformIntegration10themeNamesEv(
    const QPlatformIntegration *self) {
  return new QList<QString>(self->themeNames());
}

//  QPlatformTheme *QPlatformIntegration::createPlatformTheme(const QString
//      &name) const
extern "C" Q_DECL_EXPORT
QPlatformTheme *ritual_ZNK20QPlatformIntegration19createPlatformThemeERK7QString(
    const QPlatformIntegration *self,
    const QString *name) {
  return self->createPlatformTheme(*name);
}

//  QPlatformOffscreenSurface
//      *QPlatformIntegration::createPlatformOffscreenSurface(QOffscreenSurfa
//      ce *surface) const
extern "C" Q_DECL_EXPORT
QPlatformOffscreenSurface *ritual_ZNK20QPlatformIntegration30createPlatformOffscreenSurfaceEP17QOffscreenSurface(
    const QPlatformIntegration *self,
    QOffscreenSurface *surface) {
  return self->createPlatformOffscreenSurface(surface);
}

#if !defined(QT_NO_SESSIONMANAGER)
//  QPlatformSessionManager
//      *QPlatformIntegration::createPlatformSessionManager(const QString
//      &id, const QString &key) const
extern "C" Q_DECL_EXPORT
QPlatformSessionManager *ritual_ZNK20QPlatformIntegration28createPlatformSessionManagerERK7QStringS2_(
    const QPlatformIntegration *self,
    const QString *id,
    const QString *key) {
  return self->createPlatformSessionManager(*id, *key);
}
#endif  // !defined(QT_NO_SESSIONMANAGER)

//  void QPlatformIntegration::sync()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformIntegration4syncEv(QPlatformIntegration *self) {
  self->sync();
}

#if !defined(QT_NO_OPENGL)
//  QOpenGLContext::OpenGLModuleType QPlatformIntegration::openGLModuleType()
extern "C" Q_DECL_EXPORT
QOpenGLContext::OpenGLModuleType ritual_ZN20QPlatformIntegration16openGLModuleTypeEv(
    QPlatformIntegration *self) {
  return self->openGLModuleType();
}
#endif  // !defined(QT_NO_OPENGL)

//  void QPlatformIntegration::setApplicationIcon(const QIcon &icon) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK20QPlatformIntegration18setApplicationIconERK5QIcon(
    const QPlatformIntegration *self,
    const QIcon *icon) {
  self->setApplicationIcon(*icon);
}

//  void QPlatformIntegration::setApplicationBadge(qint64 number)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QPlatformIntegration19setApplicationBadgeEx(
    QPlatformIntegration *self,
    qint64 number) {
  self->setApplicationBadge(number);
}

//  void QPlatformIntegration::beep() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK20QPlatformIntegration4beepEv(
    const QPlatformIntegration *self) {
  self->beep();
}

//  void QPlatformIntegration::quit() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK20QPlatformIntegration4quitEv(
    const QPlatformIntegration *self) {
  self->quit();
}

#if QT_CONFIG(vulkan) || defined(Q_QDOC)
//  QPlatformVulkanInstance
//      *QPlatformIntegration::createPlatformVulkanInstance(QVulkanInstance
//      *instance) const
extern "C" Q_DECL_EXPORT
QPlatformVulkanInstance *ritual_ZNK20QPlatformIntegration28createPlatformVulkanInstanceEP15QVulkanInstance(
    const QPlatformIntegration *self,
    QVulkanInstance *instance) {
  return self->createPlatformVulkanInstance(instance);
}
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)

//  a Python function taken by a CuteQPlatformIntegration, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlatformIntegration(
    QPlatformIntegration *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlatformIntegration *>(self)->take(key, call);
}

//  bool QPlatformIntegration::hasCapability(Capability cap) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK20QPlatformIntegration13hasCapabilityENS_10CapabilityE(
    const QPlatformIntegration *self,
    QPlatformIntegration::Capability cap) {
  return self->QPlatformIntegration::hasCapability(cap);
}

//  QPlatformPixmap
//      *QPlatformIntegration::createPlatformPixmap(QPlatformPixmap::PixelTyp
//      e type) const
extern "C" Q_DECL_EXPORT
QPlatformPixmap *ritual_own_ZNK20QPlatformIntegration20createPlatformPixmapEN15QPlatformPixmap9PixelTypeE(
    const QPlatformIntegration *self,
    QPlatformPixmap::PixelType type) {
  return self->QPlatformIntegration::createPlatformPixmap(type);
}

//  QPlatformWindow *QPlatformIntegration::createForeignWindow(QWindow *a0,
//      WId a1) const
extern "C" Q_DECL_EXPORT
QPlatformWindow *ritual_own_ZNK20QPlatformIntegration19createForeignWindowEP7QWindowy(
    const QPlatformIntegration *self,
    QWindow *a0,
    WId a1) {
  return self->QPlatformIntegration::createForeignWindow(a0, a1);
}

#if !defined(QT_NO_OPENGL)
//  QPlatformOpenGLContext
//      *QPlatformIntegration::createPlatformOpenGLContext(QOpenGLContext
//      *context) const
extern "C" Q_DECL_EXPORT
QPlatformOpenGLContext *ritual_own_ZNK20QPlatformIntegration27createPlatformOpenGLContextEP14QOpenGLContext(
    const QPlatformIntegration *self,
    QOpenGLContext *context) {
  return self->QPlatformIntegration::createPlatformOpenGLContext(context);
}
#endif  // !defined(QT_NO_OPENGL)

//  QPaintEngine *QPlatformIntegration::createImagePaintEngine(QPaintDevice
//      *paintDevice) const
extern "C" Q_DECL_EXPORT
QPaintEngine *ritual_own_ZNK20QPlatformIntegration22createImagePaintEngineEP12QPaintDevice(
    const QPlatformIntegration *self,
    QPaintDevice *paintDevice) {
  return self->QPlatformIntegration::createImagePaintEngine(paintDevice);
}

//  void QPlatformIntegration::initialize()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QPlatformIntegration10initializeEv(
    QPlatformIntegration *self) {
  self->QPlatformIntegration::initialize();
}

//  void QPlatformIntegration::destroy()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QPlatformIntegration7destroyEv(
    QPlatformIntegration *self) {
  self->QPlatformIntegration::destroy();
}

//  QPlatformFontDatabase *QPlatformIntegration::fontDatabase() const
extern "C" Q_DECL_EXPORT
QPlatformFontDatabase *ritual_own_ZNK20QPlatformIntegration12fontDatabaseEv(
    const QPlatformIntegration *self) {
  return self->QPlatformIntegration::fontDatabase();
}

#if !defined(QT_NO_CLIPBOARD)
//  QPlatformClipboard *QPlatformIntegration::clipboard() const
extern "C" Q_DECL_EXPORT
QPlatformClipboard *ritual_own_ZNK20QPlatformIntegration9clipboardEv(
    const QPlatformIntegration *self) {
  return self->QPlatformIntegration::clipboard();
}
#endif  // !defined(QT_NO_CLIPBOARD)

#if QT_CONFIG(draganddrop)
//  QPlatformDrag *QPlatformIntegration::drag() const
extern "C" Q_DECL_EXPORT
QPlatformDrag *ritual_own_ZNK20QPlatformIntegration4dragEv(
    const QPlatformIntegration *self) {
  return self->QPlatformIntegration::drag();
}
#endif  // QT_CONFIG(draganddrop)

//  QPlatformInputContext *QPlatformIntegration::inputContext() const
extern "C" Q_DECL_EXPORT
QPlatformInputContext *ritual_own_ZNK20QPlatformIntegration12inputContextEv(
    const QPlatformIntegration *self) {
  return self->QPlatformIntegration::inputContext();
}

#if QT_CONFIG(accessibility)
//  QPlatformAccessibility *QPlatformIntegration::accessibility() const
extern "C" Q_DECL_EXPORT
QPlatformAccessibility *ritual_own_ZNK20QPlatformIntegration13accessibilityEv(
    const QPlatformIntegration *self) {
  return self->QPlatformIntegration::accessibility();
}
#endif  // QT_CONFIG(accessibility)

//  QPlatformNativeInterface *QPlatformIntegration::nativeInterface() const
extern "C" Q_DECL_EXPORT
QPlatformNativeInterface *ritual_own_ZNK20QPlatformIntegration15nativeInterfaceEv(
    const QPlatformIntegration *self) {
  return self->QPlatformIntegration::nativeInterface();
}

//  QPlatformServices *QPlatformIntegration::services() const
extern "C" Q_DECL_EXPORT
QPlatformServices *ritual_own_ZNK20QPlatformIntegration8servicesEv(
    const QPlatformIntegration *self) {
  return self->QPlatformIntegration::services();
}

//  QVariant QPlatformIntegration::styleHint(StyleHint hint) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK20QPlatformIntegration9styleHintENS_9StyleHintE(
    const QPlatformIntegration *self,
    QPlatformIntegration::StyleHint hint) {
  return new QVariant(self->QPlatformIntegration::styleHint(hint));
}

//  Qt::WindowState QPlatformIntegration::defaultWindowState(Qt::WindowFlags
//      a0) const
extern "C" Q_DECL_EXPORT
Qt::WindowState ritual_own_ZNK20QPlatformIntegration18defaultWindowStateE6QFlagsIN2Qt10WindowTypeEE(
    const QPlatformIntegration *self,
    int a0) {
  return self->QPlatformIntegration::defaultWindowState(
      QFlags<Qt::WindowType>::fromInt(a0));
}

//  Qt::KeyboardModifiers QPlatformIntegration::queryKeyboardModifiers()
//      const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK20QPlatformIntegration22queryKeyboardModifiersEv(
    const QPlatformIntegration *self) {
  return static_cast<int>(
      static_cast<const OwnQPlatformIntegration *>(self)->OwnQPlatformIntegration::queryKeyboardModifiers().toInt());
}

//  QPlatformKeyMapper *QPlatformIntegration::keyMapper() const
extern "C" Q_DECL_EXPORT
QPlatformKeyMapper *ritual_own_ZNK20QPlatformIntegration9keyMapperEv(
    const QPlatformIntegration *self) {
  return self->QPlatformIntegration::keyMapper();
}

//  QPlatformTheme *QPlatformIntegration::createPlatformTheme(const QString
//      &name) const
extern "C" Q_DECL_EXPORT
QPlatformTheme *ritual_own_ZNK20QPlatformIntegration19createPlatformThemeERK7QString(
    const QPlatformIntegration *self,
    const QString *name) {
  return self->QPlatformIntegration::createPlatformTheme(*name);
}

//  QPlatformOffscreenSurface
//      *QPlatformIntegration::createPlatformOffscreenSurface(QOffscreenSurfa
//      ce *surface) const
extern "C" Q_DECL_EXPORT
QPlatformOffscreenSurface *ritual_own_ZNK20QPlatformIntegration30createPlatformOffscreenSurfaceEP17QOffscreenSurface(
    const QPlatformIntegration *self,
    QOffscreenSurface *surface) {
  return self->QPlatformIntegration::createPlatformOffscreenSurface(surface);
}

#if !defined(QT_NO_SESSIONMANAGER)
//  QPlatformSessionManager
//      *QPlatformIntegration::createPlatformSessionManager(const QString
//      &id, const QString &key) const
extern "C" Q_DECL_EXPORT
QPlatformSessionManager *ritual_own_ZNK20QPlatformIntegration28createPlatformSessionManagerERK7QStringS2_(
    const QPlatformIntegration *self,
    const QString *id,
    const QString *key) {
  return self->QPlatformIntegration::createPlatformSessionManager(*id, *key);
}
#endif  // !defined(QT_NO_SESSIONMANAGER)

//  void QPlatformIntegration::sync()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QPlatformIntegration4syncEv(QPlatformIntegration *self) {
  self->QPlatformIntegration::sync();
}

#if !defined(QT_NO_OPENGL)
//  QOpenGLContext::OpenGLModuleType QPlatformIntegration::openGLModuleType()
extern "C" Q_DECL_EXPORT
QOpenGLContext::OpenGLModuleType ritual_own_ZN20QPlatformIntegration16openGLModuleTypeEv(
    QPlatformIntegration *self) {
  return self->QPlatformIntegration::openGLModuleType();
}
#endif  // !defined(QT_NO_OPENGL)

//  void QPlatformIntegration::setApplicationIcon(const QIcon &icon) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK20QPlatformIntegration18setApplicationIconERK5QIcon(
    const QPlatformIntegration *self,
    const QIcon *icon) {
  self->QPlatformIntegration::setApplicationIcon(*icon);
}

//  void QPlatformIntegration::setApplicationBadge(qint64 number)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QPlatformIntegration19setApplicationBadgeEx(
    QPlatformIntegration *self,
    qint64 number) {
  self->QPlatformIntegration::setApplicationBadge(number);
}

//  void QPlatformIntegration::beep() const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK20QPlatformIntegration4beepEv(
    const QPlatformIntegration *self) {
  self->QPlatformIntegration::beep();
}

//  void QPlatformIntegration::quit() const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK20QPlatformIntegration4quitEv(
    const QPlatformIntegration *self) {
  self->QPlatformIntegration::quit();
}

#if QT_CONFIG(vulkan) || defined(Q_QDOC)
//  QPlatformVulkanInstance
//      *QPlatformIntegration::createPlatformVulkanInstance(QVulkanInstance
//      *instance) const
extern "C" Q_DECL_EXPORT
QPlatformVulkanInstance *ritual_own_ZNK20QPlatformIntegration28createPlatformVulkanInstanceEP15QVulkanInstance(
    const QPlatformIntegration *self,
    QVulkanInstance *instance) {
  return self->QPlatformIntegration::createPlatformVulkanInstance(instance);
}
#endif  // QT_CONFIG(vulkan) || defined(Q_QDOC)
