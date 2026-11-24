//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qtextdocument_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtextdocument_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qtextdocument.h>
#include <QtGui/qtextformat.h>
#include <QtGui/private/qtextcursor_p.h>
#include <QtGui/private/qtextdocument_p.h>
#include <QtGui/private/qtextdocumentlayout_p.h>
#include <QtGui/qtextdocumentfragment.h>
#include <QtGui/private/qtextdocumentfragment_p.h>
#include <QtGui/qtexttable.h>
#include <QtGui/qtextlist.h>
#include <QtCore/qdebug.h>
#include <QtCore/qloggingcategory.h>
#if QT_CONFIG(regularexpression)
#include <QtCore/qregularexpression.h>
#endif
#include <QtCore/qvarlengtharray.h>
#include <QtCore/qthread.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/qmetaobject.h>
#include <QtGui/private/qtexthtmlparser_p.h>
#include <QtGui/qpainter.h>
#include <QtCore/qfile.h>
#include <QtCore/qfileinfo.h>
#include <QtCore/qdir.h>
#include <QtGui/private/qfont_p.h>
#include <QtCore/private/qdataurl_p.h>
#include <QtGui/private/qtextdocument_p.h>
#include <QtGui/private/qabstracttextdocumentlayout_p.h>
#include <QtGui/qpagedpaintdevice.h>
#include <QtGui/private/qpagedpaintdevice_p.h>
#if QT_CONFIG(textmarkdownreader)
#include <QtGui/private/qtextmarkdownimporter_p.h>
#endif
#if QT_CONFIG(textmarkdownwriter)
#include <QtGui/private/qtextmarkdownwriter_p.h>
#endif
#include <limits.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/text/qtextdocument.cpp, line 2394, as _ZN17QTextHtmlExporterC1EPK13QTextDocument
inline QTextHtmlExporter::QTextHtmlExporter(const QTextDocument *_doc)
    : doc(_doc), fragmentMarkers(false)
{
    const QFont defaultFont = doc->defaultFont();
    defaultCharFormat.setFont(defaultFont);
}

//  from src/gui/text/qtextdocument.cpp, line 3385, as _ZN17QTextHtmlExporter15findUrlForImageEPK13QTextDocumentxb
inline QString QTextHtmlExporter::findUrlForImage(const QTextDocument *doc, qint64 cacheKey, bool isPixmap)
{
    QString url;
    if (!doc)
        return url;

    if (QTextDocument *parent = qobject_cast<QTextDocument *>(doc->parent()))
        return findUrlForImage(parent, cacheKey, isPixmap);

    const QTextDocumentPrivate *priv = QTextDocumentPrivate::get(doc);
    Q_ASSERT(priv != nullptr);

    QMap<QUrl, QVariant>::const_iterator it = priv->cachedResources.constBegin();
    for (; it != priv->cachedResources.constEnd(); ++it) {

        const QVariant &v = it.value();
        if (v.userType() == QMetaType::QImage && !isPixmap) {
            if (qvariant_cast<QImage>(v).cacheKey() == cacheKey)
                break;
        }

        if (v.userType() == QMetaType::QPixmap && isPixmap) {
            if (qvariant_cast<QPixmap>(v).cacheKey() == cacheKey)
                break;
        }
    }

    if (it != priv->cachedResources.constEnd())
        url = it.key().toString();

    return url;
}
//  -----------------------------------------------------------------------

//  QTextHtmlExporter::QTextHtmlExporter(const QTextDocument *_doc)
extern "C" Q_DECL_EXPORT
QTextHtmlExporter *ritual_ZN17QTextHtmlExporterC1EPK13QTextDocument(
    const QTextDocument *_doc) {
  return new QTextHtmlExporter(_doc);
}

//  QString QTextHtmlExporter::findUrlForImage(const QTextDocument *doc,
//      qint64 cacheKey, bool isPixmap)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QTextHtmlExporter15findUrlForImageEPK13QTextDocumentxb(
    QTextHtmlExporter *self,
    const QTextDocument *doc,
    qint64 cacheKey,
    bool isPixmap) {
  return new QString(self->findUrlForImage(doc, cacheKey, isPixmap));
}

//  QTextHtmlExporter::~QTextHtmlExporter()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QTextHtmlExporterD1Ev(QTextHtmlExporter *self) {
  delete self;
}
