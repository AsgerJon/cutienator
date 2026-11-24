//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qtextmarkdownwriter_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/qglobal.h>
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if QT_CONFIG(textmarkdownwriter)
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qtextmarkdownwriter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qtextobject.h>
#include <QtCore/qstring.h>

//  bool QTextMarkdownWriter::writeAll(const QTextDocument *document)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QTextMarkdownWriter8writeAllEPK13QTextDocument(
    QTextMarkdownWriter *self,
    const QTextDocument *document) {
  return self->writeAll(document);
}

#if QT_CONFIG(itemmodel)
//  void QTextMarkdownWriter::writeTable(const QAbstractItemModel *table)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTextMarkdownWriter10writeTableEPK18QAbstractItemModel(
    QTextMarkdownWriter *self,
    const QAbstractItemModel *table) {
  self->writeTable(table);
}
#endif  // QT_CONFIG(itemmodel)

//  int QTextMarkdownWriter::writeBlock(const QTextBlock &block, bool table,
//      bool ignoreFormat, bool ignoreEmpty)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QTextMarkdownWriter10writeBlockERK10QTextBlockbbb(
    QTextMarkdownWriter *self,
    const QTextBlock *block,
    bool table,
    bool ignoreFormat,
    bool ignoreEmpty) {
  return self->writeBlock(*block, table, ignoreFormat, ignoreEmpty);
}

//  void QTextMarkdownWriter::writeFrame(const QTextFrame *frame)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTextMarkdownWriter10writeFrameEPK10QTextFrame(
    QTextMarkdownWriter *self,
    const QTextFrame *frame) {
  self->writeFrame(frame);
}

//  void QTextMarkdownWriter::writeFrontMatter(const QString &fm)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTextMarkdownWriter16writeFrontMatterERK7QString(
    QTextMarkdownWriter *self,
    const QString *fm) {
  self->writeFrontMatter(*fm);
}

//  void QTextMarkdownWriter::setLinePrefixForBlockQuote(int level)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTextMarkdownWriter26setLinePrefixForBlockQuoteEi(
    QTextMarkdownWriter *self,
    int level) {
  self->setLinePrefixForBlockQuote(level);
}

//  QTextMarkdownWriter::~QTextMarkdownWriter()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTextMarkdownWriterD1Ev(QTextMarkdownWriter *self) {
  delete self;
}

#endif  // QT_CONFIG(textmarkdownwriter)
