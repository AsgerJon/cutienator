//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qwidgettextcontrol_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(widgettextcontrol)
#if QT_CONFIG(widgettextcontrol)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qwidgettextcontrol_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetatype.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/private/qwidgettextcontrol_p.h>
#include <QtWidgets/private/qwidgettextcontrol_p_p.h>
#ifndef QT_NO_TEXTCONTROL
#include <QtGui/qfont.h>
#include <QtGui/qpainter.h>
#include <QtGui/qevent.h>
#include <QtCore/qdebug.h>
#if QT_CONFIG(draganddrop)
#include <QtGui/qdrag.h>
#endif
#include <QtGui/qclipboard.h>
#include <QtWidgets/qstyle.h>
#include <QtWidgets/private/qapplication_p.h>
#include <QtGui/private/qtextdocumentlayout_p.h>
#include <QtGui/private/qabstracttextdocumentlayout_p.h>
#if QT_CONFIG(menu)
#include <QtWidgets/private/qmenu_p.h>
#endif
#include <QtGui/qtextdocument.h>
#include <QtGui/private/qtextdocument_p.h>
#include <QtGui/private/qtextdocumentfragment_p.h>
#include <QtGui/qtextlist.h>
#include <QtWidgets/private/qwidgettextcontrol_p.h>
#if QT_CONFIG(style_stylesheet)
#  include <QtWidgets/private/qstylesheetstyle_p.h>
#endif
#if QT_CONFIG(graphicsview)
#include <QtWidgets/qgraphicssceneevent.h>
#endif
#include <QtGui/qpagedpaintdevice.h>
#include <QtGui/private/qpagedpaintdevice_p.h>
#include <QtGui/qtextdocumentwriter.h>
#include <QtGui/qstylehints.h>
#include <QtGui/private/qtextcursor_p.h>
#include <QtGui/qtextformat.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qbuffer.h>
#include <QtWidgets/qapplication.h>
#include <limits.h>
#include <QtGui/qtexttable.h>
#include <QtCore/qvariant.h>
#include <QtCore/qurl.h>
#include <QtGui/qdesktopservices.h>
#include <QtGui/qinputmethod.h>
#if QT_CONFIG(tooltip)
#include <QtWidgets/qtooltip.h>
#endif
#include <QtWidgets/qstyleoption.h>
#if QT_CONFIG(lineedit)
#include <QtWidgets/qlineedit.h>
#endif
#include <QtGui/qaccessible.h>
#include <QtCore/qmetaobject.h>
#ifdef Q_OS_WASM
#include <QtCore/private/qstdweb_p.h>
#endif
#include <QtCore/private/qoffsetstringarray_p.h>
#if QT_CONFIG(shortcut)
#include <QtWidgets/private/qapplication_p.h>
#include <QtGui/private/qshortcutmap_p.h>
#include <QtGui/qkeysequence.h>
#else
#endif
#include <algorithm>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/widgets/widgets/qwidgettextcontrol.cpp, line 3457, as local:qwidgettextcontrol.cpp:supportedMimeTypes
#if !defined(QT_NO_TEXTCONTROL)
static constexpr auto supportedMimeTypes = qOffsetStringArray(
    "text/plain",
    "text/html"
#if QT_CONFIG(textmarkdownwriter)
    , "text/markdown"
#endif
#if QT_CONFIG(textodfwriter)
    , "application/vnd.oasis.opendocument.text"
#endif
);
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from src/widgets/widgets/qwidgettextcontrol.cpp, line 3503, as _ZNK17QTextEditMimeData12retrieveDataERK7QString9QMetaType
#if !defined(QT_NO_TEXTCONTROL)
inline QVariant QTextEditMimeData::retrieveData(const QString &mimeType, QMetaType type) const
{
    if (!fragment.isEmpty())
        setup();
    return QMimeData::retrieveData(mimeType, type);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from src/widgets/widgets/qwidgettextcontrol.cpp, line 3510, as _ZNK17QTextEditMimeData5setupEv
#if !defined(QT_NO_TEXTCONTROL)
inline void QTextEditMimeData::setup() const
{
    QTextEditMimeData *that = const_cast<QTextEditMimeData *>(this);
#ifndef QT_NO_TEXTHTMLPARSER
    that->setData("text/html"_L1, fragment.toHtml().toUtf8());
#endif
#if QT_CONFIG(textmarkdownwriter)
    that->setData("text/markdown"_L1, fragment.toMarkdown().toUtf8());
#endif
#ifndef QT_NO_TEXTODFWRITER
    {
        QBuffer buffer;
        QTextDocumentWriter writer(&buffer, "ODF");
        writer.write(fragment);
        buffer.close();
        that->setData("application/vnd.oasis.opendocument.text"_L1, buffer.data());
    }
#endif
    that->setText(fragment.toPlainText());
    fragment = QTextDocumentFragment();
}
#endif  // !defined(QT_NO_TEXTCONTROL)
//  -----------------------------------------------------------------------

//  Only a class built on QTextEditMimeData may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQTextEditMimeData : QTextEditMimeData {
  using QTextEditMimeData::retrieveData;
};

//  QStringList QTextEditMimeData::formats() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK17QTextEditMimeData7formatsEv(
    const QTextEditMimeData *self) {
  return new QList<QString>(self->formats());
}

//  bool QTextEditMimeData::hasFormat(const QString &format) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QTextEditMimeData9hasFormatERK7QString(
    const QTextEditMimeData *self,
    const QString *format) {
  return self->hasFormat(*format);
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

#if !defined(QT_NO_TEXTCONTROL)
//  void QTextEditMimeData::setup() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK17QTextEditMimeData5setupEv(const QTextEditMimeData *self) {
  self->setup();
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  QVariant QTextEditMimeData::retrieveData(const QString &mimeType,
//      QMetaType type) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK17QTextEditMimeData12retrieveDataERK7QString9QMetaType(
    const QTextEditMimeData *self,
    const QString *mimeType,
    const QMetaType *type) {
  return new QVariant(
      static_cast<const OwnQTextEditMimeData *>(self)->OwnQTextEditMimeData::retrieveData(
          *mimeType,
          *type));
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#endif  // QT_CONFIG(widgettextcontrol)
#endif  // QT_CONFIG(widgettextcontrol)
