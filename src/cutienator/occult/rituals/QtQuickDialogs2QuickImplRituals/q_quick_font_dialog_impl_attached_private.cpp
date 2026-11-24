//  Written by dev_tooling.RitualGenerator from the records of QtQuickDialogs
//  2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfontdialogimpl_p
//  _p.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuickDialogs2QuickImpl/qtquickdialogs2quickimplexports.h>
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#if QT_CONFIG(quick_listview) && QT_CONFIG(quick_draganddrop)
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qtquickdialogs2quickimplglobal_p.h>
#include <QtQuickDialogs2QuickImpl/QtQuickDialogs2QuickImpl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfontdialogimpl_p.h>
#include <QtQuickDialogs2QuickImpl/6.12.0/QtQuickDialogs2QuickImpl/private/qquickfontdialogimpl_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qfont.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickDialogs2QuickImpl/private/qquickfontdialogimpl_p.h>
#include <QtQuickDialogs2QuickImpl/private/qquickfontdialogimpl_p_p.h>
#include <QtQuickTemplates2/private/qquickdialogbuttonbox_p_p.h>
#include <QtGui/private/qfontdatabase_p.h>
#include <QtCore/QRegularExpression>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quickdialogs/quickdialogsquickimpl/qquickfontdialogimpl.cpp, line 822, as _ZN35QQuickFontDialogImplAttachedPrivate18currentFontChangedERK5QFont
inline void QQuickFontDialogImplAttachedPrivate::currentFontChanged(const QFont &font)
{
    auto fontDialogImpl = qobject_cast<QQuickFontDialogImpl *>(parent);

    if (!fontDialogImpl) {
        return;
    }

    fontDialogImpl->setCurrentFont(font);
}
//  -----------------------------------------------------------------------

//  void QQuickFontDialogImplAttachedPrivate::currentFontChanged(const QFont
//      &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN35QQuickFontDialogImplAttachedPrivate18currentFontChangedERK5QFont(
    QQuickFontDialogImplAttachedPrivate *self,
    const QFont *font) {
  self->currentFontChanged(*font);
}

//  QQuickFontDialogImplAttached
//      *QQuickFontDialogImplAttachedPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickFontDialogImplAttached *ritual_ZN35QQuickFontDialogImplAttachedPrivate6q_funcEv(
    QQuickFontDialogImplAttachedPrivate *self) {
  return self->q_func();
}

//  const QQuickFontDialogImplAttached
//      *QQuickFontDialogImplAttachedPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickFontDialogImplAttached *ritual_ZNK35QQuickFontDialogImplAttachedPrivate6q_funcEv(
    const QQuickFontDialogImplAttachedPrivate *self) {
  return self->q_func();
}

#endif  // QT_CONFIG(quick_listview) && QT_CONFIG(quick_draganddrop)
