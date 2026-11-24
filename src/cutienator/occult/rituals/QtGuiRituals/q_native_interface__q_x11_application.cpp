//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qguiapplication_platform.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#if QT_CONFIG(xcb) || defined(Q_QDOC)
#include <QtGui/qguiapplication.h>

//  QNativeInterface::QX11Application::~QX11Application()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNativeInterface15QX11ApplicationD1Ev(
    QNativeInterface::QX11Application *self) {
  delete self;
}

#endif  // QT_CONFIG(xcb) || defined(Q_QDOC)
