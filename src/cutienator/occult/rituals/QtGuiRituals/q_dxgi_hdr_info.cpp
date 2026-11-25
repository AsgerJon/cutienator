//  Written by hand on 2026-11-25 from
//  QtGui/6.12.0/QtGui/private/qdxgihdrinfo_p.h, Qt 6.12.0, as the
//  Qt of Windows installs it. Kept as it is when the generator runs
//  again.
//  What DirectX has, as 'IDXGIAdapter1 *' and a 'LUID', is passed as an
//  address.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if defined(Q_OS_WIN)
#include <QtGui/6.12.0/QtGui/private/qdxgihdrinfo_p.h>
#include <rhi/qrhi.h>

//  QDxgiHdrInfo::QDxgiHdrInfo(IDXGIAdapter1 *adapter)
extern "C" Q_DECL_EXPORT
QDxgiHdrInfo *ritual_ZN12QDxgiHdrInfoC1EP13IDXGIAdapter1(
    IDXGIAdapter1 *adapter) {
  return new QDxgiHdrInfo(adapter);
}

//  QDxgiHdrInfo::QDxgiHdrInfo(LUID luid)
extern "C" Q_DECL_EXPORT
QDxgiHdrInfo *ritual_ZN12QDxgiHdrInfoC1E5_LUID(const LUID *luid) {
  return new QDxgiHdrInfo(*luid);
}

//  QDxgiHdrInfo::QDxgiHdrInfo()
extern "C" Q_DECL_EXPORT
QDxgiHdrInfo *ritual_ZN12QDxgiHdrInfoC1Ev() {
  return new QDxgiHdrInfo();
}

//  QDxgiHdrInfo::~QDxgiHdrInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QDxgiHdrInfoD1Ev(QDxgiHdrInfo *self) {
  delete self;
}

//  bool QDxgiHdrInfo::isHdrCapable(QWindow *w)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QDxgiHdrInfo12isHdrCapableEP7QWindow(
    QDxgiHdrInfo *self,
    QWindow *w) {
  return self->isHdrCapable(w);
}

//  QRhiSwapChainHdrInfo QDxgiHdrInfo::queryHdrInfo(QWindow *w)
extern "C" Q_DECL_EXPORT
QRhiSwapChainHdrInfo *ritual_ZN12QDxgiHdrInfo12queryHdrInfoEP7QWindow(
    QDxgiHdrInfo *self,
    QWindow *w) {
  return new QRhiSwapChainHdrInfo(self->queryHdrInfo(w));
}

//  bool QDxgiHdrInfo::output6ForWindow(QWindow *w, IDXGIAdapter1 *adapter,
//      IDXGIOutput6 **result)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QDxgiHdrInfo16output6ForWindowEP7QWindowP13IDXGIAdapter1PP12IDXGIOutput6(
    QWindow *w,
    IDXGIAdapter1 *adapter,
    IDXGIOutput6 **result) {
  return QDxgiHdrInfo::output6ForWindow(w, adapter, result);
}

//  bool QDxgiHdrInfo::outputDesc1ForWindow(QWindow *w, IDXGIAdapter1
//      *adapter, DXGI_OUTPUT_DESC1 *result)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QDxgiHdrInfo20outputDesc1ForWindowEP7QWindowP13IDXGIAdapter1P17DXGI_OUTPUT_DESC1(
    QWindow *w,
    IDXGIAdapter1 *adapter,
    DXGI_OUTPUT_DESC1 *result) {
  return QDxgiHdrInfo::outputDesc1ForWindow(w, adapter, result);
}

//  float QDxgiHdrInfo::sdrWhiteLevelInNits(const DXGI_OUTPUT_DESC1
//      &outputDesc)
extern "C" Q_DECL_EXPORT
float ritual_ZN12QDxgiHdrInfo19sdrWhiteLevelInNitsERK17DXGI_OUTPUT_DESC1(
    const DXGI_OUTPUT_DESC1 *outputDesc) {
  return QDxgiHdrInfo::sdrWhiteLevelInNits(*outputDesc);
}

#endif  // defined(Q_OS_WIN)
