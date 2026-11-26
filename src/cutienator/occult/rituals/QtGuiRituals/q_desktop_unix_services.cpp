//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qdesktopunixservices_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if defined(Q_OS_UNIX) && (QT_CONFIG(xcb) || !(defined(Q_OS_IOS) || defined(Q_OS_TVOS) || defined(Q_OS_VISIONOS)))
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qdesktopunixservices_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qurl.h>
#include <QtCore/qstring.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/private/qdesktopunixservices_p.h>
#include <QtGui/private/qtguiglobal_p.h>
#include <QtGui/qguiapplication.h>
#include <QtGui/qwindow.h>
#include <QtGui/qpa/qplatformwindow_p.h>
#include <QtGui/qpa/qplatformwindow.h>
#include <QtGui/qpa/qplatformnativeinterface.h>
#include <QtCore/QDebug>
#include <QtCore/QFile>
#include <QtCore/QFileInfo>
#if QT_CONFIG(process)
# include <QtCore/QProcess>
#endif
#if QT_CONFIG(settings)
#include <QtCore/QSettings>
#endif
#include <QtCore/QStandardPaths>
#include <QtCore/QUrl>
#if QT_CONFIG(dbus)
#include <QtCore/private/qcore_unix_p.h>
#include <QtCore/QFileInfo>
#include <QtCore/QUrlQuery>
#include <QtDBus/QDBusConnection>
#include <QtDBus/QDBusServiceWatcher>
#include <QtDBus/QDBusMessage>
#include <QtDBus/QDBusPendingCall>
#include <QtDBus/QDBusPendingCallWatcher>
#include <QtDBus/QDBusPendingReply>
#include <QtDBus/QDBusUnixFileDescriptor>
#include <fcntl.h>
#endif
#include <stdlib.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/gui/platform/unix/qdesktopunixservices.cpp, line 92, as local:qdesktopunixservices.cpp:checkExecutable
#if QT_CONFIG(multiprocess)
static inline bool checkExecutable(const QString &candidate, QString *result)
{
    *result = QStandardPaths::findExecutable(candidate);
    return !result->isEmpty();
}
#endif  // QT_CONFIG(multiprocess)

//  from src/gui/platform/unix/qdesktopunixservices.cpp, line 182, as local:qdesktopunixservices.cpp:xdgDesktopPortalOpenFile
#if QT_CONFIG(multiprocess)
#if QT_CONFIG(dbus)
static inline QDBusMessage xdgDesktopPortalOpenFile(const QUrl &url, const QString &parentWindow,
                                                    const QString &xdgActivationToken)
{
    // DBus signature:
    // OpenFile (IN   s      parent_window,
    //           IN   h      fd,
    //           IN   a{sv}  options,
    //           OUT  o      handle)
    // Options:
    // handle_token (s) -  A string that will be used as the last element of the @handle.
    // writable (b) - Whether to allow the chosen application to write to the file.

    const int fd = qt_safe_open(QFile::encodeName(url.toLocalFile()), O_RDONLY);
    if (fd != -1) {
        QDBusMessage message = QDBusMessage::createMethodCall("org.freedesktop.portal.Desktop"_L1,
                                                              "/org/freedesktop/portal/desktop"_L1,
                                                              "org.freedesktop.portal.OpenURI"_L1,
                                                              "OpenFile"_L1);

        QDBusUnixFileDescriptor descriptor;
        descriptor.giveFileDescriptor(fd);

        QVariantMap options = {};

        if (!xdgActivationToken.isEmpty()) {
            options.insert("activation_token"_L1, xdgActivationToken);
        }

        message << parentWindow << QVariant::fromValue(descriptor) << options;

        return QDBusConnection::sessionBus().call(message);
    }

    return QDBusMessage::createError(QDBusError::InternalError, qt_error_string());
}
#endif  // QT_CONFIG(dbus)
#endif  // QT_CONFIG(multiprocess)

//  from src/gui/platform/unix/qdesktopunixservices.cpp, line 218, as local:qdesktopunixservices.cpp:xdgDesktopPortalOpenUrl
#if QT_CONFIG(multiprocess)
#if QT_CONFIG(dbus)
static inline QDBusMessage xdgDesktopPortalOpenUrl(const QUrl &url, const QString &parentWindow,
                                                   const QString &xdgActivationToken)
{
    // DBus signature:
    // OpenURI (IN   s      parent_window,
    //          IN   s      uri,
    //          IN   a{sv}  options,
    //          OUT  o      handle)
    // Options:
    // handle_token (s) -  A string that will be used as the last element of the @handle.
    // writable (b) - Whether to allow the chosen application to write to the file.
    //                This key only takes effect the uri points to a local file that is exported in the document portal,
    //                and the chosen application is sandboxed itself.

    QDBusMessage message = QDBusMessage::createMethodCall("org.freedesktop.portal.Desktop"_L1,
                                                          "/org/freedesktop/portal/desktop"_L1,
                                                          "org.freedesktop.portal.OpenURI"_L1,
                                                          "OpenURI"_L1);
    // FIXME parent_window_id and handle writable option
    QVariantMap options;

    if (!xdgActivationToken.isEmpty()) {
        options.insert("activation_token"_L1, xdgActivationToken);
    }

    message << parentWindow << url.toString() << options;

    return QDBusConnection::sessionBus().call(message);
}
#endif  // QT_CONFIG(dbus)
#endif  // QT_CONFIG(multiprocess)

//  from src/gui/platform/unix/qdesktopunixservices.cpp, line 248, as local:qdesktopunixservices.cpp:xdgDesktopPortalSendEmail
#if QT_CONFIG(multiprocess)
#if QT_CONFIG(dbus)
static inline QDBusMessage xdgDesktopPortalSendEmail(const QUrl &url, const QString &parentWindow,
                                                     const QString &xdgActivationToken)
{
    // DBus signature:
    // ComposeEmail (IN   s      parent_window,
    //               IN   a{sv}  options,
    //               OUT  o      handle)
    // Options:
    // address (s) - The email address to send to.
    // subject (s) - The subject for the email.
    // body (s) - The body for the email.
    // attachment_fds (ah) - File descriptors for files to attach.

    QUrlQuery urlQuery(url);
    QVariantMap options;
    options.insert("address"_L1, url.path());
    options.insert("subject"_L1, urlQuery.queryItemValue("subject"_L1));
    options.insert("body"_L1, urlQuery.queryItemValue("body"_L1));

    // O_PATH seems to be present since Linux 2.6.39, which is not case of RHEL 6
#ifdef O_PATH
    QList<QDBusUnixFileDescriptor> attachments;
    const QStringList attachmentUris = urlQuery.allQueryItemValues("attachment"_L1);

    for (const QString &attachmentUri : attachmentUris) {
        const int fd = qt_safe_open(QFile::encodeName(attachmentUri), O_PATH);
        if (fd != -1) {
            QDBusUnixFileDescriptor descriptor(fd);
            attachments << descriptor;
            qt_safe_close(fd);
        }
    }

    options.insert("attachment_fds"_L1, QVariant::fromValue(attachments));
#endif

    if (!xdgActivationToken.isEmpty()) {
        options.insert("activation_token"_L1, xdgActivationToken);
    }

    QDBusMessage message = QDBusMessage::createMethodCall("org.freedesktop.portal.Desktop"_L1,
                                                          "/org/freedesktop/portal/desktop"_L1,
                                                          "org.freedesktop.portal.Email"_L1,
                                                          "ComposeEmail"_L1);

    message << parentWindow << options;

    return QDBusConnection::sessionBus().call(message);
}
#endif  // QT_CONFIG(dbus)
#endif  // QT_CONFIG(multiprocess)

//  from src/gui/platform/unix/qdesktopunixservices.cpp, line 504, as _ZN20QDesktopUnixServices27portalFocusWindowIdentifierEv
#if QT_CONFIG(multiprocess)
inline QString QDesktopUnixServices::portalFocusWindowIdentifier()
{
    if (QWindow *focusWindow = QGuiApplication::focusWindow())
        return portalWindowIdentifier(focusWindow);
    return QString();
}
#endif  // QT_CONFIG(multiprocess)
//  -----------------------------------------------------------------------

//  A QDesktopUnixServices that Python can take functions over in. Every QDesktopUnixServices
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QByteArray * (*CuteQDesktopUnixServicesCall0)(const void *, int *);
typedef bool (*CuteQDesktopUnixServicesCall1)(const void *, int, int *);
typedef bool (*CuteQDesktopUnixServicesCall2)(const void *, const QUrl *, int *);
typedef bool (*CuteQDesktopUnixServicesCall3)(const void *, const QUrl *, int *);
typedef void * (*CuteQDesktopUnixServicesCall4)(const void *, QWindow *, int *);
typedef QString * (*CuteQDesktopUnixServicesCall5)(const void *, QWindow *, int *);
typedef void (*CuteQDesktopUnixServicesCall6)(const void *, QWindow *, const QString *, const QString *, int *);
typedef void (*CuteQDesktopUnixServicesCall7)(const void *, QWindow *, int *);
class CuteQDesktopUnixServices : public QDesktopUnixServices {
public:
  using QDesktopUnixServices::QDesktopUnixServices;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK17QPlatformServices18desktopEnvironmentEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QPlatformServices13hasCapabilityENS_10CapabilityE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QPlatformServices7openUrlERK4QUrl")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QPlatformServices12openDocumentERK4QUrl")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QPlatformServices11colorPickerEP7QWindow")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QDesktopUnixServices22portalWindowIdentifierEP7QWindow")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QDesktopUnixServices25registerDBusMenuForWindowEP7QWindowRK7QStringS4_")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QDesktopUnixServices27unregisterDBusMenuForWindowEP7QWindow")) {
      taken[7] = call;
      return true;
    }
    return false;
  }

  //  QByteArray QDesktopUnixServices::desktopEnvironment() const
  QByteArray desktopEnvironment() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQDesktopUnixServicesCall0 call = reinterpret_cast<CuteQDesktopUnixServicesCall0>(taken[0]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QDesktopUnixServices::desktopEnvironment();
  }

  //  bool QDesktopUnixServices::hasCapability(Capability capability) const
  bool hasCapability(
      QPlatformServices::Capability capability) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQDesktopUnixServicesCall1 call = reinterpret_cast<CuteQDesktopUnixServicesCall1>(taken[1]);
      bool given = call(this, static_cast<int>(capability), &handled);
      if (handled) return given;
    }
    return QDesktopUnixServices::hasCapability(capability);
  }

  //  bool QDesktopUnixServices::openUrl(const QUrl &url)
  bool openUrl(const QUrl &url) override {
    if (taken[2]) {
      int handled = 0;
      CuteQDesktopUnixServicesCall2 call = reinterpret_cast<CuteQDesktopUnixServicesCall2>(taken[2]);
      bool given = call(this, &url, &handled);
      if (handled) return given;
    }
    return QDesktopUnixServices::openUrl(url);
  }

  //  bool QDesktopUnixServices::openDocument(const QUrl &url)
  bool openDocument(const QUrl &url) override {
    if (taken[3]) {
      int handled = 0;
      CuteQDesktopUnixServicesCall3 call = reinterpret_cast<CuteQDesktopUnixServicesCall3>(taken[3]);
      bool given = call(this, &url, &handled);
      if (handled) return given;
    }
    return QDesktopUnixServices::openDocument(url);
  }

  //  QPlatformServiceColorPicker
  //      *QDesktopUnixServices::colorPicker(QWindow *parent)
  QPlatformServiceColorPicker *colorPicker(QWindow *parent) override {
    if (taken[4]) {
      int handled = 0;
      CuteQDesktopUnixServicesCall4 call = reinterpret_cast<CuteQDesktopUnixServicesCall4>(taken[4]);
      void * given = call(this, parent, &handled);
      if (handled) return static_cast<QPlatformServiceColorPicker *>(given);
    }
    return QDesktopUnixServices::colorPicker(parent);
  }

  //  QString QDesktopUnixServices::portalWindowIdentifier(QWindow *window)
  QString portalWindowIdentifier(QWindow *window) override {
    if (taken[5]) {
      int handled = 0;
      CuteQDesktopUnixServicesCall5 call = reinterpret_cast<CuteQDesktopUnixServicesCall5>(taken[5]);
      QString * given = call(this, window, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QDesktopUnixServices::portalWindowIdentifier(window);
  }

  //  void QDesktopUnixServices::registerDBusMenuForWindow(QWindow *window,
  //      const QString &service, const QString &path)
  void registerDBusMenuForWindow(
      QWindow *window,
      const QString &service,
      const QString &path) override {
    if (taken[6]) {
      int handled = 0;
      CuteQDesktopUnixServicesCall6 call = reinterpret_cast<CuteQDesktopUnixServicesCall6>(taken[6]);
      call(this, window, &service, &path, &handled);
      if (handled) return;
    }
    QDesktopUnixServices::registerDBusMenuForWindow(window, service, path);
  }

  //  void QDesktopUnixServices::unregisterDBusMenuForWindow(QWindow
  //      *window)
  void unregisterDBusMenuForWindow(QWindow *window) override {
    if (taken[7]) {
      int handled = 0;
      CuteQDesktopUnixServicesCall7 call = reinterpret_cast<CuteQDesktopUnixServicesCall7>(taken[7]);
      call(this, window, &handled);
      if (handled) return;
    }
    QDesktopUnixServices::unregisterDBusMenuForWindow(window);
  }
};

//  QDesktopUnixServices::QDesktopUnixServices()
extern "C" Q_DECL_EXPORT
QDesktopUnixServices *ritual_ZN20QDesktopUnixServicesC1Ev() {
  return new CuteQDesktopUnixServices();
}

//  QDesktopUnixServices::~QDesktopUnixServices()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDesktopUnixServicesD1Ev(QDesktopUnixServices *self) {
  delete self;
}

//  QByteArray QDesktopUnixServices::desktopEnvironment() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK20QDesktopUnixServices18desktopEnvironmentEv(
    const QDesktopUnixServices *self) {
  return new QByteArray(self->desktopEnvironment());
}

//  bool QDesktopUnixServices::hasCapability(Capability capability) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QDesktopUnixServices13hasCapabilityEN17QPlatformServices10CapabilityE(
    const QDesktopUnixServices *self,
    QPlatformServices::Capability capability) {
  return self->hasCapability(capability);
}

//  bool QDesktopUnixServices::openUrl(const QUrl &url)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QDesktopUnixServices7openUrlERK4QUrl(
    QDesktopUnixServices *self,
    const QUrl *url) {
  return self->openUrl(*url);
}

//  bool QDesktopUnixServices::openDocument(const QUrl &url)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QDesktopUnixServices12openDocumentERK4QUrl(
    QDesktopUnixServices *self,
    const QUrl *url) {
  return self->openDocument(*url);
}

//  QPlatformServiceColorPicker *QDesktopUnixServices::colorPicker(QWindow
//      *parent)
extern "C" Q_DECL_EXPORT
QPlatformServiceColorPicker *ritual_ZN20QDesktopUnixServices11colorPickerEP7QWindow(
    QDesktopUnixServices *self,
    QWindow *parent) {
  return self->colorPicker(parent);
}

//  void QDesktopUnixServices::setApplicationBadge(qint64 number)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDesktopUnixServices19setApplicationBadgeEx(
    QDesktopUnixServices *self,
    qint64 number) {
  self->setApplicationBadge(number);
}

//  QString QDesktopUnixServices::portalWindowIdentifier(QWindow *window)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QDesktopUnixServices22portalWindowIdentifierEP7QWindow(
    QDesktopUnixServices *self,
    QWindow *window) {
  return new QString(self->portalWindowIdentifier(window));
}

//  void QDesktopUnixServices::registerDBusMenuForWindow(QWindow *window,
//      const QString &service, const QString &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDesktopUnixServices25registerDBusMenuForWindowEP7QWindowRK7QStringS4_(
    QDesktopUnixServices *self,
    QWindow *window,
    const QString *service,
    const QString *path) {
  self->registerDBusMenuForWindow(window, *service, *path);
}

//  void QDesktopUnixServices::unregisterDBusMenuForWindow(QWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QDesktopUnixServices27unregisterDBusMenuForWindowEP7QWindow(
    QDesktopUnixServices *self,
    QWindow *window) {
  self->unregisterDBusMenuForWindow(window);
}

#if QT_CONFIG(multiprocess)
//  QString QDesktopUnixServices::portalFocusWindowIdentifier()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QDesktopUnixServices27portalFocusWindowIdentifierEv(
    QDesktopUnixServices *self) {
  return new QString(self->portalFocusWindowIdentifier());
}
#endif  // QT_CONFIG(multiprocess)

//  a Python function taken by a CuteQDesktopUnixServices, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDesktopUnixServices(
    QDesktopUnixServices *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDesktopUnixServices *>(self)->take(key, call);
}

//  QByteArray QDesktopUnixServices::desktopEnvironment() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZNK20QDesktopUnixServices18desktopEnvironmentEv(
    const QDesktopUnixServices *self) {
  return new QByteArray(self->QDesktopUnixServices::desktopEnvironment());
}

//  bool QDesktopUnixServices::hasCapability(Capability capability) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK20QDesktopUnixServices13hasCapabilityEN17QPlatformServices10CapabilityE(
    const QDesktopUnixServices *self,
    QPlatformServices::Capability capability) {
  return self->QDesktopUnixServices::hasCapability(capability);
}

//  bool QDesktopUnixServices::openUrl(const QUrl &url)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20QDesktopUnixServices7openUrlERK4QUrl(
    QDesktopUnixServices *self,
    const QUrl *url) {
  return self->QDesktopUnixServices::openUrl(*url);
}

//  bool QDesktopUnixServices::openDocument(const QUrl &url)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20QDesktopUnixServices12openDocumentERK4QUrl(
    QDesktopUnixServices *self,
    const QUrl *url) {
  return self->QDesktopUnixServices::openDocument(*url);
}

//  QPlatformServiceColorPicker *QDesktopUnixServices::colorPicker(QWindow
//      *parent)
extern "C" Q_DECL_EXPORT
QPlatformServiceColorPicker *ritual_own_ZN20QDesktopUnixServices11colorPickerEP7QWindow(
    QDesktopUnixServices *self,
    QWindow *parent) {
  return self->QDesktopUnixServices::colorPicker(parent);
}

//  QString QDesktopUnixServices::portalWindowIdentifier(QWindow *window)
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZN20QDesktopUnixServices22portalWindowIdentifierEP7QWindow(
    QDesktopUnixServices *self,
    QWindow *window) {
  return new QString(
      self->QDesktopUnixServices::portalWindowIdentifier(
          window));
}

//  void QDesktopUnixServices::registerDBusMenuForWindow(QWindow *window,
//      const QString &service, const QString &path)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QDesktopUnixServices25registerDBusMenuForWindowEP7QWindowRK7QStringS4_(
    QDesktopUnixServices *self,
    QWindow *window,
    const QString *service,
    const QString *path) {
  self->QDesktopUnixServices::registerDBusMenuForWindow(
      window,
      *service,
      *path);
}

//  void QDesktopUnixServices::unregisterDBusMenuForWindow(QWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QDesktopUnixServices27unregisterDBusMenuForWindowEP7QWindow(
    QDesktopUnixServices *self,
    QWindow *window) {
  self->QDesktopUnixServices::unregisterDBusMenuForWindow(window);
}

#endif  // defined(Q_OS_UNIX) && (QT_CONFIG(xcb) || !(defined(Q_OS_IOS) || defined(Q_OS_TVOS) || defined(Q_OS_VISIONOS)))
