//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qwidgettextcontrol_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(widgettextcontrol)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qwidgettextcontrol_p.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qwidgettextcontrol_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtGui/qtextcursor.h>
#include <QtCore/qrect.h>
#include <QtGui/qtextobject.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
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
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/widgets/qwidgettextcontrol.cpp, line 283, as _ZN25QWidgetTextControlPrivate23updateCurrentCharFormatEv
#if !defined(QT_NO_TEXTCONTROL)
inline void QWidgetTextControlPrivate::updateCurrentCharFormat()
{
    Q_Q(QWidgetTextControl);

    QTextCharFormat fmt = cursor.charFormat();
    if (fmt == lastCharFormat)
        return;
    lastCharFormat = fmt;

    emit q->currentCharFormatChanged(fmt);
    emit q->microFocusChanged();
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from src/widgets/widgets/qwidgettextcontrol.cpp, line 296, as _ZN25QWidgetTextControlPrivate6indentEv
#if !defined(QT_NO_TEXTCONTROL)
inline void QWidgetTextControlPrivate::indent()
{
    QTextBlockFormat blockFmt = cursor.blockFormat();

    QTextList *list = cursor.currentList();
    if (!list) {
        QTextBlockFormat modifier;
        modifier.setIndent(blockFmt.indent() + 1);
        cursor.mergeBlockFormat(modifier);
    } else {
        QTextListFormat format = list->format();
        format.setIndent(format.indent() + 1);

        if (list->itemNumber(cursor.block()) == 1)
            list->setFormat(format);
        else
            cursor.createList(format);
    }
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from src/widgets/widgets/qwidgettextcontrol.cpp, line 316, as _ZN25QWidgetTextControlPrivate7outdentEv
#if !defined(QT_NO_TEXTCONTROL)
inline void QWidgetTextControlPrivate::outdent()
{
    QTextBlockFormat blockFmt = cursor.blockFormat();

    QTextList *list = cursor.currentList();

    if (!list) {
        QTextBlockFormat modifier;
        modifier.setIndent(blockFmt.indent() - 1);
        cursor.mergeBlockFormat(modifier);
    } else {
        QTextListFormat listFmt = list->format();
        listFmt.setIndent(listFmt.indent() - 1);
        list->setFormat(listFmt);
    }
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from src/widgets/widgets/qwidgettextcontrol.cpp, line 333, as _ZN25QWidgetTextControlPrivate17gotoNextTableCellEv
#if !defined(QT_NO_TEXTCONTROL)
inline void QWidgetTextControlPrivate::gotoNextTableCell()
{
    QTextTable *table = cursor.currentTable();
    QTextTableCell cell = table->cellAt(cursor);

    int newColumn = cell.column() + cell.columnSpan();
    int newRow = cell.row();

    if (newColumn >= table->columns()) {
        newColumn = 0;
        ++newRow;
        if (newRow >= table->rows())
            table->insertRows(table->rows(), 1);
    }

    cell = table->cellAt(newRow, newColumn);
    cursor = cell.firstCursorPosition();
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from src/widgets/widgets/qwidgettextcontrol.cpp, line 352, as _ZN25QWidgetTextControlPrivate21gotoPreviousTableCellEv
#if !defined(QT_NO_TEXTCONTROL)
inline void QWidgetTextControlPrivate::gotoPreviousTableCell()
{
    QTextTable *table = cursor.currentTable();
    QTextTableCell cell = table->cellAt(cursor);

    int newColumn = cell.column() - 1;
    int newRow = cell.row();

    if (newColumn < 0) {
        newColumn = table->columns() - 1;
        --newRow;
        if (newRow < 0)
            return;
    }

    cell = table->cellAt(newRow, newColumn);
    cursor = cell.firstCursorPosition();
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from src/widgets/widgets/qwidgettextcontrol.cpp, line 371, as _ZN25QWidgetTextControlPrivate20createAutoBulletListEv
#if !defined(QT_NO_TEXTCONTROL)
inline void QWidgetTextControlPrivate::createAutoBulletList()
{
    cursor.beginEditBlock();

    QTextBlockFormat blockFmt = cursor.blockFormat();

    QTextListFormat listFmt;
    listFmt.setStyle(QTextListFormat::ListDisc);
    listFmt.setIndent(blockFmt.indent() + 1);

    blockFmt.setIndent(0);
    cursor.setBlockFormat(blockFmt);

    cursor.createList(listFmt);

    cursor.endEditBlock();
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from src/widgets/widgets/qwidgettextcontrol.cpp, line 389, as _ZN25QWidgetTextControlPrivate4initEN2Qt10TextFormatERK7QStringP13QTextDocument
#if !defined(QT_NO_TEXTCONTROL)
inline void QWidgetTextControlPrivate::init(Qt::TextFormat format, const QString &text, QTextDocument *document)
{
    Q_Q(QWidgetTextControl);
    setContent(format, text, document);

    doc->setUndoRedoEnabled(interactionFlags & Qt::TextEditable);
    q->setCursorWidth(-1);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from src/widgets/widgets/qwidgettextcontrol.cpp, line 398, as _ZN25QWidgetTextControlPrivate10setContentEN2Qt10TextFormatERK7QStringP13QTextDocument
#if !defined(QT_NO_TEXTCONTROL)
inline void QWidgetTextControlPrivate::setContent(Qt::TextFormat format, const QString &text, QTextDocument *document)
{
    Q_Q(QWidgetTextControl);

    // for use when called from setPlainText. we may want to re-use the currently
    // set char format then.
    const QTextCharFormat charFormatForInsertion = cursor.charFormat();

    bool clearDocument = true;
    if (!doc) {
        if (document) {
            doc = document;
        } else {
            palette = QApplication::palette("QWidgetTextControl");
            doc = new QTextDocument(q);
        }
        clearDocument = false;
        _q_documentLayoutChanged();
        cursor = QTextCursor(doc);

// ####        doc->documentLayout()->setPaintDevice(viewport);

        QObjectPrivate::connect(doc, &QTextDocument::contentsChanged, this,
                                &QWidgetTextControlPrivate::_q_updateCurrentCharFormatAndSelection);
        QObjectPrivate::connect(doc, &QTextDocument::cursorPositionChanged, this,
                                &QWidgetTextControlPrivate::_q_emitCursorPosChanged);
        QObjectPrivate::connect(doc, &QTextDocument::documentLayoutChanged, this,
                                &QWidgetTextControlPrivate::_q_documentLayoutChanged);

        // convenience signal forwards
        QObject::connect(doc, &QTextDocument::undoAvailable, q, &QWidgetTextControl::undoAvailable);
        QObject::connect(doc, &QTextDocument::redoAvailable, q, &QWidgetTextControl::redoAvailable);
        QObject::connect(doc, &QTextDocument::modificationChanged, q,
                         &QWidgetTextControl::modificationChanged);
        QObject::connect(doc, &QTextDocument::blockCountChanged, q,
                         &QWidgetTextControl::blockCountChanged);
    }

    bool previousUndoRedoState = doc->isUndoRedoEnabled();
    if (!document)
        doc->setUndoRedoEnabled(false);

    //Saving the index save some time.
    static int contentsChangedIndex = QMetaMethod::fromSignal(&QTextDocument::contentsChanged).methodIndex();
    static int textChangedIndex = QMetaMethod::fromSignal(&QWidgetTextControl::textChanged).methodIndex();
    // avoid multiple textChanged() signals being emitted
    QMetaObject::disconnect(doc, contentsChangedIndex, q, textChangedIndex);

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
            doc->setMarkdown(text);
            doc->setUndoRedoEnabled(false);
#endif
        } else {
#ifndef QT_NO_TEXTHTMLPARSER
            doc->setHtml(text);
#else
            doc->setPlainText(text);
#endif
            doc->setUndoRedoEnabled(false);
        }
        cursor = QTextCursor(doc);
    } else if (clearDocument) {
        doc->clear();
    }
    cursor.setCharFormat(charFormatForInsertion);

    QMetaObject::connect(doc, contentsChangedIndex, q, textChangedIndex);
    emit q->textChanged();
    if (!document)
        doc->setUndoRedoEnabled(previousUndoRedoState);
    _q_updateCurrentCharFormatAndSelection();
    if (!document)
        doc->setModified(false);

    q->ensureCursorVisible();
    emit q->cursorPositionChanged();

    QObjectPrivate::connect(doc, &QTextDocument::contentsChange, this,
                            &QWidgetTextControlPrivate::_q_contentsChanged, Qt::UniqueConnection);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from src/widgets/widgets/qwidgettextcontrol.cpp, line 499, as _ZN25QWidgetTextControlPrivate9startDragEv
#if !defined(QT_NO_TEXTCONTROL)
inline void QWidgetTextControlPrivate::startDrag()
{

#ifdef Q_OS_WASM
    // QDrag::exec() will crash without asyncify; disable drag instead.
    if (!qstdweb::haveAsyncify())
        return;
#endif

#if QT_CONFIG(draganddrop)
    Q_Q(QWidgetTextControl);
    mousePressed = false;
    if (!contextWidget)
        return;
    QMimeData *data = q->createMimeDataFromSelection();

    QDrag *drag = new QDrag(contextWidget);
    drag->setMimeData(data);

    Qt::DropActions actions = Qt::CopyAction;
    Qt::DropAction action;
    if (interactionFlags & Qt::TextEditable) {
        actions |= Qt::MoveAction;
        action = drag->exec(actions, Qt::MoveAction);
    } else {
        action = drag->exec(actions, Qt::CopyAction);
    }

    if (action == Qt::MoveAction && drag->target() != contextWidget)
        cursor.removeSelectedText();
#endif
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from src/widgets/widgets/qwidgettextcontrol.cpp, line 532, as _ZN25QWidgetTextControlPrivate17setCursorPositionERK7QPointF
#if !defined(QT_NO_TEXTCONTROL)
inline void QWidgetTextControlPrivate::setCursorPosition(const QPointF &pos)
{
    Q_Q(QWidgetTextControl);
    const int cursorPos = q->hitTest(pos, Qt::FuzzyHit);
    if (cursorPos == -1)
        return;
    cursor.setPosition(cursorPos);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from src/widgets/widgets/qwidgettextcontrol.cpp, line 541, as _ZN25QWidgetTextControlPrivate17setCursorPositionEiN11QTextCursor8MoveModeE
#if !defined(QT_NO_TEXTCONTROL)
inline void QWidgetTextControlPrivate::setCursorPosition(int pos, QTextCursor::MoveMode mode)
{
    cursor.setPosition(pos, mode);

    if (mode != QTextCursor::KeepAnchor) {
        selectedWordOnDoubleClick = QTextCursor();
        selectedBlockOnTrippleClick = QTextCursor();
    }
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from src/widgets/widgets/qwidgettextcontrol.cpp, line 551, as _ZN25QWidgetTextControlPrivate13repaintCursorEv
#if !defined(QT_NO_TEXTCONTROL)
inline void QWidgetTextControlPrivate::repaintCursor()
{
    Q_Q(QWidgetTextControl);
    emit q->updateRequest(cursorRectPlusUnicodeDirectionMarkers(cursor));
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from src/widgets/widgets/qwidgettextcontrol.cpp, line 557, as _ZN25QWidgetTextControlPrivate25repaintOldAndNewSelectionERK11QTextCursor
#if !defined(QT_NO_TEXTCONTROL)
inline void QWidgetTextControlPrivate::repaintOldAndNewSelection(const QTextCursor &oldSelection)
{
    Q_Q(QWidgetTextControl);
    if (cursor.hasSelection()
        && oldSelection.hasSelection()
        && cursor.currentFrame() == oldSelection.currentFrame()
        && !cursor.hasComplexSelection()
        && !oldSelection.hasComplexSelection()
        && cursor.anchor() == oldSelection.anchor()
        ) {
        QTextCursor differenceSelection(doc);
        differenceSelection.setPosition(oldSelection.position());
        differenceSelection.setPosition(cursor.position(), QTextCursor::KeepAnchor);
        emit q->updateRequest(q->selectionRect(differenceSelection));
    } else {
        if (!oldSelection.isNull())
            emit q->updateRequest(q->selectionRect(oldSelection) | cursorRectPlusUnicodeDirectionMarkers(oldSelection));
        emit q->updateRequest(q->selectionRect() | cursorRectPlusUnicodeDirectionMarkers(cursor));
    }
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from src/widgets/widgets/qwidgettextcontrol.cpp, line 578, as _ZN25QWidgetTextControlPrivate16selectionChangedEb
#if !defined(QT_NO_TEXTCONTROL)
inline void QWidgetTextControlPrivate::selectionChanged(bool forceEmitSelectionChanged /*=false*/)
{
    Q_Q(QWidgetTextControl);
    if (forceEmitSelectionChanged) {
        emit q->selectionChanged();
#if QT_CONFIG(accessibility)
        if (q->parent() && q->parent()->isWidgetType()) {
            QAccessibleTextSelectionEvent ev(q->parent(), cursor.anchor(), cursor.position());
            QAccessible::updateAccessibility(&ev);
        }
#endif
    }

    if (cursor.position() == lastSelectionPosition
        && cursor.anchor() == lastSelectionAnchor)
        return;

    bool selectionStateChange = (cursor.hasSelection()
                                 != (lastSelectionPosition != lastSelectionAnchor));
    if (selectionStateChange)
        emit q->copyAvailable(cursor.hasSelection());

    if (!forceEmitSelectionChanged
        && (selectionStateChange
            || (cursor.hasSelection()
                && (cursor.position() != lastSelectionPosition
                    || cursor.anchor() != lastSelectionAnchor)))) {
        emit q->selectionChanged();
#if QT_CONFIG(accessibility)
        if (q->parent() && q->parent()->isWidgetType()) {
            QAccessibleTextSelectionEvent ev(q->parent(), cursor.anchor(), cursor.position());
            QAccessible::updateAccessibility(&ev);
        }
#endif
    }
    emit q->microFocusChanged();
    lastSelectionPosition = cursor.position();
    lastSelectionAnchor = cursor.anchor();
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from src/widgets/widgets/qwidgettextcontrol.cpp, line 618, as _ZN25QWidgetTextControlPrivate38_q_updateCurrentCharFormatAndSelectionEv
#if !defined(QT_NO_TEXTCONTROL)
inline void QWidgetTextControlPrivate::_q_updateCurrentCharFormatAndSelection()
{
    updateCurrentCharFormat();
    selectionChanged();
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from src/widgets/widgets/qwidgettextcontrol.cpp, line 625, as _ZN25QWidgetTextControlPrivate21setClipboardSelectionEv
#if !defined(QT_NO_TEXTCONTROL)
#if !defined(QT_NO_CLIPBOARD)
inline void QWidgetTextControlPrivate::setClipboardSelection()
{
    QClipboard *clipboard = QGuiApplication::clipboard();
    if (!cursor.hasSelection() || !clipboard->supportsSelection())
        return;
    Q_Q(QWidgetTextControl);
    QMimeData *data = q->createMimeDataFromSelection();
    clipboard->setMimeData(data, QClipboard::Selection);
}
#endif  // !defined(QT_NO_CLIPBOARD)
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from src/widgets/widgets/qwidgettextcontrol.cpp, line 636, as _ZN25QWidgetTextControlPrivate23_q_emitCursorPosChangedERK11QTextCursor
#if !defined(QT_NO_TEXTCONTROL)
inline void QWidgetTextControlPrivate::_q_emitCursorPosChanged(const QTextCursor &someCursor)
{
    Q_Q(QWidgetTextControl);
    if (someCursor.isCopyOf(cursor)) {
        emit q->cursorPositionChanged();
        emit q->microFocusChanged();
    }
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from src/widgets/widgets/qwidgettextcontrol.cpp, line 645, as _ZN25QWidgetTextControlPrivate18_q_contentsChangedEiii
#if !defined(QT_NO_TEXTCONTROL)
inline void QWidgetTextControlPrivate::_q_contentsChanged(int from, int charsRemoved, int charsAdded)
{
#if QT_CONFIG(accessibility)
    Q_Q(QWidgetTextControl);

    if (QAccessible::isActive() && q->parent() && q->parent()->isWidgetType()) {
        QTextCursor tmp(doc);
        tmp.setPosition(from);
        // when setting a new text document the length is off
        // QTBUG-32583 - characterCount is off by 1 requires the -1
        tmp.setPosition(qMin(doc->characterCount() - 1, from + charsAdded), QTextCursor::KeepAnchor);
        QString newText = tmp.selectedText();

        // always report the right number of removed chars, but in lack of the real string use spaces
        QString oldText = QString(charsRemoved, u' ');

        QAccessibleEvent *ev = nullptr;
        if (charsRemoved == 0) {
            ev = new QAccessibleTextInsertEvent(q->parent(), from, newText);
        } else if (charsAdded == 0) {
            ev = new QAccessibleTextRemoveEvent(q->parent(), from, oldText);
        } else {
            ev = new QAccessibleTextUpdateEvent(q->parent(), from, oldText, newText);
        }
        QAccessible::updateAccessibility(ev);
        delete ev;
    }
#else
    Q_UNUSED(from);
    Q_UNUSED(charsRemoved);
    Q_UNUSED(charsAdded);
#endif
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from src/widgets/widgets/qwidgettextcontrol.cpp, line 691, as _ZN25QWidgetTextControlPrivate16setCursorVisibleEb
#if !defined(QT_NO_TEXTCONTROL)
inline void QWidgetTextControlPrivate::setCursorVisible(bool visible)
{
    if (cursorVisible == visible)
        return;

    cursorVisible = visible;
    updateCursorBlinking();

    if (cursorVisible)
        connect(QGuiApplication::styleHints(), &QStyleHints::cursorFlashTimeChanged, this, &QWidgetTextControlPrivate::updateCursorBlinking);
    else
        disconnect(QGuiApplication::styleHints(), &QStyleHints::cursorFlashTimeChanged, this, &QWidgetTextControlPrivate::updateCursorBlinking);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from src/widgets/widgets/qwidgettextcontrol.cpp, line 705, as _ZN25QWidgetTextControlPrivate20updateCursorBlinkingEv
#if !defined(QT_NO_TEXTCONTROL)
inline void QWidgetTextControlPrivate::updateCursorBlinking()
{
    cursorBlinkTimer.stop();
    if (cursorVisible) {
        int flashTime = QGuiApplication::styleHints()->cursorFlashTime();
        if (flashTime >= 2)
            cursorBlinkTimer.start(flashTime / 2, q_func());
    }

    cursorOn = cursorVisible;
    repaintCursor();
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from src/widgets/widgets/qwidgettextcontrol.cpp, line 792, as _ZN25QWidgetTextControlPrivate24extendBlockwiseSelectionEi
#if !defined(QT_NO_TEXTCONTROL)
inline void QWidgetTextControlPrivate::extendBlockwiseSelection(int suggestedNewPosition)
{
    Q_Q(QWidgetTextControl);

    // if inside the initial selected line keep that
    if (suggestedNewPosition >= selectedBlockOnTrippleClick.selectionStart()
        && suggestedNewPosition <= selectedBlockOnTrippleClick.selectionEnd()) {
        q->setTextCursor(selectedBlockOnTrippleClick);
        return;
    }

    if (suggestedNewPosition < selectedBlockOnTrippleClick.position()) {
        cursor.setPosition(selectedBlockOnTrippleClick.selectionEnd());
        cursor.setPosition(suggestedNewPosition, QTextCursor::KeepAnchor);
        cursor.movePosition(QTextCursor::StartOfBlock, QTextCursor::KeepAnchor);
    } else {
        cursor.setPosition(selectedBlockOnTrippleClick.selectionStart());
        cursor.setPosition(suggestedNewPosition, QTextCursor::KeepAnchor);
        cursor.movePosition(QTextCursor::EndOfBlock, QTextCursor::KeepAnchor);
        cursor.movePosition(QTextCursor::NextCharacter, QTextCursor::KeepAnchor);
    }

    if (interactionFlags & Qt::TextSelectableByMouse) {
#ifndef QT_NO_CLIPBOARD
        setClipboardSelection();
#endif
        selectionChanged(true);
    }
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from src/widgets/widgets/qwidgettextcontrol.cpp, line 822, as _ZN25QWidgetTextControlPrivate17_q_deleteSelectedEv
#if !defined(QT_NO_TEXTCONTROL)
inline void QWidgetTextControlPrivate::_q_deleteSelected()
{
    if (!(interactionFlags & Qt::TextEditable) || !cursor.hasSelection())
        return;
    cursor.removeSelectedText();
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from src/widgets/widgets/qwidgettextcontrol.cpp, line 2398, as _ZNK25QWidgetTextControlPrivate37cursorRectPlusUnicodeDirectionMarkersERK11QTextCursor
#if !defined(QT_NO_TEXTCONTROL)
inline QRectF QWidgetTextControlPrivate::cursorRectPlusUnicodeDirectionMarkers(const QTextCursor &cursor) const
{
    if (cursor.isNull())
        return QRectF();

    return rectForPosition(cursor.position()).adjusted(-4, 0, 4, 0);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from src/widgets/widgets/qwidgettextcontrol.cpp, line 1390, as _ZNK25QWidgetTextControlPrivate15rectForPositionEi
#if !defined(QT_NO_TEXTCONTROL)
inline QRectF QWidgetTextControlPrivate::rectForPosition(int position) const
{
    Q_Q(const QWidgetTextControl);
    const QTextBlock block = doc->findBlock(position);
    if (!block.isValid())
        return QRectF();
    const QAbstractTextDocumentLayout *docLayout = doc->documentLayout();
    const QTextLayout *layout = block.layout();
    const QPointF layoutPos = q->blockBoundingRect(block).topLeft();
    int relativePos = position - block.position();
    if (preeditCursor != 0) {
        int preeditPos = layout->preeditAreaPosition();
        if (relativePos == preeditPos)
            relativePos += preeditCursor;
        else if (relativePos > preeditPos)
            relativePos += layout->preeditAreaText().size();
    }
    QTextLine line = layout->lineForTextPosition(relativePos);

    int cursorWidth;
    {
        bool ok = false;
        cursorWidth = docLayout->property("cursorWidth").toInt(&ok);
        if (!ok)
            cursorWidth = 1;
    }

    QRectF r;

    if (line.isValid()) {
        qreal x = line.cursorToX(relativePos);
        qreal w = 0;
        if (overwriteMode) {
            if (relativePos < line.textLength() - line.textStart())
                w = line.cursorToX(relativePos + 1) - x;
            else
                w = QFontMetrics(block.layout()->font()).horizontalAdvance(u' '); // in sync with QTextLine::draw()
        }
        r = QRectF(layoutPos.x() + x, layoutPos.y() + line.y(),
                   cursorWidth + w, line.height());
    } else {
        r = QRectF(layoutPos.x(), layoutPos.y(), cursorWidth, 10); // #### correct height
    }

    return r;
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from src/widgets/widgets/qwidgettextcontrol.cpp, line 2265, as _ZNK25QWidgetTextControlPrivate15anchorForCursorERK11QTextCursor
#if !defined(QT_NO_TEXTCONTROL)
inline QString QWidgetTextControlPrivate::anchorForCursor(const QTextCursor &anchorCursor) const
{
    if (anchorCursor.hasSelection()) {
        QTextCursor cursor = anchorCursor;
        if (cursor.selectionStart() != cursor.position())
            cursor.setPosition(cursor.selectionStart());
        cursor.movePosition(QTextCursor::NextCharacter);
        QTextCharFormat fmt = cursor.charFormat();
        if (fmt.isAnchor() && fmt.hasProperty(QTextFormat::AnchorHref))
            return fmt.stringProperty(QTextFormat::AnchorHref);
    }
    return QString();
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from src/widgets/widgets/qwidgettextcontrol.cpp, line 2945, as _ZN25QWidgetTextControlPrivate23updateHighlightedAnchorE7QPointF
#if !defined(QT_NO_TEXTCONTROL)
inline void QWidgetTextControlPrivate::updateHighlightedAnchor(QPointF mousePos)
{
    Q_Q(QWidgetTextControl);
    const QString anchor = q->anchorAt(mousePos);
    if (anchor != highlightedAnchor) {
        highlightedAnchor = anchor;
        emit q->linkHovered(anchor);
    }
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from src/widgets/widgets/qwidgettextcontrol.cpp, line 2955, as _ZN25QWidgetTextControlPrivate22resetHighlightedAnchorEv
#if !defined(QT_NO_TEXTCONTROL)
inline void QWidgetTextControlPrivate::resetHighlightedAnchor()
{
    Q_Q(QWidgetTextControl);
    if (!highlightedAnchor.isEmpty()) {
        highlightedAnchor.clear();
        emit q->linkHovered(QString());
    }
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from src/widgets/widgets/qwidgettextcontrol.cpp, line 1750, as _ZN25QWidgetTextControlPrivate17mouseReleaseEventEP6QEventN2Qt11MouseButtonERK7QPointF6QFlagsINS2_16KeyboardModifierEES7_IS3_ES6_
#if !defined(QT_NO_TEXTCONTROL)
inline void QWidgetTextControlPrivate::mouseReleaseEvent(QEvent *e, Qt::MouseButton button, const QPointF &pos, Qt::KeyboardModifiers modifiers,
                                            Qt::MouseButtons buttons, const QPointF &globalPos)
{
    Q_Q(QWidgetTextControl);

    const QTextCursor oldSelection = cursor;
    if (sendMouseEventToInputContext(
            e, QEvent::MouseButtonRelease, button, pos, modifiers, buttons, globalPos)) {
        repaintOldAndNewSelection(oldSelection);
        return;
    }

    const int oldCursorPos = cursor.position();

#if QT_CONFIG(draganddrop)
    if (mightStartDrag && (button & Qt::LeftButton)) {
        mousePressed = false;
        setCursorPosition(pos);
        cursor.clearSelection();
        selectionChanged();
    }
#endif
    if (mousePressed) {
        mousePressed = false;
#ifndef QT_NO_CLIPBOARD
        setClipboardSelection();
        selectionChanged(true);
    } else if (button == Qt::MiddleButton
               && (interactionFlags & Qt::TextEditable)
               && QGuiApplication::clipboard()->supportsSelection()) {
        setCursorPosition(pos);
        const QMimeData *md = QGuiApplication::clipboard()->mimeData(QClipboard::Selection);
        if (md)
            q->insertFromMimeData(md);
#endif
    }

    repaintOldAndNewSelection(oldSelection);

    if (cursor.position() != oldCursorPos) {
        emit q->cursorPositionChanged();
        emit q->microFocusChanged();
    }

    // toggle any checkbox that the user clicks
    if ((interactionFlags & Qt::TextEditable) && (button & Qt::LeftButton) &&
            (blockWithMarkerUnderMouse.isValid()) && !cursor.hasSelection()) {
        QTextBlock markerBlock = q->blockWithMarkerAt(pos);
        if (markerBlock == blockWithMarkerUnderMouse) {
            auto fmt = blockWithMarkerUnderMouse.blockFormat();
            switch (fmt.marker()) {
            case QTextBlockFormat::MarkerType::Unchecked :
                fmt.setMarker(QTextBlockFormat::MarkerType::Checked);
                break;
            case QTextBlockFormat::MarkerType::Checked:
                fmt.setMarker(QTextBlockFormat::MarkerType::Unchecked);
                break;
            default:
                break;
            }
            cursor.setBlockFormat(fmt);
        }
    }

    if (interactionFlags & Qt::LinksAccessibleByMouse) {

        // Ignore event unless left button has been pressed
        if (!(button & Qt::LeftButton)) {
            e->ignore();
            return;
        }

        const QString anchor = q->anchorAt(pos);

        // Ignore event without selection anchor
        if (anchor.isEmpty()) {
            e->ignore();
            return;
        }

        if (!cursor.hasSelection()
            || (anchor == anchorOnMousePress && hadSelectionOnMousePress)) {

            const int anchorPos = q->hitTest(pos, Qt::ExactHit);

            // Ignore event without valid anchor position
            if (anchorPos < 0) {
                e->ignore();
                return;
            }

            cursor.setPosition(anchorPos);
            activateLinkUnderCursor(std::exchange(anchorOnMousePress, QString()));
        }
    }
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from src/widgets/widgets/qwidgettextcontrol.cpp, line 1899, as _ZN25QWidgetTextControlPrivate28sendMouseEventToInputContextEP6QEventNS0_4TypeEN2Qt11MouseButtonERK7QPointF6QFlagsINS3_16KeyboardModifierEES8_IS4_ES7_
#if !defined(QT_NO_TEXTCONTROL)
inline bool QWidgetTextControlPrivate::sendMouseEventToInputContext(
        QEvent *e, QEvent::Type eventType, Qt::MouseButton button, const QPointF &pos,
        Qt::KeyboardModifiers modifiers, Qt::MouseButtons buttons, const QPointF &globalPos)
{
    Q_UNUSED(eventType);
    Q_UNUSED(button);
    Q_UNUSED(pos);
    Q_UNUSED(modifiers);
    Q_UNUSED(buttons);
    Q_UNUSED(globalPos);
#if !defined(QT_NO_IM)
    Q_Q(QWidgetTextControl);

    if (isPreediting()) {
        QTextLayout *layout = cursor.block().layout();
        int cursorPos = q->hitTest(pos, Qt::FuzzyHit) - cursor.position();

        if (cursorPos < 0 || cursorPos > layout->preeditAreaText().size())
            cursorPos = -1;

        if (cursorPos >= 0) {
            if (eventType == QEvent::MouseButtonRelease)
                QGuiApplication::inputMethod()->invokeAction(QInputMethod::Click, cursorPos);

            e->setAccepted(true);
            return true;
        }
    }
#else
    Q_UNUSED(e);
#endif
    return false;
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from src/widgets/widgets/qwidgettextcontrol.cpp, line 1933, as _ZN25QWidgetTextControlPrivate16contextMenuEventERK7QPointFS2_P7QWidget
#if !defined(QT_NO_TEXTCONTROL)
inline void QWidgetTextControlPrivate::contextMenuEvent(const QPointF &screenPos, const QPointF &docPos, QWidget *contextWidget)
{
#ifdef QT_NO_CONTEXTMENU
    Q_UNUSED(screenPos);
    Q_UNUSED(docPos);
    Q_UNUSED(contextWidget);
#else
    Q_Q(QWidgetTextControl);
    QMenu *menu = q->createStandardContextMenu(docPos, contextWidget);
    if (!menu)
        return;
    menu->setAttribute(Qt::WA_DeleteOnClose);

    if (auto *widget = qobject_cast<QWidget *>(parent)) {
        if (auto *window = widget->window()->windowHandle())
            QMenuPrivate::get(menu)->topData()->initialScreen = window->screen();
    }

    menu->popup(screenPos.toPoint());
#endif
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from src/widgets/widgets/qwidgettextcontrol.cpp, line 2242, as _ZN25QWidgetTextControlPrivate10focusEventEP11QFocusEvent
#if !defined(QT_NO_TEXTCONTROL)
inline void QWidgetTextControlPrivate::focusEvent(QFocusEvent *e)
{
    Q_Q(QWidgetTextControl);
    emit q->updateRequest(q->selectionRect());
    if (e->gotFocus()) {
        cursorOn = (interactionFlags & (Qt::TextSelectableByKeyboard | Qt::TextEditable));
        if (interactionFlags & Qt::TextEditable) {
            setCursorVisible(true);
        }
    } else {
        setCursorVisible(false);
        cursorOn = false;

        if (cursorIsFocusIndicator
            && e->reason() != Qt::ActiveWindowFocusReason
            && e->reason() != Qt::PopupFocusReason
            && cursor.hasSelection()) {
            cursor.clearSelection();
        }
    }
    hasFocus = e->gotFocus();
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from src/widgets/widgets/qwidgettextcontrol.cpp, line 1955, as _ZN25QWidgetTextControlPrivate14dragEnterEventEP6QEventPK9QMimeData
#if !defined(QT_NO_TEXTCONTROL)
inline bool QWidgetTextControlPrivate::dragEnterEvent(QEvent *e, const QMimeData *mimeData)
{
    Q_Q(QWidgetTextControl);
    if (!(interactionFlags & Qt::TextEditable) || !q->canInsertFromMimeData(mimeData)) {
        e->ignore();
        return false;
    }

    dndFeedbackCursor = QTextCursor();

    return true; // accept proposed action
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from src/widgets/widgets/qwidgettextcontrol.cpp, line 1968, as _ZN25QWidgetTextControlPrivate14dragLeaveEventEv
#if !defined(QT_NO_TEXTCONTROL)
inline void QWidgetTextControlPrivate::dragLeaveEvent()
{
    Q_Q(QWidgetTextControl);

    const QRectF crect = q->cursorRect(dndFeedbackCursor);
    dndFeedbackCursor = QTextCursor();

    if (crect.isValid())
        emit q->updateRequest(crect);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from src/widgets/widgets/qwidgettextcontrol.cpp, line 1979, as _ZN25QWidgetTextControlPrivate13dragMoveEventEP6QEventPK9QMimeDataRK7QPointF
#if !defined(QT_NO_TEXTCONTROL)
inline bool QWidgetTextControlPrivate::dragMoveEvent(QEvent *e, const QMimeData *mimeData, const QPointF &pos)
{
    Q_Q(QWidgetTextControl);
    if (!(interactionFlags & Qt::TextEditable) || !q->canInsertFromMimeData(mimeData)) {
        e->ignore();
        return false;
    }

    const int cursorPos = q->hitTest(pos, Qt::FuzzyHit);
    if (cursorPos != -1) {
        QRectF crect = q->cursorRect(dndFeedbackCursor);
        if (crect.isValid())
            emit q->updateRequest(crect);

        dndFeedbackCursor = cursor;
        dndFeedbackCursor.setPosition(cursorPos);

        crect = q->cursorRect(dndFeedbackCursor);
        emit q->updateRequest(crect);
    }

    return true; // accept proposed action
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from src/widgets/widgets/qwidgettextcontrol.cpp, line 2003, as _ZN25QWidgetTextControlPrivate9dropEventEPK9QMimeDataRK7QPointFN2Qt10DropActionEP7QObject
#if !defined(QT_NO_TEXTCONTROL)
inline bool QWidgetTextControlPrivate::dropEvent(const QMimeData *mimeData, const QPointF &pos, Qt::DropAction dropAction, QObject *source)
{
    Q_Q(QWidgetTextControl);
    dndFeedbackCursor = QTextCursor();

    if (!(interactionFlags & Qt::TextEditable) || !q->canInsertFromMimeData(mimeData))
        return false;

    repaintSelection();

    QTextCursor insertionCursor = q->cursorForPosition(pos);
    insertionCursor.beginEditBlock();

    if (dropAction == Qt::MoveAction && source == contextWidget)
        cursor.removeSelectedText();

    cursor = insertionCursor;
    q->insertFromMimeData(mimeData);
    insertionCursor.endEditBlock();
    q->ensureCursorVisible();
    return true; // accept proposed action
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from src/widgets/widgets/qwidgettextcontrol.cpp, line 2026, as _ZN25QWidgetTextControlPrivate16inputMethodEventEP17QInputMethodEvent
#if !defined(QT_NO_TEXTCONTROL)
inline void QWidgetTextControlPrivate::inputMethodEvent(QInputMethodEvent *e)
{
    Q_Q(QWidgetTextControl);
    if (!(interactionFlags & (Qt::TextEditable | Qt::TextSelectableByMouse)) || cursor.isNull()) {
        e->ignore();
        return;
    }
    bool isGettingInput = !e->commitString().isEmpty()
            || e->preeditString() != cursor.block().layout()->preeditAreaText()
            || e->replacementLength() > 0;

    if (!isGettingInput && e->attributes().isEmpty()) {
        e->ignore();
        return;
    }

    int oldCursorPos = cursor.position();

    cursor.beginEditBlock();
    if (isGettingInput) {
        cursor.removeSelectedText();
    }

    QTextBlock block;

    // insert commit string
    if (!e->commitString().isEmpty() || e->replacementLength()) {
        auto *mimeData = QInputControl::mimeDataForInputEvent(e);
        if (mimeData && q->canInsertFromMimeData(mimeData)) {
            q->insertFromMimeData(mimeData);
        } else {
            if (e->commitString().endsWith(QChar::LineFeed))
                block = cursor.block(); // Remember the block where the preedit text is
            QTextCursor c = cursor;
            c.setPosition(c.position() + e->replacementStart());
            c.setPosition(c.position() + e->replacementLength(), QTextCursor::KeepAnchor);
            c.insertText(e->commitString());
        }
    }

    for (int i = 0; i < e->attributes().size(); ++i) {
        const QInputMethodEvent::Attribute &a = e->attributes().at(i);
        if (a.type == QInputMethodEvent::Selection) {
            QTextCursor oldCursor = cursor;
            int blockStart = a.start + cursor.block().position();
            cursor.setPosition(blockStart, QTextCursor::MoveAnchor);
            cursor.setPosition(blockStart + a.length, QTextCursor::KeepAnchor);
            q->ensureCursorVisible();
            repaintOldAndNewSelection(oldCursor);
        }
    }

    if (!block.isValid())
        block = cursor.block();
    QTextLayout *layout = block.layout();
    if (isGettingInput)
        layout->setPreeditArea(cursor.position() - block.position(), e->preeditString());
    QList<QTextLayout::FormatRange> overrides;
    overrides.reserve(e->attributes().size());
    const int oldPreeditCursor = preeditCursor;
    preeditCursor = e->preeditString().size();
    hideCursor = false;
    for (int i = 0; i < e->attributes().size(); ++i) {
        const QInputMethodEvent::Attribute &a = e->attributes().at(i);
        if (a.type == QInputMethodEvent::Cursor) {
            preeditCursor = a.start;
            hideCursor = !a.length;
        } else if (a.type == QInputMethodEvent::TextFormat) {
            QTextCharFormat f = cursor.charFormat();
            f.merge(qvariant_cast<QTextFormat>(a.value).toCharFormat());
            if (f.isValid()) {
                QTextLayout::FormatRange o;
                o.start = a.start + cursor.position() - block.position();
                o.length = a.length;
                o.format = f;

                // Make sure list is sorted by start index
                QList<QTextLayout::FormatRange>::iterator it = overrides.end();
                while (it != overrides.begin()) {
                    QList<QTextLayout::FormatRange>::iterator previous = it - 1;
                    if (o.start >= previous->start) {
                        overrides.insert(it, o);
                        break;
                    }
                    it = previous;
                }

                if (it == overrides.begin())
                    overrides.prepend(o);
            }
        }
    }

    if (cursor.charFormat().isValid()) {
        int start = cursor.position() - block.position();
        int end = start + e->preeditString().size();

        QList<QTextLayout::FormatRange>::iterator it = overrides.begin();
        while (it != overrides.end()) {
            QTextLayout::FormatRange range = *it;
            int rangeStart = range.start;
            if (rangeStart > start) {
                QTextLayout::FormatRange o;
                o.start = start;
                o.length = rangeStart - start;
                o.format = cursor.charFormat();
                it = overrides.insert(it, o) + 1;
            }

            ++it;
            start = range.start + range.length;
        }

        if (start < end) {
            QTextLayout::FormatRange o;
            o.start = start;
            o.length = end - start;
            o.format = cursor.charFormat();
            overrides.append(o);
        }
    }
    layout->setFormats(overrides);

    cursor.endEditBlock();

    if (cursor.d)
        cursor.d->setX();
    if (oldCursorPos != cursor.position())
        emit q->cursorPositionChanged();
    if (oldPreeditCursor != preeditCursor)
        emit q->microFocusChanged();
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from src/widgets/widgets/qwidgettextcontrol.cpp, line 2876, as _ZN25QWidgetTextControlPrivate23activateLinkUnderCursorE7QString
#if !defined(QT_NO_TEXTCONTROL)
inline void QWidgetTextControlPrivate::activateLinkUnderCursor(QString href)
{
    QTextCursor oldCursor = cursor;

    if (href.isEmpty()) {
        QTextCursor tmp = cursor;
        if (tmp.selectionStart() != tmp.position())
            tmp.setPosition(tmp.selectionStart());
        tmp.movePosition(QTextCursor::NextCharacter);
        href = tmp.charFormat().anchorHref();
    }
    if (href.isEmpty())
        return;

    if (!cursor.hasSelection()) {
        QTextBlock block = cursor.block();
        const int cursorPos = cursor.position();

        QTextBlock::Iterator it = block.begin();
        QTextBlock::Iterator linkFragment;

        for (; !it.atEnd(); ++it) {
            QTextFragment fragment = it.fragment();
            const int fragmentPos = fragment.position();
            if (fragmentPos <= cursorPos &&
                fragmentPos + fragment.length() > cursorPos) {
                linkFragment = it;
                break;
            }
        }

        if (!linkFragment.atEnd()) {
            it = linkFragment;
            cursor.setPosition(it.fragment().position());
            if (it != block.begin()) {
                do {
                    --it;
                    QTextFragment fragment = it.fragment();
                    if (fragment.charFormat().anchorHref() != href)
                        break;
                    cursor.setPosition(fragment.position());
                } while (it != block.begin());
            }

            for (it = linkFragment; !it.atEnd(); ++it) {
                QTextFragment fragment = it.fragment();
                if (fragment.charFormat().anchorHref() != href)
                    break;
                cursor.setPosition(fragment.position() + fragment.length(), QTextCursor::KeepAnchor);
            }
        }
    }

    if (hasFocus) {
        cursorIsFocusIndicator = true;
    } else {
        cursorIsFocusIndicator = false;
        cursor.clearSelection();
    }
    repaintOldAndNewSelection(oldCursor);

#ifndef QT_NO_DESKTOPSERVICES
    if (openExternalLinks)
        QDesktopServices::openUrl(QUrl{href});
    else
#endif
        emit q_func()->linkActivated(href);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from src/widgets/widgets/qwidgettextcontrol.cpp, line 2965, as _ZN25QWidgetTextControlPrivate11showToolTipERK6QPointRK7QPointFP7QWidget
#if !defined(QT_NO_TEXTCONTROL)
#if QT_CONFIG(tooltip)
inline void QWidgetTextControlPrivate::showToolTip(const QPoint &globalPos, const QPointF &pos, QWidget *contextWidget)
{
    const QString toolTip = q_func()->cursorForPosition(pos).charFormat().toolTip();
    if (toolTip.isEmpty())
        return;
    QToolTip::showText(globalPos, toolTip, contextWidget);
}
#endif  // QT_CONFIG(tooltip)
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from src/widgets/widgets/qwidgettextcontrol.cpp, line 2974, as _ZNK25QWidgetTextControlPrivate12isPreeditingEv
#if !defined(QT_NO_TEXTCONTROL)
inline bool QWidgetTextControlPrivate::isPreediting() const
{
    QTextLayout *layout = cursor.block().layout();
    if (layout && !layout->preeditAreaText().isEmpty())
        return true;

    return false;
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from src/widgets/widgets/qwidgettextcontrol.cpp, line 2983, as _ZN25QWidgetTextControlPrivate13commitPreeditEv
#if !defined(QT_NO_TEXTCONTROL)
inline void QWidgetTextControlPrivate::commitPreedit()
{
    if (!isPreediting())
        return;

    QGuiApplication::inputMethod()->commit();

    if (!isPreediting())
        return;

    cursor.beginEditBlock();
    preeditCursor = 0;
    QTextBlock block = cursor.block();
    QTextLayout *layout = block.layout();
    layout->setPreeditArea(-1, QString());
    layout->clearFormats();
    cursor.endEditBlock();
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from src/widgets/widgets/qwidgettextcontrol.cpp, line 3194, as _ZN25QWidgetTextControlPrivate24insertParagraphSeparatorEv
#if !defined(QT_NO_TEXTCONTROL)
inline void QWidgetTextControlPrivate::insertParagraphSeparator()
{
    // clear blockFormat properties that the user is unlikely to want duplicated:
    // - don't insert <hr/> automatically
    // - the next paragraph after a heading should be a normal paragraph
    // - remove the bottom margin from the last list item before appending
    // - the next checklist item after a checked item should be unchecked
    auto blockFmt = cursor.blockFormat();
    auto charFmt = cursor.charFormat();
    blockFmt.clearProperty(QTextFormat::BlockTrailingHorizontalRulerWidth);
    if (blockFmt.hasProperty(QTextFormat::HeadingLevel)) {
        blockFmt.clearProperty(QTextFormat::HeadingLevel);
        charFmt = QTextCharFormat();
    }
    if (cursor.currentList()) {
        auto existingFmt = cursor.blockFormat();
        existingFmt.clearProperty(QTextBlockFormat::BlockBottomMargin);
        cursor.setBlockFormat(existingFmt);
        if (blockFmt.marker() == QTextBlockFormat::MarkerType::Checked)
            blockFmt.setMarker(QTextBlockFormat::MarkerType::Unchecked);
    }

    // After a blank line, reset block and char formats. I.e. you can end a list,
    // block quote, etc. by hitting enter twice, and get back to normal paragraph style.
    if (cursor.block().text().isEmpty() &&
            !cursor.blockFormat().hasProperty(QTextFormat::BlockTrailingHorizontalRulerWidth) &&
            !cursor.blockFormat().hasProperty(QTextFormat::BlockCodeLanguage)) {
        blockFmt = QTextBlockFormat();
        const bool blockFmtChanged = (cursor.blockFormat() != blockFmt);
        charFmt = QTextCharFormat();
        cursor.setBlockFormat(blockFmt);
        cursor.setCharFormat(charFmt);
        // If the user hit enter twice just to get back to default format,
        // don't actually insert a new block. But if the user then hits enter
        // yet again, the block format will not change, so we will insert a block.
        // This is what many word processors do.
        if (blockFmtChanged)
            return;
    }

    cursor.insertBlock(blockFmt, charFmt);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from src/widgets/widgets/qwidgettextcontrol.cpp, line 3237, as _ZN25QWidgetTextControlPrivate6appendERK7QStringN2Qt10TextFormatE
#if !defined(QT_NO_TEXTCONTROL)
inline void QWidgetTextControlPrivate::append(const QString &text, Qt::TextFormat format)
{
    QTextCursor tmp(doc);
    tmp.beginEditBlock();
    tmp.movePosition(QTextCursor::End);

    if (!doc->isEmpty())
        tmp.insertBlock(cursor.blockFormat(), cursor.charFormat());
    else
        tmp.setCharFormat(cursor.charFormat());

    // preserve the char format
    QTextCharFormat oldCharFormat = cursor.charFormat();

#ifndef QT_NO_TEXTHTMLPARSER
    if (format == Qt::RichText || (format == Qt::AutoText && Qt::mightBeRichText(text))) {
        tmp.insertHtml(text);
    } else {
        tmp.insertText(text);
    }
#else
    Q_UNUSED(format);
    tmp.insertText(text);
#endif // QT_NO_TEXTHTMLPARSER
    if (!cursor.hasSelection())
        cursor.setCharFormat(oldCharFormat);

    tmp.endEditBlock();
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from src/widgets/widgets/qwidgettextcontrol.cpp, line 3378, as _ZN25QWidgetTextControlPrivate11_q_copyLinkEv
#if !defined(QT_NO_TEXTCONTROL)
inline void QWidgetTextControlPrivate::_q_copyLink()
{
#ifndef QT_NO_CLIPBOARD
    QMimeData *md = new QMimeData;
    md->setText(linkToCopy);
    QGuiApplication::clipboard()->setMimeData(md);
#endif
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from src/widgets/widgets/qwidgettextcontrol.cpp, line 1382, as _ZN25QWidgetTextControlPrivate14_q_updateBlockERK10QTextBlock
#if !defined(QT_NO_TEXTCONTROL)
inline void QWidgetTextControlPrivate::_q_updateBlock(const QTextBlock &block)
{
    Q_Q(QWidgetTextControl);
    QRectF br = q->blockBoundingRect(block);
    br.setRight(qreal(INT_MAX)); // the block might have shrunk
    emit q->updateRequest(br);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

//  from src/widgets/widgets/qwidgettextcontrol.cpp, line 679, as _ZN25QWidgetTextControlPrivate24_q_documentLayoutChangedEv
#if !defined(QT_NO_TEXTCONTROL)
inline void QWidgetTextControlPrivate::_q_documentLayoutChanged()
{
    Q_Q(QWidgetTextControl);
    QAbstractTextDocumentLayout *layout = doc->documentLayout();
    QObject::connect(layout, &QAbstractTextDocumentLayout::update, q,
                     &QWidgetTextControl::updateRequest);
    QObjectPrivate::connect(layout, &QAbstractTextDocumentLayout::updateBlock, this,
                            &QWidgetTextControlPrivate::_q_updateBlock);
    QObject::connect(layout, &QAbstractTextDocumentLayout::documentSizeChanged, q,
                     &QWidgetTextControl::documentSizeChanged);
}
#endif  // !defined(QT_NO_TEXTCONTROL)
//  -----------------------------------------------------------------------

//  QWidgetTextControl *QWidgetTextControlPrivate::q_func()
extern "C" Q_DECL_EXPORT
QWidgetTextControl *ritual_ZN25QWidgetTextControlPrivate6q_funcEv(
    QWidgetTextControlPrivate *self) {
  return self->q_func();
}

//  const QWidgetTextControl *QWidgetTextControlPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QWidgetTextControl *ritual_ZNK25QWidgetTextControlPrivate6q_funcEv(
    const QWidgetTextControlPrivate *self) {
  return self->q_func();
}

#if !defined(QT_NO_TEXTCONTROL)
//  void QWidgetTextControlPrivate::updateCurrentCharFormat()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWidgetTextControlPrivate23updateCurrentCharFormatEv(
    QWidgetTextControlPrivate *self) {
  self->updateCurrentCharFormat();
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  void QWidgetTextControlPrivate::indent()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWidgetTextControlPrivate6indentEv(
    QWidgetTextControlPrivate *self) {
  self->indent();
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  void QWidgetTextControlPrivate::outdent()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWidgetTextControlPrivate7outdentEv(
    QWidgetTextControlPrivate *self) {
  self->outdent();
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  void QWidgetTextControlPrivate::gotoNextTableCell()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWidgetTextControlPrivate17gotoNextTableCellEv(
    QWidgetTextControlPrivate *self) {
  self->gotoNextTableCell();
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  void QWidgetTextControlPrivate::gotoPreviousTableCell()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWidgetTextControlPrivate21gotoPreviousTableCellEv(
    QWidgetTextControlPrivate *self) {
  self->gotoPreviousTableCell();
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  void QWidgetTextControlPrivate::createAutoBulletList()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWidgetTextControlPrivate20createAutoBulletListEv(
    QWidgetTextControlPrivate *self) {
  self->createAutoBulletList();
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  void QWidgetTextControlPrivate::init(Qt::TextFormat format, const QString
//      &text, QTextDocument *document)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWidgetTextControlPrivate4initEN2Qt10TextFormatERK7QStringP13QTextDocument(
    QWidgetTextControlPrivate *self,
    Qt::TextFormat format,
    const QString *text,
    QTextDocument *document) {
  self->init(format, *text, document);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  void QWidgetTextControlPrivate::setContent(Qt::TextFormat format, const
//      QString &text, QTextDocument *document)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWidgetTextControlPrivate10setContentEN2Qt10TextFormatERK7QStringP13QTextDocument(
    QWidgetTextControlPrivate *self,
    Qt::TextFormat format,
    const QString *text,
    QTextDocument *document) {
  self->setContent(format, *text, document);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  void QWidgetTextControlPrivate::startDrag()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWidgetTextControlPrivate9startDragEv(
    QWidgetTextControlPrivate *self) {
  self->startDrag();
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  void QWidgetTextControlPrivate::setCursorPosition(const QPointF &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWidgetTextControlPrivate17setCursorPositionERK7QPointF(
    QWidgetTextControlPrivate *self,
    const QPointF *pos) {
  self->setCursorPosition(*pos);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  void QWidgetTextControlPrivate::setCursorPosition(int pos,
//      QTextCursor::MoveMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWidgetTextControlPrivate17setCursorPositionEiN11QTextCursor8MoveModeE(
    QWidgetTextControlPrivate *self,
    int pos,
    QTextCursor::MoveMode mode) {
  self->setCursorPosition(pos, mode);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  void QWidgetTextControlPrivate::repaintCursor()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWidgetTextControlPrivate13repaintCursorEv(
    QWidgetTextControlPrivate *self) {
  self->repaintCursor();
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  void QWidgetTextControlPrivate::repaintSelection()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWidgetTextControlPrivate16repaintSelectionEv(
    QWidgetTextControlPrivate *self) {
  self->repaintSelection();
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  void QWidgetTextControlPrivate::repaintOldAndNewSelection(const
//      QTextCursor &oldSelection)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWidgetTextControlPrivate25repaintOldAndNewSelectionERK11QTextCursor(
    QWidgetTextControlPrivate *self,
    const QTextCursor *oldSelection) {
  self->repaintOldAndNewSelection(*oldSelection);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  void QWidgetTextControlPrivate::selectionChanged(bool
//      forceEmitSelectionChanged)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWidgetTextControlPrivate16selectionChangedEb(
    QWidgetTextControlPrivate *self,
    bool forceEmitSelectionChanged) {
  self->selectionChanged(forceEmitSelectionChanged);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  void QWidgetTextControlPrivate::_q_updateCurrentCharFormatAndSelection()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWidgetTextControlPrivate38_q_updateCurrentCharFormatAndSelectionEv(
    QWidgetTextControlPrivate *self) {
  self->_q_updateCurrentCharFormatAndSelection();
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_CLIPBOARD)
#if !defined(QT_NO_TEXTCONTROL)
//  void QWidgetTextControlPrivate::setClipboardSelection()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWidgetTextControlPrivate21setClipboardSelectionEv(
    QWidgetTextControlPrivate *self) {
  self->setClipboardSelection();
}
#endif  // !defined(QT_NO_TEXTCONTROL)
#endif  // !defined(QT_NO_CLIPBOARD)

#if !defined(QT_NO_TEXTCONTROL)
//  void QWidgetTextControlPrivate::_q_emitCursorPosChanged(const QTextCursor
//      &someCursor)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWidgetTextControlPrivate23_q_emitCursorPosChangedERK11QTextCursor(
    QWidgetTextControlPrivate *self,
    const QTextCursor *someCursor) {
  self->_q_emitCursorPosChanged(*someCursor);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  void QWidgetTextControlPrivate::_q_contentsChanged(int from, int
//      charsRemoved, int charsAdded)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWidgetTextControlPrivate18_q_contentsChangedEiii(
    QWidgetTextControlPrivate *self,
    int from,
    int charsRemoved,
    int charsAdded) {
  self->_q_contentsChanged(from, charsRemoved, charsAdded);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  void QWidgetTextControlPrivate::setCursorVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWidgetTextControlPrivate16setCursorVisibleEb(
    QWidgetTextControlPrivate *self,
    bool visible) {
  self->setCursorVisible(visible);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  void QWidgetTextControlPrivate::updateCursorBlinking()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWidgetTextControlPrivate20updateCursorBlinkingEv(
    QWidgetTextControlPrivate *self) {
  self->updateCursorBlinking();
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
#if !defined(QT_NO_CLIPBOARD)
//  void QWidgetTextControlPrivate::extendBlockwiseSelection(int
//      suggestedNewPosition)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWidgetTextControlPrivate24extendBlockwiseSelectionEi(
    QWidgetTextControlPrivate *self,
    int suggestedNewPosition) {
  self->extendBlockwiseSelection(suggestedNewPosition);
}
#endif  // !defined(QT_NO_CLIPBOARD)
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  void QWidgetTextControlPrivate::_q_deleteSelected()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWidgetTextControlPrivate17_q_deleteSelectedEv(
    QWidgetTextControlPrivate *self) {
  self->_q_deleteSelected();
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  QRectF
//      QWidgetTextControlPrivate::cursorRectPlusUnicodeDirectionMarkers(cons
//      t QTextCursor &cursor) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK25QWidgetTextControlPrivate37cursorRectPlusUnicodeDirectionMarkersERK11QTextCursor(
    const QWidgetTextControlPrivate *self,
    const QTextCursor *cursor) {
  return new QRectF(self->cursorRectPlusUnicodeDirectionMarkers(*cursor));
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  QRectF QWidgetTextControlPrivate::rectForPosition(int position) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK25QWidgetTextControlPrivate15rectForPositionEi(
    const QWidgetTextControlPrivate *self,
    int position) {
  return new QRectF(self->rectForPosition(position));
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  QString QWidgetTextControlPrivate::anchorForCursor(const QTextCursor
//      &anchor) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK25QWidgetTextControlPrivate15anchorForCursorERK11QTextCursor(
    const QWidgetTextControlPrivate *self,
    const QTextCursor *anchor) {
  return new QString(self->anchorForCursor(*anchor));
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  void QWidgetTextControlPrivate::updateHighlightedAnchor(QPointF mousePos)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWidgetTextControlPrivate23updateHighlightedAnchorE7QPointF(
    QWidgetTextControlPrivate *self,
    const QPointF *mousePos) {
  self->updateHighlightedAnchor(*mousePos);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  void QWidgetTextControlPrivate::resetHighlightedAnchor()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWidgetTextControlPrivate22resetHighlightedAnchorEv(
    QWidgetTextControlPrivate *self) {
  self->resetHighlightedAnchor();
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
#if !defined(QT_NO_CLIPBOARD)
//  void QWidgetTextControlPrivate::mouseReleaseEvent(QEvent *e,
//      Qt::MouseButton button, const QPointF &pos, Qt::KeyboardModifiers
//      modifiers, Qt::MouseButtons buttons, const QPointF &globalPos)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWidgetTextControlPrivate17mouseReleaseEventEP6QEventN2Qt11MouseButtonERK7QPointF6QFlagsINS2_16KeyboardModifierEES7_IS3_ES6_(
    QWidgetTextControlPrivate *self,
    QEvent *e,
    Qt::MouseButton button,
    const QPointF *pos,
    int modifiers,
    int buttons,
    const QPointF *globalPos) {
  self->mouseReleaseEvent(
      e,
      button,
      *pos,
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers),
      QFlags<Qt::MouseButton>::fromInt(buttons),
      *globalPos);
}
#endif  // !defined(QT_NO_CLIPBOARD)
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  bool QWidgetTextControlPrivate::sendMouseEventToInputContext(QEvent *e,
//      QEvent::Type eventType, Qt::MouseButton button, const QPointF &pos,
//      Qt::KeyboardModifiers modifiers, Qt::MouseButtons buttons, const
//      QPointF &globalPos)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QWidgetTextControlPrivate28sendMouseEventToInputContextEP6QEventNS0_4TypeEN2Qt11MouseButtonERK7QPointF6QFlagsINS3_16KeyboardModifierEES8_IS4_ES7_(
    QWidgetTextControlPrivate *self,
    QEvent *e,
    QEvent::Type eventType,
    Qt::MouseButton button,
    const QPointF *pos,
    int modifiers,
    int buttons,
    const QPointF *globalPos) {
  return self->sendMouseEventToInputContext(
      e,
      eventType,
      button,
      *pos,
      QFlags<Qt::KeyboardModifier>::fromInt(modifiers),
      QFlags<Qt::MouseButton>::fromInt(buttons),
      *globalPos);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  void QWidgetTextControlPrivate::contextMenuEvent(const QPointF
//      &screenPos, const QPointF &docPos, QWidget *contextWidget)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWidgetTextControlPrivate16contextMenuEventERK7QPointFS2_P7QWidget(
    QWidgetTextControlPrivate *self,
    const QPointF *screenPos,
    const QPointF *docPos,
    QWidget *contextWidget) {
  self->contextMenuEvent(*screenPos, *docPos, contextWidget);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  void QWidgetTextControlPrivate::focusEvent(QFocusEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWidgetTextControlPrivate10focusEventEP11QFocusEvent(
    QWidgetTextControlPrivate *self,
    QFocusEvent *e) {
  self->focusEvent(e);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  bool QWidgetTextControlPrivate::dragEnterEvent(QEvent *e, const QMimeData
//      *mimeData)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QWidgetTextControlPrivate14dragEnterEventEP6QEventPK9QMimeData(
    QWidgetTextControlPrivate *self,
    QEvent *e,
    const QMimeData *mimeData) {
  return self->dragEnterEvent(e, mimeData);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  void QWidgetTextControlPrivate::dragLeaveEvent()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWidgetTextControlPrivate14dragLeaveEventEv(
    QWidgetTextControlPrivate *self) {
  self->dragLeaveEvent();
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  bool QWidgetTextControlPrivate::dragMoveEvent(QEvent *e, const QMimeData
//      *mimeData, const QPointF &pos)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QWidgetTextControlPrivate13dragMoveEventEP6QEventPK9QMimeDataRK7QPointF(
    QWidgetTextControlPrivate *self,
    QEvent *e,
    const QMimeData *mimeData,
    const QPointF *pos) {
  return self->dragMoveEvent(e, mimeData, *pos);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  bool QWidgetTextControlPrivate::dropEvent(const QMimeData *mimeData,
//      const QPointF &pos, Qt::DropAction dropAction, QObject *source)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QWidgetTextControlPrivate9dropEventEPK9QMimeDataRK7QPointFN2Qt10DropActionEP7QObject(
    QWidgetTextControlPrivate *self,
    const QMimeData *mimeData,
    const QPointF *pos,
    Qt::DropAction dropAction,
    QObject *source) {
  return self->dropEvent(mimeData, *pos, dropAction, source);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  void QWidgetTextControlPrivate::inputMethodEvent(QInputMethodEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWidgetTextControlPrivate16inputMethodEventEP17QInputMethodEvent(
    QWidgetTextControlPrivate *self,
    QInputMethodEvent *a0) {
  self->inputMethodEvent(a0);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  void QWidgetTextControlPrivate::activateLinkUnderCursor(QString href)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWidgetTextControlPrivate23activateLinkUnderCursorE7QString(
    QWidgetTextControlPrivate *self,
    const QString *href) {
  self->activateLinkUnderCursor(*href);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if QT_CONFIG(tooltip)
#if !defined(QT_NO_TEXTCONTROL)
//  void QWidgetTextControlPrivate::showToolTip(const QPoint &globalPos,
//      const QPointF &pos, QWidget *contextWidget)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWidgetTextControlPrivate11showToolTipERK6QPointRK7QPointFP7QWidget(
    QWidgetTextControlPrivate *self,
    const QPoint *globalPos,
    const QPointF *pos,
    QWidget *contextWidget) {
  self->showToolTip(*globalPos, *pos, contextWidget);
}
#endif  // !defined(QT_NO_TEXTCONTROL)
#endif  // QT_CONFIG(tooltip)

#if !defined(QT_NO_TEXTCONTROL)
//  bool QWidgetTextControlPrivate::isPreediting() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QWidgetTextControlPrivate12isPreeditingEv(
    const QWidgetTextControlPrivate *self) {
  return self->isPreediting();
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  void QWidgetTextControlPrivate::commitPreedit()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWidgetTextControlPrivate13commitPreeditEv(
    QWidgetTextControlPrivate *self) {
  self->commitPreedit();
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  void QWidgetTextControlPrivate::insertParagraphSeparator()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWidgetTextControlPrivate24insertParagraphSeparatorEv(
    QWidgetTextControlPrivate *self) {
  self->insertParagraphSeparator();
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  void QWidgetTextControlPrivate::append(const QString &text,
//      Qt::TextFormat format)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWidgetTextControlPrivate6appendERK7QStringN2Qt10TextFormatE(
    QWidgetTextControlPrivate *self,
    const QString *text,
    Qt::TextFormat format) {
  self->append(*text, format);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  void QWidgetTextControlPrivate::_q_copyLink()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWidgetTextControlPrivate11_q_copyLinkEv(
    QWidgetTextControlPrivate *self) {
  self->_q_copyLink();
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  void QWidgetTextControlPrivate::_q_updateBlock(const QTextBlock &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWidgetTextControlPrivate14_q_updateBlockERK10QTextBlock(
    QWidgetTextControlPrivate *self,
    const QTextBlock *a0) {
  self->_q_updateBlock(*a0);
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#if !defined(QT_NO_TEXTCONTROL)
//  void QWidgetTextControlPrivate::_q_documentLayoutChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QWidgetTextControlPrivate24_q_documentLayoutChangedEv(
    QWidgetTextControlPrivate *self) {
  self->_q_documentLayoutChanged();
}
#endif  // !defined(QT_NO_TEXTCONTROL)

#endif  // QT_CONFIG(widgettextcontrol)
