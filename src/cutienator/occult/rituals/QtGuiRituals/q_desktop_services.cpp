//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qdesktopservices.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if !defined(QT_NO_DESKTOPSERVICES)
#include <QtGui/qdesktopservices.h>
#include <QtCore/qurl.h>
#include <QtCore/qstring.h>

//  bool QDesktopServices::openUrl(const QUrl &url)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QDesktopServices7openUrlERK4QUrl(const QUrl *url) {
  return QDesktopServices::openUrl(*url);
}

//  void QDesktopServices::setUrlHandler(const QString &scheme, QObject
//      *receiver, const char *method)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDesktopServices13setUrlHandlerERK7QStringP7QObjectPKc(
    const QString *scheme,
    QObject *receiver,
    const char *method) {
  QDesktopServices::setUrlHandler(*scheme, receiver, method);
}

//  void QDesktopServices::unsetUrlHandler(const QString &scheme)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDesktopServices15unsetUrlHandlerERK7QString(
    const QString *scheme) {
  QDesktopServices::unsetUrlHandler(*scheme);
}

//  QDesktopServices::~QDesktopServices()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QDesktopServicesD1Ev(QDesktopServices *self) {
  delete self;
}

#endif  // !defined(QT_NO_DESKTOPSERVICES)
