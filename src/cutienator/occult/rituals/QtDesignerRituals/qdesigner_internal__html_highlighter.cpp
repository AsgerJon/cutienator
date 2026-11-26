//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/htmlhighlighter_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'qdesigner_internal::HtmlHighlighter' is pasted in, cut from what the moc
//  of Qt 6.12.0 writes for its header: Qt's library keeps it to itself;
//  added are 2 rituals that lean on what moc writes for a class of the part
//  Qt keeps to itself, whose ritual file carries moc's output, drafted by a
//  copy of the generator that lets those names through. A copy of a meta-
//  object is a second one: 'qobject_cast' between it and Qt's own does not
//  match. Kept as it is when the generator runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/htmlhighlighter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qtextformat.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <QtCore/qtextstream.h>
#include <QtWidgets/qtextedit.h>
#include <QtDesigner/private/htmlhighlighter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only WITH Qt-GPL-exception-1.0
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from QtDesigner__qdesigner_internal_HtmlHighlighter.cpp, line 1, as moc:qdesigner_internal::HtmlHighlighter
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN18qdesigner_internal15HtmlHighlighterE_t {};
} // unnamed namespace

template <> constexpr inline auto qdesigner_internal::HtmlHighlighter::qt_create_metaobjectdata<qt_meta_tag_ZN18qdesigner_internal15HtmlHighlighterE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "qdesigner_internal::HtmlHighlighter"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<HtmlHighlighter, qt_meta_tag_ZN18qdesigner_internal15HtmlHighlighterE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject qdesigner_internal::HtmlHighlighter::staticMetaObject = { {
    QMetaObject::SuperData::link<QSyntaxHighlighter::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18qdesigner_internal15HtmlHighlighterE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18qdesigner_internal15HtmlHighlighterE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN18qdesigner_internal15HtmlHighlighterE_t>.metaTypes,
    nullptr
} };

void qdesigner_internal::HtmlHighlighter::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<HtmlHighlighter *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *qdesigner_internal::HtmlHighlighter::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *qdesigner_internal::HtmlHighlighter::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN18qdesigner_internal15HtmlHighlighterE_t>.strings))
        return static_cast<void*>(this);
    return QSyntaxHighlighter::qt_metacast(_clname);
}

int qdesigner_internal::HtmlHighlighter::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QSyntaxHighlighter::qt_metacall(_c, _id, _a);
    return _id;
}
QT_WARNING_POP

//  from ../qttools/src/designer/src/lib/shared/htmlhighlighter.cpp, line 50, as _ZN18qdesigner_internal15HtmlHighlighter14highlightBlockERK7QString
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void HtmlHighlighter::highlightBlock(const QString &text)
{
    static const QChar tab = u'\t';
    static const QChar space = u' ';

    int state = previousBlockState();
    qsizetype len = text.size();
    qsizetype start = 0;
    qsizetype pos = 0;

    while (pos < len) {
        switch (state) {
        case NormalState:
        default:
            while (pos < len) {
                QChar ch = text.at(pos);
                if (ch == u'<') {
                    if (QStringView{text}.sliced(pos).startsWith("<!--"_L1)) {
                        state = InComment;
                    } else {
                        state = InTag;
                        start = pos;
                        while (pos < len && text.at(pos) != space
                               && text.at(pos) != u'>'
                               && text.at(pos) != tab
                               && !QStringView{text}.sliced(pos).startsWith("/>"_L1)) {
                            ++pos;
                        }
                        if (QStringView{text}.sliced(pos).startsWith("/>"_L1))
                            ++pos;
                        setFormat(start, pos - start,
                                  m_formats[Tag]);
                        break;
                    }
                    break;
                }
                if (ch == u'&') {
                    start = pos;
                    while (pos < len && text.at(pos++) != u';')
                        ;
                    setFormat(start, pos - start,
                              m_formats[Entity]);
                } else {
                    // No tag, comment or entity started, continue...
                    ++pos;
                }
            }
            break;
        case InComment:
            start = pos;
            for ( ; pos < len; ++pos) {
                if (QStringView{text}.sliced(pos).startsWith("-->"_L1)) {
                    pos += 3;
                    state = NormalState;
                    break;
                }
            }
            setFormat(start, pos - start, m_formats[Comment]);
            break;
        case InTag:
            QChar quote = QChar::Null;
            while (pos < len) {
                QChar ch = text.at(pos);
                if (quote.isNull()) {
                    start = pos;
                    if (ch == '\''_L1 || ch == u'"') {
                        quote = ch;
                    } else if (ch == u'>') {
                        ++pos;
                        setFormat(start, pos - start, m_formats[Tag]);
                        state = NormalState;
                        break;
                    } else if (QStringView{text}.sliced(pos).startsWith("/>"_L1)) {
                        pos += 2;
                        setFormat(start, pos - start, m_formats[Tag]);
                        state = NormalState;
                        break;
                    } else if (ch != space && text.at(pos) != tab) {
                        // Tag not ending, not a quote and no whitespace, so
                        // we must be dealing with an attribute.
                        ++pos;
                        while (pos < len && text.at(pos) != space
                               && text.at(pos) != tab
                               && text.at(pos) != u'=')
                            ++pos;
                        setFormat(start, pos - start, m_formats[Attribute]);
                        start = pos;
                    }
                } else if (ch == quote) {
                    quote = QChar::Null;

                    // Anything quoted is a value
                    setFormat(start, pos - start, m_formats[Value]);
                }
                ++pos;
            }
            break;
        }
    }
    setCurrentBlockState(state);
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/htmlhighlighter.cpp, line 16, as _ZN18qdesigner_internal15HtmlHighlighterC1EP9QTextEdit
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline HtmlHighlighter::HtmlHighlighter(QTextEdit *textEdit)
    : QSyntaxHighlighter(textEdit->document())
{
    QTextCharFormat entityFormat;
    entityFormat.setForeground(Qt::red);
    setFormatFor(Entity, entityFormat);

    QTextCharFormat tagFormat;
    tagFormat.setForeground(Qt::darkMagenta);
    tagFormat.setFontWeight(QFont::Bold);
    setFormatFor(Tag, tagFormat);

    QTextCharFormat commentFormat;
    commentFormat.setForeground(Qt::gray);
    commentFormat.setFontItalic(true);
    setFormatFor(Comment, commentFormat);

    QTextCharFormat attributeFormat;
    attributeFormat.setForeground(Qt::black);
    attributeFormat.setFontWeight(QFont::Bold);
    setFormatFor(Attribute, attributeFormat);

    QTextCharFormat valueFormat;
    valueFormat.setForeground(Qt::blue);
    setFormatFor(Value, valueFormat);
}
}  // namespace qdesigner_internal

//  from ../qttools/src/designer/src/lib/shared/htmlhighlighter.cpp, line 43, as _ZN18qdesigner_internal15HtmlHighlighter12setFormatForENS0_9ConstructERK15QTextCharFormat
namespace qdesigner_internal {
using namespace Qt::StringLiterals;
inline void HtmlHighlighter::setFormatFor(Construct construct,
                                   const QTextCharFormat &format)
{
    m_formats[construct] = format;
    rehighlight();
}
}  // namespace qdesigner_internal
//  -----------------------------------------------------------------------

//  Only a class built on qdesigner_internal::HtmlHighlighter may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct Ownqdesigner_internal_HtmlHighlighter : qdesigner_internal::HtmlHighlighter {
  using qdesigner_internal::HtmlHighlighter::highlightBlock;
};

//  const QMetaObject *qdesigner_internal::HtmlHighlighter::metaObject()
//      const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal15HtmlHighlighter10metaObjectEv(
    const qdesigner_internal::HtmlHighlighter *self) {
  return self->metaObject();
}

//  void *qdesigner_internal::HtmlHighlighter::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18qdesigner_internal15HtmlHighlighter11qt_metacastEPKc(
    qdesigner_internal::HtmlHighlighter *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int qdesigner_internal::HtmlHighlighter::qt_metacall(QMetaObject::Call
//      a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18qdesigner_internal15HtmlHighlighter11qt_metacallEN11QMetaObject4CallEiPPv(
    qdesigner_internal::HtmlHighlighter *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString qdesigner_internal::HtmlHighlighter::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18qdesigner_internal15HtmlHighlighter2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(qdesigner_internal::HtmlHighlighter::tr(s, c, n));
}

//  qdesigner_internal::HtmlHighlighter::HtmlHighlighter(QTextEdit *textEdit)
extern "C" Q_DECL_EXPORT
qdesigner_internal::HtmlHighlighter *ritual_ZN18qdesigner_internal15HtmlHighlighterC1EP9QTextEdit(
    QTextEdit *textEdit) {
  return new qdesigner_internal::HtmlHighlighter(textEdit);
}

//  void qdesigner_internal::HtmlHighlighter::setFormatFor(Construct
//      construct, const QTextCharFormat &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal15HtmlHighlighter12setFormatForENS0_9ConstructERK15QTextCharFormat(
    qdesigner_internal::HtmlHighlighter *self,
    qdesigner_internal::HtmlHighlighter::Construct construct,
    const QTextCharFormat *format) {
  self->setFormatFor(construct, *format);
}

//  QTextCharFormat qdesigner_internal::HtmlHighlighter::formatFor(Construct
//      construct) const
extern "C" Q_DECL_EXPORT
QTextCharFormat *ritual_ZNK18qdesigner_internal15HtmlHighlighter9formatForENS0_9ConstructE(
    const qdesigner_internal::HtmlHighlighter *self,
    qdesigner_internal::HtmlHighlighter::Construct construct) {
  return new QTextCharFormat(self->formatFor(construct));
}

//  void qdesigner_internal::HtmlHighlighter::highlightBlock(const QString
//      &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal15HtmlHighlighter14highlightBlockERK7QString(
    qdesigner_internal::HtmlHighlighter *self,
    const QString *text) {
  self->highlightBlock(*text);
}

//  void qdesigner_internal::HtmlHighlighter::highlightBlock(const QString
//      &text)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18qdesigner_internal15HtmlHighlighter14highlightBlockERK7QString(
    qdesigner_internal::HtmlHighlighter *self,
    const QString *text) {
  static_cast<Ownqdesigner_internal_HtmlHighlighter *>(self)->Ownqdesigner_internal_HtmlHighlighter::highlightBlock(
      *text);
}
