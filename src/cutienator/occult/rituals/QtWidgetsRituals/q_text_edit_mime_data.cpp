//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qwidgettextcontrol_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/QtWidgets>
#include <QtWidgets/6.12.0/QtWidgets/private/qwidgettextcontrol_p.h>
#include <QtCore/qstring.h>
#include <QtCore/qmetatype.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>
#include "qwidgettextcontrol_p.h"
#include "qwidgettextcontrol_p_p.h"
#ifndef QT_NO_TEXTCONTROL
#include <qfont.h>
#include <qpainter.h>
#include <qevent.h>
#include <qdebug.h>
#if QT_CONFIG(draganddrop)
#include <qdrag.h>
#endif
#include <qclipboard.h>
#include <qstyle.h>
#include "private/qapplication_p.h"
#include "private/qtextdocumentlayout_p.h"
#include "private/qabstracttextdocumentlayout_p.h"
#if QT_CONFIG(menu)
#include "private/qmenu_p.h"
#endif
#include "qtextdocument.h"
#include "private/qtextdocument_p.h"
#include "private/qtextdocumentfragment_p.h"
#include "qtextlist.h"
#include "private/qwidgettextcontrol_p.h"
#if QT_CONFIG(style_stylesheet)
#  include "private/qstylesheetstyle_p.h"
#endif
#if QT_CONFIG(graphicsview)
#include "qgraphicssceneevent.h"
#endif
#include "qpagedpaintdevice.h"
#include "private/qpagedpaintdevice_p.h"
#include "qtextdocumentwriter.h"
#include "qstylehints.h"
#include "private/qtextcursor_p.h"
#include <qtextformat.h>
#include <qdatetime.h>
#include <qbuffer.h>
#include <qapplication.h>
#include <limits.h>
#include <qtexttable.h>
#include <qvariant.h>
#include <qurl.h>
#include <qdesktopservices.h>
#include <qinputmethod.h>
#if QT_CONFIG(tooltip)
#include <qtooltip.h>
#endif
#include <qstyleoption.h>
#if QT_CONFIG(lineedit)
#include <QtWidgets/qlineedit.h>
#endif
#include <QtGui/qaccessible.h>
#include <QtCore/qmetaobject.h>
#ifdef Q_OS_WASM
#include <QtCore/private/qstdweb_p.h>
#endif
#include <private/qoffsetstringarray_p.h>
#if QT_CONFIG(shortcut)
#include "private/qapplication_p.h"
#include "private/qshortcutmap_p.h"
#include <qkeysequence.h>
#else
#endif
#include <algorithm>
#endif

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it.

//  from src/widgets/widgets/qwidgettextcontrol.cpp, line 3503, as _ZNK17QTextEditMimeData12retrieveDataERK7QString9QMetaType
inline QVariant QTextEditMimeData::retrieveData(const QString &mimeType, QMetaType type) const
{
    if (!fragment.isEmpty())
        setup();
    return QMimeData::retrieveData(mimeType, type);
}
//  -----------------------------------------------------------------------

//  QStringList QTextEditMimeData::formats() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK17QTextEditMimeData7formatsEv(
    const QTextEditMimeData *self) {
  return new QList<QString>(self->formats());
}

//  QVariant QTextEditMimeData::retrieveData(const QString &mimeType,
//      QMetaType type) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK17QTextEditMimeData12retrieveDataERK7QString9QMetaType(
    const QTextEditMimeData *self,
    const QString *mimeType,
    const QMetaType *type) {
  return new QVariant(self->retrieveData(*mimeType, *type));
}
