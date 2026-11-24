//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qwindowsysteminterface_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>

//  QWindowSystemInterfacePrivate::FileOpenEvent::FileOpenEvent(const QString
//      &fileName)
extern "C" Q_DECL_EXPORT
QWindowSystemInterfacePrivate::FileOpenEvent *ritual_ZN29QWindowSystemInterfacePrivate13FileOpenEventC1ERK7QString(
    const QString *fileName) {
  return new QWindowSystemInterfacePrivate::FileOpenEvent(*fileName);
}

//  QWindowSystemInterfacePrivate::FileOpenEvent::FileOpenEvent(const QUrl
//      &url)
extern "C" Q_DECL_EXPORT
QWindowSystemInterfacePrivate::FileOpenEvent *ritual_ZN29QWindowSystemInterfacePrivate13FileOpenEventC1ERK4QUrl(
    const QUrl *url) {
  return new QWindowSystemInterfacePrivate::FileOpenEvent(*url);
}

//  QWindowSystemInterfacePrivate::FileOpenEvent::~FileOpenEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QWindowSystemInterfacePrivate13FileOpenEventD1Ev(
    QWindowSystemInterfacePrivate::FileOpenEvent *self) {
  delete self;
}
