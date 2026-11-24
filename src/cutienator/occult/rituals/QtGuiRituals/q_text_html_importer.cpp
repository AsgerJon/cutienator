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
//  -----------------------------------------------------------------------

#if !defined(QT_NO_TEXTHTMLPARSER)
//  bool QTextHtmlImporter::closeTag()
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QTextHtmlImporter8closeTagEv(QTextHtmlImporter *self) {
  return self->closeTag();
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

//  QTextHtmlImporter::~QTextHtmlImporter()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QTextHtmlImporterD1Ev(QTextHtmlImporter *self) {
  delete self;
}

#endif  // !defined(QT_NO_TEXTHTMLPARSER)
