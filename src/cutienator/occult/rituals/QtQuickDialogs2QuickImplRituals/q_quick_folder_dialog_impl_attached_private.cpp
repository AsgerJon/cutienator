//  Written by dev_tooling.RitualGenerator from the records of QtQuickDialogs
//  2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfolderdialogimpl
//  _p_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickDialogs2QuickImpl/qtquickdialogs2quickimplexports.h>
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#if QT_CONFIG(quick_listview) && QT_CONFIG(quick_draganddrop)
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#if QT_CONFIG(quick_listview) && QT_CONFIG(quick_draganddrop)
#include <QtQuickDialogs2QuickImpl/QtQuickDialogs2QuickImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfolderdialogimpl_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#endif
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfolderdialogimpl_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2QuickImpl/private/qquickfolderdialogimpl_p.h>
#include <QtQuickDialogs2QuickImpl/private/qquickfolderdialogimpl_p_p.h>
#include <QtCore/qloggingcategory.h>
#include <QtQuickTemplates2/private/qquickdialogbuttonbox_p_p.h>
#include <QtQuickDialogs2QuickImpl/private/qquickfiledialogdelegate_p.h>
#include <QtQuickDialogs2QuickImpl/private/qquickfolderbreadcrumbbar_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quickdialogs/quickdialogsquickimpl/qquickfolderdialogimpl.cpp, line 315, as _ZN37QQuickFolderDialogImplAttachedPrivate39folderDialogListViewCurrentIndexChangedEv
inline void QQuickFolderDialogImplAttachedPrivate::folderDialogListViewCurrentIndexChanged()
{
    auto folderDialogImpl = qobject_cast<QQuickFolderDialogImpl*>(parent);
    if (!folderDialogImpl)
        return;

    auto folderDialogDelegate = qobject_cast<QQuickFileDialogDelegate*>(folderDialogListView->currentItem());
    if (!folderDialogDelegate)
        return;

    folderDialogImpl->setSelectedFolder(folderDialogDelegate->file());
}
//  -----------------------------------------------------------------------

//  QQuickFolderDialogImplAttached
//      *QQuickFolderDialogImplAttachedPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickFolderDialogImplAttached *ritual_ZN37QQuickFolderDialogImplAttachedPrivate6q_funcEv(
    QQuickFolderDialogImplAttachedPrivate *self) {
  return self->q_func();
}

//  const QQuickFolderDialogImplAttached
//      *QQuickFolderDialogImplAttachedPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickFolderDialogImplAttached *ritual_ZNK37QQuickFolderDialogImplAttachedPrivate6q_funcEv(
    const QQuickFolderDialogImplAttachedPrivate *self) {
  return self->q_func();
}

//  void QQuickFolderDialogImplAttachedPrivate::folderDialogListViewCurrentIn
//      dexChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN37QQuickFolderDialogImplAttachedPrivate39folderDialogListViewCurrentIndexChangedEv(
    QQuickFolderDialogImplAttachedPrivate *self) {
  self->folderDialogListViewCurrentIndexChanged();
}

#endif  // QT_CONFIG(quick_listview) && QT_CONFIG(quick_draganddrop)
