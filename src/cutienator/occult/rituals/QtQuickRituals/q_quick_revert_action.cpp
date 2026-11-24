//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickstate_p_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickstate_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/QtQml>
#include <QtQml/qqmlproperty.h>

//  QQuickRevertAction::QQuickRevertAction()
extern "C" Q_DECL_EXPORT
QQuickRevertAction *ritual_ZN18QQuickRevertActionC1Ev() {
  return new QQuickRevertAction();
}

//  QQuickRevertAction::QQuickRevertAction(const QQmlProperty &prop)
extern "C" Q_DECL_EXPORT
QQuickRevertAction *ritual_ZN18QQuickRevertActionC1ERK12QQmlProperty(
    const QQmlProperty *prop) {
  return new QQuickRevertAction(*prop);
}

//  QQuickRevertAction::QQuickRevertAction(QQuickStateActionEvent *e)
extern "C" Q_DECL_EXPORT
QQuickRevertAction *ritual_ZN18QQuickRevertActionC1EP22QQuickStateActionEvent(
    QQuickStateActionEvent *e) {
  return new QQuickRevertAction(e);
}

//  QQuickRevertAction::~QQuickRevertAction()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickRevertActionD1Ev(QQuickRevertAction *self) {
  delete self;
}
