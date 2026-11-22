//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qaccessible.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qaccessible.h>
#include <QtGui/QtGui>
#include <QtGui/qtestsupport_gui.h>
#include <QtGui/qvulkanfunctions.h>
#include <QtGui/qvulkaninstance.h>
#include <QtGui/qvulkanwindow.h>

//  QAccessibleStateChangeEvent::QAccessibleStateChangeEvent(QObject *obj,
//      QAccessible::State state)
extern "C" Q_DECL_EXPORT
QAccessibleStateChangeEvent *ritual_ZN27QAccessibleStateChangeEventC1EP7QObjectN11QAccessible5StateE(
    QObject *obj,
    const QAccessible::State *state) {
  return new QAccessibleStateChangeEvent(obj, *state);
}

//  QAccessibleStateChangeEvent::QAccessibleStateChangeEvent(QAccessibleInter
//      face *iface, QAccessible::State state)
extern "C" Q_DECL_EXPORT
QAccessibleStateChangeEvent *ritual_ZN27QAccessibleStateChangeEventC1EP20QAccessibleInterfaceN11QAccessible5StateE(
    QAccessibleInterface *iface,
    const QAccessible::State *state) {
  return new QAccessibleStateChangeEvent(iface, *state);
}

//  QAccessibleStateChangeEvent::~QAccessibleStateChangeEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QAccessibleStateChangeEventD1Ev(
    QAccessibleStateChangeEvent *self) {
  delete self;
}

//  QAccessible::State QAccessibleStateChangeEvent::changedStates() const
extern "C" Q_DECL_EXPORT
QAccessible::State *ritual_ZNK27QAccessibleStateChangeEvent13changedStatesEv(
    const QAccessibleStateChangeEvent *self) {
  return new QAccessible::State(self->changedStates());
}
