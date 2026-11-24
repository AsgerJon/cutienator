//  Written by dev_tooling.RitualGenerator from the records of QtQuickDialogs
//  2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfiledialogimpl_p
//  _p.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickDialogs2QuickImpl/qtquickdialogs2quickimplexports.h>
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#if QT_CONFIG(quick_listview) && QT_CONFIG(quick_draganddrop)
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#include <QtQuickDialogs2QuickImpl/QtQuickDialogs2QuickImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfiledialogimpl_p.h>
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfiledialogimpl_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qquickfiledialogimpl_p.h"
#include "qquickfiledialogimpl_p_p.h"
#include <QtCore/qloggingcategory.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/qpa/qplatformtheme.h>
#include <QtQml/qqmlinfo.h>
#include <QtQml/qqmlfile.h>
#if QT_CONFIG(accessibility)
#include <QtQuick/private/qquickaccessibleattached_p.h>
#endif
#include <QtQuick/private/qquickitemview_p_p.h>
#include <QtQuickTemplates2/private/qquickdialogbuttonbox_p_p.h>
#include <QtQuickTemplates2/private/qquickpopupitem_p_p.h>
#include <QtQuickControls2Impl/private/qquickplatformtheme_p.h>
#include <QtQuickDialogs2Utils/private/qquickfilenamefilter_p.h>
#include "qquickfiledialogdelegate_p.h"
#include "qquickfolderbreadcrumbbar_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quickdialogs/quickdialogsquickimpl/qquickfiledialogimpl.cpp, line 636, as _ZN35QQuickFileDialogImplAttachedPrivate20fileNameEditedByUserEv
inline void QQuickFileDialogImplAttachedPrivate::fileNameEditedByUser()
{
    if (!buttonBox)
        return;
    auto openButton = buttonBox->standardButton(QPlatformDialogHelper::Open);
    if (!openButton || !fileNameTextField)
        return;
    openButton->setEnabled(!fileNameTextField->text().isEmpty());
}

//  from ../qtdeclarative/src/quickdialogs/quickdialogsquickimpl/qquickfiledialogimpl.cpp, line 646, as _ZN35QQuickFileDialogImplAttachedPrivate29fileNameEditingByUserFinishedEv
inline void QQuickFileDialogImplAttachedPrivate::fileNameEditingByUserFinished()
{
    auto fileDialogImpl = qobject_cast<QQuickFileDialogImpl *>(parent);
    if (!fileDialogImpl)
        return;

    fileDialogImpl->setFileName(fileNameTextField->text());
}
//  -----------------------------------------------------------------------

//  void QQuickFileDialogImplAttachedPrivate::fileNameEditedByUser()
extern "C" Q_DECL_EXPORT
void ritual_ZN35QQuickFileDialogImplAttachedPrivate20fileNameEditedByUserEv(
    QQuickFileDialogImplAttachedPrivate *self) {
  self->fileNameEditedByUser();
}

//  void QQuickFileDialogImplAttachedPrivate::fileNameEditingByUserFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN35QQuickFileDialogImplAttachedPrivate29fileNameEditingByUserFinishedEv(
    QQuickFileDialogImplAttachedPrivate *self) {
  self->fileNameEditingByUserFinished();
}

//  QQuickFileDialogImplAttached
//      *QQuickFileDialogImplAttachedPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickFileDialogImplAttached *ritual_ZN35QQuickFileDialogImplAttachedPrivate6q_funcEv(
    QQuickFileDialogImplAttachedPrivate *self) {
  return self->q_func();
}

//  const QQuickFileDialogImplAttached
//      *QQuickFileDialogImplAttachedPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickFileDialogImplAttached *ritual_ZNK35QQuickFileDialogImplAttachedPrivate6q_funcEv(
    const QQuickFileDialogImplAttachedPrivate *self) {
  return self->q_func();
}

#endif  // QT_CONFIG(quick_listview) && QT_CONFIG(quick_draganddrop)
