//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qtexthtmlparser_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: the ritual of parseWord() and the
//  copy of its body are taken out, as the body calls
//  parseEntity() without arguments, which Qt's library does not
//  offer (undefined reference). Kept as it is when the generator
//  runs again.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if !defined(QT_NO_TEXTHTMLPARSER)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtexthtmlparser_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qbrush.h>
#include <QtCore/qanystringview.h>
#include <QtCore/qstring.h>
#include <QtCore/qstringview.h>
#include <QtCore/qchar.h>
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
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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

//  from src/gui/text/qtexthtmlparser.cpp, line 576, as _ZNK15QTextHtmlParser9topMarginEi
#if !defined(QT_NO_TEXTHTMLPARSER)
inline int QTextHtmlParser::topMargin(int i) const
{
    if (!i)
        return 0;
    return at(i).margin[MarginTop];
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

//  from src/gui/text/qtexthtmlparser.cpp, line 479, as _ZN15QTextHtmlParser7newNodeEi
#if !defined(QT_NO_TEXTHTMLPARSER)
inline QTextHtmlParserNode *QTextHtmlParser::newNode(int parent)
{
    QTextHtmlParserNode *lastNode = nodes.last();
    QTextHtmlParserNode *newNode = nullptr;

    bool reuseLastNode = true;

    if (nodes.size() == 1) {
        reuseLastNode = false;
    } else if (lastNode->tag.isEmpty()) {

        if (lastNode->text.isEmpty()) {
            reuseLastNode = true;
        } else { // last node is a text node (empty tag) with some text

            if (lastNode->text.size() == 1 && lastNode->text.at(0).isSpace()) {

                int lastSibling = count() - 2;
                while (lastSibling
                       && at(lastSibling).parent != lastNode->parent
                       && at(lastSibling).displayMode == QTextHtmlElement::DisplayInline) {
                    lastSibling = at(lastSibling).parent;
                }

                if (at(lastSibling).displayMode == QTextHtmlElement::DisplayInline) {
                    reuseLastNode = false;
                } else {
                    reuseLastNode = true;
                }
            } else {
                // text node with real (non-whitespace) text -> nothing to re-use
                reuseLastNode = false;
            }

        }

    } else {
        // last node had a proper tag -> nothing to re-use
        reuseLastNode = false;
    }

    if (reuseLastNode) {
        newNode = lastNode;
        newNode->tag.clear();
        newNode->text.clear();
        newNode->id = Html_unknown;
    } else {
        nodes.append(new QTextHtmlParserNode);
        newNode = nodes.last();
    }

    newNode->parent = parent;
    return newNode;
}
#endif  // !defined(QT_NO_TEXTHTMLPARSER)

//  from src/gui/text/qtexthtmlparser.cpp, line 590, as _ZN15QTextHtmlParser8eatSpaceEv
#if !defined(QT_NO_TEXTHTMLPARSER)
inline void QTextHtmlParser::eatSpace()
{
    while (pos < len && txt.at(pos).isSpace() && txt.at(pos) != QChar::ParagraphSeparator)
        pos++;
}
#endif  // !defined(QT_NO_TEXTHTMLPARSER)

//  from src/gui/text/qtexthtmlparser.cpp, line 2267, as _ZNK15QTextHtmlParser13nodeIsChildOfEi17QTextHTMLElements
#if !defined(QT_NO_TEXTHTMLPARSER)
#if !defined(QT_NO_CSSPARSER)
inline bool QTextHtmlParser::nodeIsChildOf(int i, QTextHTMLElements id) const
{
    while (i) {
        if (at(i).id == id)
            return true;
        i = at(i).parent;
    }
    return false;
}
#endif  // !defined(QT_NO_CSSPARSER)
#endif  // !defined(QT_NO_TEXTHTMLPARSER)
//  -----------------------------------------------------------------------

//  QTextHtmlParser::~QTextHtmlParser()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTextHtmlParserD1Ev(QTextHtmlParser *self) {
  delete self;
}

//  const QTextHtmlParserNode &QTextHtmlParser::at(int i) const
extern "C" Q_DECL_EXPORT
QTextHtmlParserNode *ritual_ZNK15QTextHtmlParser2atEi(
    const QTextHtmlParser *self,
    int i) {
  return new QTextHtmlParserNode(self->at(i));
}

//  QTextHtmlParserNode &QTextHtmlParser::operator[](int i)
extern "C" Q_DECL_EXPORT
QTextHtmlParserNode *ritual_ZN15QTextHtmlParserixEi(
    QTextHtmlParser *self,
    int i) {
  return &(self->operator[](i));
}

//  int QTextHtmlParser::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QTextHtmlParser5countEv(const QTextHtmlParser *self) {
  return self->count();
}

//  int QTextHtmlParser::last() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QTextHtmlParser4lastEv(const QTextHtmlParser *self) {
  return self->last();
}

#if !defined(QT_NO_TEXTHTMLPARSER)
//  int QTextHtmlParser::depth(int i) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QTextHtmlParser5depthEi(const QTextHtmlParser *self, int i) {
  return self->depth(i);
}
#endif  // !defined(QT_NO_TEXTHTMLPARSER)

#if !defined(QT_NO_TEXTHTMLPARSER)
//  int QTextHtmlParser::topMargin(int i) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QTextHtmlParser9topMarginEi(
    const QTextHtmlParser *self,
    int i) {
  return self->topMargin(i);
}
#endif  // !defined(QT_NO_TEXTHTMLPARSER)

#if !defined(QT_NO_TEXTHTMLPARSER)
//  int QTextHtmlParser::bottomMargin(int i) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QTextHtmlParser12bottomMarginEi(
    const QTextHtmlParser *self,
    int i) {
  return self->bottomMargin(i);
}
#endif  // !defined(QT_NO_TEXTHTMLPARSER)

//  int QTextHtmlParser::topPadding(int i) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QTextHtmlParser10topPaddingEi(
    const QTextHtmlParser *self,
    int i) {
  return self->topPadding(i);
}

//  int QTextHtmlParser::bottomPadding(int i) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QTextHtmlParser13bottomPaddingEi(
    const QTextHtmlParser *self,
    int i) {
  return self->bottomPadding(i);
}

//  int QTextHtmlParser::leftPadding(int i) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QTextHtmlParser11leftPaddingEi(
    const QTextHtmlParser *self,
    int i) {
  return self->leftPadding(i);
}

//  int QTextHtmlParser::rightPadding(int i) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QTextHtmlParser12rightPaddingEi(
    const QTextHtmlParser *self,
    int i) {
  return self->rightPadding(i);
}

//  qreal QTextHtmlParser::tableCellBorder(int i, int edge) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK15QTextHtmlParser15tableCellBorderEii(
    const QTextHtmlParser *self,
    int i,
    int edge) {
  return self->tableCellBorder(i, edge);
}

//  QTextFrameFormat::BorderStyle QTextHtmlParser::tableCellBorderStyle(int
//      i, int edge) const
extern "C" Q_DECL_EXPORT
QTextFrameFormat::BorderStyle ritual_ZNK15QTextHtmlParser20tableCellBorderStyleEii(
    const QTextHtmlParser *self,
    int i,
    int edge) {
  return self->tableCellBorderStyle(i, edge);
}

//  QBrush QTextHtmlParser::tableCellBorderBrush(int i, int edge) const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK15QTextHtmlParser20tableCellBorderBrushEii(
    const QTextHtmlParser *self,
    int i,
    int edge) {
  return new QBrush(self->tableCellBorderBrush(i, edge));
}

//  int QTextHtmlParser::lookupElement(QAnyStringView element)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QTextHtmlParser13lookupElementE14QAnyStringView(
    const QString *element) {
  return QTextHtmlParser::lookupElement(QAnyStringView(*element));
}

//  QString QTextHtmlParser::parseEntity(QStringView entity)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QTextHtmlParser11parseEntityE11QStringView(
    const QString *entity) {
  return new QString(QTextHtmlParser::parseEntity(QStringView(*entity)));
}

#if !defined(QT_NO_TEXTHTMLPARSER)
//  QTextHtmlParserNode *QTextHtmlParser::newNode(int parent)
extern "C" Q_DECL_EXPORT
QTextHtmlParserNode *ritual_ZN15QTextHtmlParser7newNodeEi(
    QTextHtmlParser *self,
    int parent) {
  return self->newNode(parent);
}
#endif  // !defined(QT_NO_TEXTHTMLPARSER)

#if !defined(QT_NO_TEXTHTMLPARSER)
//  void QTextHtmlParser::eatSpace()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QTextHtmlParser8eatSpaceEv(QTextHtmlParser *self) {
  self->eatSpace();
}
#endif  // !defined(QT_NO_TEXTHTMLPARSER)

//  bool QTextHtmlParser::hasPrefix(QChar c, int lookahead) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QTextHtmlParser9hasPrefixE5QChari(
    const QTextHtmlParser *self,
    const QChar *c,
    int lookahead) {
  return self->hasPrefix(*c, lookahead);
}

#if !defined(QT_NO_TEXTHTMLPARSER)
#if !defined(QT_NO_CSSPARSER)
//  bool QTextHtmlParser::nodeIsChildOf(int i, QTextHTMLElements id) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QTextHtmlParser13nodeIsChildOfEi17QTextHTMLElements(
    const QTextHtmlParser *self,
    int i,
    QTextHTMLElements id) {
  return self->nodeIsChildOf(i, id);
}
#endif  // !defined(QT_NO_CSSPARSER)
#endif  // !defined(QT_NO_TEXTHTMLPARSER)

#endif  // !defined(QT_NO_TEXTHTMLPARSER)
