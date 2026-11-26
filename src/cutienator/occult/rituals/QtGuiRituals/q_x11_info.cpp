//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qtx11extras_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if defined(Q_OS_UNIX) && (QT_CONFIG(xcb))
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtx11extras_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>

//  bool QX11Info::isPlatformX11()
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QX11Info13isPlatformX11Ev() {
  return QX11Info::isPlatformX11();
}

//  int QX11Info::appDpiX(int screen)
extern "C" Q_DECL_EXPORT
int ritual_ZN8QX11Info7appDpiXEi(int screen) {
  return QX11Info::appDpiX(screen);
}

//  int QX11Info::appDpiY(int screen)
extern "C" Q_DECL_EXPORT
int ritual_ZN8QX11Info7appDpiYEi(int screen) {
  return QX11Info::appDpiY(screen);
}

//  quint32 QX11Info::appRootWindow(int screen)
extern "C" Q_DECL_EXPORT
quint32 ritual_ZN8QX11Info13appRootWindowEi(int screen) {
  return QX11Info::appRootWindow(screen);
}

//  int QX11Info::appScreen()
extern "C" Q_DECL_EXPORT
int ritual_ZN8QX11Info9appScreenEv() {
  return QX11Info::appScreen();
}

//  quint32 QX11Info::appTime()
extern "C" Q_DECL_EXPORT
quint32 ritual_ZN8QX11Info7appTimeEv() {
  return QX11Info::appTime();
}

//  quint32 QX11Info::appUserTime()
extern "C" Q_DECL_EXPORT
quint32 ritual_ZN8QX11Info11appUserTimeEv() {
  return QX11Info::appUserTime();
}

//  void QX11Info::setAppTime(quint32 time)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QX11Info10setAppTimeEj(quint32 time) {
  QX11Info::setAppTime(time);
}

//  void QX11Info::setAppUserTime(quint32 time)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QX11Info14setAppUserTimeEj(quint32 time) {
  QX11Info::setAppUserTime(time);
}

//  quint32 QX11Info::getTimestamp()
extern "C" Q_DECL_EXPORT
quint32 ritual_ZN8QX11Info12getTimestampEv() {
  return QX11Info::getTimestamp();
}

//  QByteArray QX11Info::nextStartupId()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN8QX11Info13nextStartupIdEv() {
  return new QByteArray(QX11Info::nextStartupId());
}

//  void QX11Info::setNextStartupId(const QByteArray &id)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QX11Info16setNextStartupIdERK10QByteArray(
    const QByteArray *id) {
  QX11Info::setNextStartupId(*id);
}

//  Display *QX11Info::display()
extern "C" Q_DECL_EXPORT
Display *ritual_ZN8QX11Info7displayEv() {
  return QX11Info::display();
}

//  xcb_connection_t *QX11Info::connection()
extern "C" Q_DECL_EXPORT
xcb_connection_t *ritual_ZN8QX11Info10connectionEv() {
  return QX11Info::connection();
}

//  bool QX11Info::isCompositingManagerRunning(int screen)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QX11Info27isCompositingManagerRunningEi(int screen) {
  return QX11Info::isCompositingManagerRunning(screen);
}

//  qint32 QX11Info::generatePeekerId()
extern "C" Q_DECL_EXPORT
qint32 ritual_ZN8QX11Info16generatePeekerIdEv() {
  return QX11Info::generatePeekerId();
}

//  bool QX11Info::removePeekerId(qint32 peekerId)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QX11Info14removePeekerIdEi(qint32 peekerId) {
  return QX11Info::removePeekerId(peekerId);
}

//  bool QX11Info::peekEventQueue(PeekerCallback peeker, void *peekerData,
//      PeekOptions option, qint32 peekerId)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QX11Info14peekEventQueueEPFbP19xcb_generic_event_tPvES2_6QFlagsINS_10PeekOptionEEi(
    void *peeker,
    void *peekerData,
    int option,
    qint32 peekerId) {
  return QX11Info::peekEventQueue(
      reinterpret_cast<QX11Info::PeekerCallback>(peeker),
      peekerData,
      QFlags<QX11Info::PeekOption>::fromInt(option),
      peekerId);
}

//  QX11Info::QX11Info()
extern "C" Q_DECL_EXPORT
QX11Info *ritual_ZN8QX11InfoC1Ev() {
  return new QX11Info();
}

//  QX11Info::~QX11Info()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QX11InfoD1Ev(QX11Info *self) {
  delete self;
}

#endif  // defined(Q_OS_UNIX) && (QT_CONFIG(xcb))
