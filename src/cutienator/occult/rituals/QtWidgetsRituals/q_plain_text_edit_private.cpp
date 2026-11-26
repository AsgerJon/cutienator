//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qplaintextedit_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: added are 1 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(textedit)
#if QT_CONFIG(textedit)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qplaintextedit.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qplaintextedit_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformbackingstore.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/qabstractscrollarea.h>
#if QT_CONFIG(scrollarea)
#include <QtWidgets/qscrollbar.h>
#include <QtWidgets/qapplication.h>
#include <QtWidgets/qstyle.h>
#include <QtWidgets/qstyleoption.h>
#include <QtGui/qevent.h>
#include <QtCore/qdebug.h>
#include <QtWidgets/qboxlayout.h>
#include <QtGui/qpainter.h>
#include <QtCore/qmargins.h>
#if QT_CONFIG(itemviews)
#include <QtWidgets/qheaderview.h>
#endif
#include <QtCore/QDebug>
#include <QtWidgets/private/qabstractscrollarea_p.h>
#include <QtWidgets/private/qscrollbar_p.h>
#include <QtWidgets/qwidget.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/qpa/qplatformtheme.h>
#include <QtWidgets/private/qapplication_p.h>
#ifdef Q_OS_WIN
#  include <QtCore/qt_windows.h>
#endif
#endif
#include <QtWidgets/private/qplaintextedit_p.h>
#include <QtGui/qfont.h>
#include <QtGui/qpainter.h>
#include <QtGui/qevent.h>
#include <QtCore/qdebug.h>
#if QT_CONFIG(draganddrop)
#include <QtGui/qdrag.h>
#endif
#include <QtGui/qclipboard.h>
#include <QtCore/qmath.h>
#if QT_CONFIG(menu)
#include <QtWidgets/qmenu.h>
#endif
#include <QtWidgets/qstyle.h>
#include <QtWidgets/private/qapplication_p.h>
#include <QtGui/private/qtextdocumentlayout_p.h>
#include <QtGui/private/qabstracttextdocumentlayout_p.h>
#include <QtGui/qtextdocument.h>
#include <QtGui/private/qtextdocument_p.h>
#include <QtGui/qtextlist.h>
#include <QtGui/qaccessible.h>
#include <QtGui/qtextformat.h>
#include <QtCore/qdatetime.h>
#include <QtWidgets/qapplication.h>
#include <limits.h>
#include <QtGui/qtexttable.h>
#include <QtCore/qvariant.h>
#include <QtWidgets/qframe.h>
#include <QtGui/qbitmap.h>
#include <QtWidgets/qdrawutil.h>
#include <QtGui/qevent.h>
#include <QtGui/qpainter.h>
#include <QtWidgets/qstyle.h>
#include <QtWidgets/qstyleoption.h>
#include <QtWidgets/qstylepainter.h>
#include <QtWidgets/qapplication.h>
#include <QtWidgets/private/qframe_p.h>
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

//  from src/widgets/widgets/qplaintextedit.cpp, line 48, as local:qplaintextedit.cpp:QPlainTextDocumentLayoutPrivate
class QPlainTextDocumentLayoutPrivate : public QAbstractTextDocumentLayoutPrivate
{
    Q_DECLARE_PUBLIC(QPlainTextDocumentLayout)
public:
    QPlainTextDocumentLayoutPrivate() {
        mainViewPrivate = nullptr;
        width = 0;
        maximumWidth = 0;
        maximumWidthBlockNumber = 0;
        blockCount = 1;
        blockUpdate = blockDocumentSizeChanged = false;
        cursorWidth = 1;
        textLayoutFlags = 0;
    }

    qreal width;
    qreal maximumWidth;
    int maximumWidthBlockNumber;
    int blockCount;
    QPlainTextEditPrivate *mainViewPrivate;
    bool blockUpdate;
    bool blockDocumentSizeChanged;
    int cursorWidth;
    int textLayoutFlags;

    void layoutBlock(const QTextBlock &block);
    qreal blockWidth(const QTextBlock &block);

    void relayout();
};

//  from src/widgets/widgets/qplaintextedit.cpp, line 243, as local:qplaintextedit.cpp:QPlainTextDocumentLayoutPrivate::relayout
inline void QPlainTextDocumentLayoutPrivate::relayout()
{
    Q_Q(QPlainTextDocumentLayout);
    QTextBlock block = q->document()->firstBlock();
    while (block.isValid()) {
        block.layout()->clearLayout();
        block.setLineCount(block.isVisible() ? 1 : 0);
        block = block.next();
    }
    emit q->update();
}

//  from src/widgets/widgets/qabstractscrollarea.cpp, line 133, as _ZN26QAbstractScrollAreaPrivateC2Ev
#if QT_CONFIG(scrollarea)
inline QAbstractScrollAreaPrivate::QAbstractScrollAreaPrivate()
    :hbar(nullptr), vbar(nullptr), vbarpolicy(Qt::ScrollBarAsNeeded), hbarpolicy(Qt::ScrollBarAsNeeded),
     shownOnce(false), inResize(false), sizeAdjustPolicy(QAbstractScrollArea::AdjustIgnored),
     viewport(nullptr), cornerWidget(nullptr), left(0), top(0), right(0), bottom(0),
     xoffset(0), yoffset(0), viewportFilter(nullptr)
{
}
#endif  // QT_CONFIG(scrollarea)

//  from src/widgets/widgets/qabstractscrollarea.cpp, line 141, as _ZN26QAbstractScrollAreaPrivateD2Ev
#if QT_CONFIG(scrollarea)
inline QAbstractScrollAreaPrivate::~QAbstractScrollAreaPrivate()
{
}
#endif  // QT_CONFIG(scrollarea)

//  from src/widgets/widgets/qabstractscrollarea.cpp, line 1368, as _ZNK26QAbstractScrollAreaPrivate14contentsOffsetEv
#if QT_CONFIG(scrollarea)
inline QPoint QAbstractScrollAreaPrivate::contentsOffset() const
{
    Q_Q(const QAbstractScrollArea);
    QPoint offset;
    if (vbar->isVisible())
        offset.setY(vbar->value());
    if (hbar->isVisible()) {
        if (q->isRightToLeft())
            offset.setX(hbar->maximum() - hbar->value());
        else
            offset.setX(hbar->value());
    }
    return offset;
}
#endif  // QT_CONFIG(scrollarea)

//  from src/widgets/widgets/qabstractscrollarea.cpp, line 1315, as _ZNK26QAbstractScrollAreaPrivate19canStartScrollingAtERK6QPoint
#if QT_CONFIG(scrollarea)
inline bool QAbstractScrollAreaPrivate::canStartScrollingAt(const QPoint &startPos) const
{
    Q_Q(const QAbstractScrollArea);

    // don't start scrolling on a QAbstractSlider
    if (qobject_cast<QAbstractSlider *>(q->viewport()->childAt(startPos)))
        return false;

    return true;
}
#endif  // QT_CONFIG(scrollarea)

//  from src/widgets/widgets/qplaintextedit.cpp, line 414, as _ZN21QPlainTextEditControlC1EP14QPlainTextEdit
inline QPlainTextEditControl::QPlainTextEditControl(QPlainTextEdit *parent)
    : QWidgetTextControl(parent), textEdit(parent),
      topBlock(0)
{
    setAcceptRichText(false);
}

//  from src/widgets/widgets/qplaintextedit.cpp, line 945, as _ZN21QPlainTextEditPrivate16adjustScrollbarsEv
#if QT_CONFIG(scrollbar)
inline void QPlainTextEditPrivate::adjustScrollbars()
{
    Q_Q(QPlainTextEdit);
    QTextDocument *doc = control->document();
    QPlainTextDocumentLayout *documentLayout = qobject_cast<QPlainTextDocumentLayout*>(doc->documentLayout());
    Q_ASSERT(documentLayout);
    bool documentSizeChangedBlocked = documentLayout->priv()->blockDocumentSizeChanged;
    documentLayout->priv()->blockDocumentSizeChanged = true;
    qreal margin = doc->documentMargin();

    int vmax = 0;

    int vSliderLength = 0;
    if (!centerOnScroll && q->isVisible()) {
        QTextBlock block = doc->lastBlock();
        const qreal visible = viewport->rect().height() - margin - 1;
        qreal y = 0;
        int visibleFromBottom = 0;

        while (block.isValid()) {
            if (!block.isVisible()) {
                block = block.previous();
                continue;
            }
            y += documentLayout->blockBoundingRect(block).height();

            QTextLayout *layout = block.layout();
            int layoutLineCount = layout->lineCount();
            if (y > visible) {
                int lineNumber = 0;
                while (lineNumber < layoutLineCount) {
                    QTextLine line = layout->lineAt(lineNumber);
                    const QRectF lr = line.naturalTextRect();
                    if (lr.top() >= y - visible)
                        break;
                    ++lineNumber;
                }
                if (lineNumber < layoutLineCount)
                    visibleFromBottom += (layoutLineCount - lineNumber);
                break;

            }
            visibleFromBottom += layoutLineCount;
            block = block.previous();
        }
        vmax = qMax(0, doc->lineCount() - visibleFromBottom);
        vSliderLength = visibleFromBottom;

    } else {
        vmax = qMax(0, doc->lineCount() - 1);
        int lineSpacing = q->fontMetrics().lineSpacing();
        vSliderLength = lineSpacing != 0 ? viewport->height() / lineSpacing : 0;
    }

    QSizeF documentSize = documentLayout->documentSize();
    vbar->setRange(0, qMax(0, vmax));
    vbar->setPageStep(vSliderLength);
    int visualTopLine = vmax;
    QTextBlock firstVisibleBlock = q->firstVisibleBlock();
    if (firstVisibleBlock.isValid())
        visualTopLine = firstVisibleBlock.firstLineNumber() + topLine;

    vbar->setValue(visualTopLine);

    hbar->setRange(0, (int)documentSize.width() - viewport->width());
    hbar->setPageStep(viewport->width());
    documentLayout->priv()->blockDocumentSizeChanged = documentSizeChangedBlocked;
    setTopLine(vbar->value());
}
#endif  // QT_CONFIG(scrollbar)

//  from src/widgets/widgets/qabstractscrollarea.cpp, line 1485, as _ZNK26QAbstractScrollAreaPrivate17defaultSingleStepEv
#if QT_CONFIG(scrollarea)
inline int QAbstractScrollAreaPrivate::defaultSingleStep() const
{
    auto *platformTheme = QGuiApplicationPrivate::platformTheme();
    return platformTheme->themeHint(QPlatformTheme::ScrollSingleStepDistance).value<int>();
}
#endif  // QT_CONFIG(scrollarea)

//  from src/widgets/widgets/qframe.cpp, line 19, as _ZN13QFramePrivateC2Ev
inline QFramePrivate::QFramePrivate()
    : frect(0, 0, 0, 0),
      frameStyle(QFrame::NoFrame | QFrame::Plain),
      lineWidth(1),
      midLineWidth(0),
      frameWidth(0),
      leftFrameWidth(0), rightFrameWidth(0),
      topFrameWidth(0), bottomFrameWidth(0)
{
}

//  from src/widgets/widgets/qframe.cpp, line 30, as _ZN13QFramePrivateD2Ev
inline QFramePrivate::~QFramePrivate()
{
}

//  from src/widgets/widgets/qplaintextedit.cpp, line 727, as _ZN21QPlainTextEditPrivateC1Ev
inline QPlainTextEditPrivate::QPlainTextEditPrivate()
    : tabChangesFocus(false)
    , showCursorOnInitialShow(false)
    , backgroundVisible(false)
    , centerOnScroll(false)
    , inDrag(false)
    , clickCausedFocus(false)
    , pageUpDownLastCursorYIsValid(false)
    , placeholderTextShown(false)
{
}

//  from src/widgets/widgets/qplaintextedit.cpp, line 739, as _ZN21QPlainTextEditPrivate4initERK7QString
inline void QPlainTextEditPrivate::init(const QString &txt)
{
    Q_Q(QPlainTextEdit);
    control = new QPlainTextEditControl(q);

    QTextDocument *doc = new QTextDocument(control);
    QAbstractTextDocumentLayout *layout = new QPlainTextDocumentLayout(doc);
    doc->setDocumentLayout(layout);
    control->setDocument(doc);

    control->setPalette(q->palette());

    QObjectPrivate::connect(vbar, &QAbstractSlider::actionTriggered,
                            this, &QPlainTextEditPrivate::verticalScrollbarActionTriggered);
    QObject::connect(control, &QWidgetTextControl::microFocusChanged, q,
                     [q](){q->updateMicroFocus(); });
    QObjectPrivate::connect(control, &QWidgetTextControl::documentSizeChanged,
                            this, &QPlainTextEditPrivate::adjustScrollbars);
    QObject::connect(control, &QWidgetTextControl::blockCountChanged,
                     q, &QPlainTextEdit::blockCountChanged);
    QObjectPrivate::connect(control, &QWidgetTextControl::updateRequest,
                            this, &QPlainTextEditPrivate::repaintContents);
    QObject::connect(control, &QWidgetTextControl::modificationChanged,
                     q, &QPlainTextEdit::modificationChanged);
    QObject::connect(control, &QWidgetTextControl::textChanged, q, &QPlainTextEdit::textChanged);
    QObject::connect(control, &QWidgetTextControl::undoAvailable, q, &QPlainTextEdit::undoAvailable);
    QObject::connect(control, &QWidgetTextControl::redoAvailable, q, &QPlainTextEdit::redoAvailable);
    QObject::connect(control, &QWidgetTextControl::copyAvailable, q, &QPlainTextEdit::copyAvailable);
    QObject::connect(control, &QWidgetTextControl::selectionChanged, q, &QPlainTextEdit::selectionChanged);
    QObjectPrivate::connect(control, &QWidgetTextControl::cursorPositionChanged,
                            this, &QPlainTextEditPrivate::cursorPositionChanged);
    QObjectPrivate::connect(control, &QWidgetTextControl::textChanged,
                            this, &QPlainTextEditPrivate::updatePlaceholderVisibility);
    QObject::connect(control, &QWidgetTextControl::textChanged, q, [q](){q->updateMicroFocus(); });

    // set a null page size initially to avoid any relayouting until the textedit
    // is shown. relayoutDocument() will take care of setting the page size to the
    // viewport dimensions later.
    doc->setTextWidth(-1);
    doc->documentLayout()->setPaintDevice(viewport);
    doc->setDefaultFont(q->font());


    if (!txt.isEmpty())
        control->setPlainText(txt);

    hbar->setSingleStep(defaultSingleStep());
    vbar->setSingleStep(1);

    viewport->setBackgroundRole(QPalette::Base);
    q->setAcceptDrops(true);
    q->setFocusPolicy(Qt::StrongFocus);
    q->setAttribute(Qt::WA_KeyCompression);
    q->setAttribute(Qt::WA_InputMethodEnabled);
    q->setInputMethodHints(Qt::ImhMultiLine);

#ifndef QT_NO_CURSOR
    viewport->setCursor(Qt::IBeamCursor);
#endif
}

//  from src/widgets/widgets/qplaintextedit.cpp, line 812, as _ZN21QPlainTextEditPrivate15repaintContentsERK6QRectF
inline void QPlainTextEditPrivate::repaintContents(const QRectF &contentsRect)
{
    Q_Q(QPlainTextEdit);
    if (!contentsRect.isValid()) {
        updateViewport();
        return;
    }
    const int xOffset = horizontalOffset();
    const int yOffset = (int)verticalOffset();
    const QRect visibleRect(xOffset, yOffset, viewport->width(), viewport->height());

    QRect r = contentsRect.adjusted(-1, -1, 1, 1).intersected(visibleRect).toAlignedRect();
    if (r.isEmpty())
        return;

    r.translate(-xOffset, -yOffset);
    viewport->update(r);
    emit q->updateRequest(r, 0);
}

//  from src/widgets/widgets/qplaintextedit.cpp, line 800, as _ZN21QPlainTextEditPrivate27updatePlaceholderVisibilityEv
inline void QPlainTextEditPrivate::updatePlaceholderVisibility()
{
    // We normally only repaint the part of view that contains text in the
    // document that has changed (in repaintContents). But the placeholder
    // text is not a part of the document, but is drawn on separately. So whenever
    // we either show or hide the placeholder text, we issue a full update.
    if (placeholderTextShown != placeHolderTextToBeShown()) {
        viewport->update();
        placeholderTextShown = placeHolderTextToBeShown();
    }
}

//  from src/widgets/widgets/qplaintextedit.cpp, line 432, as _ZN21QPlainTextEditPrivate32verticalScrollbarActionTriggeredEi
inline void QPlainTextEditPrivate::verticalScrollbarActionTriggered(int action) {

    const auto a = static_cast<QAbstractSlider::SliderAction>(action);
    switch (a) {
    case QAbstractSlider::SliderPageStepAdd:
        pageUpDown(QTextCursor::Down, QTextCursor::MoveAnchor, false);
        break;
    case QAbstractSlider::SliderPageStepSub:
        pageUpDown(QTextCursor::Up, QTextCursor::MoveAnchor, false);
        break;
    default:
        break;
    }
}

//  from src/widgets/widgets/qplaintextedit.cpp, line 1018, as _ZN21QPlainTextEditPrivate22ensureViewportLayoutedEv
inline void QPlainTextEditPrivate::ensureViewportLayouted()
{
}

//  from src/widgets/widgets/qplaintextedit.cpp, line 832, as _ZN21QPlainTextEditPrivate10pageUpDownEN11QTextCursor13MoveOperationENS0_8MoveModeEb
inline void QPlainTextEditPrivate::pageUpDown(QTextCursor::MoveOperation op, QTextCursor::MoveMode moveMode, bool moveCursor)
{

    Q_Q(QPlainTextEdit);

    QTextCursor cursor = control->textCursor();
    if (moveCursor) {
        ensureCursorVisible();
        if (!pageUpDownLastCursorYIsValid)
            pageUpDownLastCursorY = control->cursorRect(cursor).top() - verticalOffset();
    }

    qreal lastY = pageUpDownLastCursorY;


    if (op == QTextCursor::Down) {
        QRectF visible = QRectF(viewport->rect()).translated(-q->contentOffset());
        QTextBlock firstVisibleBlock = q->firstVisibleBlock();
        QTextBlock block = firstVisibleBlock;
        QRectF br = q->blockBoundingRect(block);
        qreal h = 0;
        int atEnd = false;
        while (h + br.height() <= visible.bottom()) {
            if (!block.next().isValid()) {
                atEnd = true;
                lastY = visible.bottom(); // set cursor to last line
                break;
            }
            h += br.height();
            block = block.next();
            br = q->blockBoundingRect(block);
        }

        if (!atEnd) {
            int line = 0;
            qreal diff = visible.bottom() - h;
            int lineCount = block.layout()->lineCount();
            while (line < lineCount - 1) {
                if (block.layout()->lineAt(line).naturalTextRect().bottom() > diff) {
                    // the first line that did not completely fit the screen
                    break;
                }
                ++line;
            }
            setTopBlock(block.blockNumber(), line);
        }

        if (moveCursor) {
            // move using movePosition to keep the cursor's x
            lastY += verticalOffset();
            bool moved = false;
            do {
                moved = cursor.movePosition(op, moveMode);
            } while (moved && control->cursorRect(cursor).top() < lastY);
        }

    } else if (op == QTextCursor::Up) {

        QRectF visible = QRectF(viewport->rect()).translated(-q->contentOffset());
        visible.translate(0, -visible.height()); // previous page
        QTextBlock block = q->firstVisibleBlock();
        qreal h = 0;
        while (h >= visible.top()) {
            if (!block.previous().isValid()) {
                if (control->topBlock == 0 && topLine == 0) {
                    lastY = 0; // set cursor to first line
                }
                break;
            }
            block = block.previous();
            QRectF br = q->blockBoundingRect(block);
            h -= br.height();
        }

        int line = 0;
        if (block.isValid()) {
            qreal diff = visible.top() - h;
            int lineCount = block.layout()->lineCount();
            while (line < lineCount) {
                if (block.layout()->lineAt(line).naturalTextRect().top() >= diff)
                    break;
                ++line;
            }
            if (line == lineCount) {
                if (block.next().isValid() && block.next() != q->firstVisibleBlock()) {
                    block = block.next();
                    line = 0;
                } else {
                    --line;
                }
            }
        }
        setTopBlock(block.blockNumber(), line);

        if (moveCursor) {
            cursor.setVisualNavigation(true);
            // move using movePosition to keep the cursor's x
            lastY += verticalOffset();
            bool moved = false;
            do {
                moved = cursor.movePosition(op, moveMode);
            } while (moved && control->cursorRect(cursor).top() > lastY);
        }
    }

    if (moveCursor) {
        control->setTextCursor(cursor, moveMode == QTextCursor::KeepAnchor);
        pageUpDownLastCursorYIsValid = true;
    }
}

//  from src/widgets/widgets/qplaintextedit.cpp, line 467, as _ZNK21QPlainTextEditPrivate14verticalOffsetEii
inline qreal QPlainTextEditPrivate::verticalOffset(int topBlock, int topLine) const
{
    qreal offset = 0;
    QTextDocument *doc = control->document();

    if (topLine) {
        QTextBlock currentBlock = doc->findBlockByNumber(topBlock);
        QPlainTextDocumentLayout *documentLayout = qobject_cast<QPlainTextDocumentLayout*>(doc->documentLayout());
        Q_ASSERT(documentLayout);
        QRectF r = documentLayout->blockBoundingRect(currentBlock);
        Q_UNUSED(r);
        QTextLayout *layout = currentBlock.layout();
        if (layout && topLine <= layout->lineCount()) {
            QTextLine line = layout->lineAt(topLine - 1);
            const QRectF lr = line.naturalTextRect();
            offset = lr.bottom();
        }
    }
    if (topBlock == 0 && topLine == 0)
        offset -= doc->documentMargin(); // top margin
    return offset;
}

//  from src/widgets/widgets/qplaintextedit.cpp, line 491, as _ZNK21QPlainTextEditPrivate14verticalOffsetEv
inline qreal QPlainTextEditPrivate::verticalOffset() const {
    return verticalOffset(control->topBlock, topLine) + topLineFracture;
}

//  from src/widgets/widgets/qplaintextedit.cpp, line 1903, as _ZN21QPlainTextEditPrivate23updateDefaultTextOptionEv
inline void QPlainTextEditPrivate::updateDefaultTextOption()
{
    QTextDocument *doc = control->document();

    QTextOption opt = doc->defaultTextOption();
    QTextOption::WrapMode oldWrapMode = opt.wrapMode();

    if (lineWrap == QPlainTextEdit::NoWrap)
        opt.setWrapMode(QTextOption::NoWrap);
    else
        opt.setWrapMode(wordWrap);

    if (opt.wrapMode() != oldWrapMode)
        doc->setDefaultTextOption(opt);
}

//  from src/widgets/widgets/qplaintextedit.cpp, line 606, as _ZN21QPlainTextEditPrivate10setTopLineEii
inline void QPlainTextEditPrivate::setTopLine(int visualTopLine, int dx)
{
    QTextDocument *doc = control->document();
    QTextBlock block = doc->findBlockByLineNumber(visualTopLine);
    int blockNumber = block.blockNumber();
    int lineNumber = visualTopLine - block.firstLineNumber();
    setTopBlock(blockNumber, lineNumber, dx);
}

//  from src/widgets/widgets/qplaintextedit.cpp, line 615, as _ZN21QPlainTextEditPrivate11setTopBlockEiii
inline void QPlainTextEditPrivate::setTopBlock(int blockNumber, int lineNumber, int dx)
{
    Q_Q(QPlainTextEdit);
    blockNumber = qMax(0, blockNumber);
    lineNumber = qMax(0, lineNumber);
    QTextDocument *doc = control->document();
    QTextBlock block = doc->findBlockByNumber(blockNumber);

    int newTopLine = block.firstLineNumber() + lineNumber;
    int maxTopLine = vbar->maximum();

    if (newTopLine > maxTopLine) {
        block = doc->findBlockByLineNumber(maxTopLine);
        blockNumber = block.blockNumber();
        lineNumber = maxTopLine - block.firstLineNumber();
    }

    vbar->setValue(newTopLine);

    if (!dx && blockNumber == control->topBlock && lineNumber == topLine)
        return;

    if (viewport->updatesEnabled() && viewport->isVisible()) {
        int dy = 0;
        if (doc->findBlockByNumber(control->topBlock).isValid()) {
            qreal realdy = -q->blockBoundingGeometry(block).y()
                    + verticalOffset() - verticalOffset(blockNumber, lineNumber);
            dy = (int)realdy;
            topLineFracture = realdy - dy;
        }
        control->topBlock = blockNumber;
        topLine = lineNumber;

        vbar->setValue(block.firstLineNumber() + lineNumber);

        if (dx || dy) {
            viewport->scroll(q->isRightToLeft() ? -dx : dx, dy);
            QGuiApplication::inputMethod()->update(Qt::ImCursorRectangle | Qt::ImAnchorRectangle);
        } else {
            viewport->update();
            topLineFracture = 0;
        }
        emit q->updateRequest(viewport->rect(), dy);
    } else {
        control->topBlock = blockNumber;
        topLine = lineNumber;
        topLineFracture = 0;
    }

}

//  from src/widgets/widgets/qplaintextedit.cpp, line 668, as _ZN21QPlainTextEditPrivate13ensureVisibleEibb
inline void QPlainTextEditPrivate::ensureVisible(int position, bool center, bool forceCenter) {
    Q_Q(QPlainTextEdit);
    QRectF visible = QRectF(viewport->rect()).translated(-q->contentOffset());
    QTextBlock block = control->document()->findBlock(position);
    if (!block.isValid())
        return;
    QRectF br = control->blockBoundingRect(block);
    if (!br.isValid())
        return;
    QTextLine line = block.layout()->lineForTextPosition(position - block.position());
    Q_ASSERT(line.isValid());
    QRectF lr = line.naturalTextRect().translated(br.topLeft());

    if (lr.bottom() >= visible.bottom() || (center && lr.top() < visible.top()) || forceCenter){

        qreal height = visible.height();
        if (center)
            height /= 2;

        qreal h = center ? line.naturalTextRect().center().y() : line.naturalTextRect().bottom();

        QTextBlock previousVisibleBlock = block;
        while (h < height && block.previous().isValid()) {
            previousVisibleBlock = block;
            do {
                block = block.previous();
            } while (!block.isVisible() && block.previous().isValid());
            h += q->blockBoundingRect(block).height();
        }

        int l = 0;
        int lineCount = block.layout()->lineCount();
        qreal voffset = verticalOffset(block.blockNumber(), 0);
        while (l < lineCount) {
            QRectF lineRect = block.layout()->lineAt(l).naturalTextRect();
            if (h - voffset - lineRect.top() <= height)
                break;
            ++l;
        }

        if (l >= lineCount) {
            block = previousVisibleBlock;
            l = 0;
        }
        setTopBlock(block.blockNumber(), l);
    } else if (lr.top() < visible.top()) {
        setTopBlock(block.blockNumber(), line.lineNumber());
    }

}

//  from src/widgets/widgets/qplaintextedit.cpp, line 2944, as _ZN21QPlainTextEditPrivate19ensureCursorVisibleEb
inline void QPlainTextEditPrivate::ensureCursorVisible(bool center)
{
    Q_Q(QPlainTextEdit);
    QRect visible = viewport->rect();
    QRect cr = q->cursorRect();
    if (cr.top() < visible.top() || cr.bottom() > visible.bottom()) {
        ensureVisible(control->textCursor().position(), center);
    }

    const bool rtl = q->isRightToLeft();
    if (cr.left() < visible.left() || cr.right() > visible.right()) {
        int x = cr.center().x() + horizontalOffset() - visible.width()/2;
        hbar->setValue(rtl ? hbar->maximum() - x : x);
    }
}

//  from src/widgets/widgets/qplaintextedit.cpp, line 720, as _ZN21QPlainTextEditPrivate14updateViewportEv
inline void QPlainTextEditPrivate::updateViewport()
{
    Q_Q(QPlainTextEdit);
    viewport->update();
    emit q->updateRequest(viewport->rect(), 0);
}

//  from src/widgets/widgets/qplaintextedit.cpp, line 421, as _ZN21QPlainTextEditPrivate21cursorPositionChangedEv
inline void QPlainTextEditPrivate::cursorPositionChanged()
{
    pageUpDownLastCursorYIsValid = false;
    Q_Q(QPlainTextEdit);
#if QT_CONFIG(accessibility)
    QAccessibleTextCursorEvent ev(q, q->textCursor().position());
    QAccessible::updateAccessibility(&ev);
#endif
    emit q->cursorPositionChanged();
}
//  -----------------------------------------------------------------------

//  A QPlainTextEditPrivate that Python can take functions over in. Every QPlainTextEditPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(scrollarea)
typedef void (*CuteQPlainTextEditPrivateCall0)(const void *, int, int, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef bool (*CuteQPlainTextEditPrivateCall1)(const void *, const QPoint *, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef const QPoint * (*CuteQPlainTextEditPrivateCall2)(const void *, int *);
#endif  // QT_CONFIG(scrollarea)
typedef void (*CuteQPlainTextEditPrivateCall3)(const void *, bool, int *);
typedef void (*CuteQPlainTextEditPrivateCall4)(const void *, int, int *);
typedef void (*CuteQPlainTextEditPrivateCall5)(const void *, int *);
typedef void (*CuteQPlainTextEditPrivateCall6)(const void *, int *);
typedef void * (*CuteQPlainTextEditPrivateCall7)(const void *, int *);
typedef const QPlatformBackingStoreRhiConfig * (*CuteQPlainTextEditPrivateCall8)(const void *, int *);
typedef const QWidgetPrivate::TextureData * (*CuteQPlainTextEditPrivateCall9)(const void *, int *);
typedef int (*CuteQPlainTextEditPrivateCall10)(const void *, int *);
typedef const QImage * (*CuteQPlainTextEditPrivateCall11)(const void *, int *);
typedef void (*CuteQPlainTextEditPrivateCall12)(const void *, int *);
typedef void (*CuteQPlainTextEditPrivateCall13)(const void *, int *);
typedef void (*CuteQPlainTextEditPrivateCall14)(const void *, int *);
typedef void (*CuteQPlainTextEditPrivateCall15)(const void *, int *);
typedef void (*CuteQPlainTextEditPrivateCall16)(const void *, int *);
typedef void (*CuteQPlainTextEditPrivateCall17)(const void *, int *);
typedef void (*CuteQPlainTextEditPrivateCall18)(const void *, int *);
typedef bool (*CuteQPlainTextEditPrivateCall19)(const void *, int *);
typedef bool (*CuteQPlainTextEditPrivateCall20)(const void *, int *);
class CuteQPlainTextEditPrivate : public QPlainTextEditPrivate {
public:
  using QPlainTextEditPrivate::QPlainTextEditPrivate;
  void *taken[21] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN26QAbstractScrollAreaPrivate22scrollBarPolicyChangedEN2Qt11OrientationENS0_15ScrollBarPolicyE")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZNK26QAbstractScrollAreaPrivate19canStartScrollingAtERK6QPoint")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZNK26QAbstractScrollAreaPrivate14contentsOffsetEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN14QWidgetPrivate10setVisibleEb")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate14setWindowFlagsE6QFlagsIN2Qt10WindowTypeEE")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate14aboutToDestroyEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate8recreateEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate11focusObjectEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWidgetPrivate9rhiConfigEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWidgetPrivate7textureEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate16textureListFlagsEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate15grabFramebufferEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate25beginBackingStorePaintingEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate23endBackingStorePaintingEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate12beginComposeEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate10endComposeEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate29initializeViewportFramebufferEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate25resizeViewportFramebufferEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate14resolveSamplesEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate15isStereoEnabledEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate24toggleStereoTargetBufferEv")) {
      taken[20] = call;
      return true;
    }
    return false;
  }

#if QT_CONFIG(scrollarea)
  //  void
  //      QAbstractScrollAreaPrivate::scrollBarPolicyChanged(Qt::Orientatio
  //      n a0, Qt::ScrollBarPolicy a1)
  void scrollBarPolicyChanged(
      Qt::Orientation a0,
      Qt::ScrollBarPolicy a1) override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlainTextEditPrivateCall0 call = reinterpret_cast<CuteQPlainTextEditPrivateCall0>(taken[0]);
      call(this, static_cast<int>(a0), static_cast<int>(a1), &handled);
      if (handled) return;
    }
    QAbstractScrollAreaPrivate::scrollBarPolicyChanged(a0, a1);
  }
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
  //  bool QAbstractScrollAreaPrivate::canStartScrollingAt(const QPoint
  //      &startPos) const
  bool canStartScrollingAt(const QPoint &startPos) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlainTextEditPrivateCall1 call = reinterpret_cast<CuteQPlainTextEditPrivateCall1>(taken[1]);
      bool given = call(this, &startPos, &handled);
      if (handled) return given;
    }
    return QAbstractScrollAreaPrivate::canStartScrollingAt(startPos);
  }
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
  //  QPoint QAbstractScrollAreaPrivate::contentsOffset() const
  QPoint contentsOffset() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQPlainTextEditPrivateCall2 call = reinterpret_cast<CuteQPlainTextEditPrivateCall2>(taken[2]);
      const QPoint * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractScrollAreaPrivate::contentsOffset();
  }
#endif  // QT_CONFIG(scrollarea)

  //  void QWidgetPrivate::setVisible(bool a0)
  void setVisible(bool a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQPlainTextEditPrivateCall3 call = reinterpret_cast<CuteQPlainTextEditPrivateCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidgetPrivate::setVisible(a0);
  }

  //  void QWidgetPrivate::setWindowFlags(Qt::WindowFlags windowFlags)
  void setWindowFlags(Qt::WindowFlags windowFlags) override {
    if (taken[4]) {
      int handled = 0;
      CuteQPlainTextEditPrivateCall4 call = reinterpret_cast<CuteQPlainTextEditPrivateCall4>(taken[4]);
      call(this, static_cast<int>(windowFlags.toInt()), &handled);
      if (handled) return;
    }
    QWidgetPrivate::setWindowFlags(windowFlags);
  }

  //  void QWidgetPrivate::aboutToDestroy()
  void aboutToDestroy() override {
    if (taken[5]) {
      int handled = 0;
      CuteQPlainTextEditPrivateCall5 call = reinterpret_cast<CuteQPlainTextEditPrivateCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::aboutToDestroy();
  }

  //  void QWidgetPrivate::recreate()
  void recreate() override {
    if (taken[6]) {
      int handled = 0;
      CuteQPlainTextEditPrivateCall6 call = reinterpret_cast<CuteQPlainTextEditPrivateCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::recreate();
  }

  //  QObject *QWidgetPrivate::focusObject()
  QObject *focusObject() override {
    if (taken[7]) {
      int handled = 0;
      CuteQPlainTextEditPrivateCall7 call = reinterpret_cast<CuteQPlainTextEditPrivateCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWidgetPrivate::focusObject();
  }

  //  QPlatformBackingStoreRhiConfig QWidgetPrivate::rhiConfig() const
  QPlatformBackingStoreRhiConfig rhiConfig() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQPlainTextEditPrivateCall8 call = reinterpret_cast<CuteQPlainTextEditPrivateCall8>(taken[8]);
      const QPlatformBackingStoreRhiConfig * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::rhiConfig();
  }

  //  TextureData QWidgetPrivate::texture() const
  QWidgetPrivate::TextureData texture() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQPlainTextEditPrivateCall9 call = reinterpret_cast<CuteQPlainTextEditPrivateCall9>(taken[9]);
      const QWidgetPrivate::TextureData * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::texture();
  }

  //  QPlatformTextureList::Flags QWidgetPrivate::textureListFlags()
  QPlatformTextureList::Flags textureListFlags() override {
    if (taken[10]) {
      int handled = 0;
      CuteQPlainTextEditPrivateCall10 call = reinterpret_cast<CuteQPlainTextEditPrivateCall10>(taken[10]);
      int given = call(this, &handled);
      if (handled) return QFlags<QPlatformTextureList::Flag>::fromInt(given);
    }
    return QWidgetPrivate::textureListFlags();
  }

  //  QImage QWidgetPrivate::grabFramebuffer()
  QImage grabFramebuffer() override {
    if (taken[11]) {
      int handled = 0;
      CuteQPlainTextEditPrivateCall11 call = reinterpret_cast<CuteQPlainTextEditPrivateCall11>(taken[11]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::grabFramebuffer();
  }

  //  void QWidgetPrivate::beginBackingStorePainting()
  void beginBackingStorePainting() override {
    if (taken[12]) {
      int handled = 0;
      CuteQPlainTextEditPrivateCall12 call = reinterpret_cast<CuteQPlainTextEditPrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginBackingStorePainting();
  }

  //  void QWidgetPrivate::endBackingStorePainting()
  void endBackingStorePainting() override {
    if (taken[13]) {
      int handled = 0;
      CuteQPlainTextEditPrivateCall13 call = reinterpret_cast<CuteQPlainTextEditPrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endBackingStorePainting();
  }

  //  void QWidgetPrivate::beginCompose()
  void beginCompose() override {
    if (taken[14]) {
      int handled = 0;
      CuteQPlainTextEditPrivateCall14 call = reinterpret_cast<CuteQPlainTextEditPrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginCompose();
  }

  //  void QWidgetPrivate::endCompose()
  void endCompose() override {
    if (taken[15]) {
      int handled = 0;
      CuteQPlainTextEditPrivateCall15 call = reinterpret_cast<CuteQPlainTextEditPrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endCompose();
  }

  //  void QWidgetPrivate::initializeViewportFramebuffer()
  void initializeViewportFramebuffer() override {
    if (taken[16]) {
      int handled = 0;
      CuteQPlainTextEditPrivateCall16 call = reinterpret_cast<CuteQPlainTextEditPrivateCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::initializeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resizeViewportFramebuffer()
  void resizeViewportFramebuffer() override {
    if (taken[17]) {
      int handled = 0;
      CuteQPlainTextEditPrivateCall17 call = reinterpret_cast<CuteQPlainTextEditPrivateCall17>(taken[17]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resizeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resolveSamples()
  void resolveSamples() override {
    if (taken[18]) {
      int handled = 0;
      CuteQPlainTextEditPrivateCall18 call = reinterpret_cast<CuteQPlainTextEditPrivateCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resolveSamples();
  }

  //  bool QWidgetPrivate::isStereoEnabled()
  bool isStereoEnabled() override {
    if (taken[19]) {
      int handled = 0;
      CuteQPlainTextEditPrivateCall19 call = reinterpret_cast<CuteQPlainTextEditPrivateCall19>(taken[19]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::isStereoEnabled();
  }

  //  bool QWidgetPrivate::toggleStereoTargetBuffer()
  bool toggleStereoTargetBuffer() override {
    if (taken[20]) {
      int handled = 0;
      CuteQPlainTextEditPrivateCall20 call = reinterpret_cast<CuteQPlainTextEditPrivateCall20>(taken[20]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::toggleStereoTargetBuffer();
  }
};

//  QPlainTextEdit *QPlainTextEditPrivate::q_func()
extern "C" Q_DECL_EXPORT
QPlainTextEdit *ritual_ZN21QPlainTextEditPrivate6q_funcEv(
    QPlainTextEditPrivate *self) {
  return self->q_func();
}

//  const QPlainTextEdit *QPlainTextEditPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QPlainTextEdit *ritual_ZNK21QPlainTextEditPrivate6q_funcEv(
    const QPlainTextEditPrivate *self) {
  return self->q_func();
}

#if QT_CONFIG(scrollarea)
//  QPlainTextEditPrivate::QPlainTextEditPrivate()
extern "C" Q_DECL_EXPORT
QPlainTextEditPrivate *ritual_ZN21QPlainTextEditPrivateC1Ev() {
  return new CuteQPlainTextEditPrivate();
}
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollbar)
#if QT_CONFIG(scrollarea)
//  void QPlainTextEditPrivate::init(const QString &txt)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlainTextEditPrivate4initERK7QString(
    QPlainTextEditPrivate *self,
    const QString *txt) {
  self->init(*txt);
}
#endif  // QT_CONFIG(scrollarea)
#endif  // QT_CONFIG(scrollbar)

//  void QPlainTextEditPrivate::repaintContents(const QRectF &contentsRect)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlainTextEditPrivate15repaintContentsERK6QRectF(
    QPlainTextEditPrivate *self,
    const QRectF *contentsRect) {
  self->repaintContents(*contentsRect);
}

//  void QPlainTextEditPrivate::updatePlaceholderVisibility()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlainTextEditPrivate27updatePlaceholderVisibilityEv(
    QPlainTextEditPrivate *self) {
  self->updatePlaceholderVisibility();
}

//  QPoint QPlainTextEditPrivate::mapToContents(const QPoint &point) const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK21QPlainTextEditPrivate13mapToContentsERK6QPoint(
    const QPlainTextEditPrivate *self,
    const QPoint *point) {
  return new QPoint(self->mapToContents(*point));
}

//  void QPlainTextEditPrivate::verticalScrollbarActionTriggered(int action)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlainTextEditPrivate32verticalScrollbarActionTriggeredEi(
    QPlainTextEditPrivate *self,
    int action) {
  self->verticalScrollbarActionTriggered(action);
}

//  void QPlainTextEditPrivate::ensureViewportLayouted()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlainTextEditPrivate22ensureViewportLayoutedEv(
    QPlainTextEditPrivate *self) {
  self->ensureViewportLayouted();
}

//  void QPlainTextEditPrivate::pageUpDown(QTextCursor::MoveOperation op,
//      QTextCursor::MoveMode moveMode, bool moveCursor)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlainTextEditPrivate10pageUpDownEN11QTextCursor13MoveOperationENS0_8MoveModeEb(
    QPlainTextEditPrivate *self,
    QTextCursor::MoveOperation op,
    QTextCursor::MoveMode moveMode,
    bool moveCursor) {
  self->pageUpDown(op, moveMode, moveCursor);
}

//  int QPlainTextEditPrivate::horizontalOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QPlainTextEditPrivate16horizontalOffsetEv(
    const QPlainTextEditPrivate *self) {
  return self->horizontalOffset();
}

//  qreal QPlainTextEditPrivate::verticalOffset(int topBlock, int topLine)
//      const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QPlainTextEditPrivate14verticalOffsetEii(
    const QPlainTextEditPrivate *self,
    int topBlock,
    int topLine) {
  return self->verticalOffset(topBlock, topLine);
}

//  qreal QPlainTextEditPrivate::verticalOffset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK21QPlainTextEditPrivate14verticalOffsetEv(
    const QPlainTextEditPrivate *self) {
  return self->verticalOffset();
}

//  void QPlainTextEditPrivate::sendControlEvent(QEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlainTextEditPrivate16sendControlEventEP6QEvent(
    QPlainTextEditPrivate *self,
    QEvent *e) {
  self->sendControlEvent(e);
}

//  void QPlainTextEditPrivate::updateDefaultTextOption()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlainTextEditPrivate23updateDefaultTextOptionEv(
    QPlainTextEditPrivate *self) {
  self->updateDefaultTextOption();
}

//  void QPlainTextEditPrivate::setTopLine(int visualTopLine, int dx)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlainTextEditPrivate10setTopLineEii(
    QPlainTextEditPrivate *self,
    int visualTopLine,
    int dx) {
  self->setTopLine(visualTopLine, dx);
}

//  void QPlainTextEditPrivate::setTopBlock(int newTopBlock, int newTopLine,
//      int dx)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlainTextEditPrivate11setTopBlockEiii(
    QPlainTextEditPrivate *self,
    int newTopBlock,
    int newTopLine,
    int dx) {
  self->setTopBlock(newTopBlock, newTopLine, dx);
}

//  void QPlainTextEditPrivate::ensureVisible(int position, bool center, bool
//      forceCenter)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlainTextEditPrivate13ensureVisibleEibb(
    QPlainTextEditPrivate *self,
    int position,
    bool center,
    bool forceCenter) {
  self->ensureVisible(position, center, forceCenter);
}

//  void QPlainTextEditPrivate::ensureCursorVisible(bool center)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlainTextEditPrivate19ensureCursorVisibleEb(
    QPlainTextEditPrivate *self,
    bool center) {
  self->ensureCursorVisible(center);
}

//  void QPlainTextEditPrivate::updateViewport()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlainTextEditPrivate14updateViewportEv(
    QPlainTextEditPrivate *self) {
  self->updateViewport();
}

//  void QPlainTextEditPrivate::cursorPositionChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlainTextEditPrivate21cursorPositionChangedEv(
    QPlainTextEditPrivate *self) {
  self->cursorPositionChanged();
}

//  bool QPlainTextEditPrivate::placeHolderTextToBeShown() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QPlainTextEditPrivate24placeHolderTextToBeShownEv(
    const QPlainTextEditPrivate *self) {
  return self->placeHolderTextToBeShown();
}

//  a Python function taken by a CuteQPlainTextEditPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlainTextEditPrivate(
    QPlainTextEditPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlainTextEditPrivate *>(self)->take(key, call);
}

#endif  // QT_CONFIG(textedit)
#endif  // QT_CONFIG(textedit)
