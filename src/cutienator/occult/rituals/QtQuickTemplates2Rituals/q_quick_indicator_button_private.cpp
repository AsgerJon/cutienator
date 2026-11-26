//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquickindicatorbutton_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickindicatorbutton_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/private/qquickindicatorbutton_p.h>
#include <QtQuickTemplates2/private/qquickdeferredexecute_p_p.h>
#include <QtQuickTemplates2/private/qquickcontrol_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quicktemplates/qquickindicatorbutton_p.cpp, line 12, as _ZN28QQuickIndicatorButtonPrivate15cancelIndicatorEv
inline void QQuickIndicatorButtonPrivate::cancelIndicator()
{
    Q_Q(QQuickIndicatorButton);
    quickCancelDeferred(q, indicatorName());
}

//  from ../qtdeclarative/src/quicktemplates/qquickindicatorbutton_p.cpp, line 18, as _ZN28QQuickIndicatorButtonPrivate16executeIndicatorEb
inline void QQuickIndicatorButtonPrivate::executeIndicator(bool complete)
{
    Q_Q(QQuickIndicatorButton);
    if (indicator.wasExecuted())
        return;

    if (!indicator || complete)
        quickBeginDeferred(q, indicatorName(), indicator);
    if (complete)
        quickCompleteDeferred(q, indicatorName(), indicator);
}
//  -----------------------------------------------------------------------

//  QQuickIndicatorButton *QQuickIndicatorButtonPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickIndicatorButton *ritual_ZN28QQuickIndicatorButtonPrivate6q_funcEv(
    QQuickIndicatorButtonPrivate *self) {
  return self->q_func();
}

//  const QQuickIndicatorButton *QQuickIndicatorButtonPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickIndicatorButton *ritual_ZNK28QQuickIndicatorButtonPrivate6q_funcEv(
    const QQuickIndicatorButtonPrivate *self) {
  return self->q_func();
}

//  QQuickIndicatorButtonPrivate
//      *QQuickIndicatorButtonPrivate::get(QQuickIndicatorButton *button)
extern "C" Q_DECL_EXPORT
QQuickIndicatorButtonPrivate *ritual_ZN28QQuickIndicatorButtonPrivate3getEP21QQuickIndicatorButton(
    QQuickIndicatorButton *button) {
  return QQuickIndicatorButtonPrivate::get(button);
}

//  void QQuickIndicatorButtonPrivate::cancelIndicator()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickIndicatorButtonPrivate15cancelIndicatorEv(
    QQuickIndicatorButtonPrivate *self) {
  self->cancelIndicator();
}

//  void QQuickIndicatorButtonPrivate::executeIndicator(bool complete)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QQuickIndicatorButtonPrivate16executeIndicatorEb(
    QQuickIndicatorButtonPrivate *self,
    bool complete) {
  self->executeIndicator(complete);
}
