//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qtextdocument_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtextdocument_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qtextobject.h>
#include <QtGui/qtextformat.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qtextdocument.h>
#include <QtGui/qtextformat.h>
#include <QtGui/private/qtextcursor_p.h>
#include <QtGui/private/qtextdocument_p.h>
#include <QtGui/private/qtextdocumentlayout_p.h>
#include <QtGui/qtextdocumentfragment.h>
#include <QtGui/private/qtextdocumentfragment_p.h>
#include <QtGui/qtexttable.h>
#include <QtGui/qtextlist.h>
#include <QtCore/qdebug.h>
#include <QtCore/qloggingcategory.h>
#if QT_CONFIG(regularexpression)
#include <QtCore/qregularexpression.h>
#endif
#include <QtCore/qvarlengtharray.h>
#include <QtCore/qthread.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/qmetaobject.h>
#include <QtGui/private/qtexthtmlparser_p.h>
#include <QtGui/qpainter.h>
#include <QtCore/qfile.h>
#include <QtCore/qfileinfo.h>
#include <QtCore/qdir.h>
#include <QtGui/private/qfont_p.h>
#include <QtCore/private/qdataurl_p.h>
#include <QtGui/private/qtextdocument_p.h>
#include <QtGui/private/qabstracttextdocumentlayout_p.h>
#include <QtGui/qpagedpaintdevice.h>
#include <QtGui/private/qpagedpaintdevice_p.h>
#if QT_CONFIG(textmarkdownreader)
#include <QtGui/private/qtextmarkdownimporter_p.h>
#endif
#if QT_CONFIG(textmarkdownwriter)
#include <QtGui/private/qtextmarkdownwriter_p.h>
#endif
#include <limits.h>
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

//  from src/gui/text/qtextdocument.cpp, line 2353, as local:qtextdocument.cpp:formatDifference
static QTextFormat formatDifference(const QTextFormat &from, const QTextFormat &to)
{
    QTextFormat diff = to;

    const QMap<int, QVariant> props = to.properties();
    for (QMap<int, QVariant>::ConstIterator it = props.begin(), end = props.end();
         it != end; ++it)
        if (it.value() == from.property(it.key()))
            diff.clearProperty(it.key());

    return diff;
}

//  from src/gui/text/qtextdocument.cpp, line 2366, as local:qtextdocument.cpp:colorValue
static QString colorValue(QColor color)
{
    QString result;

    if (color.alpha() == 255) {
        result = color.name();
    } else if (color.alpha()) {
        QString alphaValue = QString::number(color.alphaF(), 'f', 6);
        while (alphaValue.size() > 1 && alphaValue.at(alphaValue.size() - 1) == u'0')
            alphaValue.chop(1);
        if (alphaValue.at(alphaValue.size() - 1) == u'.')
            alphaValue.chop(1);
        result = QString::fromLatin1("rgba(%1,%2,%3,%4)").arg(color.red())
                                                         .arg(color.green())
                                                         .arg(color.blue())
                                                         .arg(alphaValue);
    } else {
        result = "transparent"_L1;
    }

    return result;
}

//  from src/gui/text/qtextdocument.cpp, line 2401, as local:qtextdocument.cpp:resolvedFontFamilies
static QStringList resolvedFontFamilies(const QTextCharFormat &format)
{
    return format.fontFamilies().toStringList();
}

//  from src/gui/text/qtextdocument.cpp, line 2867, as local:qtextdocument.cpp:richtextBorderStyleToHtmlBorderStyle
static QLatin1StringView richtextBorderStyleToHtmlBorderStyle(QTextFrameFormat::BorderStyle style)
{
    switch (style) {
    case QTextFrameFormat::BorderStyle_None:
        return "none"_L1;
    case QTextFrameFormat::BorderStyle_Dotted:
        return "dotted"_L1;
    case QTextFrameFormat::BorderStyle_Dashed:
        return "dashed"_L1;
    case QTextFrameFormat::BorderStyle_Solid:
        return "solid"_L1;
    case QTextFrameFormat::BorderStyle_Double:
        return "double"_L1;
    case QTextFrameFormat::BorderStyle_DotDash:
        return "dot-dash"_L1;
    case QTextFrameFormat::BorderStyle_DotDotDash:
        return "dot-dot-dash"_L1;
    case QTextFrameFormat::BorderStyle_Groove:
        return "groove"_L1;
    case QTextFrameFormat::BorderStyle_Ridge:
        return "ridge"_L1;
    case QTextFrameFormat::BorderStyle_Inset:
        return "inset"_L1;
    case QTextFrameFormat::BorderStyle_Outset:
        return "outset"_L1;
    default:
        Q_UNREACHABLE();
    };
    return ""_L1;
}

//  from src/gui/text/qtextdocument.cpp, line 3089, as local:qtextdocument.cpp:isOrderedList
static bool isOrderedList(int style)
{
    return style == QTextListFormat::ListDecimal || style == QTextListFormat::ListLowerAlpha
           || style == QTextListFormat::ListUpperAlpha
           || style == QTextListFormat::ListUpperRoman
           || style == QTextListFormat::ListLowerRoman
           ;
}

//  from src/gui/text/qtextdocument.cpp, line 3654, as _ZN17QTextHtmlExporter14emitFrameStyleERK16QTextFrameFormatNS_9FrameTypeE
inline void QTextHtmlExporter::emitFrameStyle(const QTextFrameFormat &format, FrameType frameType)
{
    const auto styleAttribute = " style=\""_L1;
    html += styleAttribute;
    const qsizetype originalHtmlLength = html.size();

    if (frameType == TextFrame)
        html += "-qt-table-type: frame;"_L1;
    else if (frameType == RootFrame)
        html += "-qt-table-type: root;"_L1;

    const QTextFrameFormat defaultFormat;

    emitFloatStyle(format.position(), OmitStyleTag);
    emitPageBreakPolicy(format.pageBreakPolicy());

    if (format.borderBrush() != defaultFormat.borderBrush()) {
        html += " border-color:"_L1;
        html += colorValue(format.borderBrush().color());
        html += u';';
    }

    if (format.borderStyle() != defaultFormat.borderStyle())
        emitBorderStyle(format.borderStyle());

    if (format.hasProperty(QTextFormat::FrameMargin)
        || format.hasProperty(QTextFormat::FrameLeftMargin)
        || format.hasProperty(QTextFormat::FrameRightMargin)
        || format.hasProperty(QTextFormat::FrameTopMargin)
        || format.hasProperty(QTextFormat::FrameBottomMargin))
        emitMargins(QString::number(format.topMargin()),
                    QString::number(format.bottomMargin()),
                    QString::number(format.leftMargin()),
                    QString::number(format.rightMargin()));

    if (format.property(QTextFormat::TableBorderCollapse).toBool())
        html += " border-collapse:collapse;"_L1;

    if (html.size() == originalHtmlLength) // nothing emitted?
        html.chop(styleAttribute.size());
    else
        html += u'\"';
}

//  from src/gui/text/qtextdocument.cpp, line 3098, as _ZN17QTextHtmlExporter19emitBlockAttributesERK10QTextBlock
inline void QTextHtmlExporter::emitBlockAttributes(const QTextBlock &block)
{
    QTextBlockFormat format = block.blockFormat();
    emitAlignment(format.alignment());

    // assume default to not bloat the html too much
    // html += " dir='ltr'"_L1;
    if (block.textDirection() == Qt::RightToLeft)
        html += " dir='rtl'"_L1;

    const auto style = " style=\""_L1;
    html += style;

    const bool emptyBlock = block.begin().atEnd();
    if (emptyBlock) {
        html += "-qt-paragraph-type:empty;"_L1;
    }

    emitMargins(QString::number(format.topMargin()),
                QString::number(format.bottomMargin()),
                QString::number(format.leftMargin()),
                QString::number(format.rightMargin()));

    html += " -qt-block-indent:"_L1;
    html += QString::number(format.indent());
    html += u';';

    html += " text-indent:"_L1;
    html += QString::number(format.textIndent());
    html += "px;"_L1;

    if (block.userState() != -1) {
        html += " -qt-user-state:"_L1;
        html += QString::number(block.userState());
        html += u';';
    }

    if (format.lineHeightType() != QTextBlockFormat::SingleHeight) {
        html += " line-height:"_L1
             + QString::number(format.lineHeight());
        switch (format.lineHeightType()) {
            case QTextBlockFormat::ProportionalHeight:
                html += "%;"_L1;
                break;
            case QTextBlockFormat::FixedHeight:
                html += "; -qt-line-height-type: fixed;"_L1;
                break;
            case QTextBlockFormat::MinimumHeight:
                html += "px;"_L1;
                break;
            case QTextBlockFormat::LineDistanceHeight:
                html += "; -qt-line-height-type: line-distance;"_L1;
                break;
            default:
                html += ";"_L1;
                break; // Should never reach here
        }
    }

    emitPageBreakPolicy(format.pageBreakPolicy());

    QTextCharFormat diff;
    if (emptyBlock) { // only print character properties when we don't expect them to be repeated by actual text in the parag
        const QTextCharFormat blockCharFmt = block.charFormat();
        diff = formatDifference(defaultCharFormat, blockCharFmt).toCharFormat();
    }

    diff.clearProperty(QTextFormat::BackgroundBrush);
    if (format.hasProperty(QTextFormat::BackgroundBrush)) {
        QBrush bg = format.background();
        if (bg.style() != Qt::NoBrush)
            diff.setProperty(QTextFormat::BackgroundBrush, format.property(QTextFormat::BackgroundBrush));
    }

    if (!diff.properties().isEmpty())
        emitCharFormatStyle(diff);

    html += u'"';

}

//  from src/gui/text/qtextdocument.cpp, line 2534, as _ZN17QTextHtmlExporter19emitCharFormatStyleERK15QTextCharFormat
inline bool QTextHtmlExporter::emitCharFormatStyle(const QTextCharFormat &format)
{
    bool attributesEmitted = false;

    {
        const QStringList families = resolvedFontFamilies(format);
        if (!families.isEmpty() && families != resolvedFontFamilies(defaultCharFormat)) {
            emitFontFamily(families);
            attributesEmitted = true;
        }
    }

    if (format.hasProperty(QTextFormat::FontPointSize)
        && format.fontPointSize() != defaultCharFormat.fontPointSize()) {
        html += " font-size:"_L1;
        html += QString::number(format.fontPointSize());
        html += "pt;"_L1;
        attributesEmitted = true;
    } else if (format.hasProperty(QTextFormat::FontSizeAdjustment)) {
        static const char sizeNameData[] =
            "small" "\0"
            "medium" "\0"
            "xx-large" ;
        static const quint8 sizeNameOffsets[] = {
            0,                                         // "small"
            sizeof("small"),                           // "medium"
            sizeof("small") + sizeof("medium") + 3,    // "large"    )
            sizeof("small") + sizeof("medium") + 1,    // "x-large"  )> compressed into "xx-large"
            sizeof("small") + sizeof("medium"),        // "xx-large" )
        };
        const char *name = nullptr;
        const int idx = format.intProperty(QTextFormat::FontSizeAdjustment) + 1;
        if (idx >= 0 && idx <= 4) {
            name = sizeNameData + sizeNameOffsets[idx];
        }
        if (name) {
            html += " font-size:"_L1;
            html += QLatin1StringView(name);
            html += u';';
            attributesEmitted = true;
        }
    } else if (format.hasProperty(QTextFormat::FontPixelSize)
               && format.property(QTextFormat::FontPixelSize)
                       != defaultCharFormat.property(QTextFormat::FontPixelSize)) {
        html += " font-size:"_L1;
        html += QString::number(format.intProperty(QTextFormat::FontPixelSize));
        html += "px;"_L1;
        attributesEmitted = true;
    }

    if (format.hasProperty(QTextFormat::FontWeight)
        && format.fontWeight() != defaultCharFormat.fontWeight()) {
        html += " font-weight:"_L1;
        html += QString::number(format.fontWeight());
        html += u';';
        attributesEmitted = true;
    }

    if (format.hasProperty(QTextFormat::FontItalic)
        && format.fontItalic() != defaultCharFormat.fontItalic()) {
        html += " font-style:"_L1;
        html += (format.fontItalic() ? "italic"_L1 : "normal"_L1);
        html += u';';
        attributesEmitted = true;
    }

    const auto decorationTag = " text-decoration:"_L1;
    html += decorationTag;
    bool hasDecoration = false;
    bool atLeastOneDecorationSet = false;

    if ((format.hasProperty(QTextFormat::FontUnderline) || format.hasProperty(QTextFormat::TextUnderlineStyle))
        && format.fontUnderline() != defaultCharFormat.fontUnderline()) {
        hasDecoration = true;
        if (format.fontUnderline()) {
            html += " underline"_L1;
            atLeastOneDecorationSet = true;
        }
    }

    if (format.hasProperty(QTextFormat::FontOverline)
        && format.fontOverline() != defaultCharFormat.fontOverline()) {
        hasDecoration = true;
        if (format.fontOverline()) {
            html += " overline"_L1;
            atLeastOneDecorationSet = true;
        }
    }

    if (format.hasProperty(QTextFormat::FontStrikeOut)
        && format.fontStrikeOut() != defaultCharFormat.fontStrikeOut()) {
        hasDecoration = true;
        if (format.fontStrikeOut()) {
            html += " line-through"_L1;
            atLeastOneDecorationSet = true;
        }
    }

    if (hasDecoration) {
        if (!atLeastOneDecorationSet)
            html += "none"_L1;
        html += u';';
        if (format.hasProperty(QTextFormat::TextUnderlineColor)) {
            html += " text-decoration-color:"_L1;
            html += colorValue(format.underlineColor());
            html += u';';
        }
        attributesEmitted = true;
    } else {
        html.chop(decorationTag.size());
    }

    if (format.foreground() != defaultCharFormat.foreground()
        && format.foreground().style() != Qt::NoBrush) {
        QBrush brush = format.foreground();
        if (brush.style() == Qt::TexturePattern) {
            const bool isPixmap = qHasPixmapTexture(brush);
            const qint64 cacheKey = isPixmap ? brush.texture().cacheKey() : brush.textureImage().cacheKey();

            html += " -qt-fg-texture-cachekey:"_L1;
            html += QString::number(cacheKey);
            html += ";"_L1;
        } else if (brush.style() == Qt::LinearGradientPattern
                   || brush.style() == Qt::RadialGradientPattern
                   || brush.style() == Qt::ConicalGradientPattern) {
            const QGradient *gradient = brush.gradient();
            if (gradient->type() == QGradient::LinearGradient) {
                const QLinearGradient *linearGradient = static_cast<const QLinearGradient *>(brush.gradient());

                html += " -qt-foreground: qlineargradient("_L1;
                html += "x1:"_L1 + QString::number(linearGradient->start().x()) + u',';
                html += "y1:"_L1 + QString::number(linearGradient->start().y()) + u',';
                html += "x2:"_L1 + QString::number(linearGradient->finalStop().x()) + u',';
                html += "y2:"_L1 + QString::number(linearGradient->finalStop().y()) + u',';
            } else if (gradient->type() == QGradient::RadialGradient) {
                const QRadialGradient *radialGradient = static_cast<const QRadialGradient *>(brush.gradient());

                html += " -qt-foreground: qradialgradient("_L1;
                html += "cx:"_L1 + QString::number(radialGradient->center().x()) + u',';
                html += "cy:"_L1 + QString::number(radialGradient->center().y()) + u',';
                html += "fx:"_L1 + QString::number(radialGradient->focalPoint().x()) + u',';
                html += "fy:"_L1 + QString::number(radialGradient->focalPoint().y()) + u',';
                html += "radius:"_L1 + QString::number(radialGradient->radius()) + u',';
            } else {
                const QConicalGradient *conicalGradient = static_cast<const QConicalGradient *>(brush.gradient());

                html += " -qt-foreground: qconicalgradient("_L1;
                html += "cx:"_L1 + QString::number(conicalGradient->center().x()) + u',';
                html += "cy:"_L1 + QString::number(conicalGradient->center().y()) + u',';
                html += "angle:"_L1 + QString::number(conicalGradient->angle()) + u',';
            }

            const QStringList coordinateModes = { "logical"_L1, "stretchtodevice"_L1, "objectbounding"_L1, "object"_L1 };
            html += "coordinatemode:"_L1;
            html += coordinateModes.at(int(gradient->coordinateMode()));
            html += u',';

            const QStringList spreads = { "pad"_L1, "reflect"_L1, "repeat"_L1 };
            html += "spread:"_L1;
            html += spreads.at(int(gradient->spread()));

            for (const QGradientStop &stop : gradient->stops()) {
                html += ",stop:"_L1;
                html += QString::number(stop.first);
                html += u' ';
                html += colorValue(stop.second);
            }

            html += ");"_L1;
        } else {
            html += " color:"_L1;
            html += colorValue(brush.color());
            html += u';';
        }
        attributesEmitted = true;
    }

    if (format.background() != defaultCharFormat.background()
        && format.background().style() == Qt::SolidPattern) {
        html += " background-color:"_L1;
        html += colorValue(format.background().color());
        html += u';';
        attributesEmitted = true;
    }

    if (format.verticalAlignment() != defaultCharFormat.verticalAlignment()
        && format.verticalAlignment() != QTextCharFormat::AlignNormal)
    {
        html += " vertical-align:"_L1;

        QTextCharFormat::VerticalAlignment valign = format.verticalAlignment();
        if (valign == QTextCharFormat::AlignSubScript)
            html += "sub"_L1;
        else if (valign == QTextCharFormat::AlignSuperScript)
            html += "super"_L1;
        else if (valign == QTextCharFormat::AlignMiddle)
            html += "middle"_L1;
        else if (valign == QTextCharFormat::AlignTop)
            html += "top"_L1;
        else if (valign == QTextCharFormat::AlignBottom)
            html += "bottom"_L1;

        html += u';';
        attributesEmitted = true;
    }

    if (format.fontCapitalization() != QFont::MixedCase) {
        const QFont::Capitalization caps = format.fontCapitalization();
        if (caps == QFont::AllUppercase)
            html += " text-transform:uppercase;"_L1;
        else if (caps == QFont::AllLowercase)
            html += " text-transform:lowercase;"_L1;
        else if (caps == QFont::SmallCaps)
            html += " font-variant:small-caps;"_L1;
        attributesEmitted = true;
    }

    if (format.fontWordSpacing() != 0.0) {
        html += " word-spacing:"_L1;
        html += QString::number(format.fontWordSpacing());
        html += "px;"_L1;
        attributesEmitted = true;
    }

    if (format.hasProperty(QTextFormat::TextOutline)) {
        QPen outlinePen = format.textOutline();
        html += " -qt-stroke-color:"_L1;
        html += colorValue(outlinePen.color());
        html += u';';

        html += " -qt-stroke-width:"_L1;
        html += QString::number(outlinePen.widthF());
        html += "px;"_L1;

        html += " -qt-stroke-linecap:"_L1;
        if (outlinePen.capStyle() == Qt::SquareCap)
            html += "squarecap;"_L1;
        else if (outlinePen.capStyle() == Qt::FlatCap)
            html += "flatcap;"_L1;
        else if (outlinePen.capStyle() == Qt::RoundCap)
            html += "roundcap;"_L1;

        html += " -qt-stroke-linejoin:"_L1;
        if (outlinePen.joinStyle() == Qt::MiterJoin)
            html += "miterjoin;"_L1;
        else if (outlinePen.joinStyle() == Qt::SvgMiterJoin)
            html += "svgmiterjoin;"_L1;
        else if (outlinePen.joinStyle() == Qt::BevelJoin)
            html += "beveljoin;"_L1;
        else if (outlinePen.joinStyle() == Qt::RoundJoin)
            html += "roundjoin;"_L1;

        if (outlinePen.joinStyle() == Qt::MiterJoin ||
            outlinePen.joinStyle() == Qt::SvgMiterJoin) {
            html += " -qt-stroke-miterlimit:"_L1;
            html += QString::number(outlinePen.miterLimit());
            html += u';';
        }

        if (outlinePen.style() == Qt::CustomDashLine && !outlinePen.dashPattern().empty()) {
            html += " -qt-stroke-dasharray:"_L1;
            QString dashArrayString;
            QList<qreal> dashes = outlinePen.dashPattern();

            for (int i = 0; i < dashes.length() - 1; i++) {
                qreal dash = dashes[i];
                dashArrayString += QString::number(dash) + u',';
            }

            dashArrayString += QString::number(dashes.last());
            html += dashArrayString;
            html += u';';

            html += " -qt-stroke-dashoffset:"_L1;
            html += QString::number(outlinePen.dashOffset());
            html += u';';
        }

        attributesEmitted = true;
    }

    return attributesEmitted;
}

//  from src/gui/text/qtextdocument.cpp, line 3426, as _ZN17QTextHtmlExporter23emitBackgroundAttributeERK11QTextFormat
inline void QTextHtmlExporter::emitBackgroundAttribute(const QTextFormat &format)
{
    if (format.hasProperty(QTextFormat::BackgroundImageUrl)) {
        QString url = format.property(QTextFormat::BackgroundImageUrl).toString();
        emitAttribute("background", url);
    } else {
        const QBrush &brush = format.background();
        if (brush.style() == Qt::SolidPattern) {
            emitAttribute("bgcolor", colorValue(brush.color()));
        } else if (brush.style() == Qt::TexturePattern) {
            const bool isPixmap = qHasPixmapTexture(brush);
            const qint64 cacheKey = isPixmap ? brush.texture().cacheKey() : brush.textureImage().cacheKey();

            const QString url = findUrlForImage(doc, cacheKey, isPixmap);

            if (!url.isEmpty())
                emitAttribute("background", url);
        }
    }
}

//  from src/gui/text/qtextdocument.cpp, line 3447, as _ZN17QTextHtmlExporter9emitTableEPK10QTextTable
inline void QTextHtmlExporter::emitTable(const QTextTable *table)
{
    QTextTableFormat format = table->format();

    html += "\n<table"_L1;

    if (format.hasProperty(QTextFormat::FrameBorder))
        emitAttribute("border", QString::number(format.border()));

    emitFrameStyle(format, TableFrame);

    emitAlignment(format.alignment());
    emitTextLength("width", format.width());

    if (format.hasProperty(QTextFormat::TableCellSpacing))
        emitAttribute("cellspacing", QString::number(format.cellSpacing()));
    if (format.hasProperty(QTextFormat::TableCellPadding))
        emitAttribute("cellpadding", QString::number(format.cellPadding()));

    emitBackgroundAttribute(format);

    html += u'>';

    const int rows = table->rows();
    const int columns = table->columns();

    QList<QTextLength> columnWidths = format.columnWidthConstraints();
    if (columnWidths.isEmpty()) {
        columnWidths.resize(columns);
        columnWidths.fill(QTextLength());
    }
    Q_ASSERT(columnWidths.size() == columns);

    QVarLengthArray<bool> widthEmittedForColumn(columns);
    for (int i = 0; i < columns; ++i)
        widthEmittedForColumn[i] = false;

    const int headerRowCount = qMin(format.headerRowCount(), rows);
    if (headerRowCount > 0)
        html += "<thead>"_L1;

    for (int row = 0; row < rows; ++row) {
        html += "\n<tr>"_L1;

        for (int col = 0; col < columns; ++col) {
            const QTextTableCell cell = table->cellAt(row, col);

            // for col/rowspans
            if (cell.row() != row)
                continue;

            if (cell.column() != col)
                continue;

            html += "\n<td"_L1;

            if (!widthEmittedForColumn[col] && cell.columnSpan() == 1) {
                emitTextLength("width", columnWidths.at(col));
                widthEmittedForColumn[col] = true;
            }

            if (cell.columnSpan() > 1)
                emitAttribute("colspan", QString::number(cell.columnSpan()));

            if (cell.rowSpan() > 1)
                emitAttribute("rowspan", QString::number(cell.rowSpan()));

            const QTextTableCellFormat cellFormat = cell.format().toTableCellFormat();
            emitBackgroundAttribute(cellFormat);

            if (!cellFormat.toolTip().isEmpty())
                emitAttribute("title", cellFormat.toolTip());

            QTextCharFormat oldDefaultCharFormat = defaultCharFormat;

            QTextCharFormat::VerticalAlignment valign = cellFormat.verticalAlignment();

            QString styleString;
            if (valign >= QTextCharFormat::AlignMiddle && valign <= QTextCharFormat::AlignBottom) {
                styleString += " vertical-align:"_L1;
                switch (valign) {
                case QTextCharFormat::AlignMiddle:
                    styleString += "middle"_L1;
                    break;
                case QTextCharFormat::AlignTop:
                    styleString += "top"_L1;
                    break;
                case QTextCharFormat::AlignBottom:
                    styleString += "bottom"_L1;
                    break;
                default:
                    break;
                }
                styleString += u';';

                QTextCharFormat temp;
                temp.setVerticalAlignment(valign);
                defaultCharFormat.merge(temp);
            }

            if (cellFormat.hasProperty(QTextFormat::TableCellLeftPadding))
                styleString += " padding-left:"_L1 + QString::number(cellFormat.leftPadding()) + u';';
            if (cellFormat.hasProperty(QTextFormat::TableCellRightPadding))
                styleString += " padding-right:"_L1 + QString::number(cellFormat.rightPadding()) + u';';
            if (cellFormat.hasProperty(QTextFormat::TableCellTopPadding))
                styleString += " padding-top:"_L1 + QString::number(cellFormat.topPadding()) + u';';
            if (cellFormat.hasProperty(QTextFormat::TableCellBottomPadding))
                styleString += " padding-bottom:"_L1 + QString::number(cellFormat.bottomPadding()) + u';';

            if (cellFormat.hasProperty(QTextFormat::TableCellTopBorder))
                styleString += " border-top:"_L1 + QString::number(cellFormat.topBorder()) + "px;"_L1;
            if (cellFormat.hasProperty(QTextFormat::TableCellRightBorder))
                styleString += " border-right:"_L1 + QString::number(cellFormat.rightBorder()) + "px;"_L1;
            if (cellFormat.hasProperty(QTextFormat::TableCellBottomBorder))
                styleString += " border-bottom:"_L1 + QString::number(cellFormat.bottomBorder()) + "px;"_L1;
            if (cellFormat.hasProperty(QTextFormat::TableCellLeftBorder))
                styleString += " border-left:"_L1 + QString::number(cellFormat.leftBorder()) + "px;"_L1;

            if (cellFormat.hasProperty(QTextFormat::TableCellTopBorderBrush))
                styleString += " border-top-color:"_L1 + cellFormat.topBorderBrush().color().name() + u';';
            if (cellFormat.hasProperty(QTextFormat::TableCellRightBorderBrush))
                styleString += " border-right-color:"_L1 + cellFormat.rightBorderBrush().color().name() + u';';
            if (cellFormat.hasProperty(QTextFormat::TableCellBottomBorderBrush))
                styleString += " border-bottom-color:"_L1 + cellFormat.bottomBorderBrush().color().name() + u';';
            if (cellFormat.hasProperty(QTextFormat::TableCellLeftBorderBrush))
                styleString += " border-left-color:"_L1 + cellFormat.leftBorderBrush().color().name() + u';';

            if (cellFormat.hasProperty(QTextFormat::TableCellTopBorderStyle))
                styleString += " border-top-style:"_L1 + richtextBorderStyleToHtmlBorderStyle(cellFormat.topBorderStyle()) + u';';
            if (cellFormat.hasProperty(QTextFormat::TableCellRightBorderStyle))
                styleString += " border-right-style:"_L1 + richtextBorderStyleToHtmlBorderStyle(cellFormat.rightBorderStyle()) + u';';
            if (cellFormat.hasProperty(QTextFormat::TableCellBottomBorderStyle))
                styleString += " border-bottom-style:"_L1 + richtextBorderStyleToHtmlBorderStyle(cellFormat.bottomBorderStyle()) + u';';
            if (cellFormat.hasProperty(QTextFormat::TableCellLeftBorderStyle))
                styleString += " border-left-style:"_L1 + richtextBorderStyleToHtmlBorderStyle(cellFormat.leftBorderStyle()) + u';';

            if (!styleString.isEmpty())
                html += " style=\""_L1 + styleString + u'\"';

            html += u'>';

            emitFrame(cell.begin());

            html += "</td>"_L1;

            defaultCharFormat = oldDefaultCharFormat;
        }

        html += "</tr>"_L1;
        if (headerRowCount > 0 && row == headerRowCount - 1)
            html += "</thead>"_L1;
    }

    html += "</table>"_L1;
}

//  from src/gui/text/qtextdocument.cpp, line 2898, as _ZN17QTextHtmlExporter15emitBorderStyleEN16QTextFrameFormat11BorderStyleE
inline void QTextHtmlExporter::emitBorderStyle(QTextFrameFormat::BorderStyle style)
{
    Q_ASSERT(style <= QTextFrameFormat::BorderStyle_Outset);

    html += " border-style:"_L1;
    html += richtextBorderStyleToHtmlBorderStyle(style);
    html += u';';
}

//  from src/gui/text/qtextdocument.cpp, line 2394, as _ZN17QTextHtmlExporterC1EPK13QTextDocument
inline QTextHtmlExporter::QTextHtmlExporter(const QTextDocument *_doc)
    : doc(_doc), fragmentMarkers(false)
{
    const QFont defaultFont = doc->defaultFont();
    defaultCharFormat.setFont(defaultFont);
}

//  from src/gui/text/qtextdocument.cpp, line 2411, as _ZN17QTextHtmlExporter6toHtmlENS_10ExportModeE
inline QString QTextHtmlExporter::toHtml(ExportMode mode)
{
    html = "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
           "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
           "<html><head><meta name=\"qrichtext\" content=\"1\" />"_L1;
    html.reserve(QTextDocumentPrivate::get(doc)->length());

    fragmentMarkers = (mode == ExportFragment);

    html += "<meta charset=\"utf-8\" />"_L1;

    QString title  = doc->metaInformation(QTextDocument::DocumentTitle);
    if (!title.isEmpty()) {
        html += "<title>"_L1;
        html += title;
        html += "</title>"_L1;
    }
    html += "<style type=\"text/css\">\n"_L1;
    html += "p, li { white-space: pre-wrap; }\n"_L1;
    html += "hr { height: 1px; border-width: 0; }\n"_L1;
    html += "li.unchecked::marker { content: \"\\2610\"; }\n"_L1;
    html += "li.checked::marker { content: \"\\2612\"; }\n"_L1;
    html += "</style>"_L1;
    html += "</head><body"_L1;

    if (mode == ExportEntireDocument) {
        html += " style=\""_L1;

        emitFontFamily(resolvedFontFamilies(defaultCharFormat));

        if (defaultCharFormat.hasProperty(QTextFormat::FontPointSize)) {
            html += " font-size:"_L1;
            html += QString::number(defaultCharFormat.fontPointSize());
            html += "pt;"_L1;
        } else if (defaultCharFormat.hasProperty(QTextFormat::FontPixelSize)) {
            html += " font-size:"_L1;
            html += QString::number(defaultCharFormat.intProperty(QTextFormat::FontPixelSize));
            html += "px;"_L1;
        }

        html += " font-weight:"_L1;
        html += QString::number(defaultCharFormat.fontWeight());
        html += u';';

        html += " font-style:"_L1;
        html += (defaultCharFormat.fontItalic() ? "italic"_L1 : "normal"_L1);
        html += u';';

        const bool percentSpacing = (defaultCharFormat.fontLetterSpacingType() == QFont::PercentageSpacing);
        if (defaultCharFormat.hasProperty(QTextFormat::FontLetterSpacing) &&
            (!percentSpacing || defaultCharFormat.fontLetterSpacing() != 0.0)) {
            html += " letter-spacing:"_L1;
            qreal value = defaultCharFormat.fontLetterSpacing();
            if (percentSpacing) // Map to em (100% == 0em)
                value = (value / 100) - 1;
            html += QString::number(value);
            html += percentSpacing ? "em;"_L1 : "px;"_L1;
        }

        if (defaultCharFormat.hasProperty(QTextFormat::FontWordSpacing) &&
            defaultCharFormat.fontWordSpacing() != 0.0) {
            html += " word-spacing:"_L1;
            html += QString::number(defaultCharFormat.fontWordSpacing());
            html += "px;"_L1;
        }

        QString decorationTag(" text-decoration:"_L1);
        bool atLeastOneDecorationSet = false;
        if (defaultCharFormat.hasProperty(QTextFormat::FontUnderline) || defaultCharFormat.hasProperty(QTextFormat::TextUnderlineStyle)) {
            if (defaultCharFormat.fontUnderline()) {
                decorationTag += " underline"_L1;
                atLeastOneDecorationSet = true;
            }
        }
        if (defaultCharFormat.hasProperty(QTextFormat::FontOverline)) {
            if (defaultCharFormat.fontOverline()) {
                decorationTag += " overline"_L1;
                atLeastOneDecorationSet = true;
            }
        }
        if (defaultCharFormat.hasProperty(QTextFormat::FontStrikeOut)) {
            if (defaultCharFormat.fontStrikeOut()) {
                decorationTag += " line-through"_L1;
                atLeastOneDecorationSet = true;
            }
        }
        if (atLeastOneDecorationSet)
            html += decorationTag + u';';

        html += u'\"';

        const QTextFrameFormat fmt = doc->rootFrame()->frameFormat();
        emitBackgroundAttribute(fmt);

    } else {
        defaultCharFormat = QTextCharFormat();
    }
    html += u'>';

    QTextFrameFormat rootFmt = doc->rootFrame()->frameFormat();
    rootFmt.clearProperty(QTextFormat::BackgroundBrush);

    QTextFrameFormat defaultFmt;
    defaultFmt.setMargin(doc->documentMargin());

    if (rootFmt == defaultFmt)
        emitFrame(doc->rootFrame()->begin());
    else
        emitTextFrame(doc->rootFrame());

    html += "</body></html>"_L1;
    return html;
}

//  from src/gui/text/qtextdocument.cpp, line 3603, as _ZN17QTextHtmlExporter9emitFrameERKN10QTextFrame8iteratorE
inline void QTextHtmlExporter::emitFrame(const QTextFrame::Iterator &frameIt)
{
    if (!frameIt.atEnd()) {
        QTextFrame::Iterator next = frameIt;
        ++next;
        if (next.atEnd()
            && frameIt.currentFrame() == nullptr
            && frameIt.parentFrame() != doc->rootFrame()
            && frameIt.currentBlock().begin().atEnd())
            return;
    }

    for (QTextFrame::Iterator it = frameIt;
         !it.atEnd(); ++it) {
        if (QTextFrame *f = it.currentFrame()) {
            if (QTextTable *table = qobject_cast<QTextTable *>(f)) {
                emitTable(table);
            } else {
                emitTextFrame(f);
            }
        } else if (it.currentBlock().isValid()) {
            emitBlock(it.currentBlock());
        }
    }
}

//  from src/gui/text/qtextdocument.cpp, line 3629, as _ZN17QTextHtmlExporter13emitTextFrameEPK10QTextFrame
inline void QTextHtmlExporter::emitTextFrame(const QTextFrame *f)
{
    FrameType frameType = f->parentFrame() ? TextFrame : RootFrame;

    html += "\n<table"_L1;
    QTextFrameFormat format = f->frameFormat();

    if (format.hasProperty(QTextFormat::FrameBorder))
        emitAttribute("border", QString::number(format.border()));

    emitFrameStyle(format, frameType);

    emitTextLength("width", format.width());
    emitTextLength("height", format.height());

    // root frame's bcolor goes in the <body> tag
    if (frameType != RootFrame)
        emitBackgroundAttribute(format);

    html += u'>';
    html += "\n<tr>\n<td style=\"border: none;\">"_L1;
    emitFrame(f->begin());
    html += "</td></tr></table>"_L1;
}

//  from src/gui/text/qtextdocument.cpp, line 3179, as _ZN17QTextHtmlExporter9emitBlockERK10QTextBlock
inline void QTextHtmlExporter::emitBlock(const QTextBlock &block)
{
    if (block.begin().atEnd()) {
        // ### HACK, remove once QTextFrame::Iterator is fixed
        int p = block.position();
        if (p > 0)
            --p;

        QTextDocumentPrivate::FragmentIterator frag = QTextDocumentPrivate::get(doc)->find(p);
        QChar ch = QTextDocumentPrivate::get(doc)->buffer().at(frag->stringPosition);
        if (ch == QTextBeginningOfFrame
            || ch == QTextEndOfFrame)
            return;
    }

    html += u'\n';

    // save and later restore, in case we 'change' the default format by
    // emitting block char format information
    QTextCharFormat oldDefaultCharFormat = defaultCharFormat;

    QTextList *list = block.textList();
    if (list) {
        if (list->itemNumber(block) == 0) { // first item? emit <ul> or appropriate
            const QTextListFormat format = list->format();
            const int style = format.style();
            bool ordered = false;
            switch (style) {
                case QTextListFormat::ListDisc: html += "<ul"_L1; break;
                case QTextListFormat::ListCircle: html += "<ul type=\"circle\""_L1; break;
                case QTextListFormat::ListSquare: html += "<ul type=\"square\""_L1; break;
                case QTextListFormat::ListDecimal: html += "<ol"_L1; ordered = true; break;
                case QTextListFormat::ListLowerAlpha: html += "<ol type=\"a\""_L1; ordered = true; break;
                case QTextListFormat::ListUpperAlpha: html += "<ol type=\"A\""_L1; ordered = true; break;
                case QTextListFormat::ListLowerRoman: html += "<ol type=\"i\""_L1; ordered = true; break;
                case QTextListFormat::ListUpperRoman: html += "<ol type=\"I\""_L1; ordered = true; break;
                default: html += "<ul"_L1; // ### should not happen
            }

            if (ordered && format.start() != 1) {
                html += " start=\""_L1;
                html += QString::number(format.start());
                html += u'"';
            }

            QString styleString;
            styleString += "margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px;"_L1;

            if (format.hasProperty(QTextFormat::ListIndent)) {
                styleString += " -qt-list-indent: "_L1;
                styleString += QString::number(format.indent());
                styleString += u';';
            }

            if (format.hasProperty(QTextFormat::ListNumberPrefix)) {
                QString numberPrefix = format.numberPrefix();
                numberPrefix.replace(u'"', "\\22"_L1);
                numberPrefix.replace(u'\'', "\\27"_L1); // FIXME: There's a problem in the CSS parser the prevents this from being correctly restored
                styleString += " -qt-list-number-prefix: "_L1;
                styleString += u'\'';
                styleString += numberPrefix;
                styleString += u'\'';
                styleString += u';';
            }

            if (format.hasProperty(QTextFormat::ListNumberSuffix)) {
                if (format.numberSuffix() != "."_L1) { // this is our default
                    QString numberSuffix = format.numberSuffix();
                    numberSuffix.replace(u'"', "\\22"_L1);
                    numberSuffix.replace(u'\'', "\\27"_L1); // see above
                    styleString += " -qt-list-number-suffix: "_L1;
                    styleString += u'\'';
                    styleString += numberSuffix;
                    styleString += u'\'';
                    styleString += u';';
                }
            }

            html += " style=\""_L1;
            html += styleString;
            html += "\">\n"_L1;
        }

        html += "<li"_L1;

        const QTextCharFormat blockFmt = formatDifference(defaultCharFormat, block.charFormat()).toCharFormat();
        if (!blockFmt.properties().isEmpty()) {
            html += " style=\""_L1;
            emitCharFormatStyle(blockFmt);
            html += u'\"';

            defaultCharFormat.merge(block.charFormat());
        }
        if (block.blockFormat().hasProperty(QTextFormat::BlockMarker)) {
            switch (block.blockFormat().marker()) {
            case QTextBlockFormat::MarkerType::Checked:
                html += " class=\"checked\""_L1;
                break;
            case QTextBlockFormat::MarkerType::Unchecked:
                html += " class=\"unchecked\""_L1;
                break;
            case QTextBlockFormat::MarkerType::NoMarker:
                break;
            }
        }
    }

    const QTextBlockFormat blockFormat = block.blockFormat();
    if (blockFormat.hasProperty(QTextFormat::BlockTrailingHorizontalRulerWidth)) {
        html += "<hr"_L1;

        QTextLength width = blockFormat.lengthProperty(QTextFormat::BlockTrailingHorizontalRulerWidth);
        if (width.type() != QTextLength::VariableLength)
            emitTextLength("width", width);
        html += u' ';

        if (blockFormat.hasProperty(QTextFormat::BackgroundBrush)) {
            html += "style=\""_L1;
            html += "background-color:"_L1;
            html += colorValue(qvariant_cast<QBrush>(blockFormat.property(QTextFormat::BackgroundBrush)).color());
            html += u';';
            html += u'\"';
        }

        html += "/>"_L1;
        return;
    }

    const bool pre = blockFormat.nonBreakableLines();
    if (pre) {
        if (list)
            html += u'>';
        html += "<pre"_L1;
    } else if (!list) {
        int headingLevel = blockFormat.headingLevel();
        if (headingLevel > 0 && headingLevel <= 6)
            html += "<h"_L1 + QString::number(headingLevel);
        else
            html += "<p"_L1;
    }

    emitBlockAttributes(block);

    html += u'>';
    if (block.begin().atEnd())
        html += "<br />"_L1;

    QTextBlock::Iterator it = block.begin();
    if (fragmentMarkers && !it.atEnd() && block == doc->begin())
        html += "<!--StartFragment-->"_L1;

    for (; !it.atEnd(); ++it)
        emitFragment(it.fragment());

    if (fragmentMarkers && block.position() + block.length() == QTextDocumentPrivate::get(doc)->length())
        html += "<!--EndFragment-->"_L1;

    QString closeTags;

    if (pre)
        html += "</pre>"_L1;
    else if (list)
        closeTags += "</li>"_L1;
    else {
        int headingLevel = blockFormat.headingLevel();
        if (headingLevel > 0 && headingLevel <= 6)
            html += QString::asprintf("</h%d>", headingLevel);
        else
            html += "</p>"_L1;
    }

    if (list) {
        if (list->itemNumber(block) == list->count() - 1) { // last item? close list
            if (isOrderedList(list->format().style()))
                closeTags += "</ol>"_L1;
            else
                closeTags += "</ul>"_L1;
        }
        const QTextBlock nextBlock = block.next();
        // If the next block is the beginning of a new deeper nested list, then we don't
        // want to close the current list item just yet. This should be closed when this
        // item is fully finished
        if (nextBlock.isValid() && nextBlock.textList() &&
            nextBlock.textList()->itemNumber(nextBlock) == 0 &&
            nextBlock.textList()->format().indent() > list->format().indent()) {
            QString lastTag;
            if (!closingTags.isEmpty() && list->itemNumber(block) == list->count() - 1)
                lastTag = closingTags.takeLast();
            lastTag.prepend(closeTags);
            closingTags << lastTag;
        } else if (list->itemNumber(block) == list->count() - 1) {
            // If we are at the end of the list now then we can add in the closing tags for that
            // current block
            html += closeTags;
            if (!closingTags.isEmpty())
                html += closingTags.takeLast();
        } else {
            html += closeTags;
        }
    }

    defaultCharFormat = oldDefaultCharFormat;
}

//  from src/gui/text/qtextdocument.cpp, line 2956, as _ZN17QTextHtmlExporter12emitFragmentERK13QTextFragment
inline void QTextHtmlExporter::emitFragment(const QTextFragment &fragment)
{
    const QTextCharFormat format = fragment.charFormat();

    bool closeAnchor = false;

    if (format.isAnchor()) {
        const auto names = format.anchorNames();
        if (!names.isEmpty()) {
            html += "<a name=\""_L1;
            html += names.constFirst().toHtmlEscaped();
            html += "\"></a>"_L1;
        }
        const QString href = format.anchorHref();
        const QString tooltip = format.toolTip();
        const bool hasHref = !href.isEmpty();
        const bool hasTooltip = !tooltip.isEmpty();
        if (hasHref || hasTooltip) {
            html += "<a"_L1;
            if (hasHref) {
                html += " href=\""_L1;
                html += href.toHtmlEscaped();
                html += u'"';
            }
            if (hasTooltip) {
                html += " title=\""_L1;
                html += tooltip.toHtmlEscaped();
                html += u'"';
            }
            html += u'>';
            closeAnchor = true;
        }
    }

    QString txt = fragment.text();
    const bool isObject = txt.contains(QChar::ObjectReplacementCharacter);
    const bool isImage = isObject && format.isImageFormat();

    // A tool tip on a fragment that is not an (href) anchor and not an image is
    // exported as a title attribute on the wrapping span. title and href are
    // independent, so a tool tip does not require an anchor; the anchor case
    // already emitted the tool tip as the <a> title above, and images carry
    // their own title attribute.
    const QString spanToolTip = (!closeAnchor && !isImage) ? format.toolTip() : QString();

    const auto styleTag = "<span style=\""_L1;
    html += styleTag;

    bool attributesEmitted = false;
    if (!isImage)
        attributesEmitted = emitCharFormatStyle(format);

    bool spanEmitted = attributesEmitted;
    if (attributesEmitted)
        html += u'"'; // close the style="..." value; the tag is closed below
    else
        html.chop(styleTag.size()); // there was no style attribute after all

    if (!spanToolTip.isEmpty()) {
        if (!spanEmitted) {
            html += "<span"_L1;
            spanEmitted = true;
        }
        html += " title=\""_L1;
        html += spanToolTip.toHtmlEscaped();
        html += u'"';
    }
    if (spanEmitted)
        html += u'>';

    if (isObject) {
        for (int i = 0; isImage && i < txt.size(); ++i) {
            QTextImageFormat imgFmt = format.toImageFormat();

            html += "<img"_L1;

            QString maxWidthCss;

            if (imgFmt.hasProperty(QTextFormat::ImageMaxWidth)) {
                auto length = imgFmt.lengthProperty(QTextFormat::ImageMaxWidth);
                maxWidthCss += "max-width:"_L1;
                if (length.type() == QTextLength::PercentageLength)
                    maxWidthCss += QString::number(length.rawValue()) + "%;"_L1;
                else if (length.type() == QTextLength::FixedLength)
                    maxWidthCss += QString::number(length.rawValue()) + "px;"_L1;
            }

            if (imgFmt.hasProperty(QTextFormat::ImageName))
                emitAttribute("src", imgFmt.name());

            if (imgFmt.hasProperty(QTextFormat::ImageAltText))
                emitAttribute("alt", imgFmt.stringProperty(QTextFormat::ImageAltText));

            if (imgFmt.hasProperty(QTextFormat::ImageTitle))
                emitAttribute("title", imgFmt.stringProperty(QTextFormat::ImageTitle));

            if (imgFmt.hasProperty(QTextFormat::ImageWidth))
                emitAttribute("width", QString::number(imgFmt.width()));

            if (imgFmt.hasProperty(QTextFormat::ImageHeight))
                emitAttribute("height", QString::number(imgFmt.height()));

            if (imgFmt.verticalAlignment() == QTextCharFormat::AlignMiddle)
                html += " style=\"vertical-align: middle;"_L1 + maxWidthCss + u'\"';
            else if (imgFmt.verticalAlignment() == QTextCharFormat::AlignTop)
                html += " style=\"vertical-align: top;"_L1 + maxWidthCss + u'\"';
            else if (!maxWidthCss.isEmpty())
                html += " style=\""_L1 + maxWidthCss + u'\"';

            if (QTextFrame *imageFrame = qobject_cast<QTextFrame *>(doc->objectForFormat(imgFmt)))
                emitFloatStyle(imageFrame->frameFormat().position());

            html += " />"_L1;
        }
    } else {
        Q_ASSERT(!txt.contains(QChar::ObjectReplacementCharacter));

        txt = txt.toHtmlEscaped();

        // split for [\n{LineSeparator}]
        // space in BR on purpose for compatibility with old-fashioned browsers
        txt.replace(u'\n', "<br />"_L1);
        txt.replace(QChar::LineSeparator, "<br />"_L1);
        html += txt;
    }

    if (spanEmitted)
        html += "</span>"_L1;

    if (closeAnchor)
        html += "</a>"_L1;
}

//  from src/gui/text/qtextdocument.cpp, line 2818, as _ZN17QTextHtmlExporter14emitTextLengthEPKcRK11QTextLength
inline void QTextHtmlExporter::emitTextLength(const char *attribute, const QTextLength &length)
{
    if (length.type() == QTextLength::VariableLength) // default
        return;

    html += u' ';
    html += QLatin1StringView(attribute);
    html += "=\""_L1;
    html += QString::number(length.rawValue());

    if (length.type() == QTextLength::PercentageLength)
        html += "%\""_L1;
    else
        html += u'\"';
}

//  from src/gui/text/qtextdocument.cpp, line 2834, as _ZN17QTextHtmlExporter13emitAlignmentE6QFlagsIN2Qt13AlignmentFlagEE
inline void QTextHtmlExporter::emitAlignment(Qt::Alignment align)
{
    if (align & Qt::AlignLeft)
        return;
    else if (align & Qt::AlignRight)
        html += " align=\"right\""_L1;
    else if (align & Qt::AlignHCenter)
        html += " align=\"center\""_L1;
    else if (align & Qt::AlignJustify)
        html += " align=\"justify\""_L1;
}

//  from src/gui/text/qtextdocument.cpp, line 2846, as _ZN17QTextHtmlExporter14emitFloatStyleEN16QTextFrameFormat8PositionENS_9StyleModeE
inline void QTextHtmlExporter::emitFloatStyle(QTextFrameFormat::Position pos, StyleMode mode)
{
    if (pos == QTextFrameFormat::InFlow)
        return;

    if (mode == EmitStyleTag)
        html += " style=\"float:"_L1;
    else
        html += " float:"_L1;

    if (pos == QTextFrameFormat::FloatLeft)
        html += " left;"_L1;
    else if (pos == QTextFrameFormat::FloatRight)
        html += " right;"_L1;
    else
        Q_ASSERT_X(0, "QTextHtmlExporter::emitFloatStyle()", "pos should be a valid enum type");

    if (mode == EmitStyleTag)
        html += u'\"';
}

//  from src/gui/text/qtextdocument.cpp, line 2937, as _ZN17QTextHtmlExporter11emitMarginsERK7QStringS2_S2_S2_
inline void QTextHtmlExporter::emitMargins(const QString &top, const QString &bottom, const QString &left, const QString &right)
{
    html += " margin-top:"_L1;
    html += top;
    html += "px;"_L1;

    html += " margin-bottom:"_L1;
    html += bottom;
    html += "px;"_L1;

    html += " margin-left:"_L1;
    html += left;
    html += "px;"_L1;

    html += " margin-right:"_L1;
    html += right;
    html += "px;"_L1;
}

//  from src/gui/text/qtextdocument.cpp, line 2525, as _ZN17QTextHtmlExporter13emitAttributeEPKcRK7QString
inline void QTextHtmlExporter::emitAttribute(const char *attribute, const QString &value)
{
    html += u' ';
    html += QLatin1StringView(attribute);
    html += "=\""_L1;
    html += value.toHtmlEscaped();
    html += u'"';
}

//  from src/gui/text/qtextdocument.cpp, line 2907, as _ZN17QTextHtmlExporter19emitPageBreakPolicyE6QFlagsIN11QTextFormat13PageBreakFlagEE
inline void QTextHtmlExporter::emitPageBreakPolicy(QTextFormat::PageBreakFlags policy)
{
    if (policy & QTextFormat::PageBreak_AlwaysBefore)
        html += " page-break-before:always;"_L1;

    if (policy & QTextFormat::PageBreak_AlwaysAfter)
        html += " page-break-after:always;"_L1;
}

//  from src/gui/text/qtextdocument.cpp, line 2916, as _ZN17QTextHtmlExporter14emitFontFamilyERK5QListI7QStringE
inline void QTextHtmlExporter::emitFontFamily(const QStringList &families)
{
    html += " font-family:"_L1;

    bool first = true;
    for (const QString &family : families) {
        auto quote = "\'"_L1;
        if (family.contains(u'\''))
            quote = "&quot;"_L1;

        if (!first)
            html += ","_L1;
        else
            first = false;
        html += quote;
        html += family.toHtmlEscaped();
        html += quote;
    }
    html += u';';
}

//  from src/gui/text/qtextdocument.cpp, line 3385, as _ZN17QTextHtmlExporter15findUrlForImageEPK13QTextDocumentxb
inline QString QTextHtmlExporter::findUrlForImage(const QTextDocument *doc, qint64 cacheKey, bool isPixmap)
{
    QString url;
    if (!doc)
        return url;

    if (QTextDocument *parent = qobject_cast<QTextDocument *>(doc->parent()))
        return findUrlForImage(parent, cacheKey, isPixmap);

    const QTextDocumentPrivate *priv = QTextDocumentPrivate::get(doc);
    Q_ASSERT(priv != nullptr);

    QMap<QUrl, QVariant>::const_iterator it = priv->cachedResources.constBegin();
    for (; it != priv->cachedResources.constEnd(); ++it) {

        const QVariant &v = it.value();
        if (v.userType() == QMetaType::QImage && !isPixmap) {
            if (qvariant_cast<QImage>(v).cacheKey() == cacheKey)
                break;
        }

        if (v.userType() == QMetaType::QPixmap && isPixmap) {
            if (qvariant_cast<QPixmap>(v).cacheKey() == cacheKey)
                break;
        }
    }

    if (it != priv->cachedResources.constEnd())
        url = it.key().toString();

    return url;
}
//  -----------------------------------------------------------------------

//  QTextHtmlExporter::QTextHtmlExporter(const QTextDocument *_doc)
extern "C" Q_DECL_EXPORT
QTextHtmlExporter *ritual_ZN17QTextHtmlExporterC1EPK13QTextDocument(
    const QTextDocument *_doc) {
  return new QTextHtmlExporter(_doc);
}

//  QString QTextHtmlExporter::toHtml(ExportMode mode)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QTextHtmlExporter6toHtmlENS_10ExportModeE(
    QTextHtmlExporter *self,
    QTextHtmlExporter::ExportMode mode) {
  return new QString(self->toHtml(mode));
}

//  void QTextHtmlExporter::emitFrame(const QTextFrame::Iterator &frameIt)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QTextHtmlExporter9emitFrameERKN10QTextFrame8iteratorE(
    QTextHtmlExporter *self,
    const QTextFrame::Iterator *frameIt) {
  self->emitFrame(*frameIt);
}

//  void QTextHtmlExporter::emitTextFrame(const QTextFrame *frame)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QTextHtmlExporter13emitTextFrameEPK10QTextFrame(
    QTextHtmlExporter *self,
    const QTextFrame *frame) {
  self->emitTextFrame(frame);
}

//  void QTextHtmlExporter::emitBlock(const QTextBlock &block)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QTextHtmlExporter9emitBlockERK10QTextBlock(
    QTextHtmlExporter *self,
    const QTextBlock *block) {
  self->emitBlock(*block);
}

//  void QTextHtmlExporter::emitFragment(const QTextFragment &fragment)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QTextHtmlExporter12emitFragmentERK13QTextFragment(
    QTextHtmlExporter *self,
    const QTextFragment *fragment) {
  self->emitFragment(*fragment);
}

//  void QTextHtmlExporter::emitTextLength(const char *attribute, const
//      QTextLength &length)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QTextHtmlExporter14emitTextLengthEPKcRK11QTextLength(
    QTextHtmlExporter *self,
    const char *attribute,
    const QTextLength *length) {
  self->emitTextLength(attribute, *length);
}

//  void QTextHtmlExporter::emitAlignment(Qt::Alignment alignment)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QTextHtmlExporter13emitAlignmentE6QFlagsIN2Qt13AlignmentFlagEE(
    QTextHtmlExporter *self,
    int alignment) {
  self->emitAlignment(QFlags<Qt::AlignmentFlag>::fromInt(alignment));
}

//  void QTextHtmlExporter::emitFloatStyle(QTextFrameFormat::Position pos,
//      StyleMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QTextHtmlExporter14emitFloatStyleEN16QTextFrameFormat8PositionENS_9StyleModeE(
    QTextHtmlExporter *self,
    QTextFrameFormat::Position pos,
    QTextHtmlExporter::StyleMode mode) {
  self->emitFloatStyle(pos, mode);
}

//  void QTextHtmlExporter::emitMargins(const QString &top, const QString
//      &bottom, const QString &left, const QString &right)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QTextHtmlExporter11emitMarginsERK7QStringS2_S2_S2_(
    QTextHtmlExporter *self,
    const QString *top,
    const QString *bottom,
    const QString *left,
    const QString *right) {
  self->emitMargins(*top, *bottom, *left, *right);
}

//  void QTextHtmlExporter::emitAttribute(const char *attribute, const
//      QString &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QTextHtmlExporter13emitAttributeEPKcRK7QString(
    QTextHtmlExporter *self,
    const char *attribute,
    const QString *value) {
  self->emitAttribute(attribute, *value);
}

//  void QTextHtmlExporter::emitPageBreakPolicy(QTextFormat::PageBreakFlags
//      policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QTextHtmlExporter19emitPageBreakPolicyE6QFlagsIN11QTextFormat13PageBreakFlagEE(
    QTextHtmlExporter *self,
    int policy) {
  self->emitPageBreakPolicy(
      QFlags<QTextFormat::PageBreakFlag>::fromInt(policy));
}

//  void QTextHtmlExporter::emitFontFamily(const QStringList &families)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QTextHtmlExporter14emitFontFamilyERK5QListI7QStringE(
    QTextHtmlExporter *self,
    const QList<QString> *families) {
  self->emitFontFamily(*families);
}

//  QString QTextHtmlExporter::findUrlForImage(const QTextDocument *doc,
//      qint64 cacheKey, bool isPixmap)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QTextHtmlExporter15findUrlForImageEPK13QTextDocumentxb(
    QTextHtmlExporter *self,
    const QTextDocument *doc,
    qint64 cacheKey,
    bool isPixmap) {
  return new QString(self->findUrlForImage(doc, cacheKey, isPixmap));
}

//  QTextHtmlExporter::~QTextHtmlExporter()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QTextHtmlExporterD1Ev(QTextHtmlExporter *self) {
  delete self;
}
