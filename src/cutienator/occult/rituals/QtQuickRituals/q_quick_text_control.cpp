//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktextcontrol_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicktextcontrol_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qtextcursor.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtGui/qtextobject.h>
#include <QtGui/qtextformat.h>
#include <QtGui/qtransform.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qquicktextcontrol_p.h>
#include <QtQuick/private/qquicktextcontrol_p_p.h>
#ifndef QT_NO_TEXTCONTROL
#include <QtCore/qcoreapplication.h>
#include <QtGui/qfont.h>
#include <QtGui/qfontmetrics.h>
#include <QtGui/qevent.h>
#include <QtCore/qdebug.h>
#include <QtGui/qclipboard.h>
#include <QtCore/qtimer.h>
#include <QtGui/qinputmethod.h>
#include <QtGui/private/qtextdocumentlayout_p.h>
#include <QtGui/private/qabstracttextdocumentlayout_p.h>
#include <QtGui/qtextdocument.h>
#include <QtGui/private/qtextdocument_p.h>
#include <QtGui/qtextlist.h>
#include <QtGui/qtextdocumentwriter.h>
#include <QtGui/private/qtextcursor_p.h>
#include <QtCore/qloggingcategory.h>
#include <QtGui/qtextformat.h>
#include <QtGui/qtransform.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qbuffer.h>
#include <QtGui/qguiapplication.h>
#include <limits.h>
#include <QtGui/qtexttable.h>
#include <QtCore/qvariant.h>
#include <QtCore/qurl.h>
#include <QtGui/qstylehints.h>
#include <QtCore/qmetaobject.h>
#include <QtQml/private/qqmlglobal_p.h>
#include <QtQuick/private/qquickdeliveryagent_p_p.h>
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

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 43, as local:qquicktextcontrol.cpp:textCursorWidth
#if !defined(QT_NO_TEXTCONTROL)
const int textCursorWidth = 1;
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 779, as _ZN17QQuickTextControl10timerEventEP11QTimerEvent
#if !defined(QT_NO_TEXTCONTROL)
inline void QQuickTextControl::timerEvent(QTimerEvent *e)
{
    Q_D(QQuickTextControl);
    if (e->timerId() == d->cursorBlinkTimer.timerId()) {
        d->cursorOn = !d->cursorOn;

        d->repaintCursor();
    }
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 439, as _ZN24QQuickTextControlPrivate24setBlinkingCursorEnabledEb
#if !defined(QT_NO_TEXTCONTROL)
inline void QQuickTextControlPrivate::setBlinkingCursorEnabled(bool enable)
{
    if (cursorBlinkingEnabled == enable)
        return;

    cursorBlinkingEnabled = enable;
    updateCursorFlashTime();

    if (enable)
        connect(qApp->styleHints(), &QStyleHints::cursorFlashTimeChanged, this, &QQuickTextControlPrivate::updateCursorFlashTime);
    else
        disconnect(qApp->styleHints(), &QStyleHints::cursorFlashTimeChanged, this, &QQuickTextControlPrivate::updateCursorFlashTime);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 975, as _ZNK24QQuickTextControlPrivate15rectForPositionEi
#if !defined(QT_NO_TEXTCONTROL)
inline QRectF QQuickTextControlPrivate::rectForPosition(int position) const
{
    Q_Q(const QQuickTextControl);
    const QTextBlock block = doc->findBlock(position);
    if (!block.isValid())
        return QRectF();
    const QTextLayout *layout = block.layout();
    const QPointF layoutPos = q->blockBoundingRect(block).topLeft();
    int relativePos = position - block.position();
#if QT_CONFIG(im)
    if (preeditCursor != 0) {
        int preeditPos = layout->preeditAreaPosition();
        if (relativePos == preeditPos)
            relativePos += preeditCursor;
        else if (relativePos > preeditPos)
            relativePos += layout->preeditAreaText().size();
    }
#endif
    QTextLine line = layout->lineForTextPosition(relativePos);

    QRectF r;

    if (line.isValid()) {
        qreal x = line.cursorToX(relativePos);
        qreal w = 0;
        if (overwriteMode) {
            if (relativePos < line.textLength() - line.textStart())
                w = line.cursorToX(relativePos + 1) - x;
            else
                w = QFontMetrics(block.layout()->font()).horizontalAdvance(QLatin1Char(' ')); // in sync with QTextLine::draw()
        }
        r = QRectF(layoutPos.x() + x, layoutPos.y() + line.y(), textCursorWidth + w, line.height());
    } else {
        r = QRectF(layoutPos.x(), layoutPos.y(), textCursorWidth, 10); // #### correct height
    }

    return r;
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 343, as _ZN24QQuickTextControlPrivate13repaintCursorEv
#if !defined(QT_NO_TEXTCONTROL)
inline void QQuickTextControlPrivate::repaintCursor()
{
    Q_Q(QQuickTextControl);
    emit q->updateCursorRequest();
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 1875, as _ZNK17QQuickTextControl7hitTestERK7QPointFN2Qt15HitTestAccuracyE
#if !defined(QT_NO_TEXTCONTROL)
inline int QQuickTextControl::hitTest(const QPointF &point, Qt::HitTestAccuracy accuracy) const
{
    Q_D(const QQuickTextControl);
    return d->doc->documentLayout()->hitTest(point, accuracy);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 1881, as _ZNK17QQuickTextControl17blockBoundingRectERK10QTextBlock
#if !defined(QT_NO_TEXTCONTROL)
inline QRectF QQuickTextControl::blockBoundingRect(const QTextBlock &block) const
{
    Q_D(const QQuickTextControl);
    return d->doc->documentLayout()->blockBoundingRect(block);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 1419, as _ZNK17QQuickTextControl16inputMethodQueryEN2Qt16InputMethodQueryE
#if !defined(QT_NO_TEXTCONTROL)
#if QT_CONFIG(im)
inline QVariant QQuickTextControl::inputMethodQuery(Qt::InputMethodQuery property) const
{
    return inputMethodQuery(property, QVariant());
}
#endif  // QT_CONFIG(im)
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 1676, as _ZNK17QQuickTextControl27createMimeDataFromSelectionEv
#if !defined(QT_NO_TEXTCONTROL)
inline QMimeData *QQuickTextControl::createMimeDataFromSelection() const
{
    Q_D(const QQuickTextControl);
    const QTextDocumentFragment fragment(d->cursor);
    return new QQuickTextEditMimeData(fragment);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 1683, as _ZNK17QQuickTextControl21canInsertFromMimeDataEPK9QMimeData
#if !defined(QT_NO_TEXTCONTROL)
inline bool QQuickTextControl::canInsertFromMimeData(const QMimeData *source) const
{
    Q_D(const QQuickTextControl);
    if (d->acceptRichText)
        return source->hasText()
            || source->hasHtml()
            || source->hasFormat(QLatin1String("application/x-qrichtext"))
            || source->hasFormat(QLatin1String("application/x-qt-richtext"));
    else
        return source->hasText();
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 1695, as _ZN17QQuickTextControl18insertFromMimeDataEPK9QMimeData
#if !defined(QT_NO_TEXTCONTROL)
inline void QQuickTextControl::insertFromMimeData(const QMimeData *source)
{
    Q_D(QQuickTextControl);
    if (!(d->interactionFlags & Qt::TextEditable) || !source)
        return;

    bool hasData = false;
    QTextDocumentFragment fragment;
#if QT_CONFIG(texthtmlparser)
    if (source->hasFormat(QLatin1String("application/x-qrichtext")) && d->acceptRichText) {
        // x-qrichtext is always UTF-8 (taken from Qt3 since we don't use it anymore).
        const QString richtext = QLatin1String("<meta name=\"qrichtext\" content=\"1\" />")
                + QString::fromUtf8(source->data(QLatin1String("application/x-qrichtext")));
        fragment = QTextDocumentFragment::fromHtml(richtext, d->doc);
        hasData = true;
    } else if (source->hasHtml() && d->acceptRichText) {
        fragment = QTextDocumentFragment::fromHtml(source->html(), d->doc);
        hasData = true;
    } else {
        QString text = source->text();
        if (!text.isNull()) {
            fragment = QTextDocumentFragment::fromPlainText(text);
            hasData = true;
        }
    }
#else
    fragment = QTextDocumentFragment::fromPlainText(source->text());
#endif // texthtmlparser

    if (hasData)
        d->cursor.insertFragment(fragment);
    updateCursorRectangle(true);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 768, as _ZN17QQuickTextControl5eventEP6QEvent
#if !defined(QT_NO_TEXTCONTROL)
inline bool QQuickTextControl::event(QEvent *e)
{
    return QObject::event(e);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 1902, as _ZNK22QQuickTextEditMimeData7formatsEv
#if !defined(QT_NO_TEXTCONTROL)
inline QStringList QQuickTextEditMimeData::formats() const
{
    if (!fragment.isEmpty())
        return QStringList() << QString::fromLatin1("text/plain") << QString::fromLatin1("text/html")
#if QT_CONFIG(textodfwriter)
            << QString::fromLatin1("application/vnd.oasis.opendocument.text")
#endif
        ;
    else
        return QMimeData::formats();
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 1914, as _ZNK22QQuickTextEditMimeData12retrieveDataERK7QString9QMetaType
#if !defined(QT_NO_TEXTCONTROL)
inline QVariant QQuickTextEditMimeData::retrieveData(const QString &mimeType, QMetaType type) const
{
    if (!fragment.isEmpty())
        setup();
    return QMimeData::retrieveData(mimeType, type);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 632, as _ZN17QQuickTextControl21updateCursorRectangleEb
#if !defined(QT_NO_TEXTCONTROL)
inline void QQuickTextControl::updateCursorRectangle(bool force)
{
    Q_D(QQuickTextControl);
    const bool update = d->cursorRectangleChanged || force;
    d->cursorRectangleChanged = false;
    if (update)
        emit cursorRectangleChanged();
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 1921, as _ZNK22QQuickTextEditMimeData5setupEv
#if !defined(QT_NO_TEXTCONTROL)
inline void QQuickTextEditMimeData::setup() const
{
    QQuickTextEditMimeData *that = const_cast<QQuickTextEditMimeData *>(this);
#if QT_CONFIG(texthtmlparser)
    that->setData(QLatin1String("text/html"), fragment.toHtml().toUtf8());
#endif
#if QT_CONFIG(textodfwriter)
    {
        QBuffer buffer;
        QTextDocumentWriter writer(&buffer, "ODF");
        writer.write(fragment);
        buffer.close();
        that->setData(QLatin1String("application/vnd.oasis.opendocument.text"), buffer.data());
    }
#endif
    that->setText(fragment.toPlainText());
    fragment = QTextDocumentFragment();
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 595, as _ZNK17QQuickTextControl8documentEv
#if !defined(QT_NO_TEXTCONTROL)
inline QTextDocument *QQuickTextControl::document() const
{
    Q_D(const QQuickTextControl);
    return d->doc;
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 659, as _ZNK17QQuickTextControl10textCursorEv
#if !defined(QT_NO_TEXTCONTROL)
inline QTextCursor QQuickTextControl::textCursor() const
{
    Q_D(const QQuickTextControl);
    return d->cursor;
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 1844, as _ZNK17QQuickTextControl20textInteractionFlagsEv
#if !defined(QT_NO_TEXTCONTROL)
inline Qt::TextInteractionFlags QQuickTextControl::textInteractionFlags() const
{
    Q_D(const QQuickTextControl);
    return d->interactionFlags;
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 1850, as _ZNK17QQuickTextControl11toPlainTextEv
#if !defined(QT_NO_TEXTCONTROL)
inline QString QQuickTextControl::toPlainText() const
{
    return document()->toPlainText();
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 1856, as _ZNK17QQuickTextControl6toHtmlEv
#if !defined(QT_NO_TEXTCONTROL)
#if QT_CONFIG(texthtmlparser)
inline QString QQuickTextControl::toHtml() const
{
    return document()->toHtml();
}
#endif  // QT_CONFIG(texthtmlparser)
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 1863, as _ZNK17QQuickTextControl10toMarkdownEv
#if !defined(QT_NO_TEXTCONTROL)
#if QT_CONFIG(textmarkdownwriter)
inline QString QQuickTextControl::toMarkdown() const
{
    return document()->toMarkdown();
}
#endif  // QT_CONFIG(textmarkdownwriter)
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 1546, as _ZNK17QQuickTextControl10hasImStateEv
#if !defined(QT_NO_TEXTCONTROL)
inline bool QQuickTextControl::hasImState() const
{
    Q_D(const QQuickTextControl);
    return d->hasImState;
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 1552, as _ZNK17QQuickTextControl13overwriteModeEv
#if !defined(QT_NO_TEXTCONTROL)
inline bool QQuickTextControl::overwriteMode() const
{
    Q_D(const QQuickTextControl);
    return d->overwriteMode;
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 1567, as _ZNK17QQuickTextControl13cursorVisibleEv
#if !defined(QT_NO_TEXTCONTROL)
inline bool QQuickTextControl::cursorVisible() const
{
    Q_D(const QQuickTextControl);
    return d->cursorVisible;
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 1581, as _ZNK17QQuickTextControl10anchorRectEv
#if !defined(QT_NO_TEXTCONTROL)
inline QRectF QQuickTextControl::anchorRect() const
{
    Q_D(const QQuickTextControl);
    QRectF rect;
    QTextCursor cursor = d->cursor;
    if (!cursor.isNull()) {
        rect = d->rectForPosition(cursor.anchor());
    }
    return rect;
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 1592, as _ZNK17QQuickTextControl10cursorRectERK11QTextCursor
#if !defined(QT_NO_TEXTCONTROL)
inline QRectF QQuickTextControl::cursorRect(const QTextCursor &cursor) const
{
    Q_D(const QQuickTextControl);
    if (cursor.isNull())
        return QRectF();

    return d->rectForPosition(cursor.position());
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 1601, as _ZNK17QQuickTextControl10cursorRectEv
#if !defined(QT_NO_TEXTCONTROL)
inline QRectF QQuickTextControl::cursorRect() const
{
    Q_D(const QQuickTextControl);
    return cursorRect(d->cursor);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 1607, as _ZNK17QQuickTextControl11hoveredLinkEv
#if !defined(QT_NO_TEXTCONTROL)
inline QString QQuickTextControl::hoveredLink() const
{
    Q_D(const QQuickTextControl);
    return d->hoveredLink;
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 1613, as _ZNK17QQuickTextControl8anchorAtERK7QPointF
#if !defined(QT_NO_TEXTCONTROL)
inline QString QQuickTextControl::anchorAt(const QPointF &pos) const
{
    Q_D(const QQuickTextControl);
    return d->doc->documentLayout()->anchorAt(pos);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 1619, as _ZNK17QQuickTextControl17blockWithMarkerAtERK7QPointF
#if !defined(QT_NO_TEXTCONTROL)
inline QTextBlock QQuickTextControl::blockWithMarkerAt(const QPointF &pos) const
{
    Q_D(const QQuickTextControl);
    return d->doc->documentLayout()->blockWithMarkerAt(pos);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 1625, as _ZN17QQuickTextControl17setAcceptRichTextEb
#if !defined(QT_NO_TEXTCONTROL)
inline void QQuickTextControl::setAcceptRichText(bool accept)
{
    Q_D(QQuickTextControl);
    d->acceptRichText = accept;
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 1643, as _ZNK17QQuickTextControl8canPasteEv
#if !defined(QT_NO_TEXTCONTROL)
inline bool QQuickTextControl::canPaste() const
{
#if QT_CONFIG(clipboard)
    Q_D(const QQuickTextControl);
    if (d->interactionFlags & Qt::TextEditable) {
        const QMimeData *md = QGuiApplication::clipboard()->mimeData();
        return md && canInsertFromMimeData(md);
    }
#endif
    return false;
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 1662, as _ZN17QQuickTextControl23setWordSelectionEnabledEb
#if !defined(QT_NO_TEXTCONTROL)
inline void QQuickTextControl::setWordSelectionEnabled(bool enabled)
{
    Q_D(QQuickTextControl);
    d->wordSelectionEnabled = enabled;
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 1669, as _ZN17QQuickTextControl28setTouchDragSelectionEnabledEb
#if !defined(QT_NO_TEXTCONTROL)
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
inline void QQuickTextControl::setTouchDragSelectionEnabled(bool enabled)
{
    Q_D(QQuickTextControl);
    d->selectByTouchDrag = enabled;
}
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 1887, as _ZNK17QQuickTextControl11preeditTextEv
#if !defined(QT_NO_TEXTCONTROL)
inline QString QQuickTextControl::preeditText() const
{
#if QT_CONFIG(im)
    Q_D(const QQuickTextControl);
    QTextLayout *layout = d->cursor.block().layout();
    if (!layout)
        return QString();

    return layout->preeditAreaText();
#else
    return QString();
#endif
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 703, as _ZN17QQuickTextControl12processEventEP6QEventRK7QPointF
#if !defined(QT_NO_TEXTCONTROL)
inline void QQuickTextControl::processEvent(QEvent *e, const QPointF &coordinateOffset)
{
    QTransform t;
    t.translate(coordinateOffset.x(), coordinateOffset.y());
    processEvent(e, t);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 1424, as _ZNK17QQuickTextControl16inputMethodQueryEN2Qt16InputMethodQueryERK8QVariant
#if !defined(QT_NO_TEXTCONTROL)
#if QT_CONFIG(im)
inline QVariant QQuickTextControl::inputMethodQuery(Qt::InputMethodQuery property, const QVariant &argument) const
{
    Q_D(const QQuickTextControl);
    QTextBlock block = d->cursor.block();
    switch (property) {
    case Qt::ImCursorRectangle:
        return cursorRect();
    case Qt::ImAnchorRectangle:
        return anchorRect();
    case Qt::ImFont:
        return QVariant(d->cursor.charFormat().font());
    case Qt::ImCursorPosition: {
        const QPointF pt = argument.toPointF();
        if (!pt.isNull())
            return QVariant(d->doc->documentLayout()->hitTest(pt, Qt::FuzzyHit) - block.position());
        return QVariant(d->cursor.position() - block.position());
    }
    case Qt::ImSurroundingText:
        return QVariant(block.text());
    case Qt::ImCurrentSelection: {
        QMimeData *mimeData = createMimeDataFromSelection();
        mimeData->deleteLater();
        return QInputControl::selectionWrapper(mimeData);
    }
    case Qt::ImMaximumTextLength:
        return QVariant(); // No limit.
    case Qt::ImAnchorPosition:
        return QVariant(d->cursor.anchor() - block.position());
    case Qt::ImAbsolutePosition:
        return QVariant(d->cursor.position());
    case Qt::ImTextAfterCursor:
    {
        int maxLength = argument.isValid() ? argument.toInt() : 1024;
        QTextCursor tmpCursor = d->cursor;
        int localPos = d->cursor.position() - block.position();
        QString result = block.text().mid(localPos);
        while (result.size() < maxLength) {
            int currentBlock = tmpCursor.blockNumber();
            tmpCursor.movePosition(QTextCursor::NextBlock);
            if (tmpCursor.blockNumber() == currentBlock)
                break;
            result += QLatin1Char('\n') + tmpCursor.block().text();
        }
        return QVariant(result);
    }
    case Qt::ImTextBeforeCursor:
    {
        int maxLength = argument.isValid() ? argument.toInt() : 1024;
        QTextCursor tmpCursor = d->cursor;
        int localPos = d->cursor.position() - block.position();
        int numBlocks = 0;
        int resultLen = localPos;
        while (resultLen < maxLength) {
            int currentBlock = tmpCursor.blockNumber();
            tmpCursor.movePosition(QTextCursor::PreviousBlock);
            if (tmpCursor.blockNumber() == currentBlock)
                break;
            numBlocks++;
            resultLen += tmpCursor.block().length();
        }
        QString result;
        while (numBlocks) {
            result += tmpCursor.block().text() + QLatin1Char('\n');
            tmpCursor.movePosition(QTextCursor::NextBlock);
            --numBlocks;
        }
        result += QStringView{block.text()}.mid(0,localPos);
        return QVariant(result);
    }
    case Qt::ImReadOnly:
        return QVariant(!d->interactionFlags.testFlag(Qt::TextEditable));
    default:
        return QVariant();
    }
}
#endif  // QT_CONFIG(im)
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 1869, as _ZNK17QQuickTextControl8cursorOnEv
#if !defined(QT_NO_TEXTCONTROL)
inline bool QQuickTextControl::cursorOn() const
{
    Q_D(const QQuickTextControl);
    return d->cursorOn;
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 773, as _ZN17QQuickTextControl13isBeingEditedEv
#if !defined(QT_NO_TEXTCONTROL)
inline bool QQuickTextControl::isBeingEdited()
{
    Q_D(QQuickTextControl);
    return d->beingEdited;
}
#endif  // !defined(QT_NO_TEXTCONTROL)
//  -----------------------------------------------------------------------

//  Only a class built on QQuickTextControl may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickTextControl : QQuickTextControl {
  using QQuickTextControl::event;
};

//  A QQuickTextControl that Python can take functions over in. Every QQuickTextControl
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQQuickTextControlCall0)(const void *, const QPointF *, int, int *);
typedef const QRectF * (*CuteQQuickTextControlCall1)(const void *, const QTextBlock *, int *);
typedef void (*CuteQQuickTextControlCall2)(const void *, QEvent *, const QTransform *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQQuickTextControlCall3)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef void * (*CuteQQuickTextControlCall4)(const void *, int *);
typedef bool (*CuteQQuickTextControlCall5)(const void *, const QMimeData *, int *);
typedef void (*CuteQQuickTextControlCall6)(const void *, const QMimeData *, int *);
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTextControlCall7)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickTextControlCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuickTextControlCall9)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTextControlCall10)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTextControlCall11)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTextControlCall12)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuickTextControlCall13)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuickTextControl : public QQuickTextControl {
public:
  using QQuickTextControl::QQuickTextControl;
  void *taken[14] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK17QQuickTextControl7hitTestERK7QPointFN2Qt15HitTestAccuracyE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickTextControl17blockBoundingRectERK10QTextBlock")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickTextControl12processEventEP6QEventRK10QTransform")) {
      taken[2] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK17QQuickTextControl16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK17QQuickTextControl27createMimeDataFromSelectionEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickTextControl21canInsertFromMimeDataEPK9QMimeData")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickTextControl18insertFromMimeDataEPK9QMimeData")) {
      taken[6] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  int QQuickTextControl::hitTest(const QPointF &point,
  //      Qt::HitTestAccuracy accuracy) const
  int hitTest(
      const QPointF &point,
      Qt::HitTestAccuracy accuracy) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickTextControlCall0 call = reinterpret_cast<CuteQQuickTextControlCall0>(taken[0]);
      int given = call(this, &point, static_cast<int>(accuracy), &handled);
      if (handled) return given;
    }
    return QQuickTextControl::hitTest(point, accuracy);
  }

  //  QRectF QQuickTextControl::blockBoundingRect(const QTextBlock &block)
  //      const
  QRectF blockBoundingRect(const QTextBlock &block) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickTextControlCall1 call = reinterpret_cast<CuteQQuickTextControlCall1>(taken[1]);
      const QRectF * given = call(this, &block, &handled);
      if (handled && given) return *given;
    }
    return QQuickTextControl::blockBoundingRect(block);
  }

  //  void QQuickTextControl::processEvent(QEvent *e, const QTransform
  //      &transform)
  void processEvent(QEvent *e, const QTransform &transform) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickTextControlCall2 call = reinterpret_cast<CuteQQuickTextControlCall2>(taken[2]);
      call(this, e, &transform, &handled);
      if (handled) return;
    }
    QQuickTextControl::processEvent(e, transform);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickTextControl::inputMethodQuery(Qt::InputMethodQuery
  //      property) const
  QVariant inputMethodQuery(Qt::InputMethodQuery property) const override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickTextControlCall3 call = reinterpret_cast<CuteQQuickTextControlCall3>(taken[3]);
      const QVariant * given = call(this, static_cast<int>(property), &handled);
      if (handled && given) return *given;
    }
    return QQuickTextControl::inputMethodQuery(property);
  }
#endif  // QT_CONFIG(im)

  //  QMimeData *QQuickTextControl::createMimeDataFromSelection() const
  QMimeData *createMimeDataFromSelection() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickTextControlCall4 call = reinterpret_cast<CuteQQuickTextControlCall4>(taken[4]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QMimeData *>(given);
    }
    return QQuickTextControl::createMimeDataFromSelection();
  }

  //  bool QQuickTextControl::canInsertFromMimeData(const QMimeData
  //      *source) const
  bool canInsertFromMimeData(const QMimeData *source) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickTextControlCall5 call = reinterpret_cast<CuteQQuickTextControlCall5>(taken[5]);
      bool given = call(this, source, &handled);
      if (handled) return given;
    }
    return QQuickTextControl::canInsertFromMimeData(source);
  }

  //  void QQuickTextControl::insertFromMimeData(const QMimeData *source)
  void insertFromMimeData(const QMimeData *source) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickTextControlCall6 call = reinterpret_cast<CuteQQuickTextControlCall6>(taken[6]);
      call(this, source, &handled);
      if (handled) return;
    }
    QQuickTextControl::insertFromMimeData(source);
  }

#if !defined(QT_NO_QOBJECT)
  //  void QQuickTextControl::timerEvent(QTimerEvent *e)
  void timerEvent(QTimerEvent *e) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickTextControlCall7 call = reinterpret_cast<CuteQQuickTextControlCall7>(taken[7]);
      call(this, e, &handled);
      if (handled) return;
    }
    QQuickTextControl::timerEvent(e);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickTextControl::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickTextControlCall8 call = reinterpret_cast<CuteQQuickTextControlCall8>(taken[8]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return QQuickTextControl::event(e);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickTextControlCall9 call = reinterpret_cast<CuteQQuickTextControlCall9>(taken[9]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickTextControlCall10 call = reinterpret_cast<CuteQQuickTextControlCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickTextControlCall11 call = reinterpret_cast<CuteQQuickTextControlCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickTextControlCall12 call = reinterpret_cast<CuteQQuickTextControlCall12>(taken[12]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickTextControlCall13 call = reinterpret_cast<CuteQQuickTextControlCall13>(taken[13]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuickTextControl::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QQuickTextControl10metaObjectEv(
    const QQuickTextControl *self) {
  return self->metaObject();
}

//  void *QQuickTextControl::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN17QQuickTextControl11qt_metacastEPKc(
    QQuickTextControl *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuickTextControl::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN17QQuickTextControl11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuickTextControl *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QQuickTextControlPrivate *QQuickTextControl::d_func()
extern "C" Q_DECL_EXPORT
QQuickTextControlPrivate *ritual_ZN17QQuickTextControl6d_funcEv(
    QQuickTextControl *self) {
  return self->d_func();
}

//  const QQuickTextControlPrivate *QQuickTextControl::d_func() const
extern "C" Q_DECL_EXPORT
const QQuickTextControlPrivate *ritual_ZNK17QQuickTextControl6d_funcEv(
    const QQuickTextControl *self) {
  return self->d_func();
}

//  QQuickTextControl::~QQuickTextControl()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextControlD1Ev(QQuickTextControl *self) {
  delete self;
}

#if !defined(QT_NO_TEXTCONTROL)
//  QTextDocument *QQuickTextControl::document() const
extern "C" Q_DECL_EXPORT
QTextDocument *ritual_ZNK17QQuickTextControl8documentEv(
    const QQuickTextControl *self) {
  return self->document();
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  QTextCursor QQuickTextControl::textCursor() const
extern "C" Q_DECL_EXPORT
QTextCursor *ritual_ZNK17QQuickTextControl10textCursorEv(
    const QQuickTextControl *self) {
  return new QTextCursor(self->textCursor());
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  Qt::TextInteractionFlags QQuickTextControl::textInteractionFlags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQuickTextControl20textInteractionFlagsEv(
    const QQuickTextControl *self) {
  return static_cast<int>(self->textInteractionFlags().toInt());
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  QString QQuickTextControl::toPlainText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QQuickTextControl11toPlainTextEv(
    const QQuickTextControl *self) {
  return new QString(self->toPlainText());
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if QT_CONFIG(texthtmlparser)
#if !defined(QT_NO_TEXTCONTROL)
//  QString QQuickTextControl::toHtml() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QQuickTextControl6toHtmlEv(
    const QQuickTextControl *self) {
  return new QString(self->toHtml());
}
#endif  // !defined(QT_NO_TEXTCONTROL)
#endif  // QT_CONFIG(texthtmlparser)

#if QT_CONFIG(textmarkdownwriter)
#if !defined(QT_NO_TEXTCONTROL)
//  QString QQuickTextControl::toMarkdown() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QQuickTextControl10toMarkdownEv(
    const QQuickTextControl *self) {
  return new QString(self->toMarkdown());
}
#endif  // !defined(QT_NO_TEXTCONTROL)
#endif  // QT_CONFIG(textmarkdownwriter)

#if !defined(QT_NO_TEXTCONTROL)
//  bool QQuickTextControl::hasImState() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickTextControl10hasImStateEv(
    const QQuickTextControl *self) {
  return self->hasImState();
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  bool QQuickTextControl::overwriteMode() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickTextControl13overwriteModeEv(
    const QQuickTextControl *self) {
  return self->overwriteMode();
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  bool QQuickTextControl::cursorVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickTextControl13cursorVisibleEv(
    const QQuickTextControl *self) {
  return self->cursorVisible();
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  QRectF QQuickTextControl::anchorRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK17QQuickTextControl10anchorRectEv(
    const QQuickTextControl *self) {
  return new QRectF(self->anchorRect());
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  QRectF QQuickTextControl::cursorRect(const QTextCursor &cursor) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK17QQuickTextControl10cursorRectERK11QTextCursor(
    const QQuickTextControl *self,
    const QTextCursor *cursor) {
  return new QRectF(self->cursorRect(*cursor));
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  QRectF QQuickTextControl::cursorRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK17QQuickTextControl10cursorRectEv(
    const QQuickTextControl *self) {
  return new QRectF(self->cursorRect());
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  QString QQuickTextControl::hoveredLink() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QQuickTextControl11hoveredLinkEv(
    const QQuickTextControl *self) {
  return new QString(self->hoveredLink());
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  QString QQuickTextControl::anchorAt(const QPointF &pos) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QQuickTextControl8anchorAtERK7QPointF(
    const QQuickTextControl *self,
    const QPointF *pos) {
  return new QString(self->anchorAt(*pos));
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  QTextBlock QQuickTextControl::blockWithMarkerAt(const QPointF &pos) const
extern "C" Q_DECL_EXPORT
QTextBlock *ritual_ZNK17QQuickTextControl17blockWithMarkerAtERK7QPointF(
    const QQuickTextControl *self,
    const QPointF *pos) {
  return new QTextBlock(self->blockWithMarkerAt(*pos));
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  void QQuickTextControl::setAcceptRichText(bool accept)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextControl17setAcceptRichTextEb(
    QQuickTextControl *self,
    bool accept) {
  self->setAcceptRichText(accept);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  bool QQuickTextControl::canPaste() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickTextControl8canPasteEv(
    const QQuickTextControl *self) {
  return self->canPaste();
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  void QQuickTextControl::setWordSelectionEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextControl23setWordSelectionEnabledEb(
    QQuickTextControl *self,
    bool enabled) {
  self->setWordSelectionEnabled(enabled);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
#if !defined(QT_NO_TEXTCONTROL)
//  void QQuickTextControl::setTouchDragSelectionEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextControl28setTouchDragSelectionEnabledEb(
    QQuickTextControl *self,
    bool enabled) {
  self->setTouchDragSelectionEnabled(enabled);
}
#endif  // !defined(QT_NO_TEXTCONTROL)
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

//  int QQuickTextControl::hitTest(const QPointF &point, Qt::HitTestAccuracy
//      accuracy) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQuickTextControl7hitTestERK7QPointFN2Qt15HitTestAccuracyE(
    const QQuickTextControl *self,
    const QPointF *point,
    Qt::HitTestAccuracy accuracy) {
  return self->hitTest(*point, accuracy);
}

//  QRectF QQuickTextControl::blockBoundingRect(const QTextBlock &block)
//      const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK17QQuickTextControl17blockBoundingRectERK10QTextBlock(
    const QQuickTextControl *self,
    const QTextBlock *block) {
  return new QRectF(self->blockBoundingRect(*block));
}

#if !defined(QT_NO_TEXTCONTROL)
//  QString QQuickTextControl::preeditText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QQuickTextControl11preeditTextEv(
    const QQuickTextControl *self) {
  return new QString(self->preeditText());
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  void QQuickTextControl::setPlainText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextControl12setPlainTextERK7QString(
    QQuickTextControl *self,
    const QString *text) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickTextControl")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "setPlainText(const QString &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "setPlainText(const QString &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(text)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickTextControl::setMarkdownText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextControl15setMarkdownTextERK7QString(
    QQuickTextControl *self,
    const QString *text) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickTextControl")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "setMarkdownText(const QString &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "setMarkdownText(const QString &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(text)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickTextControl::setHtml(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextControl7setHtmlERK7QString(
    QQuickTextControl *self,
    const QString *text) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickTextControl")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "setHtml(const QString &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "setHtml(const QString &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(text)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

#if QT_CONFIG(clipboard)
//  void QQuickTextControl::cut()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextControl3cutEv(QQuickTextControl *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickTextControl")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "cut()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "cut()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}
#endif  // QT_CONFIG(clipboard)

#if QT_CONFIG(clipboard)
//  void QQuickTextControl::copy()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextControl4copyEv(QQuickTextControl *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickTextControl")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "copy()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "copy()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}
#endif  // QT_CONFIG(clipboard)

#if QT_CONFIG(clipboard)
//  void QQuickTextControl::paste(QClipboard::Mode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextControl5pasteEN10QClipboard4ModeE(
    QQuickTextControl *self,
    QClipboard::Mode mode) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickTextControl")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "paste(QClipboard::Mode)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "paste(QClipboard::Mode)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&mode)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}
#endif  // QT_CONFIG(clipboard)

//  void QQuickTextControl::undo()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextControl4undoEv(QQuickTextControl *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickTextControl")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "undo()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "undo()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickTextControl::redo()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextControl4redoEv(QQuickTextControl *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickTextControl")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "redo()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "redo()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickTextControl::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextControl5clearEv(QQuickTextControl *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickTextControl")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "clear()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "clear()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickTextControl::selectAll()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextControl9selectAllEv(QQuickTextControl *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickTextControl")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "selectAll()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "selectAll()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickTextControl::textChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextControl11textChangedEv(QQuickTextControl *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickTextControl")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "textChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "textChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickTextControl::preeditTextChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextControl18preeditTextChangedEv(
    QQuickTextControl *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickTextControl")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "preeditTextChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "preeditTextChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickTextControl::contentsChange(int from, int charsRemoved, int
//      charsAdded)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextControl14contentsChangeEiii(
    QQuickTextControl *self,
    int from,
    int charsRemoved,
    int charsAdded) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickTextControl")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "contentsChange(int,int,int)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "contentsChange(int,int,int)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&from)),
      const_cast<void *>(static_cast<const void *>(&charsRemoved)),
      const_cast<void *>(static_cast<const void *>(&charsAdded)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickTextControl::undoAvailable(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextControl13undoAvailableEb(
    QQuickTextControl *self,
    bool b) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickTextControl")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "undoAvailable(bool)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "undoAvailable(bool)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&b)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickTextControl::redoAvailable(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextControl13redoAvailableEb(
    QQuickTextControl *self,
    bool b) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickTextControl")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "redoAvailable(bool)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "redoAvailable(bool)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&b)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickTextControl::currentCharFormatChanged(const QTextCharFormat
//      &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextControl24currentCharFormatChangedERK15QTextCharFormat(
    QQuickTextControl *self,
    const QTextCharFormat *format) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickTextControl")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "currentCharFormatChanged(const QTextCharFormat &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "currentCharFormatChanged(const QTextCharFormat &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(format)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickTextControl::copyAvailable(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextControl13copyAvailableEb(
    QQuickTextControl *self,
    bool b) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickTextControl")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "copyAvailable(bool)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "copyAvailable(bool)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&b)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickTextControl::selectionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextControl16selectionChangedEv(
    QQuickTextControl *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickTextControl")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "selectionChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "selectionChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickTextControl::cursorPositionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextControl21cursorPositionChangedEv(
    QQuickTextControl *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickTextControl")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "cursorPositionChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "cursorPositionChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickTextControl::overwriteModeChanged(bool overwriteMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextControl20overwriteModeChangedEb(
    QQuickTextControl *self,
    bool overwriteMode) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickTextControl")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "overwriteModeChanged(bool)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "overwriteModeChanged(bool)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&overwriteMode)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickTextControl::updateCursorRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextControl19updateCursorRequestEv(
    QQuickTextControl *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickTextControl")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "updateCursorRequest()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "updateCursorRequest()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickTextControl::updateRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextControl13updateRequestEv(QQuickTextControl *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickTextControl")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "updateRequest()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "updateRequest()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickTextControl::cursorRectangleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextControl22cursorRectangleChangedEv(
    QQuickTextControl *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickTextControl")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "cursorRectangleChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "cursorRectangleChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickTextControl::linkActivated(const QString &link)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextControl13linkActivatedERK7QString(
    QQuickTextControl *self,
    const QString *link) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickTextControl")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "linkActivated(const QString &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "linkActivated(const QString &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(link)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickTextControl::linkHovered(const QString &link)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextControl11linkHoveredERK7QString(
    QQuickTextControl *self,
    const QString *link) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickTextControl")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "linkHovered(const QString &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "linkHovered(const QString &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(link)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickTextControl::markerClicked()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextControl13markerClickedEv(QQuickTextControl *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickTextControl")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "markerClicked()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "markerClicked()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickTextControl::markerHovered(bool marker)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextControl13markerHoveredEb(
    QQuickTextControl *self,
    bool marker) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuickTextControl")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "markerHovered(bool)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "markerHovered(bool)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&marker)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuickTextControl::processEvent(QEvent *e, const QTransform
//      &transform)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextControl12processEventEP6QEventRK10QTransform(
    QQuickTextControl *self,
    QEvent *e,
    const QTransform *transform) {
  self->processEvent(e, *transform);
}

#if !defined(QT_NO_TEXTCONTROL)
//  void QQuickTextControl::processEvent(QEvent *e, const QPointF
//      &coordinateOffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextControl12processEventEP6QEventRK7QPointF(
    QQuickTextControl *self,
    QEvent *e,
    const QPointF *coordinateOffset) {
  self->processEvent(e, *coordinateOffset);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if QT_CONFIG(im)
//  QVariant QQuickTextControl::inputMethodQuery(Qt::InputMethodQuery
//      property) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK17QQuickTextControl16inputMethodQueryEN2Qt16InputMethodQueryE(
    const QQuickTextControl *self,
    Qt::InputMethodQuery property) {
  return new QVariant(self->inputMethodQuery(property));
}
#endif  // QT_CONFIG(im)

#if QT_CONFIG(im)
#if !defined(QT_NO_TEXTCONTROL)
//  QVariant QQuickTextControl::inputMethodQuery(Qt::InputMethodQuery query,
//      const QVariant &argument) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK17QQuickTextControl16inputMethodQueryEN2Qt16InputMethodQueryERK8QVariant(
    const QQuickTextControl *self,
    Qt::InputMethodQuery query,
    const QVariant *argument) {
  return new QVariant(self->inputMethodQuery(query, *argument));
}
#endif  // !defined(QT_NO_TEXTCONTROL)
#endif  // QT_CONFIG(im)

//  QMimeData *QQuickTextControl::createMimeDataFromSelection() const
extern "C" Q_DECL_EXPORT
QMimeData *ritual_ZNK17QQuickTextControl27createMimeDataFromSelectionEv(
    const QQuickTextControl *self) {
  return self->createMimeDataFromSelection();
}

//  bool QQuickTextControl::canInsertFromMimeData(const QMimeData *source)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickTextControl21canInsertFromMimeDataEPK9QMimeData(
    const QQuickTextControl *self,
    const QMimeData *source) {
  return self->canInsertFromMimeData(source);
}

//  void QQuickTextControl::insertFromMimeData(const QMimeData *source)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextControl18insertFromMimeDataEPK9QMimeData(
    QQuickTextControl *self,
    const QMimeData *source) {
  self->insertFromMimeData(source);
}

#if !defined(QT_NO_TEXTCONTROL)
//  bool QQuickTextControl::cursorOn() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickTextControl8cursorOnEv(
    const QQuickTextControl *self) {
  return self->cursorOn();
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  bool QQuickTextControl::isBeingEdited()
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QQuickTextControl13isBeingEditedEv(QQuickTextControl *self) {
  return self->isBeingEdited();
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  void QQuickTextControl::timerEvent(QTimerEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextControl10timerEventEP11QTimerEvent(
    QQuickTextControl *self,
    QTimerEvent *e) {
  self->timerEvent(e);
}

//  bool QQuickTextControl::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QQuickTextControl5eventEP6QEvent(
    QQuickTextControl *self,
    QEvent *e) {
  return self->event(e);
}

//  a Python function taken by a CuteQQuickTextControl, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickTextControl(
    QQuickTextControl *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickTextControl *>(self)->take(key, call);
}

#if !defined(QT_NO_TEXTCONTROL)
//  int QQuickTextControl::hitTest(const QPointF &point, Qt::HitTestAccuracy
//      accuracy) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK17QQuickTextControl7hitTestERK7QPointFN2Qt15HitTestAccuracyE(
    const QQuickTextControl *self,
    const QPointF *point,
    Qt::HitTestAccuracy accuracy) {
  return self->QQuickTextControl::hitTest(*point, accuracy);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  QRectF QQuickTextControl::blockBoundingRect(const QTextBlock &block)
//      const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK17QQuickTextControl17blockBoundingRectERK10QTextBlock(
    const QQuickTextControl *self,
    const QTextBlock *block) {
  return new QRectF(self->QQuickTextControl::blockBoundingRect(*block));
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if QT_CONFIG(im)
#if !defined(QT_NO_TEXTCONTROL)
//  QVariant QQuickTextControl::inputMethodQuery(Qt::InputMethodQuery
//      property) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK17QQuickTextControl16inputMethodQueryEN2Qt16InputMethodQueryE(
    const QQuickTextControl *self,
    Qt::InputMethodQuery property) {
  return new QVariant(self->QQuickTextControl::inputMethodQuery(property));
}
#endif  // !defined(QT_NO_TEXTCONTROL)
#endif  // QT_CONFIG(im)

#if !defined(QT_NO_TEXTCONTROL)
//  QMimeData *QQuickTextControl::createMimeDataFromSelection() const
extern "C" Q_DECL_EXPORT
QMimeData *ritual_own_ZNK17QQuickTextControl27createMimeDataFromSelectionEv(
    const QQuickTextControl *self) {
  return self->QQuickTextControl::createMimeDataFromSelection();
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  bool QQuickTextControl::canInsertFromMimeData(const QMimeData *source)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK17QQuickTextControl21canInsertFromMimeDataEPK9QMimeData(
    const QQuickTextControl *self,
    const QMimeData *source) {
  return self->QQuickTextControl::canInsertFromMimeData(source);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  bool QQuickTextControl::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QQuickTextControl5eventEP6QEvent(
    QQuickTextControl *self,
    QEvent *e) {
  return static_cast<OwnQQuickTextControl *>(self)->OwnQQuickTextControl::event(
      e);
}
#endif  // !defined(QT_NO_TEXTCONTROL)
