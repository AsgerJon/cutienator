//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qtextdocumentfragment_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if !defined(QT_NO_TEXTHTMLPARSER)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtextdocumentfragment_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qtextformat.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/private/qtexthtmlparser_p.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qstack.h>
#include <QtCore/qdebug.h>
#include <QtCore/qthread.h>
#include <QtGui/qguiapplication.h>
#include <QtGui/qtextdocument.h>
#include <QtGui/private/qtextformat_p.h>
#include <QtGui/private/qtextdocument_p.h>
#include <QtGui/qtextcursor.h>
#include <QtGui/private/qfont_p.h>
#include <algorithm>
#include <QtGui/qtextdocumentfragment.h>
#include <QtGui/private/qtextdocumentfragment_p.h>
#include <QtGui/private/qtextcursor_p.h>
#include <QtGui/qtextlist.h>
#if QT_CONFIG(textmarkdownreader)
#include <QtGui/private/qtextmarkdownimporter_p.h>
#endif
#if QT_CONFIG(textmarkdownwriter)
#include <QtGui/private/qtextmarkdownwriter_p.h>
#endif
#include <QtCore/qdebug.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qdatastream.h>
#include <QtCore/qdatetime.h>
#include <QtCore/private/qstringiterator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/gui/text/qtextdocumentfragment.cpp, line 424, as local:qtextdocumentfragment.cpp:nextListStyle
#if !defined(QT_NO_TEXTHTMLPARSER)
static QTextListFormat::Style nextListStyle(QTextListFormat::Style style)
{
    if (style == QTextListFormat::ListDisc)
        return QTextListFormat::ListCircle;
    else if (style == QTextListFormat::ListCircle)
        return QTextListFormat::ListSquare;
    return style;
}
#endif  // !defined(QT_NO_TEXTHTMLPARSER)

//  from src/gui/text/qtexthtmlparser.cpp, line 345, as local:qtexthtmlparser.cpp:elements
#if !defined(QT_NO_TEXTHTMLPARSER)
static constexpr QTextHtmlElement elements[]= {
    { "a",          Html_a,          QTextHtmlElement::DisplayInline },
    { "address",    Html_address,    QTextHtmlElement::DisplayInline },
    { "b",          Html_b,          QTextHtmlElement::DisplayInline },
    { "big",        Html_big,        QTextHtmlElement::DisplayInline },
    { "blockquote", Html_blockquote, QTextHtmlElement::DisplayBlock },
    { "body",       Html_body,       QTextHtmlElement::DisplayBlock },
    { "br",         Html_br,         QTextHtmlElement::DisplayInline },
    { "caption",    Html_caption,    QTextHtmlElement::DisplayBlock },
    { "center",     Html_center,     QTextHtmlElement::DisplayBlock },
    { "cite",       Html_cite,       QTextHtmlElement::DisplayInline },
    { "code",       Html_code,       QTextHtmlElement::DisplayInline },
    { "dd",         Html_dd,         QTextHtmlElement::DisplayBlock },
    { "del",        Html_del,        QTextHtmlElement::DisplayInline },
    { "dfn",        Html_dfn,        QTextHtmlElement::DisplayInline },
    { "div",        Html_div,        QTextHtmlElement::DisplayBlock },
    { "dl",         Html_dl,         QTextHtmlElement::DisplayBlock },
    { "dt",         Html_dt,         QTextHtmlElement::DisplayBlock },
    { "em",         Html_em,         QTextHtmlElement::DisplayInline },
    { "font",       Html_font,       QTextHtmlElement::DisplayInline },
    { "h1",         Html_h1,         QTextHtmlElement::DisplayBlock },
    { "h2",         Html_h2,         QTextHtmlElement::DisplayBlock },
    { "h3",         Html_h3,         QTextHtmlElement::DisplayBlock },
    { "h4",         Html_h4,         QTextHtmlElement::DisplayBlock },
    { "h5",         Html_h5,         QTextHtmlElement::DisplayBlock },
    { "h6",         Html_h6,         QTextHtmlElement::DisplayBlock },
    { "head",       Html_head,       QTextHtmlElement::DisplayNone },
    { "hr",         Html_hr,         QTextHtmlElement::DisplayBlock },
    { "html",       Html_html,       QTextHtmlElement::DisplayInline },
    { "i",          Html_i,          QTextHtmlElement::DisplayInline },
    { "img",        Html_img,        QTextHtmlElement::DisplayInline },
    { "kbd",        Html_kbd,        QTextHtmlElement::DisplayInline },
    { "li",         Html_li,         QTextHtmlElement::DisplayBlock },
    { "link",       Html_link,       QTextHtmlElement::DisplayNone },
    { "meta",       Html_meta,       QTextHtmlElement::DisplayNone },
    { "nobr",       Html_nobr,       QTextHtmlElement::DisplayInline },
    { "ol",         Html_ol,         QTextHtmlElement::DisplayBlock },
    { "p",          Html_p,          QTextHtmlElement::DisplayBlock },
    { "pre",        Html_pre,        QTextHtmlElement::DisplayBlock },
    { "qt",         Html_body /*deliberate mapping*/, QTextHtmlElement::DisplayBlock },
    { "s",          Html_s,          QTextHtmlElement::DisplayInline },
    { "samp",       Html_samp,       QTextHtmlElement::DisplayInline },
    { "script",     Html_script,     QTextHtmlElement::DisplayNone },
    { "small",      Html_small,      QTextHtmlElement::DisplayInline },
    { "span",       Html_span,       QTextHtmlElement::DisplayInline },
    { "strong",     Html_strong,     QTextHtmlElement::DisplayInline },
    { "style",      Html_style,      QTextHtmlElement::DisplayNone },
    { "sub",        Html_sub,        QTextHtmlElement::DisplayInline },
    { "sup",        Html_sup,        QTextHtmlElement::DisplayInline },
    { "table",      Html_table,      QTextHtmlElement::DisplayTable },
    { "tbody",      Html_tbody,      QTextHtmlElement::DisplayTable },
    { "td",         Html_td,         QTextHtmlElement::DisplayBlock },
    { "tfoot",      Html_tfoot,      QTextHtmlElement::DisplayTable },
    { "th",         Html_th,         QTextHtmlElement::DisplayBlock },
    { "thead",      Html_thead,      QTextHtmlElement::DisplayTable },
    { "title",      Html_title,      QTextHtmlElement::DisplayNone },
    { "tr",         Html_tr,         QTextHtmlElement::DisplayTable },
    { "tt",         Html_tt,         QTextHtmlElement::DisplayInline },
    { "u",          Html_u,          QTextHtmlElement::DisplayInline },
    { "ul",         Html_ul,         QTextHtmlElement::DisplayBlock },
    { "var",        Html_var,        QTextHtmlElement::DisplayInline },
};
#endif  // !defined(QT_NO_TEXTHTMLPARSER)

//  from src/gui/text/qtexthtmlparser.cpp, line 534, as _ZN15QTextHtmlParser5parseERK7QStringPK13QTextDocument
#if !defined(QT_NO_TEXTHTMLPARSER)
inline void QTextHtmlParser::parse(const QString &text, const QTextDocument *_resourceProvider)
{
    qDeleteAll(nodes);
    nodes.clear();
    nodes.append(new QTextHtmlParserNode);
    txt = text;
    pos = 0;
    len = txt.size();
    textEditMode = false;
    resourceProvider = _resourceProvider;
    parse();
    //dumpHtml();
}
#endif  // !defined(QT_NO_TEXTHTMLPARSER)

//  from src/gui/text/qtexthtmlparser.cpp, line 583, as _ZNK15QTextHtmlParser12bottomMarginEi
#if !defined(QT_NO_TEXTHTMLPARSER)
inline int QTextHtmlParser::bottomMargin(int i) const
{
    if (!i)
        return 0;
    return at(i).margin[MarginBottom];
}
#endif  // !defined(QT_NO_TEXTHTMLPARSER)

//  from src/gui/text/qtexthtmlparser.cpp, line 548, as _ZNK15QTextHtmlParser5depthEi
#if !defined(QT_NO_TEXTHTMLPARSER)
inline int QTextHtmlParser::depth(int i) const
{
    int depth = 0;
    while (i) {
        i = at(i).parent;
        ++depth;
    }
    return depth;
}
#endif  // !defined(QT_NO_TEXTHTMLPARSER)

//  from src/gui/text/qtexthtmlparser.cpp, line 558, as _ZNK15QTextHtmlParser6marginEii
#if !defined(QT_NO_TEXTHTMLPARSER)
inline int QTextHtmlParser::margin(int i, int mar) const {
    int m = 0;
    const QTextHtmlParserNode *node;
    if (mar == MarginLeft
        || mar == MarginRight) {
        while (i) {
            node = &at(i);
            if (!node->isBlock() && node->id != Html_table)
                break;
            if (node->isTableCell())
                break;
            m += node->margin[mar];
            i = node->parent;
        }
    }
    return m;
}
#endif  // !defined(QT_NO_TEXTHTMLPARSER)

//  from src/gui/text/qtexthtmlparser.cpp, line 576, as _ZNK15QTextHtmlParser9topMarginEi
#if !defined(QT_NO_TEXTHTMLPARSER)
inline int QTextHtmlParser::topMargin(int i) const
{
    if (!i)
        return 0;
    return at(i).margin[MarginTop];
}
#endif  // !defined(QT_NO_TEXTHTMLPARSER)

//  from src/gui/text/qtexthtmlparser.cpp, line 1590, as _ZNK19QTextHtmlParserNode17hasOnlyWhitespaceEv
#if !defined(QT_NO_TEXTHTMLPARSER)
inline bool QTextHtmlParserNode::hasOnlyWhitespace() const
{
    for (int i = 0; i < text.size(); ++i)
        if (!text.at(i).isSpace() || text.at(i) == QChar::LineSeparator)
            return false;
    return true;
}
#endif  // !defined(QT_NO_TEXTHTMLPARSER)

//  from src/gui/text/qtexthtmlparser.cpp, line 596, as _ZN15QTextHtmlParser5parseEv
#if !defined(QT_NO_TEXTHTMLPARSER)
inline void QTextHtmlParser::parse()
{
    while (pos < len) {
        QChar c = txt.at(pos++);
        if (c == u'<') {
            parseTag();
        } else if (c == u'&') {
            nodes.last()->text += parseEntity();
        } else {
            nodes.last()->text += c;
        }
    }
}
#endif  // !defined(QT_NO_TEXTHTMLPARSER)

//  from src/gui/text/qtexthtmlparser.cpp, line 447, as _ZN19QTextHtmlParserNodeC1Ev
#if !defined(QT_NO_TEXTHTMLPARSER)
inline QTextHtmlParserNode::QTextHtmlParserNode()
    : parent(0), id(Html_unknown),
      cssFloat(QTextFrameFormat::InFlow), hasOwnListStyle(false), hasOwnLineHeightType(false), hasLineHeightMultiplier(false),
      hasCssListIndent(false), isEmptyParagraph(false), isTextFrame(false), isRootFrame(false),
      displayMode(QTextHtmlElement::DisplayInline), hasHref(false),
      listStyle(QTextListFormat::ListStyleUndefined), imageWidth(-1), imageHeight(-1), tableBorder(0),
      tableCellRowSpan(1), tableCellColSpan(1), tableCellSpacing(2), tableCellPadding(0),
      borderBrush(Qt::darkGray), borderStyle(QTextFrameFormat::BorderStyle_Outset),
      borderCollapse(false),
      userState(-1), cssListIndent(0), wsm(WhiteSpaceModeUndefined)
{
    margin[QTextHtmlParser::MarginLeft] = 0;
    margin[QTextHtmlParser::MarginRight] = 0;
    margin[QTextHtmlParser::MarginTop] = 0;
    margin[QTextHtmlParser::MarginBottom] = 0;

    for (int i = 0; i < 4; ++i) {
        tableCellBorderStyle[i] = QTextFrameFormat::BorderStyle_None;
        tableCellBorder[i] = 0;
        tableCellBorderBrush[i] = Qt::NoBrush;
    }
}
#endif  // !defined(QT_NO_TEXTHTMLPARSER)

//  from src/gui/text/qtextdocumentfragment.cpp, line 461, as _ZN17QTextHtmlImporter6importEv
#if !defined(QT_NO_TEXTHTMLPARSER)
inline void QTextHtmlImporter::import()
{
    cursor.beginEditBlock();
    hasBlock = true;
    forceBlockMerging = false;
    compressNextWhitespace = RemoveWhiteSpace;
    blockTagClosed = false;
    for (currentNodeIdx = 0; currentNodeIdx < count(); ++currentNodeIdx) {
        currentNode = &at(currentNodeIdx);
        wsm = textEditMode ? QTextHtmlParserNode::WhiteSpacePreWrap : currentNode->wsm;

        /*
         * process each node in three stages:
         * 1) check if the hierarchy changed and we therefore passed the
         *    equivalent of a closing tag -> we may need to finish off
         *    some structures like tables
         *
         * 2) check if the current node is a special node like a
         *    <table>, <ul> or <img> tag that requires special processing
         *
         * 3) if the node should result in a QTextBlock create one and
         *    finally insert text that may be attached to the node
         */

        /* emit 'closing' table blocks or adjust current indent level
         * if we
         *  1) are beyond the first node
         *  2) the current node not being a child of the previous node
         *      means there was a tag closing in the input html
         */
        if (currentNodeIdx > 0 && (currentNode->parent != currentNodeIdx - 1)) {
            const bool lastBlockTagClosed = closeTag();
            blockTagClosed = blockTagClosed || lastBlockTagClosed;
            // visually collapse subsequent block tags, but if the element after the closed block tag
            // is for example an inline element (!isBlock) we have to make sure we start a new paragraph by setting
            // hasBlock to false.
            if (blockTagClosed
                && !currentNode->isBlock()
                && currentNode->id != Html_unknown)
            {
                hasBlock = false;
            } else if (blockTagClosed && hasBlock) {
                // when collapsing subsequent block tags we need to clear the block format
                QTextBlockFormat blockFormat = currentNode->blockFormat;
                blockFormat.setIndent(indent);

                QTextBlockFormat oldFormat = cursor.blockFormat();
                if (oldFormat.hasProperty(QTextFormat::PageBreakPolicy)) {
                    QTextFormat::PageBreakFlags pageBreak = oldFormat.pageBreakPolicy();
                    if (pageBreak == QTextFormat::PageBreak_AlwaysAfter)
                        /* We remove an empty paragrah that requested a page break after.
                           moving that request to the next paragraph means we also need to make
                            that a pagebreak before to keep the same visual appearance.
                        */
                        pageBreak = QTextFormat::PageBreak_AlwaysBefore;
                    blockFormat.setPageBreakPolicy(pageBreak);
                }

                cursor.setBlockFormat(blockFormat);
            }
        }

        if (currentNode->displayMode == QTextHtmlElement::DisplayNone) {
            if (currentNode->id == Html_title)
                doc->setMetaInformation(QTextDocument::DocumentTitle, currentNode->text);
            // ignore explicitly 'invisible' elements
            continue;
        }

        if (processSpecialNodes() == ContinueWithNextNode)
            continue;

        // make sure there's a block for 'Blah' after <ul><li>foo</ul>Blah
        if (blockTagClosed
            && !hasBlock
            && !currentNode->isBlock()
            && !currentNode->text.isEmpty() && !currentNode->hasOnlyWhitespace()
            && currentNode->displayMode == QTextHtmlElement::DisplayInline) {

            QTextBlockFormat block = currentNode->blockFormat;
            block.setIndent(indent);

            appendBlock(block, currentNode->charFormat);

            blockTagClosed = false;
            hasBlock = true;
        }

        if (currentNode->isBlock()) {
            QTextHtmlImporter::ProcessNodeResult result = processBlockNode();
            if (result == ContinueWithNextNode) {
                continue;
            } else if (result == ContinueWithNextSibling) {
                currentNodeIdx += currentNode->children.size();
                continue;
            }
        }

        if (currentNode->charFormat.isAnchor()) {
            const auto names = currentNode->charFormat.anchorNames();
            if (!names.isEmpty())
                namedAnchors.append(names.constFirst());
        }

        if (appendNodeText())
            hasBlock = false; // if we actually appended text then we don't
                              // have an empty block anymore
    }

    cursor.endEditBlock();
}
#endif  // !defined(QT_NO_TEXTHTMLPARSER)

//  from src/gui/text/qtextdocumentfragment.cpp, line 807, as _ZN17QTextHtmlImporter8closeTagEv
#if !defined(QT_NO_TEXTHTMLPARSER)
inline bool QTextHtmlImporter::closeTag()
{
    const QTextHtmlParserNode *closedNode = &at(currentNodeIdx - 1);
    const int endDepth = depth(currentNodeIdx) - 1;
    int depth = this->depth(currentNodeIdx - 1);
    bool blockTagClosed = false;

    while (depth > endDepth) {
        Table *t = nullptr;
        if (!tables.isEmpty())
            t = &tables.last();

        switch (closedNode->id) {
            case Html_tr:
                if (t && !t->isTextFrame) {
                    ++t->currentRow;

                    // for broken html with rowspans but missing tr tags
                    while (!t->currentCell.atEnd() && t->currentCell.row < t->currentRow)
                        ++t->currentCell;
                }

                blockTagClosed = true;
                break;

            case Html_table:
                if (!t)
                    break;
                indent = t->lastIndent;

                tables.resize(tables.size() - 1);
                t = nullptr;

                if (tables.isEmpty()) {
                    cursor = doc->rootFrame()->lastCursorPosition();
                } else {
                    t = &tables.last();
                    if (t->isTextFrame)
                        cursor = t->frame->lastCursorPosition();
                    else if (!t->currentCell.atEnd())
                        cursor = t->currentCell.cell().lastCursorPosition();
                }

                // we don't need an extra block after tables, so we don't
                // claim to have closed one for the creation of a new one
                // in import()
                blockTagClosed = false;
                compressNextWhitespace = RemoveWhiteSpace;
                break;

            case Html_th:
            case Html_td:
                if (t && !t->isTextFrame)
                    ++t->currentCell;
                blockTagClosed = true;
                compressNextWhitespace = RemoveWhiteSpace;
                break;

            case Html_ol:
            case Html_ul:
                if (lists.isEmpty())
                    break;
                lists.resize(lists.size() - 1);
                if (closedNode->hasCssListIndent)
                    indent -= closedNode->cssListIndent;
                else
                    --indent;
                blockTagClosed = true;
                break;

            case Html_br:
                compressNextWhitespace = RemoveWhiteSpace;
                break;

            case Html_div:
                if (cursor.position() > 0) {
                    const QChar curChar = cursor.document()->characterAt(cursor.position() - 1);
                    if (!closedNode->children.isEmpty() && curChar != QChar::LineSeparator) {
                        blockTagClosed = true;
                    }
                }
                break;
            case Html_h1:
            case Html_h2:
            case Html_h3:
            case Html_h4:
            case Html_h5:
            case Html_h6:
                headingLevel = 0;
                blockTagClosed = true;
                break;
            default:
                if (closedNode->isBlock())
                    blockTagClosed = true;
                break;
        }

        closedNode = &at(closedNode->parent);
        --depth;
    }

    return blockTagClosed;
}
#endif  // !defined(QT_NO_TEXTHTMLPARSER)

//  from src/gui/text/qtextdocumentfragment.cpp, line 911, as _ZN17QTextHtmlImporter9scanTableEi
#if !defined(QT_NO_TEXTHTMLPARSER)
inline QTextHtmlImporter::Table QTextHtmlImporter::scanTable(int tableNodeIdx)
{
    Table table;
    table.columns = 0;

    QList<QTextLength> columnWidths;

    int tableHeaderRowCount = 0;
    QList<int> rowNodes;
    rowNodes.reserve(at(tableNodeIdx).children.size());
    for (int row : at(tableNodeIdx).children) {
        switch (at(row).id) {
            case Html_tr:
                rowNodes += row;
                break;
            case Html_thead:
            case Html_tbody:
            case Html_tfoot:
                for (int potentialRow : at(row).children) {
                    if (at(potentialRow).id == Html_tr) {
                        rowNodes += potentialRow;
                        if (at(row).id == Html_thead)
                            ++tableHeaderRowCount;
                    }
                }
                break;
            default: break;
        }
    }

    QList<RowColSpanInfo> rowColSpans;
    QList<RowColSpanInfo> rowColSpanForColumn;

    int effectiveRow = 0;
    for (int row : std::as_const(rowNodes)) {
        int colsInRow = 0;

        for (int cell : at(row).children) {
            if (at(cell).isTableCell()) {
                // skip all columns with spans from previous rows
                while (colsInRow < rowColSpanForColumn.size()) {
                    const RowColSpanInfo &spanInfo = rowColSpanForColumn.at(colsInRow);

                    if (spanInfo.row + spanInfo.rowSpan > effectiveRow) {
                        Q_ASSERT(spanInfo.col == colsInRow);
                        colsInRow += spanInfo.colSpan;
                    } else
                        break;
                }

                const QTextHtmlParserNode &c = at(cell);
                const int currentColumn = colsInRow;
                colsInRow += c.tableCellColSpan;

                RowColSpanInfo spanInfo;
                spanInfo.row = effectiveRow;
                spanInfo.col = currentColumn;
                spanInfo.colSpan = c.tableCellColSpan;
                spanInfo.rowSpan = c.tableCellRowSpan;
                if (spanInfo.colSpan > 1 || spanInfo.rowSpan > 1)
                    rowColSpans.append(spanInfo);

                columnWidths.resize(qMax(columnWidths.size(), colsInRow));
                rowColSpanForColumn.resize(columnWidths.size());
                for (int i = currentColumn; i < currentColumn + c.tableCellColSpan; ++i) {
                    if (columnWidths.at(i).type() == QTextLength::VariableLength) {
                        QTextLength w = c.width;
                        if (c.tableCellColSpan > 1 && w.type() != QTextLength::VariableLength)
                            w = QTextLength(w.type(), w.value(100.) / c.tableCellColSpan);
                        columnWidths[i] = w;
                    }
                    rowColSpanForColumn[i] = spanInfo;
                }
            }
        }

        table.columns = qMax(table.columns, colsInRow);

        ++effectiveRow;
    }
    table.rows = effectiveRow;

    table.lastIndent = indent;
    indent = 0;

    if (table.rows == 0 || table.columns == 0)
        return table;

    QTextFrameFormat fmt;
    const QTextHtmlParserNode &node = at(tableNodeIdx);

    if (!node.isTextFrame) {
        QTextTableFormat tableFmt;
        tableFmt.setCellSpacing(node.tableCellSpacing);
        tableFmt.setCellPadding(node.tableCellPadding);
        if (node.blockFormat.hasProperty(QTextFormat::BlockAlignment))
            tableFmt.setAlignment(node.blockFormat.alignment());
        tableFmt.setColumns(table.columns);
        tableFmt.setColumnWidthConstraints(columnWidths);
        tableFmt.setHeaderRowCount(tableHeaderRowCount);
        tableFmt.setBorderCollapse(node.borderCollapse);
        fmt = tableFmt;
    }

    fmt.setTopMargin(topMargin(tableNodeIdx));
    fmt.setBottomMargin(bottomMargin(tableNodeIdx));
    fmt.setLeftMargin(leftMargin(tableNodeIdx)
                      + table.lastIndent * 40 // ##### not a good emulation
                      );
    fmt.setRightMargin(rightMargin(tableNodeIdx));

    // compatibility
    if (qFuzzyCompare(fmt.leftMargin(), fmt.rightMargin())
        && qFuzzyCompare(fmt.leftMargin(), fmt.topMargin())
        && qFuzzyCompare(fmt.leftMargin(), fmt.bottomMargin()))
        fmt.setProperty(QTextFormat::FrameMargin, fmt.leftMargin());

    fmt.setBorderStyle(node.borderStyle);
    fmt.setBorderBrush(node.borderBrush);
    fmt.setBorder(node.tableBorder);
    fmt.setWidth(node.width);
    fmt.setHeight(node.height);
    if (node.blockFormat.hasProperty(QTextFormat::PageBreakPolicy))
        fmt.setPageBreakPolicy(node.blockFormat.pageBreakPolicy());

    if (node.blockFormat.hasProperty(QTextFormat::LayoutDirection))
        fmt.setLayoutDirection(node.blockFormat.layoutDirection());
    if (node.charFormat.background().style() != Qt::NoBrush)
        fmt.setBackground(node.charFormat.background());
    fmt.setPosition(QTextFrameFormat::Position(node.cssFloat));

    if (node.isTextFrame) {
        if (node.isRootFrame) {
            table.frame = cursor.currentFrame();
            table.frame->setFrameFormat(fmt);
        } else
            table.frame = cursor.insertFrame(fmt);

        table.isTextFrame = true;
    } else {
        const int oldPos = cursor.position();
        QTextTable *textTable = cursor.insertTable(table.rows, table.columns, fmt.toTableFormat());
        table.frame = textTable;

        for (int i = 0; i < rowColSpans.size(); ++i) {
            const RowColSpanInfo &nfo = rowColSpans.at(i);
            textTable->mergeCells(nfo.row, nfo.col, nfo.rowSpan, nfo.colSpan);
        }

        table.currentCell = TableCellIterator(textTable);
        cursor.setPosition(oldPos); // restore for caption support which needs to be inserted right before the table
    }
    return table;
}
#endif  // !defined(QT_NO_TEXTHTMLPARSER)

//  from src/gui/text/qtextdocumentfragment.cpp, line 1266, as _ZN17QTextHtmlImporter11appendBlockERK16QTextBlockFormat15QTextCharFormat
#if !defined(QT_NO_TEXTHTMLPARSER)
inline void QTextHtmlImporter::appendBlock(const QTextBlockFormat &format, QTextCharFormat charFmt)
{
    if (!namedAnchors.isEmpty()) {
        charFmt.setAnchor(true);
        charFmt.setAnchorNames(namedAnchors);
        namedAnchors.clear();
    }

    cursor.insertBlock(format, charFmt);

    if (wsm != QTextHtmlParserNode::WhiteSpacePre && wsm != QTextHtmlParserNode::WhiteSpacePreWrap)
        compressNextWhitespace = RemoveWhiteSpace;
}
#endif  // !defined(QT_NO_TEXTHTMLPARSER)

//  from src/gui/text/qtextdocumentfragment.cpp, line 573, as _ZN17QTextHtmlImporter14appendNodeTextEv
#if !defined(QT_NO_TEXTHTMLPARSER)
inline bool QTextHtmlImporter::appendNodeText()
{
    const int initialCursorPosition = cursor.position();
    QTextCharFormat format = currentNode->charFormat;

    if (wsm == QTextHtmlParserNode::WhiteSpacePre || wsm == QTextHtmlParserNode::WhiteSpacePreWrap)
        compressNextWhitespace = PreserveWhiteSpace;

    const QString text = currentNode->text;

    QString textToInsert;
    textToInsert.reserve(text.size());

    QStringIterator it(text);
    while (it.hasNext()) {
        char32_t ch = it.next();

        if (QChar::isSpace(ch)
            && ch != QChar::Nbsp
            && ch != QChar::ParagraphSeparator) {

            if (wsm == QTextHtmlParserNode::WhiteSpacePreLine && (ch == u'\n' || ch == u'\r'))
                compressNextWhitespace = PreserveWhiteSpace;

            if (compressNextWhitespace == CollapseWhiteSpace)
                compressNextWhitespace = RemoveWhiteSpace; // allow this one, and remove the ones coming next.
            else if (compressNextWhitespace == RemoveWhiteSpace)
                continue;

            if (wsm == QTextHtmlParserNode::WhiteSpacePre
                || textEditMode
               ) {
                if (ch == u'\n') {
                    if (textEditMode)
                        continue;
                } else if (ch == u'\r') {
                    continue;
                }
            } else if (wsm != QTextHtmlParserNode::WhiteSpacePreWrap) {
                compressNextWhitespace = RemoveWhiteSpace;
                if (wsm == QTextHtmlParserNode::WhiteSpacePreLine && (ch == u'\n' || ch == u'\r'))
                { }
                else if (wsm == QTextHtmlParserNode::WhiteSpaceNoWrap)
                    ch = QChar::Nbsp;
                else
                    ch = u' ';
            }
        } else {
            compressNextWhitespace = PreserveWhiteSpace;
        }

        if (ch == u'\n'
            || ch == QChar::ParagraphSeparator) {

            if (!textToInsert.isEmpty()) {
                if (wsm == QTextHtmlParserNode::WhiteSpacePreLine && textToInsert.at(textToInsert.size() - 1) == u' ')
                    textToInsert = textToInsert.chopped(1);
                cursor.insertText(textToInsert, format);
                textToInsert.clear();
            }

            QTextBlockFormat fmt = cursor.blockFormat();

            if (fmt.hasProperty(QTextFormat::BlockBottomMargin)) {
                QTextBlockFormat tmp = fmt;
                tmp.clearProperty(QTextFormat::BlockBottomMargin);
                cursor.setBlockFormat(tmp);
            }

            fmt.clearProperty(QTextFormat::BlockTopMargin);
            appendBlock(fmt, cursor.charFormat());
        } else {
            if (!namedAnchors.isEmpty()) {
                if (!textToInsert.isEmpty()) {
                    cursor.insertText(textToInsert, format);
                    textToInsert.clear();
                }

                format.setAnchor(true);
                format.setAnchorNames(namedAnchors);
                cursor.insertText(QString::fromUcs4(&ch, 1), format);
                namedAnchors.clear();
                format.clearProperty(QTextFormat::IsAnchor);
                format.clearProperty(QTextFormat::AnchorName);
            } else {
                textToInsert += QChar::fromUcs4(ch);
            }
        }
    }

    if (!textToInsert.isEmpty()) {
        cursor.insertText(textToInsert, format);
    }

    return cursor.position() != initialCursorPosition;
}
#endif  // !defined(QT_NO_TEXTHTMLPARSER)

//  from src/gui/text/qtextdocumentfragment.cpp, line 1066, as _ZN17QTextHtmlImporter16processBlockNodeEv
#if !defined(QT_NO_TEXTHTMLPARSER)
inline QTextHtmlImporter::ProcessNodeResult QTextHtmlImporter::processBlockNode()
{
    QTextBlockFormat block;
    QTextCharFormat charFmt;
    bool modifiedBlockFormat = true;
    bool modifiedCharFormat = true;

    if (currentNode->isTableCell() && !tables.isEmpty()) {
        Table &t = tables.last();
        if (!t.isTextFrame && !t.currentCell.atEnd()) {
            QTextTableCell cell = t.currentCell.cell();
            if (cell.isValid()) {
                QTextTableCellFormat fmt = cell.format().toTableCellFormat();
                if (topPadding(currentNodeIdx) >= 0)
                    fmt.setTopPadding(topPadding(currentNodeIdx));
                if (bottomPadding(currentNodeIdx) >= 0)
                    fmt.setBottomPadding(bottomPadding(currentNodeIdx));
                if (leftPadding(currentNodeIdx) >= 0)
                    fmt.setLeftPadding(leftPadding(currentNodeIdx));
                if (rightPadding(currentNodeIdx) >= 0)
                    fmt.setRightPadding(rightPadding(currentNodeIdx));
#ifndef QT_NO_CSSPARSER
                if (tableCellBorder(currentNodeIdx, QCss::TopEdge) > 0)
                    fmt.setTopBorder(tableCellBorder(currentNodeIdx, QCss::TopEdge));
                if (tableCellBorder(currentNodeIdx, QCss::RightEdge) > 0)
                    fmt.setRightBorder(tableCellBorder(currentNodeIdx, QCss::RightEdge));
                if (tableCellBorder(currentNodeIdx, QCss::BottomEdge) > 0)
                    fmt.setBottomBorder(tableCellBorder(currentNodeIdx, QCss::BottomEdge));
                if (tableCellBorder(currentNodeIdx, QCss::LeftEdge) > 0)
                    fmt.setLeftBorder(tableCellBorder(currentNodeIdx, QCss::LeftEdge));
                if (tableCellBorderStyle(currentNodeIdx, QCss::TopEdge) != QTextFrameFormat::BorderStyle_None)
                    fmt.setTopBorderStyle(tableCellBorderStyle(currentNodeIdx, QCss::TopEdge));
                if (tableCellBorderStyle(currentNodeIdx, QCss::RightEdge) != QTextFrameFormat::BorderStyle_None)
                    fmt.setRightBorderStyle(tableCellBorderStyle(currentNodeIdx, QCss::RightEdge));
                if (tableCellBorderStyle(currentNodeIdx, QCss::BottomEdge) != QTextFrameFormat::BorderStyle_None)
                    fmt.setBottomBorderStyle(tableCellBorderStyle(currentNodeIdx, QCss::BottomEdge));
                if (tableCellBorderStyle(currentNodeIdx, QCss::LeftEdge) != QTextFrameFormat::BorderStyle_None)
                    fmt.setLeftBorderStyle(tableCellBorderStyle(currentNodeIdx, QCss::LeftEdge));
                if (tableCellBorderBrush(currentNodeIdx, QCss::TopEdge) != Qt::NoBrush)
                    fmt.setTopBorderBrush(tableCellBorderBrush(currentNodeIdx, QCss::TopEdge));
                if (tableCellBorderBrush(currentNodeIdx, QCss::RightEdge) != Qt::NoBrush)
                    fmt.setRightBorderBrush(tableCellBorderBrush(currentNodeIdx, QCss::RightEdge));
                if (tableCellBorderBrush(currentNodeIdx, QCss::BottomEdge) != Qt::NoBrush)
                    fmt.setBottomBorderBrush(tableCellBorderBrush(currentNodeIdx, QCss::BottomEdge));
                if (tableCellBorderBrush(currentNodeIdx, QCss::LeftEdge) != Qt::NoBrush)
                    fmt.setLeftBorderBrush(tableCellBorderBrush(currentNodeIdx, QCss::LeftEdge));
#endif

                cell.setFormat(fmt);

                cursor.setPosition(cell.firstPosition());
            }
        }
        hasBlock = true;
        compressNextWhitespace = RemoveWhiteSpace;

        if (currentNode->charFormat.background().style() != Qt::NoBrush) {
            charFmt.setBackground(currentNode->charFormat.background());
            cursor.mergeBlockCharFormat(charFmt);
        }
    }

    if (hasBlock) {
        block = cursor.blockFormat();
        charFmt = cursor.blockCharFormat();
        modifiedBlockFormat = false;
        modifiedCharFormat = false;
    }

    // collapse
    {
        qreal tm = qreal(topMargin(currentNodeIdx));
        if (tm > block.topMargin()) {
            block.setTopMargin(tm);
            modifiedBlockFormat = true;
        }
    }

    int bottomMargin = this->bottomMargin(currentNodeIdx);

    // for list items we may want to collapse with the bottom margin of the
    // list.
    const QTextHtmlParserNode *parentNode = currentNode->parent ? &at(currentNode->parent) : nullptr;
    if ((currentNode->id == Html_li || currentNode->id == Html_dt || currentNode->id == Html_dd)
        && parentNode
        && (parentNode->isListStart() || parentNode->id == Html_dl)
        && (parentNode->children.last() == currentNodeIdx)) {
        bottomMargin = qMax(bottomMargin, this->bottomMargin(currentNode->parent));
    }

    if (block.bottomMargin() != bottomMargin) {
        block.setBottomMargin(bottomMargin);
        modifiedBlockFormat = true;
    }

    {
        const qreal lm = leftMargin(currentNodeIdx);
        const qreal rm = rightMargin(currentNodeIdx);

        if (block.leftMargin() != lm) {
            block.setLeftMargin(lm);
            modifiedBlockFormat = true;
        }
        if (block.rightMargin() != rm) {
            block.setRightMargin(rm);
            modifiedBlockFormat = true;
        }
    }

    if (currentNode->id != Html_li
        && indent != 0
        && (lists.isEmpty()
            || !hasBlock
            || !lists.constLast().list
            || lists.constLast().list->itemNumber(cursor.block()) == -1
           )
       ) {
        block.setIndent(indent);
        modifiedBlockFormat = true;
    }

    if (headingLevel) {
        block.setHeadingLevel(headingLevel);
        modifiedBlockFormat = true;
    }

    if (currentNode->blockFormat.propertyCount() > 0) {
        modifiedBlockFormat = true;
        block.merge(currentNode->blockFormat);
    }

    if (currentNode->charFormat.propertyCount() > 0) {
        modifiedCharFormat = true;
        charFmt.merge(currentNode->charFormat);
    }

    // ####################
    //                block.setFloatPosition(node->cssFloat);

    if (wsm == QTextHtmlParserNode::WhiteSpacePre
            || wsm == QTextHtmlParserNode::WhiteSpaceNoWrap) {
        block.setNonBreakableLines(true);
        modifiedBlockFormat = true;
    }

    if (currentNode->charFormat.background().style() != Qt::NoBrush && !currentNode->isTableCell()) {
        block.setBackground(currentNode->charFormat.background());
        modifiedBlockFormat = true;
    }

    if (hasBlock && (!currentNode->isEmptyParagraph || forceBlockMerging)) {
        if (modifiedBlockFormat)
            cursor.setBlockFormat(block);
        if (modifiedCharFormat)
            cursor.setBlockCharFormat(charFmt);
    } else {
        if (currentNodeIdx == 1 && cursor.position() == 0 && currentNode->isEmptyParagraph) {
            cursor.setBlockFormat(block);
            cursor.setBlockCharFormat(charFmt);
        } else {
            appendBlock(block, charFmt);
        }
    }

    if (currentNode->userState != -1)
        cursor.block().setUserState(currentNode->userState);

    if (currentNode->id == Html_li && !lists.isEmpty()) {
        List &l = lists.last();
        if (l.list) {
            l.list->add(cursor.block());
        } else {
            l.list = cursor.createList(l.format);
            const qreal listTopMargin = topMargin(l.listNode);
            if (listTopMargin > block.topMargin()) {
                block.setTopMargin(listTopMargin);
                cursor.mergeBlockFormat(block);
            }
        }
        if (hasBlock) {
            QTextBlockFormat fmt;
            fmt.setIndent(currentNode->blockFormat.indent());
            cursor.mergeBlockFormat(fmt);
        }
    }

    forceBlockMerging = false;
    if (currentNode->id == Html_body || currentNode->id == Html_html)
        forceBlockMerging = true;

    if (currentNode->isEmptyParagraph) {
        hasBlock = false;
        return ContinueWithNextSibling;
    }

    hasBlock = true;
    blockTagClosed = false;
    return ContinueWithCurrentNode;
}
#endif  // !defined(QT_NO_TEXTHTMLPARSER)

//  from src/gui/text/qtextdocumentfragment.cpp, line 670, as _ZN17QTextHtmlImporter19processSpecialNodesEv
#if !defined(QT_NO_TEXTHTMLPARSER)
inline QTextHtmlImporter::ProcessNodeResult QTextHtmlImporter::processSpecialNodes()
{
    switch (currentNode->id) {
        case Html_body:
            if (currentNode->charFormat.background().style() != Qt::NoBrush) {
                QTextFrameFormat fmt = doc->rootFrame()->frameFormat();
                fmt.setBackground(currentNode->charFormat.background());
                doc->rootFrame()->setFrameFormat(fmt);
                const_cast<QTextHtmlParserNode *>(currentNode)->charFormat.clearProperty(QTextFormat::BackgroundBrush);
            }
            compressNextWhitespace = RemoveWhiteSpace;
            break;

        case Html_ol:
        case Html_ul: {
            QTextListFormat::Style style = currentNode->listStyle;

            if (currentNode->id == Html_ul && !currentNode->hasOwnListStyle && currentNode->parent) {
                const QTextHtmlParserNode *n = &at(currentNode->parent);
                while (n) {
                    if (n->id == Html_ul) {
                        style = nextListStyle(currentNode->listStyle);
                    }
                    if (n->parent)
                        n = &at(n->parent);
                    else
                        n = nullptr;
                }
            }

            QTextListFormat listFmt;
            listFmt.setStyle(style);
            if (!currentNode->textListNumberPrefix.isNull())
                listFmt.setNumberPrefix(currentNode->textListNumberPrefix);
            if (!currentNode->textListNumberSuffix.isNull())
                listFmt.setNumberSuffix(currentNode->textListNumberSuffix);
            if (currentNode->listStart != 1)
                listFmt.setStart(currentNode->listStart);

            if (currentNode->hasCssListIndent) {
                indent += currentNode->cssListIndent;
                listFmt.setIndent(currentNode->cssListIndent);
            } else {
                ++indent;
                listFmt.setIndent(indent);
            }

            List l;
            l.format = listFmt;
            l.listNode = currentNodeIdx;
            lists.append(l);
            compressNextWhitespace = RemoveWhiteSpace;

            // broken html: <ul>Text here<li>Foo
            const QString simpl = currentNode->text.simplified();
            if (simpl.isEmpty() || simpl.at(0).isSpace())
                return ContinueWithNextNode;
            break;
        }

        case Html_table: {
            Table t = scanTable(currentNodeIdx);
            tables.append(t);
            hasBlock = false;
            compressNextWhitespace = RemoveWhiteSpace;
            return ContinueWithNextNode;
        }

        case Html_tr:
            return ContinueWithNextNode;

        case Html_img: {
            QTextImageFormat fmt;
            fmt.setName(currentNode->imageName);
            if (!currentNode->text.isEmpty())
                fmt.setProperty(QTextFormat::ImageTitle, currentNode->text);
            if (!currentNode->imageAlt.isEmpty())
                fmt.setProperty(QTextFormat::ImageAltText, currentNode->imageAlt);

            fmt.merge(currentNode->charFormat);

            if (currentNode->imageWidth != -1)
                fmt.setWidth(currentNode->imageWidth);
            if (currentNode->imageHeight != -1)
                fmt.setHeight(currentNode->imageHeight);

            cursor.insertImage(fmt, QTextFrameFormat::Position(currentNode->cssFloat));

            cursor.movePosition(QTextCursor::PreviousCharacter, QTextCursor::KeepAnchor);
            cursor.mergeCharFormat(currentNode->charFormat);
            cursor.movePosition(QTextCursor::NextCharacter);
            compressNextWhitespace = CollapseWhiteSpace;

            hasBlock = false;
            return ContinueWithNextNode;
        }

        case Html_hr: {
            QTextBlockFormat blockFormat = currentNode->blockFormat;
            blockFormat.setTopMargin(topMargin(currentNodeIdx));
            blockFormat.setBottomMargin(bottomMargin(currentNodeIdx));
            blockFormat.setProperty(QTextFormat::BlockTrailingHorizontalRulerWidth, currentNode->width);
            if (hasBlock && importMode == ImportToDocument)
                cursor.mergeBlockFormat(blockFormat);
            else
                appendBlock(blockFormat);
            hasBlock = false;
            compressNextWhitespace = RemoveWhiteSpace;
            return ContinueWithNextNode;
        }

        case Html_h1:
            headingLevel = 1;
            break;
        case Html_h2:
            headingLevel = 2;
            break;
        case Html_h3:
            headingLevel = 3;
            break;
        case Html_h4:
            headingLevel = 4;
            break;
        case Html_h5:
            headingLevel = 5;
            break;
        case Html_h6:
            headingLevel = 6;
            break;

        default: break;
    }

    return ContinueWithCurrentNode;
}
#endif  // !defined(QT_NO_TEXTHTMLPARSER)
//  -----------------------------------------------------------------------

#if !defined(QT_NO_TEXTHTMLPARSER)
//  void QTextHtmlImporter::import()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QTextHtmlImporter6importEv(QTextHtmlImporter *self) {
  self->import();
}
#endif  // !defined(QT_NO_TEXTHTMLPARSER)

#if !defined(QT_NO_TEXTHTMLPARSER)
//  bool QTextHtmlImporter::closeTag()
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QTextHtmlImporter8closeTagEv(QTextHtmlImporter *self) {
  return self->closeTag();
}
#endif  // !defined(QT_NO_TEXTHTMLPARSER)

#if !defined(QT_NO_TEXTHTMLPARSER)
//  Table QTextHtmlImporter::scanTable(int tableNodeIdx)
extern "C" Q_DECL_EXPORT
QTextHtmlImporter::Table *ritual_ZN17QTextHtmlImporter9scanTableEi(
    QTextHtmlImporter *self,
    int tableNodeIdx) {
  return new QTextHtmlImporter::Table(self->scanTable(tableNodeIdx));
}
#endif  // !defined(QT_NO_TEXTHTMLPARSER)

#if !defined(QT_NO_TEXTHTMLPARSER)
//  void QTextHtmlImporter::appendBlock(const QTextBlockFormat &format,
//      QTextCharFormat charFmt)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QTextHtmlImporter11appendBlockERK16QTextBlockFormat15QTextCharFormat(
    QTextHtmlImporter *self,
    const QTextBlockFormat *format,
    const QTextCharFormat *charFmt) {
  self->appendBlock(*format, *charFmt);
}
#endif  // !defined(QT_NO_TEXTHTMLPARSER)

#if !defined(QT_NO_TEXTHTMLPARSER)
//  bool QTextHtmlImporter::appendNodeText()
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QTextHtmlImporter14appendNodeTextEv(
    QTextHtmlImporter *self) {
  return self->appendNodeText();
}
#endif  // !defined(QT_NO_TEXTHTMLPARSER)

#if !defined(QT_NO_TEXTHTMLPARSER)
//  ProcessNodeResult QTextHtmlImporter::processBlockNode()
extern "C" Q_DECL_EXPORT
QTextHtmlImporter::ProcessNodeResult ritual_ZN17QTextHtmlImporter16processBlockNodeEv(
    QTextHtmlImporter *self) {
  return self->processBlockNode();
}
#endif  // !defined(QT_NO_TEXTHTMLPARSER)

#if !defined(QT_NO_TEXTHTMLPARSER)
//  ProcessNodeResult QTextHtmlImporter::processSpecialNodes()
extern "C" Q_DECL_EXPORT
QTextHtmlImporter::ProcessNodeResult ritual_ZN17QTextHtmlImporter19processSpecialNodesEv(
    QTextHtmlImporter *self) {
  return self->processSpecialNodes();
}
#endif  // !defined(QT_NO_TEXTHTMLPARSER)

//  QTextHtmlImporter::~QTextHtmlImporter()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QTextHtmlImporterD1Ev(QTextHtmlImporter *self) {
  delete self;
}

//  a QTextHtmlImporter::Table a ritual of QTextHtmlImporter gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QTextHtmlImporter__QTextHtmlImporter_Table(
    QTextHtmlImporter::Table *self) {
  delete self;
}

#endif  // !defined(QT_NO_TEXTHTMLPARSER)
