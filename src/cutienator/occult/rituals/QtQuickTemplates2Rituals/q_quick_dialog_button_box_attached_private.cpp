//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquickdialogbuttonbox_p_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuickTemplates2/qtquicktemplates2exports.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(quicktemplates2_container)
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(quicktemplates2_container)
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickdialogbuttonbox_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#endif
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickdialogbuttonbox_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/private/qquickdialogbuttonbox_p.h>
#include <QtQuickTemplates2/private/qquickdialogbuttonbox_p_p.h>
#include <QtQuickTemplates2/private/qquickabstractbutton_p.h>
#include <QtQuickTemplates2/private/qquickbutton_p.h>
#include <QtQuickTemplates2/private/qquickdialog_p_p.h>
#include <QtCore/qpointer.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/qpa/qplatformtheme.h>
#include <QtQml/qqmlengine.h>
#include <QtQml/qqmlcontext.h>
#include <QtQml/qqmlcomponent.h>
#if QT_CONFIG(accessibility)
#include <QtQuick/private/qquickaccessibleattached_p.h>
#endif
#include <QtQuick/private/qquickitemview_p.h>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quicktemplates/qquickdialogbuttonbox.cpp, line 933, as _ZN36QQuickDialogButtonBoxAttachedPrivate12setButtonBoxEP21QQuickDialogButtonBox
inline void QQuickDialogButtonBoxAttachedPrivate::setButtonBox(QQuickDialogButtonBox *box)
{
    Q_Q(QQuickDialogButtonBoxAttached);
    if (buttonBox == box)
        return;

    buttonBox = box;
    emit q->buttonBoxChanged();
}
//  -----------------------------------------------------------------------

//  QQuickDialogButtonBoxAttached
//      *QQuickDialogButtonBoxAttachedPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickDialogButtonBoxAttached *ritual_ZN36QQuickDialogButtonBoxAttachedPrivate6q_funcEv(
    QQuickDialogButtonBoxAttachedPrivate *self) {
  return self->q_func();
}

//  const QQuickDialogButtonBoxAttached
//      *QQuickDialogButtonBoxAttachedPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickDialogButtonBoxAttached *ritual_ZNK36QQuickDialogButtonBoxAttachedPrivate6q_funcEv(
    const QQuickDialogButtonBoxAttachedPrivate *self) {
  return self->q_func();
}

//  QQuickDialogButtonBoxAttachedPrivate
//      *QQuickDialogButtonBoxAttachedPrivate::get(QQuickDialogButtonBoxAttac
//      hed *q)
extern "C" Q_DECL_EXPORT
QQuickDialogButtonBoxAttachedPrivate *ritual_ZN36QQuickDialogButtonBoxAttachedPrivate3getEP29QQuickDialogButtonBoxAttached(
    QQuickDialogButtonBoxAttached *q) {
  return QQuickDialogButtonBoxAttachedPrivate::get(q);
}

//  void
//      QQuickDialogButtonBoxAttachedPrivate::setButtonBox(QQuickDialogButton
//      Box *box)
extern "C" Q_DECL_EXPORT
void ritual_ZN36QQuickDialogButtonBoxAttachedPrivate12setButtonBoxEP21QQuickDialogButtonBox(
    QQuickDialogButtonBoxAttachedPrivate *self,
    QQuickDialogButtonBox *box) {
  self->setButtonBox(box);
}

#endif  // QT_CONFIG(quicktemplates2_container)
