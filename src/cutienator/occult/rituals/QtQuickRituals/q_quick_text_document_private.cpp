//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktextdocument_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquicktextdocument.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicktextdocument_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/qquicktextdocument.h>
#include <QtQuick/private/qquicktextdocument_p.h>
#include <QtQuick/private/qquicktextedit_p.h>
#include <QtQml/qqmlcontext.h>
#include <QtQml/qqmlfile.h>
#include <QtQml/qqmlinfo.h>
#include <QtQuick/private/qquickpixmap_p.h>
#include <QtCore/qfile.h>
#include <QtCore/qpointer.h>
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

//  from ../qtdeclarative/src/quick/items/qquicktextdocument.cpp, line 375, as _ZN25QQuickTextDocumentPrivate7writeToERK4QUrl
inline void QQuickTextDocumentPrivate::writeTo(const QUrl &fileUrl)
{
    auto *doc = editor->document();
    if (!doc)
        return;

    const QString filePath = QQmlFile::urlToLocalFileOrQrc(fileUrl);
    const bool sameUrl = fileUrl == url;
    if (!sameUrl) {
#if QT_CONFIG(mimetype)
        const auto type = QMimeDatabase().mimeTypeForUrl(fileUrl);
        if (type.inherits("text/html"_L1))
            detectedFormat = Qt::RichText;
        else if (type.inherits("text/markdown"_L1))
            detectedFormat = Qt::MarkdownText;
        else
            detectedFormat = Qt::PlainText;
#else
        if (filePath.endsWith(".html"_L1, Qt::CaseInsensitive) ||
            filePath.endsWith(".htm"_L1, Qt::CaseInsensitive))
            detectedFormat = Qt::RichText;
        else if (filePath.endsWith(".md"_L1, Qt::CaseInsensitive) ||
                 filePath.endsWith(".markdown"_L1, Qt::CaseInsensitive))
            detectedFormat = Qt::MarkdownText;
        else
            detectedFormat = Qt::PlainText;
#endif
    }
    QFile file(filePath);
    if (!file.open(QFile::WriteOnly | QFile::Truncate |
                   (detectedFormat == Qt::RichText ? QFile::NotOpen : QFile::Text))) {
        setStatus(QQuickTextDocument::Status::WriteError,
                  QQuickTextDocument::tr("Cannot save: %1").arg(file.errorString()));
        return;
    }
    setStatus(QQuickTextDocument::Status::Saving, {});
    QByteArray raw;

    switch (detectedFormat) {
#if QT_CONFIG(textmarkdownwriter)
    case Qt::MarkdownText:
        raw = doc->toMarkdown().toUtf8();
        break;
#endif
#if QT_CONFIG(texthtmlparser)
    case Qt::RichText:
        if (sameUrl && encoding) {
            QStringEncoder enc(*encoding);
            raw = enc.encode(doc->toHtml());
        } else {
            // default to UTF-8 unless the user is saving the same file as previously loaded
            raw = doc->toHtml().toUtf8();
        }
        break;
#endif
    default:
        raw = doc->toPlainText().toUtf8();
        break;
    }

    file.write(raw);
    file.close();
    setStatus(QQuickTextDocument::Status::Saved, {});
    doc->setModified(false);
}

//  from ../qtdeclarative/src/quick/items/qquicktextdocument.cpp, line 441, as _ZNK25QQuickTextDocumentPrivate8documentEv
inline QTextDocument *QQuickTextDocumentPrivate::document() const
{
    return editor->document();
}

//  from ../qtdeclarative/src/quick/items/qquicktextdocument.cpp, line 446, as _ZN25QQuickTextDocumentPrivate11setDocumentEP13QTextDocument
inline void QQuickTextDocumentPrivate::setDocument(QTextDocument *doc)
{
    Q_Q(QQuickTextDocument);
    QTextDocument *oldDoc = editor->document();
    if (doc == oldDoc)
        return;

    if (oldDoc)
        oldDoc->disconnect(q);
    if (doc) {
        q->connect(doc, &QTextDocument::modificationChanged,
                   q, &QQuickTextDocument::modifiedChanged);
    }
    editor->setDocument(doc);
    emit q->textDocumentChanged();
}

//  from ../qtdeclarative/src/quick/items/qquicktextdocument.cpp, line 176, as _ZN25QQuickTextDocumentPrivate9setStatusEN18QQuickTextDocument6StatusERK7QString
inline void QQuickTextDocumentPrivate::setStatus(QQuickTextDocument::Status s, const QString &err)
{
    Q_Q(QQuickTextDocument);
    if (status == s)
        return;

    status = s;
    emit q->statusChanged();

    if (errorString == err)
        return;
    errorString = err;
    emit q->errorStringChanged();
    if (!err.isEmpty())
        qmlWarning(q) << err;
}
//  -----------------------------------------------------------------------

//  QQuickTextDocument *QQuickTextDocumentPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickTextDocument *ritual_ZN25QQuickTextDocumentPrivate6q_funcEv(
    QQuickTextDocumentPrivate *self) {
  return self->q_func();
}

//  const QQuickTextDocument *QQuickTextDocumentPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickTextDocument *ritual_ZNK25QQuickTextDocumentPrivate6q_funcEv(
    const QQuickTextDocumentPrivate *self) {
  return self->q_func();
}

//  QQuickTextDocumentPrivate
//      *QQuickTextDocumentPrivate::get(QQuickTextDocument *doc)
extern "C" Q_DECL_EXPORT
QQuickTextDocumentPrivate *ritual_ZN25QQuickTextDocumentPrivate3getEP18QQuickTextDocument(
    QQuickTextDocument *doc) {
  return QQuickTextDocumentPrivate::get(doc);
}

//  const QQuickTextDocumentPrivate *QQuickTextDocumentPrivate::get(const
//      QQuickTextDocument *doc)
extern "C" Q_DECL_EXPORT
const QQuickTextDocumentPrivate *ritual_ZN25QQuickTextDocumentPrivate3getEPK18QQuickTextDocument(
    const QQuickTextDocument *doc) {
  return QQuickTextDocumentPrivate::get(doc);
}

//  void QQuickTextDocumentPrivate::writeTo(const QUrl &fileUrl)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickTextDocumentPrivate7writeToERK4QUrl(
    QQuickTextDocumentPrivate *self,
    const QUrl *fileUrl) {
  self->writeTo(*fileUrl);
}

//  QTextDocument *QQuickTextDocumentPrivate::document() const
extern "C" Q_DECL_EXPORT
QTextDocument *ritual_ZNK25QQuickTextDocumentPrivate8documentEv(
    const QQuickTextDocumentPrivate *self) {
  return self->document();
}

//  void QQuickTextDocumentPrivate::setDocument(QTextDocument *doc)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickTextDocumentPrivate11setDocumentEP13QTextDocument(
    QQuickTextDocumentPrivate *self,
    QTextDocument *doc) {
  self->setDocument(doc);
}

//  void QQuickTextDocumentPrivate::setStatus(QQuickTextDocument::Status s,
//      const QString &err)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickTextDocumentPrivate9setStatusEN18QQuickTextDocument6StatusERK7QString(
    QQuickTextDocumentPrivate *self,
    QQuickTextDocument::Status s,
    const QString *err) {
  self->setStatus(s, *err);
}
