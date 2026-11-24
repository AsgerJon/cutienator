//  Written by dev_tooling.RitualGenerator from the records of
//  QtLabsPlatform/6.12.0/QtLabsPlatform/private/qwidgetplatformdialog_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtLabsPlatform/qtlabsplatformexports.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if (1) && (QT_CONFIG(colordialog) || QT_CONFIG(filedialog) || QT_CONFIG(fontdialog) || QT_CONFIG(messagebox))
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtLabsPlatform/QtLabsPlatform>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsPlatform/6.12.0/QtLabsPlatform/private/qwidgetplatformdialog_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLabsPlatform/private/qwidgetplatformdialog_p.h>
#include <QtGui/qwindow.h>
#include <QtWidgets/qdialog.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/labs/platform/widgets/qwidgetplatformdialog.cpp, line 11, as _ZN21QWidgetPlatformDialog4showEP7QDialog6QFlagsIN2Qt10WindowTypeEENS3_14WindowModalityEP7QWindow
inline bool QWidgetPlatformDialog::show(QDialog *dialog, Qt::WindowFlags flags, Qt::WindowModality modality, QWindow *parent)
{
    dialog->setWindowFlags(flags);
    dialog->setWindowModality(modality);

    dialog->createWinId();
    QWindow *handle = dialog->windowHandle();
    Q_ASSERT(handle);
    handle->setTransientParent(const_cast<QWindow *>(parent));

    dialog->show();
    return true;
}
//  -----------------------------------------------------------------------

//  bool QWidgetPlatformDialog::show(QDialog *dialog, Qt::WindowFlags flags,
//      Qt::WindowModality modality, QWindow *parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QWidgetPlatformDialog4showEP7QDialog6QFlagsIN2Qt10WindowTypeEENS3_14WindowModalityEP7QWindow(
    QDialog *dialog,
    int flags,
    Qt::WindowModality modality,
    QWindow *parent) {
  return QWidgetPlatformDialog::show(
      dialog,
      QFlags<Qt::WindowType>::fromInt(flags),
      modality,
      parent);
}

//  QWidgetPlatformDialog::~QWidgetPlatformDialog()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QWidgetPlatformDialogD1Ev(QWidgetPlatformDialog *self) {
  delete self;
}

#endif  // (1) && (QT_CONFIG(colordialog) || QT_CONFIG(filedialog) || QT_CONFIG(fontdialog) || QT_CONFIG(messagebox))
