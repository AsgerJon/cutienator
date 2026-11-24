//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformservices.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformservices.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <QtCore/qbytearray.h>
#include <cstring>

//  A QPlatformServices that Python can take functions over in. Every QPlatformServices
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQPlatformServicesCall0)(const void *, const QUrl *, int *);
typedef bool (*CuteQPlatformServicesCall1)(const void *, const QUrl *, int *);
typedef const QByteArray * (*CuteQPlatformServicesCall2)(const void *, int *);
typedef bool (*CuteQPlatformServicesCall3)(const void *, int, int *);
typedef void * (*CuteQPlatformServicesCall4)(const void *, QWindow *, int *);
class CuteQPlatformServices : public QPlatformServices {
public:
  using QPlatformServices::QPlatformServices;
  void *taken[5] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN17QPlatformServices7openUrlERK4QUrl")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QPlatformServices12openDocumentERK4QUrl")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QPlatformServices18desktopEnvironmentEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QPlatformServices13hasCapabilityENS_10CapabilityE")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QPlatformServices11colorPickerEP7QWindow")) {
      taken[4] = call;
      return true;
    }
    return false;
  }

  //  bool QPlatformServices::openUrl(const QUrl &url)
  bool openUrl(const QUrl &url) override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlatformServicesCall0 call = reinterpret_cast<CuteQPlatformServicesCall0>(taken[0]);
      bool given = call(this, &url, &handled);
      if (handled) return given;
    }
    return QPlatformServices::openUrl(url);
  }

  //  bool QPlatformServices::openDocument(const QUrl &url)
  bool openDocument(const QUrl &url) override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlatformServicesCall1 call = reinterpret_cast<CuteQPlatformServicesCall1>(taken[1]);
      bool given = call(this, &url, &handled);
      if (handled) return given;
    }
    return QPlatformServices::openDocument(url);
  }

  //  QByteArray QPlatformServices::desktopEnvironment() const
  QByteArray desktopEnvironment() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQPlatformServicesCall2 call = reinterpret_cast<CuteQPlatformServicesCall2>(taken[2]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QPlatformServices::desktopEnvironment();
  }

  //  bool QPlatformServices::hasCapability(Capability capability) const
  bool hasCapability(
      QPlatformServices::Capability capability) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQPlatformServicesCall3 call = reinterpret_cast<CuteQPlatformServicesCall3>(taken[3]);
      bool given = call(this, static_cast<int>(capability), &handled);
      if (handled) return given;
    }
    return QPlatformServices::hasCapability(capability);
  }

  //  QPlatformServiceColorPicker *QPlatformServices::colorPicker(QWindow
  //      *parent)
  QPlatformServiceColorPicker *colorPicker(QWindow *parent) override {
    if (taken[4]) {
      int handled = 0;
      CuteQPlatformServicesCall4 call = reinterpret_cast<CuteQPlatformServicesCall4>(taken[4]);
      void * given = call(this, parent, &handled);
      if (handled) return static_cast<QPlatformServiceColorPicker *>(given);
    }
    return QPlatformServices::colorPicker(parent);
  }
};

//  QPlatformServices::QPlatformServices()
extern "C" Q_DECL_EXPORT
QPlatformServices *ritual_ZN17QPlatformServicesC1Ev() {
  return new CuteQPlatformServices();
}

//  QPlatformServices::~QPlatformServices()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QPlatformServicesD1Ev(QPlatformServices *self) {
  delete self;
}

//  bool QPlatformServices::openUrl(const QUrl &url)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QPlatformServices7openUrlERK4QUrl(
    QPlatformServices *self,
    const QUrl *url) {
  return self->openUrl(*url);
}

//  bool QPlatformServices::openDocument(const QUrl &url)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QPlatformServices12openDocumentERK4QUrl(
    QPlatformServices *self,
    const QUrl *url) {
  return self->openDocument(*url);
}

//  QByteArray QPlatformServices::desktopEnvironment() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK17QPlatformServices18desktopEnvironmentEv(
    const QPlatformServices *self) {
  return new QByteArray(self->desktopEnvironment());
}

//  bool QPlatformServices::hasCapability(Capability capability) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QPlatformServices13hasCapabilityENS_10CapabilityE(
    const QPlatformServices *self,
    QPlatformServices::Capability capability) {
  return self->hasCapability(capability);
}

//  QPlatformServiceColorPicker *QPlatformServices::colorPicker(QWindow
//      *parent)
extern "C" Q_DECL_EXPORT
QPlatformServiceColorPicker *ritual_ZN17QPlatformServices11colorPickerEP7QWindow(
    QPlatformServices *self,
    QWindow *parent) {
  return self->colorPicker(parent);
}

//  a Python function taken by a CuteQPlatformServices, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlatformServices(
    QPlatformServices *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlatformServices *>(self)->take(key, call);
}

//  bool QPlatformServices::openUrl(const QUrl &url)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QPlatformServices7openUrlERK4QUrl(
    QPlatformServices *self,
    const QUrl *url) {
  return self->QPlatformServices::openUrl(*url);
}

//  bool QPlatformServices::openDocument(const QUrl &url)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QPlatformServices12openDocumentERK4QUrl(
    QPlatformServices *self,
    const QUrl *url) {
  return self->QPlatformServices::openDocument(*url);
}

//  QByteArray QPlatformServices::desktopEnvironment() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZNK17QPlatformServices18desktopEnvironmentEv(
    const QPlatformServices *self) {
  return new QByteArray(self->QPlatformServices::desktopEnvironment());
}

//  bool QPlatformServices::hasCapability(Capability capability) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK17QPlatformServices13hasCapabilityENS_10CapabilityE(
    const QPlatformServices *self,
    QPlatformServices::Capability capability) {
  return self->QPlatformServices::hasCapability(capability);
}

//  QPlatformServiceColorPicker *QPlatformServices::colorPicker(QWindow
//      *parent)
extern "C" Q_DECL_EXPORT
QPlatformServiceColorPicker *ritual_own_ZN17QPlatformServices11colorPickerEP7QWindow(
    QPlatformServices *self,
    QWindow *parent) {
  return self->QPlatformServices::colorPicker(parent);
}
