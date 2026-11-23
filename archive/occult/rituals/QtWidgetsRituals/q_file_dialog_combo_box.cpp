//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qfiledialog_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/QtWidgets>
#include <QtWidgets/6.12.0/QtWidgets/private/qfiledialog_p.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#include <qvariant.h>
#include <private/qwidgetitemdata_p.h>
#include "qfiledialog.h"
#include "qfiledialog_p.h"
#include <private/qapplication_p.h>
#include <private/qguiapplication_p.h>
#include <qfontmetrics.h>
#include <qaction.h>
#include <qactiongroup.h>
#include <qheaderview.h>
#if QT_CONFIG(shortcut)
#  include <qshortcut.h>
#endif
#include <qgridlayout.h>
#if QT_CONFIG(menu)
#include <qmenu.h>
#endif
#if QT_CONFIG(messagebox)
#include <qmessagebox.h>
#endif
#include <stdlib.h>
#if QT_CONFIG(settings)
#include <qsettings.h>
#endif
#include <qdebug.h>
#if QT_CONFIG(mimetype)
#include <qmimedatabase.h>
#endif
#if QT_CONFIG(regularexpression)
#include <qregularexpression.h>
#endif
#include <qapplication.h>
#include <qstylepainter.h>
#if defined(Q_OS_UNIX)
#include <pwd.h>
#include <unistd.h> // for pathconf() on OS X
#elif defined(Q_OS_WIN)
#  include <QtCore/qt_windows.h>
#endif
#if defined(Q_OS_WASM)
#include <private/qwasmlocalfileaccess_p.h>
#endif
#include <algorithm>
#include <QMetaEnum>
#if QT_CONFIG(shortcut)
#  include <qshortcut.h>
#endif

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it.

//  from src/widgets/dialogs/qfiledialog.cpp, line 4097, as _ZN19QFileDialogComboBox10paintEventEP11QPaintEvent
inline void QFileDialogComboBox::paintEvent(QPaintEvent *)
{
    QStylePainter painter(this);
    painter.setPen(palette().color(QPalette::Text));

    // draw the combobox frame, focusrect and selected etc.
    QStyleOptionComboBox opt;
    initStyleOption(&opt);

    QRect editRect = style()->subControlRect(QStyle::CC_ComboBox, &opt,
                                                QStyle::SC_ComboBoxEditField, this);
    int size = editRect.width() - opt.iconSize.width() - 4;
    opt.currentText = opt.fontMetrics.elidedText(opt.currentText, Qt::ElideMiddle, size);
    painter.drawComplexControl(QStyle::CC_ComboBox, opt);

    // draw the icon and text
    painter.drawControl(QStyle::CE_ComboBoxLabel, opt);
}
//  -----------------------------------------------------------------------

//  QStringList QFileDialogComboBox::history() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK19QFileDialogComboBox7historyEv(
    const QFileDialogComboBox *self) {
  return new QList<QString>(self->history());
}

//  void QFileDialogComboBox::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QFileDialogComboBox10paintEventEP11QPaintEvent(
    QFileDialogComboBox *self,
    QPaintEvent *a0) {
  self->paintEvent(a0);
}

//  void QFileDialogComboBox::paintEvent(QPaintEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QFileDialogComboBox10paintEventEP11QPaintEvent(
    QFileDialogComboBox *self,
    QPaintEvent *a0) {
  self->QFileDialogComboBox::paintEvent(a0);
}
