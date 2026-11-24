//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktextcontrol_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicktextcontrol_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qtextcursor.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtGui/qtextobject.h>
#include <QtCore/qrect.h>
#include <QtGui/qtransform.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qquicktextcontrol_p.h"
#include "qquicktextcontrol_p_p.h"
#ifndef QT_NO_TEXTCONTROL
#include <qcoreapplication.h>
#include <qfont.h>
#include <qfontmetrics.h>
#include <qevent.h>
#include <qdebug.h>
#include <qclipboard.h>
#include <qtimer.h>
#include <qinputmethod.h>
#include "private/qtextdocumentlayout_p.h"
#include "private/qabstracttextdocumentlayout_p.h"
#include "qtextdocument.h"
#include "private/qtextdocument_p.h"
#include "qtextlist.h"
#include "qtextdocumentwriter.h"
#include "private/qtextcursor_p.h"
#include <QtCore/qloggingcategory.h>
#include <qtextformat.h>
#include <qtransform.h>
#include <qdatetime.h>
#include <qbuffer.h>
#include <qguiapplication.h>
#include <limits.h>
#include <qtexttable.h>
#include <qvariant.h>
#include <qurl.h>
#include <qstylehints.h>
#include <qmetaobject.h>
#include <private/qqmlglobal_p.h>
#include <private/qquickdeliveryagent_p_p.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 343, as _ZN24QQuickTextControlPrivate13repaintCursorEv
#if !defined(QT_NO_TEXTCONTROL)
inline void QQuickTextControlPrivate::repaintCursor()
{
    Q_Q(QQuickTextControl);
    emit q->updateCursorRequest();
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 255, as _ZN24QQuickTextControlPrivate10setContentEN2Qt10TextFormatERK7QString
#if !defined(QT_NO_TEXTCONTROL)
inline void QQuickTextControlPrivate::setContent(Qt::TextFormat format, const QString &text)
{
    Q_Q(QQuickTextControl);

#if QT_CONFIG(im)
    cancelPreedit();
#endif

    // for use when called from setPlainText. we may want to re-use the currently
    // set char format then.
    const QTextCharFormat charFormatForInsertion = cursor.charFormat();

    bool previousUndoRedoState = doc->isUndoRedoEnabled();
    doc->setUndoRedoEnabled(false);

    const int oldCursorPos = cursor.position();

    // avoid multiple textChanged() signals being emitted
    QObject::disconnect(doc, &QTextDocument::contentsChanged, q, &QQuickTextControl::textChanged);

    if (!text.isEmpty()) {
        // clear 'our' cursor for insertion to prevent
        // the emission of the cursorPositionChanged() signal.
        // instead we emit it only once at the end instead of
        // at the end of the document after loading and when
        // positioning the cursor again to the start of the
        // document.
        cursor = QTextCursor();
        if (format == Qt::PlainText) {
            QTextCursor formatCursor(doc);
            // put the setPlainText and the setCharFormat into one edit block,
            // so that the syntax highlight triggers only /once/ for the entire
            // document, not twice.
            formatCursor.beginEditBlock();
            doc->setPlainText(text);
            doc->setUndoRedoEnabled(false);
            formatCursor.select(QTextCursor::Document);
            formatCursor.setCharFormat(charFormatForInsertion);
            formatCursor.endEditBlock();
#if QT_CONFIG(textmarkdownreader)
        } else if (format == Qt::MarkdownText) {
            doc->setBaseUrl(doc->baseUrl().adjusted(QUrl::RemoveFilename));
            doc->setMarkdown(text);
#endif
        } else {
#if QT_CONFIG(texthtmlparser)
            doc->setHtml(text);
#else
            doc->setPlainText(text);
#endif
            doc->setUndoRedoEnabled(false);
        }
        cursor = QTextCursor(doc);
    } else {
        doc->clear();
    }
    cursor.setCharFormat(charFormatForInsertion);

    QObject::connect(doc, &QTextDocument::contentsChanged, q, &QQuickTextControl::textChanged);
    emit q->textChanged();
    doc->setUndoRedoEnabled(previousUndoRedoState);
    _q_updateCurrentCharFormatAndSelection();
    doc->setModified(false);

    q->updateCursorRectangle(true);
    if (cursor.position() != oldCursorPos)
        emit q->cursorPositionChanged();
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

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 667, as _ZN17QQuickTextControl3cutEv
#if !defined(QT_NO_TEXTCONTROL)
#if QT_CONFIG(clipboard)
inline void QQuickTextControl::cut()
{
    Q_D(QQuickTextControl);
    if (!(d->interactionFlags & Qt::TextEditable) || !d->cursor.hasSelection())
        return;
    copy();
    d->cursor.removeSelectedText();
}
#endif  // QT_CONFIG(clipboard)
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 676, as _ZN17QQuickTextControl4copyEv
#if !defined(QT_NO_TEXTCONTROL)
#if QT_CONFIG(clipboard)
inline void QQuickTextControl::copy()
{
    Q_D(QQuickTextControl);
    if (!d->cursor.hasSelection())
        return;
    QMimeData *data = createMimeDataFromSelection();
    QGuiApplication::clipboard()->setMimeData(data);
}
#endif  // QT_CONFIG(clipboard)
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 685, as _ZN17QQuickTextControl5pasteEN10QClipboard4ModeE
#if !defined(QT_NO_TEXTCONTROL)
#if QT_CONFIG(clipboard)
inline void QQuickTextControl::paste(QClipboard::Mode mode)
{
    const QMimeData *md = QGuiApplication::clipboard()->mimeData(mode);
    if (md)
        insertFromMimeData(md);
}
#endif  // QT_CONFIG(clipboard)
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 578, as _ZN17QQuickTextControl5clearEv
#if !defined(QT_NO_TEXTCONTROL)
inline void QQuickTextControl::clear()
{
    Q_D(QQuickTextControl);
    d->cursor.select(QTextCursor::Document);
    d->cursor.removeSelectedText();
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

//  from ../qtdeclarative/src/quick/items/qquicktextcontrol.cpp, line 768, as _ZN17QQuickTextControl5eventEP6QEvent
#if !defined(QT_NO_TEXTCONTROL)
inline bool QQuickTextControl::event(QEvent *e)
{
    return QObject::event(e);
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

#if QT_CONFIG(clipboard)
#if !defined(QT_NO_TEXTCONTROL)
//  void QQuickTextControl::cut()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextControl3cutEv(QQuickTextControl *self) {
  self->cut();
}
#endif  // !defined(QT_NO_TEXTCONTROL)
#endif  // QT_CONFIG(clipboard)

#if QT_CONFIG(clipboard)
#if !defined(QT_NO_TEXTCONTROL)
//  void QQuickTextControl::copy()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextControl4copyEv(QQuickTextControl *self) {
  self->copy();
}
#endif  // !defined(QT_NO_TEXTCONTROL)
#endif  // QT_CONFIG(clipboard)

#if QT_CONFIG(clipboard)
#if !defined(QT_NO_TEXTCONTROL)
//  void QQuickTextControl::paste(QClipboard::Mode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextControl5pasteEN10QClipboard4ModeE(
    QQuickTextControl *self,
    QClipboard::Mode mode) {
  self->paste(mode);
}
#endif  // !defined(QT_NO_TEXTCONTROL)
#endif  // QT_CONFIG(clipboard)

#if !defined(QT_NO_TEXTCONTROL)
//  void QQuickTextControl::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickTextControl5clearEv(QQuickTextControl *self) {
  self->clear();
}
#endif  // !defined(QT_NO_TEXTCONTROL)

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
