//  Written by hand on 2026-11-25 from
//  QtPrintSupport/6.12.0/QtPrintSupport/private/qpaintengine_mac_p.h, Qt
//  6.12.0, as the Qt of macOS installs it. Kept as it is when the
//  generator runs again.
//  Its header names CoreGraphics' types without including
//  CoreGraphics, as Qt's own sources include it first; so does this
//  file.
//  Qt's library offers nothing of this class by name: only its
//  virtual functions are called, through the object, and what its
//  header writes out.
//  Not written: 'drawPath', 'setClip', 'resetClip', 'setFillBrush',
//  'setStrokePen', 'penOffset', 'devicePixelSize' and
//  'adjustPenWidth', which Qt's library offers not, and
//  'saveGraphicsState', 'restoreGraphicsState' and 'setTransform',
//  which the header writes out over CoreGraphics, a library outside
//  Qt.
#include <QtPrintSupport/qtprintsupportglobal.h>
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qtprintsupportglobal_p.h>
#if defined(Q_OS_MACOS)
#include <ApplicationServices/ApplicationServices.h>
#include <QtPrintSupport/6.12.0/QtPrintSupport/private/qpaintengine_mac_p.h>

//  QCoreGraphicsPaintEnginePrivate::QCoreGraphicsPaintEnginePrivate()
extern "C" Q_DECL_EXPORT
QCoreGraphicsPaintEnginePrivate *ritual_ZN31QCoreGraphicsPaintEnginePrivateC1Ev() {
  return new QCoreGraphicsPaintEnginePrivate();
}

//  QCoreGraphicsPaintEnginePrivate::~QCoreGraphicsPaintEnginePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QCoreGraphicsPaintEnginePrivateD1Ev(
    QCoreGraphicsPaintEnginePrivate *self) {
  delete self;
}

//  QCoreGraphicsPaintEngine *QCoreGraphicsPaintEnginePrivate::q_func()
extern "C" Q_DECL_EXPORT
QCoreGraphicsPaintEngine *ritual_ZN31QCoreGraphicsPaintEnginePrivate6q_funcEv(
    QCoreGraphicsPaintEnginePrivate *self) {
  return self->q_func();
}

//  const QCoreGraphicsPaintEngine *QCoreGraphicsPaintEnginePrivate::q_func()
//      const
extern "C" Q_DECL_EXPORT
const QCoreGraphicsPaintEngine *ritual_ZNK31QCoreGraphicsPaintEnginePrivate6q_funcEv(
    const QCoreGraphicsPaintEnginePrivate *self) {
  return self->q_func();
}

#endif  // defined(Q_OS_MACOS)
