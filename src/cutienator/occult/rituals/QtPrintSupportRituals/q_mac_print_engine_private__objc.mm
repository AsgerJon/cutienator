//  Written by hand on 2026-11-26 from
//  QtPrintSupport/6.12.0/QtPrintSupport/private/qprintengine_mac_p.h,
//  Qt 6.12.0, from Qt's source. Kept as it is when the generator runs
//  again. Objective-C++: the header sends Objective-C messages in its own
//  code and asks for no '__OBJC__', so only a compiler of Objective-C++ on
//  Apple's systems reads it; 'summon' builds this file there only. Qt writes
//  the class's functions in 'qprintengine_mac.mm', whose whole code
//  'q_mac_print_engine__objc.mm' copies into the same library, with the
//  class's table of virtual functions; the rituals here call that code.
//  'PMPageFormat', 'PMPrintSession' and 'PMPrintSettings' cross as their
//  address.
#include <QtPrintSupport/qtprintsupportglobal.h>
#if defined(Q_OS_MACOS)
#ifndef QT_NO_PRINTER
#include <AppKit/AppKit.h>
#include <ApplicationServices/ApplicationServices.h>
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qprintengine_mac_p.h>

//  QMacPrintEnginePrivate::QMacPrintEnginePrivate()
extern "C" Q_DECL_EXPORT
QMacPrintEnginePrivate *ritual_ZN22QMacPrintEnginePrivateC1Ev() {
  return new QMacPrintEnginePrivate();
}

//  QMacPrintEnginePrivate::~QMacPrintEnginePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QMacPrintEnginePrivateD1Ev(QMacPrintEnginePrivate *self) {
  delete self;
}

//  void QMacPrintEnginePrivate::initialize()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QMacPrintEnginePrivate10initializeEv(
    QMacPrintEnginePrivate *self) {
  self->initialize();
}

//  void QMacPrintEnginePrivate::releaseSession()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QMacPrintEnginePrivate14releaseSessionEv(
    QMacPrintEnginePrivate *self) {
  self->releaseSession();
}

//  bool QMacPrintEnginePrivate::newPage_helper()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QMacPrintEnginePrivate14newPage_helperEv(
    QMacPrintEnginePrivate *self) {
  return self->newPage_helper();
}

//  void QMacPrintEnginePrivate::setPageSize(const QPageSize &pageSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QMacPrintEnginePrivate11setPageSizeERK9QPageSize(
    QMacPrintEnginePrivate *self,
    const QPageSize *a0) {
  self->setPageSize(*a0);
}

//  bool QMacPrintEnginePrivate::isPrintSessionInitialized() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QMacPrintEnginePrivate25isPrintSessionInitializedEv(
    const QMacPrintEnginePrivate *self) {
  return self->isPrintSessionInitialized();
}

//  PMPageFormat QMacPrintEnginePrivate::format() const
extern "C" Q_DECL_EXPORT
void *ritual_ZNK22QMacPrintEnginePrivate6formatEv(
    const QMacPrintEnginePrivate *self) {
  return self->format();
}

//  PMPrintSession QMacPrintEnginePrivate::session() const
extern "C" Q_DECL_EXPORT
void *ritual_ZNK22QMacPrintEnginePrivate7sessionEv(
    const QMacPrintEnginePrivate *self) {
  return self->session();
}

//  PMPrintSettings QMacPrintEnginePrivate::settings() const
extern "C" Q_DECL_EXPORT
void *ritual_ZNK22QMacPrintEnginePrivate8settingsEv(
    const QMacPrintEnginePrivate *self) {
  return self->settings();
}

//  QPaintEngine *QMacPrintEnginePrivate::aggregateEngine()
extern "C" Q_DECL_EXPORT
QPaintEngine *ritual_ZN22QMacPrintEnginePrivate15aggregateEngineEv(
    QMacPrintEnginePrivate *self) {
  return self->aggregateEngine();
}

//  Qt::HANDLE QMacPrintEnginePrivate::nativeHandle()
extern "C" Q_DECL_EXPORT
void *ritual_ZN22QMacPrintEnginePrivate12nativeHandleEv(
    QMacPrintEnginePrivate *self) {
  return self->nativeHandle();
}

#endif  // QT_NO_PRINTER
#endif  // defined(Q_OS_MACOS)
