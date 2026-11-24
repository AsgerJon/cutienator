//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qtextodfwriter_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(textodfwriter)
#if !defined(QT_NO_TEXTODFWRITER)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtextodfwriter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qtextformat.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qglobal.h>
#ifndef QT_NO_TEXTODFWRITER
#include <QtGui/private/qtextodfwriter_p.h>
#include <QtGui/QImageReader>
#include <QtGui/QImageWriter>
#include <QtGui/QTextListFormat>
#include <QtGui/QTextList>
#include <QtCore/QBuffer>
#include <QtCore/QUrl>
#include <QtCore/QXmlStreamWriter>
#include <QtGui/private/qtextdocument_p.h>
#include <QtGui/qtexttable.h>
#include <QtGui/qtextcursor.h>
#include <QtGui/private/qtextimagehandler_p.h>
#include <QtCore/QDebug>
#include <QtCore/private/qzipwriter_p.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/text/qtextodfwriter.cpp, line 919, as _ZN14QTextOdfWriter12mergeFormatsERK20QTextTableCellFormatRK16QTextTableFormat
#if !defined(QT_NO_TEXTODFWRITER)
inline QTextTableCellFormat QTextOdfWriter::mergeFormats(const QTextTableCellFormat &cell,
                                                  const QTextTableFormat &table)
{
    QTextTableCellFormat ret(cell);
    const auto tryCopyProperties =
            [&](const QVariant &value,
                const std::initializer_list<QTextFormat::Property> &properties) {
        if (value.isNull())
            return;
        for (const auto prop : properties) {
            if (ret.property(prop).isNull())
                ret.setProperty(prop, value);
        }
    };
    const auto &paddingVal = table.property(QTextFormat::TableCellPadding);
    if (!paddingVal.isNull()) {
        // ### Qt7: why is the padding added and not overriden?
        ret.setLeftPadding(ret.leftPadding() + table.cellPadding());
        ret.setRightPadding(ret.rightPadding() + table.cellPadding());
        ret.setTopPadding(ret.topPadding() + table.cellPadding());
        ret.setBottomPadding(ret.bottomPadding() + table.cellPadding());
    }

    tryCopyProperties(table.property(QTextFormat::FrameBorder),
                      { QTextFormat::TableCellTopBorder, QTextFormat::TableCellBottomBorder,
                        QTextFormat::TableCellLeftBorder, QTextFormat::TableCellRightBorder });

    tryCopyProperties(table.property(QTextFormat::FrameBorderBrush),
                     { QTextFormat::TableCellTopBorderBrush, QTextFormat::TableCellBottomBorderBrush,
                       QTextFormat::TableCellLeftBorderBrush, QTextFormat::TableCellRightBorderBrush });

    tryCopyProperties(table.property(QTextFormat::FrameBorderStyle),
                     { QTextFormat::TableCellTopBorderStyle, QTextFormat::TableCellBottomBorderStyle,
                       QTextFormat::TableCellLeftBorderStyle, QTextFormat::TableCellRightBorderStyle });

    return ret;
}
#endif  // !defined(QT_NO_TEXTODFWRITER)
//  -----------------------------------------------------------------------

//  void QTextOdfWriter::setCreateArchive(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QTextOdfWriter16setCreateArchiveEb(
    QTextOdfWriter *self,
    bool on) {
  self->setCreateArchive(on);
}

//  bool QTextOdfWriter::createArchive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QTextOdfWriter13createArchiveEv(
    const QTextOdfWriter *self) {
  return self->createArchive();
}

#if !defined(QT_NO_TEXTODFWRITER)
//  QTextTableCellFormat QTextOdfWriter::mergeFormats(const
//      QTextTableCellFormat &cell, const QTextTableFormat &table)
extern "C" Q_DECL_EXPORT
QTextTableCellFormat *ritual_ZN14QTextOdfWriter12mergeFormatsERK20QTextTableCellFormatRK16QTextTableFormat(
    const QTextTableCellFormat *cell,
    const QTextTableFormat *table) {
  return new QTextTableCellFormat(
      QTextOdfWriter::mergeFormats(
          *cell,
          *table));
}
#endif  // !defined(QT_NO_TEXTODFWRITER)

//  QTextOdfWriter::~QTextOdfWriter()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QTextOdfWriterD1Ev(QTextOdfWriter *self) {
  delete self;
}

#endif  // !defined(QT_NO_TEXTODFWRITER)
#endif  // QT_CONFIG(textodfwriter)
