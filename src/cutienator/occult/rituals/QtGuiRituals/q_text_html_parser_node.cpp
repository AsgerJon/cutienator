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

using namespace Qt::StringLiterals;

//  from src/gui/text/qtexthtmlparser.cpp, line 1136, as local:qtexthtmlparser.cpp:toQTextFrameFormat
#if !defined(QT_NO_TEXTHTMLPARSER)
#if !defined(QT_NO_CSSPARSER)
static QTextFrameFormat::BorderStyle toQTextFrameFormat(QCss::BorderStyle cssStyle)
{
    switch (cssStyle) {
    case QCss::BorderStyle::BorderStyle_Dotted:
        return QTextFrameFormat::BorderStyle::BorderStyle_Dotted;
    case QCss::BorderStyle::BorderStyle_Dashed:
        return QTextFrameFormat::BorderStyle::BorderStyle_Dashed;
    case QCss::BorderStyle::BorderStyle_Solid:
        return QTextFrameFormat::BorderStyle::BorderStyle_Solid;
    case QCss::BorderStyle::BorderStyle_Double:
        return QTextFrameFormat::BorderStyle::BorderStyle_Double;
    case QCss::BorderStyle::BorderStyle_DotDash:
        return QTextFrameFormat::BorderStyle::BorderStyle_DotDash;
    case QCss::BorderStyle::BorderStyle_DotDotDash:
        return QTextFrameFormat::BorderStyle::BorderStyle_DotDotDash;
    case QCss::BorderStyle::BorderStyle_Groove:
        return QTextFrameFormat::BorderStyle::BorderStyle_Groove;
    case QCss::BorderStyle::BorderStyle_Ridge:
        return QTextFrameFormat::BorderStyle::BorderStyle_Ridge;
    case QCss::BorderStyle::BorderStyle_Inset:
        return QTextFrameFormat::BorderStyle::BorderStyle_Inset;
    case QCss::BorderStyle::BorderStyle_Outset:
        return QTextFrameFormat::BorderStyle::BorderStyle_Outset;
    case QCss::BorderStyle::BorderStyle_Unknown:
    case QCss::BorderStyle::BorderStyle_None:
    case QCss::BorderStyle::BorderStyle_Native:
        return QTextFrameFormat::BorderStyle::BorderStyle_None;
    // Intentionally no "default" to allow a compiler warning when extending the enum
    // without updating this here. clang gives such a warning.
    }
    // Must not happen, intentionally trigger undefined behavior which sanitizers will detect.
    // Having all cases covered in switch is not sufficient:
    // MSVC would warn when there is no "default".
    return static_cast<QTextFrameFormat::BorderStyle>(-1);
}
#endif  // !defined(QT_NO_CSSPARSER)
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

//  from src/gui/text/qtexthtmlparser.cpp, line 978, as _ZN19QTextHtmlParserNode20initializePropertiesEPKS_PK15QTextHtmlParser
#if !defined(QT_NO_TEXTHTMLPARSER)
inline void QTextHtmlParserNode::initializeProperties(const QTextHtmlParserNode *parent, const QTextHtmlParser *parser)
{
    // inherit properties from parent element
    charFormat = parent->charFormat;

    if (id == Html_html)
        blockFormat.setLayoutDirection(Qt::LeftToRight); // HTML default
    else if (parent->blockFormat.hasProperty(QTextFormat::LayoutDirection))
        blockFormat.setLayoutDirection(parent->blockFormat.layoutDirection());

    if (parent->displayMode == QTextHtmlElement::DisplayNone)
        displayMode = QTextHtmlElement::DisplayNone;

    if (parent->id != Html_table || id == Html_caption) {
        if (parent->blockFormat.hasProperty(QTextFormat::BlockAlignment))
            blockFormat.setAlignment(parent->blockFormat.alignment());
        else
            blockFormat.clearProperty(QTextFormat::BlockAlignment);
    }
    // we don't paint per-row background colors, yet. so as an
    // exception inherit the background color here
    // we also inherit the background between inline elements
    // we also inherit from non-body block elements since we merge them together
    if ((parent->id != Html_tr || !isTableCell())
        && (displayMode != QTextHtmlElement::DisplayInline || parent->displayMode != QTextHtmlElement::DisplayInline)
        && (parent->id == Html_body || displayMode != QTextHtmlElement::DisplayBlock || parent->displayMode != QTextHtmlElement::DisplayBlock)
       ) {
        charFormat.clearProperty(QTextFormat::BackgroundBrush);
    }

    listStyle = parent->listStyle;
    // makes no sense to inherit that property, a named anchor is a single point
    // in the document, which is set by the DocumentFragment
    charFormat.clearProperty(QTextFormat::AnchorName);
    wsm = parent->wsm;

    // initialize remaining properties
    margin[QTextHtmlParser::MarginLeft] = 0;
    margin[QTextHtmlParser::MarginRight] = 0;
    margin[QTextHtmlParser::MarginTop] = 0;
    margin[QTextHtmlParser::MarginBottom] = 0;
    cssFloat = QTextFrameFormat::InFlow;

    for (int i = 0; i < 4; ++i)
        padding[i] = -1;

    // set element specific attributes
    switch (id) {
        case Html_a:
            for (int i = 0; i < attributes.size(); i += 2) {
                const QString key = attributes.at(i);
                if (key.compare("href"_L1, Qt::CaseInsensitive) == 0
                    && !attributes.at(i + 1).isEmpty()) {
                    hasHref = true;
                }
            }
            charFormat.setAnchor(true);
            break;
        case Html_big:
            charFormat.setProperty(QTextFormat::FontSizeAdjustment, int(1));
            break;
        case Html_small:
            charFormat.setProperty(QTextFormat::FontSizeAdjustment, int(-1));
            break;
        case Html_h1:
            charFormat.setProperty(QTextFormat::FontSizeAdjustment, int(3));
            margin[QTextHtmlParser::MarginTop] = 18;
            margin[QTextHtmlParser::MarginBottom] = 12;
            break;
        case Html_h2:
            charFormat.setProperty(QTextFormat::FontSizeAdjustment, int(2));
            margin[QTextHtmlParser::MarginTop] = 16;
            margin[QTextHtmlParser::MarginBottom] = 12;
            break;
        case Html_h3:
            charFormat.setProperty(QTextFormat::FontSizeAdjustment, int(1));
            margin[QTextHtmlParser::MarginTop] = 14;
            margin[QTextHtmlParser::MarginBottom] = 12;
            break;
        case Html_h4:
            charFormat.setProperty(QTextFormat::FontSizeAdjustment, int(0));
            margin[QTextHtmlParser::MarginTop] = 12;
            margin[QTextHtmlParser::MarginBottom] = 12;
            break;
        case Html_h5:
            charFormat.setProperty(QTextFormat::FontSizeAdjustment, int(-1));
            margin[QTextHtmlParser::MarginTop] = 12;
            margin[QTextHtmlParser::MarginBottom] = 4;
            break;
        case Html_p:
            margin[QTextHtmlParser::MarginTop] = 12;
            margin[QTextHtmlParser::MarginBottom] = 12;
            break;
        case Html_ul:
            // nested lists don't have margins, except for the toplevel one
            if (!isNestedList(parser)) {
                margin[QTextHtmlParser::MarginTop] = 12;
                margin[QTextHtmlParser::MarginBottom] = 12;
            }
            // no left margin as we use indenting instead
            break;
        case Html_ol:
            // nested lists don't have margins, except for the toplevel one
            if (!isNestedList(parser)) {
                margin[QTextHtmlParser::MarginTop] = 12;
                margin[QTextHtmlParser::MarginBottom] = 12;
            }
            // no left margin as we use indenting instead
            break;
        case Html_br:
            text = QChar(QChar::LineSeparator);
            break;
        case Html_pre:
            margin[QTextHtmlParser::MarginTop] = 12;
            margin[QTextHtmlParser::MarginBottom] = 12;
            break;
        case Html_blockquote:
            margin[QTextHtmlParser::MarginTop] = 12;
            margin[QTextHtmlParser::MarginBottom] = 12;
            margin[QTextHtmlParser::MarginLeft] = 40;
            margin[QTextHtmlParser::MarginRight] = 40;
            blockFormat.setProperty(QTextFormat::BlockQuoteLevel, 1);
            break;
        case Html_dl:
            margin[QTextHtmlParser::MarginTop] = 8;
            margin[QTextHtmlParser::MarginBottom] = 8;
            break;
        case Html_dd:
            margin[QTextHtmlParser::MarginLeft] = 30;
            break;
        default: break;
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

//  from src/gui/text/qtexthtmlparser.cpp, line 1636, as _ZN19QTextHtmlParserNode19parseStyleAttributeERK7QStringPK13QTextDocument
#if !defined(QT_NO_TEXTHTMLPARSER)
#if !defined(QT_NO_CSSPARSER)
inline void QTextHtmlParserNode::parseStyleAttribute(const QString &value, const QTextDocument *resourceProvider)
{
    const QString css = "* {"_L1 + value + u'}';
    QCss::Parser parser(css);
    QCss::StyleSheet sheet;
    parser.parse(&sheet, Qt::CaseInsensitive);
    if (sheet.styleRules.size() != 1) return;
    applyCssDeclarations(sheet.styleRules.at(0).declarations, resourceProvider);
}
#endif  // !defined(QT_NO_CSSPARSER)
#endif  // !defined(QT_NO_TEXTHTMLPARSER)

//  from src/gui/text/qtexthtmlparser.cpp, line 1172, as _ZN19QTextHtmlParserNode20applyCssDeclarationsERK5QListIN4QCss11DeclarationEEPK13QTextDocument
#if !defined(QT_NO_TEXTHTMLPARSER)
#if !defined(QT_NO_CSSPARSER)
inline void QTextHtmlParserNode::applyCssDeclarations(const QList<QCss::Declaration> &declarations, const QTextDocument *resourceProvider)
{
    QCss::ValueExtractor extractor(declarations);
    extractor.extractBox(margin, padding);

    auto getBorderValues = [&extractor](qreal *borderWidth, QBrush *borderBrush, QTextFrameFormat::BorderStyle *borderStyles) {
        QCss::BorderStyle cssStyles[4];
        int cssBorder[4];
        QSize cssRadii[4]; // unused
        for (int i = 0; i < 4; ++i) {
            cssStyles[i] = QCss::BorderStyle_None;
            cssBorder[i] = 0;
        }
        // this will parse (and cache) "border-width" as a list so the
        // QCss::BorderWidth parsing below which expects a single value
        // will not work as expected - which in this case does not matter
        // because tableBorder is not relevant for cells.
        bool hit = extractor.extractBorder(cssBorder, borderBrush, cssStyles, cssRadii);
        for (int i = 0; i < 4; ++i) {
            borderStyles[i] = toQTextFrameFormat(cssStyles[i]);
            borderWidth[i] = static_cast<qreal>(cssBorder[i]);
        }
        return hit;
    };

    if (id == Html_td || id == Html_th)
        getBorderValues(tableCellBorder, tableCellBorderBrush, tableCellBorderStyle);

    for (int i = 0; i < declarations.size(); ++i) {
        const QCss::Declaration &decl = declarations.at(i);
        if (decl.d->values.isEmpty()) continue;

        QCss::KnownValue identifier = QCss::UnknownValue;
        if (decl.d->values.constFirst().type == QCss::Value::KnownIdentifier)
            identifier = static_cast<QCss::KnownValue>(decl.d->values.constFirst().variant.toInt());

        switch (decl.d->propertyId) {
        case QCss::BorderColor: {
            QBrush bordersBrush[4];
            decl.brushValues(bordersBrush);
            if (bordersBrush[0].color().isValid())
                borderBrush = bordersBrush[0];
            break;
        }
        case QCss::BorderStyles:
            if (decl.styleValue() != QCss::BorderStyle_Unknown && decl.styleValue() != QCss::BorderStyle_Native)
                borderStyle = static_cast<QTextFrameFormat::BorderStyle>(decl.styleValue() - 1);
            break;
        case QCss::BorderWidth: {
            int borders[4];
            extractor.lengthValues(decl, borders);
            tableBorder = borders[0];
            }
            break;
        case QCss::Border: {
            qreal tblBorder[4];
            QBrush tblBorderBrush[4];
            QTextFrameFormat::BorderStyle tblBorderStyle[4];
            if (getBorderValues(tblBorder, tblBorderBrush, tblBorderStyle)) {
                tableBorder = tblBorder[0];
                if (tblBorderBrush[0].color().isValid())
                    borderBrush = tblBorderBrush[0];
                if (tblBorderStyle[0] != static_cast<QTextFrameFormat::BorderStyle>(-1))
                    borderStyle = tblBorderStyle[0];
            }
        }
        break;
        case QCss::BorderCollapse:
            borderCollapse = decl.borderCollapseValue();
            break;
        case QCss::Color: charFormat.setForeground(decl.colorValue()); break;
        case QCss::Float:
            cssFloat = QTextFrameFormat::InFlow;
            switch (identifier) {
            case QCss::Value_Left: cssFloat = QTextFrameFormat::FloatLeft; break;
            case QCss::Value_Right: cssFloat = QTextFrameFormat::FloatRight; break;
            default: break;
            }
            break;
        case QCss::QtBlockIndent:
            blockFormat.setIndent(decl.d->values.constFirst().variant.toInt());
            break;
        case QCss::QtLineHeightType: {
            QString lineHeightTypeName = decl.d->values.constFirst().variant.toString();
            QTextBlockFormat::LineHeightTypes lineHeightType;
            if (lineHeightTypeName.compare("proportional"_L1, Qt::CaseInsensitive) == 0)
                lineHeightType = QTextBlockFormat::ProportionalHeight;
            else if (lineHeightTypeName.compare("fixed"_L1, Qt::CaseInsensitive) == 0)
                lineHeightType = QTextBlockFormat::FixedHeight;
            else if (lineHeightTypeName.compare("minimum"_L1, Qt::CaseInsensitive) == 0)
                lineHeightType = QTextBlockFormat::MinimumHeight;
            else if (lineHeightTypeName.compare("line-distance"_L1, Qt::CaseInsensitive) == 0)
                lineHeightType = QTextBlockFormat::LineDistanceHeight;
            else
                lineHeightType = QTextBlockFormat::SingleHeight;

            if (hasLineHeightMultiplier) {
                qreal lineHeight = blockFormat.lineHeight() / 100.0;
                blockFormat.setProperty(QTextBlockFormat::LineHeight, lineHeight);
            }

            blockFormat.setProperty(QTextBlockFormat::LineHeightType, lineHeightType);
            hasOwnLineHeightType = true;
        }
        break;
        case QCss::LineHeight: {
            qreal lineHeight;
            QTextBlockFormat::LineHeightTypes lineHeightType;
            if (decl.realValue(&lineHeight, "px")) {
                lineHeightType = QTextBlockFormat::MinimumHeight;
            } else {
                bool ok;
                QCss::Value cssValue = decl.d->values.constFirst();
                QString value = cssValue.toString();
                lineHeight = value.toDouble(&ok);
                if (ok) {
                    if (!hasOwnLineHeightType && cssValue.type == QCss::Value::Number) {
                        lineHeight *= 100.0;
                        hasLineHeightMultiplier = true;
                    }
                    lineHeightType = QTextBlockFormat::ProportionalHeight;
                } else {
                    lineHeight = 0.0;
                    lineHeightType = QTextBlockFormat::SingleHeight;
                }
            }

            // Only override line height type if specified in same node
            if (hasOwnLineHeightType)
                lineHeightType = QTextBlockFormat::LineHeightTypes(blockFormat.lineHeightType());

            blockFormat.setLineHeight(lineHeight, lineHeightType);
            break;
        }
        case QCss::TextIndent: {
            qreal indent = 0;
            if (decl.realValue(&indent, "px"))
                blockFormat.setTextIndent(indent);
            break; }
        case QCss::QtListIndent:
            if (decl.intValue(&cssListIndent))
                hasCssListIndent = true;
            break;
        case QCss::QtParagraphType:
            if (decl.d->values.constFirst().variant.toString().compare("empty"_L1, Qt::CaseInsensitive) == 0)
                isEmptyParagraph = true;
            break;
        case QCss::QtTableType:
            if (decl.d->values.constFirst().variant.toString().compare("frame"_L1, Qt::CaseInsensitive) == 0)
                isTextFrame = true;
            else if (decl.d->values.constFirst().variant.toString().compare("root"_L1, Qt::CaseInsensitive) == 0) {
                isTextFrame = true;
                isRootFrame = true;
            }
            break;
        case QCss::QtUserState:
            userState = decl.d->values.constFirst().variant.toInt();
            break;
        case QCss::Whitespace:
            switch (identifier) {
            case QCss::Value_Normal: wsm = QTextHtmlParserNode::WhiteSpaceNormal; break;
            case QCss::Value_Pre: wsm = QTextHtmlParserNode::WhiteSpacePre; break;
            case QCss::Value_NoWrap: wsm = QTextHtmlParserNode::WhiteSpaceNoWrap; break;
            case QCss::Value_PreWrap: wsm = QTextHtmlParserNode::WhiteSpacePreWrap; break;
            case QCss::Value_PreLine: wsm = QTextHtmlParserNode::WhiteSpacePreLine; break;
            default: break;
            }
            break;
        case QCss::VerticalAlignment:
            switch (identifier) {
            case QCss::Value_Sub: charFormat.setVerticalAlignment(QTextCharFormat::AlignSubScript); break;
            case QCss::Value_Super: charFormat.setVerticalAlignment(QTextCharFormat::AlignSuperScript); break;
            case QCss::Value_Middle: charFormat.setVerticalAlignment(QTextCharFormat::AlignMiddle); break;
            case QCss::Value_Top: charFormat.setVerticalAlignment(QTextCharFormat::AlignTop); break;
            case QCss::Value_Bottom: charFormat.setVerticalAlignment(QTextCharFormat::AlignBottom); break;
            default: charFormat.setVerticalAlignment(QTextCharFormat::AlignNormal); break;
            }
            break;
        case QCss::PageBreakBefore:
            switch (identifier) {
            case QCss::Value_Always: blockFormat.setPageBreakPolicy(blockFormat.pageBreakPolicy() | QTextFormat::PageBreak_AlwaysBefore); break;
            case QCss::Value_Auto: blockFormat.setPageBreakPolicy(blockFormat.pageBreakPolicy() & ~QTextFormat::PageBreak_AlwaysBefore); break;
            default: break;
            }
            break;
        case QCss::PageBreakAfter:
            switch (identifier) {
            case QCss::Value_Always: blockFormat.setPageBreakPolicy(blockFormat.pageBreakPolicy() | QTextFormat::PageBreak_AlwaysAfter); break;
            case QCss::Value_Auto: blockFormat.setPageBreakPolicy(blockFormat.pageBreakPolicy() & ~QTextFormat::PageBreak_AlwaysAfter); break;
            default: break;
            }
            break;
        case QCss::TextUnderlineStyle:
            switch (identifier) {
            case QCss::Value_None: charFormat.setUnderlineStyle(QTextCharFormat::NoUnderline); break;
            case QCss::Value_Solid: charFormat.setUnderlineStyle(QTextCharFormat::SingleUnderline); break;
            case QCss::Value_Dashed: charFormat.setUnderlineStyle(QTextCharFormat::DashUnderline); break;
            case QCss::Value_Dotted: charFormat.setUnderlineStyle(QTextCharFormat::DotLine); break;
            case QCss::Value_DotDash: charFormat.setUnderlineStyle(QTextCharFormat::DashDotLine); break;
            case QCss::Value_DotDotDash: charFormat.setUnderlineStyle(QTextCharFormat::DashDotDotLine); break;
            case QCss::Value_Wave: charFormat.setUnderlineStyle(QTextCharFormat::WaveUnderline); break;
            default: break;
            }
            break;
        case QCss::TextDecorationColor: charFormat.setUnderlineColor(decl.colorValue()); break;
        case QCss::ListStyleType:
        case QCss::ListStyle:
            setListStyle(decl.d->values);
            break;
        case QCss::QtListNumberPrefix:
            textListNumberPrefix = decl.d->values.constFirst().variant.toString();
            break;
        case QCss::QtListNumberSuffix:
            textListNumberSuffix = decl.d->values.constFirst().variant.toString();
            break;
        case QCss::TextAlignment:
            switch (identifier) {
            case QCss::Value_Left: blockFormat.setAlignment(Qt::AlignLeft); break;
            case QCss::Value_Center: blockFormat.setAlignment(Qt::AlignCenter); break;
            case QCss::Value_Right: blockFormat.setAlignment(Qt::AlignRight); break;
            default: break;
            }
            break;

        case QCss::QtForegroundTextureCacheKey:
        {
            if (resourceProvider != nullptr && QTextDocumentPrivate::get(resourceProvider) != nullptr) {
                bool ok;
                qint64 searchKey = decl.d->values.constFirst().variant.toLongLong(&ok);
                if (ok)
                    applyForegroundImage(searchKey, resourceProvider);
            }
            break;
        }
        case QCss::QtStrokeColor:
        {
            QPen pen = charFormat.textOutline();
            pen.setStyle(Qt::SolidLine);
            pen.setColor(decl.colorValue());
            charFormat.setTextOutline(pen);
            break;
        }
        case QCss::QtStrokeWidth:
        {
            qreal width;
            if (decl.realValue(&width, "px")) {
                QPen pen = charFormat.textOutline();
                pen.setWidthF(width);
                charFormat.setTextOutline(pen);
            }
            break;
        }
        case QCss::QtStrokeLineCap:
        {
            QPen pen = charFormat.textOutline();
            switch (identifier) {
            case QCss::Value_SquareCap: pen.setCapStyle(Qt::SquareCap); break;
            case QCss::Value_FlatCap: pen.setCapStyle(Qt::FlatCap); break;
            case QCss::Value_RoundCap: pen.setCapStyle(Qt::RoundCap); break;
            default: break;
            }
            charFormat.setTextOutline(pen);
            break;
        }
        case QCss::QtStrokeLineJoin:
        {
            QPen pen = charFormat.textOutline();
            switch (identifier) {
            case QCss::Value_MiterJoin: pen.setJoinStyle(Qt::MiterJoin); break;
            case QCss::Value_BevelJoin: pen.setJoinStyle(Qt::BevelJoin); break;
            case QCss::Value_RoundJoin: pen.setJoinStyle(Qt::RoundJoin); break;
            case QCss::Value_SvgMiterJoin: pen.setJoinStyle(Qt::SvgMiterJoin); break;
            default: break;
            }
            charFormat.setTextOutline(pen);
            break;
        }
        case QCss::QtStrokeMiterLimit:
        {
            qreal miterLimit;
            if (decl.realValue(&miterLimit)) {
                QPen pen = charFormat.textOutline();
                pen.setMiterLimit(miterLimit);
                charFormat.setTextOutline(pen);
            }
            break;
        }
        case QCss::QtStrokeDashArray:
        {
            QList<qreal> dashes = decl.dashArray();
            if (!dashes.empty()) {
                QPen pen = charFormat.textOutline();
                pen.setDashPattern(dashes);
                charFormat.setTextOutline(pen);
            }
            break;
        }
        case QCss::QtStrokeDashOffset:
        {
            qreal dashOffset;
            if (decl.realValue(&dashOffset)) {
                QPen pen = charFormat.textOutline();
                pen.setDashOffset(dashOffset);
                charFormat.setTextOutline(pen);
            }
            break;
        }
        case QCss::QtForeground:
        {
            QBrush brush = decl.brushValue();
            charFormat.setForeground(brush);
            break;
        }
        case QCss::MaximumWidth:
            if (id == Html_img) {
                auto imageFormat = charFormat.toImageFormat();
                imageFormat.setMaximumWidth(extractor.textLength(decl));
                charFormat = imageFormat;
            }
            break;
        default: break;
        }
    }

    QFont f;
    int adjustment = -255;
    extractor.extractFont(&f, &adjustment);
    if (f.pixelSize() > INT32_MAX / 2)
        f.setPixelSize(INT32_MAX / 2);   // avoid even more extreme values
    charFormat.setFont(f, QTextCharFormat::FontPropertiesSpecifiedOnly);

    if (adjustment >= -1)
        charFormat.setProperty(QTextFormat::FontSizeAdjustment, adjustment);

    {
        Qt::Alignment ignoredAlignment;
        QCss::Repeat ignoredRepeat;
        QString bgImage;
        QBrush bgBrush;
        QCss::Origin ignoredOrigin, ignoredClip;
        QCss::Attachment ignoredAttachment;
        extractor.extractBackground(&bgBrush, &bgImage, &ignoredRepeat, &ignoredAlignment,
                                    &ignoredOrigin, &ignoredAttachment, &ignoredClip);

        if (!bgImage.isEmpty() && resourceProvider) {
            applyBackgroundImage(bgImage, resourceProvider);
        } else if (bgBrush.style() != Qt::NoBrush) {
            charFormat.setBackground(bgBrush);
            if (id == Html_hr)
                blockFormat.setProperty(QTextFormat::BackgroundBrush, bgBrush);
        }
    }
}
#endif  // !defined(QT_NO_CSSPARSER)
#endif  // !defined(QT_NO_TEXTHTMLPARSER)

//  from src/gui/text/qtexthtmlparser.cpp, line 1113, as _ZN19QTextHtmlParserNode12setListStyleERK5QListIN4QCss5ValueEE
#if !defined(QT_NO_TEXTHTMLPARSER)
#if !defined(QT_NO_CSSPARSER)
inline void QTextHtmlParserNode::setListStyle(const QList<QCss::Value> &cssValues)
{
    for (int i = 0; i < cssValues.size(); ++i) {
        if (cssValues.at(i).type == QCss::Value::KnownIdentifier) {
            switch (static_cast<QCss::KnownValue>(cssValues.at(i).variant.toInt())) {
                case QCss::Value_None: hasOwnListStyle = true; listStyle = QTextListFormat::ListStyleUndefined; break;
                case QCss::Value_Disc: hasOwnListStyle = true; listStyle = QTextListFormat::ListDisc; break;
                case QCss::Value_Square: hasOwnListStyle = true; listStyle = QTextListFormat::ListSquare; break;
                case QCss::Value_Circle: hasOwnListStyle = true; listStyle = QTextListFormat::ListCircle; break;
                case QCss::Value_Decimal: hasOwnListStyle = true; listStyle = QTextListFormat::ListDecimal; break;
                case QCss::Value_LowerAlpha: hasOwnListStyle = true; listStyle = QTextListFormat::ListLowerAlpha; break;
                case QCss::Value_UpperAlpha: hasOwnListStyle = true; listStyle = QTextListFormat::ListUpperAlpha; break;
                case QCss::Value_LowerRoman: hasOwnListStyle = true; listStyle = QTextListFormat::ListLowerRoman; break;
                case QCss::Value_UpperRoman: hasOwnListStyle = true; listStyle = QTextListFormat::ListUpperRoman; break;
                default: break;
            }
        }
    }
    // allow individual list items to override the style
    if (id == Html_li && hasOwnListStyle)
        blockFormat.setProperty(QTextFormat::ListStyle, listStyle);
}
#endif  // !defined(QT_NO_CSSPARSER)
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

#if !defined(QT_NO_TEXTHTMLPARSER)
//  void QTextHtmlParserNode::initializeProperties(const QTextHtmlParserNode
//      *parent, const QTextHtmlParser *parser)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTextHtmlParserNode20initializePropertiesEPKS_PK15QTextHtmlParser(
    QTextHtmlParserNode *self,
    const QTextHtmlParserNode *parent,
    const QTextHtmlParser *parser) {
  self->initializeProperties(parent, parser);
}
#endif  // !defined(QT_NO_TEXTHTMLPARSER)

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
#if !defined(QT_NO_CSSPARSER)
//  void QTextHtmlParserNode::parseStyleAttribute(const QString &value, const
//      QTextDocument *resourceProvider)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTextHtmlParserNode19parseStyleAttributeERK7QStringPK13QTextDocument(
    QTextHtmlParserNode *self,
    const QString *value,
    const QTextDocument *resourceProvider) {
  self->parseStyleAttribute(*value, resourceProvider);
}
#endif  // !defined(QT_NO_CSSPARSER)
#endif  // !defined(QT_NO_TEXTHTMLPARSER)

#if QT_CONFIG(cssparser)
#if !defined(QT_NO_TEXTHTMLPARSER)
#if !defined(QT_NO_CSSPARSER)
//  void QTextHtmlParserNode::applyCssDeclarations(const
//      QList<QCss::Declaration> &declarations, const QTextDocument
//      *resourceProvider)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTextHtmlParserNode20applyCssDeclarationsERK5QListIN4QCss11DeclarationEEPK13QTextDocument(
    QTextHtmlParserNode *self,
    const QList<QCss::Declaration> *declarations,
    const QTextDocument *resourceProvider) {
  self->applyCssDeclarations(*declarations, resourceProvider);
}
#endif  // !defined(QT_NO_CSSPARSER)
#endif  // !defined(QT_NO_TEXTHTMLPARSER)
#endif  // QT_CONFIG(cssparser)

#if QT_CONFIG(cssparser)
#if !defined(QT_NO_TEXTHTMLPARSER)
#if !defined(QT_NO_CSSPARSER)
//  void QTextHtmlParserNode::setListStyle(const QList<QCss::Value>
//      &cssValues)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTextHtmlParserNode12setListStyleERK5QListIN4QCss5ValueEE(
    QTextHtmlParserNode *self,
    const QList<QCss::Value> *cssValues) {
  self->setListStyle(*cssValues);
}
#endif  // !defined(QT_NO_CSSPARSER)
#endif  // !defined(QT_NO_TEXTHTMLPARSER)
#endif  // QT_CONFIG(cssparser)

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
