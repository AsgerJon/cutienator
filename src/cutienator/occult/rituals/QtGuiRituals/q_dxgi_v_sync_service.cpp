//  Written by hand on 2026-11-25 from
//  QtGui/6.12.0/QtGui/private/qdxgivsyncservice_p.h, Qt 6.12.0, as the
//  Qt of Windows installs it. Kept as it is when the generator runs
//  again.
//  A 'LUID' of Windows is passed as the address of one. Not written:
//  'registerCallback', which takes a 'std::function'.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtGui/6.12.0/QtGui/private/qdxgivsyncservice_p.h>
#include <QtGui/qwindow.h>

//  QDxgiVSyncService *QDxgiVSyncService::instance()
extern "C" Q_DECL_EXPORT
QDxgiVSyncService *ritual_ZN17QDxgiVSyncService8instanceEv() {
  return QDxgiVSyncService::instance();
}

//  void QDxgiVSyncService::refAdapter(LUID luid)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDxgiVSyncService10refAdapterE5_LUID(
    QDxgiVSyncService *self,
    const LUID *luid) {
  self->refAdapter(*luid);
}

//  void QDxgiVSyncService::derefAdapter(LUID luid)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDxgiVSyncService12derefAdapterE5_LUID(
    QDxgiVSyncService *self,
    const LUID *luid) {
  self->derefAdapter(*luid);
}

//  void QDxgiVSyncService::beginFrame(LUID luid)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDxgiVSyncService10beginFrameE5_LUID(
    QDxgiVSyncService *self,
    const LUID *luid) {
  self->beginFrame(*luid);
}

//  void QDxgiVSyncService::registerWindow(QWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDxgiVSyncService14registerWindowEP7QWindow(
    QDxgiVSyncService *self,
    QWindow *window) {
  self->registerWindow(window);
}

//  void QDxgiVSyncService::unregisterWindow(QWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDxgiVSyncService16unregisterWindowEP7QWindow(
    QDxgiVSyncService *self,
    QWindow *window) {
  self->unregisterWindow(window);
}

//  bool QDxgiVSyncService::supportsWindow(QWindow *window)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QDxgiVSyncService14supportsWindowEP7QWindow(
    QDxgiVSyncService *self,
    QWindow *window) {
  return self->supportsWindow(window);
}

//  void QDxgiVSyncService::unregisterCallback(qsizetype id)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDxgiVSyncService18unregisterCallbackEx(
    QDxgiVSyncService *self,
    qsizetype id) {
  self->unregisterCallback(id);
}

//  QDxgiVSyncService::QDxgiVSyncService()
extern "C" Q_DECL_EXPORT
QDxgiVSyncService *ritual_ZN17QDxgiVSyncServiceC1Ev() {
  return new QDxgiVSyncService();
}

//  QDxgiVSyncService::~QDxgiVSyncService()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDxgiVSyncServiceD1Ev(QDxgiVSyncService *self) {
  delete self;
}

//  void QDxgiVSyncService::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDxgiVSyncService7destroyEv(QDxgiVSyncService *self) {
  self->destroy();
}

//  void QDxgiVSyncService::teardownDxgi()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDxgiVSyncService12teardownDxgiEv(QDxgiVSyncService *self) {
  self->teardownDxgi();
}

//  void QDxgiVSyncService::global_destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDxgiVSyncService14global_destroyEv() {
  QDxgiVSyncService::global_destroy();
}

//  void QDxgiVSyncService::cleanupAdapterData(AdapterData *a)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDxgiVSyncService18cleanupAdapterDataEPNS_11AdapterDataE(
    QDxgiVSyncService *self,
    QDxgiVSyncService::AdapterData *a) {
  self->cleanupAdapterData(a);
}

//  void QDxgiVSyncService::cleanupWindowData(WindowData *w)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDxgiVSyncService17cleanupWindowDataEPNS_10WindowDataE(
    QDxgiVSyncService *self,
    QDxgiVSyncService::WindowData *w) {
  self->cleanupWindowData(w);
}

//  void QDxgiVSyncService::updateWindowData(QWindow *window, WindowData *w)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QDxgiVSyncService16updateWindowDataEP7QWindowPNS_10WindowDataE(
    QDxgiVSyncService *self,
    QWindow *window,
    QDxgiVSyncService::WindowData *w) {
  self->updateWindowData(window, w);
}

#endif  // defined(Q_OS_WIN)
