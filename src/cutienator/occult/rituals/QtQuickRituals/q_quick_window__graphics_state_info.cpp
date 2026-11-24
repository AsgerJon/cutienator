//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qquickwindow.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/QtQuick>
#include <QtQuick/qquickwindow.h>

//  QQuickWindow::GraphicsStateInfo::~GraphicsStateInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QQuickWindow17GraphicsStateInfoD1Ev(
    QQuickWindow::GraphicsStateInfo *self) {
  delete self;
}
