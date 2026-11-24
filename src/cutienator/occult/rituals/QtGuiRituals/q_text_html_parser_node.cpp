//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qtexthtmlparser_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if !defined(QT_NO_TEXTHTMLPARSER)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtexthtmlparser_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
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
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
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

//  from src/gui/text/qtexthtmlparser.cpp, line 964, as _ZNK19QTextHtmlParserNode12isNestedListEPK15QTextHtmlParser
#if !defined(QT_NO_TEXTHTMLPARSER)
inline bool QTextHtmlParserNode::isNestedList(const QTextHtmlParser *parser) const
{
    if (!isListStart())
        return false;

    int p = parent;
    while (p) {
        if (parser->at(p).isListStart())
            return true;
        p = parser->at(p).parent;
    }
    return false;
}
#endif  // !defined(QT_NO_TEXTHTMLPARSER)

//  from src/gui/text/qtexthtmlparser.cpp, line 1528, as _ZN19QTextHtmlParserNode20applyForegroundImageExPK13QTextDocument
#if !defined(QT_NO_TEXTHTMLPARSER)
inline void QTextHtmlParserNode::applyForegroundImage(qint64 searchKey, const QTextDocument *resourceProvider)
{
    const QTextDocumentPrivate *priv = QTextDocumentPrivate::get(resourceProvider);
    for (int i = 0; i < priv->formats.numFormats(); ++i) {
        QTextCharFormat format = priv->formats.charFormat(i);
        if (format.isValid()) {
            QBrush brush = format.foreground();
            if (brush.style() == Qt::TexturePattern) {
                const bool isPixmap = qHasPixmapTexture(brush);

                if (isPixmap && QCoreApplication::instance()->thread() != QThread::currentThread()) {
                    qWarning("Can't apply QPixmap outside of GUI thread");
                    return;
                }

                const qint64 cacheKey = isPixmap ? brush.texture().cacheKey() : brush.textureImage().cacheKey();
                if (cacheKey == searchKey) {
                    QBrush b;
                    if (isPixmap)
                        b.setTexture(brush.texture());
                    else
                        b.setTextureImage(brush.textureImage());
                    b.setStyle(Qt::TexturePattern);
                    charFormat.setForeground(b);
                }
            }
        }
    }

}
#endif  // !defined(QT_NO_TEXTHTMLPARSER)

//  from src/gui/text/qtexthtmlparser.cpp, line 1559, as _ZN19QTextHtmlParserNode20applyBackgroundImageERK7QStringPK13QTextDocument
#if !defined(QT_NO_TEXTHTMLPARSER)
inline void QTextHtmlParserNode::applyBackgroundImage(const QString &url, const QTextDocument *resourceProvider)
{
    if (!url.isEmpty() && resourceProvider) {
        QVariant val = resourceProvider->resource(QTextDocument::ImageResource, QUrl{url});

        if (QCoreApplication::instance()->thread() != QThread::currentThread()) {
            // must use images in non-GUI threads
            if (val.userType() == QMetaType::QImage) {
                QImage image = qvariant_cast<QImage>(val);
                charFormat.setBackground(image);
            } else if (val.userType() == QMetaType::QByteArray) {
                QImage image;
                if (image.loadFromData(val.toByteArray())) {
                    charFormat.setBackground(image);
                }
            }
        } else {
            if (val.userType() == QMetaType::QImage || val.userType() == QMetaType::QPixmap) {
                charFormat.setBackground(qvariant_cast<QPixmap>(val));
            } else if (val.userType() == QMetaType::QByteArray) {
                QPixmap pm;
                if (pm.loadFromData(val.toByteArray())) {
                    charFormat.setBackground(pm);
                }
            }
        }
    }
    if (!url.isEmpty())
        charFormat.setProperty(QTextFormat::BackgroundImageUrl, url);
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
//  -----------------------------------------------------------------------

//  QTextHtmlParserNode::QTextHtmlParserNode()
extern "C" Q_DECL_EXPORT
QTextHtmlParserNode *ritual_ZN19QTextHtmlParserNodeC1Ev() {
  return new QTextHtmlParserNode();
}

//  bool QTextHtmlParserNode::isListStart() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QTextHtmlParserNode11isListStartEv(
    const QTextHtmlParserNode *self) {
  return self->isListStart();
}

//  bool QTextHtmlParserNode::isTableCell() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QTextHtmlParserNode11isTableCellEv(
    const QTextHtmlParserNode *self) {
  return self->isTableCell();
}

//  bool QTextHtmlParserNode::isBlock() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QTextHtmlParserNode7isBlockEv(
    const QTextHtmlParserNode *self) {
  return self->isBlock();
}

//  bool QTextHtmlParserNode::isNotSelfNesting() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QTextHtmlParserNode16isNotSelfNestingEv(
    const QTextHtmlParserNode *self) {
  return self->isNotSelfNesting();
}

//  bool QTextHtmlParserNode::allowedInContext(int parentId) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QTextHtmlParserNode16allowedInContextEi(
    const QTextHtmlParserNode *self,
    int parentId) {
  return self->allowedInContext(parentId);
}

//  bool QTextHtmlParserNode::mayNotHaveChildren() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QTextHtmlParserNode18mayNotHaveChildrenEv(
    const QTextHtmlParserNode *self) {
  return self->mayNotHaveChildren();
}

//  int QTextHtmlParserNode::uncollapsedMargin(int mar) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QTextHtmlParserNode17uncollapsedMarginEi(
    const QTextHtmlParserNode *self,
    int mar) {
  return self->uncollapsedMargin(mar);
}

#if !defined(QT_NO_TEXTHTMLPARSER)
//  bool QTextHtmlParserNode::isNestedList(const QTextHtmlParser *parser)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QTextHtmlParserNode12isNestedListEPK15QTextHtmlParser(
    const QTextHtmlParserNode *self,
    const QTextHtmlParser *parser) {
  return self->isNestedList(parser);
}
#endif  // !defined(QT_NO_TEXTHTMLPARSER)

#if !defined(QT_NO_TEXTHTMLPARSER)
//  void QTextHtmlParserNode::applyForegroundImage(qint64 cacheKey, const
//      QTextDocument *resourceProvider)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTextHtmlParserNode20applyForegroundImageExPK13QTextDocument(
    QTextHtmlParserNode *self,
    qint64 cacheKey,
    const QTextDocument *resourceProvider) {
  self->applyForegroundImage(cacheKey, resourceProvider);
}
#endif  // !defined(QT_NO_TEXTHTMLPARSER)

#if !defined(QT_NO_TEXTHTMLPARSER)
//  void QTextHtmlParserNode::applyBackgroundImage(const QString &url, const
//      QTextDocument *resourceProvider)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTextHtmlParserNode20applyBackgroundImageERK7QStringPK13QTextDocument(
    QTextHtmlParserNode *self,
    const QString *url,
    const QTextDocument *resourceProvider) {
  self->applyBackgroundImage(*url, resourceProvider);
}
#endif  // !defined(QT_NO_TEXTHTMLPARSER)

#if !defined(QT_NO_TEXTHTMLPARSER)
//  bool QTextHtmlParserNode::hasOnlyWhitespace() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QTextHtmlParserNode17hasOnlyWhitespaceEv(
    const QTextHtmlParserNode *self) {
  return self->hasOnlyWhitespace();
}
#endif  // !defined(QT_NO_TEXTHTMLPARSER)

//  QTextHtmlParserNode::~QTextHtmlParserNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTextHtmlParserNodeD1Ev(QTextHtmlParserNode *self) {
  delete self;
}

#endif  // !defined(QT_NO_TEXTHTMLPARSER)
