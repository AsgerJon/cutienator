//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qscreen_platform.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if QT_CONFIG(wayland) || defined(Q_QDOC)
#include <QtGui/qscreen.h>

//  QNativeInterface::QWaylandScreen::~QWaylandScreen()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNativeInterface14QWaylandScreenD1Ev(
    QNativeInterface::QWaylandScreen *self) {
  delete self;
}

#endif  // QT_CONFIG(wayland) || defined(Q_QDOC)
