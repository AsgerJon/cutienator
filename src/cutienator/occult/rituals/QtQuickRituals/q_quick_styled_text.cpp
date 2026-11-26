//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickstyledtext_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickstyledtext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QStack>
#include <QtCore/QList>
#include <QtGui/QPainter>
#include <QtGui/QTextLayout>
#include <QtCore/QDebug>
#include <QtCore/qmath.h>
#include <QtQuick/private/qquickstyledtext_p.h>
#include <QtQml/QQmlContext>
#include <QtGui/private/qtexthtmlparser_p.h>
#include <QtGui/private/qoutlinemapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/util/qquickstyledtext.cpp, line 47, as local:qquickstyledtext.cpp:QQuickStyledTextPrivate
class QQuickStyledTextPrivate
{
public:
    enum ListType { Ordered, Unordered };
    enum ListFormat { Bullet, Disc, Square, Decimal, LowerAlpha, UpperAlpha, LowerRoman, UpperRoman };

    struct List {
        int level;
        ListType type;
        ListFormat format;
    };

    QQuickStyledTextPrivate(const QString &t, QTextLayout &l,
                                  QList<QQuickStyledTextImgTag*> &imgTags,
                                  const QUrl &baseUrl,
                                  QQmlContext *context,
                                  bool preloadImages,
                                  bool *fontSizeModified)
        : text(t), layout(l), imgTags(&imgTags), baseFont(layout.font()), baseUrl(baseUrl),
          fontSizeModified(fontSizeModified), context(context), preloadImages(preloadImages)
    {
    }

    void parse();
    void appendText(const QString &textIn, int start, int length, QString &textOut);
    bool parseTag(const QChar *&ch, const QString &textIn, QString &textOut, QTextCharFormat &format);
    bool parseCloseTag(const QChar *&ch, const QString &textIn, QString &textOut);
    void parseEntity(const QChar *&ch, const QString &textIn, QString &textOut);
    bool parseFontAttributes(const QChar *&ch, const QString &textIn, QTextCharFormat &format);
    bool parseOrderedListAttributes(const QChar *&ch, const QString &textIn);
    bool parseUnorderedListAttributes(const QChar *&ch, const QString &textIn);
    bool parseAnchorAttributes(const QChar *&ch, const QString &textIn, QTextCharFormat &format);
    void parseImageAttributes(const QChar *&ch, const QString &textIn, QString &textOut);
    std::pair<QStringView,QStringView> parseAttribute(const QChar *&ch, const QString &textIn);
    QStringView parseValue(const QChar *&ch, const QString &textIn);
    void setFontSize(int size, QTextCharFormat &format);

    inline void skipSpace(const QChar *&ch) {
        while (ch->isSpace() && !ch->isNull())
            ++ch;
    }

    static QString toAlpha(int value, bool upper);
    static QString toRoman(int value, bool upper);

    QString text;
    QTextLayout &layout;
    QList<QQuickStyledTextImgTag*> *imgTags;
    QFont baseFont;
    QStack<List> listStack;
    QUrl baseUrl;
    bool *fontSizeModified;
    QQmlContext *context;
    int nbImages = 0;
    bool hasNewLine = true;
    bool updateImagePositions = false;
    bool preFormat = false;
    bool prependSpace = false;
    bool hasSpace = true;
    bool preloadImages;

    static const QChar lessThan;
    static const QChar greaterThan;
    static const QChar equals;
    static const QChar singleQuote;
    static const QChar doubleQuote;
    static const QChar slash;
    static const QChar ampersand;
    static const QChar bullet;
    static const QChar disc;
    static const QChar square;
    static const QChar lineFeed;
    static const QChar space;
    static const int tabsize = 6;
};

//  from ../qtdeclarative/src/quick/util/qquickstyledtext.cpp, line 137, as local:qquickstyledtext.cpp:is_equal_ignoring_case
namespace {
inline bool is_equal_ignoring_case(QStringView s1, QLatin1StringView s2) noexcept
{
    return s1.compare(s2, Qt::CaseInsensitive) == 0;
}
}  // namespace

//  from ../qtdeclarative/src/quick/util/qquickstyledtext.cpp, line 142, as local:qquickstyledtext.cpp:lookupHtmlTag
namespace {
inline int lookupHtmlTag(QStringView tag)
{
    return QTextHtmlParser::lookupElement(tag);
}
}  // namespace

//  from ../qtdeclarative/src/quick/util/qquickstyledtext.cpp, line 176, as local:qquickstyledtext.cpp:QQuickStyledTextPrivate::parse
inline void QQuickStyledTextPrivate::parse()
{
    QList<QTextLayout::FormatRange> ranges;
    QStack<QTextCharFormat> formatStack;

    QString drawText;
    drawText.reserve(text.size());

    updateImagePositions = !imgTags->isEmpty();

    int textStart = 0;
    int textLength = 0;
    int rangeStart = 0;
    bool formatChanged = false;

    const QChar *ch = text.constData();
    while (!ch->isNull()) {
        if (*ch == lessThan) {
            if (textLength) {
                appendText(text, textStart, textLength, drawText);
            } else if (prependSpace) {
                drawText.append(space);
                prependSpace = false;
                hasSpace = true;
            }

            if (rangeStart != drawText.size() && formatStack.size()) {
                if (formatChanged) {
                    QTextLayout::FormatRange formatRange;
                    formatRange.format = formatStack.top();
                    formatRange.start = rangeStart;
                    formatRange.length = drawText.size() - rangeStart;
                    ranges.append(formatRange);
                    formatChanged = false;
                } else if (ranges.size()) {
                    ranges.last().length += drawText.size() - rangeStart;
                }
            }
            rangeStart = drawText.size();
            ++ch;
            if (*ch == slash) {
                ++ch;
                if (parseCloseTag(ch, text, drawText)) {
                    if (formatStack.size()) {
                        formatChanged = true;
                        formatStack.pop();
                    }
                }
            } else {
                QTextCharFormat format;
                if (formatStack.size())
                    format = formatStack.top();
                if (parseTag(ch, text, drawText, format)) {
                    formatChanged = true;
                    formatStack.push(format);
                }
            }
            textStart = ch - text.constData() + 1;
            textLength = 0;
        } else if (*ch == ampersand) {
            ++ch;
            appendText(text, textStart, textLength, drawText);
            parseEntity(ch, text, drawText);
            textStart = ch - text.constData() + 1;
            textLength = 0;
        } else if (ch->isSpace()) {
            if (textLength)
                appendText(text, textStart, textLength, drawText);
            if (!preFormat) {
                prependSpace = !hasSpace;
                for (const QChar *n = ch + 1; !n->isNull() && n->isSpace(); ++n)
                    ch = n;
                hasNewLine = false;
            } else  if (*ch == lineFeed) {
                drawText.append(QChar(QChar::LineSeparator));
                hasNewLine = true;
            } else {
                drawText.append(QChar(QChar::Nbsp));
                hasNewLine = false;
            }
            textStart = ch - text.constData() + 1;
            textLength = 0;
        } else {
            ++textLength;
        }
        if (!ch->isNull())
            ++ch;
    }
    if (textLength)
        appendText(text, textStart, textLength, drawText);
    if (rangeStart != drawText.size() && formatStack.size()) {
        if (formatChanged) {
            QTextLayout::FormatRange formatRange;
            formatRange.format = formatStack.top();
            formatRange.start = rangeStart;
            formatRange.length = drawText.size() - rangeStart;
            ranges.append(formatRange);
        } else if (ranges.size()) {
            ranges.last().length += drawText.size() - rangeStart;
        }
    }

    // Add QTextImageFormat ranges for each inline image so that
    // QTextEngine sizes the ObjectReplacementCharacter correctly.
    if (imgTags) {
        for (int i = 0; i < imgTags->size(); ++i) {
            const QQuickStyledTextImgTag *image = imgTags->at(i);
            QTextLayout::FormatRange range;
            QTextImageFormat imgFmt;
            if (image->size.isValid()) {
                imgFmt.setWidth(image->size.width() + QQuickStyledTextImgTag::HMargin * 2);
                imgFmt.setHeight(image->size.height());
            }
            // Ensures line.height() equals the image height, not inflated by font descent.
            imgFmt.setVerticalAlignment(QTextCharFormat::AlignBaseline);
            imgFmt.setObjectIndex(i); // index into imgTags, used by image positioning in QQuickText
            range.format = imgFmt;
            range.start = image->position;
            range.length = 1;
            ranges.append(range);
        }
    }

    layout.setText(drawText);
    layout.setFormats(ranges);
}

//  from ../qtdeclarative/src/quick/util/qquickstyledtext.cpp, line 303, as local:qquickstyledtext.cpp:QQuickStyledTextPrivate::appendText
inline void QQuickStyledTextPrivate::appendText(const QString &textIn, int start, int length, QString &textOut)
{
    if (prependSpace)
        textOut.append(space);
    textOut.append(QStringView(textIn).mid(start, length));
    prependSpace = false;
    hasSpace = false;
    hasNewLine = false;
}

//  from ../qtdeclarative/src/quick/util/qquickstyledtext.cpp, line 737, as local:qquickstyledtext.cpp:QQuickStyledTextPrivate::parseAttribute
inline std::pair<QStringView,QStringView> QQuickStyledTextPrivate::parseAttribute(const QChar *&ch, const QString &textIn)
{
    skipSpace(ch);

    int attrStart = ch - textIn.constData();
    int attrLength = 0;
    while (!ch->isNull()) {
        if (*ch == greaterThan) {
            break;
        } else if (*ch == equals) {
            ++ch;
            if (*ch != singleQuote && *ch != doubleQuote) {
                while (*ch != greaterThan && !ch->isNull())
                    ++ch;
                break;
            }
            ++ch;
            if (!attrLength)
                break;
            auto attr = QStringView(textIn).mid(attrStart, attrLength);
            QStringView val = parseValue(ch, textIn);
            if (!val.isEmpty())
                return std::pair<QStringView,QStringView>(attr,val);
            break;
        } else {
            ++attrLength;
        }
        ++ch;
    }

    return std::pair<QStringView,QStringView>();
}

//  from ../qtdeclarative/src/quick/util/qquickstyledtext.cpp, line 770, as local:qquickstyledtext.cpp:QQuickStyledTextPrivate::parseValue
inline QStringView QQuickStyledTextPrivate::parseValue(const QChar *&ch, const QString &textIn)
{
    int valStart = ch - textIn.constData();
    int valLength = 0;
    while (*ch != singleQuote && *ch != doubleQuote && !ch->isNull()) {
        ++valLength;
        ++ch;
    }
    if (ch->isNull())
        return QStringView();
    ++ch; // skip quote

    return QStringView(textIn).mid(valStart, valLength);
}

//  from ../qtdeclarative/src/quick/util/qquickstyledtext.cpp, line 785, as local:qquickstyledtext.cpp:QQuickStyledTextPrivate::toAlpha
inline QString QQuickStyledTextPrivate::toAlpha(int value, bool upper)
{
    const char baseChar = upper ? 'A' : 'a';

    QString result;
    int c = value;
    while (c > 0) {
        c--;
        result.prepend(QChar(baseChar + (c % 26)));
        c /= 26;
    }
    return result;
}

//  from ../qtdeclarative/src/quick/util/qquickstyledtext.cpp, line 799, as local:qquickstyledtext.cpp:QQuickStyledTextPrivate::toRoman
inline QString QQuickStyledTextPrivate::toRoman(int value, bool upper)
{
    QString result = QLatin1String("?");
    // works for up to 4999 items
    if (value < 5000) {
        QByteArray romanNumeral;

        static const char romanSymbolsLower[] = "iiivixxxlxcccdcmmmm";
        static const char romanSymbolsUpper[] = "IIIVIXXXLXCCCDCMMMM";
        QByteArray romanSymbols;
        if (!upper)
            romanSymbols = QByteArray::fromRawData(romanSymbolsLower, sizeof(romanSymbolsLower));
        else
            romanSymbols = QByteArray::fromRawData(romanSymbolsUpper, sizeof(romanSymbolsUpper));

        int c[] = { 1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000 };
        int n = value;
        for (int i = 12; i >= 0; n %= c[i], i--) {
            int q = n / c[i];
            if (q > 0) {
                int startDigit = i + (i + 3) / 4;
                int numDigits;
                if (i % 4) {
                    if ((i - 2) % 4)
                        numDigits = 2;
                    else
                        numDigits = 1;
                }
                else
                    numDigits = q;
                romanNumeral.append(romanSymbols.mid(startDigit, numDigits));
            }
        }
        result = QString::fromLatin1(romanNumeral);
    }
    return result;
}

//  from ../qtdeclarative/src/quick/util/qquickstyledtext.cpp, line 148, as _ZN16QQuickStyledTextC1ERK7QStringR11QTextLayoutR5QListIP22QQuickStyledTextImgTagERK4QUrlP11QQmlContextbPb
inline QQuickStyledText::QQuickStyledText(const QString &string, QTextLayout &layout,
                                               QList<QQuickStyledTextImgTag*> &imgTags,
                                               const QUrl &baseUrl,
                                               QQmlContext *context,
                                               bool preloadImages,
                                               bool *fontSizeModified)
    : d(new QQuickStyledTextPrivate(string, layout, imgTags, baseUrl, context, preloadImages, fontSizeModified))
{
}

//  from ../qtdeclarative/src/quick/util/qquickstyledtext.cpp, line 476, as _ZN23QQuickStyledTextPrivate13parseCloseTagERPK5QCharRK7QStringRS4_
inline bool QQuickStyledTextPrivate::parseCloseTag(const QChar *&ch, const QString &textIn, QString &textOut)
{
    skipSpace(ch);

    int tagStart = ch - textIn.constData();
    int tagLength = 0;
    while (!ch->isNull()) {
        if (*ch == greaterThan) {
            if (tagLength == 0)
                return false;
            auto tag = QStringView(textIn).mid(tagStart, tagLength);
            hasNewLine = false;
            switch (lookupHtmlTag(tag)) {
            case Html_b:
            case Html_i:
            case Html_a:
            case Html_u:
            case Html_font:
            case Html_strong:
            case Html_del:
            case Html_s:
                return true;
            case Html_br:
                return false;
            case Html_p:
                textOut.append(QChar::LineSeparator);
                hasNewLine = true;
                hasSpace = true;
                return false;
            case Html_pre:
                preFormat = false;
                if (!hasNewLine)
                    textOut.append(QChar::LineSeparator);
                hasNewLine = true;
                hasSpace = true;
                return true;
            case Html_ul:
            case Html_ol:
                if (!listStack.isEmpty()) {
                    listStack.pop();
                    if (!listStack.size())
                        textOut.append(QChar::LineSeparator);
                }
                return false;
            case Html_h1:
            case Html_h2:
            case Html_h3:
            case Html_h4:
            case Html_h5:
            case Html_h6:
                textOut.append(QChar::LineSeparator);
                hasNewLine = true;
                hasSpace = true;
                return true;
            case Html_li:
                return false;
            default:
                break;
            }
            return false;
        } else if (!ch->isSpace()){
            tagLength++;
        }
        ++ch;
    }

    return false;
}

//  from ../qtdeclarative/src/quick/util/qquickstyledtext.cpp, line 158, as _ZN16QQuickStyledTextD1Ev
inline QQuickStyledText::~QQuickStyledText()
{
    delete d;
}
//  -----------------------------------------------------------------------

//  QQuickStyledText::~QQuickStyledText()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QQuickStyledTextD1Ev(QQuickStyledText *self) {
  delete self;
}
