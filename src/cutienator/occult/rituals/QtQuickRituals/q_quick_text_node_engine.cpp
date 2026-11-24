//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktextnodeengine_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicktextnodeengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qtextlayout.h>
#include <QtCore/qrect.h>
#include <QtGui/qbrush.h>
#include <QtGui/qimage.h>
#include <QtGui/qtextobject.h>
#include <QtCore/qpoint.h>
#include <QtGui/qtextformat.h>
#include <QtGui/qglyphrun.h>
#include <QtGui/qcolor.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qquicktextnodeengine_p.h>
#include <QtCore/qpoint.h>
#include <QtGui/qabstracttextdocumentlayout.h>
#include <QtGui/qrawfont.h>
#include <QtGui/qtextdocument.h>
#include <QtGui/qtextlayout.h>
#include <QtGui/qtextobject.h>
#include <QtGui/qtexttable.h>
#include <QtGui/qtextlist.h>
#include <QtGui/qimageiohandler.h>
#include <QtQuick/private/qquicktext_p.h>
#include <QtGui/private/qtextdocumentlayout_p.h>
#include <QtGui/private/qtextimagehandler_p.h>
#include <QtGui/private/qrawfont_p.h>
#include <QtGui/private/qglyphrun_p.h>
#include <QtQuick/private/qquickitem_p.h>
#include <QtQuick/private/qsgdistancefieldglyphnode_p.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/qpa/qplatformtheme.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/items/qquicktextnodeengine.cpp, line 151, as _ZN20QQuickTextNodeEngine14BinaryTreeNode7inOrderERK15QVarLengthArrayIS0_Lx16EEPS1_IiLx256EEi
inline void QQuickTextNodeEngine::BinaryTreeNode::inOrder(const QVarLengthArray<BinaryTreeNode, 16> &binaryTree,
                                              QVarLengthArray<int> *sortedIndexes, int currentIndex)
{
    Q_ASSERT(currentIndex < binaryTree.size());

    const BinaryTreeNode *node = binaryTree.data() + currentIndex;
    if (node->leftChildIndex >= 0)
        inOrder(binaryTree, sortedIndexes, node->leftChildIndex);

    sortedIndexes->append(currentIndex);

    if (node->rightChildIndex >= 0)
        inOrder(binaryTree, sortedIndexes, node->rightChildIndex);
}

//  from ../qtdeclarative/src/quick/items/qquicktextnodeengine.cpp, line 208, as _ZN20QQuickTextNodeEngine18addTextDecorationsE5QSpanIKNS_14TextDecorationELm18446744073709551615EEdd
inline void QQuickTextNodeEngine::addTextDecorations(QSpan<const TextDecoration> textDecorations,
                                              qreal offset, qreal thickness)
{
    for (auto textDecoration : textDecorations) {
        QRectF &rect = textDecoration.rect;
        rect.setY(qRound(rect.y() + m_currentLine.ascent() + offset));
        rect.setHeight(thickness);

        m_lines.append(textDecoration);
    }
}

//  from ../qtdeclarative/src/quick/items/qquicktextnodeengine.cpp, line 123, as _ZN20QQuickTextNodeEngine14BinaryTreeNode6insertEP15QVarLengthArrayIS0_Lx16EERKS0_
inline void QQuickTextNodeEngine::BinaryTreeNode::insert(QVarLengthArray<BinaryTreeNode, 16> *binaryTree, const BinaryTreeNode &binaryTreeNode)
{
    int newIndex = binaryTree->size();
    binaryTree->append(binaryTreeNode);
    if (newIndex == 0)
        return;

    int searchIndex = 0;
    forever {
        BinaryTreeNode *node = binaryTree->data() + searchIndex;
        if (binaryTreeNode.boundingRect.left() < node->boundingRect.left()) {
            if (node->leftChildIndex < 0) {
                node->leftChildIndex = newIndex;
                break;
            } else {
                searchIndex = node->leftChildIndex;
            }
        } else {
            if (node->rightChildIndex < 0) {
                node->rightChildIndex = newIndex;
                break;
            } else {
                searchIndex = node->rightChildIndex;
            }
        }
    }
}

//  from ../qtdeclarative/src/quick/items/qquicktextnodeengine.cpp, line 94, as _ZN20QQuickTextNodeEngine14BinaryTreeNode6insertEP15QVarLengthArrayIS0_Lx16EERK9QGlyphRunNS_14SelectionStateE6QFlagsINS_10DecorationEEN15QTextCharFormat14UnderlineStyleERK6QColorSF_SF_RK7QPointF
inline void QQuickTextNodeEngine::BinaryTreeNode::insert(QVarLengthArray<BinaryTreeNode, 16> *binaryTree, const QGlyphRun &glyphRun, SelectionState selectionState,
                                             Decorations decorations, QTextCharFormat::UnderlineStyle underlineStyle, const QColor &textColor,
                                             const QColor &backgroundColor, const QColor &decorationColor, const QPointF &position)
{
    QRectF searchRect = glyphRun.boundingRect();
    searchRect.translate(position);

    if (qFuzzyIsNull(searchRect.width()) || qFuzzyIsNull(searchRect.height()))
        return;

    if (glyphRun.underline() || underlineStyle != QTextCharFormat::NoUnderline)
        decorations |= Decoration::Underline;
    decorations |= (glyphRun.overline()  ? Decoration::Overline  : Decoration::NoDecoration);
    decorations |= (glyphRun.strikeOut() ? Decoration::StrikeOut : Decoration::NoDecoration);
    decorations |= (backgroundColor.isValid() ? Decoration::Background : Decoration::NoDecoration);

    qreal ascent = glyphRun.rawFont().ascent();
    insert(binaryTree, BinaryTreeNode(glyphRun,
                                      selectionState,
                                      searchRect,
                                      decorations,
                                      underlineStyle,
                                      textColor,
                                      backgroundColor,
                                      decorationColor,
                                      position,
                                      ascent));
}

//  from ../qtdeclarative/src/quick/items/qquicktextnodeengine.cpp, line 68, as _ZN20QQuickTextNodeEngine14BinaryTreeNodeC1ERK9QGlyphRunNS_14SelectionStateERK6QRectFRK6QFlagsINS_10DecorationEEN15QTextCharFormat14UnderlineStyleERK6QColorSH_SH_RK7QPointFd
inline QQuickTextNodeEngine::BinaryTreeNode::BinaryTreeNode(const QGlyphRun &g,
                                                     SelectionState selState,
                                                     const QRectF &brect,
                                                     const Decorations &decs,
                                                     QTextCharFormat::UnderlineStyle us,
                                                     const QColor &c,
                                                     const QColor &bc, const QColor &dc,
                                                     const QPointF &pos, qreal a)
    : glyphRun(g)
    , boundingRect(brect)
    , selectionState(selState)
    , clipNode(nullptr)
    , decorations(decs)
    , underlineStyle(us)
    , color(c)
    , backgroundColor(bc)
    , decorationColor(dc)
    , position(pos)
    , ascent(a)
    , leftChildIndex(-1)
    , rightChildIndex(-1)
{
    QGlyphRunPrivate *d = QGlyphRunPrivate::get(g);
    ranges.append(std::make_pair(d->textRangeStart, d->textRangeEnd));
}

//  from ../qtdeclarative/src/quick/items/qquicktextnodeengine.cpp, line 693, as _ZN20QQuickTextNodeEngine9addBorderERK6QRectFdN16QTextFrameFormat11BorderStyleERK6QBrush
inline void QQuickTextNodeEngine::addBorder(const QRectF &rect, qreal border,
                                     QTextFrameFormat::BorderStyle borderStyle,
                                     const QBrush &borderBrush)
{
    const QColor &color = borderBrush.color();

    // Currently we don't support other styles than solid
    Q_UNUSED(borderStyle);

    m_backgrounds.append(std::make_pair(QRectF(rect.left(), rect.top(), border, rect.height() + border), color));
    m_backgrounds.append(std::make_pair(QRectF(rect.left() + border, rect.top(), rect.width(), border), color));
    m_backgrounds.append(std::make_pair(QRectF(rect.right(), rect.top() + border, border, rect.height() - border), color));
    m_backgrounds.append(std::make_pair(QRectF(rect.left() + border, rect.bottom(), rect.width(), border), color));
}

//  from ../qtdeclarative/src/quick/items/qquicktextnodeengine.cpp, line 708, as _ZN20QQuickTextNodeEngine19addFrameDecorationsEP13QTextDocumentP10QTextFrame
inline void QQuickTextNodeEngine::addFrameDecorations(QTextDocument *document, QTextFrame *frame)
{
    QTextDocumentLayout *documentLayout = qobject_cast<QTextDocumentLayout *>(document->documentLayout());
    if (Q_UNLIKELY(!documentLayout))
        return;

    QTextFrameFormat frameFormat = frame->format().toFrameFormat();
    QTextTable *table = qobject_cast<QTextTable *>(frame);

    QRectF boundingRect = table == nullptr
            ? documentLayout->frameBoundingRect(frame)
            : documentLayout->tableBoundingRect(table);

    QBrush bg = frame->frameFormat().background();
    if (bg.style() != Qt::NoBrush)
        m_backgrounds.append(std::make_pair(boundingRect, bg.color()));

    if (!frameFormat.hasProperty(QTextFormat::FrameBorder))
        return;

    qreal borderWidth = frameFormat.border();
    if (qFuzzyIsNull(borderWidth))
        return;

    QBrush borderBrush = frameFormat.borderBrush();
    QTextFrameFormat::BorderStyle borderStyle = frameFormat.borderStyle();
    if (borderStyle == QTextFrameFormat::BorderStyle_None)
        return;

    const auto collapsed = table->format().borderCollapse();

    if (!collapsed) {
        addBorder(boundingRect.adjusted(frameFormat.leftMargin(), frameFormat.topMargin(),
                                        -frameFormat.rightMargin() - borderWidth,
                                        -frameFormat.bottomMargin() - borderWidth),
                  borderWidth, borderStyle, borderBrush);
    }
    if (table != nullptr) {
        int rows = table->rows();
        int columns = table->columns();

        for (int row=0; row<rows; ++row) {
            for (int column=0; column<columns; ++column) {
                QTextTableCell cell = table->cellAt(row, column);

                QRectF cellRect = documentLayout->tableCellBoundingRect(table, cell);
                addBorder(cellRect.adjusted(-borderWidth, -borderWidth, collapsed ? -borderWidth : 0, collapsed ? -borderWidth : 0), borderWidth,
                          borderStyle, borderBrush);
            }
        }
    }
}

//  from ../qtdeclarative/src/quick/items/qquicktextnodeengine.cpp, line 453, as _ZN20QQuickTextNodeEngine8addImageERK6QRectFRK6QImagedNS_14SelectionStateEN16QTextFrameFormat8PositionE
inline void QQuickTextNodeEngine::addImage(const QRectF &rect, const QImage &image, qreal ascent,
                                    SelectionState selectionState,
                                    QTextFrameFormat::Position layoutPosition)
{
    QRectF searchRect = rect;
    if (layoutPosition == QTextFrameFormat::InFlow) {
        if (m_currentLineTree.isEmpty()) {
            qreal y = m_currentLine.ascent() - ascent;
            if (m_currentTextDirection == Qt::RightToLeft)
                searchRect.moveTopRight(m_position + m_currentLine.rect().topRight() + QPointF(0, y));
            else
                searchRect.moveTopLeft(m_position + m_currentLine.position() + QPointF(0, y));
        } else {
            const BinaryTreeNode *lastNode = m_currentLineTree.data() + m_currentLineTree.size() - 1;
            if (lastNode->glyphRun.isRightToLeft()) {
                QPointF lastPos = lastNode->boundingRect.topLeft();
                searchRect.moveTopRight(lastPos - QPointF(0, ascent - lastNode->ascent));
            } else {
                QPointF lastPos = lastNode->boundingRect.topRight();
                searchRect.moveTopLeft(lastPos - QPointF(0, ascent - lastNode->ascent));
            }
        }
    }

    BinaryTreeNode::insert(&m_currentLineTree, searchRect, image, ascent, selectionState);
    m_hasContents = true;
}

//  from ../qtdeclarative/src/quick/items/qquicktextnodeengine.cpp, line 481, as _ZN20QQuickTextNodeEngine13addTextObjectERK10QTextBlockRK7QPointFRK15QTextCharFormatNS_14SelectionStateEP13QTextDocumentiN16QTextFrameFormat8PositionE
inline void QQuickTextNodeEngine::addTextObject(const QTextBlock &block, const QPointF &position, const QTextCharFormat &format,
                                         SelectionState selectionState,
                                         QTextDocument *textDocument, int pos,
                                         QTextFrameFormat::Position layoutPosition)
{
    QTextObjectInterface *handler = textDocument->documentLayout()->handlerForObject(format.objectType());
    if (handler != nullptr) {
        QImage image;
        QSizeF size = handler->intrinsicSize(textDocument, pos, format);

        if (format.objectType() == QTextFormat::ImageObject) {
            QTextImageFormat imageFormat = format.toImageFormat();
            QTextImageHandler *imageHandler = static_cast<QTextImageHandler *>(handler);
            image = imageHandler->image(textDocument, imageFormat);
        }

        if (image.isNull()) {
            if (QImageIOHandler::allocateImage((size * m_devicePixelRatio).toSize(),
                                               QImage::Format_ARGB32_Premultiplied,
                                               &image)) {
                image.setDevicePixelRatio(m_devicePixelRatio);
                image.fill(Qt::transparent);
                {
                    QPainter painter(&image);
                    handler->drawObject(&painter, QRectF({}, size), textDocument, pos, format);
                }
            }
        }

        // Use https://developer.mozilla.org/de/docs/Web/CSS/vertical-align as a reference
        // The top/bottom positions are supposed to be higher/lower than the text and reference
        // the line height, not the text height (using QFontMetrics)
        qreal ascent;
        QTextLine line = block.layout()->lineForTextPosition(pos - block.position());
        switch (format.verticalAlignment())
        {
        case QTextCharFormat::AlignTop:
            ascent = line.ascent();
            break;
        case QTextCharFormat::AlignMiddle:
            //       Middlepoint of line (height - descent) + Half object height
            ascent = (line.ascent() + line.descent()) / 2 - line.descent() + size.height() / 2;
            break;
        case QTextCharFormat::AlignBottom:
            ascent = size.height() - line.descent();
            break;
        case QTextCharFormat::AlignBaseline: {
            QFontMetricsF m(format.font());
            ascent = size.height() - m.descent();
            break;
        }
        default:
            ascent = size.height();
        }

        addImage(QRectF(position, size), image, ascent, selectionState, layoutPosition);
    }
}

//  from ../qtdeclarative/src/quick/items/qquicktextnodeengine.cpp, line 553, as _ZN20QQuickTextNodeEngine17addSelectedGlyphsERK9QGlyphRun
inline void QQuickTextNodeEngine::addSelectedGlyphs(const QGlyphRun &glyphRun)
{
    int currentSize = m_currentLineTree.size();
    BinaryTreeNode::insert(&m_currentLineTree,
                           glyphRun,
                           Selected,
                           Decoration::NoDecoration,
                           m_underlineStyle,
                           m_textColor,
                           m_backgroundColor,
                           m_decorationColor,
                           m_position);
    m_hasSelection = m_hasSelection || m_currentLineTree.size() > currentSize;
}

//  from ../qtdeclarative/src/quick/items/qquicktextnodeengine.cpp, line 540, as _ZN20QQuickTextNodeEngine19addUnselectedGlyphsERK9QGlyphRun
inline void QQuickTextNodeEngine::addUnselectedGlyphs(const QGlyphRun &glyphRun)
{
    BinaryTreeNode::insert(&m_currentLineTree,
                           glyphRun,
                           Unselected,
                           Decoration::NoDecoration,
                           m_underlineStyle,
                           m_textColor,
                           m_backgroundColor,
                           m_decorationColor,
                           m_position);
}

//  from ../qtdeclarative/src/quick/items/qquicktextnodeengine.cpp, line 621, as _ZN20QQuickTextNodeEngine16addGlyphsInRangeEiiN15QTextCharFormat14UnderlineStyleERK6QColorS4_S4_ii
inline void QQuickTextNodeEngine::addGlyphsInRange(int rangeStart, int rangeLength,
                                            QTextCharFormat::UnderlineStyle underlineStyle,
                                            const QColor &color, const QColor &backgroundColor, const QColor &decorationColor,
                                            int selectionStart, int selectionEnd)
{
    QColor oldColor;
    if (color.isValid()) {
        oldColor = m_textColor;
        m_textColor = color;
    }

    QColor oldBackgroundColor = m_backgroundColor;
    if (backgroundColor.isValid()) {
        oldBackgroundColor = m_backgroundColor;
        m_backgroundColor = backgroundColor;
    }

    QColor oldDecorationColor = m_decorationColor;
    if (decorationColor.isValid()) {
        oldDecorationColor = m_decorationColor;
        m_decorationColor = decorationColor;
    }

    QTextCharFormat::UnderlineStyle oldUnderlineStyle = m_underlineStyle;
    m_underlineStyle = underlineStyle;

    bool hasSelection = selectionEnd >= 0
            && selectionStart <= selectionEnd;

    QTextLine &line = m_currentLine;
    int rangeEnd = rangeStart + rangeLength;
    if (!hasSelection || (selectionStart > rangeEnd || selectionEnd < rangeStart)) {
        const QList<QGlyphRun> glyphRuns = line.glyphRuns(rangeStart, rangeLength);
        for (const QGlyphRun &glyphRun : glyphRuns)
            addUnselectedGlyphs(glyphRun);
    } else {
        if (rangeStart < selectionStart) {
            int length = qMin(selectionStart - rangeStart, rangeLength);
            const QList<QGlyphRun> glyphRuns = line.glyphRuns(rangeStart, length);
            for (const QGlyphRun &glyphRun : glyphRuns)
                addUnselectedGlyphs(glyphRun);
        }

        if (rangeEnd > selectionStart) {
            int start = qMax(selectionStart, rangeStart);
            int length = qMin(selectionEnd - start + 1, rangeEnd - start);
            const QList<QGlyphRun> glyphRuns = line.glyphRuns(start, length);
            for (const QGlyphRun &glyphRun : glyphRuns)
                addSelectedGlyphs(glyphRun);
        }

        if (selectionEnd >= rangeStart && selectionEnd < rangeEnd) {
            int start = selectionEnd + 1;
            int length = rangeEnd - selectionEnd - 1;
            const QList<QGlyphRun> glyphRuns = line.glyphRuns(start, length);
            for (const QGlyphRun &glyphRun : glyphRuns)
                addUnselectedGlyphs(glyphRun);
        }
    }

    if (decorationColor.isValid())
        m_decorationColor = oldDecorationColor;

    if (backgroundColor.isValid())
        m_backgroundColor = oldBackgroundColor;

    if (oldColor.isValid())
        m_textColor = oldColor;

    m_underlineStyle = oldUnderlineStyle;
}

//  from ../qtdeclarative/src/quick/items/qquicktextnodeengine.cpp, line 220, as _ZN20QQuickTextNodeEngine18processCurrentLineEv
inline void QQuickTextNodeEngine::processCurrentLine()
{
    // No glyphs, do nothing
    if (m_currentLineTree.isEmpty())
        return;

    // 1. Go through current line and get correct decoration position for each node based on
    // neighbouring decorations. Add decoration to global list
    // 2. Create clip nodes for all selected text. Try to merge as many as possible within
    // the line.
    // 3. Add QRects to a list of selection rects.
    // 4. Add all nodes to a global processed list
    QVarLengthArray<int> sortedIndexes; // Indexes in tree sorted by x position
    BinaryTreeNode::inOrder(m_currentLineTree, &sortedIndexes);

    Q_ASSERT(sortedIndexes.size() == m_currentLineTree.size());

    SelectionState currentSelectionState = Unselected;
    QRectF currentRect;

    Decorations currentDecorations = Decoration::NoDecoration;
    qreal underlineOffset = 0.0;
    qreal underlineThickness = 0.0;

    qreal overlineOffset = 0.0;
    qreal overlineThickness = 0.0;

    qreal strikeOutOffset = 0.0;
    qreal strikeOutThickness = 0.0;

    QRectF decorationRect = currentRect;

    QColor lastColor;
    QColor lastBackgroundColor;
    QColor lastDecorationColor;
    QTextCharFormat::UnderlineStyle lastUnderlineStyle = QTextCharFormat::NoUnderline;

    QVarLengthArray<TextDecoration, 16> pendingUnderlines;
    QVarLengthArray<TextDecoration, 16> pendingOverlines;
    QVarLengthArray<TextDecoration, 16> pendingStrikeOuts;
    if (!sortedIndexes.isEmpty()) {
        QQuickDefaultClipNode *currentClipNode = m_hasSelection ? new QQuickDefaultClipNode(QRectF()) : nullptr;
        bool currentClipNodeUsed = false;
        for (int i=0; i<=sortedIndexes.size(); ++i) {
            BinaryTreeNode *node = nullptr;
            if (i < sortedIndexes.size()) {
                int sortedIndex = sortedIndexes.at(i);
                Q_ASSERT(sortedIndex < m_currentLineTree.size());

                node = m_currentLineTree.data() + sortedIndex;
                if (i == 0)
                    currentSelectionState = node->selectionState;
            }

            // Update decorations
            if (currentDecorations != Decoration::NoDecoration) {
                decorationRect.setY(m_position.y() + m_currentLine.y());
                decorationRect.setHeight(m_currentLine.height());

                // Extend decoration rect to the next node only if the next node continues the
                // same decoration, or if it is directly adjacent. Don't extend across gaps
                // (e.g. tab characters) to a node that does not share the same decoration, as
                // that would draw the decoration through invisible content.
                if (node != nullptr) {
                    const bool continuesDecoration = node->decorations & currentDecorations;
                    if (continuesDecoration || node->boundingRect.left() < decorationRect.right())
                        decorationRect.setRight(node->boundingRect.left());
                }

                TextDecoration textDecoration(currentSelectionState, decorationRect, lastColor);
                if (lastDecorationColor.isValid() &&
                        (currentDecorations.testFlag(Decoration::Underline) ||
                         currentDecorations.testFlag(Decoration::Overline) ||
                         currentDecorations.testFlag(Decoration::StrikeOut)))
                    textDecoration.color = lastDecorationColor;

                if (currentDecorations & Decoration::Underline) {
                    textDecoration.underlineStyle = lastUnderlineStyle;
                    // Try to merge with previous underline if style, color, and selection match
                    if (!pendingUnderlines.isEmpty()) {
                        TextDecoration &last = pendingUnderlines.last();
                        // Half-pixel threshold accounts for floating-point gaps between adjacent glyph runs
                        constexpr qreal mergeThreshold = 0.5;
                        if (last.underlineStyle == lastUnderlineStyle
                            && last.color == textDecoration.color
                            && last.selectionState == textDecoration.selectionState
                            && qAbs(last.rect.right() - textDecoration.rect.left()) < mergeThreshold) {
                            // Extend previous range instead of creating a new one
                            last.rect.setRight(textDecoration.rect.right());
                        } else {
                            pendingUnderlines.append(textDecoration);
                        }
                    } else {
                        pendingUnderlines.append(textDecoration);
                    }
                }

                if (currentDecorations & Decoration::Overline)
                    pendingOverlines.append(textDecoration);

                if (currentDecorations & Decoration::StrikeOut)
                    pendingStrikeOuts.append(textDecoration);

                if (currentDecorations & Decoration::Background)
                    m_backgrounds.append(std::make_pair(decorationRect, lastBackgroundColor));
            }

            // If we've reached an unselected node from a selected node, we add the
            // selection rect to the graph, and we add decoration every time the
            // selection state changes, because that means the text color changes
            if (node == nullptr || node->selectionState != currentSelectionState) {
                currentRect.setY(m_position.y() + m_currentLine.y());
                currentRect.setHeight(m_currentLine.height());

                if (currentSelectionState == Selected)
                    m_selectionRects.append(currentRect);

                if (currentClipNode != nullptr) {
                    if (!currentClipNodeUsed) {
                        delete currentClipNode;
                    } else {
                        currentClipNode->setIsRectangular(true);
                        currentClipNode->setRect(currentRect);
                        currentClipNode->update();
                    }
                }

                if (node != nullptr && m_hasSelection)
                    currentClipNode = new QQuickDefaultClipNode(QRectF());
                else
                    currentClipNode = nullptr;
                currentClipNodeUsed = false;

                if (node != nullptr) {
                    currentSelectionState = node->selectionState;
                    currentRect = node->boundingRect;

                    // Make sure currentRect is valid, otherwise the unite won't work
                    if (currentRect.isNull())
                        currentRect.setSize(QSizeF(1, 1));
                }
            } else {
                if (currentRect.isNull())
                    currentRect = node->boundingRect;
                else
                    currentRect = currentRect.united(node->boundingRect);
            }

            if (node != nullptr) {
                if (node->selectionState == Selected) {
                    node->clipNode = currentClipNode;
                    currentClipNodeUsed = true;
                }

                decorationRect = node->boundingRect;

                // If previous item(s) had underline and current does not, then we add the
                // pending lines to the lists and likewise for overlines and strikeouts
                if (!pendingUnderlines.isEmpty()
                        && !(node->decorations & Decoration::Underline)) {
                    addTextDecorations(pendingUnderlines, underlineOffset, underlineThickness);

                    pendingUnderlines.clear();

                    underlineOffset = 0.0;
                    underlineThickness = 0.0;
                }

                // ### Add pending when overlineOffset/thickness changes to minimize number of
                // nodes
                if (!pendingOverlines.isEmpty()) {
                    addTextDecorations(pendingOverlines, overlineOffset, overlineThickness);

                    pendingOverlines.clear();

                    overlineOffset = 0.0;
                    overlineThickness = 0.0;
                }

                // ### Add pending when overlineOffset/thickness changes to minimize number of
                // nodes
                if (!pendingStrikeOuts.isEmpty()) {
                    addTextDecorations(pendingStrikeOuts, strikeOutOffset, strikeOutThickness);

                    pendingStrikeOuts.clear();

                    strikeOutOffset = 0.0;
                    strikeOutThickness = 0.0;
                }

                // Merge current values with previous. Prefer greatest thickness
                QRawFont rawFont = node->glyphRun.rawFont();
                if (node->decorations & Decoration::Underline) {
                    if (rawFont.lineThickness() > underlineThickness) {
                        underlineThickness = rawFont.lineThickness();
                        underlineOffset = rawFont.underlinePosition();
                    }
                }

                if (node->decorations & Decoration::Overline) {
                    overlineOffset = -rawFont.ascent();
                    overlineThickness = rawFont.lineThickness();
                }

                if (node->decorations & Decoration::StrikeOut) {
                    strikeOutThickness = rawFont.lineThickness();
                    strikeOutOffset = rawFont.ascent() / -3.0;
                }

                currentDecorations = node->decorations;
                lastColor = node->color;
                lastBackgroundColor = node->backgroundColor;
                lastDecorationColor = node->decorationColor;
                lastUnderlineStyle = node->underlineStyle;
                m_processedNodes.append(*node);
            }
        }

        if (!pendingUnderlines.isEmpty())
            addTextDecorations(pendingUnderlines, underlineOffset, underlineThickness);

        if (!pendingOverlines.isEmpty())
            addTextDecorations(pendingOverlines, overlineOffset, overlineThickness);

        if (!pendingStrikeOuts.isEmpty())
            addTextDecorations(pendingStrikeOuts, strikeOutOffset, strikeOutThickness);
    }

    m_currentLineTree.clear();
    m_currentLine = QTextLine();
    m_hasSelection = false;
}
//  -----------------------------------------------------------------------

//  QQuickTextNodeEngine::QQuickTextNodeEngine()
extern "C" Q_DECL_EXPORT
QQuickTextNodeEngine *ritual_ZN20QQuickTextNodeEngineC1Ev() {
  return new QQuickTextNodeEngine();
}

//  bool QQuickTextNodeEngine::hasContents() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQuickTextNodeEngine11hasContentsEv(
    const QQuickTextNodeEngine *self) {
  return self->hasContents();
}

//  QTextLine QQuickTextNodeEngine::currentLine() const
extern "C" Q_DECL_EXPORT
QTextLine *ritual_ZNK20QQuickTextNodeEngine11currentLineEv(
    const QQuickTextNodeEngine *self) {
  return new QTextLine(self->currentLine());
}

//  void QQuickTextNodeEngine::setCurrentLine(const QTextLine &currentLine)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickTextNodeEngine14setCurrentLineERK9QTextLine(
    QQuickTextNodeEngine *self,
    const QTextLine *currentLine) {
  self->setCurrentLine(*currentLine);
}

//  void QQuickTextNodeEngine::setCurrentTextDirection(Qt::LayoutDirection
//      textDirection)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickTextNodeEngine23setCurrentTextDirectionEN2Qt15LayoutDirectionE(
    QQuickTextNodeEngine *self,
    Qt::LayoutDirection textDirection) {
  self->setCurrentTextDirection(textDirection);
}

//  void QQuickTextNodeEngine::addBorder(const QRectF &rect, qreal border,
//      QTextFrameFormat::BorderStyle borderStyle, const QBrush &borderBrush)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickTextNodeEngine9addBorderERK6QRectFdN16QTextFrameFormat11BorderStyleERK6QBrush(
    QQuickTextNodeEngine *self,
    const QRectF *rect,
    qreal border,
    QTextFrameFormat::BorderStyle borderStyle,
    const QBrush *borderBrush) {
  self->addBorder(*rect, border, borderStyle, *borderBrush);
}

//  void QQuickTextNodeEngine::addFrameDecorations(QTextDocument *document,
//      QTextFrame *frame)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickTextNodeEngine19addFrameDecorationsEP13QTextDocumentP10QTextFrame(
    QQuickTextNodeEngine *self,
    QTextDocument *document,
    QTextFrame *frame) {
  self->addFrameDecorations(document, frame);
}

//  void QQuickTextNodeEngine::addImage(const QRectF &rect, const QImage
//      &image, qreal ascent, SelectionState selectionState,
//      QTextFrameFormat::Position layoutPosition)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickTextNodeEngine8addImageERK6QRectFRK6QImagedNS_14SelectionStateEN16QTextFrameFormat8PositionE(
    QQuickTextNodeEngine *self,
    const QRectF *rect,
    const QImage *image,
    qreal ascent,
    QQuickTextNodeEngine::SelectionState selectionState,
    QTextFrameFormat::Position layoutPosition) {
  self->addImage(*rect, *image, ascent, selectionState, layoutPosition);
}

//  void QQuickTextNodeEngine::addTextObject(const QTextBlock &block, const
//      QPointF &position, const QTextCharFormat &format, SelectionState
//      selectionState, QTextDocument *textDocument, int pos,
//      QTextFrameFormat::Position layoutPosition)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickTextNodeEngine13addTextObjectERK10QTextBlockRK7QPointFRK15QTextCharFormatNS_14SelectionStateEP13QTextDocumentiN16QTextFrameFormat8PositionE(
    QQuickTextNodeEngine *self,
    const QTextBlock *block,
    const QPointF *position,
    const QTextCharFormat *format,
    QQuickTextNodeEngine::SelectionState selectionState,
    QTextDocument *textDocument,
    int pos,
    QTextFrameFormat::Position layoutPosition) {
  self->addTextObject(
      *block,
      *position,
      *format,
      selectionState,
      textDocument,
      pos,
      layoutPosition);
}

//  void QQuickTextNodeEngine::addSelectedGlyphs(const QGlyphRun &glyphRun)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickTextNodeEngine17addSelectedGlyphsERK9QGlyphRun(
    QQuickTextNodeEngine *self,
    const QGlyphRun *glyphRun) {
  self->addSelectedGlyphs(*glyphRun);
}

//  void QQuickTextNodeEngine::addUnselectedGlyphs(const QGlyphRun &glyphRun)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickTextNodeEngine19addUnselectedGlyphsERK9QGlyphRun(
    QQuickTextNodeEngine *self,
    const QGlyphRun *glyphRun) {
  self->addUnselectedGlyphs(*glyphRun);
}

//  void QQuickTextNodeEngine::addGlyphsInRange(int rangeStart, int rangeEnd,
//      QTextCharFormat::UnderlineStyle underlineStyle, const QColor &color,
//      const QColor &backgroundColor, const QColor &underlineColor, int
//      selectionStart, int selectionEnd)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickTextNodeEngine16addGlyphsInRangeEiiN15QTextCharFormat14UnderlineStyleERK6QColorS4_S4_ii(
    QQuickTextNodeEngine *self,
    int rangeStart,
    int rangeEnd,
    QTextCharFormat::UnderlineStyle underlineStyle,
    const QColor *color,
    const QColor *backgroundColor,
    const QColor *underlineColor,
    int selectionStart,
    int selectionEnd) {
  self->addGlyphsInRange(
      rangeStart,
      rangeEnd,
      underlineStyle,
      *color,
      *backgroundColor,
      *underlineColor,
      selectionStart,
      selectionEnd);
}

//  void QQuickTextNodeEngine::setSelectionColor(const QColor
//      &selectionColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickTextNodeEngine17setSelectionColorERK6QColor(
    QQuickTextNodeEngine *self,
    const QColor *selectionColor) {
  self->setSelectionColor(*selectionColor);
}

//  void QQuickTextNodeEngine::setSelectedTextColor(const QColor
//      &selectedTextColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickTextNodeEngine20setSelectedTextColorERK6QColor(
    QQuickTextNodeEngine *self,
    const QColor *selectedTextColor) {
  self->setSelectedTextColor(*selectedTextColor);
}

//  void QQuickTextNodeEngine::setTextColor(const QColor &textColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickTextNodeEngine12setTextColorERK6QColor(
    QQuickTextNodeEngine *self,
    const QColor *textColor) {
  self->setTextColor(*textColor);
}

//  void QQuickTextNodeEngine::setAnchorColor(const QColor &anchorColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickTextNodeEngine14setAnchorColorERK6QColor(
    QQuickTextNodeEngine *self,
    const QColor *anchorColor) {
  self->setAnchorColor(*anchorColor);
}

//  void QQuickTextNodeEngine::setPosition(const QPointF &position)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickTextNodeEngine11setPositionERK7QPointF(
    QQuickTextNodeEngine *self,
    const QPointF *position) {
  self->setPosition(*position);
}

//  void QQuickTextNodeEngine::setDevicePixelRatio(qreal dpr)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickTextNodeEngine19setDevicePixelRatioEd(
    QQuickTextNodeEngine *self,
    qreal dpr) {
  self->setDevicePixelRatio(dpr);
}

//  void QQuickTextNodeEngine::processCurrentLine()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickTextNodeEngine18processCurrentLineEv(
    QQuickTextNodeEngine *self) {
  self->processCurrentLine();
}

//  QQuickTextNodeEngine::~QQuickTextNodeEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickTextNodeEngineD1Ev(QQuickTextNodeEngine *self) {
  delete self;
}
