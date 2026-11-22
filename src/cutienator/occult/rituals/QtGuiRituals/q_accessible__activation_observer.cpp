//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessible_base.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/QtGui>
#include <QtGui/qtestsupport_gui.h>
#include <QtGui/qvulkanfunctions.h>
#include <QtGui/qvulkaninstance.h>
#include <QtGui/qvulkanwindow.h>

//  QAccessible::ActivationObserver::~ActivationObserver()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAccessible18ActivationObserverD1Ev(
    QAccessible::ActivationObserver *self) {
  delete self;
}

//  void QAccessible::ActivationObserver::accessibilityActiveChanged(bool
//      active)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QAccessible18ActivationObserver26accessibilityActiveChangedEb(
    QAccessible::ActivationObserver *self,
    bool active) {
  self->accessibilityActiveChanged(active);
}
