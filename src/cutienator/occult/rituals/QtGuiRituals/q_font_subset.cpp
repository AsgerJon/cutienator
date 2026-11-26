//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qfontsubset_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qfontsubset_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QList>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/private/qpdf_p.h>
#ifndef QT_NO_PDF
#include "qplatformdefs.h"
#include <QtGui/private/qcmyk_p.h>
#include <QtGui/private/qfont_p.h>
#include <QtGui/private/qmath_p.h>
#include <QtGui/private/qpainter_p.h>
#include <QtCore/qbuffer.h>
#include <QtCore/qcryptographichash.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qdebug.h>
#include <QtCore/qfile.h>
#include <QtGui/qimagewriter.h>
#include <QtCore/qnumeric.h>
#include <QtCore/qtemporaryfile.h>
#include <QtCore/qtimezone.h>
#include <QtCore/quuid.h>
#include <QtCore/qxmlstream.h>
#include <cstdio>
#include <map>
#ifndef QT_NO_COMPRESS
#include <zlib.h>
#endif
#endif
#include <QtGui/private/qfontsubset_p.h>
#include <QtCore/qdebug.h>
#include <QtCore/qendian.h>
#include <QtGui/qpainterpath.h>
#include <QtGui/private/qpdf_p.h>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/gui/text/qfontsubset.cpp, line 22, as local:qfontsubset.cpp:symbol_map
#if !defined(QT_NO_PDF)
static const unsigned short symbol_map[0x100] = {
    0x0000, 0x0001, 0x0002, 0x0003, 0x0004, 0x0005, 0x0006, 0x0007,
    0x0008, 0x0009, 0x000a, 0x000b, 0x000c, 0x000d, 0x000e, 0x000f,
    0x0010, 0x0011, 0x0012, 0x0013, 0x0014, 0x0015, 0x0016, 0x0017,
    0x0018, 0x0019, 0x001a, 0x001b, 0x001c, 0x001d, 0x001e, 0x001f,
    0x0020, 0x0021, 0x2200, 0x0023, 0x2203, 0x0025, 0x0026, 0x220b,
    0x0028, 0x0029, 0x2217, 0x002b, 0x002c, 0x2212, 0x002e, 0x002f,
    0x0030, 0x0031, 0x0032, 0x0033, 0x0034, 0x0035, 0x0036, 0x0037,
    0x0038, 0x0039, 0x003a, 0x003b, 0x003c, 0x003d, 0x003e, 0x003f,

    0x2245, 0x0391, 0x0392, 0x03a7, 0x0394, 0x0395, 0x03a6, 0x0393,
    0x0397, 0x0399, 0x03d1, 0x039a, 0x039b, 0x039c, 0x039d, 0x039f,
    0x03a0, 0x0398, 0x03a1, 0x03a3, 0x03a4, 0x03a5, 0x03c2, 0x03a9,
    0x039e, 0x03a8, 0x0396, 0x005b, 0x2234, 0x005d, 0x22a5, 0x005f,
    0xf8e5, 0x03b1, 0x03b2, 0x03c7, 0x03b4, 0x03b5, 0x03c6, 0x03b3,
    0x03b7, 0x03b9, 0x03d5, 0x03ba, 0x03bb, 0x03bc, 0x03bd, 0x03bf,
    0x03c0, 0x03b8, 0x03c1, 0x03c3, 0x03c4, 0x03c5, 0x03d6, 0x03c9,
    0x03be, 0x03c8, 0x03b6, 0x007b, 0x007c, 0x007d, 0x223c, 0x007f,

    0x0080, 0x0081, 0x0082, 0x0083, 0x0084, 0x0085, 0x0086, 0x0087,
    0x0088, 0x0089, 0x008a, 0x008b, 0x008c, 0x008d, 0x008e, 0x008f,
    0x0090, 0x0091, 0x0092, 0x0093, 0x0094, 0x0095, 0x0096, 0x0097,
    0x0098, 0x0099, 0x009a, 0x009b, 0x009c, 0x009d, 0x009e, 0x009f,
    0x20ac, 0x03d2, 0x2023, 0x2264, 0x2044, 0x221e, 0x0192, 0x2263,
    0x2666, 0x2665, 0x2660, 0x2194, 0x2190, 0x2191, 0x2192, 0x2193,
    0x00b0, 0x00b1, 0x2033, 0x2265, 0x00d7, 0x221d, 0x2202, 0x2022,
    0x00f7, 0x2260, 0x2261, 0x2248, 0x2026, 0xf8e6, 0xf8e7, 0x21b5,

    0x2135, 0x2111, 0x211c, 0x2118, 0x2297, 0x2295, 0x2205, 0x2229,
    0x222a, 0x2283, 0x2287, 0x2284, 0x2282, 0x2286, 0x2208, 0x2209,
    0x2220, 0x2207, 0xf6da, 0xf6d9, 0xf6db, 0x220f, 0x221a, 0x22c5,
    0x00ac, 0x2227, 0x2228, 0x21d4, 0x21d0, 0x21d1, 0x21d2, 0x21d3,
    0x25ca, 0x2329, 0xf8e8, 0xf8e9, 0xf8ea, 0x2211, 0xf8eb, 0xf8ec,
    0xf8ed, 0xf8ee, 0xf8ef, 0xf8f0, 0xf8f1, 0xf8f2, 0xf8f3, 0xf8f4,
    0x0000, 0x232a, 0x222b, 0x2320, 0xf8f5, 0x2321, 0xf8f6, 0xf8f7,
    0xf8f8, 0xf8f9, 0xf8fa, 0xf8fb, 0xf8fc, 0xf8fd, 0xf8fe, 0x0000
};
#endif  // !defined(QT_NO_PDF)

//  from src/gui/text/qfontsubset.cpp, line 139, as local:qfontsubset.cpp:checkRanges
#if !defined(QT_NO_PDF)
static void checkRanges(QPdf::ByteStream &ts, QByteArray &ranges, int &nranges)
{
    if (++nranges > 100) {
        ts << nranges << "beginbfrange\n"
           << ranges << "endbfrange\n";
        ranges = QByteArray();
        nranges = 0;
    }
}
#endif  // !defined(QT_NO_PDF)

//  from src/gui/text/qfontsubset.cpp, line 298, as local:qfontsubset.cpp:qttf_head_table
struct qttf_head_table {
    qint32 font_revision;
    quint16 flags;
    qint64 created;
    qint64 modified;
    qint16 xMin;
    qint16 yMin;
    qint16 xMax;
    qint16 yMax;
    quint16 macStyle;
    qint16 indexToLocFormat;
};

//  from src/gui/text/qfontsubset.cpp, line 313, as local:qfontsubset.cpp:qttf_hhea_table
struct qttf_hhea_table {
    qint16 ascender;
    qint16 descender;
    qint16 lineGap;
    quint16 maxAdvanceWidth;
    qint16 minLeftSideBearing;
    qint16 minRightSideBearing;
    qint16 xMaxExtent;
    quint16 numberOfHMetrics;
};

//  from src/gui/text/qfontsubset.cpp, line 326, as local:qfontsubset.cpp:qttf_maxp_table
struct qttf_maxp_table {
    quint16 numGlyphs;
    quint16 maxPoints;
    quint16 maxContours;
    quint16 maxCompositePoints;
    quint16 maxCompositeContours;
    quint16 maxComponentElements;
    quint16 maxComponentDepth;
};

//  from src/gui/text/qfontsubset.cpp, line 351, as local:qfontsubset.cpp:qttf_font_tables
struct qttf_font_tables
{
    qttf_head_table head;
    qttf_hhea_table hhea;
    qttf_maxp_table maxp;
};

//  from src/gui/painting/qpdf.cpp, line 184, as _ZN4QPdf10ByteStreamC1EP10QByteArrayb
#if !defined(QT_NO_PDF)
namespace QPdf {
using namespace Qt::StringLiterals;
inline ByteStream::ByteStream(QByteArray *byteArray, bool fileBacking)
            : dev(new QBuffer(byteArray)),
            fileBackingEnabled(fileBacking),
            fileBackingActive(false),
            handleDirty(false)
    {
        dev->open(QIODevice::ReadWrite | QIODevice::Append);
    }
}  // namespace QPdf
#endif  // !defined(QT_NO_PDF)

//  from src/gui/painting/qpdf.cpp, line 202, as _ZN4QPdf10ByteStreamD1Ev
#if !defined(QT_NO_PDF)
namespace QPdf {
using namespace Qt::StringLiterals;
inline ByteStream::~ByteStream()
    {
        delete dev;
    }
}  // namespace QPdf
#endif  // !defined(QT_NO_PDF)

//  from src/gui/text/qfontsubset.cpp, line 149, as _ZNK11QFontSubset13getReverseMapEv
#if !defined(QT_NO_PDF)
inline QList<int> QFontSubset::getReverseMap() const
{
    QList<int> reverseMap(0x10000, 0);
    for (uint uc = 0; uc < 0x10000; ++uc) {
        auto idx = glyph_indices.indexOf(fontEngine->glyphIndex(uc));
        if (idx >= 0 && !reverseMap.at(idx))
            reverseMap[idx] = uc;
    }
    return reverseMap;
}
#endif  // !defined(QT_NO_PDF)

//  from src/gui/text/qfontsubset.cpp, line 252, as _ZN11QFontSubset8addGlyphEj
#if !defined(QT_NO_PDF)
inline qsizetype QFontSubset::addGlyph(uint index)
{
    qsizetype idx = glyph_indices.indexOf(index);
    if (idx < 0) {
        idx = glyph_indices.size();
        glyph_indices.append(index);
    }
    return idx;
}
#endif  // !defined(QT_NO_PDF)
//  -----------------------------------------------------------------------

#if !defined(QT_NO_PDF)
//  QFontSubset::QFontSubset(QFontEngine *fe, uint obj_id)
extern "C" Q_DECL_EXPORT
QFontSubset *ritual_ZN11QFontSubsetC1EP11QFontEnginej(
    QFontEngine *fe,
    uint obj_id) {
  return new QFontSubset(fe, obj_id);
}
#endif  // !defined(QT_NO_PDF)

//  QFontSubset::~QFontSubset()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QFontSubsetD1Ev(QFontSubset *self) {
  delete self;
}

#if !defined(QT_NO_PDF)
//  QList<int> QFontSubset::getReverseMap() const
extern "C" Q_DECL_EXPORT
QList<int> *ritual_ZNK11QFontSubset13getReverseMapEv(
    const QFontSubset *self) {
  return new QList<int>(self->getReverseMap());
}
#endif  // !defined(QT_NO_PDF)

#if !defined(QT_NO_PDF)
//  qsizetype QFontSubset::addGlyph(uint index)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN11QFontSubset8addGlyphEj(QFontSubset *self, uint index) {
  return self->addGlyph(index);
}
#endif  // !defined(QT_NO_PDF)

//  qsizetype QFontSubset::nGlyphs() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK11QFontSubset7nGlyphsEv(const QFontSubset *self) {
  return self->nGlyphs();
}

//  a QList<int> a ritual of QFontSubset gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QFontSubset__QList_int(QList<int> *self) {
  delete self;
}
