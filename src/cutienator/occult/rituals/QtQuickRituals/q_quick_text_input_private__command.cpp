//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktextinput_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicktextinput_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qchar.h>

//  QQuickTextInputPrivate::Command::Command()
extern "C" Q_DECL_EXPORT
QQuickTextInputPrivate::Command *ritual_ZN22QQuickTextInputPrivate7CommandC1Ev() {
  return new QQuickTextInputPrivate::Command();
}

//  QQuickTextInputPrivate::Command::Command(CommandType t, int p, QChar c,
//      int ss, int se)
extern "C" Q_DECL_EXPORT
QQuickTextInputPrivate::Command *ritual_ZN22QQuickTextInputPrivate7CommandC1ENS_11CommandTypeEi5QCharii(
    QQuickTextInputPrivate::CommandType t,
    int p,
    const QChar *c,
    int ss,
    int se) {
  return new QQuickTextInputPrivate::Command(t, p, *c, ss, se);
}

//  QQuickTextInputPrivate::Command::~Command()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickTextInputPrivate7CommandD1Ev(
    QQuickTextInputPrivate::Command *self) {
  delete self;
}
